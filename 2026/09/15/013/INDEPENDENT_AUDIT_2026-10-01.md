---
audit_date_utc: 2026-10-01
status: passed
record_id: SCOPE-20260915-013
---

# Scientific audit

## Final claim

For the \(B_2\)-irreducible Dolbeault--Dirac spectral triple, \(\zeta_b(s)=\operatorname{Tr}(b|D|^{-s})\) is holomorphic for \(\Re(s)>0\) for every bounded algebra element \(b\); for \(b=1\) each eigenvalue-square branch has an exact \(Kq^{-2(n+l)}B(q^n,q^l)\) factorization with \(B(0,0)=1\), \(s^6\zeta_1(s)	o640/(\log q^{-1})^6\), and every fixed-row or fixed-column sector extends meromorphically with exact order-4 poles on the principal lattice and possible shifted pole lattices.

## Correctness — PASS

The primary spectrum and multiplicity formulas were reconstructed from Corollary 15. Each \(q\)-number product factors as a positive constant times \(q^{-2(n+l)}\) times a polynomial in \(q^n,q^l\) with constant term 1. The even and odd Weyl multiplicities have the same degree-4 top part \((8/3)nl(n+l)(2n+l)\); its double geometric-sum moment contributes \(80/(\log q^{-1})^6\) per signed branch, and the four \(\pm\) branch pairs give \(8\cdot80=640\). Boundary rows have lower order. For a fixed row or column, the multiplicity is cubic and the analytic binomial expansion of \(B(q^n)^{-s/2}\) yields shifted geometric sums; the \(j=0\) term has a nonzero cubic coefficient, giving exact order 4 on the principal lattice. All-\(b\) holomorphy on \(\Re(s)>0\) follows from boundedness of \(b\) and the source's \(0^+\)-summability.

Checked sources: Díaz García--Ó Buachalla--Wagner, arXiv:2109.09885, Corollary 15 and Theorem 16; artifacts/zeta1_factorisation.py; artifacts/branches_factor.py; artifacts/emergent_checks.py; artifacts/test_domination.py

Residual risk: The auxiliary script `emergent_checks.py` contains a misleading extra factor in one printed heuristic line; the audited \(640\) constant was derived independently from the source multiplicities and does not rely on that printout. No bulk two-variable meromorphic continuation is claimed.

## Originality — PASS

The primary paper computes the spectrum, multiplicities, and \(0^+\)-summability but does not analyze the zeta function's exact small-\(s\) coefficient or meromorphic sector structure. Searches for the \(B_2\) triple together with zeta, dimension spectrum, meromorphic continuation, and the constant \(640\) found no prior result beyond this record. The new statements are analytic consequences requiring a nontrivial summation of all spectral branches, not a quoted theorem from the source.

### Equivalent Formulations

Searches: B2 irreducible quantum flag Dolbeault Dirac zeta meromorphic continuation; dimension spectrum B2 quantum flag

Evidence: The primary paper stops at exponential spectral growth and \(0^+\)-summability.

Reasoning: Neither a dimension-spectrum statement nor the exact zeta asymptotic is present.

### Broader Coverage

Searches: quantum flag manifold zeta function Dolbeault Dirac dimension spectrum; q spectral triple zeta meromorphic continuation

Evidence: General \(0^+\)-summability results do not determine the coefficient \(640\) or the sector pole lattice.

Reasoning: The explicit branch factorization is needed.

### Exact Database Or Table

Searches: 640 log(q)^-6 B2 Dolbeault Dirac; B2 zeta sector poles

Evidence: No exact table or formula was found.

Reasoning: The constant and pole orders are not standard database outputs.

### Claim Vs Prior Implication

Searches: Corollary 15 arXiv 2109.09885 zeta

Evidence: Corollary 15 gives raw branch eigenvalues and multiplicities only.

Reasoning: Substantial asymptotic summation and meromorphic-expansion work remains after the source theorem.


### Source inspections

- **SUPPORTING_NOT_COVERING** — 2109.09885 (https://arxiv.org/pdf/2109.09885): Primary full PDF, especially Corollary 15 pages 40--41 and Theorem 16 page 42, including all four spectral branches, Weyl multiplicities, and \(0^+\)-summability. Evidence: It supplies the spectral data but no zeta asymptotic or meromorphic sector continuation.
- **SUPPORTING_NOT_COVERING** — s00220-022-04435-5 (https://doi.org/10.1007/s00220-022-04435-5): Published version metadata and theorem scope corresponding to the arXiv source. Evidence: Same spectral-triple result, no zeta-structure theorem located.

Checked sources: https://arxiv.org/pdf/2109.09885; https://doi.org/10.1007/s00220-022-04435-5; artifacts/zeta1_factorisation.py; artifacts/branches_factor.py; artifacts/emergent_checks.py; artifacts/test_domination.py

Residual risks: A specialist noncommutative-geometry paper may derive analogous general \(q\)-Dirac zeta expansions, but no source inspected states this \(B_2\) coefficient or sector pole result.

## Value — PASS

Exact zeta asymptotics and sector pole orders are natural spectral invariants for a \(0^+\)-summable quantum flag spectral triple. They sharpen qualitative summability into reusable analytic information relevant to dimension-spectrum and heat/zeta questions while explicitly stopping short of the unresolved bulk continuation.

Checked sources: Díaz García--Ó Buachalla--Wagner spectral formulas

Residual risk: The strongest two-variable bulk continuation and full dimension spectrum remain open.

## Disposition

**PASSED**. Acceptance requires PASS on correctness, originality, and value.
