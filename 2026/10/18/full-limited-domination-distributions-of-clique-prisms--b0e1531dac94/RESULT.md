# Full limited-domination distributions of clique prisms

## Finding

Let \(n\ge2\), and let \(R_n=K_n\square K_2\) have two labelled complete layers \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with matching edges \(a_i b_i\). A vertex set \(D\) is *\(k\)-limited dominating* if every vertex outside \(D\) has a neighbour in \(D\), and every vertex in \(D\) has at most \(k\) neighbours outside \(D\). Let

\[
L_{n,k}(z)=\sum_{D\;\mathrm{admissible}}z^{|D|},\qquad 0\le k\le n.
\]

For nonnegative integers \(c,x,y,d\) with \(c+x+y+d=n\), define \(a=c+x\) and \(b=c+y\). Let \(\mathcal F_{n,k}\) consist of those quadruples satisfying

\[
a<n,\quad b<n,\quad a+\mathbf 1_{y>0}\le k,\quad b+\mathbf 1_{x>0}\le k.
\]

Then the **complete cardinality enumerator**, for all \(n\ge2\) and \(0\le k\le n\), is

\[
\boxed{L_{n,k}(z)=2\mathbf 1_{k\ge1}z^n+\sum_{(c,x,y,d)\in\mathcal F_{n,k}}\frac{n!}{c!x!y!d!}z^{x+y+2d}.}
\]

This equation comes from a necessary-and-sufficient classification of **every** admissible set, including all labelled realizations; it is not merely an extremal-value identity. The minimum-set multiplicities are:

\[
\boxed{
\begin{aligned}
[k=0]&:\quad (\gamma_k^{\mathrm L},M_{n,k})=(2n,1),\\
[1\le k<n,\ 2k<n]&:\quad (\gamma_k^{\mathrm L},M_{n,k})=(n,2),\\
[1\le k<n,\ 2k=n]&:\quad (\gamma_k^{\mathrm L},M_{n,k})=(n,2+\tbinom nk),\\
[1\le k<n,\ 2k>n]&:\quad (\gamma_k^{\mathrm L},M_{n,k})=(2(n-k),\tbinom nk),\\
[k=n]&:\quad (\gamma_k^{\mathrm L},M_{n,k})=(2,n^2+2\mathbf 1_{n=2}).
\end{aligned}}
\]

Here \(M_{n,k}\) is the number of minimum-cardinality admissible labelled subsets. In the nontrivial interior range \(2\le k<n\), the minimizers are exactly the two full layers when \(2k<n\), the two full layers together with every set formed by retaining both vertices in exactly \(n-k\) matched columns when \(2k=n\), and only those matched-column sets when \(2k>n\). The minimum *size* formula was previously recorded for general rectangular rook graphs and is included only for context; the full polynomial and the missing minimizer-count classification are the refinements established here.

For \(k=n\), the polynomial simplifies to the ordinary domination enumerator

\[
L_{n,n}(z)=\bigl((1+z)^n-1\bigr)^2+2z^n.
\]

## Assumptions and scope

Graphs are finite, simple and labelled. The two layers and the matching-column indices are fixed; exchanging the two layers gives generally a different labelled vertex subset. The graph has \(2n\) vertices and degree \(n\). The parameter \(k\) is an integer in \([0,n]\), including both boundary values. The polynomial counts vertex subsets rather than isomorphism types, and each such subset contributes once.

For each matching column, use exactly one of four types: \(c\), both vertices omitted; \(x\), top omitted and bottom selected; \(y\), top selected and bottom omitted; \(d\), both vertices selected. The letters denote numbers of columns of those types, not graph parameters.

## Proof

**1. Domination structure.** If a set \(D\) meets both complete layers, then any omitted vertex has a selected neighbour in its own layer, and hence \(D\) dominates. If \(D\) misses \(A\), then each \(a_i\) can only be dominated through its matched neighbour \(b_i\), so all of \(B\) must be selected. The symmetric case gives \(A\) alone. Thus the only dominating sets meeting fewer than two layers are the two entire layers.

**2. Exact limited condition.** Fix a set meeting both layers. In the four-type notation, the numbers of omitted vertices in the top and bottom layers are respectively \(a=c+x\) and \(b=c+y\). A selected top vertex has exactly \(a\) omitted neighbours within its clique, plus one more precisely when its matched bottom vertex is omitted. Such a vertex of the latter kind exists exactly when \(y>0\). Consequently all selected top vertices obey the limit exactly when \(a+\mathbf1_{y>0}\le k\). In the bottom layer the analogous condition is \(b+\mathbf1_{x>0}\le k\). Since both layers are occupied, these inequalities are also sufficient. The conditions \(a<n\) and \(b<n\) enforce occupation of both layers.

For either exceptional whole-layer set, each selected vertex has exactly one omitted neighbour (its matched partner), and therefore these two sets are permitted exactly when \(k\ge1\). This proves the necessary-and-sufficient all-set classification.

**3. Enumeration.** For each feasible quadruple \((c,x,y,d)\), assign the four types to the \(n\) labelled columns in \(n!/(c!x!y!d!)\) ways. The selected vertices number \(x+y+2d\). Different type assignments yield different labelled sets, and every set meeting both layers has a unique type assignment. The exceptional whole layers are disjoint from this sum. Summing gives the claimed polynomial with no overcount.

**4. Sharp minima and their multiplicities.** Suppose \(1\le k<n\). Any admissible set meeting both layers has at most \(k\) omitted vertices from either layer, hence at least \(2(n-k)\) selected vertices. Equality requires \(a=b=k\). If \(x>0\) or \(y>0\), the corresponding tightened inequality in Step 2 rules out equality. Thus equality is possible only when \(x=y=0\), \(c=k\), and \(d=n-k\). Such a set exists and is obtained uniquely by choosing which \(k\) entire matched columns to omit; there are \(\binom nk\) choices. The only admissible sets missing a layer are the two full-layer sets of size \(n\). Comparing these two sizes proves the three interior cases, identifies every minimizer, and counts them.

When \(k=0\), the connectedness of \(R_n\) and the zero outside-neighbour limit force \(D=V(R_n)\), yielding size \(2n\) and count one. When \(k=n\), the degree constraint is automatic. A two-vertex dominating set must meet both layers, giving \(n^2\) ordered top/bottom choices; only for \(n=2\) do the two full layers also have size two. No one-vertex set dominates because \(n\ge2\). This finishes the minimum-count formula. For \(k=n\), multiplying the nonempty-subset generating polynomials for the two layers and adjoining the two full layers yields the stated simplified enumerator.

## Verification

A standalone Python file, `verify.py`, implements (i) the multinomial four-type formula and (ii) a separate exhaustive test of every labelled vertex subset directly against the graph-neighbourhood definition, without using the proposed type conditions. For every \(n\in\{2,\ldots,8\}\) and every \(k\in\{0,\ldots,n\}\), the complete coefficient vectors agree. The same test compares the least degree and its coefficient with the closed minimizer formula. Additional direct formula-versus-minimizer comparisons cover selected capacities for \(9\le n\le35\). Run `python3 verify.py` in the directory containing the file; the expected terminal marker is `VERIFY_OK`. This finite experiment is supporting evidence only: Steps 1–4 prove the universal statement.

For example, the exact polynomial for \(n=6\), \(k=3\) begins with \(22z^6\), while for \(n=6\), \(k=4\) it begins with \(15z^4\). In the first case the minimum sets comprise twenty common matched-column selections plus the two whole layers; in the second there are fifteen matched-column selections and no whole-layer minimizers.

## Relationship to prior work

The definition and graph-product motivation come from Božović, Radić, Kovijanić-Vukićević and Tepeh, and from Tepeh's 2026 paper on Cartesian products. Tepeh proves product inequalities and a sharp rook-graph result for two equal factors of order \(k+2\) (Proposition 8), not the all-subset polynomial above. An earlier documented rectangular-rook finding already determines \(\gamma_k^{\mathrm L}(K_m\square K_n)\) for all parameters, and classifies its minimizers when \(k<\min\{m,n\}\). For \(m=2\), its numerical minimum formula subsumes the numerical \(\gamma_k^{\mathrm L}\) formula here. We therefore make **no novelty claim** for the minimum cardinality itself or its previously covered low-capacity minimizers. The new portion is the complete all-set criterion, the polynomial for every size, and the minimizer counts in the range \(2\le k<n\), which are not consequences of a minimum-value formula alone.

This graph is a two-row rook graph and also a clique prism. It is **not** complete multipartite for general \(n\ge3\), so complete-multipartite formulas concern a different graph family. The ordinary domination case \(k=n\) is elementary and is included as a consistency boundary, not independently claimed as new.

## Limitations

The theorem is restricted to two-layer clique prisms and ordinary vertex-subset counting; it does not assert a formula for arbitrary Cartesian products or for arbitrary rook-graph dimensions. No infinite theorem follows from exhaustive computation alone. Bibliographic priority remains provisional: the inspected public full text of Tepeh's first preprint is from June 2026, and later revised full text was not independently read; equivalent all-set enumerators under \((0,k)\)-pitchfork-domination terminology could have escaped indexed searches. The theorem has received only self-review, not independent mathematical audit.

## References

1. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, initial public arXiv version June 21, 2026, arXiv:2606.22428. Full public text of its initial version inspected through a licensed/open ResearchGate transcription; especially Section 4.1, Proposition 8 and general product bounds. https://arxiv.org/abs/2606.22428
2. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On k-limited domination in graphs*, Computational and Applied Mathematics, DOI 10.1007/s40314-026-03902-2, available open access. https://doi.org/10.1007/s40314-026-03902-2
3. *Exact k-limited domination of rectangular rook graphs*, earlier recorded mathematical statement; its numerical formula and stated minimizer range are credited, not asserted anew (publication status unverified).
