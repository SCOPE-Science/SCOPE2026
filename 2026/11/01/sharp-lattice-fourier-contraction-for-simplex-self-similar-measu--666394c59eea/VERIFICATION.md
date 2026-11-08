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

Independent product factorization from iid digits shows μhat(m)=Πj[1+Σ_i exp(-2πi m_i/b^j)]/(d+1); factor out common b powers to primitive q. The exact identity (d+1)^2−|Σ_{i=0}^d z_i|²=Σ_{r<s}|z_r−z_s|² forces at least d unequal N-th-root pairs and the minimum chord gap 4 sin²(π/b^j), giving each product factor and convergence. Equality for every scale and a sufficiently large N forbidding residue aliasing forces two phase classes of sizes 1,d with representatives differing exactly ±1; yields precisely listed frequencies. Fourier characters diagonalize convolution and attain power contraction. Fresh independent bounded enumeration d=2,3 and b=2,3,4 over integer boxes [-3,3]^d matched every predicted maximizing frequency, with no mask-bound violations; proof, not enumeration, establishes infinite claim.

## originality

PASS

Earlier Li 2007 spectral self-affine measure investigations concern existence of exponential orthogonal bases and compatible pairs (zeros of mask); the current positive nonzero coefficient maximum and its rigid equality classification is logically different. Later Li 2012 and Yuan 2015 Sierpiński spectrality abstracts likewise do not demonstrate coverage; their inaccessible full texts remain priority risks. Resultary searched for equivalence without matching positive-modulus theorem.

## value

PASS

For a canonical simplex self-similar measure, Fourier coefficients directly determine convergence of torus convolution powers and spectral mixing rates. Exact operator contraction and all extremizing characters are a natural unknown invariant, independent of whether the measure is spectral. It is useful even without a general classification of nonextremal frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
