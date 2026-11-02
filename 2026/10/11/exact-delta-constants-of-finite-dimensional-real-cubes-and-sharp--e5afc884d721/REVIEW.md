# Independent mathematical audit

## correctness

PASS

For real X=ell_infinity^n, n>=1, and any x in its closed unit ball, normalize coordinate signs and write a_i=|x_i|, b_i=1-a_i, b*=max b_i. The defining infimum over slices is exactly the largest r with x in conv(E_r(x)); finite-dimensional compactness and strict separation justify both directions even at thresholds. The 2-point midpoint (replace a maximal-escape coordinate by 1 and by 2a_i-1) proves the floor b*. For r>b* all far points lie in opposite-coordinate caps y_i<=a_i-r, active iff r<=1+a_i. Grouping any convex decomposition by a cap forces weights lambda_i <= b_i/(r+b_i), hence Phi>=1. Conversely when Phi>=1, lambda_i=c_i/Phi give explicit cap points with y_i^(j)=a_i-r if i=j and a_i+lambda_i*r/(1-lambda_i) otherwise; they stay inside [-1,1]^n and average to x. When Phi<1 the separating functional sum_i y_i/(r+b_i) over active i has exact gap 1-Phi. The capacity is nonincreasing piecewise rational, giving the complete all-r formula. Equal-coordinate cases n=1 vs n>=2, the root 3r^2-r-2(1-t)=0 on (2/3,2/3,t), and the unit-sphere cap bound Phi(r)<=(n-1)(2-r)/2 for r>1 prove exact values and equality cases n=2, n=3, n>=4. Independent vertex-hull linear-feasibility comparisons across 4080 rational cases of n=1..4 yielded zero mismatches; this numerical check supports examples but is not the infinite-dimensional family proof.

## originality

PASS

Best-of-knowledge originality PASS. Choi–Jung introduce this quantitative Delta constant and prove exact finite-cube values only for n=2, stating n>=3 difficulty. Full readable 2026 Resultary c0 and C(K) all-point results are excluded from finite cubes by infinite-tail/nonisolated-core assumptions; the finite-vs-c0 counterexample is concrete. A nearby positive-square-point cube classification is a different invariant. Actual semantic and web searches found only the audited record as an exact self-match, not independent earlier coverage. Residual priority risks remain explicit.

## value

PASS

The finite real cube is a canonical Banach polytope, and the Delta constant is a natural established quantitative slice-diameter invariant. The defining primary source explicitly says exact n=3 values are difficult, while the current result determines every coordinate point and every dimension, a sharp 3D radial profile, and a global sphere maximum with extremal orbit classification. The cap-budget formula explains a structural finite/infinite boundary rather than merely computing small examples. It is a natural complete quantitative classification, not a textbook renaming, arbitrary slice, or known-table recomputation; no general downstream theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
