# All zero forcing sets of crown graphs

## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) have bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching is \(M=\{a_i b_i:1\le i\le n\}\). Thus \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\).

For an initial blue set \(S\), define the white-index sets
\[
I=\{i:a_i\notin S\},\qquad J=\{j:b_j\notin S\}.
\]
Then \(S\) is a zero forcing set if and only if
\[
|I|\le2,\qquad |J|\le2,
\]
and it is not the case that \(|I|=|J|=2\) with \(I=J\).

Equivalently, after restricting to complements with at most two vertices on each side, the only nonforcing complements are the aligned four-vertex sets
\[
\{a_i,a_j,b_i,b_j\}\qquad (1\le i<j\le n).
\]
Writing
\[
A_n(x)=x^n+n x^{n-1}+\binom n2 x^{n-2},
\]
the complete zero forcing polynomial is
\[
\mathcal Z(\operatorname{Cr}_n;x)=A_n(x)^2-\binom n2 x^{2n-4}.
\]
Therefore
\[
Z(\operatorname{Cr}_n)=2n-4
\]
and the number of minimum zero forcing sets is
\[
\binom n2^2-\binom n2
=\binom n2\left(\binom n2-1\right).
\]
The total number of zero forcing sets is
\[
\left(1+n+\binom n2\right)^2-\binom n2.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The zero forcing color-change rule is the standard rule: a blue vertex with exactly one white neighbor changes that neighbor to blue, and a set is zero forcing when repeated legal forces color every vertex blue.

The theorem is stated for \(n\ge3\), exactly the connected crown graphs. The case \(n=3\) satisfies \(\operatorname{Cr}_3\cong C_6\), so its polynomial is already implied by the known cycle formula; this boundary is included to make the structural statement uniform but is not asserted as a separately original special case.

## Proof
Put \(p=|I|\) and \(q=|J|\). A blue vertex \(a_i\) has exactly
\[
q-\mathbf 1_{\{i\in J\}}
\]
white neighbors, while a blue vertex \(b_i\) has exactly
\[
p-\mathbf 1_{\{i\in I\}}
\]
white neighbors.

First suppose \(p\ge3\). Every blue vertex in \(B\) then has at least \(p-1\ge2\) white neighbors in \(A\), so no force from \(B\) to \(A\) is possible. Forces from \(A\) to \(B\), if any, do not change \(p\). Even if all of \(B\) eventually becomes blue, each blue vertex in \(B\) still has at least two white neighbors in \(A\), so the process cannot finish. Thus every zero forcing set has \(p\le2\). By symmetry, it also has \(q\le2\).

Now let \(p=q=2\) and \(I=J\). Every blue \(a_i\) has index \(i\notin J\), hence sees both white vertices of \(B\); symmetrically every blue \(b_i\) sees both white vertices of \(A\). No first force exists, so such a set is not zero forcing.

It remains to prove sufficiency. Assume \(p,q\le2\) and exclude the aligned case above.

If \(p=0\), then for \(q=2\), writing \(J=\{j,k\}\), the blue vertex \(a_j\) is nonadjacent to \(b_j\) and has \(b_k\) as its unique white neighbor, so it forces \(b_k\); the case \(q=1\) then finishes immediately from any blue \(a_i\) with \(i\ne j\). The case \(q=0\) is already finished. The argument with \(A\) and \(B\) interchanged handles \(q=0\).

If \(p=q=1\), write \(I=\{i\}\) and \(J=\{j\}\). When \(i=j\), any blue \(a_k\) with \(k\ne i\) forces \(b_i\). When \(i\ne j\), because \(n\ge3\) there is \(k\notin\{i,j\}\); the blue vertex \(a_k\) forces \(b_j\). In either case the remaining single white vertex in \(A\) is then forced.

If \(p=2,q=1\), choose \(i\in I\setminus J\). Then \(b_i\) is blue, is nonadjacent to the white vertex \(a_i\), and is adjacent to the other white vertex in \(A\); hence \(b_i\) has a unique white neighbor and reduces to the previous \(p=q=1\) case. The case \(p=1,q=2\) is symmetric.

Finally, if \(p=q=2\) with \(I\ne J\), choose \(j\in J\setminus I\). Then \(a_j\) is blue, is nonadjacent to the white vertex \(b_j\), and is adjacent to the other white vertex in \(B\), so it forces that other vertex and reduces to the \(p=2,q=1\) case. This proves the characterization.

For the polynomial, independently choosing at most two omitted vertices from each bipartition class contributes
\[
A_n(x)^2=\left(\sum_{r=0}^2\binom nr x^{n-r}\right)^2.
\]
Exactly \(\binom n2\) of those choices are the forbidden aligned pairs \(I=J\) with \(|I|=2\), and each corresponding blue set has size \(2n-4\). Subtracting them gives the displayed polynomial. Its smallest nonzero degree and the coefficient in that degree give the two stated corollaries.

## Verification
A standalone exhaustive verifier accompanies this result. For every \(3\le n\le9\), it constructs \(\operatorname{Cr}_n\), tests every subset under the standard zero forcing process, compares the result with the stated \((I,J)\) criterion, checks every polynomial coefficient, and checks the minimum number and number of minimum sets. The finite computation is only a cross-check; the proof above establishes the theorem for every \(n\ge3\).

As a boundary check, \(n=3\) gives
\[
6x^2+18x^3+15x^4+6x^5+x^6,
\]
which agrees with the published cycle formula for \(C_6\).

## Relationship to prior work
The original zero forcing paper introduced \(Z(G)\) and was available online on 26 November 2007; its primary AMS classification includes 05C50. Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart later introduced the zero forcing polynomial and gave formulas for complete graphs, complete multipartite graphs, paths, cycles, and several other families.

Their complete multipartite result does not imply the crown formula: \(\operatorname{Cr}_n\) is obtained from \(K_{n,n}\) by deleting a perfect matching and is not complete multipartite for \(n\ge3\). Indeed, their formula gives
\[
\mathcal Z(K_{n,n};x)=n^2x^{2n-2}+2n x^{2n-1}+x^{2n},
\]
whereas deleting the matching lowers the zero forcing number by two and creates a five-degree polynomial support. Their cycle formula covers only the boundary \(\operatorname{Cr}_3\cong C_6\).

A full-text crown-graph paper by Raghavan Unnithan, Kannan, and Jathavedan defines exactly the same object \(K_{n,n}-M\), but studies betweenness centrality rather than zero forcing. Searches under the aliases “crown graph”, “bipartite double cover of a complete graph”, “tensor product with \(K_2\)”, and “bipartite Kneser graph \(H_{n,1}\)” did not expose an all-zero-forcing-set classification or polynomial that implies this theorem.

## Limitations
The theorem concerns ordinary zero forcing only; it makes no claim about signed, skew, positive-semidefinite, connected, or other forcing variants. It does not determine minimum rank or maximum nullity.

A 2013 item by Leah S. Mays titled “The Zero Forcing Number Of Bipartite Graphs” is cited by later literature, but its original full text was not obtainable from the accessible link during this comparison. The later source attributes to it the standard scalar formula for complete bipartite graphs, not crown graphs. This leaves a residual access risk for hidden same-object scalar material, although such a scalar result alone would not imply the all-set characterization or polynomial proved here.

No literature search can logically prove global novelty; the originality conclusion is a comparison against the named inspected sources, aliases, and database results. The case \(n=3\) is explicitly treated as previously covered by the cycle formula.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009. Available online 26 November 2007.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 26 January 2018.
3. S. K. Raghavan Unnithan, B. Kannan, and M. Jathavedan, “Betweenness Centrality in Some Classes of Graphs,” *International Journal of Combinatorics* (2014), Article 241723. DOI: 10.1155/2014/241723.
4. M. R. Raksha and C. Dominic, “Some properties of the closed global shadow graphs and their zero forcing number,” *Acta Universitatis Sapientiae, Informatica* 14 (2022), 137–154. DOI: 10.2478/ausi-2022-0009. This paper cites the inaccessible 2013 Mays item and attributes to it the complete-bipartite zero forcing formula.
