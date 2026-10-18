---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Writing R(e1)=ae1+be2, R(e2)=ce1+de2 and applying the weight-zero Rota–Baxter identity to (e1,e2) yields c²=0, hence c=0 over a field; (e1,e1) then gives a(a−2d)=0, including char 2. The automorphism group follows from φ(e2)=φ(e1)²=s²e2 (s≠0), and explicit triangular-matrix conjugation sends b to sb+(a−d)t/s. The cases a=d=0 give {0,N}, and all remaining branches have a−d≠0 so b may be killed; char2 collapses the 2d branch. This derives complete mutually exclusive normal forms 0,N,P_d,Q_d (char odd), 0,N,P_d (char2), q-dependent class and orbit-size distributions. Independently checked the defining identity and orbit actions for GF2,GF3,GF5,GF7; (operator counts, orbit counts) were (4,3),(15,6),(45,10),(91,14). Exhaustive finite checks are corroboration, not an arbitrary-field proof. Assumes fields, not rings or scheme-point multiplicities.

## originality

PASS

Best-of-knowledge priority judgment based on direct statement/implication comparisons with specified inspected sources, published semantic search and alias checks; neither the source names nor negative searches by themselves demonstrate novelty. Searches covered conjugacy, equivalence under algebra automorphisms, normal forms and characteristic degeneration. The raw family contains the orbit representatives but does not state the equivalence quotient or field-uniform orbit-size result.

## value

PASS

The automorphism quotient and stabilizer distribution of the smallest nontrivial Zinbiel algebra are natural moduli invariants absent from the published complex raw-matrix classification. Characteristic-two degeneration and finite-field counts supply a meaningful all-field classification, not a mere variable change or recomputation of complex matrices; the narrow size is motivated by the first nonzero Zinbiel product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
