# Location-resolved descent dependence of prescribed edges in random matchings

## Finding
For an even number \(N\ge6\) of linearly ordered vertices, let a uniform perfect matching define a fixed-point-free involution \(\pi\). Write
\[
D=\sum_{j=1}^{N-1}\mathbf1_{\{\pi(j)>\pi(j+1)\}},\quad X_{ab}=\mathbf1_{\{\pi(a)=b\}},\quad S=\sum_{j=1}^{N-1}X_{j,j+1}.
\]
For \(a<b\), the entire prescribed-edge covariance map is determined by \(H_{ab}=(N-1)\operatorname{Cov}(X_{ab},D)\):
\[
H_{ab}=\begin{cases}
1,&a=1,\ b=N,\\
0,&(a,b)=(1,2)\text{ or }(N-1,N),\\
\dfrac{b-N/2-2}{N-3},&a=1,\ 3\le b\le N-1,\\
\dfrac{N/2-a-1}{N-3},&2\le a\le N-2,\ b=N,\\
\dfrac{N-2}{2(N-3)},&2\le a,\ b=a+1\le N-1,\\
-\dfrac1{N-3},&2\le a<b-1,\ b\le N-1.
\end{cases}
\]
Consequently the interior sign pattern is uniform: nonadjacent edges have negative covariance, while adjacent edges have positive covariance. The two outer boundary profiles vary linearly, and the spanning edge \(\{1,N\}\) causes the maximal shift of one full descent. Moreover,
\[
\mathbb ES=1,\qquad \operatorname{Var}(S)=\frac{N-2}{N-1},\qquad \operatorname{Cov}(S,D)=\frac{N-2}{2(N-1)}\longrightarrow\frac12.
\]

## Assumptions and scope
The vertex set is \([N]=\{1,\ldots,N\}\) with its usual linear order, \(N\) is even and at least six, all \((N-1)!!\) fixed-point-free involutions are equiprobable, and a short chord is a matched pair of consecutive labels. Ascents, descents and chord adjacency refer to this same order, without a circular wrap-around. \(X_{ab}\) is an indicator of the specified edge, not a count of all edges with that length. The shift \(H_{ab}\) is an unnormalized conditional change; the actual covariance is \(H_{ab}/(N-1)\). The additive one used in some Eulerian conventions for the descent number does not alter any covariance.

## Proof
**Unconditional mean.** Every specified edge has probability \(1/(N-1)\). For a neighboring pair of positions \(j,j+1\), their involution partners equal each other (the two vertices are matched) with probability \(1/(N-1)\); this event forces a descent. Otherwise, their two partners are distinct labels outside \(\{j,j+1\}\), and their order is exchangeable. Hence
\[
\mathbb P(\pi(j)>\pi(j+1))=\frac1{N-1}+\frac12\left(1-\frac1{N-1}\right)=\frac{N}{2(N-1)},
\quad\mathbb ED=\frac N2.
\]

**Conditional local table.** Fix the pair \(a<b\) and condition on \(X_{ab}=1\). The remaining \(N-2\) vertices form a uniformly random perfect matching. If neither \(j\) nor \(j+1\) belongs to \(\{a,b\}\), the conditional probability of a descent is the baseline
\[
p_0=\frac1{N-3}+\frac12\left(1-\frac1{N-3}\right)=\frac{N-2}{2(N-3)}.
\]
At any neighboring position meeting the fixed endpoints, write \(p_j=\mathbb P(\pi(j)>\pi(j+1)\mid X_{ab}=1)\). For nonadjacent endpoints \(b\ge a+2\), the four possible affected positions have the explicit probabilities
\[
\begin{array}{c|cccc}
j&a-1&a&b-1&b\\\hline
p_j&\dfrac{N-b}{N-3}&\dfrac{b-3}{N-3}&\dfrac{N-a-2}{N-3}&\dfrac{a-1}{N-3}
\end{array}.
\]
Only positions in \(\{1,\ldots,N-1\}\) are included. Each fraction follows from counting eligible smaller/larger partners of one endpoint among the \(N-3\) possible partners of the other vertex. For adjacent endpoints \(b=a+1\), the position \(j=a\) is a sure descent, with \(p_a=1\), and the only other possibly affected positions are \(j=a-1\), with probability \((N-a-1)/(N-3)\), and \(j=a+1\), with probability \((a-1)/(N-3)\); omit them at the boundaries. Every other position has probability \(p_0\). These cases exhaust all positions and are valid even when the affected positions touch.

**Sum of positions and boundaries.** Summing the preceding probabilities and subtracting \(\mathbb ED=N/2\) gives \(H_{ab}\) exactly as displayed. To illustrate the mechanisms: for \(2\le a<b-1\) and \(b<N\), there are four affected sites whose probabilities sum to \((2N-6)/(N-3)=2\), while \(N-5\) unaffected sites contribute \((N-5)p_0\); subtraction yields \(-1/(N-3)\). For an interior adjacent edge, two exceptional neighbor positions have probabilities summing to \((N-2)/(N-3)\), and the paired location has probability one; the remaining \(N-4\) sites contribute \(p_0\), yielding \((N-2)/(2(N-3))\). For boundary pairs, delete the missing affected site(s) and count the remaining partners: this yields the two affine boundary expressions and the two corner zeros. When \(a=1,b=N\), the two endpoint positions are sure descents and the others have probability \(p_0\), giving shift one. Finally, since \(\mathbb P(X_{ab}=1)=1/(N-1)\), covariance equals \(H_{ab}/(N-1)\). In particular this proof is exact for every allowed even \(N\), not an inference from finite enumeration.

**Short-chord consequence.** The sum \(S=\sum_jX_{j,j+1}\) contains two boundary adjacent edges, each with shift zero, and \(N-3\) interior adjacent edges, each with shift \((N-2)/(2(N-3))\); therefore
\[
\operatorname{Cov}(S,D)=\frac1{N-1}(N-3)\frac{N-2}{2(N-3)}=\frac{N-2}{2(N-1)}.
\]
Likewise \(\mathbb ES=(N-1)/(N-1)=1\). Of the unordered pairs of candidate adjacent edges, exactly \((N-2)(N-3)/2\) are vertex-disjoint and hence can coexist. Their joint presence probability is \(1/((N-1)(N-3))\). Thus \(\mathbb E[S(S-1)]=(N-2)/(N-1)\) and \(\operatorname{Var}(S)=(N-2)/(N-1)\).

## Verification
The standalone script `check_matching_descents.py` independently enumerates every perfect matching on \(N=6,8,10,12\) vertices (respectively 15, 105, 945, and 10,395 matchings), reconstructs the permutation, computes its descent count, and checks every specified edge's exact conditional shift against both the derived piecewise map and the direct position-by-position probability sum. It also checks the means, variance, short-chord covariance, and the normalization identity \(\sum_{a<b}H_{ab}=0\) for even \(N=12,14,\ldots,100\). A total of 215 exact-integer or rational assertions pass. Enumerating small matchings is only an independent finite check; the proof above establishes the all-size statements.

## Relationship to prior work
Kim [1] analyzes the full distribution, mean and variance of descents in fixed-point-free involutions by indicator counting, but its inspected theorems and proofs do not condition on the presence of an arbitrarily positioned prescribed edge or give the five-part edge–descent covariance map. Kim and Lee [2] study asymptotic descent laws for conjugacy classes. Cameron and Killpatrick [3] study the marginal distribution of short chords and identify their mean as one; those marginal formulas do not imply covariance with the ordinary permutation descent statistic. Marmor [4] studies the short-chord *set* through Schur positivity and discusses usual ascents and an involutive weak-order descent set; those equidistribution and representation-theoretic results do not explicitly imply the present position-resolved mixed moments. Adin and Roichman [5] introduce a separate geometric cyclic descent statistic and prove equidistribution, which does not by itself determine dependence on a specified ordinary chord. The new statement concerns the *joint* effect of prescribing actual labeled endpoints, not a marginal Eulerian count or the distribution of the matching's short-chord set. Historical priority could still be obscured by an implicit specialization of a more general multivariate matching enumeration.

## Limitations
The graph is the complete graph on an ordered even number of labels, and matchings must be uniformly sampled; no general claim is made for weighted matchings, incomplete host graphs, other permutation statistics, nonlinear conditional independence or asymptotic joint normality. The finite checker is not an infinite proof. Earlier implicit equivalent formulas may exist, and no independent mathematical audit has been performed.

## References
[1] G. B. Kim, *Distribution of descents in matchings*, arXiv:1710.03896v1 (first public 2017-10-11), especially Section 2.

[2] G. B. Kim and S. Lee, *Central limit theorem for descents in conjugacy classes of* \(S_n\), arXiv:1803.10457v1 (first public 2018-03-28), Sections 1–3.

[3] N. T. Cameron and K. Killpatrick, *Statistics on linear chord diagrams*, arXiv:1902.09021v1 (first public 2019-02-24).

[4] A. Marmor, *Schur-Positivity of Short Chords in Matchings*, arXiv:2307.09894v1 (first public 2023-07-19), especially Sections 1, 4 and 6.3.

[5] R. M. Adin and Y. Roichman, *Cyclic Descents, Matchings and Schur-Positivity*, Electron. J. Combin. 30(2) (2023), P2.41, doi:10.37236/11761.
