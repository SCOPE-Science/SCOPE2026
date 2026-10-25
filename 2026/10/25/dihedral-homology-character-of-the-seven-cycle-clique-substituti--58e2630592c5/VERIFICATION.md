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
# Reproducibility and scope
Run `python3 checker.py` with Python 3 and no additional packages. For \(q=2,3,4\) it enumerates every simplex, constructs the complete integral incidence combinatorics and ranks boundary matrices over \(\mathbb F_2\), checks signed chain traces of a generator rotation and reflection, and solves the irreducible character count constraints.

Expected output gives f-vectors \((14,56,56)\), \((21,126,189)\), \((28,224,448)\) and rational predicted Betti ranks \((1,1,14)\), \((1,1,84)\), \((1,1,252)\). The checker is finite and does not certify integral torsion or all parameters: the proof's integral chain direct sum supplies the infinite and torsion statements. The characteristic-zero character computation uses the signed simplicial chain action, never an identification of mod-two traces with signs.

The module decomposition holds only for the natural \(D_7\) action on layers fixing clique colors and for integer \(q\ge2\). No external audit or independent validation has been performed.
