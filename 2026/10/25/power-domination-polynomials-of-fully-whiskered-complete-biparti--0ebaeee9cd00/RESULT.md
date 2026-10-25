# Power-domination polynomials of fully whiskered complete bipartite graphs

## Finding
For all integers \(p,q\ge 2\), let \(G_{p,q}=K_{p,q}\circ K_1\) be the graph obtained by adjoining one private pendant leaf to each vertex of the complete bipartite graph \(K_{p,q}\). The entire power-domination polynomial \(\mathcal P(G_{p,q};z)\), counting power-dominating vertex subsets by cardinality, is
\[
\begin{aligned}
\mathcal P(G_{p,q};z)={}&F_p(z)F_q(z)\\
&+A_p(z)(1+z)^q+B_p(z)((1+z)^q-1)\\
&+A_q(z)(1+z)^p+B_q(z)((1+z)^p-1)\\
&+C_p(z)C_q(z),
\end{aligned}
\]
where, for every integer \(n\ge2\),
\[
\begin{aligned}
F_n(z)&=(1+z)^{2n}-(1+z)^n,\\
A_n(z)&=(2z+z^2)^n-z^n,\\
B_n(z)&=n\bigl((2z+z^2)^{n-1}-z^{n-1}\bigr),\\
C_n(z)&=z^n+nz^{n-1}.
\end{aligned}
\]
In particular,
\[
\gamma_P(G_{p,q})=2,
\]
and the number of minimum power-dominating sets is
\[
[z^2]\mathcal P(G_{p,q};z)=
\begin{cases}
22,&p=q=2,\\
4\max\{p,q\}+3,&\min\{p,q\}=2<\max\{p,q\},\\
pq,&p,q\ge3.
\end{cases}
\]
This is a complete enumeration in the one-leaf-corona case, distinct from the previously studied corona formulas with larger attached cliques.

## Assumptions and scope
Graphs are finite, simple, and undirected. Write \(A\sqcup B\) for the original bipartition, with \(|A|=p\) and \(|B|=q\). Every original (core) vertex \(v\) has one private pendant neighbor \(v'\); there are exactly \(2(p+q)\) vertices. The parameter restrictions \(p,q\ge2\) are part of the statement.

For any graph \(G\), start with a chosen set \(S\subseteq V(G)\). First observe \(N_G[S]\). Subsequently an observed vertex with exactly one unobserved neighbor forces that neighbor to become observed. The set \(S\) is *power dominating* precisely when this process can observe every vertex. Define \(\mathcal P(G;z)=\sum_{S\text{ power dominating}}z^{|S|}\); in particular the empty set does not count for a nonempty graph.

Call a private core–leaf pair *touched* if \(S\) contains at least one member, and *untouched* otherwise. Say that a part is *core-supported* when at least one original vertex in that part belongs to \(S\).

## Proof
**Lemma (six disjoint support classes).** For \(p,q\ge2\), a set \(S\) is power dominating exactly in one of these six mutually exclusive cases:

1. Both parts are core-supported.
2. Only \(A\) is core-supported; every core–leaf pair in \(A\) is touched.
3. Only \(A\) is core-supported; exactly one pair in \(A\) is untouched and at least one private leaf of \(B\) belongs to \(S\).
4. Only \(B\) is core-supported, with every pair in \(B\) touched.
5. Only \(B\) is core-supported, with exactly one pair in \(B\) untouched and at least one private leaf of \(A\) in \(S\).
6. Neither part is core-supported; \(S\) consists of private leaves and leaves at most one untouched pair in each part.

*Proof of the lemma.* When both parts contain a selected core, every core vertex is observed immediately, and then each remaining private leaf is either observed or is the unique unobserved neighbor of its core. This proves case 1.

Assume next that \(A\) but not \(B\) contains a selected core. Every \(B\)-core is observed at the domination step, while an \(A\)-core is observed there exactly if its own pair is touched. If no pair in \(A\) is untouched, every core is observed and all remaining private leaves can be forced. If precisely one \(A\)-pair is untouched, denote its core by \(a\). A \(B\)-core can force \(a\) exactly if its private leaf has already been observed. Since no \(B\)-core is selected, this happens exactly when that private leaf is selected in \(S\). Once \(a\) is forced, all remaining private leaves are forced by their cores. If two or more \(A\)-pairs are untouched, no \(B\)-core can force an unobserved \(A\)-core because it has at least two such unobserved neighbors. Also, no selected \(A\)-core is adjacent to an untouched \(A\)-core, and a private leaf has no other neighbors. Consequently the process cannot finish. If exactly one \(A\)-pair is untouched but no \(B\)-private leaf was selected, every observed \(B\)-core has the two unobserved neighbors consisting of \(a\) and its own private leaf, and the process again stalls. These observations establish precisely cases 2 and 3. Exchanging \(A\) and \(B\) establishes cases 4 and 5.

Finally suppose no core is selected, so every selected vertex is a private leaf. Immediately after the domination step the observed cores are exactly those whose own leaves were selected; their private leaves are also observed. Suppose there is at most one untouched pair on each side. Since both side sizes are at least two, there is at least one observed core in each side; such a core has no unobserved private neighbor. It can force the lone unobserved core on the opposite side if that exists. After these at most two core-forces, every core is observed and the remaining private leaves can be forced. Conversely, if some side has two untouched pairs, their two cores are unobserved. Every observed core on the opposite side has at least those two unobserved neighbors and cannot force either; and no pendant vertex can observe either untouched core. Even if a single core on the opposite side is eventually forced, the two untouched cores remain unobserved. Thus the process cannot finish. This proves case 6 and the lemma. \(\square\)

We now count these disjoint cases. On a part of size \(n\), the weight enumerator of choices containing at least one *core* is \(F_n(z)=(1+z)^{2n}-(1+z)^n\), because choices consisting exclusively of private leaves are subtracted. Hence case 1 contributes \(F_pF_q\).

For case 2, every pair on \(A\) must be touched. Such a pair can contribute one of its two vertices (weight \(2z\)) or both (weight \(z^2\)). Of all \((2z+z^2)^p\) choices, exactly the single choice consisting of all \(A\)-private leaves has no selected \(A\)-core, and must be excluded. This gives \(A_p(z)\). Every private leaf on \(B\) is independently optional, contributing \((1+z)^q\). Case 3 has \(p\) choices for the unique untouched \(A\)-pair, with the remaining \(p-1\) pairs touched and at least one selected core, giving \(B_p(z)\); the set of selected \(B\)-leaves must be nonempty, giving \((1+z)^q-1\). Interchanging parts counts cases 4 and 5. In case 6, on each side either all \(n\) private leaves are chosen or exactly one is omitted; this gives \(C_n(z)=z^n+nz^{n-1}\). Their choices are independent, contributing \(C_pC_q\). Summing the six classes proves the displayed polynomial.

Every power-dominating set has cardinality at least two: there is no constant or degree-one contribution in the formula for \(p,q\ge2\), and a pair of selected cores from opposite parts always succeeds. To extract the coefficient of degree two, observe \([z]F_n=n\), \([z^2]A_2=3\), \([z]B_2=2\), and \(A_n\) has minimum degree \(n\), while \(B_n\) has minimum degree \(n-1\). Similarly \(C_n\) has minimum degree \(n-1\). If both part sizes exceed two, only \(F_pF_q\) contributes degree two, yielding \(pq\). If exactly one side has size two, the additional terms contribute \(3+2\max\{p,q\}\), yielding \(4\max\{p,q\}+3\). When both sides have size two, the two one-core-side contributions and the leaf-only contribution combine with the core-supported contribution to give \(22\). \(\square\)

## Verification
The standalone `verify.py` independently constructs adjacency lists for the original graph and applies the original domination step and forcing rule to every vertex subset for eight parameter pairs. For each board it computes the cardinality distribution by direct observation and compares every coefficient with a separately implemented polynomial construction. It also checks the degree-two coefficient and tests the symbolic minimum-coefficient formula for every \(2\le p,q\le20\). The exact output is recorded in `verification_output.txt`: eight graphs, 173,312 exhaustively checked subsets, 361 symbolic parameter pairs, and `VERIFY_OK`.

## Relationship to prior work
Brimkov, Patel, Suriyanarayana, and Teich introduced the power-domination polynomial (arXiv:1805.10984v1, first publicly posted 28 May 2018). Their corona construction handles attached cliques of size larger than one and they explicitly highlight the one-leaf corona \(G\circ K_1\) as a distinct computation question. The present result answers that counting problem for the two-parameter base family of complete bipartite graphs; it does **not** claim a formula for arbitrary bases. Yuliana and collaborators consider power-domination **numbers** for certain corona products but not the present all-cardinality polynomial. Bjorkman and collaborators study sensor-failure reliability on unwhiskered complete multipartite graphs, a different graph class. Published enumerations for book graphs, double stars, and spider trees similarly do not imply the formula because their neighborhood and forcing structures are different.

## Limitations
Only the ordinary power-domination process and fully whiskered complete bipartite bases with \(p,q\ge2\) are covered. No statement is made for star bases, other corona attachments, or arbitrary graph bases. Finite exhaustive checks corroborate rather than replace the proof. Equivalent formulas in unindexed or inaccessible publications cannot be ruled out by the literature inspection.

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (first posted 2018-05-28), https://arxiv.org/abs/1805.10984.
2. I. Yuliana, D. Dafik, I. H. Agustin, and D. A. Retnowardani, *On the power domination number of corona product and join graphs*, Journal of Physics: Conference Series 1211 (2019), 012020, DOI 10.1088/1742-6596/1211/1/012020.
3. B. Bjorkman, Z. Brennan, M. Flagg, and J. Koch, *Power domination with random sensor failure*, arXiv:2312.12259v1 (first posted 2023-12-19), https://arxiv.org/abs/2312.12259.
