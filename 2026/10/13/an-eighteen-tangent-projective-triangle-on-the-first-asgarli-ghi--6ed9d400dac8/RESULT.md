# An eighteen-tangent projective triangle on the first Asgarli–Ghioca curve

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_{11}}\) be the degree-ten curve
\[
C:\quad X^{10}+Y^{10}+Z^{10}-3(X+Y+Z)^{10}=0.
\]
Among the distinct \(\mathbb F_{11}\)-lines tangent to \(C\) at smooth \(\mathbb F_{11}\)-points, the minimum number whose union is all of \(\mathbb P^2(\mathbb F_{11})\) is **exactly \(18\)**. There is an optimal set of eighteen tangent lines whose eighteen dual points form a three-sided projective triangle: seven selected points lie on each dual side and the three vertices lie on two sides each. The eighteen coefficients, in projective normalization, are
\[
\begin{gathered}
[0:1:3],\; [1:0:4],\; [1:1:2],\; [1:1:7],\; [1:1:8],\; [1:2:1],\; [1:3:0],\; [1:4:9],\; [1:5:9],\; [1:6:6],\; [1:7:3],\; [1:7:7],\; [1:7:10],\; [1:8:6],\; [1:9:5],\; [1:9:7],\; [1:9:9],\; [1:10:1].
\end{gathered}
\]
These are **line coefficients**: the displayed triple \([a:b:c]\) denotes the original-plane tangent \(aX+bY+cZ=0\), rather than its point of contact.

## Assumptions and scope
All coordinates and incidence tests are over the prime field \(\mathbb F_{11}\). A tangent means the projective gradient line at a smooth rational point of the specific reduced curve above. A tangent cover is a set of **distinct** such rational lines whose union contains every one of the \(133\) points of \(\mathbb P^2(\mathbb F_{11})\). No claim is made concerning tangent covers in extensions or at other values of \(q\). The geometric irreducibility and tangent-filling property of this curve are already established by Asgarli and Ghioca.

## Proof
**1. Exhaustive description of eligible tangents.** Every nonzero triple over \(\mathbb F_{11}\) is normalized by scaling its first nonzero coordinate to \(1\). There are \(11^2+11+1=133\) distinct normalized triples. Fermat's theorem shows that the rational points on \(C\) are exactly the normalized triples \(Q=[x:y:z]\) with \(xyz(x+y+z)\ne0\). Its sole geometric singular point is \([1:1:1]\) by Proposition 3.4 of the originating paper. The remaining smooth rational points number \(90\), by the explicit exhaustive enumeration supplied in `verify.py`.

At such a point, write \(s=x+y+z\). Differentiating the defining homogeneous polynomial in characteristic \(11\) gives a tangent whose normalized coefficient triple is
\[
\tau(Q)=\left[\frac3s-\frac1x:\frac3s-\frac1y:\frac3s-\frac1z\right].
\]
The modular normalization and the tangent computation in `verify.py` enumerate exactly \(72\) distinct such tangent lines. In particular, every one of the displayed eighteen line coefficients is an attained value of \(\tau\) on a smooth rational point, not a hypothetical dual line.

**2. Explicit cover.** Let \(W\) be the eighteen coefficient triples displayed above. For every projective point \(P=[u:v:w]\), calculate \(n_W(P)=\#\{[a:b:c]\in W:au+bv+cw=0\}\). Enumerating the complete \(133\)-point projective plane gives the following exact distribution:
\[
\#\{P:n_W(P)=1,2,3,7\}=(90,15,25,3).
\]
All entries are positive multiplicities, so \(n_W(P)\ge1\) for every \(P\). This proves that the eighteen tangent lines cover all rational points. The three dual-side equations are
\[
 A+ B+8C=0,\qquad A+7B+7C=0,\qquad A+9B+8C=0.
\]
Each contains seven of the eighteen dual points, and every selected point belongs to at least one side. The three pairwise intersections are distinct selected vertices, so this is a projective triangle (not three concurrent lines).

**3. Sharp lower bound.** Let \(T\) denote the entire set of seventy-two eligible tangent coefficient points in the dual projective plane. The exact count of lines of \(T\) through each \(P\in\mathbb P^2(\mathbb F_{11})\) has histogram
\[
\#\{P:n_T(P)=1,4,5,6,7,8,11\}=(3,6,30,25,24,42,3).
\]
In particular the maximum is \(11\). Because a projective line in the dual plane has \(12\) points, \(T\) contains **no entire dual projective line**, and neither does any subset of \(T\). A set of primal lines covers all primal points if and only if the corresponding dual points meet every dual line, i.e. constitute a blocking set. Any eligible tangent cover is therefore a **nontrivial** blocking set of \(\mathrm{PG}(2,11)\) in the dual plane. Blokhuis's prime-order blocking-set theorem gives
\[
|W'|\ge\frac{3(11+1)}{2}=18
\]
for every such nontrivial blocking set \(W'\). Together with the explicit eighteen-line cover this establishes the exact minimum.

## Verification
Execute `python3 verify.py` using only Python's standard library. It regenerates every normalized point of \(\mathbb P^2(\mathbb F_{11})\) and all rational smooth curve points, computes all tangent gradients, verifies the eighteen selected tangents individually, establishes the complete point-cover and full-tangent incidence histograms, and verifies the three-side geometry. All finite statements are proved by complete exhaustive enumeration of explicitly defined finite sets, not by sampling. The only external theorem needed for the global **minimum** is the published Blokhuis nontrivial-blocking-set lower bound, applied with verified nontriviality.

## Relationship to prior work
Asgarli and Ghioca (arXiv:2302.13420) prove irreducibility and **qualitative tangent-filling** for this family; their introduction discusses a general projective triangle as a potential tangent-filling strategy, and their Section 3 determines rational points and a tangent equation. They do **not** exhibit the eighteen selected tangents of this particular degree-ten curve or show that it realizes the optimum cover cardinality. Blokhuis's 1994 theorem provides the general lower bound; the Blokhuis–Brouwer 1986 paper already establishes that an abstract eighteen-point blocking set exists in \(\mathrm{PG}(2,11)\). Neither supplies containment of such a set inside the tangent dual points of this fixed curve. Previously determined Gauss-fiber counts for this same curve establish the number \(72\) of distinct tangents but do not imply the explicit eighteen-line covering subset or its optimality.

## Limitations
This is an exact result only for \(q=11\), the first admissible prime field of the published construction. It does not classify every optimal tangent cover, prove the optimal subset is unique, or extend the value \(18\) to larger fields. Its priority has been compared against identifiable published sources and research records, but unindexed computations may exist. The mathematical review is not an independent external audit.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1 (first public 2023-02-26); revised v2 2023-04-04, Theorem 1.3 and §§3.1–3.4. https://arxiv.org/html/2302.13420v2
2. A. Blokhuis, *On the size of a blocking set in PG(2,p)*, Combinatorica **14** (1994), 111–114, DOI:10.1007/BF01305953.
3. A. Blokhuis and A. E. Brouwer, *Blocking Sets in Desarguesian Projective Planes*, Bull. London Math. Soc. **18** (1986), 132–134, DOI:10.1112/blms/18.2.132.
