---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For inactive hub and r>=3, the rim response reduces to the indicator of zero active rim neighbors, hence the active rim is a maximal independent set with cyclic gaps 2 or 3. The number with k active vertices is M_m(k)=m/k*C(k,m−2k), 0 outside m/3<=k<=m/2; hub inactive forbids exactly k=r. Active hub gives all-inactive rim, plus all-active special case m=r=3. For r=2, rim equations over F2 are x_(i−1)+x_i+x_(i+1)=1−h, yielding x_(i+3)=x_i and 3-period classifications; hub conditions generate stated indicators. Unique equilibrium occurs precisely at m=7,r=3 after checking all possible independent set sizes. Perrin recurrence and dominant root yield asymptotics r fixed≥3; r=2 bounded. Independent exhaustive Nash action enumeration for every m=3..12 and r=2..m+2 agrees.

## originality

PASS

Klimm–Stahlberg and Gilboa–Nisan/Gilboa prove general complexity for picky or nonmonotone binary response functions, not an exact wheel spectrum. Perrin enumeration of cycle maximal independent sets is classical and explicitly subtracted/filtered by strategic hub compatibility. The new modular r=2 spectrum and unique eight-vertex exception are not implied by the general complexity classification.

## value

PASS

A natural complete graph-family equilibrium classification under a nonmonotone public-goods rule, exposing a qualitative transition between bounded and exponential multiplicity and a unique-equilibrium parameter pair. It adds hub strategic constraints to the classical Perrin independent-set count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
