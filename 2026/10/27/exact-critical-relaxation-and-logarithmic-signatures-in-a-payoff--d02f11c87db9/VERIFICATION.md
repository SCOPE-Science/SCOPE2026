---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Subtracting the mixed-strategy payoffs from the reversed matrix gives (2x−1)[a+(b−a)x]. At 0,1,1/2 the drift derivatives are −a,−b,(a+b)/4. The affine factor has a simple root when nonconstant, so it can create a multiple equilibrium only by coinciding with one of these three; a=b=0 instead makes the drift identically zero. On the indicated endpoint basins u obeys u'=−cu²(1−u)(1−2u), and on the indicated interior basins u'=−cu²(1−4u²). Both have strict decay to zero for 0<u0<1/2: uniqueness precludes finite hitting and no positive limiting zero of the drift lies below u0. The other signs are repelling at the double root or in another basin. With z=1/u, partial fractions give F'=z²/[(z−1)(z−2)] and G'=z²/(z²−4); multiplying gives dF/dt=dG/dt=c on their respective basins. As z→∞, F=z+3 log z+O(1/z) while G=z−4/z+O(z^(−3)); the exact laws first give z/(ct)→1 and then the stated log coefficient and normalized constants. No asymptotic claim is made for fixed-point initial data. The finite checker was inspected, not executed; direct analytic identities and monotonicity establish the claims.

## originality

PASS

The scalar model and the two swept critical thresholds are prior work, and the same source recognizes S=P as degenerate. The supported distinct claim is the complete model-specific one-sided critical time laws, with their log/no-log contrast and initial-data constants. Earlier inspected relaxation records do not give these laws in this model. This is not a general new normal form, separation technique, or equilibrium-discovery claim.

## value

PASS

The two types of collision in the existing model cannot be distinguished by their leading 1/(ct) critical decay. In the physical cooperation coordinate an endpoint trajectory has a growing logarithmic residual in reciprocal distance after removal of ct, while an interior trajectory has a finite residual. That distinguishes the deterministic critical transients and provides exact initial-condition-dependent benchmarks for fitting or numerical comparisons, including the endpoint symmetry and the previously degenerate S=P case. This is a modest quantitative model refinement; equilibrium conditions alone or a generic leading-order critical-slowing exponent would not deliver that comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
