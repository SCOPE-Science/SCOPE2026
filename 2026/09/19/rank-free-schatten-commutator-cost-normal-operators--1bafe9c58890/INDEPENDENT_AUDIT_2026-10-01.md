# Independent audit — Rank-free mixed Schatten commutator cost for finite-rank normal operators

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** Schatten Hölder gives \(\|[A,B]\|_r\le2\|A\|_p\|B\|_q\), hence the universal lower bound. For normal \(T=U|T|\), the commuting split \(X=U|T|^{r/p}\), \(Y=|T|^{r/q}\) satisfies \(XY=YX=T\) and \(\|X\|_p\|Y\|_q=\|T\|_r\). Tensoring with a rank-one factorization \(P=[C,Z]\) gives \([X\otimes C,Y\otimes Z]=T\otimes P\). A finite-rank normal operator on an infinite-dimensional separable Hilbert space is unitarily equivalent to \(T\otimes P\), and the same holds for normal compact targets with infinite-dimensional kernel. The Brown--Anderson trace obstruction and rank-one construction give the stated strict existence threshold for nonzero positive finite-rank targets.

## Originality

**PASS.** Best-of-knowledge originality passes for the rank-free mixed factorization gauge estimate on normal targets. Classical work already owns the ideal-membership threshold and is treated as prior input.

### Equivalent formulations

The comparison used the factorization gauge itself, not merely existence of a commutator representation.

Evidence: The published archive returned this record as the exact match and no earlier quantitative norm-gauge theorem. Searches in operator-ideal terminology located ideal-membership and trace-obstruction results, not an infimum-product estimate equivalent to \(\Gamma_{p,q}(T)\asymp\|T\|_r\).

### Broader coverage

No inspected broader theorem dominates the mixed Schatten gauge estimate.

Evidence: The 2004 full paper characterizes commutator spaces of operator ideals and records the Brown--Anderson finite-rank trace threshold. Those membership theorems do not furnish the claimed rank-independent infimum of the product of \(S_p\) and \(S_q\) factor norms for a normal target. Recent operator-norm compact commutator results use a related tensor mechanism but in a different normed problem.

### Exact database or table

The membership threshold is known; the exact database check was therefore focused on the quantitative gauge statement.

Evidence: No prior archive row or standard quantitative table with the two-sided rank-free \(S_r\) estimate was located.

### Claim versus prior implication

The result is a short structural quantitative consequence of classical ingredients, but it is not mechanically identical to the known threshold.

Evidence: Membership alone only asserts existence and does not control an infimum product of factor norms. The upper estimate additionally requires the balanced commuting polar split and the unitary equivalence of the tensor model; these are not stated as a quantitative theorem in the inspected source.

### Source inspections

- **The commutator structure of operator ideals** — ESSENTIAL_PRIOR_NOT_COVERING.
  Identifier: https://doi.org/10.1016/S0001-8708(03)00141-5
  Material read: complete 94-page author PDF, including the finite-rank/rank-one commutator sections and the Schatten remarks around the threshold.
  Evidence: The source supplies and attributes the ideal-membership/trace threshold but does not state the mixed infimum-product normal-target estimate.

### Checked sources

- https://doi.org/10.1016/S0001-8708(03)00141-5
- https://doi.org/10.1515/crll.1977.291.128
- https://doi.org/10.1007/s00020-024-02764-9
- https://acta.bibl.u-szeged.hu/14468/
- https://iumj.org/article/3231/
- Resultary published-finding semantic search

### Residual risks

- Older operator-ideal literature may contain an equivalent quantitative estimate under different norm/gauge terminology.
- The Anderson and Brown original papers were not both inspected in full during this audit; the threshold comparison relies on the complete Dykema--Figiel--Weiss--Wodzicki treatment and its precise attribution.

## Scientific value

**PASS.** The theorem converts a qualitative ideal-membership threshold into a dimension- and rank-free quantitative factorization estimate for a broad structured class and identifies the natural target norm. The tensor-transfer mechanism is reusable beyond a single finite example.

## Final assessment

The unchanged final claim passes correctness, originality, and scientific value. No research claim or slogan change is required.

This assessment is not formal verification or expert attestation and does not guarantee that no undiscovered prior art exists.
