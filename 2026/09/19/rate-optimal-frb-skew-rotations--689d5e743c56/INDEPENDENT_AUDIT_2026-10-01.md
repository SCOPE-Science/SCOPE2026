# Independent audit — Exact rate-optimal steps for FRB/RFB on the skew-rotation family

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The characteristic discriminant simplifies to \(1-4(1+\gamma)h^2\). Direct modulus algebra gives the two displayed branches. For \(\gamma>-1\), the pre-coalescence expression decreases with \(h\) and the post-coalescence expression increases, so the unique global minimizer is \(h=1/(2\sqrt{1+\gamma})\) with spectral radius \(1/\sqrt{\gamma+2}\). At \(\gamma=-1\), one root is exactly one. For \(\gamma<-1\), the same closed form is strictly decreasing and tends to \(1/\sqrt{-\gamma}\). Independent direct complex-root evaluations at representative positive, boundary, and negative parameters reproduced these formulas and limits; the repository verification source was inspected as supporting evidence only.

## Originality

**PASS.** Best-of-knowledge originality passes for the full parameter-dependent rate phase diagram. The sharp stability boundary and the \(\gamma=0\) rate are prior and are excluded from the novelty claim.

### Equivalent formulations

Searches included both FRB and RFB naming conventions and the repeated-root characterization.

Evidence: The archive search returned this record as the exact match; the closest later record optimizes a different reflection parameter and postdates it. No earlier inspected source states the same \(\gamma\)-dependent rate minimizer and negative-\(\gamma\) phase.

### Broader coverage

The available broader results control stability regions or the already-known zero-resolvent-skew special case, not this rate optimization.

Evidence: Shehu gives the exact stability threshold for the skew family and a broader normal-operator stability phase diagram, but the inspected paper does not optimize the spectral radius over the stable step. The \(\gamma=0\) fastest rotation rate \(1/\sqrt2\) is already known and is explicitly excluded from the novelty claim. No inspected general splitting theorem supplies the displayed optimal-step law for all \(\gamma\).

### Exact database or table

The exact database check was performed on the rate formulas rather than the already-known stability ceiling.

Evidence: No earlier archive record with \(h_{\rm opt}=1/(2\sqrt{1+\gamma})\) or the complete rate phase was located.

### Claim versus prior implication

The final claim requires analyzing both characteristic roots throughout parameter space and is not a restatement of the stability theorem.

Evidence: A stability boundary does not determine the minimizer of spectral radius; in fact the theorem shows they differ substantially. The \(\gamma=0\) rate is a single parameter value and does not imply the finite optimum for all \(\gamma>-1\) or the monotone \(\gamma<-1\) regime.

### Source inspections

- **The sharp step-size constant for one-call reflection splittings on monotone inclusions** — ESSENTIAL_PRIOR_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2609.18373
  Material read: complete five-page preprint, including the skew-family theorem and rate-related remark.
  Evidence: The source proves the stability ceiling for the relevant nonnegative skew parameter range and points to the known \(\gamma=0\) rate benchmark; it does not state the claimed all-\(\gamma\) spectral-radius optimum.

### Checked sources

- https://arxiv.org/abs/2609.18373
- https://arxiv.org/abs/2509.02005
- Malitsky--Tam, SIAM Journal on Optimization 30(2) (2020)
- Resultary published-finding semantic search

### Residual risks

- The motivating stability preprint is very recent, so contemporaneous follow-up optimization work may not yet be indexed.

## Scientific value

**PASS.** The exact rate law gives a practical and structural distinction between largest stable step and fastest asymptotic step, completely classifies the natural planar skew family, and identifies a repeated-root phase transition. This is a motivated parameter classification rather than an arbitrary slice.

## Final assessment

The unchanged final claim passes correctness, originality, and scientific value. No research claim or slogan change is required.

This assessment is not formal verification or expert attestation and does not guarantee that no undiscovered prior art exists.
