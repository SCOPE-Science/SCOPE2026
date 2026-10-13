# Node-product local rings of the hollow \(\mathrm{SO}(4)\) surface

## Finding
Let \(k\) be any algebraically closed field of characteristic different from \(2\), and give the hollow matrix slice the *scheme-theoretic* definition
\[
X=\{M\in\mathrm{SO}_{4,k}: M_{00}=M_{11}=M_{22}=M_{33}=0\}.
\]
The surface \(X\) is reduced, a local complete intersection, and Gorenstein. Every closed point has one of three completed local rings:
\[
\begin{array}{c|c|c}
\text{stratum}&\widehat{\mathcal O}_{X,p}&e(\mathcal O_{X,p})\\\hline
\text{smooth}&k[[s,t]]&1\\
\text{curve crossing}&k[[t,x,y]]/(xy)&2\\
\text{four-branch point}&k[[x,y,z,w]]/(xy,zw)&4.
\end{array}
\]
There are exactly 24 four-branch points, namely all determinant-one signed permutation matrices whose underlying permutation is one of the three fixed-point-free double transpositions. The singular *scheme*, defined by the appropriate Fitting ideal of the Kähler differentials, is reduced and has exactly 24 irreducible curve components, each isomorphic to \(\mathbb G_m\). Precisely four singular curves pass through every four-branch point. At such a point the completed local ring of the singular scheme is
\[
k[[x,y,z,w]]/(xy,xz,xw,yz,yw,zw),
\]
the reduced union of the four coordinate axes.

## Assumptions and scope
The matrix group is the split special orthogonal group for the quadratic form \(q(u)=u_0^2+u_1^2+u_2^2+u_3^2\). All assertions concern its affine algebraic zero-diagonal *scheme* over an algebraically closed field \(k\), with \(2\) invertible. Multiplicities are Hilbert--Samuel multiplicities at closed points. The singular scheme means \(\mathrm{Fitt}_{2}(\Omega_{X/k})\) on the pure two-dimensional scheme \(X\). No assertion is made in characteristic \(2\).

## Proof
**1. Étale quaternion coordinates.** Let \(Q\) be the quaternion algebra with basis \(1,i,j,\ell\), with \(i^2=j^2=\ell^2=-1\) and \(ij=\ell=-ji\). Its conjugation and norm are \(\overline a=a_0-a_1i-a_2j-a_3\ell\) and \(N(a)=\sum_{h=0}^3a_h^2\). Set \(U=\{a\in Q:N(a)=1\}\). The left-right action
\[
\pi:U\times U\longrightarrow\mathrm{SO}_{4,k},\qquad (a,b):v\longmapsto a\,v\,\overline b
\]
is a surjective separable central isogeny with kernel \(\{(1,1),(-1,-1)\}\). To check this without requiring analytic topology: multiplicativity of the norm makes \(\pi\) an orthogonal group homomorphism, its image lies in the identity component, evaluation on \(v=1\) followed by commutation with all \(v\in Q\) shows that its kernel consists exactly of those two points, and both domain and target are connected smooth groups of dimension six. As \(2\) is invertible, its differential has zero kernel; therefore its image has full dimension and equals the connected target. The isogeny is finite étale. Hence completed local rings agree at corresponding geometric points.

**2. Four monomial equations.** Put \(u_h=a_hb_h\). Direct quaternion multiplication yields the diagonal vector of the orthogonal matrix \(\pi(a,b)\):
\[
\begin{pmatrix}M_{00}\\M_{11}\\M_{22}\\M_{33}\end{pmatrix}=
\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}
\begin{pmatrix}u_0\\u_1\\u_2\\u_3\end{pmatrix}.
\]
The displayed matrix has square \(4I\), so in characteristic different from \(2\) it is invertible. Consequently the fiber of the hollow slice under \(\pi\) is exactly the subscheme
\[
Y=\{(a,b)\in U\times U:a_hb_h=0\text{ for every }h=0,1,2,3\}.
\]
This is an identity of *ideals*, not just a description of zero sets.

**3. All completed local algebras.** Fix any geometric point \((a,b)\in Y\), and write \(A=\{h:a_h\ne0\}\), \(B=\{h:b_h\ne0\}\). These are disjoint, nonempty subsets of \(\{0,1,2,3\}\), because \(N(a)=N(b)=1\) and \(a_hb_h=0\). Let \(Z\) be their complement and \(r=|Z|\); necessarily \(r\in\{0,1,2\}\). In the completed local ring, \(a_h\) is a unit for \(h\in A\), so \(b_h=0\); likewise \(a_h=0\) for \(h\in B\). Choose \(\alpha\in A\) and \(\beta\in B\). The derivatives \(2a_\alpha\) and \(2b_\beta\) of the two norm equations are units, so formal implicit-function elimination uniquely solves for these two coordinates. What remain are \(|A|+|B|-2\) smooth coordinates and, for each \(h\in Z\), two coordinates \((x_h,y_h)=(a_h,b_h)\) with equation \(x_hy_h=0\). Thus
\[
\widehat{\mathcal O}_{X,\pi(a,b)}\simeq
k[[t_1,\ldots,t_{|A|+|B|-2},(x_h,y_h)_{h\in Z}]]
/(x_hy_h:h\in Z).
\]
Here all residue fields are \(k\), so the finite étale map induces the indicated isomorphism on completed local rings. As \(|A|+|B|=4-r\), each displayed ring has dimension two. For \(r=0,1,2\) these give exactly the three rings in the statement. They are reduced complete intersections, hence Cohen--Macaulay and Gorenstein. Their Hilbert--Samuel multiplicities are respectively \(1\), \(2\), and \(2\cdot2=4\), e.g. from their homogeneous tangent-cone complete intersections.

**4. Singular scheme, not merely its support.** For \(r=0\) the surface is regular. For \(r=1\), the Jacobian singular subscheme in the completed local model \(k[[t,x,y]]/(xy)\) is \((x,y)\), giving a reduced smooth curve. For \(r=2\), consider the complete intersection \((xy,zw)\) in \(k[[x,y,z,w]]\). The two-by-two minors of its Jacobian matrix, together with the defining equations, generate precisely
\[
(xy,xz,xw,yz,yw,zw).
\]
This is the squarefree monomial ideal cutting out the union of four coordinate axes. It follows from these exhaustive geometric-point local computations, and faithful flatness of completion, that the singular scheme is reduced everywhere.

**5. Global counts.** At a generic point of a one-dimensional singular stratum the complement \(Z\) consists of one index, so \((|A|,|B|)=(1,2)\) or \((2,1)\). There are \(4\binom32=12\) ordered support patterns of the first type and another \(12\) of the second type. Each determines one irreducible curve: the singleton norm-one coordinate is \(\pm1\), while the other two support coordinates range over the affine conic \(s^2+t^2=1\). The simultaneous sign action identifies the singleton sign choices, and this conic is isomorphic to \(\mathbb G_m\) over \(k\), since \(k\) is algebraically closed and \(2\) is invertible. Their closures include exactly the appropriate branch points; hence there are 24 irreducible singular curves.

At \(r=2\), the sets \(A,B\) are disjoint singletons. There are \(4\cdot3=12\) ordered choices of support indices; each has four choices of signs for its two nonzero norm-one coordinates, with simultaneous sign reversal identifying pairs. The resulting 24 points are exactly the determinant-one signed double-transposition matrices, as is also visible by the explicit quaternion action. The four coordinate axes in the \(r=2\) Jacobian model give precisely four incident singular curves at each point. No other singular points exist by the preceding local classification.

## Verification
The accompanying exact-arithmetic program `check.py` can be run with `python3 check.py`. It checks all sixteen diagonal coefficients of the quaternion action, invertibility of the Hadamard matrix, all ordered support-pattern counts, and the six squarefree quadratic generators of the exceptional Jacobian ideal. Its success marker is `HSO4_EXACT_CHECK_OK`. The program supplies a reproducible algebraic consistency check; the statements for every algebraically closed field of characteristic different from two follow from the formal-local proof above, not from finite testing.

## Relationship to prior work
Brysiewicz and Gesmundo, *Marvelous slices of orthogonal matrices*, prove the decomposition of the hollow real \(\mathrm{SO}(4)\) slice into fourteen surfaces (eight quadric surfaces and six tori) and identify twenty-four pairwise intersection circles and twelve pairs of opposite signed permutation matrices. Their explicit incidence result provides the geometric motivation and the set-theoretic comparison. It does not supply the quaternion-derived completed local rings or establish that the Jacobian singular scheme itself is reduced. Neither the incidence complex nor degree additivity alone determines the scheme-theoretic transverse contact orders or local multiplicities. The standard spin double cover is used as an established tool rather than claimed as new.

## Limitations
The conclusion is restricted to the zero-diagonal slice of \(\mathrm{SO}(4)\), to algebraically closed fields of characteristic not two, and to the stated local and singular-scheme invariants. It does not determine arbitrary non-hollow slices, global deformation spaces, integral cohomology, or characteristic-two behavior. Earlier quaternionic treatments could contain an equivalent infinitesimal computation not recognized by the focused literature comparison; independent bibliographic review remains advisable.

## References
1. T. Brysiewicz and F. Gesmundo, *Marvelous slices of orthogonal matrices*, arXiv:2602.02668, first publicly posted 2 February 2026; revised version arXiv:2602.02668v2 (14 September 2026), especially Theorem 1.1 and Sections 2--3. https://arxiv.org/abs/2602.02668
2. Standard algebraic-group fact: the central separable isogeny \(\mathrm{Spin}_4\simeq\mathrm{SL}_2\times\mathrm{SL}_2\to\mathrm{SO}_4\) in characteristic different from two; an elementary kernel-and-dimension proof in quaternion coordinates is included above.
