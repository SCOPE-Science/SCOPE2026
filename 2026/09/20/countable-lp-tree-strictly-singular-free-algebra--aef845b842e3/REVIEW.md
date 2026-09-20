# Review: Free algebra modulo compact operators on a countable tree of ℓp spaces

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The construction was checked at the level of each required operator-ideal assertion.

For \(p<q\), the formal inclusion \(J:\ell_p\to\ell_q\) is finitely strictly singular and noncompact. Noncompactness follows immediately from the unit-vector sequence, and finite strict singularity is the classical Milman result. Thus each edge map used in the binary tree is strictly singular and noncompact.

For each generator \(S_i\), truncating to finitely many tree levels gives a finite sum of operators which factor through one edge inclusion. Such a truncation is strictly singular. The omitted tail has norm at most the largest omitted weight, and the weights tend to zero. Norm-closedness of the strictly singular ideal therefore gives \(S_i\in\mathcal{SS}(X)\). Restriction to the root-to-child edge proves \(S_i\notin\mathcal K(X)\).

The freeness argument was also checked against cancellation. Distinct nonempty words send the root copy of \(\ell_1\) into distinct tree nodes. For a finite nonzero polynomial, after collecting equal words, the image of each root unit vector has one coordinate in every node corresponding to a surviving word. The pairwise distance formula
\[
\sum_u |c_u|^2 b_{|u|}^2 2^{2/(|u|+1)}>0
\]
is independent of the two distinct unit-vector indices. Hence no nonzero polynomial with zero constant term is compact. Since every such polynomial is strictly singular, its class modulo compact operators is nonzero. This proves injectivity of the free non-unital algebra.

Potential hidden issues were tested:

- Repetition of the same exponent at a fixed tree level causes no problem because each level is finite and the strict-singularity argument uses finite sums before taking a norm limit.
- The infinite direct sum itself does not require an assertion that an arbitrary direct sum of strictly singular maps is strictly singular; the vanishing level weights are essential and provide norm approximation by finite sums.
- Polynomial terms of different lengths cannot cancel because they land in different tree levels; terms of the same length but different words land in different coordinate blocks.
- Compactness is disproved on the complemented root block, so no global compactness subtlety remains.
- The quotient statement uses only polynomials with zero constant term, matching the fact that \(\mathcal{SS}(X)/\mathcal K(X)\) is naturally non-unital.

## Originality

The older background literature establishes the gap between compact and strictly singular maps and, in particular, the finitely strictly singular noncompact formal inclusions \(\ell_p\hookrightarrow\ell_q\) for \(p<q\). Schlumprecht's 2012 exposition explicitly records Milman's formal-inclusion result and develops operator ideals on \(\ell_p\oplus\ell_q\).

The closest current theorem located is Laustsen--Wirzenius (2026): for finite direct sums of Baernstein, Schreier and \(\ell_p\)-spaces, \(\mathcal{SS}(X)/\mathcal K(X)\) is nilpotent. Its statement is explicitly finite. The present construction instead uses a countable binary tree of classical \(\ell_p\) blocks and produces a free noncommutative algebra in the quotient.

Targeted searches combined phrases and synonyms involving strictly singular/compact quotients, nonnilpotency, countable or infinite direct sums, weighted shifts, tree shifts, free semigroups, free associative algebras, and free subalgebras. No source stating this construction or an equivalent free-algebra conclusion was located. Literature on free semigroup algebras provides the general tree-shift motif but does not place the generators in the strictly singular ideal or study their classes modulo compact operators.

Residual originality risk remains because the proof is explicit and uses standard ingredients. Milman's 1970 primary article and Pietsch's classical operator-ideal monograph were not exhaustively inspected, and a result about infinite direct sums could be phrased in substantially different terminology. No concrete evidence of prior coverage was found.

Originality is therefore assessed only to the best of our knowledge.

## Value

The result identifies a qualitative boundary rather than a parameter increment. Finite direct sums in the closest literature force nilpotency of \(\mathcal{SS}/\mathcal K\); a concrete countable direct sum can instead contain the free algebra on two generators. This simultaneously gives nonnilpotency, non-nilness, noncommutativity and absence of polynomial relations among two explicit strictly singular classes.

The binary-tree mechanism is reusable: whenever a sequence of Banach spaces admits noncompact strictly singular connecting maps with noncompact finite compositions, decaying tree shifts can be used to create algebraically independent classes modulo compact operators.

## Verdict

Correctness: PASS.  
Originality: PASS, to the best of our knowledge.  
Value: PASS.

Same-model review: passed. Independent audit: not yet performed.
