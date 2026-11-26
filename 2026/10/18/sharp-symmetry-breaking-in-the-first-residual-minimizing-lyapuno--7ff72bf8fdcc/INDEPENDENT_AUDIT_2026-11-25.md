# Independent mathematical audit

## correctness

PASS

The first-step residual is ww^T with w=(H-pI)(H+pI)^(-1)u, so its Frobenius norm is ||w||^2, not ||w||^4. Orthogonality and equal forcing masses give the sum of two squared Cayley factors, independent of eigenspace multiplicities. On writing x=c^2 in (0,1), z=(p-g)/(p+g) in (-1,1), the derivative with respect to z of the objective divided by sigma^2 is 4z(1-x)[1-3x+x(3-x)z^2]/(1-x z^2)^3. As a function of z^2 it increases from zero coordinate when x<=1/3 (the derivative vanishes at the endpoint only at equality); above this it first decreases and then increases, with its unique turning point at (3x-1)/(x(3-x)) strictly in (0,1) since x^2<1. This gives precisely the two shifts with product ab and a strict local maximum at g. The critical x is equivalent to kappa=(2+sqrt(3))^2. Substitution gives the stated minimum; differentiating 8x^2/(6x-x^2-1) gives a positive derivative for x>1/3, and the limit 2 at x=1 is unattained. The worst-factor minimax solution instead balances the opposite signed spectral factors for a<=p<=b; no shift outside that interval improves it. In the independent bounded check (`python3 /workspace/branches/independent_checks.py 4`, SymPy), differentiating the two Cayley terms symbolically reproduced the full derivative, the kappa=49 witness 527/576, and the critical quartic coefficient 16/27. The proof, not any finite shift grid, establishes the global classification. Scope: real first shift, zero starting approximation, SPD two-mode operator and balanced rank-one forcing.

## originality

PASS

The residual factor and general data-dependent objective, including the possibility of multiple local minima, are established. The distinct claim supported here is the explicit balanced two-mode global bifurcation, reciprocal minimizers and sharp first-step loss; the strongest examined formulation poses the objective but does not solve that special case. No claim of bibliographic priority beyond these comparisons.

## value

PASS

This exact case uses a standard physically realizable rank-one forcing model, rather than an arbitrary matrix entry. A practitioner choosing between spectral minimax and residual-aware shifts needs to know that the minimax shift can be a strict local maximum, with a nearly twofold penalty in the norm being optimized. The threshold, explicit replacement shifts and worst-case limit give a useful analytic benchmark, without implying anything about later iterations or unbalanced data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
