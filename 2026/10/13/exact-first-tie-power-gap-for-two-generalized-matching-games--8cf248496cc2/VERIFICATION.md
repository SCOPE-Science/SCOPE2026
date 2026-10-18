---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the precisely stated generalized matching model K=L+F_(n-L), n>=4 and two IID rounds at shared θ in (0,1), the null mass p_0(k) is the derangement formula and the full alternative/null likelihood ratio is (1-θ)^n Q_k(θ/(1-θ)) with Q_k=sum_{j<=k} binom(k,j)(n)_j r^j. The exact identities Q_1^2-Q_0Q_2=n r^2>0 and Q_0Q_3-Q_1^2=nr+n(2n-3)r^2+n(n-1)(n-2)r^3>0, with coordinatewise monotonicity, strictly separate all null-support outcomes of total>=3, the balanced (1,1), the unbalanced (0,2)/(2,0), and totals<=1. The common ordering across all θ yields a UMP test for α in [β,β+A+B], and the Neyman–Pearson randomization algebra gives the complete triangular power difference AB/(A+B)*nθ²(1-θ)^(2n-2)*min((α-β)/A,(β+A+B-α)/B). Rational independently evaluated matching masses and power gaps for n=4,6,8 at θ=1/5, and checked fixed-k Poisson derangement limits for the n^-1 peak coefficient λ² exp[-2(1+λ)]/2. No significance levels outside the asserted band are covered.

## originality

PASS

O’Neill (2023) full open-access primary article constructs the same generalized matching distribution, identifies the monotone single-trial likelihood ratio, discusses the total statistic and mentions vector likelihood-ratio testing. It does not in its inspected Sections 3, 5, 6 produce the precise θ-independent two-game ordering within a tied sum, triangular finite power loss or sparse-skill peak. The Neyman–Pearson lemma is standard and is not claimed as new. Published SCOPE Resultary searches produced unrelated testing refinements rather than this same model.

## value

PASS

The finite-sample exact loss in test power from discarding an observed match-count split is a motivated statistical decision-theory quantity for an explicitly published matching model. The universal first-tie preference, sharp α-profile and sparse-skill coefficient are nontrivial precise facts; neither standard NP optimality nor the existence of a generic likelihood test determines them. The useful theoretical band has comparatively high α and is not a claim of improvement for standard 5% tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
