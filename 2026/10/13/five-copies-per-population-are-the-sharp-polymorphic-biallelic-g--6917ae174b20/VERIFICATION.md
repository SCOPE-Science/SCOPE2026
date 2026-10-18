---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Set d=|a-b| and t=|a+b-m|. Direct expansion of p=a/m,q=b/m yields H_T-H_S=d²/(2m²), H_T=(m²-t²)/(2m²), 1-H_S=(m²+d²+t²)/(2m²), hence G_ST=d²/(m²-t²), D=2d²/(m²+d²+t²). For fixed d>0 the first increases and second decreases with t. Independent rational enumeration of all strictly polymorphic pairs m=2..5 modulo population swap and joint allele exchange proves no strict reversal m<=4 and unique m=5 pair (1,2) vs (2,3), indices (1/21,1/15) vs (1/25,1/13). At m>=5 first pair (1,2) and a central adjacent pair have same d=1 and strictly separated t, proving persistence for all m, not merely finite checks.

## originality

PASS

Best-of-knowledge PASS: Jost 2008 already proves generic G_ST misranking and defines D using heterozygosities; Meirmans–Hedrick 2011 surveys the relationships. Jost’s full author-uploaded text (including eqs 9–11, comparisons and examples) does not state the polymorphic biallelic denominator-five first strict reversal, uniqueness and fixed-gap t-antimonotonicity classification. A generic misranking theorem with multi-allelic examples does not imply the exact first strictly polymorphic two-population rational grid. Prior general misranking expressly credited.

## value

PASS

PASS: These widely used population differentiation indices can contradict on an exact finite two-population biallelic frequency grid; identifying the first physically admissible common count and all boundary pairs plus a structural infinite persistence theorem provides an independently useful natural comparison invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
