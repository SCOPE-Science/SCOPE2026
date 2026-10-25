---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For integer trace t>=3 and q>=2 equal-width vertical coordinate bins, invertible toral dynamics preserve Haar. Every pair of observation coordinate row vectors has nonzero integer determinant via the recurrence a_(h+1)=t a_h-a_(h-1), so pair maps push Haar to independent Haar. Conditional on first two bins the fractional parts U,V are iid uniform, giving C2=t C1-C0+floor(tV-U) mod q; exact strip integration assigns endpoint probability 1/(2t), interior 1/t. The root-of-unity Laurent generating polynomial (1+z^-1)sum_{j=0}^{t-1}z^j/(2t) vanishes on all nontrivial qth roots precisely for q=2 or q|t. Haar central inversion kills the third signed moment of every distinct-time binary triple, and pairwise independence then implies all three-bit uniforms. CMI equals log q-H(w); for q>=t+1 all nonzero residues distinct, yielding log(q/t)-(log 2)/t. Independent rational polygon clipping checked 270 strips t3..22, and all 720 tested t,q pairs passed; unrestricted proof is Fourier/covering, not finite extrapolation.

## originality

PASS

Best-of-knowledge comparison across named aliases, original statements and implications supports a distinct result; see four checks and residual risks.

## value

PASS

A sharp arithmetic threshold and exact conditional-information defect for coarse-grained deterministic hyperbolic dynamics makes a natural boundary between pairwise and triple independence. The striking unrestricted binary three-time property and exact high-resolution log information law provide useful examples for symbolic dynamics and sensor quantization without claiming Markov coding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
