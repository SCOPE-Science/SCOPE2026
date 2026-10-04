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

The claim is proved analytically; there is no finite search, numerical certificate, or external computation on which the universal statement depends.

The following checks were reconstructed directly from the packaged proof.

1. For a segment \(UV\) of length \(\ell\), direct one-dimensional integration of \(1/|P-Q|\) gives
   \[
   \int_{UV}\frac{ds}{|P-Q|}=\log\!\left(\frac{PU+PV+\ell}{PU+PV-\ell}\right).
   \]
   The denominator is positive whenever \(P\) is not on the segment.

2. For exterior \(P\), the area integral defining \(E(P)\) is absolutely convergent. Componentwise divergence theorem applied to \(Q\mapsto |P-Q|^{-1}\) therefore gives the exact boundary expression \(E(P)=n_aJ_a+n_bJ_b+n_cJ_c\).

3. For a nondegenerate triangle, \(a n_a+b n_b+c n_c=0\), because these three vectors are the common quarter-turn of the three directed edge vectors of the closed polygon.

4. Nicollier's equality is equivalent, after taking logarithms, to \(J_a/a=J_b/b=J_c/c\). Combining this with item 3 forces \(E(P)=0\).

5. If \(P\) is exterior to the compact convex triangle, strict separation gives a unit vector \(u\) with \(u\cdot(P-Q)>0\) for every \(Q\) in the triangle. Hence \(u\cdot E(P)>0\), contradicting item 4.

The argument proves exactly the stated exterior nonexistence. It does not rely on the numerical location of the interior gravitational center and does not prove any broader polygonal analogue.
