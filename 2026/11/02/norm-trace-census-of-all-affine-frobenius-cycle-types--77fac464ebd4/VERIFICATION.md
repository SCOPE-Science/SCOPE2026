---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For f(x)=a sigma(x)+b, sigma Frobenius p^r with fixed F_Q and h=m/gcd(m,r), the semilinear linear part L obeys L^h=A id with A=relative norm(a). If A ne 1 then L-I is invertible and translation conjugates f to L; multiplicative Hilbert 90 makes the n-iterate fixed-point count 1+(Q^{gcd(n,h)}-1)1_{ord(A)|n/gcd(n,h)}. If A=1, Hilbert 90 yields L conjugate to sigma and f conjugate to sigma+c; additive Hilbert 90 gives fixed counts Q^d (trace(c)=0) or Q^d 1_{p|n/d} (trace(c) ne 0). Möbius inversion extracts all cycles and orders ht,h,ph distinguish classes, including p dividing h. Norm fibers of size (q-1)/(Q-1), trace fibers q/Q and totient counts prove M_t=q phi(t)(q-1)/(Q-1), M0=(q-1)q/((Q-1)Q) and M*= (q-1)q(Q-1)/((Q-1)Q); total q(q-1) and tau(Q-1)+1 distinct types. Independently implemented F4 and F9 finite-field arithmetic, all coefficient-pair permutations for r=1,2, compared cycle types and type counts to norm and trace classification. Standard Hilbert 90 is an invoked established theorem; finite cases are corroboration, not general proof.

## originality

PASS

General linearized permutation cycle formulas and Ugolini characteristic-two affine dynamics cover substantial cycle-length aspects, and via homogenization a broader general linearized-map theorem might cover the individual affine spectra. The surviving contribution is the all-prime complete norm/trace coefficient-pair multiplicity census and exact type number. Qualified PASS with explicit strong-prior risk from Bian–Chen–Zheng 2026, whose full text was inaccessible.

## value

PASS

A finite-field dynamical system with natural norm/trace invariants obtains a complete coefficient-space classification, not merely a formula for a given map. The number of distinct symmetric-group cycle types and multiplicity of each type are explicit for every characteristic and extension. These exact strata can be reused in finite dynamical and permutation-polynomial enumeration even though many individual cycle computations are covered by general linearized-map theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
