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
# Verification

The argument was checked at three levels.

First, the published area formula for width-one regular Reuleaux \(n\)-gons was materially inspected in Firey's paper. Its expression simplifies exactly to
\[
\frac{\pi}{2}-\frac n2\tan\!\left(\frac{\pi}{2n}\right).
\]

Second, the central-symmetry geometry was reconstructed independently. At every normal perpendicular to a reflection axis, reflection symmetry gives equal opposite support values and constant width makes each equal to \(w/2\). The corresponding \(n\) strips intersect in the regular \(2n\)-gon whose vertex set is \(\{\pm v_j\}\). This proves both containments needed for equality with the centered symmetric hull.

Third, `verify.py` was executed from the packaged path. It checks all odd \(n\) from \(3\) through \(101\), verifies the strip inequalities at every vertex, the inradius and polygon-area formula, Firey's algebraic simplification, the Estermann ratio, and strict numerical monotonicity. It returned `VERIFY_OK`.

The finite checker is not used to prove the infinite family. It only verifies indexing and algebra. The proof of minimization and containment is symbolic.

The result does not address Estermann extremality among irregular Reuleaux polygons.
