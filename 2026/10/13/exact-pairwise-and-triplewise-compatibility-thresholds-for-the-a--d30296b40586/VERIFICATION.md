---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Adjoint zero-temperature damping sends X,Y to sqrt(q) X,Y and Z to (1-q)I+qZ with C_- = q|1><1|, q in [0,1]. For XY, dual trace witness using eigmax(aX+bY)=sqrt2 forces sqrt(q)<=1/sqrt2; H_ab=[I+a sqrt(q)X+b sqrt(q)Y]/4 is positive iff q<=1/2. For XZ and YZ any lower Z branch splits rank-one qP so 2x2 determinant positivity implies t<=(1-q)/2 and t>=(3q-1)/2, forcing q<=1/2; explicit F_a,+=[Z_++a sqrt(q)X]/2 and F_a,-=qP/2 suffice. For triple, G_ab,+= [Z_++a sqrt(q)X+b sqrt(q)Y]/4, G_ab,-=qP/4, with nonnegative determinant iff q<=1/3. Necessity: average any hypothetical parent by pi/2 rotational covariance fixing Z, producing equal qP/4 lower branch, filter positive Z_+ for q<1, leaving unbiased XY pair with sharpness sqrt(q/(1-q)); trace witness forces q<=1/3. At q=1 original XY pair already impossible. All equality endpoints handled; conclusion only Pauli triad, not channel-wide incompatibility-breaking.

## originality

PASS

Full Heinosaari–Kiukas–Reitzner–Schultz paper covers incompatibility-breaking channels and white-noise, not the exact Pauli triad under nonunital damping; Kiukas–Lahti–Pellonpää examines related open-system/dephasing compatibility, not this exact three-versus-two threshold. Broad 2026 Chitambar–Zhang zonoid theorem is highly relevant but only abstract was accessible; no assertion it does not cover this specialization. Best knowledge no established exact q thresholds elsewhere, with meaningful residual priority risk.

## value

PASS

Pairwise versus triplewise joint measurability is a physically motivated Specker nonclassicality test. The exact nonunital amplitude-damped thresholds identify a sharp, operationally realizable time window with all pairs compatible and triple incompatible, together with explicit parent POVMs and proof of impossibility; not a generic channel-wide claim or a tiny arbitrary constructed example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
