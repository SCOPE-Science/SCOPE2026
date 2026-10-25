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

With the convention A(a,b)=⟨g,M_bT_ag⟩, for a≠0 the exact expansion is ω^-a³[sum_j ω^{-3aj²+(3a²+b)j}+t(1+ω^{ab})]/K. The quadratic Gauss evaluation gives ε_pχ_p(-3a)√p ω^{(3a²+b)²/(12a)} with ε_p=1 or i depending on p mod4. Writing 1+ω^{ab}=2C ω^r, r=ab/2 mod p, forces for p≡3 mod4 an imaginary iω^E unable to be real (odd p), and for p≡1 mod4 the congruence E=(9a⁴+b²)/(12a)=0 plus strict χ(-3a)C<0, with unique t=√p/(2|C|). At a=0, normalized ambiguity is 1 (b=0) or t(t+2)/K>0 (b≠0). Independent modular enumeration p=5,13,17,29,37 reproduced 0,0,8,16,36 candidate zero pairs; p=17 shows exactly two distinct amplitudes with four pairs each and direct complex ambiguity sums vanish at their corresponding locations. The Fourier diagonalization of the p² Gabor projector Gram matrix has eigenvalues proportional to |A(a,b)|², so exactly four zero coefficients give linear tomography rank p²−4. Zero ambiguity is NOT claimed to exclude rank-one phase retrieval. The all-prime result is the Gauss identity/phase reasoning, not finite floating comparisons.

## originality

PASS

Best of knowledge after inspection of specified pinned source and actual primary literature. Time-frequency conjugation or chirp normalization does not convert a degree-three chirp into quadratic Chu generally; a prime-dependent quadratic Gauss phase enables cancellation only in p≡1 mod4. The new contribution is the explicit all-prime resonance criterion and first rank defects; generic Fourier/Gauss tools are acknowledged prior art.

## value

PASS

A cubic phase window plus one physically natural real positive impulse is a concrete linear tomography design family. The exact arithmetic amplitude set identifies zero-free regimes on all p≡3 mod4 primes and the first genuinely exceptional p=17, a sharp finite defect for the same design; this is a motivated exact invariant distinct from generic Gabor sufficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
