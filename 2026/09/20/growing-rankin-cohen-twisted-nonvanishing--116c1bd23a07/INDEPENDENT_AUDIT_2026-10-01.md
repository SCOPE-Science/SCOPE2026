# Fresh mathematical audit — Square-root Rankin-Cohen independence for quadratic twists

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The endpoint coefficient is exactly a Dirichlet convolution of \(a_\ell(d)=\chi_D(d)d^{\ell-1}\) with \(n^{2e}\); because \(a_\ell\) is completely multiplicative, its Dirichlet inverse is \(\mu(d)\chi_D(d)d^{\ell-1}\). The resulting unitriangular column transform sends the endpoint matrix exactly to \(W_r=(n^{2e})\). The package's exact-integer replay independently verifies this transform and its Vandermonde determinant. After transformation, the quoted explicit Fourier-coefficient remainder gains the divisor factor \(d^{-k_e-2}\); the Lagrange bound on \(W_r^{-1}\) is subexponential on the \(r=c\sqrt\ell\) scale, while Stirling gives exponential rate \(\log(2\pi e|D|c^2)<0\). Thus the perturbation norm tends to zero, proving eventual invertibility. The Petersson spanning formula then gives the nonvanishing-dimension bound.

Sources checked: RESULT.md at the assigned source tree; artifacts/verify_mobius_vandermonde.py; Kayath–Lane–Neifeld–Ni–Xue 2025 open full text; published 2026-09-18 growing-block theorem.

Correctness risks: The very recent Takloo-Bighash preprint full text could not be retrieved in this run, so the exact Proposition 3.1 remainder inequality was not re-read at its primary source; the audit verified its use and all downstream algebra, and the same displayed estimate is also reproduced in the earlier published growing-block result..

## Originality

**PASS.** A published 18 September result already grows the block under \(r\log(2r)=o(\sqrt\ell)\), so fixed-\(r\) versus growing-\(r\) is not itself novel. The present theorem is nevertheless strictly stronger: it reaches \(r=\lfloor c\sqrt\ell\rfloor\) for every \(c<(2\pi e|D|)^{-1/2}\) by exact Möbius preconditioning. The earlier condition does not include any fixed positive multiple of \(\sqrt\ell\).

### Equivalent formulations

Searches/sources: Published-record search: Rankin Cohen brackets quadratic twists square root many independent central L values; Takloo-Bighash arXiv:2609.19649; Kayath–Lane–Neifeld–Ni–Xue DOI 10.4153/S0008414X25101697.

Evidence: Takloo-Bighash is described as proving independence for every fixed initial block. Kayath et al. construct the nonvanishing subspace/spanning framework and discuss a much larger conjectural family.

Neither primary formulation visible in this audit states the explicit square-root-scale block with the constant \(1/\sqrt{2\pi e|D|}\).

### Broader coverage

Searches/sources: Published 2026-09-18 record 'A growing block of traced Rankin--Cohen brackets is linearly independent'; Luo weight-aspect nonvanishing results for \(D=1\).

Evidence: The 18 September theorem proves \(r\log(2r)=o(\sqrt\ell)\), which is weaker than \(r=c\sqrt\ell\). For \(D=1\), stronger counting lower bounds are known, but they do not imply linear independence of this explicit Rankin–Cohen family.

Known broader counting results dominate only the \(D=1\) counting corollary, which the record explicitly does not present as new; they do not dominate the explicit-family independence theorem.

### Exact database or table

Searches/sources: Resultary exact/semantic search for growing Rankin–Cohen independence; Full inspection of the 2026-09-18 Resultary record.

Evidence: The database search found the near-prior \(r\log r=o(\sqrt\ell)\) theorem and no earlier \(c\sqrt\ell\) theorem.

The exact published-record comparison is material and establishes the novelty boundary.

### Claim versus prior implication

Searches/sources: Check whether \(r\log(2r)=o(\sqrt\ell)\) implies \(r=c\sqrt\ell\); Compare prime-index determinant method with Möbius-transformed all-index matrix.

Evidence: For \(r=c\sqrt\ell\), \(r\log(2r)/\sqrt\ell\sim c\log\ell/2\), so the earlier hypothesis fails. The exact Möbius transform removes the divisor endpoint before conditioning and is the mechanism that eliminates the logarithmic loss.

The final claim is not a corollary or special case of the 18 September theorem; it crosses that theorem's asymptotic boundary.

### Source inspections

- **A growing block of traced Rankin--Cohen brackets is linearly independent** — PARTIAL_COVERAGE.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-growing-rankin-cohen-independence--b4aacb190052
  Trigger: Closest earlier published theorem on the same bracket family.
  Material read: Complete RESULT.md and proof.
  Method: public full text
  Evidence: It proves \(r\log(2r)=o(\sqrt\ell)\), not a fixed positive multiple of \(\sqrt\ell\).
- **Subspaces spanned by eigenforms with nonvanishing twisted central L-values** — SUPPORTING_NOT_COVERING.
  Identifier: https://doi.org/10.4153/S0008414X25101697
  Trigger: Primary framework for the nonvanishing subspace and Rankin–Cohen spanning family.
  Material read: Open-access full HTML/PDF text, including Sections 1, 2 and 5 material surfaced in the audit.
  Method: lawful open-access full text
  Evidence: It constructs spanning sets and the Petersson/Rankin–Selberg framework but does not state the square-root independence theorem.
- **Simultaneous nonvanishing of quadratic twists via Rankin-Cohen brackets** — ACCESS_RISK.
  Identifier: https://arxiv.org/abs/2609.19649
  Trigger: Immediate primary predecessor supplying the explicit coefficient estimate.
  Material read: Abstract/metadata only; full text retrieval failed through the available open-access route.
  Method: lawful open-access attempt
  Evidence: The package quotes Proposition 3.1 explicitly; the primary full text was not available to re-check the displayed bound in this run.

Originality risks:
- The Takloo-Bighash full text was inaccessible in this run, leaving source-version risk for the exact constant in its quoted remainder bound.
- Unindexed concurrent work on the September 2026 preprint could overlap.

## Scientific value

**PASS.** Moving from almost-square-root divided by logarithms to a genuine \(c\sqrt\ell\) family is a mathematically meaningful asymptotic improvement, and the exact Möbius preconditioning is reusable. For nontrivial fixed quadratic twists it yields a quantitative growing lower bound on the dimension of the nonvanishing subspace.

Value risks: The result remains below the conjectural linear-size family and does not claim the constant is optimal..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to the scientific result or slogan is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
