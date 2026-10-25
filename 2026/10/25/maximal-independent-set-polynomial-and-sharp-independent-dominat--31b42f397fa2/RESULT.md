# Maximal independent-set polynomial and sharp independent domination of two-token complete bipartite graphs

## Finding
For integers \(2\le m\le n\), let \(H_{m,n}=F_2(K_{m,n})\) be the graph of two distinct unlabelled tokens on the complete bipartite graph, adjacent when one token slides along one host edge. Define the family of allowed uncovered-side cardinalities
\[
\mathcal U_s=\{1,2,\ldots,s\}\setminus\{s-1\},\qquad s\ge2.
\]
Let \(M_{m,n}(z)=\sum_{I\text{ maximal independent in }H_{m,n}}z^{|I|}\). The complete polynomial is
\[
\boxed{M_{m,n}(z)=z^{\binom m2+\binom n2}+\sum_{u\in\mathcal U_m}\sum_{v\in\mathcal U_n}\binom m u\binom n v z^{\binom{m-u}2+\binom{n-v}2+uv}.}
\]
In particular, the number of maximal independent sets is exactly
\[
\boxed{1+(2^m-m-1)(2^n-n-1).}
\]
The independent domination number (the minimum cardinality of a maximal independent set) is
\[
\boxed{i(H_{m,n})=\begin{cases}2,&m=n=2,\\2n-3,&m=2<n,\\\binom m2+n-m,&3\le m\le n.\end{cases}}
\]
The number \(T_{m,n}\) of sets attaining this minimum is
\[
\boxed{T_{m,n}=\begin{cases}
1,&m=n=2,\\
\binom n2+\mathbf1_{n\ge4}\binom n3,&m=2<n,\\
m\binom n2,&3\le m<n,\\
\displaystyle\sum_{u=1}^{m-2}\binom m u\left(\mathbf1_{u\ge2}\binom m u+\binom m{u+1}\right),&3\le m=n.
\end{cases}}
\]
For the balanced host \(K_{r,r}\), \(r\ge3\), the independent domination number grows quadratically in \(r\), whereas the previously determined ordinary domination number grows linearly. Hence the ratio of independent domination to ordinary domination is unbounded within this natural token-graph family.

## Assumptions and scope
All graphs are simple and finite. The underlying \(K_{m,n}\) has labelled bipartition \(A\sqcup B\), where \(|A|=m\) and \(|B|=n\). A token-graph vertex is an unordered two-element subset of \(A\sqcup B\); two such vertices are adjacent if their symmetric difference consists of an original host edge. An independent set is *maximal* if no further token-graph vertex can be added. An independent dominating set is exactly a maximal independent set. The polynomial counts actual labelled vertex subsets, not subsets modulo automorphisms. The indicator \(\mathbf1_{u\ge2}\) equals one if the displayed condition holds and zero otherwise. When \(\binom s2\) has nonnegative integer upper entry, it has its usual meaning.

## Proof
**1. Neighborhood structure.** Partition token-graph vertices into pure pairs \(\binom A2\cup\binom B2\), and mixed pairs \(A\times B\). Adjacency occurs only between the pure class and the mixed class. An \(A\)-pair \(\{a,a'\}\) is adjacent precisely to mixed pairs having \(A\)-coordinate \(a\) or \(a'\), and likewise for \(B\)-pairs.

**2. Unique form of every maximal independent set.** Fix a maximal independent set \(I\). Let \(U\subseteq A\) be the points not incident to a selected pure \(A\)-pair, and let \(V\subseteq B\) be the analogous points on the other side. Independence forces selected mixed pairs to lie inside \(U\times V\). Conversely, every mixed pair in \(U\times V\) must be selected: otherwise that pair has no selected pure neighbor and can be added. Thus
\[
I\cap(A\times B)=U\times V.
\]
If either \(U\) or \(V\) is empty, there are no selected mixed pairs. Every pure pair would then be addable unless already selected, so maximality forces the unique all-pure set \(\binom A2\cup\binom B2\).

Suppose \(U,V\ne\varnothing\). Each pure \(A\)-pair with both endpoints outside \(U\) must be selected: without being selected, it would have no selected mixed neighbor. Any selected \(A\)-pair already lies outside \(U\) by definition, so
\[
I=\binom{A\setminus U}{2}\ \cup\ \binom{B\setminus V}{2}\ \cup\ (U\times V).
\]
The set of vertices covered by all pairs of \(A\setminus U\) is exactly \(A\setminus U\) if its size is zero or at least two, but not if it has size one. Therefore consistency of \(U\) requires \(m-|U|\in\{0\}\cup\{2,\ldots,m-1\}\), and similarly for \(V\). Equivalently, \(|U|\in\mathcal U_m\) and \(|V|\in\mathcal U_n\). Conversely, every such \(U,V\) yields an independent set of the displayed form and each unselected pure pair is adjacent to a selected mixed pair (because it meets \(U\) or \(V\)); each unselected mixed pair meets a selected pure pair. Hence the set is maximal. Recovering \(U,V\) from selected pure pairs proves distinctness, and the all-pure set is not one of these cases. Counting choices of \(U,V\) and selected-pair cardinalities proves the polynomial.

**3. Total count.** We have \(\sum_{u\in\mathcal U_s}\binom s u=2^s-s-1\) (remove zero and \(s-1\) from the binomial sum). Setting \(z=1\) gives the asserted total.

**4. Sharp minimum and multiplicity.** Put \(u=|U|\) and \(b=n-|V|\). The cardinality of a mixed-type maximal independent set is
\[
F_{m,n}(u,b)=\binom{m-u}{2}+\binom b2+u(n-b)
=\binom m2+u(n-m)+\frac{(b-u)(b-u-1)}2.
\]
The last term is nonnegative for every integer \(b-u\), vanishing exactly when \(b=u\) or \(b=u+1\). When \(3\le m<n\), the unique smallest permitted \(u\) is one; choosing \(b=2\) is permitted and yields \(F=\binom m2+n-m\). The strict positive factor \(n-m\) forces \(u=1\) at equality. The number of optimal choices is \(\binom m1\binom n2=m\binom n2\). For \(3\le m=n\), equality is attained exactly for \(1\le u\le m-2\), with \(b=u\) (permitted only if \(u\ge2\)) or \(b=u+1\); note that \(u=m\) cannot attain equality because \(b\le m-1\). Counting \(U\) and the corresponding complements of \(V\) gives the balanced-case sum. When \(m=2\), the only permitted \(u\) is two, and \(F=2n-3+(b-2)(b-3)/2\); for \(n>2\), equality occurs when \(b=2\) or, if permitted, \(b=3\), giving the two binomial terms. For \(m=n=2\), the only mixed-type set has four members, while the all-pure set has two, uniquely.

Finally the all-pure set has size \(\binom m2+\binom n2\), strictly exceeding the mixed-type minimum in all cases except \(m=n=2\), in which it supplies the minimum. Indeed, for \(3\le m\le n\), \(\binom n2>n-m\), and for \(m=2<n\), \(1+\binom n2>2n-3\). This proves all minimum and multiplicity assertions.

**5. The structural gap.** For \(r\ge3\), \(i(H_{r,r})=\binom r2\). The established ordinary domination theorem gives \(\gamma(H_{r,r})\le\lceil r/2\rceil+r-1\) (with a smaller value for \(r=3\)). Therefore \(i(H_{r,r})/\gamma(H_{r,r})\ge\binom r2/(\lceil r/2\rceil+r-1)\), which diverges as \(r\to\infty\).

## Verification
A separate program, `verify.py`, independently constructs each token graph from the symmetric-difference adjacency definition and enumerates all maximal independent sets as maximal cliques of its complement. It compares every coefficient with the formula, the total count, minimum cardinality and number of minima for every \(2\le m\le n\le6\), amounting to 15 graph instances and 6,947 maximal independent sets. It returns `VERIFY_OK pairs= 15 distinct_maximal_independent_sets= 6947`. Run using `python3 verify.py` with the `networkx` Python package installed. The finite checks are supporting tests, not a proof of the theorem for all parameters.

## Relationship to prior work
Fabila-Monroy and Gómez-Galicia (2025, arXiv:2509.16448) study domination of two-token stars and complete graphs; their paper motivates token domination but does not address this independent-domination polynomial. De Alba and coauthors (arXiv:1606.06370), and Abdelmalek, Vander Meulen, Vander Meulen and Van Tuyl (arXiv:2010.04539), study independence numbers, well-coveredness and constructions of maximal independent sets; neither inspected work states the complete maximal-independent-set profile or the sharp independent-domination multiplicities above. Importantly, the later independent 2026 preprints arXiv:2610.28936 and arXiv:2610.31557 determine ordinary domination of \(F_2(K_{m,n})\). Lemma 2.2 of the latter already characterizes **all dominating sets** of the same token graphs; imposing independence on that criterion supplies a route to the classification here. The current contribution is the resulting exhaustive cardinality polynomial and exact minimum-with-multiplicity optimization, **not** the general dominating-set characterization or the ordinary domination number. Its independent-domination conclusion is not a logical consequence of the numerical ordinary-domination formula alone, but may be regarded as a refinement of the 2026 characterization.

## Limitations
The theorem is restricted to two-token complete bipartite hosts with both classes of size at least two; it makes no assertion about higher token counts or general complete multipartite hosts. The verification program only exhausts small parameter ranges. No claim is made that special cases of this construction are previously unknown; no independent validation has been performed. Prior studies may encode equivalent maximal-stable-set profiles under alternative terminology, especially symmetric squares, minimal vertex covers, or upper domination; the 2026 general characterization is a closely related antecedent. The present formula counts labelled sets, not automorphism orbits.

## References
1. R. Fabila-Monroy and S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448, first submitted 2025-09-19, https://arxiv.org/html/2509.16448v1.
2. H. de Alba et al., *Independence and matching numbers of some token graphs*, arXiv:1606.06370, https://arxiv.org/abs/1606.06370.
3. F. Abdelmalek, E. Vander Meulen, K. Vander Meulen and A. Van Tuyl, *Well-covered Token Graphs*, arXiv:2010.04539, https://arxiv.org/abs/2010.04539.
4. N. Chinman et al., *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936 (2026-10-20), https://arxiv.org/abs/2610.28936.
5. E. Acosta Troncoso, I. Caldera Caldera and L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557 (2026-10-22), https://arxiv.org/html/2610.31557v1. In particular see Lemma 2.2.
