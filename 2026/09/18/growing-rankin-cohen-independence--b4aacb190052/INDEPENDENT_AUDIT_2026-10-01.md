# Independent mathematical audit — 2026-10-01

## Final claim

A growing block of traced Rankin–Cohen brackets is linearly independent

## Correctness — PASS

PASS. The argument correctly uniformizes Takloo-Bighash's explicit coefficient bound. If \(P\) is the \(r\)-th test prime then \(P=O_D(r\log(2r))\); the hypothesis \(r\log(2r)=o(\sqrt{\ell})\) gives \(P^2=o(\ell)\), while Stirling makes the coefficient error superexponentially small relative to the determinant losses. The determinant without coefficient errors is a rank-one perturbation of the Vandermonde-type matrix: all terms with two constant columns vanish, the \(p_r^{\ell-1}\Delta_r\) term dominates the earlier-prime terms, and the exact determinant-ratio bounds are sufficient because \(\ell/(Pr\log P)	o\infty\). The error perturbation remains negligible since \(r^2(\log(2r))^2=o(\ell)\). The repository script checks the finite Vandermonde-ratio identities, but the asymptotic inequalities themselves were reconstructed independently.

## Originality — PASS

PASS to the best of current knowledge. Takloo-Bighash's primary theorem explicitly fixes \(r\), whereas the audited theorem allows \(r\) to grow almost at the square-root scale. Kayath–Lane–Neifeld–Ni–Xue give the spanning framework and conjecture a much larger linear-size independent block, with finite computations rather than a proof in the growing regime. Resultary found the same record and a stronger square-root result dated 20 September 2026, two days after this record; that later result does not establish earlier coverage. No pre-18-September theorem located in the inspected sources implies the stated \(r\log(2r)=o(\sqrt{\ell})\) range.

### Equivalent formulations

The source theorem cannot be converted to a growing \(r\) by quantifier rearrangement; uniform error control is the new step.

### Broader coverage

A conjecture and finite verification do not cover the audited asymptotic theorem; fixed-\(r\) existence also does not imply a uniform growing block.

### Exact database or table

Finite tables cannot establish the infinite asymptotic claim, and later work is not prior coverage of the 18 September result.

### Claim versus prior implication

The prior statements do not mechanically imply any unbounded \(r(\ell)\); additional uniform estimates are essential.

## Scientific value — PASS

PASS. This is a motivated quantitative strengthening of a fixed-block theorem toward an explicit basis/nonvanishing conjecture. It proves a genuinely growing family of independent Rankin–Cohen forms, isolates the uniform determinant mechanism, and supplies a nontrivial intermediate scale rather than an arbitrary finite instance. The record correctly limits its value claim: for \(D=1\) the numerical nonvanishing count is not best possible, while the explicit growing-block independence remains the substantive fact.

## Source inspections

- **Simultaneous nonvanishing of quadratic twists via Rankin-Cohen brackets** (arXiv:2609.19649v1): STRICTLY_WEAKER_FIXED_BLOCK. Primary arXiv abstract, which explicitly quantifies over fixed \(r\); the audited record's quoted explicit coefficient estimate was checked algebraically against the uniform argument. The source proves independence for every fixed first \(r\) brackets, not for an unbounded \(r(\ell)\).
- **Subspaces spanned by eigenforms with nonvanishing twisted central L-values** (DOI 10.4153/S0008414X25101697): CONJECTURAL_BROADER_TARGET_NOT_COVERAGE. Open-access full text including Proposition 2.4 and Discussion/Conjecture 7.1. It constructs the spanning family and reports finite computational verification of a linear-size determinant, but leaves general independence as a conjecture.

## Checked sources and replay paths

- Assigned RESULT.md and exact frozen tree
- artifacts/verify_determinants.py and verify_output.txt
- Takloo-Bighash primary abstract
- Kayath et al. open-access full text
- Resultary semantic search including the later 20 September stronger record

## Residual risks

- The Takloo-Bighash paper is extremely recent, and searchable full text of the entire preprint was not retrievable during this run; the fixed-\(r\) quantifier is explicit in the primary abstract.
- A later 20 September record proves a stronger square-root-scale bound by a different refinement, so the audited theorem is not state of the art now even though it remains original relative to earlier sources.

## Disposition

**passed**
