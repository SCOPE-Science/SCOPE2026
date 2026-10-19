---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the finite-field exterior-algebra count

Run `python3 verify.py` with the Python standard library. The script implements the exterior-product signs on the eight basis masks, computes the ranks of the full left-plus-right multiplication span, and enumerates every normalized image line in the relevant finite fields. The complete checks cover \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) by prime arithmetic, and \(\mathbb F_4\) via the extension \(\mathbb F_2[z]/(z^2+z+1)\).

For \(q=2\), it separately evaluates the defining weight-zero Rota–Baxter identity on all \(64\) ordered pairs of exterior basis elements for all \(255\times255=65025\) possible nonzero rank-one maps. Exactly \(2689\) pass. The projective image-line counts by ideal rank \((4,2,1)\) are \((112,14,1)\) for \(q=2\), \((351,39,1)\) for \(q=3\), \((5376,84,1)\) for \(q=4\), and \((3875,155,1)\) for \(q=5\). They give operator counts \(2689,58658,1731243,4917844\) respectively. Each asserted integer is obtained by the packaged script.

These finite computations do not establish the formulas for arbitrary finite fields or the dimensions of the corresponding algebraic loci. Those facts follow from the symbolic normal forms and projective bundle dimensions proved in `RESULT.md`. No independent audit has been performed.
