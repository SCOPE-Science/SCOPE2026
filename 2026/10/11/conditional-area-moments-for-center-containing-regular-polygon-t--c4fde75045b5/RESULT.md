# Conditional area moments for center-containing regular-polygon triangles

## Finding
Fix an integer \(n\ge 3\), a radius \(R>0\), and a regular \(n\)-gon of circumradius \(R\) centered at the origin. Select uniformly one of the \(\binom n3\) unordered triples of **distinct** vertices. Let \(A\) be the Euclidean area of their triangle, and \(E\) the event that the origin lies **strictly inside** it. Put \(\theta=\pi/n\), \(\mu_n=\mathbb E[A/R^2\mid E]\), and \(q_n=\mathbb E[(A/R^2)^2\mid E]\). Then for **odd** \(n\ge3\),
\[
\mathbb P(E)=\frac{n+1}{4(n-2)},\qquad
\mu_n=\frac{3n}{(n^2-1)\sin\theta},
\]
\[
q_n=\frac{3(n^2-1+\sec^2\theta)}{8(n^2-1)}
+\frac{3(1+\cos\theta)}{(n^2-1)\sin^2\theta}
+\frac{3}{2(n^2-1)\cos\theta}.
\]
For **even** \(n\ge6\),
\[
\mathbb P(E)=\frac{n-4}{4(n-1)},\qquad
\mu_n=\frac{3\cot\theta}{n-2},\qquad
q_n=\frac{3n(n-8)/8+6\cot^2\theta}{(n-2)(n-4)}.
\]
For \(n=4\), \(\mathbb P(E)=0\), so the conditional moments are undefined. For all remaining orders, \(\operatorname{Var}(A\mid E)=R^4(q_n-\mu_n^2)\). In particular, the dimensionless conditional variance has the common limit
\[
V_\infty=\frac38-\frac3{\pi^2}>0,
\]
but with distinct sharp parity corrections:
\[
\begin{aligned}
q_n-\mu_n^2&=V_\infty-\left(\frac{12}{\pi^2}+\frac58\right)n^{-2}+O(n^{-4})&&\text{for odd }n,\\
q_n-\mu_n^2&=V_\infty-\frac3{4n}+O(n^{-2})&&\text{for even }n.
\end{aligned}
\]
Both conditional means tend to \(3/\pi\). The parity difference is sensitive to diameter-side triangles at even orders, whose center lies on the boundary and which are excluded by strict containment; odd orders have no such configurations.

## Assumptions and scope
The sampling law is uniform over distinct triples of *vertices*, not independent points on the circle and not uniform points inside the disk. Strict containment excludes all boundary cases. The unit-circle normalization \(R=1\) is used in the proof; geometric area scales by \(R^2\) and its variance by \(R^4\). No formula here concerns random translations, nonregular polygons, or triangles with the center merely in the closed convex hull.

## Proof
List the three chosen vertices in counterclockwise order. Their cyclic positive integer gaps \((a,b,c)\) satisfy \(a+b+c=n\). The origin is strictly in the triangle precisely when each gap is smaller than a semicircle, equivalently
\[
a,b,c\ge1,\qquad a+b+c=n,\qquad 2\max(a,b,c)<n.
\]
Indeed, failure of this condition places all three vertices in a closed semicircle; equality places the origin on a diameter edge. Conversely, three successive arcs all shorter than a semicircle place the origin strictly on the interior side of each triangle edge.

Each admissible cyclic gap triple, together with one of \(n\) initial vertices, determines a triangle with precisely three choices of initial vertex. Thus the number of admissible unordered triangles equals \(n/3\) times the number \(N_n\) of admissible ordered gap triples. With \(k=\lfloor n/2\rfloor\), elementary bounded-composition counting gives
\[
N_n=\begin{cases}(n^2-1)/8,& n=2k+1,\\(n-2)(n-4)/8,&n=2k.\end{cases}
\]
Dividing \(nN_n/3\) by \(\binom n3\) proves both event probabilities. For \(n=4\), there is no such composition.

Write \(s_a=\sin(2a\theta)\). The central-angle formula for area gives, on every admissible triple,
\[
\frac A{R^2}=2\sin(a\theta)\sin(b\theta)\sin(c\theta)
=\frac{s_a+s_b+s_c}{2}.
\]
Here all three sine terms are positive. By symmetry of the admissible compositions, define
\[
H_n=\sum_{(a,b,c)}s_a,\quad
U_n=\sum_{(a,b,c)}s_a^2,\quad
C_n=\sum_{(a,b,c)}s_as_b,
\]
where each sum ranges over exactly the \(N_n\) admissible ordered gap triples. Expanding the area expression and rotating the three gaps yields
\[
\mu_n=\frac{3H_n}{2N_n},\qquad
q_n=\frac{3U_n+6C_n}{4N_n}.
\]

The following exact trigonometric sums evaluate all three quantities:
\[
\begin{array}{c|ccc}
& H_n & U_n & C_n\\ \hline
n\text{ odd}
&\dfrac{n}{4\sin\theta}
&\dfrac{n^2-1+\sec^2\theta}{16}
&\dfrac{\cot(\theta/2)}{4\sin\theta}+\dfrac{\tan\theta}{8\sin\theta}\\[4pt]
n\text{ even}
&\dfrac{(n-4)\cot\theta}{4}
&\dfrac{n(n-4)}{16}
&\dfrac12\cot^2\theta-\dfrac n8.
\end{array}
\]
For completeness, these evaluations reduce to one-variable finite sums as follows. When \(n=2k+1\), a fixed first gap \(a\in\{1,\ldots,k\}\) has \(a\) allowed second gaps, precisely \(b=k+1-a,\ldots,k\). When \(n=2k\), a first gap \(a\in\{1,\ldots,k-1\}\) has \(a-1\) allowed second gaps, namely \(b=k+1-a,\ldots,k-1\). Consequently,
\[
\begin{array}{ll}
\text{odd:}&H_n=\sum_{a=1}^k a\sin(2a\theta),\quad U_n=\sum_{a=1}^k a\sin^2(2a\theta),\\
\text{even:}&H_n=\sum_{a=1}^{k-1}(a-1)\sin(2a\theta),\quad U_n=\sum_{a=1}^{k-1}(a-1)\sin^2(2a\theta).
\end{array}
\]
The inner second-gap sums used for \(C_n\) are, respectively,
\[
\sum_{b=k+1-a}^{k}\sin(2b\theta)=\frac{\sin^2(a\theta)}{\sin\theta}
\quad(n=2k+1),
\]
\[
\sum_{b=k+1-a}^{k-1}\sin(2b\theta)=
\frac{\sin((a-1)\theta)\sin(a\theta)}{\sin\theta}
\quad(n=2k).
\]
Substitute these inner sums in \(C_n=\sum_a\sin(2a\theta)\sum_b\sin(2b\theta)\). The identities
\[
\sum_{j=1}^{m}jz^j=\frac{z(1-(m+1)z^m+mz^{m+1})}{(1-z)^2}
\quad(z\ne1),
\]
and \(\sin u\sin v=(\cos(u-v)-\cos(u+v))/2\), applied at \(z=e^{2i\theta}\) and \(z=e^{4i\theta}\), give the displayed table. In particular, for odd orders, \(\sum_{a=1}^k\sin(2a\theta)=\tfrac12\cot(\theta/2)\) and \(\sum_{a=1}^k\sin(4a\theta)=-\tfrac12\tan\theta\). For even orders, \(\sum_{a=1}^{k-1}\sin(2a\theta)=\cot\theta\) and \(\sum_{a=1}^{k-1}\sin((4a-1)\theta)=\sin\theta\), sufficient to reconstruct the \(C_n\) entries. Likewise the weighted geometric-series identity reconstructs both \(H_n\) and \(U_n\), with \(\sin^2u=(1-\cos2u)/2\).

Substituting the tabulated values and the counts \(N_n\) in the moment identities yields the claimed formulas after simplification, including the half-angle identity \(\cot(\theta/2)=(1+\cos\theta)/\sin\theta\). Finally, Taylor expansion at \(\theta=\pi/n\to0\) yields the parity-dependent variance expansions. More explicitly, the means satisfy
\[
\mu_n=\begin{cases}
3/\pi+(3/\pi+\pi/2)n^{-2}+O(n^{-4}),&n\text{ odd},\\
3/\pi+6/(\pi n)+O(n^{-2}),&n\text{ even};
\end{cases}
\]
and substitution into \(q_n-\mu_n^2\) gives the displayed variance coefficients. This proves the assertions.

## Verification
The standalone `verify_center_triangles.py` script uses Euclidean Cartesian coordinates, oriented-edge tests for strict origin containment, and determinant areas for all \(\binom n3\) triangles for each \(3\le n\le62\). It independently compares containment proportions, first and second moments, and admissible-gap enumeration. It additionally checks the stated asymptotic terms at large orders. Execute `python3 verify_center_triangles.py`; the observed output begins with `VERIFY_OK`, with \(595665\) total triangles and \(148800\) strictly center-containing triangles in the tested finite orders. Finite tests do not replace the all-orders trigonometric argument.

## Relationship to prior work
Madras and KC (2006) studied exactly the same uniform distinct-vertex triangle sampling model, but calculated **unconditional** expected area and perimeter; their area formula is \(3n\cot(\pi/n)/(2(n-1)(n-2))\) at unit circumradius. They mention a sample center-containing triangle, but their stated results and worked derivations do not calculate the present **conditional** moments or variance. The center-containment probability for odd orders was also derived in a 2014 mathematical discussion; it is included as background and is not asserted to be new. Classical Wendel-type sampling results treat related continuous independent-point laws. The continuous-circle limiting mean \(3/\pi\) is consistent with known geometric-probability observations and is not separately claimed as novel. The asserted contribution is the complete finite-order conditional first/second-moment evaluation together with the sharp difference between odd and even variance convergence.

## Limitations
The proof applies to one precisely specified finite discrete sampling law, not arbitrary cyclic point sets. The all-orders identities are analytic; computer checks cover only finite orders. The conditional distribution is not defined for the square, and boundary-containing triangles (diameter-side triangles in even orders) are intentionally excluded. Although relevant indexed sources were compared, an unindexed earlier equivalent calculation cannot be ruled out without independent historical review. The 2006 initiating manuscript visibly bears the date October 2, 2006; its exact first online-posting day was not separately established.

## References
1. Anna Madras and Shova KC, “Randomly Generated Triangles whose Vertices are Vertices of a Regular Polygon,” *Rose-Hulman Undergraduate Mathematics Journal* **7** (2006), issue 2, article 12. Original manuscript dated October 2, 2006. https://scholar.rose-hulman.edu/rhumj/vol7/iss2/12/
2. “Probability of a random triangle containing the center of a polygon,” *Mathematics Stack Exchange*, October 15–18, 2014, https://math.stackexchange.com/questions/975432/probability-of-a-random-triangle-containing-the-center-of-a-polygon
3. James G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–111; comparison with the continuous independent-point sampling model.
4. “The expected area of a triangle made up three points picked randomly inside a circle of radius, and contains the center,” *Mathematics Stack Exchange*, March 5, 2013, https://math.stackexchange.com/questions/321332/ ; a distinct uniform-**disk-interior** point model.
