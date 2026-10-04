# Three-edge decomposition sharpens the Hilbert comparison for the first dyadic-tree variation norm
## Finding
Let \(T\) be the rooted dyadic tree. For a real finitely supported function \(x:T\to\mathbb R\), define the first-attempt norm
\[
N_1(x)=\max\left\{\|x\|_\infty,\sup_{\mathcal I}\left(\sum_{I\in\mathcal I}|x(I_{\max})-x(I_{\min})|^2\right)^{1/2}\right\},
\]
where \(\mathcal I\) ranges over finite families of pairwise disjoint tree segments. Then
\[
\frac{\sqrt2-1}{\sqrt3}\,\|x\|_2\le N_1(x)\le\sqrt2\,\|x\|_2
\qquad(x\in c_{00}(T)).
\]
The upper constant \(\sqrt2\) is optimal. In addition, for every nonempty finite tree segment \(s\),
\[
N_1\!\left(\sum_{u\in s}e_u\right)=\sqrt{|s|}.
\]
Thus the canonical identity between the Hilbert norm and \(N_1\) has distortion at most \(\sqrt6(\sqrt2+1)\approx5.9136\).

## Assumptions and scope
The claim concerns the real first-attempt norm \(N_1\) in Section 1.1 of Argyros--Motakis, not the final norm \(\|\cdot\|_\alpha\) defining their space \(X_\alpha\). The tree is the infinite rooted binary tree, all vectors are finitely supported, and all segment families used in the supremum are finite and pairwise disjoint as subsets of the tree. No optimality is claimed for the lower comparison constant.

## Proof
For the upper estimate, if \(\mathcal I\) is pairwise disjoint, then all segment endpoints are distinct. Hence
\[
\sum_{I\in\mathcal I}|x(I_{\max})-x(I_{\min})|^2
\le 2\sum_{I\in\mathcal I}\bigl(|x(I_{\max})|^2+|x(I_{\min})|^2\bigr)
\le2\|x\|_2^2.
\]
Also \(\|x\|_\infty\le\|x\|_2\), giving \(N_1(x)\le\sqrt2\|x\|_2\). If \(u\) and \(v\) are adjacent and \(x=e_u-e_v\), then the one-edge segment \([u,v]\) gives \(N_1(x)\ge2\), while the upper estimate gives equality and \(\|x\|_2=\sqrt2\). Therefore \(\sqrt2\) is optimal.

For the lower estimate, color the tree edges with three colors so that incident edges have different colors. This can be done recursively: color the two edges from the root with two distinct colors, and at every nonroot vertex color its two outgoing edges with the two colors different from the incoming edge. Each color class is then a matching. Put
\[
E(x)=\sum_{u\to v}|x(u)-x(v)|^2=E_1(x)+E_2(x)+E_3(x),
\]
where \(E_r\) is the sum over color \(r\). Because \(x\) is finitely supported, only finitely many edges have nonzero variation. Restricting a color class to those edges therefore gives an admissible finite family of disjoint one-edge segments, so \(N_1(x)^2\ge E_r(x)\) for each \(r\), and therefore \(N_1(x)^2\ge E(x)/3\).

Let \(t=1/\sqrt2\). For every oriented parent-child edge \(u\to v\),
\[
-2x(u)x(v)\ge-tx(u)^2-t^{-1}x(v)^2.
\]
After summing over all edges, the root receives coefficient \(2-2t=2-\sqrt2\), while every nonroot vertex receives coefficient
\[
3-2t-t^{-1}=3-2\sqrt2=(\sqrt2-1)^2.
\]
Since \(2-\sqrt2>3-2\sqrt2\),
\[
E(x)\ge(3-2\sqrt2)\|x\|_2^2.
\]
Combining this with \(N_1(x)^2\ge E(x)/3\) yields
\[
N_1(x)\ge\frac{\sqrt2-1}{\sqrt3}\|x\|_2.
\]

Finally let \(x=\sum_{u\in s}e_u\) for a nonempty finite segment \(s\). Every nonzero variation term has absolute value one and must use at least one endpoint from \(s\). Pairwise disjoint test segments use distinct such endpoints, so there are at most \(|s|\) nonzero terms and \(N_1(x)\le\sqrt{|s|}\). Conversely, at each \(u\in s\) choose a one-edge segment leaving \(s\) through the child not continuing along \(s\) (and at the terminal node choose either child). These \(|s|\) segments are pairwise disjoint and each contributes one, so equality holds.

## Verification
The proof is symbolic. The three-coloring is explicit, and its only required property is that each color class is a matching. The energy estimate tracks every vertex coefficient after summing the elementary two-variable inequality. The sharp upper witness is the two-coordinate vector supported on one edge. The exact segment formula has matching upper and lower counts of nonzero unit variations. Numerically, the lower constant is approximately \(0.2391463\), the sharp upper constant is approximately \(1.4142136\), and the resulting canonical distortion bound is approximately \(5.9135914\).

## Relationship to prior work
Argyros--Motakis introduce \(N_1\) as a natural but unsuccessful dyadic-tree analogue of a James variation norm. Their Proposition 1.1 proves that its completion is isomorphic to \(\ell_2(T)\), using an upper constant \(\sqrt3\) and a four-family edge decomposition leading to the lower constant \(\sqrt{(3-2\sqrt2)/5}\). The present argument replaces the four-family split by the optimal three-edge coloring of the degree-three tree, uses the endpoint structure of the norm directly for the upper estimate, and turns their displayed lower bound for segment sums into an exact identity. A separate result previously obtained for the same source concerns the final \(X_\alpha\) norm and its uniformly bounded segment sums; it does not imply any statement about this preliminary norm \(N_1\).

## Limitations
The lower comparison constant is a certified improvement, not asserted to be optimal. The result concerns the preliminary norm \(N_1\), which the source deliberately rejects for its main construction. It does not sharpen the structural theorems for the final space \(X_\alpha\), nor does it determine the exact Banach--Mazur distance from the completion of \(N_1\) to Hilbert space.

## References
S. A. Argyros and P. Motakis, “Explicitly Defined Norms on \(JT_*\) Spaces,” arXiv:2609.31276v1, 2026, especially Section 1.1 and Proposition 1.1.
