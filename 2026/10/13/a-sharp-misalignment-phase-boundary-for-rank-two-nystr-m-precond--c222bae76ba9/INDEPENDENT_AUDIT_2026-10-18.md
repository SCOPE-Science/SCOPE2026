# Independent mathematical audit

## correctness

PASS

Direct Nyström multiplication gives Ahat=beta*wwT+e3e3T, beta=kappa/(kappa-(kappa-1)t)>1, and P=I+s*wwT with s=(kappa-1)t/((1+eta)*h). The 2x2 generalized eigenvalue polynomial has determinant ab-Sz+(1+s)z² and roots straddling b. Comparing root ratios reduces to S²-H²(1+s)=(s*(kappa-1)/(b*h))*G(t). Independent SymPy expansion returned zero for this polynomial identity, for the displayed G second derivative, and exact rational test P matrix and eigenvalue polynomial. Strict convexity plus endpoint G(0)>0,G(1)<0 yields unique crossing; continuity extends a witness to an open positive Gaussian probability set. Scope: rank-two sketch in dimension three, source-specific normalized preconditioner, exact arithmetic.

## originality

PASS

The original Frangella–Tropp–Udell paper supplies exactly the normalized Nyström operator and expected sufficient-sketch results; its Proposition 5.3 deterministic bound does not decide the sign of conditioning change for a fixed misaligned rank-two sketch. The source and other works on mixed precision and Bregman low-rank preconditioning do not appear to imply G(t) sign or its unique zero. Resultary searches did not surface an equivalent precise claim. Frangella Proposition 5.3 bounds condition number by approximation error, which does not fix the sign relative to unpreconditioned a/b for a specified two-dimensional orientation.

## value

PASS

A randomized preconditioner has probabilistic and approximation-error conditioning guarantees, but a per-realization claim that it always improves over no preconditioner is tempting and false. The sharp orientation transition, minimal-dimension witness and nonzero chance under standard Gaussian sketches provide a concrete motivated instability boundary for the actual normalized Nyström design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
