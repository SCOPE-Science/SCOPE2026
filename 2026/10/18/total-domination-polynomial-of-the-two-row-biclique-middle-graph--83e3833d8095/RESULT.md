# Total-domination polynomial of the two-row biclique middle graph

## Finding

For every integer \(n\geq3\), let \(H_n=M(K_{2,n})\), with the middle-graph construction specified below. Its complete ordinary total-domination polynomial is

\[
\boxed{D_t(H_n;z)=z^n(1+z)^n\left[\bigl((2+z)^n-2\bigr)(1+z)^2-2n\right].}
\]

Thus the coefficient of \(z^k\) counts **all** total dominating vertex subsets of \(H_n\) having size \(k\). In particular,

\[
\gamma_t(H_n)=\begin{cases}4,&n=3,\\ n,&n\ge4,\end{cases}
\qquad
\#\{S:|S|=\gamma_t(H_n),\ S\text{ total dominating}\}
=\begin{cases}24,&n=3,\\2^n-2n-2,&n\ge4.\end{cases}
\]

For \(n\ge4\), the minimum sets are exactly those selecting **one** of \(a_i,b_i\) in each column, with at least two selected vertices in each row, and selecting no original vertices. The previously known scalar minimum is recovered, whereas the exact count of every feasible size is the main assertion. An equivalent probability identity is that, if vertices are independently selected with probability \(p\in[0,1]\), then

\[
\Pr(S\text{ is total dominating})
=p^n\left[(2-p)^n-2(1-p)^n-2n(1-p)^{n+2}\right].
\]

Consequently, for each fixed \(\lambda\ge0\), at \(p=1-\lambda/\sqrt{n}\) (for sufficiently large \(n\)), this probability tends to \(e^{-\lambda^2}\). It tends to \(1\) if \(\sqrt n(1-p_n)\to0\), and to \(0\) if \(\sqrt n(1-p_n)\to\infty\).

## Assumptions and scope

All graphs are finite, undirected, and simple, and \(n\ge3\) is an integer. A *total dominating set* of a graph is a vertex subset \(S\) for which every vertex, including those in \(S\), has a neighbor in \(S\). For any graph \(G\), its *middle graph* \(M(G)\) has a vertex for each original vertex and each original edge; two edge-vertices are adjacent precisely when the edges share an endpoint, and an edge-vertex is adjacent to its two endpoints. Distinct original vertices are nonadjacent.

Fix the two vertices \(u,v\) of the size-two part of \(K_{2,n}\), and label its remaining vertices \(y_1,\ldots,y_n\). Denote the edge-vertices associated with \(uy_i\) and \(vy_i\) by \(a_i\) and \(b_i\), respectively. The graph \(H_n\) has \(3n+2\) vertices and the following exact open neighborhoods:

\[
\begin{aligned}
N(u)&=\{a_1,\ldots,a_n\},&N(v)&=\{b_1,\ldots,b_n\},\\
N(y_i)&=\{a_i,b_i\},\\
N(a_i)&=\{u,y_i,b_i\}\cup\{a_j:j\ne i\},\\
N(b_i)&=\{v,y_i,a_i\}\cup\{b_j:j\ne i\}.
\end{aligned}
\]

The two colors of edge-vertices, the original hubs, and the \(y_i\) are labeled and distinguished; no quotient by graph automorphisms is taken. For \(n=1,2\), the compact formula need not apply and no assertion about it is made.

## Proof

**Step 1: An exact admissibility criterion.** Fix a candidate set \(S\). Let \(A=\{i:a_i\in S\}\) and \(B=\{i:b_i\in S\}\), writing \(r=|A|\) and \(s=|B|\). The vertices \(y_i\) have only \(a_i,b_i\) as neighbors, so each column must contain an edge-vertex: \(A\cup B=[n]\). Similarly \(u\) and \(v\) force \(r,s\ge1\). Conversely, under these conditions, every \(y_i,u,v\), every unselected \(a_i\), and every unselected \(b_i\) is dominated: any unselected edge-vertex sees at least one selected edge-vertex in its own row. If \(r\ge2\), each selected \(a_i\) has a distinct selected neighbor in the first row; if \(r=1\), its unique selected member \(a_i\) is dominated precisely when \(u\in S\), or \(y_i\in S\), or \(b_i\in S\). The same statement with \(v\) and \(b_i\) holds for \(s=1\). These conditions are necessary and sufficient, with no assumed containment of \(S\) in the edge-vertex part.

**Step 2: Counting all edge selections.** Selecting a nonempty subset of \(\{a_i,b_i\}\) in each column gives generating factor \(2z+z^2\), hence \((2z+z^2)^n\). Exactly two edge selections have an empty row (all \(a_i\) or all \(b_i\)), each of weight \(z^n\). For \(n\ge3\), it is impossible for both rows to have exactly one selected edge-vertex. For a fixed singleton row, the possibilities are either a single unpaired edge-vertex in one chosen column and the opposite row selected everywhere else, contributing \(nz^n\), or a single paired column and the opposite row selected in all columns, contributing \(nz^{n+1}\). The two singleton-row cases are disjoint.

Therefore the edge selections with both row sizes at least two contribute

\[
(2z+z^2)^n-(2+2n)z^n-2nz^{n+1}.
\]

All \(n+2\) original vertices may then be selected independently, contributing \((1+z)^{n+2}\). For the paired singleton-row configurations, the selected opposite-row edge-vertex dominates the singleton, so all original vertices again remain free, contributing \(2nz^{n+1}(1+z)^{n+2}\). For an unpaired singleton-row configuration, at least one of the two vertices \(u,y_i\) (or \(v,y_i\)) must be selected to dominate the selected singleton; its generating factor is \((1+z)^2-1=2z+z^2\), and the other \(n\) original vertices remain free. The contribution is \(2nz^n(2z+z^2)(1+z)^n\).

Adding all three disjoint cases yields

\[
\begin{aligned}
D_t(H_n;z)={}&\left[(2z+z^2)^n-(2+2n)z^n-2nz^{n+1}\right](1+z)^{n+2}\\
&+2nz^{n+1}(1+z)^{n+2}+2nz^n(2z+z^2)(1+z)^n\\
={}&z^n(1+z)^n\left[\bigl((2+z)^n-2\bigr)(1+z)^2-2n\right],
\end{aligned}
\]

which proves the polynomial identity.

**Step 3: The minimum and its multiplicity.** The constant term of the bracket is \(2^n-2n-2\). For \(n\ge4\) this is positive, so the first nonzero coefficient of \(D_t(H_n;z)\) is that number at degree \(n\). For \(n=3\), the bracket's constant term vanishes and its coefficient of \(z\) is \(3\cdot2^2+2(2^3-2)=24\), so the minimum is four and its multiplicity is \(24\). The known scalar minimum agrees with Proposition 2.15 of Kazemnejad et al. (2022).

**Step 4: Random selection and the critical window.** Write \(q=1-p\). For independent Bernoulli selection, the weight enumerator identity gives \(\Pr(S\text{ total dominating})=q^{3n+2}D_t(H_n;p/q)\) for \(q>0\), simplifying to
\[
p^n\bigl((2-p)^n-2q^n-2nq^{n+2}\bigr).
\]
The identity extends to \(q=0\) by continuity. The main term is \((1-q^2)^n\), since \(p(2-p)=1-q^2\). For \(q=\lambda/\sqrt n\), this tends to \(e^{-\lambda^2}\), while the remaining nonnegative correction is bounded by \(2(n+1)(pq)^n\), tending to zero. If \(\sqrt n q\to\infty\), the probability is at most \((1-q^2)^n\to0\). If \(\sqrt n q\to0\), the same formula shows the correction vanishes and the main term tends to one. This establishes the stated transition.

## Verification

The standalone program `verify.py` builds each middle graph directly from its original incidences, computes open-neighborhood bitmasks, and exhaustively tests every vertex subset for total domination. It independently expands the claimed closed polynomial by integer binomial convolution. For \(n=3,4,5,6\), the program checked \(2^{11}+2^{14}+2^{17}+2^{20}=1{,}198{,}080\) candidate subsets and compared *every* coefficient, including the minimum-cardinality term. Invoke `python3 verify.py`; the recorded run is in `verification_output.txt`. These finite computations are reproducibility checks, not substitutes for the all-\(n\) proof above.

## Relationship to prior work

Kazemnejad, Pahlavsay, Palezzato, and Torielli (2022, arXiv:2204.07040, Proposition 2.15) determine the **total-domination number** of middle graphs of complete bipartite graphs, including the two-row subfamily. Their statement does not determine the distribution of all feasible cardinalities. Earlier, Latheeshkumar (2017, thesis, Section 4.3) provides total-domination polynomials for middle graphs of stars and graphs formed by attaching pendant leaves to a core; these are not the present leaf-free bicliques. Hu (2016) gives general total-domination polynomial reductions, not this explicit family formula. The present claim refines the scalar invariant to a full enumerator and its exact Bernoulli success law. Bibliographic checks do not establish absolute publication priority.

## Limitations

The formula has been proved for all integer \(n\ge3\), without a claim about the excluded smaller orders. The Bernoulli result is a consequence of the same theorem, not an independent empirical observation. Reproducibility checks stop at \(n=6\), whereas the proof covers all \(n\ge3\). The claim does not address larger first-part sizes \(K_{m,n}\) with \(m\ge3\). An unindexed equivalent enumeration, later correction, or overlooked treatment remains a bibliographic risk. No independent external verification has been performed.

## References

1. F. Kazemnejad, B. Pahlavsay, E. Palezzato, M. Torielli, *Total domination number of middle graphs*, arXiv:2204.07040 (first posted 13 April 2022); *Electronic Journal of Graph Theory and Applications* 10 (2022), 275–288. https://arxiv.org/abs/2204.07040 ; https://doi.org/10.5614/ejgta.2022.10.1.19 .
2. A. R. Latheeshkumar, *Total Domination Polynomials: A New Approach*, Ph.D. thesis, University of Calicut (2017), Section 4.3. https://scholar.uoc.ac.in/items/e118d633-90ec-4fe3-b284-a78eb20f4fc3 .
3. J. Hu, *Total domination polynomials of graphs*, arXiv:1607.00400 (2016), Sections 1–2. https://arxiv.org/abs/1607.00400 .
4. F. Kazemnejad et al., *Domination number of middle graphs*, arXiv:2008.02975 (2020). https://arxiv.org/abs/2008.02975 .
