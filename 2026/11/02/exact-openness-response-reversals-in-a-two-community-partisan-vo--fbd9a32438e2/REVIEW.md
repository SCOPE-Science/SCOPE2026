# Independent mathematical audit

## correctness

PASS

The source mean-field equations yield F1=1/2[(1+h1-2h1 x)((1-g1)x+g1 y)-(1-h1)x] and analogous F2 with h2<0. At any interior stationary point x>y: if x<=y, F1=h1 x(1-x)+A1(Q1-x)/2>0. With J=[[a,b],[c,d]], the row sums are h1(1-x-Q1), h2(1-y-Q2); -J^{-1}F_{g_i} gives exact derivatives and signs. Stable hyperbolic branch requires trace(J)<0,det(J)>0. Rational witness x=9/10,y=3/4,g1=g2=1/4,h1=5/28,h2=-2/19 has F=0, J=[[-109/448,3/28],[5/38,-3/40]], determinant 1413/340480>0, trace -713/2240<0, dP/dg1=688/785>0 and dP/dg2=-1220/471<0. Independently recomputed with exact rational symbolic Jacobian and implicit derivatives. Local undirected-block realization by reducing p11 while preserving symmetric p12=p21 and p22. No global monotonicity implied.

## originality

PASS

Zimmaro–Contucci–Kertész derived the same mean-field system and examined equilibrium polarization/segregation numerically and consensus thresholds, but did not give the asymmetric, separate-openness derivative sign identities or this strict stable rational reversal. Older partisan voter models and algorithmic bias papers have different dynamics or fewer independent exposure controls. Best-of-knowledge novelty is specifically the exact local response theorem, not the ODE or the observation that polarization may vary.

## value

PASS

A motivated exact model-level counterexample to universal monotonic decrease in polarization with openness, with independent community exposure controls, complete local sign criteria and a physically admissible undirected two-block realization. Clarifies the extent of prior numerical segregation intuition; meaningful even without global stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
