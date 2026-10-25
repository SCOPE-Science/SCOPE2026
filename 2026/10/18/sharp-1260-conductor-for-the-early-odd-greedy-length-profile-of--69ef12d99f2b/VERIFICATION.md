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

The odd-greedy algorithm on 2/p for primes p>3 preserves parity of reduced numerators, so finite termination occurs at an even number of unit-fraction terms. Explicit least odd denominator formulas transform successive residuals: 2/p ->3/M ->4/D ->5/B; length 2 iff p≡1 mod4, length 4 iff p≡7 mod20. If neither, the 5/B ->6/C branch terminates in six terms iff 3|B (p mod9 in {1,2,4,5}), or if 3∤B then the 6/C ->7/(Cv) branch ends iff 7|C (p≡4 mod7); the quadratic discriminant 6 mod7 excludes spurious B≡1. Remaining length is >=8 or infinite, NOT infinite by claim. CRT on unit residues mod1260 yields counts 144,36,78,30 and natural prime densities 1/2,1/8,13/48,5/48 by PNT in progressions. Four opposite-category same-residue witnesses for 1260/2, /3, /5, /7 plus generalized CRT and Dirichlet show every modulus sufficient on all sufficiently large primes is divisible by 1260. Independent Fractions-based greedy iteration covered each of 9590 primes 5..100000 and all 288 unit residue classes. Finite checks are corroboration, not the infinite proof.

## originality

PASS

Pihko 2001/2010 establish the odd-greedy algorithm and numerators/open termination questions; Louwsma–Martino arXiv:2309.07280/2025 prove two-term odd-greedy characterization. Earlier fixed-horizon congruence-periodicity and four-term criteria are not new. The asserted new content is the exact six-term prime-residue branch and proof that modulus 1260 is minimal, together with four prime densities. Existing broad periodicity does not numerically fix least modulus; no checked full source/table reported these combined exact values.

## value

PASS

The odd-greedy termination problem is open, so an exact bounded-horizon classification for 2/p gives a naturally motivated sharp quantitative boundary rather than unsupported eventual termination claims. The minimal congruence conductor and density profile at the first longer prime stopping horizon supply a reusable arithmetic baseline and support future deeper-step investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
