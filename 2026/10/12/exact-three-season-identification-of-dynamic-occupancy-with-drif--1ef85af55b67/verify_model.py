"""Exact-arithmetic checks for three-season occupancy identifiability.

Run: python3 verify_model.py (standard library only).
The enumeration is finite; unrestricted identifiability follows from the proof.
"""
from fractions import Fraction as F
from itertools import product


def history_law(params):
    """All detection-history probabilities, by summing over hidden paths."""
    initial, colonize, persist, detection = params
    length = len(detection)
    law = {y: F(0) for y in product((0, 1), repeat=length)}
    for z in product((0, 1), repeat=length):
        weight = initial if z[0] else 1-initial
        for a, b in zip(z, z[1:]):
            forward = persist if a else colonize
            weight *= forward if b else 1-forward
        for y in law:
            q = weight
            for state, observation, prob in zip(z, y, detection):
                if state:
                    q *= prob if observation else 1-prob
                elif observation:
                    q = F(0)
                    break
            law[y] += q
    assert sum(law.values()) == 1
    return law


def hit(law, indices):
    return sum((v for y,v in law.items() if all(y[i-1] for i in indices)), F(0))


def reconstruct_three(law):
    assert len(next(iter(law))) == 3
    means = [None]+[hit(law,(t,)) for t in (1,2,3)]
    r2 = hit(law,(1,2))/means[1]
    r3 = hit(law,(2,3))/means[2]
    h2 = means[2]/r2
    h3 = means[3]/r3
    T = hit(law,(1,3))/(means[1]*r3)
    assert h2 != 1
    delta = (T-h3)/(1-h2)
    assert delta != 0
    b = T-delta
    persist = delta/(1-b)
    colonize = b*persist
    initial = (persist*h2-colonize)/delta
    p1 = means[1]/initial
    p2 = r2/persist
    p3 = r3/persist
    return initial, colonize, persist, (p1,p2,p3)


# A distinct two-season alias in the nonsingular, strictly interior model.
A=(F(2,5),F(2,5),F(3,5),(F(1,5),F(1,5)))
B=(F(3,10),F(3,7),F(3,5),(F(4,15),F(1,5)))
assert A!=B
assert history_law(A)==history_law(B)

# Exact reconstruction at points with positive/negative persistence-minus-
# colonization and stationary/nonstationary initial occupancy.
V=[F(k,6) for k in range(1,6)]
n=0
stationary=0
for initial, colonize, persist, p in product(V,repeat=4):
    if colonize == persist:
        continue
    params=(initial,colonize,persist,(p,p,p))
    law=history_law(params)
    assert reconstruct_three(law)==params
    n+=1
    if initial==colonize/(1-persist+colonize):
        stationary+=1

# Allow all three detection probabilities to differ, independently.
variations=0
for initial, colonize, persist in product([F(1,4),F(1,2),F(3,4)],repeat=3):
    if colonize==persist:
        continue
    for ps in ((F(1,5),F(2,5),F(4,5)),
               (F(4,5),F(1,5),F(3,5)),
               (F(3,5),F(3,5),F(1,5))):
        params=(initial,colonize,persist,ps)
        assert reconstruct_three(history_law(params))==params
        variations+=1

# When persistence=colonization, each observed season is independent;
# infinitely many interior parameter sets yield exactly the same history law.
C=(F(2,5),F(1,2),F(1,2),(F(1,5),F(2,5),F(3,5)))
D=(F(1,2),F(3,5),F(3,5),(F(4,25),F(1,3),F(1,2)))
assert C!=D and history_law(C)==history_law(D)
print('VERIFY_OK two_season_alias=1 singular_three_season_alias=1 '
      f'nondegenerate_exact_reconstructions={n+variations} '
      f'varying_detection={variations} stationary_hidden={stationary}')
