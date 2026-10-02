# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **passed**.

Correctness: **PASS**. For the full evaluation set, \(P(x)=x^q-x\) gives \(P'(a)=-1\) at every \(a\in\mathbb F_q\), hence every Lagrange coefficient is \(-1\). With \(Q=p^\ell\), choose a multiplier \(eta\) satisfying \(eta^{Q+1}
e1\); for \(q>4\) such a choice exists because \(q-1>Q+1\) for \(1\le\ell<e\), apart from the excluded \(q=4\) equality case. In the strict degree range, root counting forces \(g=-f^Q\), the extension tail kills the top \(s\) coefficients, and the \(z=k-s-h\) scaled evaluation points impose exactly \(z\) distinct roots, leaving dimension \(h\). At the single boundary \(Q(k-1)=q-k\), the scalar extension matrix with \(\mu^{Q+1}
e1\) kills the one possible surviving tail coefficient and restores the same argument. The \(s=2\) distance criterion and the EAQECC conversion are then used exactly within their published domains. The supplied GF(8) and GF(27) program is a finite consistency check, not the proof.

Originality: **PASS**. PASS to the best of current knowledge. The motivating GRL paper gives the general hull criterion for arbitrary Galois index but imposes \(2\ell\mid e\) on its explicit normalized-root constructions, including its full-evaluation theorem. The audited argument uses the special full-field identity \(u_a=-1\) to remove that root-existence requirement and handles the boundary separately. Wan–Zhu treat arbitrary indices for GRS/EGRS MDS codes, not generalized Roth–Lempel extensions of length \(q+s\). Resultary found the same record and a later characteristic-two generalization, but no earlier GRL theorem dominating the full-field all-index statement. The source preprint is extremely recent, so near-simultaneous unindexed work remains a real risk.

Scientific value: **PASS**. The claim closes an explicit divisibility gap in a natural recent GRL hull construction rather than selecting an arbitrary parameter point: it covers every Galois index for the full evaluation set, preserves all hull dimensions in the stated range, and yields the length-\(q+2\) AMDS/NMDS and EAQECC consequences. The full-field normalization is elementary, but the resulting removal of an otherwise global hypothesis is a useful structural boundary.

Detailed evidence, source inspections, originality comparisons, checked sources and residual risks are in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The original same-model review remains historical evidence and is not relabeled as independent.
