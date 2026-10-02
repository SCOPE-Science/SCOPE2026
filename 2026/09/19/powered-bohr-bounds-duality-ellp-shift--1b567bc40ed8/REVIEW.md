# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The norm transference step is valid: a finite polynomial of either unilateral shift is a compression of the corresponding bilateral convolution operator, while finitely supported bilateral test vectors can be translated away from the boundary, so the unilateral and bilateral polynomial norms coincide. Banach adjoint duality therefore gives \(R_p=R_{p'}\). Testing Taylor truncations of the disk automorphism \(\phi_a(z)=(a-z)/(1-az)\) on a far basis vector produces disjoint coordinates and exactly the stated powered coefficient sum, yielding the \(eta_q\) upper bound. The endpoint \(\ell_1\) and \(\ell_\infty\) norms reduce exactly to the classical Bohr sum, while \(p=2\) is von Neumann's inequality. The two first-order expansions around \(q=2\) correctly bracket the linear defect by \((\log2)/2\) and \((\log3)/2\).

Originality: PASS. Kania's recent primary paper supplies the shift construction and the interpolation lower bound but its accessible primary statement does not contain the dual-exponent identity, powered-Bohr obstruction, endpoint limits, or Hilbert-point linear defect. Kayumov--Ponnusamy's 2019 primary paper was inspected through its journal page and full-document metadata: it proves the scalar powered Bohr radius for Schur functions, not an operator \(\ell_p\)-shift radius. Resultary searches for the operator radius, duality and powered-Bohr transfer returned this record as the only exact match. The Kania PDF could not be retrieved in verified full text during this run, so an unindexed overlap inside that very recent paper remains an explicit residual risk.

Scientific value: PASS. The result turns a one-sided interpolation estimate for a newly introduced shift radius into a quantitative two-sided theory, identifies the Hilbert exponent as the unique full-radius point, gives exact duality and endpoint limits, and pins down the first-order scale of the defect near \(p=2\). Those are natural structural properties of the new invariant rather than arbitrary evaluations.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
