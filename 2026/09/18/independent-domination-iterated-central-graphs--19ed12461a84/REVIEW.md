# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument reduces the iteration problem to two exact ingredients.

First, the subdivision vertices of \(C(G)\) form an independent set of size
\(|E(G)|\). Any independent set using original vertices determines a clique
\(Q\) in \(G\), and can contain subdivision vertices only for edges entirely
outside \(Q\). Connectedness and \(n\ge3\) imply that at least \(|Q|\) edges are
incident with \(Q\), so no independent set is larger than \(|E(G)|\). This
proves
\[
\alpha(C(G))=|E(G)|.
\]

Second, Theorem 2.12 of Cabrera-Martínez et al. gives an exact formula for
\(i(C^2(H))\) in terms of the order, size and independence number of \(H\).
Substituting \(H=C(Y)\) and the preceding lemma produces an exact cancellation,
giving
\[
i(C^3(Y))=2|E(C(Y))|.
\]
Taking \(Y=C^{k-3}(G)\) proves the claimed formula for every \(k\ge3\).

Adversarial checks considered the exceptional cases where a clique \(Q\) has
one or two vertices. The \(q=2\) case needs connectedness and \(n\ge3\) to
guarantee an edge from \(Q\) to its complement; this hypothesis is present in
the theorem. The complete-graph case is also covered: the subdivision vertices
still give \(\alpha(C(K_n))=|E(K_n)|\).

Supporting computation checks all connected NetworkX atlas graphs through order
7 for the central-graph independence identity and for the algebraic reduction of
the source formula, and directly checks independent domination in the second and
third iterates through order 5.

## Originality

**PASS, to the best of our knowledge.**

The closest source is the September 14, 2026 preprint:

- Cabrera-Martínez, López-Carmona, Rios-Villamar, Serrano-Díaz,
  *Independent domination in central graphs*, arXiv:2609.16357v1.

Its complete accessible HTML text was inspected. The paper explicitly defines
\(C^2(G)\), proves a general formula for \(i(C(G))\), and concludes its results
section with Theorem 2.12, a formula for \(i(C^2(G))\). Searches within the
paper found no \(C^3(G)\), higher-iterate, or iteration statement.

External searches used the terms and equivalent formulations
"independent domination" with "iterated central graph(s)", "second/third central
graph", "\(C^3(G)\)", "\(C^k(G)\)", and searches for the independence number of
a central graph. No equivalent or stronger coverage of the stated iteration law
was found.

The 2026 paper by Barish--Fujita--Kazemnejad--Pahlousay on vertex cover and
ordinary domination of central graphs was inspected at the abstract/available
text level. It studies \(\gamma(C(G))\), not independent domination, and does
not supply the present result.

No inaccessible paper was identified as specifically likely to contain the same
higher-iterate independent-domination law. Residual originality risk remains
from very recent unindexed parallel work and from older literature using
nonstandard terminology for repeated central-graph operations.

## Value

**PASS.**

The source paper's \(C^2\)-formula still depends on the structure-sensitive
invariant \(\alpha(G)\). The new result shows that one iteration later this
dependence disappears completely: for every \(k\ge3\),
\(i(C^k(G))\) is determined by the order and size recurrence alone. Thus any two
connected graphs with equal order and size become indistinguishable by this
parameter on every central iterate from the third onward. The exact identity
\(\alpha(C(G))=|E(G)|\) also supplies the mechanism behind this stabilization.

## Limitations

- The result is stated for finite connected simple graphs of order at least 3.
- The proof relies on the published same-setting formula for \(i(C^2(H))\).
- The computation is supporting evidence, not a substitute for the proof.
- Very recent or unindexed parallel work may exist.
- Independent audit has not been performed.
