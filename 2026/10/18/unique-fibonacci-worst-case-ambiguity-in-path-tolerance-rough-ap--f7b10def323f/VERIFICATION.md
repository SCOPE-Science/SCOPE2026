---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the labeled reflexive path with the same relation for both approximations, the endpoint output classifies a two-bit window as 00, 11, or mixed; the interior output classifies a three-bit window as 000, 111, or mixed. Fixing the two-bit states determines every compatible extension; checking the six nonconstant triples gives precisely M_*. The product accepts exactly the inputs for the target word, including unattained words and the empty product when n=2. For n>=3, after the first interior symbol the state vector is at most (1,1,1,1), attaining it only for an all-star prefix. The upper envelope s_k=(F_k,F_{k+1},F_{k+1},F_k) propagates since s_k M_*=s_{k+1} and a forced symbol kills both mixed coordinates. Each incoming state contributes to exactly one mixed coordinate of M_*, so any strict deficit reduces the next mixed total and cannot vanish. At the final endpoint a forced symbol accepts at most F_{n-2}, strictly less than 2F_{n-1}, while a star attains 2F_{n-1} only after all stars. Independently, the first and last runs must be singleton and the remaining runs have lengths 1 or 2, giving F_{n-1} compositions per initial bit. The n=2 outputs are 00, 11 and ** with counts 1,1,2. This proves the transfer count and the unique fully uncertain maximum for all n>=2.

## originality

PASS

The contribution is the exact, efficient path-fiber transfer and unique worst-case fiber, not the rough-set construction or the number of distinct outputs. The earlier transverse-read exact result does not imply either path claim. A later forest-wide theorem is genuine stronger coverage of the extremum and an alternate all-fiber count; the later catalogue date is not evidence that an earlier theorem already covered the frozen result. The exact four-state transfer remains a useful path-specific representation.

## value

PASS

Worst inverse ambiguity is a natural measure of information lost by the rough approximation map, genuinely distinct from counting its image. The result identifies an exact extremal output and exponential rate for all path lengths, proves strict rigidity, and supplies a compact algorithm for arbitrary output words, including impossible observations. That is a useful baseline for more general graphs and a sharper answer than a path image census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
