# Independent mathematical audit — 2026-10-01

**Record:** SCOPE-20260919-da564dfc32a5 — Unbounded 2-rank inside Kishi's Fibonacci class-number-five family
**Disposition:** PASSED

## Final claim assessed

For every integer \(R\ge1\), an odd \(U_R\) can be chosen so that all but finitely many admissible odd primes \(Q\) give distinct fields \(\mathbf Q(\sqrt{-F_{25U_RQ}})\) in Kishi's family with \(2\)-rank at least \(R\), hence class number divisible by \(5\cdot2^R\).

## Correctness — PASS

For distinct primitive divisors \(q_i\mid F_{25r_i}\), ranks of apparition are the distinct indices \(25r_i\). The chosen parity corrections in \(U_R\) make each \(v_{q_i}(F_{25U_RQ})\) odd, while \(v_5(F_{25U_RQ})=3\). Thus the squarefree kernel has at least \(R+1\) distinct odd prime divisors and genus theory gives \(\operatorname{rk}_2\operatorname{Cl}\ge R\). Since \(25U_RQ\equiv25\pmod{50}\), Kishi's five-divisibility applies. The infinitude argument is also valid: finite repetition forces a fixed squarefree kernel, whence the Fibonacci--Lucas identity gives infinitely many integral points on a fixed nonsingular genus-one quartic, contradicting Siegel.

## Originality — PASS

The exact audited claim is an unbounded \(2\)-rank theorem inside the same Kishi Fibonacci family, not merely five-divisibility. The accessible Kishi abstract states universal divisibility by five and an unramified quintic extension, while the 2026 Chakraborty--Rao--Dabhole abstract describes use of Kishi's family in a biquadratic construction. Targeted Resultary and literature searches found no earlier arbitrary-rank statement or a stronger theorem implying it. Because Kishi's full article was inaccessible, this remains a best-of-knowledge PASS with a named residual risk.

## Scientific value — PASS

The result concerns an already-motivated explicit Fibonacci family with a known uniform class-number divisibility phenomenon and strengthens its \(2\)-primary information from a fixed factor to arbitrarily large class-group \(2\)-rank on infinite subfamilies. This is a natural structural refinement, not an arbitrary finite computation.

## Originality comparison details

### Equivalent formulations

The claim was compared both as class-group 2-rank and as forcing arbitrarily many independent ramified prime discriminants in squarefree Fibonacci kernels.

Searches:
- Resultary semantic search: Fibonacci imaginary quadratic fields unbounded 2-rank Kishi class number five primitive divisors genus theory
- web search: Kishi Fibonacci 2-rank unbounded squarefree kernel genus theory

Evidence:
- The top Resultary match was the audited record itself; no equivalent squarefree-kernel/genus-theory theorem for arbitrary rank appeared in the returned published findings.

### Broader coverage

Neither accessible statement dominates an arbitrary \(2\)-rank lower bound within the Kishi family.

Searches:
- Y. Kishi, J. Number Theory 128 (2008), DOI 10.1016/j.jnt.2008.02.016
- P. Rao, K. Chakraborty, A. Dabhole, arXiv:2609.16678

Evidence:
- Kishi abstract: class numbers of \(\mathbf Q(\sqrt{-F_{50s+25}})\) are divisible by five; arXiv:2609.16678 abstract: Kishi family is one ingredient in a biquadratic large-class-number construction.

### Exact database or table

This is not a finite-table claim; database checking was used to detect prior published formulations, not to infer novelty from absence alone.

Searches:
- Resultary query listed above
- targeted web searches for exact family \(F_{50s+25}\) with 2-rank/class-group rank

Evidence:
- No exact database/table entry giving arbitrary 2-rank in this family was returned.

### Claim versus prior implication

No inspected prior statement logically implies the audited theorem.

Searches:
- direct implication comparison with Kishi five-divisibility and the recent biquadratic-family abstract

Evidence:
- Five-divisibility supplies odd-primary information and does not imply unbounded genus-theoretic \(2\)-rank. A construction of biquadratic fields from the Kishi family likewise does not, from its accessible statement, imply arbitrary \(2\)-rank of the Kishi quadratic factor.

## Source inspections

### A new family of imaginary quadratic fields whose class number is divisible by five

- Identifier: DOI 10.1016/j.jnt.2008.02.016
- Trigger: Same Fibonacci family and principal residual-priority risk
- Material read: Abstract and bibliographic material; full text retrieval could not proceed past human verification
- Method: Open-access search followed by authorized institutional retrieval attempt
- Assessment: NOT_COVERING on the material actually read; full-text risk remains
- Evidence: Abstract states universal five-divisibility and an unramified cyclic quintic extension, not a 2-rank theorem.

### An infinite family of imaginary biquadratic fields with a large class number

- Identifier: arXiv:2609.16678
- Trigger: Recent work using the same Kishi family
- Material read: Primary arXiv abstract
- Method: Open web/arXiv metadata
- Assessment: NOT_COVERING on accessible material
- Evidence: Abstract describes composition with Kishi family to obtain biquadratic fields with large class numbers.

## Limitations and residual risks

- Kishi 2008 full text was not inspectable in this run after human verification was required; the PASS on originality is explicitly best-of-knowledge.
- The theorem gives lower bounds on 2-rank and class-number divisibility, not the full 2-primary class group, exact 2-power orders, density, or optimized \(U_R\).
