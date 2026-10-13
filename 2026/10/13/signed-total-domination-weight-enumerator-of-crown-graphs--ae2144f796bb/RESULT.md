# Signed-total-domination weight enumerator of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\), where the deleted perfect matching is \(M_n=\{a_ib_i:1\le i\le n}\). A labeling \(f:V(\operatorname{Cr}_n)\to\{-1,1\}\) is a signed total dominating function when every open-neighborhood sum is at least \(1\).

Put
\[
A_f=\sum_{i=1}^n f(a_i),\qquad B_f=\sum_{i=1}^n f(b_i),
\]
and define
\[
\varepsilon_n=\begin{cases}2,&n\text{ even},\\3,&n\text{ odd}.\end{cases}
\]
Then \(f\) is signed total dominating if and only if
\[
A_f\ge\varepsilon_n\qquad\text{and}\qquad B_f\ge\varepsilon_n.
\]
Equivalently, writing \(h_n=(n+\varepsilon_n)/2\), each bipartition class contains at least \(h_n\) vertices labeled \(+1\).

Therefore, if \(u\) records the number of positive vertices in the \(A\)-class and \(v\) records the number in the \(B\)-class, the complete bivariate enumerator is
\[
E_n(u,v)=P_n(u)P_n(v),\qquad P_n(z)=\sum_{k=h_n}^n\binom{n}{k}z^k.
\]
The weight enumerator is
\[
W_n(t)=\left(\sum_{k=h_n}^n\binom{n}{k}t^{2k-n}\right)^2.
\]
Consequently,
\[
\gamma_{st}(\operatorname{Cr}_n)=\begin{cases}4,&n\text{ even},\\6,&n\text{ odd},\end{cases}
\]
and the number of minimum-weight signed total dominating functions is
\[
\begin{cases}
\binom{n}{n/2+1}^2,&n\text{ even},\\
\binom{n}{(n+3)/2}^2,&n\text{ odd}.
\end{cases}
\]
The total number of signed total dominating functions is
\[
\begin{cases}
\left(\dfrac{2^n-\binom{n}{n/2}}{2}\right)^2,&n\text{ even},\\
\left(2^{n-1}-\binom{n}{(n+1)/2}\right)^2,&n\text{ odd}.
\end{cases}
\]

A parity-sensitive deletion phenomenon follows. For even \(n\), the signed total dominating functions of \(\operatorname{Cr}_n\) are exactly those of \(K_{n,n}\). For odd \(n\), deleting the perfect matching removes exactly the labelings for which at least one bipartition-class sum is \(1\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The claim is for connected crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\). The signed total domination convention is \(f:V(G)\to\{-1,1\}\) with \(\sum_{x\in N(v)}f(x)\ge1\) for every vertex \(v\). The theorem classifies every such function, not only minimum-weight ones.

## Proof
For each \(i\), the open neighborhood of \(a_i\) is \(B\setminus\{b_i\}\). Therefore
\[
\sum_{x\in N(a_i)}f(x)=B_f-f(b_i).
\]
If \(f\) is signed total dominating, then not all vertices of \(B\) can have label \(-1\), so some \(b_i\) has label \(+1\). For that index the condition gives \(B_f-1\ge1\), hence \(B_f\ge2\). Conversely, if \(B_f\ge2\), then for every \(i\),
\[
B_f-f(b_i)\ge B_f-1\ge1,
\]
so all vertices in \(A\) satisfy the required inequality. Thus the constraints arising from vertices of \(A\) are equivalent to \(B_f\ge2\). By symmetry, the constraints from vertices of \(B\) are equivalent to \(A_f\ge2\).

The sum of \(n\) values in \(\{-1,1\}\) has the same parity as \(n\). Hence the least possible side sum at least \(2\) is \(2\) for even \(n\) and \(3\) for odd \(n\). This proves the criterion with \(\varepsilon_n\).

If a side has \(k\) positive vertices, its sum is \(2k-n\), so the criterion is \(k\ge h_n=(n+\varepsilon_n)/2\). The two sides can then be chosen independently, giving the product enumerator and the weight enumerator. The minimum weight is twice the least admissible side sum, and the minimum-layer counts are the corresponding binomial coefficients squared. The displayed total counts follow from binomial symmetry.

For \(K_{n,n}\), every vertex on one side sees the entire opposite side, so the condition is merely that each side sum be at least \(1\). When \(n\) is even, parity raises this to at least \(2\), identical to the crown criterion. When \(n\) is odd, the complete bipartite threshold is \(1\), whereas the crown threshold is \(3\); this proves the final deletion comparison.

## Verification
The standalone verifier exhaustively enumerates all \(2^{2n}\) sign labelings for \(3\le n\le8\). It checks the open-neighborhood inequalities directly, compares the accepted labelings with the side-sum criterion, checks every coefficient of the bivariate positive-label enumerator, and verifies the minimum weight and minimum-layer multiplicity. The computation is a finite regression check; the proof above establishes the statement for every \(n\ge3\).

## Relationship to prior work
Zelinka defined signed total domination and proved a regular-graph lower bound, then determined \(\gamma_{st}\) for complete graphs, cycles, prisms, and complete bipartite graphs. In particular, the complete-bipartite result gives \(\gamma_{st}(K_{n,n})=4\) for even \(n\) and \(2\) for odd \(n\). The crown theorem above refines that scalar comparison after deleting a perfect matching by classifying every feasible sign labeling and exhibiting an exact parity-sensitive change in the whole family.

Liang later determined signed domination, signed total domination, and minus domination numbers for arbitrary complete multipartite graphs. Crown graphs are not complete multipartite for \(n\ge3\), and those scalar complete-multipartite formulas do not imply the all-function crown enumerator. Henning's foundational treatment develops general bounds for signed total domination and the upper signed total domination parameter; no crown-specific all-function formula is stated in the accessible material inspected.

## Limitations
The theorem is specific to crown graphs. The originality check included direct searches under “crown graph,” “complete bipartite minus perfect matching,” and signed-total-domination terminology, plus comparison with the accessible full text of the complete-multipartite paper and the primary 2001 article. No claim of exhaustive bibliographic uniqueness is made. The exact day \(2001\)-\(01\)-\(01\) used as the earliest public-source date comes from an institutional repository metadata record; the journal issue itself identifies the year 2001.

## References
1. B. Zelinka, “Signed total domination number of a graph,” *Czechoslovak Mathematical Journal* 51 (2001), 225–229. DOI: 10.1023/A:1013782511179.
2. H. Liang, “Signed and Minus Domination in Complete Multipartite Graphs,” arXiv:1205.0343v1, first posted 2012-05-02; later *Ars Combinatoria* 126 (2016), 133–142.
3. M. A. Henning, “Signed total domination in graphs,” *Discrete Mathematics* 278 (2004), 109–125. DOI: 10.1016/j.disc.2003.06.002.
