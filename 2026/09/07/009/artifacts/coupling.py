"""Monotone coalescing coupling simulation for canonical P* from worst pair (0,7)."""
import random, statistics, math
random.seed(20260907)

def step(i,u):
    if i==0:
        return 0 if u<0.75 else 1
    elif i==7:
        return 6 if u<0.25 else 7
    else:
        return i-1 if u<0.75 else i+1

def one_run(rng):
    x,y=0,7
    t=0
    while x!=y:
        u=rng.random()
        x=step(x,u); y=step(y,u)
        t+=1
        if t>10**7:
            break
    return t

rng=random.Random(20260907)
N=20000
taus=[one_run(rng) for _ in range(N)]
taus_sorted=sorted(taus)
mean=sum(taus)/N
print(f"N={N} mean={mean:.2f} min={min(taus)} max={max(taus)}")
print(f"median={taus_sorted[N//2]} q75={taus_sorted[int(0.75*N)]} q95={taus_sorted[int(0.95*N)]} q99={taus_sorted[int(0.99*N)]}")
# empirical tail: P(tau>t)<=1/4 threshold
for t in [10,20,30,40,50,60,80,100]:
    tail=sum(1 for v in taus if v>t)/N
    print(f"P(tau>{t})~{tail:.4f}")
# Markov-based certified-from-mean upper: t_mix(1/4)<=4*E[tau] (via max E). Using empirical mean + Hoeffding-style note.
print(f"4*mean={4*mean:.1f}")
# sd
import statistics as st
print(f"sd={st.pstdev(taus):.2f}")
