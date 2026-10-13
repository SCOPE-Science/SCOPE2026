# Scientific review: Idempotent derivations of free two-step nilpotent Lie algebras

## Correctness — PASS
The proof directly reconstructs every derivation as a block map \(D_{A,f}\) on the generator space and its exterior square, and derives exactly three equations for \(D^2=D\). The eigenvalue decomposition of \(L_A\) forces \(r\le1\) outside characteristic \(2\), while in characteristic \(2\) the eigenvalue \(2\) vanishes and all generator ranks are permitted. A central-shear conjugation removes the free \(f\)-parameters; ordinary Gaussian subspace and complement counts give the two finite-field polynomials. Direct independent enumeration of the small cases described in `VERIFICATION.md` returned `VERIFY_OK`. Computation is not used as a substitute for proof.

## Originality — PASS, with residual bibliographic uncertainty
Benito–Roldán-López (arXiv:1911.01897, Proposition 1 and Corollary 1) is the closest object-level primary source and proves a general parametrization of all derivations and automorphisms of free nilpotent Lie algebras. Its broader representation logically accommodates the operators counted here, but the inspected text does not state the composition-idempotent condition's characteristic dichotomy, the normal-form orbits, or any labeled finite-field rank polynomial. La Rosa–Mancini (arXiv:2301.11058) analyze derivation Lie algebras and almost-inner operators on related class-two algebras. Eick–Moede (arXiv:2205.03155) enumerate inner-idempotent elements on simple modular Lie algebras; these are not the noninner idempotent derivations counted here. Hakavuori and collaborators (arXiv:2011.06871) treat characteristic-zero torsion-free gradings. Public mathematical-result searches identified related free-affine growth and filiform adjoint-rank findings, not matching statements. An equivalent theorem elsewhere remains possible; search failure is not proof of novelty.

## Value — PASS
The operator family is intrinsic and mathematically motivated by finite-field and characteristic-two Lie gradings. The theorem gives an exact all-rank/all-field classification and rational-point count for every generator dimension at least three, not only example-level data. The jump from two orbits to \(n+1\) orbits and the characteristic-two rank spectrum encode genuine structural constraints of the exterior-square bracket.

## Limits and remaining risks
The theorem concerns free Lie algebras of nilpotency class two and ordinary composition-idempotent derivations, not arbitrary nilpotent Lie algebras or Lie retractions. The exact count is proved algebraically; tests cover finitely many small instances. Broader historical grading classifications may use different terminology and warrant independent literature review. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
