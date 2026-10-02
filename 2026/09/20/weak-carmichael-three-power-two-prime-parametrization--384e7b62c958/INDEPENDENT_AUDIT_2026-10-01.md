# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-384e7b62c958`

## Correctness — PASS

Starting from the weak-Carmichael criterion, the two nontrivial divisibilities reduce to \(p-1\mid Aq-1\) and \(q-1\mid Ap-1\). Setting \(d=p-1\) and \(k=(Ap-1)/(q-1)\) gives \(1\le k\le A-1\) and the three displayed divisibility conditions; the implications reverse, so the parametrization is bijective. The divisor bound gives the stated finite bounds for \(p\) and \(q\). The \(a=2\) divisor list leaves exactly the two prime pairs shown. For fixed \((p,q)\), dividing a known solution by its congruence conditions gives a single exponent residue class modulo the lcm of the two multiplicative orders. The inspected exact-integer verifier corroborates the small-exponent classifications but is not used as the general proof.

### Correctness sources

- assigned RESULT.md
- Meštrović arXiv:1305.1867 full accessible text
- artifacts/verify.py
- later fixed-support exponent-lattice theorem

### Correctness risks

- The theorem has two non-3 primes only to the first power.

## Originality — PASS

Meštrović's 2013 primary paper supplies the weak-Carmichael Korselt criterion, tables, and fixed-support exponent facts, and a later 2026-09-21 result gives a broader lattice description for varying exponents on fixed prime support. Those ingredients cover the periodic-lifting viewpoint conceptually, but they do not supply the audited fixed-\(a\) finite divisor parametrization or cutoff-free classification of all \(9pq\) numbers. Fresh Resultary searches found no theorem dominating those two core statements.

### equivalent_formulations

Searches:
- Resultary: weak Carmichael 3^a p q 9pq divisor parametrization exponent period pseudo-Carmichael
- Meštrović arXiv:1305.1867
- later fixed-support exponent-lattice result

Evidence:
- The later lattice theorem varies exponents with fixed support and does not bound or enumerate the prime pair for fixed \(a\).
- The audited theorem converts the unknown primes themselves into divisors of explicit finite integers.

Reasoning:
Fixed-support exponent lattices and fixed-exponent prime-pair parametrization are dual-looking but non-equivalent classification problems.

### broader_coverage

Searches:
- Meštrović 2013
- 2026/9/21/SCOPE-weak-carmichael-fixed-support-lattice-density--301b67b881e5
- OEIS weak Carmichael tables

Evidence:
- The later theorem is broader in exponent dimension but not in varying prime support.
- Tables list examples but do not prove the global \(9pq\) exhaustion.

Reasoning:
Neither broader exponent structure nor finite tables imply the divisor parametrization.

### exact_database_or_table

Searches:
- OEIS A225498
- OEIS A087442
- Meštrović tables
- current Resultary search

Evidence:
- The two \(9pq\) numbers are known entries, but no table proves there are no others.

Reasoning:
Known-table presence is separated from the new cutoff-free classification theorem.

### claim_vs_prior_implication

Searches:
- claim-versus-Meštrović criterion and later lattice theorem

Evidence:
- The criterion is the starting point and mechanically yields periodicity once \(p,q\) are fixed, so periodic lifting is treated as partially covered context.
- The finite divisor reduction in \((k,d)\) and its explicit global \(a=2\) exhaustion require an additional fixed-exponent elimination not present in the inspected sources.

Reasoning:
The final package survives on the finite parametrization and global slice classification even though one corollary is structurally covered.

### source_inspections

- **Generalizations of Carmichael numbers I** — https://arxiv.org/abs/1305.1867. Trigger: Primary source for the criterion and the \(3^2\)-family context. Material read: Accessible full arXiv HTML including the weak-Carmichael criterion and surrounding arithmetic development. Method: Primary full-text theorem comparison. Assessment: PARTIAL COVERAGE only. Evidence: The paper gives \(p-1\mid n-1\) for each prime divisor as the criterion but not the audited fixed-\(a\) divisor parametrization.
- **Fixed-support exponent lattices and primitive density for weak Carmichael numbers** — https://github.com/Resultary/2026/tree/main/2026/9/21/SCOPE-weak-carmichael-fixed-support-lattice-density--301b67b881e5. Trigger: Closest later structural result. Material read: Complete published RESULT.md. Method: Full implication comparison. Assessment: Covers exponent-lattice structure, not fixed-exponent prime-pair enumeration. Evidence: It fixes prime support and varies exponents; the audited theorem fixes the 3-exponent and solves for the other primes.
- **Assigned exact-integer verifier** — artifacts/verify.py. Trigger: Finite candidate and period checks. Material read: Complete source. Method: Line-by-line inspection. Assessment: Correct corroboration. Evidence: Parametric and direct searches agree for exponents one through five and reproduce the twelve \(a=2\) structural candidates.

### checked_sources

- https://arxiv.org/abs/1305.1867
- later fixed-support lattice theorem
- OEIS A225498
- OEIS A087442
- current Resultary search
- assigned verifier

### residual_risks

- Wong's 1997 thesis on pseudo-Carmichael/normal families was not fully inspected and remains the principal historical originality risk.

## Scientific value — PASS

Turning a two-prime infinite search into an explicit finite divisor computation for every fixed exponent is a useful Diophantine classification mechanism. The global \(9pq\) exhaustion also resolves a concrete inconsistency between listed examples and a cutoff computation in the literature.

### Value sources

- weak-Carmichael criterion
- assigned finite divisor reduction
- known \(9pq\) examples

### Value risks

- The fixed-pair periodicity corollary is not by itself the value-bearing contribution.

## Limitations

- Only numbers of the form \(3^a p q\) with first powers of \(p,q\).
- The later fixed-support lattice theorem partially covers exponent-period structure.
- Wong's 1997 thesis remains an access-limited originality risk.

## Disposition

**PASSED**
