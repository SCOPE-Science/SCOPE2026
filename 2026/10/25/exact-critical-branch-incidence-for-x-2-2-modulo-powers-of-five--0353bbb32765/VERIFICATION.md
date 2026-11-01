---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

On Z/5^k, k>=1, residues 2 and -1 mod5 are periodic disks; 1,3 have depth 1 and 0 depth 2. The p-adic period-lifting lemma for g congruent to identity derivative modulo 5 and displacement valuation >=2 establishes cycle lengths 2*5^(k-t-1) in 2-disk and 4*5^(k-t-1) in -1-disk, with fixed roots 2,-1 and total 3k-1 cycles. On each near-2 valuation shell, the normalized quadratic character epsilon distinguishes the two same-length cycles. Incoming depth-2 roots of z+2 via Hensel have count 5^floor(k/2) at 2, 2*5^(t/2) exactly at even t with epsilon=+1, zero otherwise; no deeper branches. Thus complete rooted graph with multiplicities.

## originality

PASS

Best-of-knowledge original component is branch-by-branch critical depth-two incidence and complete rooted components. Earlier all-degree Chebyshev period counts cover cycle lengths but not placement of incoming nonperiodic trees.

## value

PASS

Classifies a natural nonpermutation Chebyshev/Dickson dynamical system on every prime-power ring, including critical-branch incidence that period counts omit. The distinction between equally long near-2 cycles with and without critical descendants is a mathematically structural finite-ring phenomenon, not an arbitrary small-k census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
