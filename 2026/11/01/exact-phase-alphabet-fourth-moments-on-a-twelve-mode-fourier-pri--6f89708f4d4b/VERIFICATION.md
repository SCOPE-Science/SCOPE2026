---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Orthogonality applied to P squared gives M=sum_{a in {0,1,2}² x {0,...,4}} |sum_{u+v=a} c_u c_v|², with 45 indices. Scalar and three coordinate-character modulations uniquely set c000,c100,c010,c001 to 1, leaving exactly q^8 arrays, each with q^4 original configurations. Independently implemented exact Gaussian/Eisenstein-lattice convolution enumeration tested all 256+6561+65536+1679616=1,751,969 normalized arrays; obtained minima (220,210,188,196), next attained values (228,216,196,200), and normalized minimizer counts (27,48,6,36), agreeing with source. The source CHECK.py additionally supplies exact orbit-representative reconstruction and an independent difference-correlation identity. On finite tori with each cyclic period strictly larger than the corresponding squared-polynomial degree (m,n>=3,ell>=5), the 45 sum frequencies do not alias, proving transfer for all arrays. Exhaustiveness applies only to finite phase alphabets, not continuous unimodular phases.

## originality

PASS

Best-of-knowledge originality of the exact twelve-mode full-prism table, rather than Parseval or phase gauge. Adjacent published exact results cover genuinely different index sets; no retrieved primary paper yielded this exact full aperiodic array table. No claim of exhaustive bibliographic priority.

## value

PASS

The fully occupied 2x2x3 prism is a natural smallest noncubic three-dimensional rectangular Fourier aperture; minimizing total aperiodic autocorrelation is a standard design objective. The exact winner/gap/orbit table is a genuine nontrivial finite classification for a naturally defined object, not routine normalization. Quaternary alphabet optimal fourth moment 188 beats sextic 196 despite cardinality, a useful explicit warning against assuming unconstrained alphabet-size monotonicity; the no-alias transfer gives rigorous finite sampling applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
