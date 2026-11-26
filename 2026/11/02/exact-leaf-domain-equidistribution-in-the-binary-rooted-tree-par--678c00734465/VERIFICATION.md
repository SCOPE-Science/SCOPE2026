---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Here terminal means the ambient bottom level B_n, not all leaves of the domain subtree. Prefix closure and a root-to-root isomorphism give the unique first-level partial injection and child maps in RESULT.md 33–50. An independent reconstruction marks every bottom vertex v by its own variable x_v in a square-free domain generating polynomial. Adjoin one formal empty map of weight 1. If X,Y are the augmented child polynomials in disjoint variable sets, the ranks 0,1,2 of the first-level partial injection give the parent polynomial 2+2(X−1)+2(Y−1)+2(X−1)(Y−1)=2XY: the first 2 counts the empty map and root-only map. This holds for every shape and every mask because the two variables sets are labeled by the domain children, and their injections into image children give the coefficient 2. At height zero the augmented polynomial is 1+x_root. Iteration gives c times the product of (1+x_v), c=2^(2^n−1), and removing the formal empty map gives the claimed exceptional constant term. Setting every x_v=t gives H_n(t). Normalization produces the stated probability: relative to uniform masks the empty mask alone has a deficit, of (2^b−1)/(2^bN), giving the exact total variation, including b=1. The data-processing inequality under the map to size and any subsequent normalization gives the LLN and CLT from Bin(b,1/2). For d≥3 the rank-one and rank-two counts d and d(d−1) differ at height one. Independent bounded replay: python3 /workspace/branches/independent_math_checks.py. It enumerates distinct full-automorphism restrictions to prefix-closed domains and checks every mask at heights 0–3 (1,7,127,32767 maps). All rooted partial isomorphisms extend locally by completing each partial bijection of children, so that enumeration is exhaustive in that range. The uploaded verifier was inspected, not run; the proof, not finite enumeration, establishes all heights.

## originality

PASS

The supported distinct claim is shape-independent multiplicity for every prescribed bottom-level domain, with an exact one-mask correction, not the old partial-wreath construction, total order, first moment, full-domain automorphism count, or ultimate-rank theorem. The inspected results do not subsume the set-resolved identity. The probability formulas follow from that identity and are not independent priority claims.

## value

PASS

This is a natural distribution on which leaves a random partial automorphism actually defines. The mask multiplicity collapses despite the large variety of incompatible rooted-tree shapes, and the exact law differs from independent fair bits only by removal of one empty map from the augmented uniform model. This clarifies why many leaves are defined even though the ultimate rank may be small, and the height-one failure beyond the binary case explains why the law is not a generic wreath-power statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
