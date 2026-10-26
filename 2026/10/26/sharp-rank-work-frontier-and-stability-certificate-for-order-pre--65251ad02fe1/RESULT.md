# Sharp rank–work frontier and stability certificate for order-preserving full transformations

## Finding

For each integer \(n\ge1\) let \(O_n\) be the monoid of weakly increasing full transformations \(f:\{1,\ldots,n\}\to\{1,\ldots,n\}\). The **image rank** is \(r=|\operatorname{im}f|\). The **work** of \(f\), in the sense of East–McNamara, is \(w(f)=\sum_{i=1}^{n}|i-f(i)|\). For each integer \(1\le r\le n\),

\[
\max_{\substack{f\in O_n\\|\operatorname{im}f|=r}}w(f)=\frac{n(n-1)-r(r-1)}{2}.
\]

If \(r<n\), equality holds at **exactly two** maps: the map with value vector \((1^{n-r+1},2,\ldots,r)\), and the map with value vector \((n-r+1,\ldots,n-1,n^{n-r+1})\). Superscripts here indicate repetition in a value vector. If \(r=n\), the only map is the identity and its work is zero.

A coefficientwise, nonnegative **stability certificate** further bounds the deficit. Suppose \(N=n-r>0\), the distinct image values are \(1\le v_1<\cdots<v_r\le n\) and their positive multiplicities are \(a_1,\ldots,a_r\). Define \(u_j=v_j-j\), \(g_0=u_1\), \(g_k=u_{k+1}-u_k\) for \(1\le k<r\), and \(g_r=N-u_r\). With

\[
d_{mk}=\begin{cases}m-k-1,&k<m,\\k-m,&k\ge m,\end{cases}
\]

we have

\[
\frac{n(n-1)-r(r-1)}2-w(f)\ge \frac1N\sum_{m=1}^{r}\sum_{k=0}^{r}(a_m-1)g_k(r-1-d_{mk})\ge0.
\]

In particular, the rank–work frontier and its equality cases are determined uniformly in both natural semigroup parameters.

## Assumptions and scope

All domains are labeled chains, and transformations are full and **weakly** increasing (equal consecutive values are permitted). Rank denotes image cardinality, not a generating rank. The work uses the ordinary chain metric. The assertion is for all positive integers \(n\), all integer ranks \(1\le r\le n\), and all maps in the rank layer. When \(r=1\), the two maximizers are the distinct constant endpoint maps if \(n>1\). The stability bound is stated for \(n-r>0\) to avoid dividing by zero.

## Proof

Write \(N=n-r\). For \(N=0\), a weakly increasing surjection \([n]\to[n]\) is the identity, so the assertion follows. Now let \(N>0\).

**Step 1: multiplicity simplex.** Fix the ordered image values \(v_1<\cdots<v_r\). Set \(s_j=\sum_{m=1}^{j}a_m\) for \(1\le j<r\), with \(s_0=0\) and \(s_r=n\). The work can be telescoped as

\[
w(f)=\sum_{i=1}^n|v_r-i|+\sum_{j=1}^{r-1}\sum_{i=1}^{s_j}\bigl(|v_j-i|-|v_{j+1}-i|\bigr).
\]

For \(v_j<v_{j+1}\), the sequence \(i\mapsto |v_j-i|-|v_{j+1}-i|\) is nondecreasing. Consequently its prefix-sum function, extended linearly between integer arguments, is convex in \(s_j\). Thus the displayed work is convex in the cumulative multiplicities \((s_1,\ldots,s_{r-1})\), which are affine in \((a_1,\ldots,a_r)\). Write \(\lambda_m=(a_m-1)/N\). Then \(\lambda_m\ge0\), \(\sum_m\lambda_m=1\), and \(a\) is the convex combination of vertices where one multiplicity is \(N+1\) and all others are one. Jensen's inequality therefore bounds the work by the corresponding convex combination of vertex works.

**Step 2: image-value simplex.** Each ordered value satisfies \(0\le u_1\le\cdots\le u_r\le N\) after writing \(v_j=j+u_j\). Its gap coordinates \(g_0,\ldots,g_r\) are nonnegative and sum to \(N\). This is the convex hull of \(r+1\) image vertices: for vertex \(k\in\{0,\ldots,r\}\), let \(v_j=j\) when \(j\le k\) and \(v_j=N+j\) when \(j>k\). The corresponding vertex coefficient is \(\mu_k=g_k/N\). For fixed multiplicities, work is a sum of absolute values of affine expressions in the image values and hence convex. Applying Jensen again yields

\[
w(f)\le\sum_{m=1}^{r}\sum_{k=0}^{r}\lambda_m\mu_k w_{mk},
\]

where \(w_{mk}\) is the work when multiplicity \(m\) is \(N+1\), all others are one, and the image values are at vertex \(k\).

**Step 3: exact vertex works.** At vertex \((m,k)\) the long block occupies domain positions \(m,\ldots,m+N\). If \(k\ge m\), its images move this block down to \(m\), contributing \(N(N+1)/2\), while the next \(k-m\) singleton blocks each move by \(N\). If \(k<m\), the long block moves up to \(m+N\), contributing the same triangular amount, while the preceding \(m-k-1\) singletons each move by \(N\). All other singleton blocks remain fixed. Hence

\[
w_{mk}=\frac{N(N+1)}2+Nd_{mk},\qquad d_{mk}=\begin{cases}m-k-1&k<m,\\k-m&k\ge m.\end{cases}
\]

Clearly \(d_{mk}\le r-1\). Therefore \(w(f)\le N(N+1)/2+N(r-1)=\big(n(n-1)-r(r-1)\big)/2\). Subtracting the double Jensen bound from this common maximum yields the stability certificate:

\[
\frac{n(n-1)-r(r-1)}2-w(f)\ge\sum_{m,k}\lambda_m\mu_k N(r-1-d_{mk})=\frac1N\sum_{m,k}(a_m-1)g_k(r-1-d_{mk}).
\]

**Step 4: equality rigidity.** For \(r\ge2\), the only vertex pairs with \(d_{mk}=r-1\) are \((m,k)=(1,r)\) and \((r,0)\). Since the support of the product weights \(\lambda_m\mu_k\) is a Cartesian product, the stability remainder can vanish only if both \(\lambda\) and \(\mu\) are concentrated at one of those two pairs. Such vertices are exactly the two explicitly stated transformations, and each realizes the maximum by Step 3. For \(r=1\), the only multiplicity is \(a_1=n\). The image-value simplex is the interval of possible constant values, and convexity of \(\sum_i|i-v_1|\) shows that the two endpoints attain the common maximum; for \(n>1\) all intermediate constants give a strictly smaller value. For \(n=1\) the two descriptions coincide. This completes the proof for all ranks.

## Verification

The dependency-free Python 3 program `verify.py` exhaustively visits all weakly increasing maps through \(n=9\), checks every rank maximum and exact equality set, and verifies the nonnegative stability bound individually for every map. A separate dynamic program, using a state indexed by final image value and image rank, confirms maxima and tie counts for all \(2\le n\le20\). Its terminal marker is `VERIFY_OK_RANK_RESOLVED_CHAIN_WORK_FRONTIER`. These are finite corroborations of the proof, not replacements for its all-\(n\) argument.

## Relationship to prior work

East and McNamara introduced and studied work of transformation semigroups, obtaining a closed form for the **sum of work over the entire order-preserving transformation monoid**, not the pointwise maximum at each prescribed image rank. This finding retains their work statistic but asks a different extremal question: the complete rank-conditioned maximum, its complete set of attaining maps and a quantitative deficit certificate. The earlier strictly order-preserving preprint is not conflated with the later weakly order-preserving convention used here. Other literature on ranks, presentations and generators of order-preserving monoids does not imply a displacement extremal profile without additional work.

## Limitations

The theorem does not count the number of maps having each intermediate work value, and it does not address partial maps, arbitrary permutations or nonmonotone maps. The stability bound is not claimed to be optimal term by term. An equivalent historical statement in uninspected or unindexed literature remains possible; no definitive priority claim is made. Mathematical independent review has not been performed.

## References

1. J. East and P. J. McNamara, *On the work performed by a transformation semigroup*, Australasian Journal of Combinatorics **49** (2011), 95–109. Full text: https://petermc.net/maths/papers/east,mcnamara.pdf .
2. J. East, *The Work Performed by a Transformation Semigroup*, preprint dated November 14, 2005. https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2005/east-35.pdf . The author's publicly posted copy at https://www.researchgate.net/publication/248066353_The_Work_Performed_by_a_Transformation_Semigroup has a verified September 16, 2014 upload timestamp. Earlier public release is not dated to the day by the inspected evidence.
3. Institutional publication record for the 2011 paper: https://researchers.westernsydney.edu.au/en/publications/on-the-work-performed-by-a-transformation-semigroup .
