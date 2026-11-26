# Independent mathematical audit

## correctness

PASS

Reaudited repairs/5/RESULT.md and SLOGAN.txt. The two ordered off-axis pairs yield 4GH in the energy; the two axis convolutions account for every noncentral axis fiber and the origin is counted once. Partitioning the squared-product sum by t+(s−t) gives the nonzero-axis expression N(2λG+G²−R_u)−Δ_u and its vertical analogue. Expansion gives the eight-term identity, checked independently by exact polynomial arithmetic (python3 -B /workspace/review-evidence/rederive.py, section 5). Cauchy–Schwarz in each fiber and at the antipodal products, inversion as a permutation on the punctured axes, and the triangle inequality prove termwise positivity without constraints on group exponent. The two mixed terms are θ_N GH+(2N−4−θ_N)(GH−bc), proving the added stated consequence, including θ_4=4/3. Orthogonality yields L2 source mass M/(2N−1) in squared norm and counting fourth moment N²Q/(2N−1)^4; deficit equality forces GH=0 and the single-axis Fourier transform has single-point support if nonzero. The original three-order ratio 14349/4624 was independently verified exactly, but is not a contribution in the repair. The frozen verify_axes.py was inspected only: checks use floating-point tolerances even on integer inputs and its order-three witness uses 1.186, not the exact frozen 6/5; neither is needed for the general proof.

## originality

PASS

The frozen claim treated the sharp bound and equality geometry as part of the contribution. That part has exact coverage by another theorem including order four, and the order-three failure was already known. The corrected files claim only the exact nonnegative termwise deficit and its separate quantitative information, not novelty of the sharp bound, equality, or order threshold. The two strongest inspected treatments control a centered-moment majorant; neither supplies this decomposition. Even their stated mixed-mass coefficient for N≥5 is smaller than the explicit coefficient here, and the endpoint record does not state this termwise identity at N=4. PASS is limited to the valuable repaired remainder, not the original combined novelty claim.

## value

PASS

The natural sharp deficit now yields separately observable convolution-fiber variance, antipodal-product variance, phase-cancellation and balance information, and a strictly positive explicit mixed-axis product control at order four, uniform over the group type. This can distinguish near-extremizing arrays with the same coarse masses and gives a stronger stated two-axis product bound than the compared higher-axis estimate for N≥5. The repair does not rely for value on a different normalization or a second proof of the known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
