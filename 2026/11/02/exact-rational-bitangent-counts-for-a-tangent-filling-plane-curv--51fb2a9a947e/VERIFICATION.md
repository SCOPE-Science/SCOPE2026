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

For q=p^r with p>3, rational smooth points normalize uniquely by x+y+z=1, with xyz nonzero and excluding (1/3,1/3,1/3), giving (q-1)(q-2). The Gauss/tangent map is Gamma=[1/x-3:1/y-3:1/z-3]. Tangent coincidences parametrized by d_v(t)=t+3(1-t)v factor exact contact equation -t(t-1)(At+B). Simultaneous poles when coordinates repeat are removed. Other rational contact exists exactly when distinct x,y,z and AB(A+B)≠0. Centered coordinates u=3x-1 etc decompose singleton set into six disjoint lines (6(q-3)), split conic e(q-4) with e=0/2 according q mod 3, and rational cubic q-5-e, leading S=7q-23+e(q-5), N2=((q-1)(q-2)-S)/2. Exact algebraic symbolic factor and finite-field tangent fibers over eleven primes q=5..41 independently verified. Universal field result follows from algebra, not enumeration.

## originality

PASS

Asgarli–Ghioca introduced this exact curve, its unique singular point and tangent-filling theorem; inspected full source does not state exact dual rational tangent-line numbers, smooth two-contact fiber involution, or mod-3 splitting counts. General bitangent upper bounds do not imply equality or exact contact spectrum. Historical unindexed rational-dual count might exist and should be checked.

## value

PASS

The rational tangent filling property concerns coverage, whereas the size and redundancy of the actual rational line set is an independently natural geometric incidence invariant. Exact singleton-pair involution and arithmetic split by cube roots of unity give an all-prime-power, structural count useful for finite-geometry dual arrangements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
