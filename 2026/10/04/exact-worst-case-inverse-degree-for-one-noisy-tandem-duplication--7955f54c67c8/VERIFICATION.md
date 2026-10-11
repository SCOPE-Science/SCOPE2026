---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The mismatch profile z_t=1[y_t≠y_{t+k}] makes a start legal exactly when its length-k window has weight one. Direct comparison of deletions gives the stated collision criterion. Three representatives of distinct parents cannot lie in k+1 consecutive start positions, yielding the block-packing upper bound. The periodic profile 1,0^(k−1),1 realizes exactly two legal distinct-parent starts per full block and the correct truncated remainder; any such profile is realizable over two symbols recursively along distance-k chains. Fresh independent exhaustive binary checks for fifteen small (n,k) cases reproduced the formula exactly.

## originality

PASS

Tang–Farnoud define and analyze exactly the one-noisy-duplication channel but focus on roots, derived sequences and correcting codes; the inspected complete text does not give a one-step received-word inverse-degree theorem. Exact noiseless duplication sphere formulas use equality windows rather than the audited weight-one mismatch windows and do not imply this packing law. Targeted Resultary searches returned no covering formula. Best-of-knowledge originality therefore passes with the ordinary risk of differently phrased inverse-sphere literature.

## value

PASS

Maximum inverse degree is the exact worst-case uncoded list ambiguity of the one-noisy-duplication channel, directly relevant to list decoding and sphere-packing interpretations. The theorem resolves the invariant uniformly over all alphabet sizes, duplication lengths and parent lengths with a sharp construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
