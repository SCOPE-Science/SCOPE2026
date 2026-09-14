"""Recovery test: robust region of Einstein algebraic tensors with sec>0 but 3-sum<=0."""
import numpy as np
rng = np.random.default_rng(1)

def random_traceless_triplet(scale):
    # random point on plane sum=0 with bounded norm
    v = rng.normal(size=3)
    v = v - v.mean()
    n = np.linalg.norm(v)
    if n == 0:
        return v
    # random radius
    r = rng.uniform(0, scale)
    return v / n * r

N = 200000
count_sec_pos = 0
count_both = 0  # sec>0 and 3-sum<=0
for _ in range(N):
    wa = random_traceless_triplet(1.5)
    wb = random_traceless_triplet(1.5)
    a = wa + 1/3
    b = wb + 1/3
    a1b1 = a.min() + b.min()
    if a1b1 > 0:
        count_sec_pos += 1
        c = np.sort(np.concatenate([a, b]))
        if c[0]+c[1]+c[2] <= 0:
            count_both += 1
print(f"sec>0 count: {count_sec_pos}/{N}")
print(f"sec>0 but 3-sum<=0: {count_both}/{N} = {count_both/max(1,count_sec_pos):.4f} of sec>0")
# explicit family interpolation: t from CP2-like to counterexample
print("interpolation check:")
a0 = np.array([1.0, 0.0, 0.0])
b0 = np.array([1/3, 1/3, 1/3])
a1 = np.array([-0.2, -0.1, 1.3])
b1 = np.array([0.25, 0.3, 0.45])
for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
    a = (1-t)*a0 + t*a1
    b = (1-t)*b0 + t*b1
    # fix traces (both already sum 1, convex combo sums 1)
    c = np.sort(np.concatenate([a, b]))
    print(f"t={t}: sec_proxy={(a.min()+b.min())/2:.4f} sum3={c[:3].sum():.4f}")
print("RECOVERY TEST DONE")
