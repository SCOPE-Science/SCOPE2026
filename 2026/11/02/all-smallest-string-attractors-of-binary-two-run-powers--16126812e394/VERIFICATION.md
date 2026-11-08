---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For W=(0^a1^b)^k, a,b positive and k>=2, one selected 0 and one selected 1 are forced; the 01 and internal 10 boundary tests are necessary. For any factor of length >= p=a+b, shifting all occurrences by p gives an interval union spanning [p,N-p+1], hence any marked internal 10 position intersects an occurrence. Short factors are pure run factors (slide to chosen symbol), 10-crossing factors (periodic internal boundary), or 0^u1^v (01 boundary). This proves the four-factor certificate for all lengths, not merely brute-force cases. The boundary intersection sets imply exactly (k-1)(k max(a,b)+1) pairs if min(a,b)=1, otherwise 2k(k-1), with the two disjoint pair families and the listed distance enumerator. Independently enumerated literally all factors and pairs for 48 (a,b,k) triples a,b=1..4,k=2..4; exact counts agreed. Boundary a=b=1 yields k^2-1, already published. No general arbitrary-period claim.

## originality

PASS

Qualified PASS for uniform four-factor exact certificate, both run-length regimes, all optimal pair positions and gap-spectrum polynomial; the alternating singleton-run special case is established prior art and is excluded from novelty. No inspected broader minimum-cardinality theorem logically determines all optimal pairs. Residual risk of an older general periodic-word or binary run-power optimal-set enumeration.

## value

PASS

The simplest variable-run periodic binary words are a natural string-attractor benchmark; their minimum size is already uninformative (two), but multiplicities and possible locations reveal a nontrivial singleton-run phase boundary and run-length-independent 2k(k-1) count when a,b>=2. Complete witness and distance classification is a motivated exact infinite family, not arbitrary small-word tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
