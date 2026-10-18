---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For Borovikov F_M(z)=z+i(M−1)2/pi Arg((1−z²)/(1+z²)), Re F_M(x+iy)=x. For a positive real target x, the non-real preimages occur as conjugate pairs at y>0 satisfying m=M−1=mu_x(y)=y/g_x(y), with g_x=(2/pi)arctan(4xy/[1−(x²+y²)²]). Limits mu_x(0)=pi(1−x^4)/(8x), mu_x(sqrt(1−x²))=sqrt(1−x²) are boundary limits only. Reconstructed differentiation p(z)=z/(1−z^4), g_x=−8/pi Im p prime(z), and algebraic sign factor (5−2 Re z^4−3|z|^8)Im(z^4)/|1−z^4|^4, strictly positive prefactor inside disk; sign changes at y=x. H=g−y times derivative(g) rises and then falls, so mu initially rises and has ≤1 maximum; at most two positive heights and at most five distinct fiber points. At boundary boundary derivative of g=2/(pi x), H(b)=1−2b/(pi x) yields xc=2/sqrt(pi²+4), mc=pi/sqrt(pi²+4). Below mc endpoint ordering forbids two crossings and a continuous witness provides one; above mc the perturbation around x with mu_x(0)=m and boundary/peak sign gives two distinct interior crossings. Numerical root witnesses at m near and above threshold are corroboration only. At mc no boundary preimage is counted. Negative and zero target fibers only have real preimage due to imaginary correction sign.

## originality

PASS

Borovikov 2026 supplied identical F_M and the Landau-radius/nonunivalence question. A radius or vanishing Jacobian theorem does not imply exact 3/5 count of complete REAL fibers, all M>1, and a sharp threshold ≈1.84356. However original preprint full text was inaccessible; no negative whole-paper novelty claim is made. Bound is best-of-knowledge with high-priority overlap risk.

## value

PASS

Classifies exact maximum distinct real-target fiber valence across the full one-parameter bounded-harmonic Landau-shear family and isolates a sharp geometrically interpretable phase threshold. Neither sharp univalence radius nor a local Jacobian criterion provides full-fiber count; the unimodality lemma is a reusable analytic method for noninjective harmonic shears.

The dated certificate retains the supplied scientific assessment, sources and limitations.
