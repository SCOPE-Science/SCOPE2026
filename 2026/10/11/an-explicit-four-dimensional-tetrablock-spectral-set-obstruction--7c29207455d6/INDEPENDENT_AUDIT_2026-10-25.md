# Independent mathematical audit

## correctness

PASS

The inspected RESULT.md defines phi=(1+sqrt5)/2 and 4x4 square-zero T_j=phi^-1[[0,A_j],[0,0]] for A_j=E11,E22,J. Direct Git-blob tree reconstruction matches the pinned tree. Mandal–Ray Proposition 2.1 gives cotangent scalar unit ball max(|a|+|b|,|c|)<=1. Extreme-point and singular-value calculation gives norm of u(a,b,c)=phi^-1[[a,c],[c,b]] exactly one. Disk Möbius normalization and Schur complement control every scalar rational f, including constant boundary. The rational F_rho denominator 1-rho²z1z2 is nonzero for rho<1; on the established Shilov boundary z=(omega conjugate q,q,omega), F_rho=(rU+rho omega J)(I+rU* rho omega J)^-1 and has positive contraction defect. At |q|=1 it equals a diagonal unitary, hence exact sup 1. Direct tensor computation gives real symmetric K_rho eigenvalues 1+rho,1-rho,rho,-rho, and ||F_rho(T)||=(1+rho)/phi, so the sharp threshold rho>1/phi is exact. For n=1 a contractive scalar functional on MIN(X) is completely contractive, proving only restricted block-minimality. Independent numerical eigenchecks for multiple rho and broad boundary samples corroborate (but do not prove) the analytic results. The accompanying source verify_tetrablock.py was inspected as a finite arithmetic diagnostic, not accepted as a continuum proof.

## originality

PASS

No independently prior source identified that displays this exact 4x4 centered Parrott tuple and 2x2 rational witness with golden-ratio threshold. However Mandal–Ray already prove the broad failure of rational dilation, the scalar/matricial derivative geometry and the general rational formula used here. Their explicit general interpolant specialized with E11,E22,J immediately supplies the contractivity half; only the chosen norm-one map, its exact amplification, threshold and restricted minimality remain as constructive specific content. This is a qualified narrow originality judgment, not a claim to discovery of failure of rational dilation. Pal’s earlier construction is on infinite-dimensional shifts; Ball–Sau correct a necessary-condition argument; Bhowmik’s 2x2 examples actually dilate. Exact matching Resultary entry is this finding, not independent earlier work.

## value

PASS

The prior nonconstructive MIN != MAX proof only asserts existence of some unspecified finite-dimensional Parrott witness. The fixed 4x4 triple, rational 2x2 certificate, exact (1+rho)/phi amplification and sharp rho threshold provide a small, reproducible benchmark for testing tetrablock rational dilation and identify the first possible equal-block Parrott size. This is a modest but motivated constructive boundary fact; neither a novel general theorem nor a global minimum dimension is claimed. Its value is not attributed to the already known interpolation mechanism or to proof/reproducibility alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
