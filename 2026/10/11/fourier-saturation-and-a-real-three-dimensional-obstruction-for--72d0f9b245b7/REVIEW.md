# Scientific review

## Correctness — PASS

The lower index bound follows from the coordinate norm formula and ordinary numerical index one of \(\ell_1\). The sharpness construction uses columns of a normalized Fourier or Walsh matrix and Bessel's inequality, followed by \(\ell_p\)-to-\(\ell_2\) comparison for \(p\ge2\). The dimension obstruction follows from a biorthogonal family and the strictness of an attained finite-dimensional infimum. In the real three-dimensional case, equality would force three flat signed columns and an impossible odd-order sign orthogonal matrix. The actual embedded script `verification/check_joint_index.py` replayed with output `VERIFY_OK checks=19847 ... analytical_proof_required=True`; it is a supplementary check, not the infinite proof.

## Originality — PASS, subject to residual prior-art risk

The closest same-object paper is Mal, arXiv:2212.06500v1, particularly Theorems 3.1 and 3.9 and Example 2.7. The universal bound and two-tuple \(\ell_1\) case are previously known; the arbitrary-length complex Fourier construction, dyadic real extension, dimension obstruction and strict real/complex three-tuple separation are not supplied by these statements. The paper's adjoint example explicitly prevents the obvious inference from its \(\ell_\infty\) formula. The full-text later work arXiv:2507.04700v1 studies differentiability and supporting functionals; the inspected theorems do not give index minimization or the odd-order obstruction. Semantic published-record searches for joint numerical indices, Fourier constructions, and the signed three-dimensional case returned related matrix and frame constructions, not a dominating joint-index theorem. Indexing gaps and alternate formulations remain a risk; no claim of universal literature independence is made.

## Mathematical value — PASS

The joint numerical index is a natural sharp stability factor comparing simultaneous operator norms and norming-state measurements. The result solves the missing multi-operator \(\ell_1\) branch in complex finite dimension for \(p\ge2\), identifies an infinite sequence of real saturation regimes, and proves two independent structural limits: insufficient ambient dimension, and the odd-order sign-parity failure even at equal dimension. The latter distinguishes real and complex scalars at the first nontrivial three-tuple rather than merely recomputing the already known two-tuple table.

## Limits and sources

The exact positive real three-dimensional gap and general non-dyadic real cases are open here. The relevant full-text comparators were arXiv:2212.06500v1, arXiv:2507.04700v1, and arXiv:2201.03055v1; related published mathematical-record hits concern different invariants. No finite experiment is used as proof of an infinite statement.

Same-model review: passed. Independent audit: not yet performed.
