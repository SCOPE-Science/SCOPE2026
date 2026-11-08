---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Prime cyclic Fourier nonvanishing-minors theorem applies to f and chirp-weighted f, giving each transform at most s−1 zeros when original support size s. A putative triple support ≤13 would provide zero subsets U,V with |U|+|V|=s+1 and each <=s−1; a nonzero vector in the kernel of the (s+1)×s stacked Fourier/chirped Fourier row matrix follows. Since 1009 prime and 105^7≡1 mod1009 with 105≠1, the substitution ω→105 is a valid ring homomorphism from the cyclotomic integer ring. Full column rank modulo1009 witnesses a nonzero cyclotomic minor over C. The exact exhaustive checker ranges all s=1..7, all s-subsets S and all admissible U,V; an independent, differently implemented finite-field row-elimination reproduces 149793 full-rank matrices, per-s counts 0,0,15435,51450,56595,23324,2989, zero defects. The empty s=1,2 test collections are vacuous, not failures. For f=delta0−delta1 Fourier zeros k=0 and chirp-Fourier k=1 prove supports (2,6,6). Finite exhaustive rank verification establishes exactly this finite-dimensional universal predicate for arbitrary complex coefficients, not larger dimensions or all basis triples.

## originality

PASS

Best-of-knowledge originality PASS after searches and real statement-level primary comparisons; no source found to imply the exact final claim. Explicit historical/inaccessible-source risks remain: A stronger lemma in the inaccessible 2026 complete-basis paper might imply the specified 14 bound even though its published global total does not; this is not claimed impossible.; Only a particular triple in dimension seven, no other triples, higher primes, approximate or equality-orbit classification.

## value

PASS

Three mutually unbiased measurements on a natural prime-seven system have a sharp support uncertainty that ordinary pairwise Tao inequalities do not settle (their generic triple floor is 12). The excluded total 13 is a genuine joint-zero obstruction and the finite exact certificate solves a natural focused question identified as open research direction in the primary MUB literature. No need for paper-sized or all-prime theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
