---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Direct triangular matrix multiplication gives (C²)_{ij}=(H_i−H_{j−1})/i for j≤i, T_{ii}=(1−1/i)², T_{ij}=(H_i−H_{j−1}−2)/i for j<i; rows sum 0. The offdiagonal positive region is an initial segment j≤k_i at threshold H_i−H_{j−1}>2; absolute row sum equals 2(1−1/i)²+2k_i/i(H_i−H_{k_i}−1). Let P_i=k_i(H_i−H_{k_i}−1). On passing i to i+1 at most one new index crosses threshold since harmonic adjacent gaps ≥1/i exceed δ=1/(i+1); setting ε=2−(H_i−H_k) gives i(P_{i+1}−P_i)−P_i=k(ε−δ)+i(δ−ε)_+≥0 casewise. Hence P_i/i nondecreasing, diagonal increases strictly, so last row alone maximizes for n≥2. Harmonic expansion yields k_n=e^(−2)n+O(1), norm=2+2e^(−2)−(5−e^(−2))/n+O(n^(−2)); O(1) rounding cancels at the stationary point q=e^(−2). Infinite ℓ∞ norm sup finite row sums. Independent rational direct multiplication and exact row norms for every n<60 plus separate large-n asymptotic tests corroborate proof but not infinite quantifiers.

## originality

PASS

Aliases included twice-iterated Hardy averaging defect, second Cesàro deconvolution, squared Hausdorff operator; searched works do not state the exact row threshold or 1/n correction. No broader theorem inspected implies the fine exact n-dependent positive-threshold formula and 1/n coefficient. The exact piecewise harmonic threshold and strict row ordering require new analysis, not a routine substitution of known first-defect norms. Best-of-knowledge priority assessment with listed risks, not certification.

## value

PASS

The second iterative defect of the elementary Hardy/Cesàro averaging operator is a natural de-averaging stability quantity. The exact finite-section formula, unique last-row extremizer, monotonicity and sharp 1/n error determine an unknown endpoint norm that cannot be inferred from the first-defect bound by submultiplicativity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
