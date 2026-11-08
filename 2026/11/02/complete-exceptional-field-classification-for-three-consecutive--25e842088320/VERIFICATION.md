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

Order-six character indicator I(y)=1/6 sum_{j=0}^5 (-1)^j chi(y)^j on nonzero y; character expansion of 216N(q) with support size 1,2,3 gives Weil bounds 0,sqrt(q),2sqrt(q) and 15,75,125 exponent triples, hence 216N(q)≥q−108−325sqrt(q)>0 for q≥105841. Actual verify_ns3.py file examined, including complete prime-power list, irreducibility, primitive-element checks and exhaustive negative tests. Independently enumerated all 5037 primes p<105841,p≡1 mod6 and reproduced the 28 prime exceptions, with q25,49,121,169 negative and q289 positive. Other extension cases rely on inspectable verified code/table and earlier checker logs, not falsely represented as independently re-enumerated. Finite enumeration only covers q below analytic bound.

## originality

PASS

Lehmer et al (1962) consider three consecutive cubic residues for prime fields but do not impose nonsquare coset and proper prime powers; Cohen (2026) complete pair classification is weaker than triple. The stronger-looking Zhou–Wu 2026 result proves large-q general nonsquare nonprimitive tuples and limited small-q computations, but its accessible abstract does not establish this exact 35-exception NS3 coset list. Buell–Hudson 1986 power residue sequences is a strong inaccessible possible implication; mark material-read limits and priority risk instead of asserting noncoverage.

## value

PASS

Complete field-order exception list for three consecutive members of a prescribed natural order-six multiplicative coset answers a discrete cyclotomic existence/classification question with an explicit analytic finite cutoff and genuine proper-extension exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
