---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The proof partitions arbitrary nonlinear codes by all but one input column; any two last columns at binary distance 1 or 2 give augmented matrices at Hamming distance 2 and confusable single-substitution balls, so each fiber ≤A_2(ℓ,3). A maximum length-ℓ distance-3 parity-row seed supplies that many matrices per prefix, while a length edit identifies its row and all other rows reconstruct it; one substitution is located by odd column parity and corrected through unique row-parity decoding. This handles no edit, parity-row edit, arbitrary nonlinear seeds and n>ℓ.

## originality

PASS

PASS best-of-knowledge for the matching arbitrary-ℓ upper bound; lower-bound construction and ℓ=2 optimality, as well as classical seed sizes, were already published.

## value

PASS

An exact maximum for a natural noisy parity/sum channel closes the published non-tight cardinality interval for general ℓ, with concrete nonlinear length-eight improvement; precise code cardinality is directly used to select error-correcting codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
