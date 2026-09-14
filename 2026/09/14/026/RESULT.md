# Finitistic dimension of the C2-trivial two-orbit EI algebra in characteristic 2

## Context
Finitistic dimensions measure the complexity of modules of finite projective
dimension. For EI-category algebras, Luck proved finiteness with the upper
bound Fin.dim(kC) <= l(C), the maximal chain length of non-isomorphisms, and
Dietrich recast this via directed stratifications: a two-stratum algebra
satisfies fin.dim A <= fin.dim eAe + fin.dim fAf + 1. These bounds do not give
exact values. The admitted target asks for the exact finitistic dimension of
one named dividing-characteristic example beyond that bound.

## Definitions
Let C2 be the connected skeletal finite EI-category with objects {x,y},
Aut(x) = C2 = {1,g}, Aut(y) = 1, C(x,y) = M a 3-point (1,C2)-biset with
exactly two orbits (one free 2-point orbit and one fixed point), C(y,x) empty.
Let k be a field of characteristic 2 and A2 = kC2 its category algebra.
Write B = e_x A2 e_x ~= kC2 ~= k[u]/(u^2) with u = 1+g, and
M = e_y A2 e_x, dim_k M = 3. Then A2 is the upper-triangular matrix algebra
[[k, M],[0, B]], of dimension 6. Left modules are triples (V, W, phi) with V
a k-space, W a B-module, phi: M tensor_B W -> V; right modules are triples
(V, W, psi) with psi: V tensor_k M -> W_B. Indecomposable left projectives:
P_y = (k,0,0) (dim 1), P_x = (M,B,id) (dim 5). Right projectives:
Q_y = (k,M,id) (dim 4), Q_x = (0,B,0) (dim 2).

## Result
Over any field k of characteristic 2 (algebraic closure not needed):
findim(A2) = 1 on both left and right, while gl.dim(A2) = infinity.

## Proof / evidence
Right B-structure of M: with u = 1+g, f.u = f+fl, fl.u = f+fl, z.u = 0, so
M_B ~= B (+) k (free-orbit span{f,fl} is free of rank 1, fixed-point span{z}
is trivial); u_M^2 = 0, rank 1, nullity 2. Since B is self-injective,
findim(B) = 0.

Infinite global dimension: over B = k[u]/(u^2) the trivial module k has the
periodic minimal resolution ... -> B ->[u] B ->[u] B -> k -> 0 with
im(u) = ker(u) = span{u}, non-split, so pd_B(k) = infinity. The exact
restriction functor e_x(-) sends projectives to projectives, hence
pd_B(e_x N) <= pd_{A2}(N). The module N_inf = (0,k,0) restricts to k, so
pd_{A2}(N_inf) = infinity.

Lower bound: the left module N0 = (0,B,0) has minimal resolution
0 -> P_y^3 -> P_x -> N0 -> 0 (kernel computed vertex-wise: y-part M ~= k^3,
x-part 0; dimensions 5 = 3 + 2; image inside the radical). An exhaustive
GF(2) search over all 16 k-linear h: B -> B shows the only arrow-compatible
map is h = 0, so the cover P_x -> N0 has no section; N0 is not projective
and pd(N0) = 1 exactly. The right module Nbar = (k,k,psibar) with
psibar(f) = psibar(fl) = 0, psibar(z) = 1 has 0 -> Q_x -> Q_y -> Nbar -> 0
with kernel span{f,fl} ~= B, exact, minimal, non-split, so right pd = 1.

Upper bound: for N = (V,W,phi) of finite projective dimension, restriction to
x gives pd_B(W) < infinity, so W is free. The counit P_x^r = A2 e_x tensor_B W
-> N is an isomorphism at x; kernels and cokernels of x-isomorphisms are
y-supported, hence projective. Minimal-resolution analysis at x forces the
second syzygy term to be y-supported projective, so Omega^1(N) is
projective and pd(N) <= 1. Equivalently this is Dietrich's directed-
stratification bound 0 + 0 + 1. The right side is mirrored.

Machine certificates verify_findim.py and verify_right.py (GF(2) linear
algebra) confirm B-periodicity, the M_B decomposition, exactness, the
16-case no-section result, and the dimension census; both pass.

## Limitations
The upper-bound diagram chase is prose plus the general stratification
theorem rather than machine-checked; scripts certify all non-formal inputs.
Proved in characteristic 2 only; the dividing (non-semisimple B) hypothesis
is essential. No claim of a general criterion or completed census of EI
finitistic dimensions is made.

## Reproducibility
Run `python3 output/artifacts/verify_findim.py` and
`python3 output/artifacts/verify_right.py`; both must print ALL CHECKS PASSED.

## References
- W. Luck, Transformation Groups and Algebraic K-Theory, LNM 1408 (1989).
- K. Dietrich, An upper bound for the finitistic dimension of an EI category
  algebra, arXiv:0907.2141 (2009).
- K. Dietrich, The finitistic dimension of algebras with a directed
  stratification, arXiv:1102.2577 (2011).
