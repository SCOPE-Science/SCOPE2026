# A half-congruence resolution of the odd-jump Toeplitz metric-dimension conjecture

## Finding

**Theorem.** Fix any integer \(k\ge3\), put \(b=4k+1\), and let \(n\ge b+2\). Let \(T_n\langle1,2,b\rangle\) be the simple graph with vertex set \(\{0,1,\ldots,n-1\}\) in which two distinct vertices are adjacent precisely when their absolute difference belongs to \(\{1,2,b\}\). Its metric dimension is exactly
\[
\operatorname{dim}(T_n\langle1,2,b\rangle)=3.
\]
Indeed, \(\{0,1,2k+1\}\) is a metric basis for every such \(n\), independent of the length of the interval. Thus the \(b\equiv1\pmod4\), \(b\ge13\), half of the odd-parameter family proposed in Conjecture 2 of Nadeem--Qu--Ahmad--Azeem (2022) has an exact solution. The \(b\equiv3\pmod4\) case is not addressed.

## Assumptions and scope

Graph distances count edges. A vertex set \(W\) resolves a graph if the distance vectors \((d(v,w))_{w\in W}\) are different for all distinct vertices \(v\). The metric dimension is the least cardinality of a resolving set. The theorem covers every integer \(k\ge3\) and every integer \(n\ge4k+3\); the graph is connected because its allowed steps include \(1\).

## Proof

**1. Exact interval distance.** For an arbitrary odd \(b\ge5\) and \(n\ge b+2\), put
\[
F_b(d)=q+\min\left\{\left\lceil\frac r2\right\rceil,
1+\left\lceil\frac{b-r}{2}\right\rceil\right\},
\qquad d=qb+r,\quad q\ge0,\quad 0\le r<b.
\]
We claim that \(d_{T_n}(x,y)=F_b(|x-y|)\) for all vertices \(x,y\).

For a path from \(x<y\), let \(h\) be the signed excess of \(+b\) moves over \(-b\) moves. It uses at least \(|h|\) long moves and at least \(\lceil|y-x-hb|/2\rceil\) short moves, hence has length at least
\[
\min_{h\in\mathbb Z}\left(|h|+\left\lceil\frac{|y-x-hb|}{2}\right\rceil\right).
\]
Because \(b\ge5\), this minimum is attained at \(h=q\) or \(h=q+1\) for \(y-x=qb+r\): increasing \(h\) up to \(q\) strictly decreases the objective, and decreasing or increasing it outside the interval \([0,q+1]\) cannot help. Thus the lower bound equals \(F_b(y-x)\).

The candidate \(q+\lceil r/2\rceil\) is attained by \(q\) successive \(+b\) moves followed by \(+1,+2\) moves adding to \(r\), with all visited vertices between \(x\) and \(y\). Set \(s=b-r\). For \(q\ge1\), the second candidate \(q+1+\lceil s/2\rceil\) is attained by moving \(+b\) once, retreating \(s\) using \(-1,-2\), and then making \(q\) further \(+b\) moves. Every visited vertex lies between \(x\) and \(y\).

When \(q=0\) and \(r>0\), choose an integer
\[
\max\{0,x+b-(n-1)\}\le t\le\min\{x,s\}.
\]
The interval is nonempty because \(y=x+b-s\le n-1\), and \(n-1-b\ge1\). If \(s\) is even, it contains an even integer: if \(x\le s\) and \(x>0\), it contains both \(x-1\) and \(x\); if \(x=0\), it contains \(0\); if \(x>s\), it contains \(s\). For odd \(s\), any integer in the interval is suitable. Move backward \(t\), forward \(b\), and backward \(s-t\), using the steps \(1,2\) for the backward portions. The parity choice guarantees precisely \(\lceil s/2\rceil\) short moves in total; the intermediate positions belong to \([0,n-1]\). If \(r=0\), the direct candidate already wins. Consequently, the distance formula is exact in every case.

Notice the useful periodicity \(F_b(d+b)=F_b(d)+1\).

**2. Three explicit landmarks.** Now write \(b=4k+1\) and \(s=2k+1\). Put \(F=F_b\). For \(d=qb+r\), let
\[
g(r)=\min\left\{\left\lceil\frac r2\right\rceil,
1+\left\lceil\frac{b-r}{2}\right\rceil\right\},
\qquad F(d)=q+g(r).
\]
An elementary comparison gives
\[
g(r)=\begin{cases}
\lceil r/2\rceil,&0\le r\le2k+2,\\
1+\lceil(b-r)/2\rceil,&2k+3\le r\le4k.
\end{cases}
\]
For \(i\ge s\), form the two differences of the three landmark distances
\[
\Delta(i)=\big(F(i-1)-F(i),\ F(i-s)-F(i)\big).
\]
Because \(F(d+b)=F(d)+1\), this depends only on the residue \(r=i\bmod b\). The complete residue table, with \(j\) restricted as displayed, is

| Residue \(r\) | Index range | \(\Delta(i)\) |
|---|---|---|
| \(0\) | — | \((1,k-1)\) |
| \(2j+1\) | \(0\le j\le k\) | \((-1,k-2j-1)\) |
| \(2j\) | \(1\le j\le k\) | \((0,k+1-2j)\) |
| \(2j\) | \(k+1\le j\le2k\) | \((0,2j-3k-2)\) |
| \(2j+1\) | \(k+1\le j\le2k-1\) | \((1,2j-3k-1)\) |

All \(4k+1\) pairs are different. Indeed, pairs with first coordinate \(-1\) have strictly decreasing second coordinates. The first-coordinate-zero rows have disjoint second-coordinate parities (their terms are respectively congruent to \(k-1\) and \(k\) modulo \(2\)) and are separately strictly monotone. For first coordinate \(1\), the final row runs through \(-k+1,-k+3,\ldots,k-3\), followed by the exceptional value \(k-1\) at residue zero.

For \(1\le i<s\), the same elementary formula gives \(\Delta(i)=\Delta(i+b)\); here the second entry is interpreted as \(F(s-i)-F(i)\), using the absolute distance to landmark \(s\). At \(i=0\), the difference pair is \((1,k+1)\), absent from the table. Thus any two distinct vertices \(i,j\ge1\) with equal three-landmark vectors must have \(i\equiv j\pmod b\). Their first distance coordinates \(F(i)\) and \(F(j)\) then differ by \(|i-j|/b>0\), a contradiction. Vertex zero is also distinguished. The three vertices \(\{0,1,s\}\) therefore resolve the whole half-line and hence every stated finite graph, by the exact interval-distance lemma.

**3. Optimality.** In \(T_n\langle1,2,b\rangle\), the endpoints \(0,n-1\) have degree three, while every other vertex has degree at least four. In a graph with a resolving set of two vertices, each landmark has degree at most three: all its neighbors must have pairwise different distances to the other landmark, but the triangle inequality allows at most three possible values. Thus the only candidate two-element resolving set is \(\{0,n-1\}\).

If \(n=b+2\), vertices \(1\) and \(b\) both have distance \(1\) to each endpoint, so this pair fails. If \(n\ge b+3\), the six distinct vertices
\[
3,\ 4,\ b-2,\ b-1,\ b+1,\ b+2
\]
all have distance \(2\) from vertex \(0\). If \(D=d(0,n-1)\), their distances to vertex \(n-1\) must be among the five integers \(D-2,D-1,D,D+1,D+2\). Two of the six consequently have identical distance vectors to the endpoints. Thus no resolving pair exists. A singleton cannot resolve a graph requiring more than two landmarks, and the upper bound is three; equality follows.

## Verification

Run `python3 verify_toeplitz.py` (Python standard library only). It independently builds the graph from its edge rule, computes breadth-first-search distances, verifies all source--target distances against the closed formula, and verifies the three-landmark distinctness for thirteen stated test graphs. The script checks \(21{,}945\) source--target distances and independently checks the residue formulas for \(3\le k\le300\). The executable finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Nadeem, Qu, Ahmad, and Azeem, *Metric Dimension of Some Generalized Families of Toeplitz Graphs* (2022), prove their Theorem 6 for even \(b\ge10\) and state Conjecture 2 for odd \(b\ge11\). This result proves that conjecture for all \(b\equiv1\pmod4\) with \(b\ge13\), and gives a single length-independent basis. Liu, Nadeem, Siddiqui, and Nazir (2019) treat the three-generator family only for jump values \(3,4,5,6\). Luo and colleagues (2022) investigate partition dimension, an inequivalent parameter, and their explicit three-generator analysis is limited to small or even jumps. The present argument uses the complete infinite residue signature and the exact boundary-independent metric, neither supplied by the inspected results.

## Limitations

The residue class \(b\equiv3\pmod4\), including the smallest conjectured odd case \(b=11\), is unresolved here. The finite verifier does not certify infinitely many cases by itself. An unindexed priority source might still contain an equivalent argument; coverage details are provided in REVIEW.md.

## References

1. M. F. Nadeem, S. Qu, A. Ahmad, and M. Azeem, “Metric Dimension of Some Generalized Families of Toeplitz Graphs,” *Mathematical Problems in Engineering* (2022), article 9155291, DOI: 10.1155/2022/9155291. First publicly published 2022-03-12. Section 3.3, Theorem 6 and Section 4, Conjecture 2.
2. J.-B. Liu, M. F. Nadeem, H. M. A. Siddiqui, and W. Nazir, “Computing Metric Dimension of Certain Families of Toeplitz Graphs,” *IEEE Access* **7** (2019), 126734–126741, DOI: 10.1109/ACCESS.2019.2938579. Section III and concluding open problems.
3. R. Luo, A. Khalil, A. Ahmad, M. Azeem, G. Ibragimov, and M. F. Nadeem, “Computing the partition dimension of certain families of Toeplitz graph,” *Frontiers in Computational Neuroscience* **16** (2022), 959105, DOI: 10.3389/fncom.2022.959105. Section 3.
4. A. N. A. Koam and collaborators, “On the Constant Partition Dimension of Some Generalized Families of Toeplitz Graph,” *Journal of Mathematics* (2024), article 4721104, DOI: 10.1155/2024/4721104. Sections 1–2.
