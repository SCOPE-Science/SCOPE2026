---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

Execute `python3 parallel_coset_verify.py` using the supplied standalone file. The program uses only Python's standard library and bitwise XOR, identifying the additive group of \(\mathbb F_{2^m}\) with a binary vector space. It reconstructs each local permutation and the helical sweep independently of the closed forms, verifies the unswapped quantum Yang–Baxter identity, and counts fixed points by direct enumeration for complete small systems. It checks the global-order and affine/non-affine distinct-map census, then extends deterministic checks to \(q=16\). It outputs `VERIFY_OK: assertions = 1760824` after 1,760,824 successful checks.

The exact computed map counts are \(M(4)=16\), \(M(8)=400\); for even site lengths the respective global-order class sizes are \((1,9,6)\) and \((1,147,252)\) for orders \((1,2,4)\). At \(q=8\), exactly \(224\) of these maps are non-affine and \(168\) non-affine maps have even-length global order four. The selected non-affine map with \(d=1\), \(c=2\), and mask supported on the coset \(\{2,3\}\) has \(64\) primitive two-cycles and \(96\) primitive four-cycles at site length two.

**Scope of evidence:** finite enumeration confirms only the tested dimensions and site lengths. The universal theorem for every \(m\ge2\) and every \(N\ge1\) rests on the quotient-coordinate proof and independent-counting argument in `RESULT.md`. No external audit or independent mathematical validation is represented by this record.
