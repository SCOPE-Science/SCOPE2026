---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The current McCormack–Zelinsky arXiv version (v4) uses Conjectures 46 and 47; v1 uses 47 and 48 for the same assertions. I independently read the finite certificate and checked the arithmetic in /workspace/replay_3.py using exact integers and rationals. The only primes dividing 47058 are 2,3,11,23,31; their product is 47058 and 1+23529+15686+4278+2046+1518=47058. Thus the reciprocal sum equals 1, satisfying both the primary and weak-primary definitions. The eight pairs with smaller members 1,2,3,22,23,31,33,93 have products 47058 and 16 distinct entries; their pair totals are 47059,23531,15689,2161,2069,1549,1459,599, summing to 94116. The divisor set is complement-closed and sums to twice 47058. This witness is different from 6 and disproves both conjectures. No exhaustive classification or minimum claim is required.

## originality

PASS

The primary-pseudoperfect status of 47058 is old. The novel supported ingredient is the exact strongly pseudoperfect witness for that same number and consequent counterexample to both uniqueness conjectures. The directly relevant pre-record literature and strongest distinct indexed results inspected do not supply that conjunction or imply it in their stated regimes.

## value

PASS

An exact, short witness for a known natural integer decisively settles two named conjectures in the negative. Its value is the refutation, not recomputing a listed primary pseudoperfect number or enumerating a slice of divisor sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
