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

Independence of the current annual matrix from the population history gives E[z_{n+1}]=M_p E[z_n]. Since A is invertible, X=A²B and Y=ABA are similar (Y=A⁻¹XA), and direct multiplication gives their common trace t and determinant δ. For E=X−Y the determinant along Y+pE is quadratic with leading coefficient det E and equal endpoint values, hence det M_p=δ−p(1−p)det E. Also E=A(AB−BA), so det E=−bc det(AB−BA)=J with exactly the listed sign and formula. Every entry of both annual products, and hence of M_p, is strictly positive. Its discriminant is therefore positive and the larger characteristic root is the simple Perron factor. A positive initial vector has nonzero Perron component. Monotonicity of the root in Jp(1−p) gives all three cases and the unique midpoint optimizer in each nonconstant case. All signs are realizable: the frozen witness gives J>0, b=c=e=f=1 and a≠d give J<0, and A=B gives J=0. For the frozen rational example, direct column propagation gives t=7/8, δ=−3/32 and J=9/64. The second eigenvalue is negative throughout, so the Perron root exceeds 1 exactly when det(I−M_p)=1/32−(9/64)p(1−p)<0, i.e. 1/3<p<2/3, with equality at the endpoints. The exact endpoint and midpoint discriminants are 73/64 and 82/64. The independent replay verified characteristic signs on a rational grid; the symbolic inequality proves the full interval.

## originality

PASS

Deterministic cyclic-product equality, general first-moment propagation under independent matrix draws, and the possibility of altered mean growth under vital-rate variation are not new. The supported distinct comparison is the exact sign rule under the constraint of switching only between two cyclic rotations of the same fixed two-age phase inventory, with the whole admissible probability range and an exact subcritical-to-supercritical witness. The inspected related phase-order records change the deterministic schedule, concern pathwise growth, or change the switching model. No covering published claim was established. Full-text access limitations are not negative evidence.

## value

PASS

The natural controlled comparison holds vital rates, seasonal inventory, and both deterministic growth factors fixed. The exact sign rule nevertheless allows annealed growth to rise or fall, and the rational witness isolates the full interval where a genuinely supercritical mean results from mixing two subcritical alternatives. This is a useful exact threshold for phase-sensitive demographic projections, not a claim that randomness generally improves ecological outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
