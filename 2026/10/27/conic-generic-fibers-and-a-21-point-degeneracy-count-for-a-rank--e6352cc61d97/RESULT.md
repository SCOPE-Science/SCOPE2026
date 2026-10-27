# Conic generic fibers and a 21-point degeneracy count for a rank-nine uniform bundle

## Finding
Let \(E\) be the specific globally generated rank-nine bundle on \(\mathbb P^5_\mathbb C\) constructed in Theorem 3.3 of Denham--Miró-Roig--Schenck [1]. Write \(X=\mathbb P_{\mathbb P^5}(E)\) for the projectivization **of one-dimensional quotients**, \(H\) for the pullback of the base hyperplane class, and \(\xi=c_1(\mathcal O_X(1))\). The supplied fourteen generating sections induce \(f:X\to\mathbb P^{13}\).

The smooth thirteenfold \(X\) is Fano of Picard rank two with \(-K_X=9\xi+H\). Its tautological divisor is nef but not big: \(\int_X\xi^{13}=0\), although \(\int_X\xi^{12}H=8\). In particular the image \(W=f(X)\) is an integral hypersurface. Every connected component of a general geometric fiber of \(f\) is a smooth rational curve of \(H\)-degree exactly two. If \(\delta=\deg W\) and \(r\) is the number of such components in the general geometric fiber, then \(\delta r=4\). Furthermore, the rank-drop locus of five general linear combinations of the fourteen chosen generators of \(E\) is exactly **21 distinct reduced points** on the base \(\mathbb P^5\).

## Assumptions and scope
The ground field is \(\mathbb C\). The bundle is the *specific* rank-nine quotient bundle in the exact sequences of [1, Theorem 3.3], not an arbitrary uniform bundle with the same splitting type:
\[
0\to E\to\mathcal O_{\mathbb P^5}(1)^{14}\to\Omega^1_{\mathbb P^5}(3)\to0,
\qquad \mathcal O_{\mathbb P^5}^{14}\twoheadrightarrow E.
\]
The chosen fourteen sections are the displayed surjection. General means belonging to a nonempty Zariski-open subset of \(\operatorname{Gr}(5,14)\). No assertion is made that general fibers of \(f\) are connected, that the hypersurface \(W\) is normal, or that the contracted rational curves embed as smooth conics in the base.

## Proof
**Chern polynomial.** The Euler sequence for \(\Omega^1_{\mathbb P^5}(3)\) gives \(c_t(\Omega^1(3))=(1+2t)^6/(1+3t)\), where \(t\) is the hyperplane variable. Hence
\[
c_t(E)=\frac{(1+t)^{14}(1+3t)}{(1+2t)^6}
=1+5t+13t^2+21t^3+21t^4+21t^5\pmod{t^6}.
\]
For quotient projectivization, the projective bundle pushforward identity is \(\pi_*(\xi^{8+i})=s_i(E^\vee)\), where \(s_t(E^\vee)=1/c_t(E^\vee)\). Therefore
\[
\frac1{c_t(E^\vee)}=\frac{(1-2t)^6}{(1-t)^{14}(1-3t)}=1+5t+12t^2+16t^3+8t^4+0t^5\pmod{t^6}.
\]
It follows that \(\xi^{13}\) has zero top intersection and \(\int_X\xi^{12}H=8\). Since \(E\) is globally generated, \(\xi\) is nef and basepoint-free. For a basepoint-free line bundle, its image dimension is its numerical dimension, namely the largest power having nonzero intersection with an ample divisor; thus \(\dim W=12\), so \(W\subset\mathbb P^{13}\) is a hypersurface.

**Fano property.** The relative canonical bundle formula for rank nine gives \(K_X=-9\xi+\pi^*(K_{\mathbb P^5}+c_1(E))=-9\xi-H\). Since \(\xi\) is relatively ample and globally nef, and \(H\) is the pullback of an ample class, \(9\xi+H\) is ample by the relative ampleness criterion. Thus \(X\) is a smooth Fano thirteenfold. The projective bundle Picard formula gives Picard rank two.

**General contracted curves.** Choose a dense open subset of the smooth locus of \(W\) on which \(f\) is smooth with one-dimensional geometric fibers (generic smoothness in characteristic zero). Each connected component \(C\) of such a fiber is a smooth projective connected curve. Since \(f\) is given by \(\xi\), \(\xi\cdot C=0\). Since \(\pi\) has fibers \(\mathbb P^8\) on which \(\xi\) is ample, \(C\) cannot be contained in a single fiber of \(\pi\); hence \(H\cdot C>0\). The relative dualizing bundle of the smooth morphism over the smooth base restricts to \(K_C=K_X|_C\); therefore \(2g(C)-2=-(H\cdot C)<0\). Consequently \(g(C)=0\) and \(H\cdot C=2\). For a general linear slice of twelve hyperplanes in \(\mathbb P^{13}\), the projection formula yields \(\int_X\xi^{12}H=\delta\cdot r\cdot2=8\), proving \(\delta r=4\).

**Twenty-one reduced rank-drop points.** A five-plane \(U\subset\mathbb C^{14}\) of generator combinations gives \(U\otimes\mathcal O_{\mathbb P^5}\to E\). The locus of rank at most four has Thom--Porteous expected codimension \((5-4)(9-4)=5\) and class \(c_5(E)=21H^5\). The original surjection \(\mathcal O^{14}\twoheadrightarrow E\) defines \(\mathbb P^5\to\operatorname{Gr}(9,14)\), and varying \(U\) translates the corresponding Schubert cycle under the transitive \(\operatorname{GL}_{14}\)-action. Kleiman transversality in characteristic zero makes the expected codimension-five intersection reduced and transverse for general \(U\). The rank-at-most-three locus has expected codimension \((5-3)(9-3)=12>5\) and is absent. Thus the computed degree is exactly the number of distinct points, \(21\).

## Verification
The accompanying `verify.py` computes both degree-five truncations over the integers by explicit truncated power-series operations and checks the coefficients, top Segre vanishing, the coefficient \(8\), the top Chern number \(21\), and the canonical divisor coefficients. The program is a finite algebraic identity checker; the geometric conclusions additionally use projective-bundle pushforward, generic smoothness, adjunction, and Kleiman transversality.

## Relationship to prior work
Denham--Miró-Roig--Schenck [1] establish the construction, exact sequences, global generation and nonhomogeneity; their Theorem 3.3 and surrounding discussion do not state the geometry of this induced projective-bundle contraction or the 21-point count. Landsberg--Manivel [2, Section 6.2] construct a related homogeneous constant-rank matrix bundle with the same Chern classes; their section explains its bundle structure but does not give the present numerical contraction and degeneracy package. The tautological projective-bundle, Thom--Porteous and generic smoothness tools are standard, so this is a new *specialized computation and geometric interpretation*, not a new general theorem about uniform bundles.

## Limitations
The exact degree of the image hypersurface is not determined; its possible degree and generic fiber component count satisfy \(\delta r=4\). The calculation does not classify special fibers or establish whether general fibers are connected. The enumerative claim concerns general five-dimensional spaces of the fourteen specified generators. Historical priority of implicit deductions from earlier descriptions has not been independently settled.

## References
[1] G. Denham, R. M. Miró-Roig, H. Schenck, *Uniform non-homogeneous vector bundles: A counterexample to the conjecture of Drézet and Ballico-Ellia*, arXiv:2610.20208v1, 2026, https://arxiv.org/html/2610.20208v1 (Theorem 3.3 and Remarks 3.4--3.5).

[2] J. M. Landsberg, L. Manivel, *Equivariant spaces of matrices of constant rank*, arXiv:2212.04228v1, 2022, https://arxiv.org/pdf/2212.04228 (Section 6.2).

[3] W. Fulton, *Intersection Theory*, second edition, Springer, 1998 (degeneracy loci and Thom--Porteous).
