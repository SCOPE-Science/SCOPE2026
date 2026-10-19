# Clique enumeration and full automorphism character of aperiodic Brandt commuting graphs

## Finding

For every integer \(n\ge2\), the commuting graph \(\Gamma_n\) of the aperiodic Brandt semigroup on its nonzero elements has precisely \(3^n-2^{n+1}+2\) inclusion-maximal cliques, classified explicitly below. Define the **maximal-clique size enumerator** \(M_n(z)=\sum_{K\text{ maximal}}z^{|K|}\) and the **ordinary clique polynomial** \(C_n(z)=\sum_{Q\text{ clique}}z^{|Q|}\), including the empty clique. Then

\[
M_n(z)=z^n+\sum_{\substack{s,t\ge1\\s+t\le n}}\frac{n!}{s!t!(n-s-t)!}\,z^{st+n-s-t},
\]

\[
C_n(z)=(1+z)^n+\sum_{\substack{s,t\ge1\\s+t\le n}}\frac{n!}{s!t!(n-s-t)!}(1+z)^{n-s-t}F_{s,t}(z),
\]

\[
F_{s,t}(z)=\sum_{a=0}^s\sum_{b=0}^t(-1)^{s-a+t-b}\binom{s}{a}\binom{t}{b}(1+z)^{ab}.
\]

The alternating clique sum has the simple value

\[
C_n(-1)=(-1)^{n+1}(2^n-2).
\]

The natural action of \(S_n\times C_2\), where \(C_2\) interchanges all sources and targets, acts on the set of **all** maximal cliques with permutation character

\[
\chi_n(\sigma,0)=3^{c(\sigma)}-2^{c(\sigma)+1}+2,
\qquad
\chi_n(\sigma,1)=3^{e(\sigma)}.
\]

Here \(c(\sigma)\) counts all cycles (including fixed points) and \(e(\sigma)\) counts even-length cycles of \(\sigma\). In fact, the previous literature establishes that this natural group is the full graph automorphism group. Restricting the maximal-clique permutation module to \(S_n\), the multiplicity of the rational Specht module \(S^\lambda\) is

\[
s_\lambda(1^3)-2s_\lambda(1^2)+2\mathbf 1_{\lambda=(n)},
\]

with \(s_\lambda(1^d)=\prod_{(i,j)\in\lambda}(d+j-i)/h_{ij}\), understood as zero when \(\lambda\) has more than \(d\) rows, and \(h_{ij}\) the hook length.

## Assumptions and scope

Let \([n]=\{1,\ldots,n\}\) and let \(B_n=\{0\}\cup\{e_{ij}:i,j\in[n]\}\) be the semigroup with \(0b=b0=0\) and

\[
e_{ij}e_{k\ell}=\begin{cases}e_{i\ell},&j=k,\\0,&j\ne k.\end{cases}
\]

The undirected simple commuting graph \(\Gamma_n\) has the \(n^2\) vertices \(e_{ij}\), distinct vertices being adjacent when the two products agree. Its omitted element \(0\) is central; no field or characteristic assumptions occur. Cliques are subsets, not multisets. Write \(D=\{e_{ii}:i\in[n]\}\). For any **ordered** pair \((S,T)\) of disjoint, nonempty subsets of \([n]\), put \(R=[n]\setminus(S\cup T)\) and

\[
K_{S,T}=\{e_{ij}:i\in S,j\in T\}\cup\{e_{rr}:r\in R\}.
\]

The classification is

\[
\operatorname{MaxCliques}(\Gamma_n)=\{D\}\ \sqcup\ \{K_{S,T}:S,T\ne\varnothing,\ S\cap T=\varnothing\}.
\]

## Proof

**1. Matrix-unit commutation.** For distinct units \(e_{ij}\) and \(e_{k\ell}\), equality of the two products forces both products to be zero. Indeed, if both were nonzero they would equal \(e_{i\ell}\) and \(e_{kj}\), forcing \(i=k\) and \(j=\ell\), contrary to distinctness; if only one is nonzero equality fails. Thus

\[
e_{ij}\sim e_{k\ell}\iff j\ne k\text{ and }\ell\ne i.
\]

Distinct diagonal units commute with one another; a diagonal \(e_{rr}\) commutes with a non-diagonal \(e_{ij}\) precisely when \(r\notin\{i,j\}\).

**2. Classification of all maximal cliques.** Suppose a clique \(Q\) contains a non-diagonal vertex. Define its non-diagonal source set \(S\) and target set \(T\). By step 1, no target of one selected non-diagonal unit can be the source of any selected non-diagonal unit. Hence \(S\cap T=\varnothing\), and \(S,T\) are both nonempty. Every non-diagonal unit in \(Q\) lies in \(S\times T\), and every diagonal unit lies outside \(S\cup T\). Consequently \(Q\subseteq K_{S,T}\), and this latter set is a clique by step 1.

Each \(K_{S,T}\) is maximal: all compatible diagonal vertices and all compatible units with sources in \(S\) and targets in \(T\) are already included. An additional diagonal unit with label in \(S\cup T\) is nonadjacent to an existing incident off-diagonal unit. An additional non-diagonal unit having either endpoint in \(R\) fails to commute with the included corresponding diagonal unit. A non-diagonal unit entirely on \(S\cup T\), but outside \(S\times T\), has a source in \(T\) or a target in \(S\); it therefore fails to commute with some member of \(S\times T\). Thus the inclusion is maximal.

If a clique contains no non-diagonal vertex, it is a subset of \(D\); the only maximal one is \(D\). In the other cases, \(S\) and \(T\) can be recovered uniquely from the sources and targets of non-diagonal units in \(K_{S,T}\); no double-counting occurs.

**3. Maximal-clique enumerator.** At fixed \(s=|S|\), \(t=|T|\), there are \(n!/(s!t!(n-s-t)!)\) ordered disjoint pairs. The corresponding clique size is \(st+n-s-t\). Adding \(D\) proves the formula for \(M_n\); summing its coefficients gives \(1+3^n-2\cdot2^n+1=3^n-2^{n+1}+2\).

**4. All cliques.** A clique without non-diagonal vertices contributes \((1+z)^n\). Otherwise, its selected off-diagonal edges uniquely determine disjoint, nonempty exact support sets \(S,T\), with every member of \(S\) used as a source and every member of \(T\) used as a target. Regard these as selected edges of \(K_{s,t}\), with no isolated vertex on either side. Inclusion–exclusion over uncovered source and target vertices gives exactly \(F_{s,t}(z)\) displayed above. The diagonal vertices in \(R\) may independently be included or omitted, contributing \((1+z)^{n-s-t}\). Summing over ordered disjoint supports proves \(C_n(z)\).

At \(z=-1\), all summands except \(s+t=n\) vanish. For \(s,t>0\), the inclusion–exclusion formula has value \(F_{s,t}(-1)=(-1)^{s+t+1}\): only the \(a=0\) or \(b=0\) terms survive, and their combined value is \((-1)^{s+t+1}\). Summing over the \(2^n-2\) ordered nontrivial bipartitions yields the stated alternating sum.

**5. Exact full-automorphism permutation character.** Relabeling by \(\sigma\in S_n\) sends \(K_{S,T}\) to \(K_{\sigma(S),\sigma(T)}\); simultaneous transpose sends \(K_{S,T}\) to \(K_{T,S}\). The all-diagonal clique \(D\) is always fixed. Without transpose, \(K_{S,T}\) is fixed if and only if the three-coloring of \([n]\) by \(S,T,R\) is constant on every cycle of \(\sigma\), with both the \(S\) and \(T\) colors occurring. With \(c(\sigma)\) cycles, there are \(3^{c(\sigma)}-2\cdot2^{c(\sigma)}+1\) such colorings. Adding \(D\) proves the first character formula.

With transpose, a fixed \(K_{S,T}\) must satisfy \(\sigma(S)=T\), \(\sigma(T)=S\), and \(\sigma(R)=R\). On each odd cycle, every index must lie in \(R\); on each even cycle, there are exactly three admissible assignments: all \(R\), or either of two alternating \(S,T\) choices. Every non-all-\(R\) coloring has both \(S,T\) nonempty. Hence there are \(3^{e(\sigma)}-1\) such maximal cliques; after adjoining \(D\), this yields \(\chi_n(\sigma,1)=3^{e(\sigma)}\).

Finally, the ordinary \(S_n\)-permutation representation on all functions \([n]\to[d]\) has character \(d^{c(\sigma)}\) and, by the classical Schur–Weyl decomposition, Specht multiplicities \(s_\lambda(1^d)\). The difference \(3^{c(\sigma)}-2\cdot2^{c(\sigma)}+2\) therefore gives the stated multiplicity formula. (Its integrality and nonnegativity also follow from the explicit permutation action.)

## Verification

The standalone \(\texttt{verify.py}\) constructs the \(n^2\) units explicitly and compares their **actual semigroup products**. Independently, it uses Bron–Kerbosch recursion to enumerate every inclusion-maximal clique through \(n=6\), checks the classified form and its size multiset, and enumerates every clique through \(n=5\) against the closed polynomial. It also enumerates every permutation and both transpose states through \(n=6\), comparing actual fixed maximal cliques to the character values. It reports \(\texttt{VERIFY_OK_BRANDT_CLIQUES_CHARACTER}\). Finite checks confirm tested cases only; the proof above covers all \(n\).

For illustration,

\[
C_4(z)=1+16z+66z^2+72z^3+7z^4,
\]


## Relationship to prior work

Araújo, Bentz and Konieczny (arXiv:1205.1664, first posted 8 May 2012) treat the commuting graph of the **entire** symmetric inverse semigroup, especially its maximum clique size and diameters. Kumar, Dalal and Pandey (arXiv:2010.05000, first posted 10 October 2020) analyze the exact aperiodic Brandt commuting graph, prove its adjacency criterion and clique-number theorem, and determine its graph automorphism group. Their proof of the maximum-clique bound uses the source–target cut structure for **largest** cliques, so that ingredient is not claimed as new.

The present statement instead enumerates **every inclusion-maximal clique** and **every clique of every cardinality**, including diagonal-containing and nonmaximum cliques, and gives the exact permutation character of the automorphism group on the maximal cliques. Neither inspected source states the resulting complete clique polynomial or full equivariant character. A prior equivalent result under simplicial, graph-polynomial or Rees-matrix terminology remains possible; no unrestricted historical priority assertion is made.

## Limitations

The semigroup has trivial maximal subgroup and the graph includes every nonzero matrix unit, not arbitrary elements of larger Brandt semigroups \(B_n(G)\) or the full symmetric inverse semigroup. No homotopy-type, integral homology or characteristic-dependent claim is inferred from the Euler evaluation. The finite verifier tests only sizes through \(n=6\), not the unbounded theorem. Full literature-priority review and independent mathematical audit remain outstanding.

## References

1. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664, first version 8 May 2012, https://arxiv.org/abs/1205.1664. Full text: https://arxiv.org/pdf/1205.1664.
2. J. Kumar, S. Dalal and P. Pandey, *On the Commuting Graphs of Brandt Semigroups*, arXiv:2010.05000, first version 10 October 2020, https://arxiv.org/abs/2010.05000. Full text: https://arxiv.org/pdf/2010.05000.
3. Classical Schur–Weyl duality and the hook-content formula (standard representation-theoretic identities; not claimed as new).
