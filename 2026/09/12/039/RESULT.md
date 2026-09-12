# Disproof of the genus-3 two-node biextension-determinant target: monodromy half true, determinant zero via e1+e2=0

## Context

The admitted target concerns the hyperelliptic family Ct: y^2=x(x-t)(x-1)(x-1-t)(x-2)(x-3)(x-4) over 0<|t|<delta, its two commuting Picard-Lefschetz twists, the monodromy logarithm N, the weight filtration W=W(N)[1], and the 2x2 biextension period matrix of the limit mixed Hodge structure. The target conjunction asserts rank N=2, N^2=0, graded dimensions (2,2,2), disjoint vanishing cycles, and nonzero biextension determinant (both extensions nonsplit over Q). This record decides the full conjunction on its own terms.

## Definitions

Ct is the smooth projective hyperelliptic model of the affine equation above (degree 7, hence 8 branch points counting infinity, genus 3). T=T1*T2 is total monodromy, N=log T, Wi the monodromy weight filtration shifted for weight 1. E is the normalization Y^2=X^3-X (X=x-3, Y=u) with K=Q(s), s^2=-6. P1^pm=(-3,pm 2s), P2^pm=(-2,pm s), T_=(-1,0). Extension classes ei=AJ(Pi^+)-AJ(Pi^-) in Jac(E), with AJ taken from O=infinity.

## Result

The monodromy and weight clauses hold: T1,T2 are commuting symplectic transvections, N=N1+N2 has rank 2 with N^2=0, W0=Im N, W1=ker N gives graded dimensions dim Gr^W_0=2, dim Gr^W_1=2, dim Gr^W_2=2 with Gr^W_1 canonically H^1(E), and the vanishing cycles are disjoint with zero intersection pairing. The final clause is false: e1+e2=0 in Jac(E), so every 2x2 biextension period matrix or determinant formed from (e1,e2) vanishes. The common value e=e1=-e2=(-25/24,35s/288) has infinite order, so each single-node extension is individually nonsplit over Q while the pair is Q-linearly dependent. Hence the target conjunction is rigorously disproved.

## Proof and evidence

Smoothness and genus: for 0<|t|<1/2 the seven roots 0,t,1,1+t,2,3,4 are distinct, so ft is separable of degree 7 and Ct is smooth of genus 3. At t=0, f0=x^2(x-1)^2(x-2)(x-3)(x-4) has ordinary double points at x=0 (tangent cone y^2+24x^2, c0=-24) and x=1 (y^2+6(x-1)^2, c1=-6) and no other singularities; C0 is irreducible of arithmetic genus 3 and geometric genus 1. Normalization nu:(x,u)->(x,x(x-1)u) maps E: u^2=(x-2)(x-3)(x-4), i.e. Y^2=X^3-X, onto C0, identifying the two preimages over each node. Monodromy: the coalescing branch pairs {0,t},{1,1+t} give disjoint vanishing cycles delta1,delta2 with <delta1,delta2>=0, hence commuting transvections Ti(v)=v+<v,deltai>deltai, N=N1+N2, N^2=0 by vanishing of all <deltai,deltaj>, and in a symplectic basis with delta1=a1,delta2=a2 one gets N(b1)=-a1,N(b2)=-a2, rank 2, dim ker N=4, Gr dims (2,2,2); verified exactly as integer 6x6 matrices. Biextension relation: since (Pi^+)+(Pi^-)-2O=div(x-ci), ei=2AJ(Pi^+). The line L: Y+sX+s=0 passes through P1^+,P2^+,T_, with exact identity (-sX-s)^2-(X^3-X)=-(X+1)(X+2)(X+3)+(X+1)^2(s^2+6), so over K the divisor P1^++P2^++T_-3O is principal; T_ is 2-torsion, hence doubling gives e1+e2=-2AJ(T_)=0. Infinite order: duplication x(2P)=(x^2+1)^2/(4(x^3-x)) gives x(2P1^+)=x(2P2^+)=-25/24 and e=(-25/24,35s/288) lies on E(K), not 2-torsion. E has good reduction at 5 and 3; at p5=(5,s-2) e reduces to (0,0) of order 2, so 2 divides the order; at p3=(3,s) e lies in the pro-3 kernel of reduction, which contains no element of order 2 since reduction is injective on prime-to-3 torsion -- contradiction if e were torsion. Hence e has infinite order. Confirmatory 50-digit mpmath quadrature gives periods with tau=i and z1+z2=-Omega_B mod lattice with residual below 1e-29, matching e1+e2=0; it is not needed for the exact disproof.

## Limitations

Scope is the named family only; no claim about generic two-node genus-3 degenerations. The disproof uses the standard Clemens-Schmid identification of Gr^W_1 with H^1 of the normalization and the Abel-Jacobi description of node extension classes. The SL2-orbit numerics are confirmatory only.

## Reproducibility

Exact integer, Fraction, and sympy checks in output/artifacts/exact_checks.py reproduce the collinearity identity, point memberships, duplication values, reduction images, monodromy rank, and tangent-cone constants; run `python3 output/artifacts/exact_checks.py` (all checks pass). Numerical cross-check via output/artifacts/numeric_asymptotics.py with mpmath at 50 digits.

## References

P. Deligne, Theorie de Hodge II-III; W. Schmid, Variation of Hodge structure: singularities of the period mapping; J. Steenbrink, Limits of Hodge structures; R. Hain, D. Matsumoto, Universal mixed elliptic motives; P. Brosnan and G. Pearlstein, zero loci and heights of Ceresa cycles; S. Goswami and I. Spelta, Genus three Ceresa cycles and limit of archimedean heights, arXiv:2604.01842; J. Silverman, Advanced Topics in the Arithmetic of Elliptic Curves (formal groups, reduction); LMFDB entry for y^2=x^3-x (CM curve j=1728).
