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

# Reproducibility and boundaries

Run `python3 paley17_verifier.py paley17_matching_certificate.json` with Python 3.10 or newer. The script requires only the standard library and validates the externally supplied certificate against its own deterministic reconstruction; it does not trust the listed Morse pairs without checking them.

Verified finite facts: residue set \(\{1,2,4,8,9,13,15,16\}\), exactly \(153\) nonempty faces in dimensions zero through two, a valid complete \(68\)-pair face-poset matching, acyclicity across all \(340\) covers, and a unique unpaired vertex with \(16\) unpaired triangles. The midpoint bijection is verified on all edges and for every affine group element. Signed fixed-simplex computations reproduce the rational character \((16,-1,0)\) on the three indicated classes of affine transformations. Complement-subgroup invariant dimensions \(16,8,4,2\) are checked by averaging.

The certificate is finite and exhaustive for the stated seventeen-vertex graph, and the proof establishes the exact integral homotopy type, not merely numerical mod-prime Betti numbers. Mathematical steps not supplied by computation are the standard discrete-Morse homotopy theorem, rational representation semisimplicity, and rational transfer for finite geometric quotients; their applicability is explained in the proof. No higher-order Paley classification or integral quotient calculation is claimed.

The adjacent primary literature treats broader conference-graph first-homology questions; an unindexed equivalent calculation remains a residual originality possibility. No independent external scientific audit is represented here.
