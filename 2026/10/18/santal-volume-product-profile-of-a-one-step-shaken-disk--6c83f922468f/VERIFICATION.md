---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The chord-preserving body has area pi and half-ellipse support h_±(theta)=sqrt(cos²(theta)+(1±delta)²sin²(theta)). Polar area of vertical translate is 1/2 integral 1/(h-c sin(theta))²; splitting semicircles and substitution u=cot(theta) yields I_delta(c) as stated. Positive second derivative of the polar integral and divergent boundary polar area imply unique Santaló c; derivative at 0 makes c>0 when delta>0. Differentiating elementary J(a,c), including special value J(a,-a)=4/(3a), reconstructs local expansion c=8delta/(3pi)+[32(88-9pi²)/(27pi³)]delta³+O(delta^5) and product pi²-(32/3-pi²)delta²+O(delta^4). Independent high-precision quadrature of the split polar-angle integral and of J agrees for delta=0,.25,.6,1 and endpoint product about 8.716345507; symbolic cubic coefficient cross-checked. Global strictness imports Meyer–Reisner reciprocal-polar-volume convexity and affine rigidity along shadow systems; every delta>0 boundary is two distinct elliptic arcs and cannot be a single ellipse, excluding affine plateau. Numeric samples are not substituted for convexity theorem.

## originality

PASS

Kipp–Sagmeister define the exact deformation; Meyer–Reisner imply the qualitative monotone direction from general shadow systems. The surviving original claim is the complete disk-specific polar integral and minimizer, sharp second and cubic variation and exact endpoint, not the existing general convexity theorem.

## value

PASS

The Santaló point and precise Mahler deficit are canonical affine-geometric invariants of a standard one-step symmetrization path. The disk-specific sharp second variation and cubic displacement quantify how much a volume-preserving deformation departs from the extremal disk, beyond the qualitative shadow-system inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
