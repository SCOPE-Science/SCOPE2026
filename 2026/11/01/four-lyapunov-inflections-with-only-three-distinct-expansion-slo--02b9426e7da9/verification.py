"""Recompute interval enclosures for a four-branch Lyapunov-curvature witness."""
from mpmath import iv
iv.dps = 75
levels = (0, 1, 360)
counts = (1, 2, 1)
beta = iv.mpf(1) / 16
samples = ((-2, -1), ('-0.7',1), ('-0.2',-1), ('-0.03',1), ('0.02',-1))
for raw, expected in samples:
    w = iv.mpf(raw)
    weights = [n*iv.exp(w*k) for n,k in zip(counts,levels)]
    total = sum(weights)
    mean = sum(k*v for k,v in zip(levels,weights))/total
    variance = sum(k*k*v for k,v in zip(levels,weights))/total - mean*mean
    curvature = 2*(beta*w + iv.ln(total))*variance - (beta + mean)**2
    a,b = [float(s) for s in (curvature.a, curvature.b)]
    assert a*expected > 0 and b*expected > 0, (raw,a,b)
    print(raw, f'[{a:.12g}, {b:.12g}]', 'PASS')
print('ALL FIVE STRICT SIGNS CERTIFIED')
