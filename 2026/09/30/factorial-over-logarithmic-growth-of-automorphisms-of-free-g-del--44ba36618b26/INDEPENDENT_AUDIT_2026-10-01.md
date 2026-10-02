# Mathematical audit — 2026-10-01

## Final claim assessed

Factorial-over-logarithmic growth of automorphisms of free Gödel algebras

## Correctness — PASS

PASS. Aguzzoli's exact dual-forest theorem gives \(H_0=\varnothing\), \(H_n=\sum_{j<n}\binom{n}{j}(H_j)_\perp\), the wreath-product automorphism recursion, and \(\operatorname{Aut}(F_n(G))\cong\operatorname{Aut}(H_n)^2\). Taking logarithms yields \(a_n=f_n+\sum_{j<n}\binom{n}{j}a_j\), where \(f_n=\sum_{j<n}\log(\binom{n}{j}!)\). The exponential generating function therefore satisfies \(A(z)=\Phi(z)/(2-e^z)\). The bound \(f_n=O(n2^n\log n)\) makes \(\Phi\) entire. The nearest denominator zero is the simple pole \(L=\log2\), while the next pair has modulus \(\sqrt{L^2+4\pi^2}\); residue extraction gives the claimed \(n!/L^{n+1}\) scale and error. A fresh numerical recurrence gives the normalized values converging to \(0.5656527950551602\ldots\), matching the stated constant.

## Originality — PASS

PASS to the best of current knowledge. The complete eight-page Aguzzoli primary paper was inspected. It gives the exact recursive forest and automorphism-group decompositions but no asymptotic growth analysis. A 2026 structural paper on free Gödel algebras develops dual descriptions and coproducts rather than automorphism-order asymptotics. Resultary and targeted searches for free Gödel automorphism growth, the \(n!/(\log2)^{n+1}\) scale, and the constant \(0.565652795\ldots\) found no earlier theorem.

### equivalent_formulations

Searches: Resultary: free Gödel algebra automorphism asymptotic factorial logarithm; web: automorphism free Gödel algebra asymptotic \(n!/(\log2)^{n+1}\)

Evidence: The exact search returned only the assigned asymptotic theorem. The primary 2020 paper states recursive group structure, not a growth equivalent.

Reasoning: The forest recurrence and the EGF pole formulation are equivalent descriptions after a nontrivial logarithmic/binomial-transform step; the latter asymptotic is absent from inspected prior work.
### broader_coverage

Searches: Aguzzoli 2020 complete primary paper; Carai 2026 free Gödel algebras and coproducts

Evidence: Aguzzoli gives the exact finite recursion; Carai gives modern structural duality results without an automorphism-growth asymptotic.

Reasoning: Neither inspected structural theorem contains or mechanically states the dominant singularity analysis or explicit constant.
### exact_database_or_table

Searches: Resultary semantic search for the normalized constant \(0.5656527950551603024\)

Evidence: No prior matching constant or automorphism-order sequence asymptotic was located.

Reasoning: The statement is an analytic asymptotic theorem, not a table lookup.
### claim_vs_prior_implication

Searches: Aguzzoli Theorems 11--12; dominant-pole derivation from the logarithmic recurrence

Evidence: The prior paper supplies the exact recursion; obtaining the asymptotic requires passing to logarithms, deriving an EGF resolvent, proving the numerator entire, locating the dominant pole and extracting its residue.

Reasoning: Those analytic steps are additional and yield a new quantitative theorem rather than a direct restatement of the group decomposition.

## Scientific value — PASS

PASS. The automorphism group is a natural quantitative invariant of the free algebra, and its exact recursive product formula obscures the scale of growth. The theorem identifies a non-obvious factorial-over-logarithmic scale, an explicit limiting constant, and an exponentially separated error term. This is a motivated asymptotic invariant of a standard free-algebra family, not a finite table or arbitrary slice.

## Source inspections

- **Automorphism groups of Lindenbaum algebras of some propositional many-valued logics with locally finite algebraic semantics** — https://doi.org/10.1109/FUZZ48607.2020.9177714. Material read: Complete eight-page primary paper, with detailed inspection of the Gödel-algebra section and Theorems 11--12. Assessment: STRUCTURAL_PRIOR_NOT_ASYMPTOTIC_COVERAGE. Evidence: The paper gives the recursive forests and finite automorphism-group structure but no asymptotic evaluation of their orders.
- **Free algebras and coproducts in varieties of Gödel algebras** — https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/free-algebras-and-coproducts-in-varieties-of-godel-algebras/E5DAE6CEB6B11595ADEBC5810FE27635. Material read: Primary article abstract and relevant structural statements exposed in the full public article page. Assessment: BROADER_STRUCTURE_NOT_AUTOMORPHISM_ASYMPTOTICS. Evidence: The paper concerns dual descriptions, coproducts, depth and bi-Heyting structure, not automorphism-order growth.

## Limitations and residual risks

The theorem concerns the logarithm of the finite automorphism-group order for free finitely generated Gödel algebras. It uses the published recursive dual-forest description and does not assert a comparable law for arbitrary varieties of Heyting or many-valued algebras.

- A standard analytic-combinatorics treatment of the same recurrence could exist outside the Gödel-algebra literature, but no source applying it to this automorphism sequence was located.

## Disposition

**passed**
