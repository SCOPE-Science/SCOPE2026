---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Parseval for (a+bz+cz²)^4 gives nine Fourier coefficients. I independently expanded the exact eighth-moment polynomial in A=|a|²+|c|², B=|b|², R=|ac| under aligned phases and verified all thirteen monomials in the displayed identity. Each R coefficient is nonnegative and the nonzero-variable derivative strictly positive, so for fixed A,B equality forces endpoint magnitudes equal, R=A/2. A two-term boundary has at most (8 choose 4)/16=35/8, below the interior candidate. The one-variable ratio Ψ(t)=(70t⁴+560t³+420t²+56t+1)/(1+2t)^4 has Ψ′=−24(35t³−21t−2)/(1+2t)^5, with a unique positive root and global maximum, giving K8^8=13.787723967226... and all phases satisfying arg a+arg c−2arg b=0. Independent symbolic resultant equals 891 times the claimed cubic in K8^8; exact factor and root cases checked analytically.

## originality

PASS

Best-of-knowledge original: first complete unrestricted three-coefficient Λ(8) constant and equality classification for {0,1,2} in the reviewed records. Earlier Neuwirth Sidon theorem optimizes ℓ¹→L∞ and fixed amplitudes; the 2026 phase-only theorem keeps coefficients unimodular, whereas the maximizing t≈0.8184 is nonuniform. Earlier Λ(p) structure does not compute this finite exact norm. No earlier broader moment theorem implying this p=8 value was found in the actual Resultary and primary comparisons.

## value

PASS

The consecutive three-character space is the canonical degree-two analytic polynomial; its first nontrivial eighth-moment sharp constant and unique coefficient/phase orbit give a natural exact Nikolskii/Λ(8) invariant. Deriving a rigid nontrivial amplitude ratio is more than a routine Parseval identity or table recomputation; the precise equality class is independently useful in finite-dimensional Fourier optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
