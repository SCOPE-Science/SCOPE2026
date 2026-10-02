---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The stationary-cone classification argument is coherent. Blow-up of bounded mean curvature gives stationary integral tangent cones of the same density. For a stationary two-cone \(C\), comparison of large balls centered at a nonzero point with balls centered at the vertex gives \(\Theta(C,x)\leq\Theta(C,0)=3/2\). A tangent cone at such an \(x\) splits off the radial line, so the remaining stationary integral one-cone has total ray multiplicity at most three; balancing leaves only density one (a line) or density \(3/2\) (three unit rays at 120 degrees). If equality \(3/2\) occurs at a nonzero point, monotonicity plus the common large-scale limit forces conicality about both centers and hence translation invariance, giving the \(Y\) product. If every nonzero point were regular, the spherical link would be a union of closed great circles with total length an integer multiple of \(2\pi\), contradicting the required length \(3\pi\). Thus every tangent cone is an orthogonal image of \(Y\). The package script checks only elementary identities; the classical GMT inputs remain external hypotheses.

## originality

PASS

Fresh searches found the classical Allard–Almgren structure theorem for stationary one-dimensional varifolds and modern regularity work near polyhedral or triple-junction cones, but no inspected source states the exact arbitrary-codimension classification that every stationary integral two-cone of density \(3/2\) is \(Y\). The final proof is a short structural assembly of standard ingredients rather than a parameter substitution from a stronger located theorem. Originality is therefore best-of-knowledge, with explicit residual risk that the corollary may be known folklore.

## value

PASS

Density \(3/2\) is the first natural triple-junction density for integral two-varifolds. An exact tangent-cone list at that threshold in arbitrary codimension is a motivated structural boundary result that can be used as a clean input in later regularity arguments, even without uniqueness or an epiperimetric rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
