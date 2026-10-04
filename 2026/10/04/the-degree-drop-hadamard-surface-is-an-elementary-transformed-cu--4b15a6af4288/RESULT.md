# The degree-drop Hadamard surface is an elementary-transformed cubic scroll
## Finding
Let \(X,Y\subset\mathbb P^4\) be the line and conic in Example 4.2 of Calussi--Carlini--Fatabbi--Lorenzini. With the source parametrizations
\[
X=[y_0-y_1:y_0-y_1:y_0-y_1:y_0:2y_0],\qquad
Y=[z_0^2:z_0z_1:z_1^2:z_0^2:z_0z_1],
\]
the Hadamard product \(S=X\star Y\) is exactly the smooth rational normal cubic scroll \(S(1,2)\subset\mathbb P^4\). Its prime ideal is
\[
I_S=(x_0x_2-x_1^2,\ x_0x_4-2x_1x_3,\ x_1x_4-2x_2x_3),
\]
the \(2\times2\) minors of
\[
\begin{pmatrix}x_0&x_1&2x_3\\x_1&x_2&x_4\end{pmatrix}.
\]
The Hadamard parametrization has one base point
\[
p=([1:1],[0:1])\in\mathbb P^1\times\mathbb P^1.
\]
Blowing up \(p\) resolves the map. The strict transform of the source fiber \(z_0=0\) is contracted to \(q=[0:0:1:0:0]\). The exceptional divisor maps isomorphically to the ruling line \(V(x_0,x_1,x_3)\), while the strict transform of \(y_0=y_1\) maps to the unique directrix line \(V(x_0,x_1,x_2)\). Thus the source's anomalous degree \(3\) is the intersection-theoretic drop \((1,2)^2-1=4-1=3\) caused by the single simple base point.

## Assumptions and scope
The ground field is algebraically closed of characteristic zero, as in the source. The statement concerns only Example 4.2 and its displayed coordinates. It identifies the image, its ideal, and the birational modification resolving the displayed Hadamard parametrization; it does not claim an analogous description for arbitrary non-generic Hadamard products.

## Proof
Coordinatewise multiplication of the displayed parametrizations gives
\[
[(y_0-y_1)z_0^2:(y_0-y_1)z_0z_1:(y_0-y_1)z_1^2:y_0z_0^2:2y_0z_0z_1].
\]
Direct substitution annihilates all three displayed quadrics. On the chart \(x_0\ne0\), put \(t=x_1/x_0\) and \(r=x_3/x_0\). The quadrics then force
\[
x_2/x_0=t^2,\qquad x_4/x_0=2rt,
\]
so this chart is an affine plane and the parametrization is birational there, with \(t=z_1/z_0\) and \(r=y_0/(y_0-y_1)\). The three quadrics are the standard determinantal equations of the cubic scroll; a projective Jacobian calculation has rank \(2\) everywhere, so the surface is smooth.

The five source sections vanish simultaneously only at \(p=([1:1],[0:1])\). In the affine coordinates \(y_0=z_1=1\), \(y_1=1+u\), \(z_0=t\), they become
\[
(-ut^2,-ut,-u,t^2,2t),
\]
so the base ideal is exactly \((u,t)\): the base point is simple. On the blow-up, the exceptional divisor is mapped by the linear terms \((-u,2t)\), hence isomorphically to \(V(x_0,x_1,x_3)\). Setting \(z_0=0\) gives \([0:0:y_0-y_1:0:0]\), so the strict transform of that fiber is contracted to \(q\). Setting \(y_0=y_1\) gives the line \(V(x_0,x_1,x_2)\). Before the blow-up these two source fibers meet only at \(p\); after blowing up they are disjoint. Contracting the strict transform of \(z_0=0\) leaves the strict transform of \(y_0=y_1\) with self-intersection \(-1\), identifying its image as the directrix of \(\mathbb F_1\simeq S(1,2)\).

Finally \(\mathcal O(1,2)^2=4\) on \(\mathbb P^1\times\mathbb P^1\). Resolving one simple base point replaces the moving divisor by \(\pi^*\mathcal O(1,2)-E\), whose square is \(4-1=3\), exactly the degree observed in the source.

## Verification
The accompanying `verify_example42.py` reproduces the three polynomial identities, proves the unique base point on the four standard affine charts, checks projective smoothness by adjoining all \(2\times2\) Jacobian minors on each coordinate chart, verifies the birational affine normal form, and checks the local blow-up sections and the two distinguished source fibers. Running it with SymPy returns `VERIFY_OK`.

## Relationship to prior work
Calussi--Carlini--Fatabbi--Lorenzini state that Example 4.2 has dimension \(2\), degree \(3\), no singularities, and that its projection center lies on the relevant Segre--Veronese surface; they use it to show failure of their generic degree and singular-locus conclusions. They do not identify the three defining quadrics, the rational normal scroll, the unique base point of the displayed parametrization, or the resolved contraction geometry above. The Del Pezzo--Bertini classification implies abstractly that any smooth nondegenerate degree-\(3\) surface in \(\mathbb P^4\) is a rational normal scroll; that general theorem covers the abstract scroll type once the source's smoothness and degree are known, but not the coordinate ideal or the elementary transformation that explains this specific Hadamard degree drop.

## Limitations
The argument is tied to the source coordinates. The novelty is not the general classification of smooth degree-\(3\) surfaces in \(\mathbb P^4\); it is the exact ideal and resolved source-to-scroll geometry for this named Hadamard example. No claim is made that every center lying on a Segre--Veronese surface produces the same contraction pattern.

## References
G. Calussi, E. Carlini, G. Fatabbi, A. Lorenzini, *On the Hadamard product of degenerate subvarieties*, arXiv:1804.01388, Example 4.2.

D. Eisenbud, J. Harris, *On varieties of minimal degree (a centennial account)*, Proc. Sympos. Pure Math. 46 (1987), 3--13.
