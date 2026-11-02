# Independent-dominating-set polynomial of two-token complete bipartite graphs

## Finding
For each integer pair \(m,n\ge2\), let \(H=F_2(K_{m,n})\). Its vertices are unordered pairs of distinct vertices of \(K_{m,n}\); an edge replaces one token along one edge of the base graph without collision. Write its bipartition as \(A\sqcup B\), of sizes \(m,n\).

An independent dominating set of \(H\) is equivalently an inclusion-maximal independent set. Define \(P=\binom A2\cup\binom B2\) and \(X=A\times B\), interpreted as families of token configurations. All maximal independent sets are exactly
\[
P,\qquad I(S,T)=\binom S2\cup\binom T2\cup((A\setminus S)\times(B\setminus T)),
\]
where \(S\subsetneq A\), \(T\subsetneq B\), and \(|S|,|T|\in\{0\}\cup\{2,3,\ldots\}\). This parametrization is injective.

Consequently, the maximal-independent-set (independent-dominating-set) enumerator \(D_{m,n}(z)=\sum_I z^{|I|}\) is
\[
D_{m,n}(z)=z^{\binom m2+\binom n2}+\sum_{\substack{0\le s<m,\ s\ne1\\0\le t<n,\ t\ne1}}\binom ms\binom nt z^{\binom s2+\binom t2+(m-s)(n-t)}.
\]
The number of maximal independent sets is \(D_{m,n}(1)=1+(2^m-m-1)(2^n-n-1)\).

Let \(a=\max\{m,n\}\), \(b=\min\{m,n\}\). The independent domination number, the least size of such a set, is
\[
i(H)=\begin{cases}2 &(a,b)=(2,2),\\2a-3&b=2<a,\\a+\binom{b-1}2-1&b\ge3.\end{cases}
\]
The only maximum independent sets are \(P\) if \(|P|>|X|\), \(X\) if \(|X|>|P|\), and both if their sizes tie. A tie occurs exactly when \((m-n)^2=m+n\), or, with unordered part sizes, \((m,n)=(\binom{d+1}2,\binom d2)\) for integer \(d\ge3\).

## Assumptions and scope
Simple undirected complete bipartite base graph, two *indistinguishable* tokens at different vertices, one legal token slide per edge of \(H\), \(m,n\ge2\). Maximal means inclusion-maximal, not necessarily maximum-cardinality. The polynomial enumerates labelled vertex-subsets \(I\) of the fixed labelled token graph, without quotienting by automorphisms.

## Proof
Partition the vertices of \(H\) into same-class pairs \(P\) and mixed pairs \(X\). There are no edges within either family. The neighbours of an \(A\)-pair \(\{a,a'\}\) are exactly the mixed pairs with first coordinate \(a\) or \(a'\), and analogously for \(B\)-pairs.

Let \(I\) be maximal independent. If \(I\cap X=\varnothing\), every vertex of \(P\) must be chosen (as none of them is adjacent to another in \(P\)); hence \(I=P\). Otherwise let \(S\subset A\), \(T\subset B\) be the sets of endpoints incident with the chosen same-class pairs. Independence forces every chosen mixed pair to lie in \((A\setminus S)\times(B\setminus T)\). Maximality forces *all* these mixed pairs to be included because any missing such pair has no neighbour in the chosen same-class family. Their nonemptiness forces \(S\subsetneq A\) and \(T\subsetneq B\). Each nonempty active endpoint set has at least two vertices. Furthermore every possible internal pair of \(S\) or \(T\) must be included, since such pairs are independent from the chosen mixed rectangle. Conversely, for every indicated \(S,T\), the resulting \(I(S,T)\) is independent. Each omitted same-class pair touches an unused endpoint that meets some selected mixed pair (the rectangle has both coordinates nonempty); each omitted mixed pair meets an active endpoint covered by a selected same-class pair. Thus every omitted vertex has a chosen neighbour and \(I(S,T)\) is maximal. The chosen internal pairs recover \(S,T\) uniquely, proving injectivity. Counting choices of \(S,T\) and their sizes gives the displayed polynomial and total.

To minimize a maximal set, put \(f(s,t)=\binom s2+\binom t2+(m-s)(n-t)\). The exceptional set \(P\) has size \(p=\binom m2+\binom n2\). Suppose \(m=a\ge b=n\ge3\) and let \(k=s+t\). Then
\[
f(s,t)=mn+\binom k2-nk-(m-n)t.
\]
If \(k\le n-1\), use \(t\le k\) to obtain \(f\ge m(n-k)+\binom k2\ge m+\binom{n-1}2\). If \(k\ge n-1\), use \(t\le n-1\) and put \(d=k-(n-1)\ge0\) to obtain
\[
f\ge m+\binom{n-1}2+\frac{d(d-3)}2\ge m+\binom{n-1}2-1.
\]
The latter bound is attained at \(s=2,t=n-1\), both admissible. Also \(p\) exceeds this value by \(m(m-3)/2+n>0\). If \(n=2\), admissibility forces \(t=0\) and \(f(s,0)=2m+s(s-5)/2\), minimized at \(s=2\) (also at \(s=3\) when allowed), giving \(2m-3\) for \(m\ge3\), less than \(p\). For \(m=n=2\), the only maximal sets are \(P\) of size two and \(X\) of size four.

For the largest size, observe that \(f(s,t)\) has Hessian \(\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\), so it is convex on the rectangle \([0,m-1]\times[0,n-1]\). Its four corner values are \(mn\), \(\binom{m-1}2+n\), \(\binom{n-1}2+m\), and \(\binom{m-1}2+\binom{n-1}2+1\). The last three are each smaller than \(p\) at admissible nonzero corners; apparent equality at a forbidden singleton corner when \(m=n=2\) does not arise. Thus among admissible \(I(S,T)\), only \(I(\varnothing,\varnothing)=X\) can attain \(\max\{p,mn\}\), while \(P\) has size \(p\). The tie equality simplifies to \((m-n)^2=m+n\). Writing \(d=|m-n|\), its positive integer solutions with both parts at least two are \((d(d+1)/2,d(d-1)/2)\), \(d\ge3\).

## Verification
The file `verify_primary.py` constructs the two-token graph directly from pairs of original vertices, enumerates maximal independent sets as maximal cliques of its complement, and checks the entire enumerator for ten nontrivial parameter choices, including the tie case \((m,n)=(3,6)\). `verify_alternative.cpp` independently builds pair-state compatibility masks and performs an exact Bron–Kerbosch enumeration for the same cases. Both reported complete agreement on the size histograms, independent domination minima, and maximum multiplicities. These finite checks corroborate but do not replace the all-parameter proof.

## Relationship to prior work
De Alba, Carballosa, Leaños and Rivera proved the scalar independence number \(\alpha(F_2(K_{m,n}))=\max\{mn,\binom m2+\binom n2\}\) (Theorem 1.2, initially public in June 2016); that scalar result and the bipartition construction are not new claims here. Their formulation does not supply the maximal-set size enumerator, independent domination minimum, or all optimizers. Deepalakshmi et al. (2020) gave general two-token graph properties and bounds on independent-set size, not this full distribution. Two October 2026 preprints determine the unrestricted domination number of the same token graphs; unrestricted dominating sets need not be independent, and their formulas neither count independent dominating sets nor give their minimum. Their characterizations could offer an alternative starting point for deriving the present classification but do not state it.

## Limitations
This concerns only two tokens and complete bipartite base graphs, not larger token sets or general bipartite graphs. Existing 2016 work already gave the maximum *size*; the additional output consists of the entire size distribution, the minimum maximal size, and exact maximizer classification. A mathematically equivalent result in unindexed sources remains possible. The verification programs cover finite instances only.

## References
1. H. de Alba, W. Carballosa, J. Leaños, L. M. Rivera, "Independence and matching numbers of some token graphs," arXiv:1606.06370v1 (first submitted 2016-06-21), Theorem 1.2.
2. J. Deepalakshmi, G. Marimuthu, A. Somasundaram, S. Arumugam, "On the 2-token graph of a graph," AKCE Int. J. Graphs Combin. 17 (2020), 265–268, DOI:10.1016/j.akcej.2019.05.002.
3. E. Acosta Troncoso, I. Caldera Caldera, L. M. Rivera, "The domination number of the 2-token graph of the complete bipartite graph," arXiv:2610.31557v1 (2026), Theorem 1.1 and Lemma 2.2.
4. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, L. Stenger, "The domination number of the k-token graph of the complete bipartite graph," arXiv:2610.28936v1 (2026), Theorem 1.1.
