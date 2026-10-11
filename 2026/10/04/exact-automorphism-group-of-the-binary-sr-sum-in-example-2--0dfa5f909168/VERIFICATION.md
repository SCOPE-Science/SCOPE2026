---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

After deleting the duplicate generator row, the nine columns have multiplicities 4,2,2,1 for types a=(1,1,1), b=(1,1,0), c=(0,1,1), d=(0,1,0). Any coordinate automorphism of a full-rank generator satisfies \(AH=HP\) for a unique \(A\in GL(3,2)\), so A preserves the column multiset. Multiplicities force a and d fixed and permit only fixing or interchanging b,c. Since b,c,d are a basis and a=b+c+d, these choices give exactly two row actions. Each supports \(4!2!2!=96\) coordinate bijections, yielding 192. The nontrivial action swaps the two size-two classes, giving \(S_4\times((S_2\times S_2)\rtimes S_2)\). A fresh independent enumeration of all 168 matrices in GL(3,2) found exactly these two multiset preservers; the frozen verifier independently exhausts all 9! coordinate permutations and the source-generated subgroup.

## originality

PASS

Kwiatkowski's full source explicitly exhibits the \(S_4\) repeated-column symmetry, the componentwise factor symmetries, and the factor transposition for this exact example, but does not determine the full automorphism group, its order, or the coordinate-orbit decomposition. Resultary search by the exact example, parameters, order 192, and wreath-product type found no prior covering statement.

## value

PASS

The source itself raises the natural symmetry question by showing that the obvious componentwise subgroup is not the full automorphism group. Determining the exact group, orbit decomposition, and proving that the displayed symmetries already generate everything closes that finite structural question and provides a precise benchmark for SR-sum automorphism phenomena.

The dated certificate retains the supplied scientific assessment, sources and limitations.
