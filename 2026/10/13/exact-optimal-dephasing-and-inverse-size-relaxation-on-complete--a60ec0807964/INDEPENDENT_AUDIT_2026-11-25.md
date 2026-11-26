# Independent mathematical audit

## correctness

PASS

For n≥3 the off-diagonal matrix space has independent row and column sum constraints except for their shared total: a linear dependence would require u_i+v_j=0 for all i≠j, forcing constant u_i and opposite constant v_j. The common kernel W therefore has dimension n²−3n+1. The scalar I and J−I, W, and the three zero-sum vector families D_x,P_x,Q_x form the claimed direct sum (their diagonal and row/column sums separate them). The commutator and dissipator give L(D_x)=igQ_x, L(P_x)=2γD_x−γP_x+ingQ_x and L(Q_x)=ingP_x−γQ_x. Thus the cubic has multiplicity n−1 and the −γ sector dimension (n−1)(n−2), leaving a simple zero with I/n stationary. Setting z=−γw gives F(w)=α². On (0,h), F increases from zero to infinity since F′ has the sign of (1−w)(h−3hw+2w²) and h−3hw+2w²≥h−9h²/8>0. For the residual quadratic, its value and derivative at −w are positive (the derivative is 2−3w), placing both real roots to the left; a nonreal pair has real part −1+w/2<−w. The −γ modes are faster too. The slow eigenvalue is simple per block and has full multiplicity n−1. Eliminating γ yields Δ=n|g|√[w(h−w)]/(1−w), whose logarithmic derivative changes sign at w=h/(2−h); substitution gives both quoted optima. Weak and strong limits follow from w→h and F(w)∼w/h, respectively. At fixed g,γ, 1−w/h≤1/α² proves the large-n equivalent. For P_j−I/n=D_x the contrast reads a+2b in the block; the Laplace system gives the stated numerator. At the simple slow pole this numerator and the derivative of the cubic denominator are both positive, proving nonzero positive residue and the localized TV asymptotic. Independently assembled zI−L from matrix units modulo 101 with i mapped to 10, then used Gaussian elimination for n=3,…,6 and (g,γ)=(−2,3),(1,8),(5,2). All 270 determinant evaluations at z=0,…,n² agreed; at the 255 invertible cases, every diagonal resolvent component for P_1−I/n also agreed. These are bounded modular checks, not real-spectrum certification. Frozen VERIFICATION.md and verify.py were inspected, not executed.

## originality

PASS

Pass for the full characteristic polynomial with multiplicities, proof of the all-rate dominant gap and exact spectral-gap optimization. The same dissipator and network are known. An indexed universal-vertex result also contains the complete-graph scalar transform, including its cubic, by direct specialization; it is material overlap, not the basis for distinctness here.

## value

PASS

The gap measures intrinsic long-time relaxation in this standard position-dephased generator. Its exact optimum and the contrasting fixed-noise and optimally retuned size laws quantify a choice unavailable from a qualitative noise-assisted-mixing claim. The full spectral argument shows that the localized return does not miss a slower sector. It neither asserts finite-time optimality nor relies on optimizing a different return or transfer metric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
