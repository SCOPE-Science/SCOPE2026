# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-32ea5928743e`

## Correctness — PASS

The ordered-prime criterion reconstructs. If a prime divisor \(p\) of a Novák number has multiplicative order \(2d\), then \(d\) divides the number and every prime divisor of \(d\) is smaller than \(p\); therefore \(d\) divides the preceding ordered prime-power prefix, whose quotient by \(d\) is odd, forcing \(p\) to divide two to that prefix plus one. The least prime is consequently three. Conversely, starting from a power of three, the odd-power factorization and LTE allow any power of a new prime dividing the preceding plus-one value to be adjoined. The two-prime criterion, first-occurrence cyclotomic condition, primitive classification, infinitude, and logarithmic counting bound follow. The exact verifier was read in full and reports zero mismatches in its bounded checks; it corroborates rather than proves the infinite theorem.

### Correctness sources

- assigned RESULT.md
- Bailey–Smyth, Primitive solutions of n | 2^n + 1
- Kalmynin, arXiv:1611.00417
- artifacts/verify.py and verification.txt

### Correctness risks

- The primitive statement uses the Bailey–Smyth closure notion.
- The computation is finite and is not used as exhaustion of the theorem.

## Originality — PASS

The Bailey–Smyth note gives the least-prime-three restriction, closure operations, and the primitive notion; Kalmynin gives the forward extension principle. Neither inspected primary source states the converse ordered-prefix condition or the resulting iff classification of all ordered prime-power factorizations. OEIS entries tabulate examples and cyclotomic factors rather than prove the theorem. Current semantic search returned the audited finding as the only exact theorem match.

### equivalent_formulations

Searches:
- Resultary query: Novák numbers ordered prime prefix criterion primitive two prime solutions n divides 2^n+1
- Bailey–Smyth full note
- Kalmynin arXiv:1611.00417 full text

Evidence:
- The known forward extension lemma is one direction only.
- The converse uses multiplicative-order prime support to force every new prime at its preceding prefix.

Reasoning:
The same theorem was checked both as an ordered-prefix characterization and as a recursive extension/converse statement.

### broader_coverage

Searches:
- general recurrence self-divisibility literature, DOI 10.1017/S0013091510001355
- Bailey–Smyth closure theory

Evidence:
- The recurrence paper's accessible scope is general counting for self-divisibility and did not expose a theorem implying this prime-prefix criterion.
- Bailey–Smyth supplies necessary local structure but not the full iff recursion.

Reasoning:
No inspected broader theorem mechanically gives the full result; the general recurrence source remains an access risk rather than evidence of novelty.

### exact_database_or_table

Searches:
- OEIS A006521
- OEIS A136473
- OEIS A136475

Evidence:
- These entries record Novák numbers, primitive solutions, and prime factors of the relevant cyclotomic quotients.
- No database theorem or table certifies the full ordered-prefix iff statement.

Reasoning:
The examples support known data but the theorem is not a database lookup.

### claim_vs_prior_implication

Searches:
- Kalmynin extension lemma versus audited necessity
- Bailey–Smyth least-prime result versus full prefix closure

Evidence:
- Kalmynin implies sufficiency after each admissible prime is chosen, but not that every prime factor of an arbitrary solution appears admissibly at its ordered prefix.
- The audited multiplicative-order argument supplies exactly that missing converse.

Reasoning:
The final claim is not a corollary of the located prior statements without the new converse argument.

### source_inspections

- **Primitive solutions of n | 2^n + 1** — https://webhomes.maths.ed.ac.uk/~chris/papers/n_divides_2to_nplus1.pdf. Trigger: Primary source for primitive Novák solutions. Material read: Complete two-page note. Method: Full theorem and definition comparison. Assessment: NOT COVERING the ordered-prefix iff theorem. Evidence: It gives closure operations, the primitive notion, least prime three, and restrictions involving the exact power of three.
- **On Novák numbers** — https://arxiv.org/abs/1611.00417. Trigger: Primary modern Novák-number source and forward extension lemma. Material read: Full accessible arXiv text. Method: Full-text statement and implication comparison. Assessment: PARTIAL COVERAGE only. Evidence: It supplies the forward rule for adjoining prime powers dividing a plus-one value, not the converse ordered-prefix structure.
- **Novák-number OEIS records** — https://oeis.org/A006521. Trigger: Exact databases named by the research package. Material read: A006521, A136473 and A136475 entries and comments. Method: Database/table comparison. Assessment: Data support but do not cover the theorem. Evidence: The entries list known values and cyclotomic-factor data without the full iff criterion.
- **On numbers n dividing the nth term of a linear recurrence** — https://doi.org/10.1017/S0013091510001355. Trigger: Plausible broader self-divisibility theorem. Material read: Accessible abstract and bibliographic scope; full proof text was not read. Method: Residual-risk scope comparison only. Assessment: INACCESSIBLE/UNRESOLVED AS A BROAD RISK, not decisive coverage. Evidence: The visible scope concerns counts for general linear recurrences and does not state the audited Novák prefix theorem.

### checked_sources

- Bailey–Smyth full note
- Kalmynin arXiv:1611.00417
- OEIS A006521/A136473/A136475
- Resultary exact semantic search
- DOI 10.1017/S0013091510001355 abstract

### residual_risks

- Older Novák literature, recreational sources, or a general recurrence theorem under different terminology may contain an equivalent observation.
- The general recurrence paper was not inspected in full.

## Scientific value — PASS

This is a structural characterization of an infinite divisibility class, not merely a finite census. It converts local prime-order information into a canonical recursive construction, yields complete two-prime support behavior, and proves an infinite primitive family with a quantitative lower count.

### Value sources

- Bailey–Smyth primitive problem
- Kalmynin extension mechanism
- audited theorem and exact verifier

### Value risks

- The counting bound concerns only primitive solutions with exactly two distinct prime factors.

## Limitations

- The primitive classification uses the Bailey–Smyth closure definition.
- The counting lower bound covers exactly two distinct prime factors.
- Originality is best-of-knowledge because older or broadly formulated recurrence literature remains a residual risk.

## Disposition

**PASSED**
