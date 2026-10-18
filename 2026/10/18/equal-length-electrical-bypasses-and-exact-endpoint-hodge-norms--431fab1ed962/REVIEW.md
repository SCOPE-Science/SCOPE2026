# Scientific assessment: equal-length electrical bypasses for Steiner pair designs

## Correctness — PASS

The claim fixes an existing simple Steiner \(2\)-\((v,k,1)\) design, unit incident-edge conductances and the canonical orthogonal cut/cycle projectors. The central nonstandard identity is not inferred from numerical experiments: \(NN^{\mathsf T}=(r-1)I+J\) leads to the explicit Poisson potential \(x=(k/v)\mathbf1_{p_0}-(1/v)\mathbf1_{B_0}\) and \(y=(N^{\mathsf T}x-\mathbf1_{B_0}^{\mathrm{block}})/k\). The graph gradient equals the unique electrical flow. Counting the length-five bypasses and evaluating all current signs establishes the equal-weight path decomposition and exactly \(5-4\rho\) and \(6(1-\rho)\) for the two endpoint projection norms. The dominance cases follow from the design incidence bound \(b\ge v\). There is no reliance on edge transitivity or on existence of designs with unverified parameters.

The independent exact-rational checker reconstructs grounded graph Laplacians and verifies \(279\) full projector columns and \(14{,}064\) enumerated length-five bypasses over five finite designs, including nonsymmetric affine cases. These tests corroborate, but do not substitute for, the universal proof.

## Originality — PASS (self-review, residual uncertainty)

The nearest primary framework is Dilworth–Kutzarova–Ostrovskii, arXiv:2305.12582 (2023), which develops cycle-space projection theory with explicit investigations of Hamming graphs and tori, not the Steiner point–block current law. Schild–Rao–Srivastava, arXiv:1708.01632 (2017), and Gurel-Gurevich–Nachmias–Sachdeva, arXiv:2605.24130 (2026), prove general electrical-current localization bounds rather than the present exact uniform decomposition. A related symmetric-design calculation already covers its projective-plane special cases; that statement does not cover nonsymmetric Steiner designs and does not state the equal-weight shortest-bypass theorem across all such designs. The affine-plane instances have different point/block counts and cannot be covered by the symmetric hypothesis. Relevant semantic record searches found Steiner incidence-graph topology results, but no identified equivalent electrical projector theorem.

The principal residual risk is an equivalent formula in older incidence-network, electrical-routing, or design literature that uses different terminology. Available full texts were inspected where materially relevant; a related record's full text was not accessible, so its summary is not asserted to prove complete noncoverage. Originality is not a claim of exhaustive uniqueness in all publications.

## Mathematical value — PASS

This is an exact structural statement for a broad natural class of finite linear spaces, not an arbitrarily selected small example or isolated numeric table. A **Hilbert-energy-minimizing** unit edge flow, which is generally not length-minimizing, is shown to use *only* the direct edge and equal-weight **shortest bypasses**, independently of automorphism groups or the isomorphism type of the underlying Steiner design. The theorem converts that current geometry into universal quantitative Banach-space cut/cycle norms, a strict dominance classification, and sharp asymptotic bounds. It extends the symmetric-design case to nonsymmetric Steiner triple systems and affine geometries of unbounded order.

No result is asserted for arbitrary minimum-norm projections, weighted graphs, non-Steiner block designs, or intermediate \(\ell_p\). Independent validation and comprehensive literature certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
