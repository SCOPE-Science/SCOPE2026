---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Reconstructed inclusion-exclusion 15! S(x,15), odd-even split and the independent modular base certificate M_10=sum_{j odd}C(15,j)(j^{2^10}-1)=2^22 mod 2^23. The recurrence d_{n+1}=2d_n+d_n² forces nu2(M_n)=n+12 (n>=10); high-order binomial remainder ensures odd difference nu2= n+12+nu2(a-b). The even j=2,6,10,14 group has coefficient sum 8128=64*127 mod128, giving nu2(E)=b*2^n+6. Dividing by 15! valuation11 yields distinct-scale minimum and +1 resonance cancellation. Independently verified 21 non-resonant modular examples at n=10,11,12; no finite sample substituted for the induction and LTE.

## originality

PASS

The 2014 Zhao–Zhao–Hong Stirling-difference formulas cover non-Mersenne k and small Mersenne k=3,7 and special adjacent steps, explicitly leaving the general two-parameter first omitted Mersenne k=15 case. This two-scale formula for arbitrary a>b, with sharply distinct competing terms, is not stated in the inspected primary treatment.

## value

PASS

First omitted Mersenne block count and asymptotic stabilization for all fixed nonadjacent pairs are a natural motivated 2-adic boundary. The exact two-scale valuation off resonance and positive resonance bound are structurally informative, not simply a selected computation; incomplete exact resonance is transparently delimited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
