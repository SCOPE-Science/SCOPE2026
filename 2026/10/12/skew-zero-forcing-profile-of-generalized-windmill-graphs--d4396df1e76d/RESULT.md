# Skew zero forcing profile of generalized windmill graphs
## Finding
For integers \(k\ge2\) and \(m\ge3\), define the generalized windmill
\[
W_{k,m}=K_1\vee kK_m.
\]
Let \(c\) be its center and let \(B_1,\ldots,B_k\) be the pairwise disjoint peripheral cliques, each of size \(m\). For an initial blue set \(S\subseteq V(W_{k,m})\), put
\[
w_i=|B_i\setminus S|.
\]
Then \(S\) is a skew zero forcing set if and only if both conditions hold:

1. \(w_i\le2\) for every \(i\);
2. if \(c\notin S\), then \(w_i\neq2\) for at least one \(i\).

Define
\[
F_m(x)=x^m+m x^{m-1}+\binom{m}{2}x^{m-2}.
\]
The size enumerator of all skew zero forcing sets is
\[
\mathcal Z_-(W_{k,m};x)=(1+x)F_m(x)^k-\binom{m}{2}^k x^{k(m-2)}.
\]
Hence
\[
Z_-(W_{k,m})=k(m-2)+1,
\]
and the number of minimum skew zero forcing sets is
\[
\binom{m}{2}^{k-1}\left(\binom{m}{2}+km\right).
\]
Also, since a failed set can be obtained by leaving three white vertices in one blade and every failed set leaves at least three vertices white,
\[
F^-(W_{k,m})=km-2.
\]

## Assumptions and scope
Skew zero forcing uses the standard rule that any vertex, blue or white, may force a white neighbor when that neighbor is its unique white neighbor. Graphs are finite, simple, and undirected. The theorem is stated for \(k\ge2\) and \(m\ge3\). The boundary \(m=2\), the friendship-graph family, behaves differently in the failed-set parameter: every nonempty set skew forces, a phenomenon already covered by published failed-skew-zero-forcing classifications. The displayed enumerator algebraically extends to that boundary as \((1+x)^{2k+1}-1\), but that specialization is not part of the retained originality claim.

## Proof
Let \(\varepsilon=1\) when the center is white and \(\varepsilon=0\) when it is blue. In blade \(B_i\), a blue peripheral vertex has exactly \(\varepsilon+w_i\) white neighbors, while a white peripheral vertex has exactly \(\varepsilon+w_i-1\) white neighbors. The center has \(\sum_i w_i\) white neighbors.

First suppose some \(w_i\ge3\). Even if the center is eventually forced blue using another blade, the chosen blade still has at least three white vertices. A blue peripheral vertex there then sees at least three white neighbors, a white peripheral vertex sees at least two white neighbors, and the center sees at least three white neighbors once all other blades are cleared. No force can ever reduce that blade below three white vertices. Thus \(S\) is not skew zero forcing.

Now suppose every \(w_i\le2\) and the center is blue. If \(w_i=2\), either white vertex of \(B_i\) has exactly one white neighbor, namely the other white vertex, so it forces that vertex and leaves \(w_i=1\). When \(w_i=1\), a blue vertex exists because \(m\ge3\), and it has that remaining white vertex as its unique white neighbor. Thus every blade clears.

Finally suppose every \(w_i\le2\) and the center is white. If every \(w_i=2\), then the center has \(2k\) white neighbors, each blue peripheral vertex has three white neighbors, and each white peripheral vertex has two white neighbors; hence no force is available. If some \(w_j=0\), a blue vertex of \(B_j\) has the center as its unique white neighbor and forces it. If some \(w_j=1\), the unique white peripheral vertex of \(B_j\) has the center as its unique white neighbor and forces it. In either case the center becomes blue and the preceding paragraph finishes the process. This proves the characterization.

For the enumerator, a blade with at most two white vertices contributes
\[
F_m(x)=x^m+m x^{m-1}+\binom{m}{2}x^{m-2}.
\]
Blue-center states contribute \(xF_m(x)^k\). White-center states contribute all of \(F_m(x)^k\) except the single occupancy profile in which every blade has exactly two whites; that forbidden profile contributes \(\binom{m}{2}^k x^{k(m-2)}\). Summing gives the formula.

The forbidden lowest-degree term cancels, so the minimum degree is \(k(m-2)+1\). At that degree there are \(\binom{m}{2}^k\) sets with blue center and two omitted vertices in every blade, and \(km\binom{m}{2}^{k-1}\) sets with white center, one blade omitting one vertex, and all other blades omitting two. This gives the minimum-set count. A failed set must either have three white vertices in some blade or be the white-center profile with two whites in every blade. For \(k\ge2\), the former uses fewer white vertices, so the largest failed set has \(1+km-3=km-2\) blue vertices.

## Verification
A standalone exhaustive checker enumerates every initial set for representative parameter pairs through order thirteen and compares the actual skew forcing closure with the stated occupancy criterion. It also compares every coefficient of the observed size distribution with the closed polynomial and independently checks the minimum size and minimum-set count. The packaged checker uses only the Python standard library.

## Relationship to prior work
Skew zero forcing was introduced in the minimum-skew-rank literature. The exact windmill characterization above is not asserted for the friendship boundary \(m=2\): the published classification of graphs with failed skew zero forcing number zero includes nonempty bouquets of odd cycles meeting in one vertex, which contains that boundary. Later published work classifies graphs with failed skew zero forcing number one and studies failed skew zero forcing on path powers and circulant graphs; those statements do not cover generalized windmills with \(m\ge3\).

A separate 2024 paper gives a complete description of *ordinary* zero-forcing minimal forts for windmill graphs. That is a different forcing rule: ordinary zero forcing permits only blue vertices to force, whereas skew zero forcing permits any vertex to force. Its windmill fort theorem therefore does not imply the occupancy criterion or enumerator proved here.

Database and literature searches used the aliases “windmill”, “generalized windmill”, “friendship graph”, “skew zero forcing”, “failed skew zero forcing”, and combinations with “polynomial”, “all sets”, and “minimum”. No inspected source stated this all-set skew-forcing characterization or its polynomial.

## Limitations
The proof determines the skew forcing process only for the equal-blade windmill family \(K_1\vee kK_m\); unequal blade sizes and windmills with a nontrivial central clique are not claimed. Literature searches cannot prove global novelty. The foundational skew-zero-forcing article was identifiable by DOI and public bibliographic records, but its full text was not available in the inspected public sources. An archival preprint index records the same title in a September 2009 monthly bucket without a day. The metadata therefore records the earliest day-resolved public availability verified for the exact article, \(2010\text{-}02\text{-}11\), and does not invent a day for the month-only listing.

## References
1. IMA-ISU Research Group on Minimum Rank, “Minimum rank of skew-symmetric matrices described by a graph,” *Linear Algebra and its Applications* 432 (2010), 2457–2472. DOI: 10.1016/j.laa.2009.10.001.
2. T. Ansill, B. Jacob, J. Penzellna, and D. Saavedra, “Failed skew zero forcing on a graph,” *Linear Algebra and its Applications* 509 (2016), 40–63. DOI: 10.1016/j.laa.2016.07.019.
3. A. Johnson, A. E. Vick, and D. A. Narayan, “Characterization of All Graphs with a Failed Skew Zero Forcing Number of 1,” *Mathematics* 10 (2022), 4463. DOI: 10.3390/math10234463.
4. A. Johnson, A. Vick, R. Flórez, and D. A. Narayan, “Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs,” *AppliedMath* 5 (2025), 32. DOI: 10.3390/appliedmath5020032.
5. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, “On the number of minimal forts of a graph,” arXiv:2404.05963, 2024.
