---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed the characteristic-2 geometry for F=x²y²+y²z²+z²x²+xyzw. Viewed as linear in w, coefficient xyz is coprime to the other summand, so F is absolutely irreducible. Quadrics [tu:su:st:s²+t²+u²] have no common projective zero and satisfy F=0; the inverse [yz:xz:xy] on xyz!=0 makes the map birational. Fibres over the three singular lines are finite, hence projective quasi-finite map is finite and P² normalization. Partial derivatives are (yzw,xzw,xyw,xyz), and exactly >=2 of x,y,z vanish on the singular support. Chart w=1 yields reduced (xy,xz,yz), while chart x=1 yields (yz,yw,zw,y²+z²), generically (y,z) off w=0; y,z,y²=z² are independent w-annihilated torsion classes of length 3 and all others follow by symmetry. On the dominant source line, lambda=v+v^-1 is separable degree 2, unique characteristic-2 branch v=1 with lambda=h²/(1+h), wild e=2 and different exponent 2 by Riemann-Hurwitz. Projective torus and boundary count (q-1)^2+3q+1=q²+q+2 implies the stated zeta function. Independently derived partials, charts and local Groebner ideals and enumerated GF(2), GF(4), with (surface,singular)=(8,7),(22,13). These finite tests cannot certify algebraic closure or all extensions, which rest on the proof.

## originality

PASS

The base equation, normalization form and classical six characteristic-zero pinch points were known. The qualified original contribution is the intrinsic Fitting/Jacobian embedded length-three defect at each of three characteristic-two points, paired with unique wild branch of each normalization double cover. The full author-hosted classical exposition, a full 2009 moving-plane preprint, and two related published quartic singular-scheme examples were read and compared. Nothing inspected supplies this exact characteristic-two local-algebra theorem. The most directly relevant 1996 and 2012 full journal articles were unavailable: authorized institutional retrieval returned vpn_disconnected; this is an explicit residual priority risk, not affirmative proof of noncoverage.

## value

PASS

The Roman quartic is a standard natural projected Veronese surface. Its characteristic-two exceptional fibre retains the classical three reduced double lines but acquires distinct intrinsic Jacobian torsion at exactly three wild endpoint points. Specifying local torsion length three, its module generators and the different exponent on the normalized double-line covers gives motivated scheme-level information invisible in set-theoretic singularity counts, and is useful as exact data for studying conductor, normalization and degeneration. The zeta function and P² normalization are explicitly treated as context rather than independent novelty. This is not an arbitrary numerical slice or routine invariant lookup; it identifies a concrete structural exceptional-characteristic phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
