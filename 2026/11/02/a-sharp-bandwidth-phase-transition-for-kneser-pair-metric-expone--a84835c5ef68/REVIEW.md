# Independent mathematical audit

## correctness

PASS

Full incidence matrix B gives BB^T=(n-2)I+J and adjacency A=J+I-B^TB; orthogonal eigenspaces 1,U,W of dimensions 1,n-1,N-n and adjacency eigenvalues binom(n-2,2), -(n-3),1. With x=2^p kernel K=(1-e^-xt)I+(e^-t-e^-xt)A+e^-xt J, eigenvalues constant positive, W=1+e^-t-2e^-xt>0, U=F=1-(n-3)e^-t+(n-4)e^-xt. Differentiation F_t=e^-t[(n-3)-(n-4)x e^{-(x-1)t}] gives all-positive for x<=(n-3)/(n-4), otherwise unique positive zero t_c with n-1 negative eigenvalues below. Root monotone in x and tends log(n-3). At x=1+c/(n-4), root satisfies e^t=1+(n-4)(1-e^{-ct/(n-4)}), monotone n, converges unique positive T solving e^T=1+cT, expansion from Taylor gives stated 1/(n-4) correction. Independent full K matrix tests for n=5,6,9, several powers/bandwidths reproduced 1/U/W eigenvalues; checker full text inspected and finite cases cannot replace proof.

## originality

PASS

Complete Johnson/Kneser distance spectra and Schoenberg all-scale criterion are classical. The additional scale-resolved t_c, exact inertia and fixed-c n-asymptotic correction were not found as statements in consulted prior Kneser spectrum/theory sources; best-of-knowledge qualified because formulas follow by elementary scalar calculus from known eigenspaces.

## value

PASS

Finite-bandwidth positive definiteness matters for kernel regression beyond all-scales negative type; a natural full n,p,t classification identifies a nonzero finite-size crossover not captured by all-scale positivity criterion. Exact n-1-dimensional signature matters to Gram computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
