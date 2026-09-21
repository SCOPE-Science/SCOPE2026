# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The finite-level lower bound is certified by the exact factorization
\[
I_{\ell_\infty^n}=D^{-1}QM_\varphi J,
\]
where \(J\) is an isometry, \(Q\) is contractive, and \(D\) is diagonal with entries of modulus greater than the chosen threshold. Strict normalization and the ideal axiom therefore give the lower bound for every strict s-number. The matching upper bound is a rank-\(<n\) truncation on the finite superlevel set. The finite witness is explicitly 1-complemented via \(P=JQ\).

For the ideal-distance statement, every threshold below \(\rho(\varphi)\) yields an infinite superlevel set and hence disjoint compactly supported functions generating an isometric \(c_0\) subspace on which \(M_\varphi\) is bounded below. This excludes approximation within that threshold by a strictly singular operator. Together with finite-rank truncation and \(\mathcal K\subset\mathcal{FSS}\subset\mathcal{SS}\), this gives all three exact distances. No complementability of the infinite-dimensional witness is used or claimed.

Boundary cases were checked directly: if \(\Omega\) is finite and \(n>\#\Omega\), both sides of the s-number formula are zero; if the derived set of a compact space is empty, compactness forces the space to be finite and the limiting statistic is zero.

## Originality

**PASS, to the best of our knowledge.** The claim was compared against exact and synonymous formulations involving multiplication operators, diagonal operators, approximation/Bernstein/Gelfand/Kolmogorov numbers, strict s-numbers, essential norms, strictly singular operators, and central/disjointness-preserving operators.

Prior coverage that is deliberately excluded from the novelty claim includes:

- Pietsch's foundational strict s-number theory (1974).
- Hutton--Morrell--Retherford's diagonal-operator work on approximation numbers and Kolmogorov diameters (1976).
- The discrete diagonal approximation-number formulas reported by Faried--Abd El Ghaffar (2012), including their attribution of the l-infinity case to earlier work of Pietsch.
- Edmunds--Lang's exact coincidence examples for strict s-numbers of integral operators and Sobolev embeddings (2012).
- Schep's abstract multiplication-operator essential-norm theory (2023).
- Kiwerski--Tomaszewski's essential and weak essential norm formulas for pointwise multipliers between Köthe spaces (2026).

The accessible page for Aksoy--Lewicki, *Diagonal Operators, S-Numbers, and Bernstein Pairs* (1997), confirms that diagonal operators and general s-numbers are central to that paper, but the full theorem text was not inspected. It is therefore the most specific unresolved priority risk. Older monographs and Banach-lattice literature on diagonal, central, and disjointness-preserving operators remain additional residual risks. No available statement located in the comparison established the all-strict-s-number \(C_0(\Omega)\) formula together with the exact compact/FSS/SS distance collapse.

## Value

**PASS.** The result gives the complete finite-index profile, not only an asymptotic or essential norm. The same elementary statistic controls every strict s-number, all three ideal distances, and the perfect-space flat-profile phenomenon. The explicit finite-dimensional 1-complemented witnesses also identify the geometric mechanism behind the coincidence.

## Scope and limitations

The result is restricted to scalar pointwise multiplication on \(C_0(\Omega)\). It does not claim an analogue for weighted composition operators or for arbitrary central operators on general Banach lattices. The infinite-dimensional \(c_0\) witness used for strict singularity is not claimed to be complemented.
