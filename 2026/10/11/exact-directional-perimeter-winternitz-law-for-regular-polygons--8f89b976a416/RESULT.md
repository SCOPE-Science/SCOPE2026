# Exact directional perimeter Winternitz law for regular polygons

## Finding
Let \(P_n\) be any Euclidean regular \(n\)-gon, \(n\geq3\), and let \(o\) be its centroid. Each line \(L\) through \(o\) meets \(\partial P_n\) at two points and divides the polygonal boundary into two arcs. Write \(q_n(L)\) for the shorter arc's Euclidean length divided by the whole perimeter, so that \(0<q_n(L)\leq 1/2\).

For even \(n\), every central line has \(q_n(L)=1/2\). For odd \(n\), set \(\beta=\pi/n\) and identify unoriented line directions modulo \(\pi\). By rotational symmetry choose a representative whose angle \(\alpha\) from a vertex radius satisfies \(0\leq\alpha\leq\beta\). Then the **exact directional law** is
\[
q_n(\alpha)=\frac12-\frac{\tan\alpha\tan(\beta-\alpha)}{2n}.
\]
Consequently, for each odd \(n\),
\[
\min_{L\ni o}q_n(L)=\frac12-\frac1{2n}\tan^2\!\left(\frac{\pi}{2n}\right).
\]
Exactly \(n\) unoriented lines achieve the minimum: their directions make angles \((2j+1)\pi/(2n)\), with \(j=0,\ldots,n-1\), from a fixed vertex radius, modulo \(\pi\). The exact bisection directions for odd \(n\) are the \(n\) reflection axes; they have \(q_n=1/2\). All intermediate fractions occur. The smallest fractions increase strictly along the odd integers \(n\geq3\); their deficit satisfies
\[
\frac12-\min_Lq_n(L)=\frac{\pi^2}{8n^3}+\frac{\pi^4}{48n^5}+O(n^{-7}).
\]
In particular, the triangle yields \(4/9\), already known; the regular pentagon yields \(1/2-\tan^2(\pi/10)/10\).

## Assumptions and scope
The center is the area centroid of the full regular polygon, which equals its circumcenter. Length is ordinary Euclidean boundary arclength (the length of each of the two boundary paths between the two line-intersection points), **not** the perimeter of either cut-off planar region including the cutting chord. The cutting line is unoriented, and a line passing through a vertex is admitted by continuity. All \(n\geq3\) are covered, including the triangular case. The theorem does not assert a lower bound for arbitrary convex bodies.

## Proof
When \(n\) is even, central inversion maps \(P_n\) to itself and swaps the two boundary arcs between the endpoints of every central chord. Their lengths are equal.

Let \(n=2k+1\) be odd and normalize the circumradius to one. Put \(\beta=\pi/n\), \(v_j=(\cos(2j\beta),\sin(2j\beta))\), and take the central cutting direction \((\cos\alpha,\sin\alpha)\). An unoriented line is invariant under changing its direction by \(\pi\); because \(n\) is odd, their multiples modulo \(\pi\) include shifts by \(\pi/n\). Thus, after an allowed symmetry, \(0\leq\alpha\leq\beta\). In this sector the positive-ray boundary intersection is on \([v_0,v_1]\), at \((1-u)v_0+uv_1\), and the negative-ray intersection is on \([v_k,v_{k+1}]\), at \((1-v)v_k+vv_{k+1}\), with \(u,v\in[0,1]\).

Writing \(t=\tan\alpha\) and using the equality of slopes of the positive and negative intersections gives
\[
 u=\frac{t}{\sin(2\beta)+(1-\cos(2\beta))t},
 \qquad v=\frac12+\frac{t\cot\beta}{2}.
\]
These formulas remain valid at both sector endpoints. Since every edge has the same length \(a\), the counterclockwise arc from the first intersection to the second has length \(a(k-u+v)\); the other arc has length \(a(n-k+u-v)\). Their difference from half the perimeter is controlled by
\[
\begin{aligned}
 u-\left(v-\frac12\right)
 &=\frac{t}{\sin(2\beta)+(1-\cos(2\beta))t}-\frac{t\cot\beta}{2}\\
 &=\frac{t(\tan\beta-t)}{2(1+t\tan\beta)}
 =\frac12\tan\alpha\tan(\beta-\alpha).
\end{aligned}
\]
The last expression is nonnegative because \(0\leq\alpha\leq\beta<\pi/2\). Consequently the first arc is the shorter one, of length
\[
 a\left(\frac n2-\frac12\tan\alpha\tan(\beta-\alpha)\right).
\]
Division by the total perimeter \(na\) proves the exact directional law.

For \(0\leq\alpha\leq\beta\), set \(z=\cos(2\alpha-\beta)\) and \(c=\cos\beta>0\). The product has the exact representation
\[
\tan\alpha\tan(\beta-\alpha)=\frac{z-c}{z+c}.
\]
Here \(c\leq z\leq1\), with \(z=1\) only when \(\alpha=\beta/2\). Because \(z\mapsto(z-c)/(z+c)\) is strictly increasing, the product has a unique maximum \(\tan^2(\beta/2)\) in the sector. Unoriented central lines modulo \(\pi\) therefore attain the minimum exactly at the \(n\) half-axis directions \((2j+1)\beta/2\). Zero product occurs only at the endpoints \(\alpha=0,\beta\), which correspond to reflection axes. Continuity gives all intermediate fractions.

For the odd-index monotonicity, \(n\mapsto \tan^2(\pi/(2n))/n\) is strictly decreasing for real \(n\geq3\): each of its positive factors decreases strictly. Finally, use \(\tan^2 z=z^2+(2/3)z^4+O(z^6)\) at \(z=\pi/(2n)\) to obtain the stated expansion. For \(n=3\), \(\tan^2(\pi/6)=1/3\), giving \(4/9\). This completes the proof.

## Verification
The accompanying `verify.py` computes the two intersections of a central line with an independently constructed polygonal boundary, reconstructs the two arc lengths, and compares their normalized minimum to the formula. It tests interior and near-endpoint angles for odd and even degrees, verifies equality cases, and performs exact-rational spot checks of the algebraic tangent identity. Run `python verify.py`. These checks are finite corroboration; the preceding sector decomposition and algebraic argument prove the infinite family.

## Relationship to prior work
Berele and Catoiu (2026, arXiv:2603.23653) establish the sharp boundary-perimeter split for every triangle and a broader conjecture for all planar convex sets; their equilateral triangle case is exactly the \(n=3\) instance above. They do not give a regular-polygon directional law or the sharp odd-sided coefficients for arbitrary \(n\geq5\). The classical Winternitz theorem controls enclosed *area*, a different functional. The present statement concerns boundary-length portions cut by lines through the *area centroid*; it is neither an arbitrary-body solution nor a consequence of centrally symmetric polygon bisection, since odd regular polygons are not centrally symmetric.

## Limitations
No bound is asserted for nonregular odd polygons or arbitrary planar convex bodies. The formula describes boundary arcs, excluding the chord; adding the chord changes the question. The comparison with published literature and indexed mathematical findings did not reveal equivalent coverage, but cannot exclude unindexed or inaccessible historical treatments. The full continuous-domain theorem follows analytically, not from numerical sampling.

## References
1. A. Berele and S. Catoiu, *The Perimeter Winternitz Theorem in a Triangle*, arXiv:2603.23653, first submitted 24 March 2026; primary MSC 52A10 and 52A38. https://arxiv.org/html/2603.23653v1 .
2. B. H. Neumann, *Partitions of mass distributions and of convex bodies by hyperplanes*, Journal of the London Mathematical Society 20 (1945), 226–237. Cited by Berele–Catoiu for historical context on boundary-perimeter partitions.
