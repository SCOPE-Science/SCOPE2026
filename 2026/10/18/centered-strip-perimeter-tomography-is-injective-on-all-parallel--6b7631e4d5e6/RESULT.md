# Centered-strip perimeter tomography is injective on all parallelograms

## Finding

**Theorem.** Fix \(t>0\). Let \(P,Q\subset\mathbb R^2\) be full-dimensional origin-centered Euclidean parallelograms that both contain the closed disk \(tB_2\) in their interiors. For each unit \(u\in S^1\), set
\[
S_t(u)=\{x\in\mathbb R^2:|\langle x,u\rangle|\le t\},\qquad
F_K(u)=\operatorname{per}(K\cap S_t(u)).
\]
If \(F_P(u)=F_Q(u)\) for every \(u\in S^1\), then \(P=Q\). No relation between the edge directions, side lengths, or angles of the two parallelograms is assumed.

This gives uniqueness from fixed-width **slab-intersection perimeters**, not from slab-intersection areas, ordinary perimeters, or projection widths.

## Assumptions and scope

Write each origin-centered parallelogram as
\[
K=\{sa+rb:|s|\le1,\ |r|\le1\},
\]
with independent \(a,b\in\mathbb R^2\). Put
\[
A=\|a\|_2,\quad B=\|b\|_2,\quad C=|\det(a,b)|>0,\qquad
U=|\langle u,a\rangle|,\quad V=|\langle u,b\rangle|.
\]
The distances from the origin to the pairs of supporting lines parallel to \(a\) and \(b\) are respectively \(C/A\) and \(C/B\). Thus the disk hypothesis is **equivalent** to \(0<t<\min\{C/A,C/B\}\). For every \(u\in S^1\), the support value \(U+V\) is strictly greater than \(t\).

Perimeter is ordinary Euclidean boundary length of the full-dimensional polygon \(K\cap S_t(u)\). The hypothesis avoids degeneracies in which the slab contains the entire body or intersects its supporting lines tangentially. The equalities delimiting the three formulas below are handled by continuity.

## Proof

### 1. Exact perimeter chamber formulas

For \(U+t<V\), the strip cuts only the two sides whose direction is parallel to \(a\), and the intersection is a parallelogram. In the coordinates \(x=sa+rb\), \(|s|\le1\), its \(r\)-interval has center \(-s\langle u,a\rangle/\langle u,b\rangle\) and half-length \(t/V\). The intersection has spanning half-vectors
\[
a-\frac{\langle u,a\rangle}{\langle u,b\rangle}b,\qquad
\frac{t}{\langle u,b\rangle}b,
\]
whose lengths are \(C/V\) and \(tB/V\). Hence
\[
F_K(u)=\frac{4(C+tB)}{V}\qquad\text{if }U+t<V.\tag{1}
\]
Exchanging \(a,b\) gives
\[
F_K(u)=\frac{4(C+tA)}{U}\qquad\text{if }V+t<U.\tag{2}
\]
Otherwise \(|U-V|<t<U+V\), and both strip boundaries truncate an opposite pair of vertices. The original perimeter is \(4(A+B)\). Define \(\delta=U+V-t>0\). At each truncated vertex, the two incident original edges lose lengths \(\delta A/U\) and \(\delta B/V\), while the new connecting cap has length \(\delta C/(UV)\). There are two such vertices. Therefore
\[
F_K(u)=4(A+B)-2(U+V-t)\left(\frac AU+\frac BV-\frac C{UV}\right)
\quad\text{if }|U-V|<t<U+V.\tag{3}
\]
The expression in (3) is well-defined in its chamber because \(U,V>0\). Equations (1)–(3) extend continuously to chamber walls, which do not affect the open-interval argument.

### 2. Pure-chamber and mixed-chamber germs are incompatible

On any open direction arc where the signs of \(\langle u,a\rangle\), \(\langle u,b\rangle\) are fixed, introduce the signed linear forms
\[
X(u)=\sigma\langle u,a\rangle,\qquad
Y(u)=\tau\langle u,b\rangle,
\]
so \(U=X(u)>0\), \(V=Y(u)>0\) on that arc. The right side of (3), interpreted with these signed forms **outside** its physical chamber, is the rational-trigonometric expression
\[
M(u)=4(A+B)-2(X+Y-t)\left(\frac A X+\frac B Y-\frac C{XY}\right).\tag{4}
\]
It cannot agree on any nonempty open arc with a pure-chamber expression \(H/L(u)\), where \(H\ne0\) is constant and \(L\) is a nonzero linear form in \(u\). Indeed, multiply an alleged equality by \(X(u)Y(u)L(u)\). This yields a trigonometric-polynomial identity in \(\cos\theta,\sin\theta\) on an open interval, hence on the entire circle. Consequently, as meromorphic expressions on the circle, \(M(u)=H/L(u)\), and in particular \(M(-u)=-M(u)\).

Direct algebra, however, yields
\[
M(u)+M(-u)=\frac{4}{X(u)Y(u)}
\left[(X(u)-Y(u))(A Y(u)-B X(u))-Ct\right].\tag{5}
\]
Because \(a,b\) are independent, the forms \(X,Y\) are independent. Hence there is a unit \(u_0\) with \(X(u_0)=Y(u_0)\ne0\). At that direction the right side of (5) is
\[
-\frac{4Ct}{X(u_0)^2}\ne0,
\]
a contradiction. Notice that \(t>0\) is essential to this obstruction. Thus an analytically continued mixed perimeter germ can never coincide with any analytically continued pure perimeter germ.

### 3. Recovery of the first side direction and support distance

Fix \(P\) and write it with half-edge vectors \(a_P,b_P\). Near either of the two unit directions perpendicular to \(a_P\), one has \(U_P=0\), \(V_P=C_P/A_P>t\), and therefore \(U_P+t<V_P\) on an open neighborhood. By (1), on this neighborhood
\[
F_P(u)=\frac{4(C_P+tB_P)}{|\langle u,b_P\rangle|}.\tag{6}
\]
Since a different parallelogram \(Q\) has only finitely many chamber-change directions and signed-dot-product zeros, choose a smaller open arc on which \(Q\)'s perimeter is represented by one fixed analytic formula. The assumed equality \(F_P=F_Q\), together with Step 2, **excludes** a mixed formula for \(Q\) on that arc. Therefore \(Q\) has a pure formula of the type (1) or (2), namely
\[
F_Q(u)=\frac{4(C_Q+tD_Q)}{|\langle u,d_Q\rangle|},
\]
where \(d_Q\) is one of its two half-edge vectors and \(D_Q=\|d_Q\|_2\).

On this arc both denominator signs are constant. Equality of (6) and the last formula implies equality of two linear forms after cross-multiplication. Such equality on an open arc forces their coefficient vectors to agree. Thus \(d_Q\) is **parallel to** \(b_P\), and cancellation of its length gives
\[
\frac{C_Q}{D_Q}=\frac{C_P}{B_P}.\tag{7}
\]
In geometric terms: \(Q\) and \(P\) have the same edge direction \(b_P\) and the same distance from the origin to the pair of supporting lines **parallel to** that direction.

### 4. Recovery of the second direction and conclusion

Repeat Step 3 in an arc around either direction perpendicular to \(b_P\). It forces \(Q\)'s other edge direction to be parallel to \(a_P\), and the corresponding support-line distance to equal \(C_P/A_P\). The two directions are distinct because \(a_P,b_P\) are independent, so they must match the two distinct edge families of \(Q\). An origin-centered parallelogram is uniquely the intersection of the two centered pairs of half-planes determined by its edge directions and their support-line distances. All four boundary lines of \(P,Q\) therefore coincide, and \(P=Q\).

## Verification

The formula and the decisive identity (5) are completely symbolic and require no numerical assumptions. In particular the antiperiodicity argument compares **rational-trigonometric continuations**: it never substitutes negative physical lengths into a physical chamber inequality.

The standalone `verify_formula.py` independently clips the four vertices of randomly chosen nondegenerate parallelograms against each half-plane and sums the resulting Euclidean edge lengths. It compares this independent geometric calculation to formulas (1)–(3), including pure and mixed chambers, with a fixed pseudorandom seed and a stated floating-point tolerance. Such finite tests are checks of the formula, not proofs of the universal theorem.

## Relationship to prior work

Brendan Matthews, *Hedgehog reconstruction of polygons: Non-central sections and slabs* (arXiv:2603.00002; DOI 10.4153/S0008439526102355), proves in Theorem 1.2 reconstruction of origin-symmetric polygons from **slab areas** relative to an analytic origin-symmetric hedgehog. The introduction explicitly identifies the corresponding **perimeter** uniqueness question as unresolved by its method. A disk is an analytic origin-symmetric hedgehog, and the present theorem settles that perimeter question for the first nontrivial centrally symmetric polygon class, parallelograms, without extending the conclusion to hexagons or higher-side polygons.

V. Yaskin and M. Yaskina, *Thick sections of convex bodies* (2015, DOI 10.1016/j.aam.2015.09.010), study and establish uniqueness from **volumes** of centered thick sections of symmetric polytopes, not the Euclidean boundary perimeters used here. Other nearby width-tomography results use projections and do not logically imply uniqueness of this different nonlinear measurement function.

## Limitations

The theorem assumes both bodies are origin-centered parallelograms, \(t>0\), and the entire closed disk \(tB_2\) lies strictly in both interiors. It does **not** prove perimeter-slab tomography for arbitrary centrally symmetric polygons, unknown centers, variable-width slabs, or general analytic hedgehogs. It does not quantify stability under noisy data. An exact branch identity and a numerical experiment do not independently establish global novelty; priority in historical or poorly indexed literature remains subject to further scrutiny.

## References

1. B. Matthews, *Hedgehog Reconstruction of Polygons: Non-Central Sections and Slabs*, arXiv:2603.00002 (first arXiv submission 2025-12-29; revised 2026-07-17), Canadian Mathematical Bulletin (2026), DOI: 10.4153/S0008439526102355. See Theorem 1.2 and the immediately following open perimeter question. https://arxiv.org/abs/2603.00002 ; https://doi.org/10.4153/S0008439526102355
2. V. Yaskin and M. Yaskina, *Thick Sections of Convex Bodies*, Advances in Applied Mathematics 71 (2015), 174–189, DOI: 10.1016/j.aam.2015.09.010.
