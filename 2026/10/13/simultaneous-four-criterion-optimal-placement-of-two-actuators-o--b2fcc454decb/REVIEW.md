# Independent mathematical audit

## correctness

PASS

PASS: For n>=3, A=rS (0<r<1) with S the directed cyclic coordinate permutation and independent unit coordinate inputs at two distinct positions, W_H is diagonal for full-cycle H=mn or infinity. Relabeling gaps a<=b, a+b=n, t=r² gives entries F_H(1+t^b)t^j (j=0..a−1) and F_H(1+t^a)t^j (j=0..b−1), where F_H is the positive geometric full-cycle factor. Therefore λmin=F_H t^{b−1}(1+t^a), λmax=F_H(1+t^a), κ=t^{−(b−1)}, determinant and reciprocal trace as in RESULT.md. As a grows to n/2, λmin strictly rises and κ strictly falls. For determinant, log det differs from a constant by ab[f(a)+f(b)] with f(x)=log cosh(cx)/x=∫_0^c tanh(sx) ds, strictly increasing and concave; its sum and ab both rise toward equality. For inverse trace, h(x)=(1+e^{yx})^-1 is strictly convex x>0, so h(a)+h(b) decreases toward equal gaps. Thus exactly balanced gaps optimize all four criteria, strictly versus unbalanced, for every full-cycle horizon and infinity; Gramian trace is position-independent. My independent exact rational direct time-sum computation for n=3..10, t=1/4 or 4/9 and horizons n and 2n reproduced the formulas and all strict comparisons. Other horizons and actuator weights are excluded.

## originality

PASS

PASS best-of-knowledge: General actuator selection, Gramian trace modularity, log-det or inverse-trace submodularity and qualitative leader spreading on directed rings predate the claim. Enyioha et al (2014) studies the minimum eigenvalue / fraction of leaders on large directed rings and advocates distributed leaders; the full inspected article does not supply a finite two-actuator equality case for all four metrics with explicit eigenvalue/determinant/inverse-trace/condition formulas. Cortesi–Summers–Lygeros (2014) gives general submodular metric algorithms, not closed exact equal-gap rigidity in this restricted family. A possible exact specialization in older leader-placement literature remains a stated risk.

## value

PASS

PASS: With two separately driven coordinate nodes on a stable one-way cycle, balancing gaps being jointly and strictly optimal across four ordinarily conflicting controllability criteria is a natural, nontrivial structural optimizer classification. Explicit all-horizon formulas and the distinction between invariant Gramian trace and optimized minimum eigenvalue, determinant, inverse trace and condition number clarify actuator placement geometry. The result intentionally does not generalize to arbitrary horizons or weighted channels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
