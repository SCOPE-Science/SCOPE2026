# Independent mathematical audit

## correctness

PASS

For the counting-mass Petersen graph KG(5,2), M is a pointwise maximum of three nonnegative ball averaging matrices. Thus ||M||_2^2=max over 3^10=59049 radius assignments of lambda_max(A_rho^T A_rho). I independently constructed all 120 S5 automorphisms and 792 selection orbits; computed eigenvalues and exact integer Sylvester/Bareiss positive-definite certificates for 791 nonwinning orbit representatives for 2964I-5(20A)^T(20A)>0. The sole winning orbit has 20 assignments and top squared norm 1.4841784035296353; next largest orbit max 1.4794072003558165<1.482. Independent symbolic 3x3 compressed eigenvalue calculation yields exactly (200 lambda^3-355 lambda^2+87lambda-1)/200, with positive Perron eigenvector H=1,T=(49lambda-1)/D,S=(24lambda+3)/D and l2 norm 1.21826860894042. Read source petersen_verifier.py; its exact rational activation inequalities ensure all winning prescribed radii strictly active, and distinct ordered pairs give 20 rays. Finite enumeration is genuinely exhaustive here because there are exactly 59049 cases and orbit partition was checked.

## originality

PASS

Soria-Tradacete founded maximal norms on finite graphs, González-Riquelme/Madrid establish sharp values for complete graphs and stars, and Greenblatt 2016 thesis treats spherical maximal operators on CARTESIAN POWERS of Petersen. The inspected full thesis subsection 1.4 addresses asymptotics for powers, not this one-graph ball maximal l2 cubic/equality classification. The exact coefficient polynomial and twenty-rigid rays are not inferred from the published generic finite-graph reduction. Unindexed prior equality computations remain a real priority risk.

## value

PASS

The Petersen graph is a standard small vertex-transitive cubic graph, and the complete strong l2 norm plus all equality cases is a natural exact benchmark for nonlinear graph maximal operators. Exhaustive finite certification is the appropriate complete proof for this fixed graph, and the rigidity pattern is independently meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
