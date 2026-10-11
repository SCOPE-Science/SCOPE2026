# Exact Euclidean radial spectrum of the bipermutahedron
## Finding
For Ardila's geometric realization \(\Pi_{n,n}\subset M_n\times M_n\) of the bipermutahedron, let \(n\ge2\) and use the Euclidean norm inherited from \(\mathbb R^n\times\mathbb R^n\). The unique minimum enclosing Euclidean ball of \(\Pi_{n,n}\) is centered at the origin.

Expand a bipermutation as in Ardila's construction: first occurrences are unbarred, second occurrences are barred, and the unique singleton letter is replaced by an adjacent unbarred--barred pair. If the unbarred positions are \(u_1<\cdots<u_n\), define the Dyck area
\[
A=\sum_{j=1}^n(u_j-j).
\]
Then \(0\le A\le n(n-1)/2\), every integer in this interval occurs, and every vertex on area level \(A\) has squared Euclidean norm
\[
\|v\|^2=
\frac{2n(4n^2-1)}3
+2(-n^2+2A)^2
+4(-n^2+2A).
\]
Hence the vertex set lies on exactly
\[
\frac{n(n-1)}2+1
\]
concentric spheres, one for each Dyck-area value. The circumradius is
\[
R(\Pi_{n,n})=
\sqrt{\frac{2n(n-1)(3n^2+7n+1)}3}.
\]
The farthest vertices are exactly those for which all first occurrences precede all second occurrences in the expanded word. Their number is
\[
n((n-1)!)^2.
\]

## Assumptions and scope
Here
\[
M_n=\{x\in\mathbb R^n:\sum_i x_i=0\},
\]
and \(\Pi_{n,n}\) is precisely the realization of Definition 2.4 in Ardila's paper, not merely a combinatorially equivalent bipermutahedron. The result therefore concerns its canonical integral coordinates and the induced Euclidean metric.

The theorem is about the smallest Euclidean ball containing the polytope and the complete list of distinct distances of its vertices from the center. It does not claim that vertices on a fixed radial shell form a single symmetry orbit.

## Proof
Let \(B\) be a bipermutation and let \(k\) be its singleton letter. Ardila expands \(B\) to a word of length \(2n\), replacing each first occurrence by an unbarred letter, each second occurrence by a barred letter, and the singleton \(k\) by the adjacent pair \(k\bar k\). Reading from left to right, the positions receive the odd integers
\[
-(2n-1),-(2n-3),\ldots,-1,1,\ldots,2n-3,2n-1.
\]
Write the resulting bijection as \(\pi\). Ardila defines
\[
x_i=\pi(i),\qquad y_i=-\pi(\bar i),\qquad
s=\sum_i x_i=\sum_i y_i,
\]
and the vertex
\[
v_B=u_\pi-s(e^k+f^k).
\]

First determine its norm. Because \(\pi\) bijects the \(2n\) letters with the odd integers above,
\[
\|u_\pi\|^2
=2\sum_{j=1}^n(2j-1)^2
=\frac{2n(4n^2-1)}3.
\]
Let \(p=\pi(k)\) and \(q=\pi(\bar k)\). The two special letters are adjacent in this order, so \(q-p=2\). Only the two \(k\)-coordinates change when passing from \(u_\pi\) to \(v_B\), and therefore
\[
\begin{aligned}
\|v_B\|^2-\|u_\pi\|^2
&=(p-s)^2-p^2+(-q-s)^2-(-q)^2\\
&=2s^2+2s(q-p)\\
&=2s^2+4s.
\end{aligned}
\]
Thus
\[
\|v_B\|^2=\frac{2n(4n^2-1)}3+2s^2+4s.
\tag{1}
\]

Now record where the unbarred letters occur. Since every first occurrence precedes the corresponding second occurrence, the bar/unbar pattern is a Dyck word: in every prefix, the number of unbarred letters is at least the number of barred letters. If its unbarred positions are \(u_1<\cdots<u_n\), then \(j\le u_j\le2j-1\). Setting
\[
A=\sum_{j=1}^n(u_j-j)
\]
gives \(0\le A\le n(n-1)/2\). Moreover,
\[
\begin{aligned}
s
&=\sum_{j=1}^n\bigl(2u_j-(2n+1)\bigr)\\
&=2A-n^2.
\end{aligned}
\tag{2}
\]
Combining (1) and (2) proves the stated radial formula.

Every integer area occurs. One direct way to see this is the standard bijection between Dyck paths of semilength \(n\) and Ferrers diagrams contained in the staircase
\[
(n-1,n-2,\ldots,1,0).
\]
For any integer \(A\) between \(0\) and the staircase size \(n(n-1)/2\), greedily fill rows of capacities \(n-1,n-2,\ldots,1\), with at most one partially filled row. The resulting weakly decreasing row lengths form a staircase-contained partition of size \(A\), hence a Dyck path of area \(A\). Conversely, any such Dyck bar pattern is realized by a bipermutation: choose any peak as the adjacent special pair and match each remaining unbarred position to a later barred position using the usual noncrossing Dyck matching, then assign the remaining labels bijectively to those pairs.

Since \(s=2A-n^2\) ranges through
\[
-n^2,-n^2+2,\ldots,-n,
\]
and every value is at most \(-2\), the function \(2s^2+4s=2(s+1)^2-2\) is strictly decreasing as \(s\) increases across this range. Therefore all \(n(n-1)/2+1\) area levels give distinct radii, and the largest radius occurs at \(A=0\), equivalently \(s=-n^2\). Substituting in (1) gives
\[
R^2
=\frac{2n(4n^2-1)}3+2n^4-4n^2
=\frac{2n(n-1)(3n^2+7n+1)}3.
\]

It remains to justify that this maximum vertex norm is the circumradius about the actual minimum-ball center. Euclidean minimum enclosing balls are unique. Ardila proves that \(\Pi_{n,n}\) is invariant under the simultaneous action of \(S_n\) on the two \(M_n\) factors. Hence its unique circumcenter is fixed by this action. An \(S_n\)-fixed vector in \(M_n\) is constant and has coordinate sum zero, so it is zero; therefore the only fixed vector in \(M_n\times M_n\) is the origin. Thus the minimum enclosing ball is centered at \(0\). Because every point of a polytope is a convex combination of vertices, its norm is at most the maximum vertex norm, so the radius above is the true circumradius.

Finally, \(A=0\) means the bar pattern is \(n\) unbarred letters followed by \(n\) barred letters. The required adjacent special pair must occupy the unique transition. There are \(n\) choices for its label, \((n-1)!\) orders for the other first occurrences, and independently \((n-1)!\) orders for the other second occurrences. Hence the farthest shell has \(n((n-1)!)^2\) vertices.

## Verification
The accompanying `verify.py` enumerates Dyck bar patterns through semilength \(8\), verifies that their area set is exactly every integer from \(0\) to \(n(n-1)/2\), checks the symbolic norm and circumradius identities using exact integer arithmetic, and brute-forces labeled bipermutations for \(2\le n\le4\) to confirm the predicted radial levels and farthest-shell multiplicity. These finite checks corroborate the formulas; the proof above establishes them for every \(n\ge2\).

## Relationship to prior work
Ardila's paper constructs the vertices of \(\Pi_{n,n}\), determines its face structure, enumerative invariants, deformations, and full automorphism group, and relates it to the harmonic polytope. The exact vertex coordinates and simultaneous \(S_n\)-symmetry are the inputs used here. Full-text inspection found no discussion of Euclidean radius, circumradius, enclosing spheres, or vertex norms.

A later paper of Nabijou develops toric configuration spaces based on the bipermutahedral fan. Its accessible full text likewise contains no occurrence of “circumradius”, “Euclidean”, or “radius” and does not supply a metric theorem for Ardila's realization.

The closest prior result in the checked published-result collection concerning the same polytope determines a one-skeleton graph distance between a bipermutation and its reversal. Graph distance does not determine Euclidean distance from the origin, the number of Euclidean radial shells, or the smallest enclosing ball, so that result does not imply the present theorem.

## Limitations
The radial formula is tied to Ardila's specific integral realization. Other deformations with the same normal fan generally have different Euclidean metric data. The theorem classifies distinct radial levels and the outermost level, but it does not give the multiplicity of every intermediate shell. The literature searches cannot exclude differently phrased or unindexed prior computations; that residual originality risk is recorded explicitly in the review.

## References
1. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295v1, first public version 2020-08-05; *Combinatorial Theory* 2(3) (2022), article 1, DOI 10.5070/C62359149.
2. Navid Nabijou, *Toric configuration spaces: the bipermutahedron and beyond*, arXiv:2306.03215; *Mathematische Zeitschrift* 309 (2025), article 4, DOI 10.1007/s00209-024-03608-3.
