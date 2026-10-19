# Scientific review

## Correctness — PASS

The proof uses the group Rota–Baxter equation without assuming a linear map. The center preservation argument is supplied explicitly, forcing an additive quotient map over the prime field. The alternating-form polarization gives the necessary and sufficient matrix condition \(\det A=k(1+\operatorname{tr}A)\). The exact trace/determinant matrix count, similarity-orbit count and two bijectivity tests are derived algebraically. In `verify.py`, the equation and direct bijectivity were checked for all \(810\) maps on the \(27\)-element group, and all formulas were checked for odd primes \(3,5,7,11\) where indicated. These finite checks do not establish the infinite theorem alone.

## Originality — PASS, with identified risks

Savelyev (arXiv:2608.28291, sections 3–5) proves center preservation, classifies the RB operators, and discusses which operators and their dual are bijective. The normal form and the condition on \(A,k\) should **not** be described as new on their own. Caranti–Stefanello (arXiv:2110.11028, Theorem 3.2 and Example 5.10) already construct the underlying inner skew braces; their cohomological paper (arXiv:2201.03936, section 6) already gives a scalar nonrealizability example. The present theorem assembles and proves the complete **all-matrices lift-fiber distribution**, exact liftable versus nonliftable *brace isomorphism* classification, and *four simultaneous-bijectivity counts*, which are not stated in the inspected relevant full texts. Relevant published index searches also found no identical enumeration. The coverage risk of older uncatalogued brace and cohomological classifications remains real.

## Value — PASS

This addresses a documented obstruction problem for inner skew braces on a natural infinite family. Instead of isolated counterexamples, it determines precisely which of the \(p^4\) inner brace structures lift, how many lifts each has, their exact isomorphism counts, and a sharp prevalence theorem for doubly bijective operators tied to the finite-group spectral question. The structure of the obstruction lies on a trace hyperplane and is exceptional on a determinant-zero divisor, a useful reproducible boundary.

## Scientific limitations

Only odd prime fields and the Heisenberg group of order \(p^3\); no inference to extension fields or all skew braces. The structural Rota–Baxter classification and brace construction are prior work, with new finite-field enumerations derived here. Equivalent older enumerations may exist outside indexed literature.

Self-review: passed. Independent audit: not yet performed.
