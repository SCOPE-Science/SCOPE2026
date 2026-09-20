# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The central lower bound is elementary and does not use normality of states. For a
state \(\varphi\) and pairwise orthogonal nonzero projections \((e_i)\), finite
orthogonal sums are projections bounded by \(1\). Hence, for every \(n\), at
most \(n\) indices can satisfy \(\varphi(e_i)\ge 1/n\). The indices on which
\(\varphi(e_i)>0\) are therefore countable. A separating family must cover
every index, giving
\[
|I|\le |\mathcal F|\aleph_0.
\]
This proves the required uncountable lower bound on the size of a separating
state family.

A finite or countable separating family has a faithful convex combination
with strictly positive coefficients, so the minimum separating-state
cardinality is either \(1\) or uncountable. Combining this dichotomy with a
\(\kappa\)-homogeneous orthogonal family and the assumed separating family of
size at most \(\kappa\) gives
\[
\kappa=\max\{\aleph_0,s(M)\}.
\]

The downward homogeneity argument was checked for singular as well as regular
cardinals. For every infinite \(\lambda\le\kappa\), cardinal arithmetic
partitions \(\kappa\) into \(\lambda\) sets each of size \(\kappa\).
Berberian addability applied to a bijection from the original
\(\kappa\)-decomposition onto each block shows that the join of each block is
equivalent to \(1\). This avoids any unsupported complementability or
projection-cancellation assertion. The state-cardinality bound excludes
homogeneity above \(\kappa\), proving the exact spectrum.

For the local faithful-corner application, Arulseelan's Corollary 6.2
explicitly constructs, from every maximal orthogonal \(p\)-copy extension of
the initial countable family, both a \(\kappa\)-indexed separating state
family and a \(\kappa\)-homogeneous decomposition. Therefore the general
theorem applies to each such \(\kappa\), making its cardinal independent of
the maximal extension. In the countable case the separating family has a
faithful weighted sum; conversely a faithful state cannot be positive on
uncountably many pairwise orthogonal nonzero projections.

The model case \(B(\ell_2(\tau))\) provides a consistency check: for
uncountable \(\tau\), the basis vector states give a separating family of
size \(\tau\), while the rank-one basis projections force the matching lower
bound; for separable \(H\), a faithful density-matrix state gives the
countable branch.

## Originality

**PASS, to the best of our knowledge.**

The primary recent source inspected was Jananan Arulseelan,
*A Transfinite Christensen--Pedersen Argument*, arXiv:2609.20718v1,
submitted 17 September 2026. Its Definition 1.2 introduces
\(\kappa\)-homogeneity; Theorem A combines \(\kappa\)-homogeneity with a
\(\kappa\)-indexed separating family; Theorems 5.3--5.4 supply the two
monotone-completeness steps; Corollary 6.2 constructs the cardinal
\(\kappa\) from a maximal family of equivalent corner projections. The
paper explicitly notes that countably many separating states can be combined
by a weighted sum and that no analogous uncountable weighted sum is
available. It does not state the orthogonal-family capacity lower bound,
the exact equality \(\kappa=\max\{\aleph_0,s(M)\}\), the maximality of
\(\kappa\) among homogeneity cardinals, the exact downward homogeneity
spectrum, or the resulting choice-independence of the local-corner
cardinal.

Nearby literature on faithful families of normal states in von Neumann
algebras and the classical equivalence between sigma-finiteness and the
existence of a faithful normal state was considered as conceptual prior art.
Those statements concern normal states and do not imply the ordinary-state
cardinal rigidity proved here.

The main residual prior-art risk is older AW*/Baer-* projection dimension
theory, especially S. K. Berberian, *Baer *-Rings* (1972), and related
Kaplansky-style decomposition theory. Berberian's addability theorem is
used as prior art, and the book's projection/decomposition scope was
identified, but it was not exhaustively checked for a differently named
cardinal invariant that simultaneously records projection multiplicity and
the least size of an ordinary-state separating family. Christensen--
Pedersen (1984) is the classical countable predecessor and does not use the
new transfinite homogeneity parameter.

The elementary state-counting lemma itself is not claimed as a new theorem.
The novelty claim is restricted to the exact cardinal identification and
homogeneity-spectrum consequence for the newly introduced transfinite
hypotheses, plus the canonical-cardinal consequence for the 2026
faithful-corner construction.

## Value

**PASS.**

Arulseelan's main theorem is formulated with a cardinal appearing on both
the projection-multiplicity and state-separation sides. The result here
shows that, once both hypotheses hold, that cardinal is forced rather than
chosen: in the uncountable regime the number of separating states is
optimal, and the same cardinal is the absolute ceiling for homogeneous
decompositions. This sharpens the interpretation of the transfinite theorem
and makes the cardinal produced in the local faithful-corner application
canonical despite its Zorn-maximal-family origin.

The result also supplies a clean dichotomy between the global faithful-state
regime and the genuinely uncountable regime, while using ordinary rather
than normal states.

## Limitations

The theorem does not classify homogeneity spectra of arbitrary AW*-algebras;
the interval description requires the simultaneous hypotheses of
\(\kappa\)-homogeneity and a separating family of at most \(\kappa\)
ordinary states. It does not strengthen Arulseelan's monotone-completeness
conclusion itself. It concerns ordinary-state separation rather than the
normal-state predual invariant. The local choice-independence statement is
for maximal \(p\)-copy families extending the countably infinite family used
in Corollary 6.2.

No independent validation or independent audit has been performed.
