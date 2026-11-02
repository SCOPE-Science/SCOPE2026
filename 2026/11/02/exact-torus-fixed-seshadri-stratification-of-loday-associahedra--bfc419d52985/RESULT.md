# Exact torus-fixed Seshadri stratification of Loday associahedra

## Finding
For each integer \(n\ge3\), set
\[
P_n=\sum_{1\le i\le j\le n}\Delta_{[i,j]},\qquad
\Delta_{[i,j]}=\operatorname{conv}\{e_i,\ldots,e_j\}\subset\mathbb R^n.
\]
Let \(X_n\) be its smooth projective toric variety and \(L_n\) the ample integral toric polarization given by \(P_n\). Write \(C_n=\frac{1}{n+1}\binom{2n}{n}\). The torus fixed points \(p_T\) correspond bijectively to the \(C_n\) full rooted plane binary trees with \(n\) internal vertices.

**Theorem.** Each fixed point satisfies \(\varepsilon(L_n;p_T)\in\{1,2\}\). With \(g_n\) denoting the number of fixed points where this constant is \(2\), one has
\[
\#\{p_T:\varepsilon(L_n;p_T)=2\}=g_n,
\qquad\#\{p_T:\varepsilon(L_n;p_T)=1\}=C_n-g_n,
\]
where \(G(z)=\sum_{n\ge0}g_nz^n\), uniquely determined by \(G(0)=1\), satisfies
\[
z(1+z)G(z)^2-(1+z+2z^2)G(z)+(1+z)=0.
\]
The initial numbers \((g_0,\ldots,g_{11})\) are \((1,1,0,1,2,4,10,23,56,138,344,870)\). Both values occur for every \(n\ge3\). In contrast, at every point \(q\) of the dense algebraic torus, \(\varepsilon(L_n;q)=n-1\).

## Assumptions and scope
Work over \(\mathbb C\). The affine lattice of \(P_n\) is \(\mathbb Z^n\cap\{\sum_i x_i=n(n+1)/2\}\), with difference lattice \(M=\{u\in\mathbb Z^n:\sum_i u_i=0\}\). Each subinterval simplex has unit lattice scale and each interval occurs with coefficient one. This normalization matters: multiplying the polytope by a positive integer multiplies all the stated Seshadri constants.

The symbol \(\varepsilon(L;p)\) denotes \(\inf_{C\ni p}(L\cdot C)/\operatorname{mult}_p(C)\), over integral curves through \(p\). A planar binary tree has an empty leaf as a subtree with no internal vertex. For a rotation \(((A B) C)\leftrightarrow(A(B C))\), write \(a,c\) for the respective numbers of leaves of the outer subtrees \(A,C\).

## Proof
**1. Geometry and toric reduction.** The interval sets form the graphical building set of a path; their Minkowski sum \(P_n\) is Loday's simple lattice associahedron, with a smooth normal fan. Its vertices correspond to rooted plane binary trees and its edges to local binary-tree rotations (Pilaud–Santos–Ziegler, and the underlying Loday construction). For a smooth projective polarized toric variety, \(\varepsilon(L;p)\) at a torus fixed point equals the minimum lattice length of edges incident to its vertex. Indeed, blowing up the fixed point is toric; the torus-invariant curves in the blow-up are exceptional curves of nonnegative intersection with \(\pi^*L-tE\), strict transforms of incident invariant curves of intersection \(\ell-t\) (where \(\ell\) is their lattice edge length), and invariant curves not through the point of unchanged positive degree. Toric nefness is equivalent to nonnegative intersection with all invariant curves, so the nef threshold is the smallest incident edge length.

**2. Rotation edge lengths.** In Loday's integral vertex coordinates, the coordinate attached to an internal node is the product of the numbers of leaves of its left and right children. For a rotation \(((A B) C)\leftrightarrow(A(B C))\) with \(a,b,c\) leaves in its three subtrees, the two changing coordinates, indexed in inorder by \(i,j\), change from \(ab,(a+b)c\) to \(a(b+c),bc\). The difference vector is \(ac(e_i-e_j)\), up to sign. Since \(e_i-e_j\) is primitive in \(M\), the incident lattice length is exactly \(ac\). Therefore
\[
\varepsilon(L_n;p_T)=\min_{\text{local rotations of }T}ac.
\]

**3. No fixed constant exceeds two.** Choose an internal node of maximum depth in \(T\). Both its children are leaves (it is a cherry). Its sibling at the parent is either a leaf or another cherry; otherwise that sibling has an internal descendant at greater depth. The rotation at the parent involving these two children has outer-subtree leaf counts \((1,1)\) in the first case or \((1,2)\) or \((2,1)\) in the second. Thus some edge has lattice length at most two, while all rotation lengths are positive integers. Hence the fixed-point constants are exactly in \(\{1,2\}\).

**4. Exact counting and algebraic equation.** A tree has fixed-point constant \(2\) precisely when it contains no local rotation whose outermost subtrees each have one leaf. Let \(G(z)\) enumerate such avoidance trees by internal-node count, including the empty leaf. By left–right symmetry, let \(A(z)\) enumerate avoidance trees with an internal root whose left child is a leaf; it equally counts those whose right child is a leaf.

For a good tree whose root has left child a leaf, the right child must be good and cannot itself have root-right-child a leaf, or else the new root supports the forbidden rotation. Thus
\[
A(z)=z\bigl(G(z)-A(z)\bigr),\qquad A(z)=\frac{zG(z)}{1+z}.
\]
A new root with arbitrary good children has generating function \(zG(z)^2\). It is forbidden precisely in the two *disjoint* cases: left child is a good internal tree whose root-left-child is a leaf and right child is a leaf; or the reflected case. These each contribute \(zA(z)\). Accordingly
\[
G(z)=1+zG(z)^2-2zA(z)
    =1+zG(z)^2-\frac{2z^2}{1+z}G(z).
\]
Clearing the denominator gives the announced quadratic. It determines a unique formal series with constant coefficient one, since the coefficient of \(G\) at \(z=0\) is \(-1\). The displayed sequence follows by comparing coefficients. The balanced three-internal-node tree is good, and attaching an additional root with that tree as left subtree and a leaf as right subtree preserves goodness provided the old root has internal left child; the construction preserves that condition inductively. Therefore \(g_n\ge1\) for all \(n\ge3\). Left combs supply forbidden rotations for every \(n\ge3\), so \(C_n-g_n\ge1\).

**5. Dense-torus comparison.** The lattice width of \(P_n\) is \(n-1\). To see this, the width in a nontrivial coordinate cut \(I\subsetneq[n]\) equals the number of subintervals meeting both \(I\) and its complement: each simplex \(\Delta_{[i,j]}\) contributes width one precisely in this case. Every cut has an adjacent boundary pair \(k,k+1\). The \(k(n-k)\) intervals containing both positions cross the cut, hence the cut width is at least \(k(n-k)\ge n-1\). The cut \(I=\{1\}\) has width exactly \(n-1\). Ito's generalized-permutohedron theorem shows that the width minimum is realized by such a cut and identifies the Seshadri constant at the torus identity with lattice width. Torus translation then gives \(\varepsilon(L_n;q)=n-1\) for all dense-torus points \(q\).

## Verification
The standalone Python 3 script `check_associa.py` uses exact integers only. It enumerates all rooted plane binary trees with \(2\le n\le8\), constructs their Loday coordinates, generates every local rotation, independently obtains the lattice length from the greatest common divisor of coordinate differences, and compares each with the leaf-count product. It verifies the two fixed-point strata and the interval-cut widths, and independently computes coefficients of the algebraic series through \(n=11\). It prints `VERIFY_OK`. This finite test is corroboration, not the proof for all \(n\).

For illustration, the numbers with Seshadri value \(2\) in dimensions \(n-1=2,3,4,5,6,7\) are \(1,2,4,10,23,56\), among \(5,14,42,132,429,1430\) fixed points respectively.

## Relationship to prior work
Ito's 2026 theorem establishes the dense-torus identity Seshadri constant and Gromov width for generalized permutohedra in terms of lattice width, not the distribution of local constants at their torus fixed points. The 2023 survey of Pilaud, Santos and Ziegler records the integral Loday realization, vertex coordinates and rotation combinatorics; those geometric ingredients are prior work. Dotsenko, Shadrin and Vallette study the toric varieties and their fixed-point/binary-tree correspondence. The standard fixed-point edge-minimum principle is toric intersection theory, not claimed as new. The contribution here is the exact two-stratum law and nontrivial avoidance generating function for all dimensions, together with its comparison to the known dense-torus invariant. Earlier implicit treatments of this particular tree-pattern count remain possible.

## Limitations
The statements concern the standard unit-weight integral Loday realization, not all realizations of the associahedron, arbitrary graph associahedra, or values of the Seshadri function on other non-dense torus orbits. The independent historical priority and any outside mathematical validation are unresolved. The finite checks do not prove the all-dimensional claims; the combinatorial and toric arguments above do.

## References
1. Atsushi Ito, *Seshadri constants and Gromov widths of toric varieties associated with generalized permutohedra*, arXiv:2606.06816v1 (first public June 5, 2026), Theorem 1.1 and Corollary 1.2. https://arxiv.org/html/2606.06816v1
2. Vincent Pilaud, Francisco Santos and Günter M. Ziegler, *Celebrating Loday's associahedron*, Archiv der Mathematik 121 (2023), 559–601; arXiv:2305.08471. https://link.springer.com/article/10.1007/s00013-023-01895-6
3. Vladimir Dotsenko, Sergey Shadrin and Bruno Vallette, *Toric varieties of Loday's associahedra and noncommutative cohomological field theories*, arXiv:1510.03261v2. https://arxiv.org/abs/1510.03261
4. Sandra Di Rocco, *Generation of k-jets on toric varieties*, arXiv:alg-geom/9710018. https://arxiv.org/abs/alg-geom/9710018
