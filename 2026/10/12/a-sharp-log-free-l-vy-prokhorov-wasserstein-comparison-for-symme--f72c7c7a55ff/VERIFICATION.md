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

Geometric series give E|X_r|=2r/(1-r²) and endpoint R_B=B/(1+sqrt(1+B²)). For R_B<=sqrt2-1, differentiating log p_r(k) proves every off-center mass is monotone increasing in r, while center decreases; thus total variation mismatch is exactly center-mass difference. The integer-lattice minimum nonzero distance is 1, so for mismatch <1 the Ky–Fan/Prokhorov coupling infimum is the mismatch probability. One-dimensional W1 is the infinite sum of absolute CDF differences and telescopes to the displayed moment difference. Independently checked symbolic identity of the ratio and monotone boundary maximization. The sharp constant is approached by distinct r,s coalescing at R_B; not necessarily attained by distinct pairs. Source finite verifier inspected, not used to prove all parameters.

## originality

PASS

Best-of-knowledge PASS: Marsiglietti–Pandey prove a logarithmic general bound and explicitly leave removing log open for the unrestricted centered discrete log-concave class. The full paper mentions symmetric geometric laws as reference distributions elsewhere but does not give the exact two-parameter distance formula or its sharp first-moment constant in the inspected text. General coupling inequalities do not determine the optimal constant. Exact discrete-Laplace alias formula may nevertheless exist in earlier distance literature.

## value

PASS

A sharp benchmark in a natural log-affine discrete distribution family addresses whether the general logarithmic loss is forced even in a canonical unbounded family. It supplies an all-budget exact comparison and universal sharp constant within that family, not an unmotivated single pair or an unsupported removal of log for arbitrary discrete log-concave laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
