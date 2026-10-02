# Independent mathematical audit — 2026-10-01

## Final claim

Full-field generalized Roth–Lempel Galois hulls for arbitrary indices

## Correctness — PASS

PASS. For the full evaluation set, \(P(x)=x^q-x\) gives \(P'(a)=-1\) at every \(a\in\mathbb F_q\), hence every Lagrange coefficient is \(-1\). With \(Q=p^\ell\), choose a multiplier \(eta\) satisfying \(eta^{Q+1}
e1\); for \(q>4\) such a choice exists because \(q-1>Q+1\) for \(1\le\ell<e\), apart from the excluded \(q=4\) equality case. In the strict degree range, root counting forces \(g=-f^Q\), the extension tail kills the top \(s\) coefficients, and the \(z=k-s-h\) scaled evaluation points impose exactly \(z\) distinct roots, leaving dimension \(h\). At the single boundary \(Q(k-1)=q-k\), the scalar extension matrix with \(\mu^{Q+1}
e1\) kills the one possible surviving tail coefficient and restores the same argument. The \(s=2\) distance criterion and the EAQECC conversion are then used exactly within their published domains. The supplied GF(8) and GF(27) program is a finite consistency check, not the proof.

## Originality — PASS

PASS to the best of current knowledge. The motivating GRL paper gives the general hull criterion for arbitrary Galois index but imposes \(2\ell\mid e\) on its explicit normalized-root constructions, including its full-evaluation theorem. The audited argument uses the special full-field identity \(u_a=-1\) to remove that root-existence requirement and handles the boundary separately. Wan–Zhu treat arbitrary indices for GRS/EGRS MDS codes, not generalized Roth–Lempel extensions of length \(q+s\). Resultary found the same record and a later characteristic-two generalization, but no earlier GRL theorem dominating the full-field all-index statement. The source preprint is extremely recent, so near-simultaneous unindexed work remains a real risk.

### Equivalent formulations

The audited statement is not merely a rephrasing of Proposition II.8: it supplies multipliers and extension matrices proving existence for indices excluded from the source constructions.

### Broader coverage

Those broader coding-theory results do not imply the GRL full-evaluation theorem because the appended extension coordinates change the hull equations and distance criteria.

### Exact database or table

This is a parametric theorem, not a finite database row; search failure alone is not novelty proof and is treated only as supporting evidence.

### Claim versus prior implication

No inspected prior theorem mechanically implies existence of these GRL codes at the excluded indices; a new specialization argument is required.

## Scientific value — PASS

PASS. The claim closes an explicit divisibility gap in a natural recent GRL hull construction rather than selecting an arbitrary parameter point: it covers every Galois index for the full evaluation set, preserves all hull dimensions in the stated range, and yields the length-\(q+2\) AMDS/NMDS and EAQECC consequences. The full-field normalization is elementary, but the resulting removal of an otherwise global hypothesis is a useful structural boundary.

## Source inspections

- **Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs** (arXiv:2609.20453v1): FRAMEWORK_WITH_PARAMETER_GAP. Primary arXiv HTML around Proposition II.8, Lemma II.9, Proposition IV.1, Theorem IV.6, and Proposition VI.2. The general hull criterion is index-general, but the explicit construction section retains the \(2\ell\mid e\) normalization hypothesis; the full-evaluation theorem does not cover all indices.
- **Galois self-orthogonal MDS codes with large dimensions** (arXiv:2412.05011): DIFFERENT_CODE_FAMILY. Primary arXiv abstract describing all Galois indices and arbitrary hull dimensions via GRS/EGRS MDS codes. It treats GRS/EGRS MDS constructions, not generalized Roth–Lempel codes with appended extension coordinates.

## Checked sources and replay paths

- Assigned RESULT.md and exact frozen tree
- artifacts/verify_examples.py
- Wu et al. primary arXiv full text
- Wan–Zhu primary arXiv abstract
- Resultary semantic search

## Residual risks

- The motivating preprint appeared one day before the record, so unindexed near-simultaneous work is plausible.
- The finite GF(8) and GF(27) examples do not prove the parametric theorem; correctness rests on the polynomial root-count argument.

## Disposition

**passed**
