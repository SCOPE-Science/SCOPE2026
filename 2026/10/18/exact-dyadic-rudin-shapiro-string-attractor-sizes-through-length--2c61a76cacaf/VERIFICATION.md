---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The claim fixes ordinary binary Rudin–Shapiro r_i as the parity of overlapping 11s in binary i, positions one-based, and ONLY N=128,256,512,1024. Independently enumerated all distinct factors and their complete interval-union masks from freshly generated words: 7008,28128,112608,450528 factors, and precisely 48,64,80,96 inclusion-minimal coverage masks. Canonical sorted-hex SHA256 digests of independently regenerated masks were a6544128ca3c04bbb8038882ddb3d427ab5840e81ea38e24b0c32034ec550ece, 004167c859ab00d91a6bb72c545e8c3da3c221b2cfaf4b3dc222e875e4b40a0c, 26917b5a15caa29863b6240919b91f5aef52eff32fbc0095422d75e47f3c6198, 78aaa4b7a10ab9d14f25befcb694142b1ac44062eb79699b810fc637f27704b4; independently SHA256-hashing fetched certificates.json masks gave the IDENTICAL four digests. An independently coded JS BigInt certificate check verified all listed 10/11/12/12-point witnesses hit EVERY mask and integer incidence-duals achieve lower bounds 9/10/11/12, with multiplicities 1/1/2/2. Independently coded exhaustive exact-cover recursion, restricting equality-to-dual and satisfying additional core coverages, found NO smaller 9/10/11 solutions (27,2194,1278 memo states under different pruning), while at 1024 dual=upper=12. The recursion branches on each uncovered positive-dual coverage with exact feasibility pruning and keeps undominated incidence options, proving those three finite exclusions, not relying on a solver log. Four exact finite minima survive; no infinite-word claim.

## originality

PASS

Best-of-knowledge primary-statement comparison plus actual Resultary query, checked exact and broader implications, and explicit residual source-access risk. The novelty is the substantive stated result, not a theorem inferred merely from negative search.

## value

PASS

The next four consecutive dyadic Rudin–Shapiro prefixes after the prior exact results through 64 are natural benchmark instances of the canonical compression invariant gamma. Their sharp values 10,11,12,12 improve the nearest published summary upper bounds 12,13,15,16, exposing a non-obvious 512-to-1024 plateau; the independently checkable exact hitting-set certificates are useful precisely for those benchmark lengths. This finite result merits value without an infinite asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
