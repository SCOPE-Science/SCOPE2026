# Independent mathematical audit

## correctness

PASS

Expand finite difference to residual scalar b·w+(τ/2)||u||² and use Gaussian parity, E[(b·w)²||u||²]=(d+2)||b||² and sixth chi-square moment j(j+2)(j+4). Components A=E||Px||² and B=E||(I−P)x||² satisfy F: B_next=rB+α²qC_d, A_next=sA+α²k(B+C_d); R: B_next=rB+α²qC_q, A_next=sA, r=1−2α+(q+2)α²,s=(1−α)²,C_j=τ²(j+2)(j+4)/4. At r≥1 positive forcing diverges; at r<1 both affine recurrences contract and fixed points give the two displayed F,R formulas. Independently integrated exact Wick moment polynomials for d=2,k=1 with rational parameters, matching one-step recurrences. Since C_d>C_q, full floor greater; fixed q,α<2/(q+2) gives cubic ambient growth. This is for exact oracles and quadratic only, not general nonconvex convergence.

## originality

PASS

Original full-space estimator and upper cubic noise bound are in Ryabchenko–Qian–Mou; standard residual q+2 contraction and partial-gradient concept in Chayti–Mirrokni–Jaggi. The joint exact stationary finite-radius floors and equal-evaluation complement-probe comparison were not identified in accessible primary statements; limited full-text access remains significant risk. Best-of-knowledge qualified PASS.

## value

PASS

A natural quantitative comparison between oracle-hint Gaussian finite differences, isolating avoidable Θ(d³) noise from probing known directions with explicit sharp stability window and stationary second moments. Narrow but directly motivated algorithm design fact; probe expected energies differ at fixed coordinate τ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
