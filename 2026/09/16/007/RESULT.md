# No universal fixed-patch cut-and-glue filter for homogeneous D=2 PEPS

## Context

The admitted target asked for a fixed patch size L (independent of system size n) and a fixed non-zero
LxL-local operator C (independent of the PEPS tensor A and of n), built from tensor-polynomial identities
of the boundary algebra, that projects every 2D square-torus homogeneous PEPS of bond dimension at most 2
(local dimension d=2) onto a pure patch state, keeps the complement in homogeneous-PEPS form, and thereby
drives a finite-size SDP monogamy trade-off witnessing a D=2 vs D=3 gap. An impossibility proof for all
fixed L was admitted as a complete resolution.

## Definitions

Work on the square torus with n=N^2 sites, N>L, local dimension d=2, bond dimension D=2. Let R be an
LxL patch with m=L^2 sites and E its complement (n-m>=1 sites). A fixed linear map
C:(C^2)^{⊗m}->H' acts on the physical legs of R only. Filter success on |psi> means
(C_R⊗I_E)|psi> is non-zero and product across R|E, i.e. the patch marginal is pure.
Product family (bond dimension 1): A_v(p;l,r,u,d)=v_p δ_{l0}δ_{r0}δ_{u0}δ_{d0}, giving |v>^{⊗n}.
Cat family (bond dimension 2): A(p;l,r,u,d)=(v_1)_p δ_{l0}δ_{r0}δ_{u0}δ_{d0}+(v_2)_p δ_{l1}δ_{r1}δ_{u1}δ_{d1},
giving |v_1>^{⊗n}+|v_2>^{⊗n} on the connected torus (only all-0 and all-1 bond configurations survive).

## Result

Theorem: for every fixed m=L^2>=1 and every fixed non-zero linear C independent of A and n, there are a
torus size n>m and homogeneous D<=2 PEPS on which the universal demand fails: either some product
|v>^{⊗n} is annihilated, (C⊗I)|v>^{⊗n}=0 (zero post-selection probability), or some cat filters to a
non-product vector with mixed patch marginal. Hence no fixed (L,C) projects every D<=2 homogeneous PEPS
patch onto a pure state, and the target SDP trade-off via such a universal C is impossible through this
route for all fixed L.

## Proof / evidence

Success on all products forces C|v>^{⊗m}≠0 for all v≠0. For independent v_1,v_2 (and m,n-m>=1, so both
patch and complement tensor powers are independent by Gram determinant 1-|<v_1|v_2>|^{2k}>0), the
cut-purity lemma says the filtered cat is product iff C|v_1>^{⊗m}∥C|v_2>^{⊗m}: with independent
|b_1>,|b_2>, |a_1>|b_1>+|a_2>|b_2> is zero iff a_1=a_2=0 and otherwise product iff a_1∥a_2 (duals
φ_k with φ_k(b_j)=δ_{kj} extract a_k=φ_k(y)|x>). So success on all cats forces pairwise collinearity.
Jointly, all c(v)=C|v>^{⊗m} lie on one ray; since symmetric products span Sym^m(C^2),
rank(C|_{Sym^m})=1, i.e. C|_{Sym}=|w><u| with u≠0. Then f(v)=<u|v>^{⊗m} is a non-zero binary
homogeneous form of degree m>=1, which has a projective root v*≠0 by the fundamental theorem of algebra
(f(1,z) has a complex root, else f=c·x^m with root (0,1)). Then C|v*>^{⊗m}=0, contradicting the
non-vanishing demand: the product hPEPS |v*>^{⊗n} is annihilated. The argument uses only fixed non-zero
linearity, covering projectors, Kraus maps, and boundary-algebra constructions alike.
Numerical certificate `output/artifacts/verify_impossibility.py` (numpy only, seeded): exact 2x3-torus
cat contraction (error 0); generic-C violating pair with patch RDM eigenvalues (0.637,0.363,0,0) and
rank-2 marginal; rank-1 kill roots with |f(v*)|~1e-13; Sym-killer annihilation. All checks pass.

## Limitations

Exact pure-state projection by a single A- and n-independent C only. Does not rule out A-dependent or
n-dependent filters, approximate or bounded-failure probabilistic variants, multi-operator or adaptive
schemes, or bond-dimension witnesses avoiding a universal patch filter. The hPEPS-form-complement and SDP
steps of the target chain are moot once the first universal-projection step fails.

## Reproducibility

Run `python3 output/artifacts/verify_impossibility.py` (requires numpy). Deterministic seed; prints all
sub-checks and exits with assertion failure on any mismatch.

## References

- Admitted target: cut-and-glue operators for 2D homogeneous PEPS and finite-patch monogamy trade-off.
- O. Buerschaper, Twisted injectivity in PEPS and classification of quantum phases, arXiv:1307.7763.
- Flexible-geometry PEPS studies; Seynnaeve MPS geometry/invariant-theory notes (background only).
