# Numerical intersection and Chern data of a fixed-curve quotient of a diagonal four-quadric Calabi–Yau threefold

## Finding
Let \(Y\subset\mathbf P^7_{\mathbb C}\) be a smooth diagonal complete intersection of four quadrics whose \(4\times8\) coefficient matrix has every maximal minor nonzero. Let \(\iota\) change the signs of exactly two homogeneous coordinates and let \(X=Y/\langle\iota\rangle\). The fixed curve \(C\) is smooth, connected, and has genus \(17\). The quotient has transverse \(A_1\) singularities exactly along the image of \(C\), and the blowup of this singular curve is a smooth crepant resolution \(\pi:Z\to X\).

Write \(D\in\operatorname{Pic}(Z)\) for the pullback of the descended hyperplane bundle and \(E\) for the exceptional divisor. Then \(Z\) is a simply connected Calabi–Yau threefold with
\[
(h^{1,1}(Z),h^{2,1}(Z))=(2,58),\qquad e(Z)=-112,
\]
\[
D^3=8,\quad D^2E=0,\quad DE^2=-32,\quad E^3=-128,
\]
and
\[
c_2(Z)\cdot D=56,\qquad c_2(Z)\cdot E=64.
\]
The divisor classes \(D,E\) span the rational Néron–Severi space. No assertion that they constitute an integral basis is made. The result applies to every coefficient matrix satisfying the maximal-minor hypothesis, not just a particular computational instance.

## Assumptions and scope
Coordinates are \([x_0:\cdots:x_7]\). For \(r=0,1,2,3\), let \(Q_r=\sum_{j=0}^{7}a_{rj}x_j^2\). Assume every four columns of \(A=(a_{rj})\) are linearly independent over \(\mathbb C\). Then \(Y=V(Q_0,Q_1,Q_2,Q_3)\) is smooth of dimension three and degree \(16\): a singular point would have at least four nonzero coordinates (any projective solution has at least five), and the corresponding Jacobian columns would be dependent. Let \(\iota([x_0:x_1:x_2:\dots:x_7])=[-x_0:-x_1:x_2:\dots:x_7]\). The group is order two, acts algebraically, and preserves all quadrics. Quotient and blowup are over \(\mathbb C\). The choice of the two flipped coordinates is immaterial after relabeling.

## Proof
**1. Fixed curve and the local quotient.** A projective point fixed by \(\iota\) lies either in the positive eigenspace \(x_0=x_1=0\) or the negative eigenspace \(x_2=\cdots=x_7=0\). The second has no intersection with \(Y\) because its support contains fewer than four columns of \(A\). Thus the fixed locus is
\[
C=Y\cap\{x_0=x_1=0\}\subset\mathbf P^5,
\]
a smooth complete intersection of four quadrics. Its degree is \(16\), and adjunction gives \(K_C\simeq\mathcal O_C(2)\), whence \(2g(C)-2=32\) and \(g(C)=17\). Smooth complete-intersection connectedness gives one irreducible curve. The two defining hyperplanes meet transversely on \(Y\), so
\[
N_{C/Y}\simeq\mathcal O_C(1)^{\oplus2}.
\]
The involution acts by \(-1\) on the two normal directions and by \(+1\) on tangent directions to \(C\). Hence the quotient is analytically locally \(C\) times \(\mathbb A^2/\{\pm1\}\), equivalently a transverse \(A_1\) surface singularity \(uv=w^2\). Its singular locus is exactly \(C\).

**2. Crepant resolution.** Blow up the smooth curve: \(\beta:\widehat Y=\operatorname{Bl}_C(Y)\to Y\). Its exceptional divisor is \(\widehat E=\mathbf P_C(N_{C/Y})\cong C\times\mathbf P^1\). In a local blowup chart the involution takes \((u,t,z)\mapsto(-u,t,z)\), so \(Z:=\widehat Y/\langle\iota\rangle\) is smooth and is the blowup of \(X\) along its singular curve (using the blowup of the \(A_1\) ideal). Let \(q:\widehat Y\to Z\) be the quotient. Then \(q^*E=2\widehat E\). The quotient singularities are Gorenstein rational double points transversally; the local resolution is crepant, so \(K_Z\simeq\mathcal O_Z\). Since \(Y\) is a Calabi–Yau complete intersection and quotient singularities are rational, \(h^1(Z,\mathcal O_Z)=h^2(Z,\mathcal O_Z)=0\). Lefschetz implies \(\pi_1(Y)=1\), blowup along a smooth complex codimension-two center leaves \(\pi_1\) unchanged, and the quotient of the simply connected \(\widehat Y\) by a finite involution with fixed points has \(\pi_1(Z)=1\) by the fixed-stabilizer quotient theorem.

**3. Cubic intersections.** The hyperplane line bundle \(\mathcal O_Y(1)\) descends to a line bundle on \(X\): the stabilizer acts trivially on its fibers over the positive-eigenspace fixed points. Consequently \(q^*D=\beta^*H\), where \(H=c_1(\mathcal O_Y(1))\). Standard intersection identities for a blowup along a curve give
\[
H^3=16,\quad (\beta^*H)^2\widehat E=0,\quad (\beta^*H)\widehat E^2=-H\cdot C=-16,
\]
\[
\widehat E^3=-\deg c_1(N_{C/Y})=-32.
\]
The degree-two map \(q\), with \(q^*E=2\widehat E\), therefore yields
\[
(D^3,D^2E,DE^2,E^3)=(8,0,-32,-128).
\]
This calculation uses intersection theory on the actual blowup and is independent of any chosen local coordinate trivialization.

**4. Euler characteristic and Hodge numbers.** The Chern class of \(Y\) is \(c(T_Y)=(1+H)^8/(1+2H)^4\). Its degree-three coefficient is \(-8\), so \(e(Y)=-128\). The fixed curve has \(e(C)=2-2\cdot17=-32\). The blowup adds \(e(C)\) to Euler characteristic and \(e(\widehat E)=2e(C)=-64\). The involution fixes the exceptional divisor pointwise; the finite quotient Euler formula gives
\[
e(Z)=\frac{e(\widehat Y)+e(\widehat E)}2=\frac{-160-64}{2}=-112.
\]
Rational cohomology of the finite quotient \(X\) identifies with the invariant part of \(H^*(Y,\mathbb Q)\), so \(b_2(X)=1\) by the Lefschetz theorem. The connected exceptional ruled surface contributes one degree-two class, hence \(b_2(Z)=2\). Since \(h^{2,0}(Z)=0\), \(h^{1,1}(Z)=2\). For a Calabi–Yau threefold \(e=2(h^{1,1}-h^{2,1})\), giving \(h^{2,1}=58\).

**5. Chern pairings.** By adjunction for the smooth exceptional surface, \(c_1(Z)=0\) implies \(c_2(Z)\cdot E=e(E)-E^3=-64+128=64\). The divisor \(D\) is nef and big as a pullback of an ample divisor on \(X\). Kawamata–Viehweg vanishing yields \(H^i(Z,\mathcal O_Z(D))=0\) for \(i>0\). Invariant linear forms on \(Y\) are exactly the six nonflipped coordinates, so \(h^0(Z,\mathcal O_Z(D))=6\). Hirzebruch–Riemann–Roch on the Calabi–Yau threefold gives
\[
6=\chi(Z,\mathcal O_Z(D))=\frac{D^3}{6}+\frac{c_2(Z)\cdot D}{12},
\]
therefore \(c_2(Z)\cdot D=56\).

## Verification
The accompanying standalone `verify_fixed_fermats.py` evaluates the exact Chern-coefficient and finite-orbit formulas for \(3\le t\le8\), checks Vandermonde maximal-minor examples, and independently checks the stated genus, Euler, cubic-intersection, Hodge, and Chern arithmetic. It returned `VERIFY_OK CY3 Hodge=(2,58) cubic=(8,0,-32,-128) c2=(56,64) pi1=needs_proof`. The script's final phrase means that fundamental-group triviality is supplied by the topological proof rather than computation. Finite examples do not prove the universal statement; the proof above does.

## Relationship to prior work
The geometric motivation is the generalized-Fermat Calabi–Yau quotient research publicly described in Alessandra Sarti's September 19, 2025 CAGE Leiden talk. Hidalgo–Hughes–Leyton-Álvarez introduced the generalized Fermat models and their diagonal symmetry action. Billi–Palomino–Sarti's publicly accessible October 15, 2026 manuscript treats fixed-point-free automorphisms and explicitly identifies allowing fixed points as a separate direction; its free-quotient results do not imply this fixed-curve crepant-resolution package. Classical Humbert–Edge literature already identifies the genus-17 curve as a four-quadric complete intersection, and other families of Calabi–Yau threefolds with the Hodge pair \((2,58)\) were known. Neither fact is claimed as new. The contribution evaluated here is the *specific crepant quotient construction together with its exact cubic form and second-Chern linear form*.

## Limitations
This is not a uniqueness claim, an independent priority certification, or a computation of the integral Picard lattice. In particular the two displayed divisor classes span \(N^1(Z)_\mathbb Q\), but they need not generate the full integral Picard group. The known occurrence of the same Hodge pair in other constructions does not establish deformation equivalence. The numerical invariants are insensitive to possible special changes in the coefficient moduli, and no claim is made about the variation of complex structures or mirror symmetry. The 2025 conference abstract is a verified dated public introduction of the research direction, but it is not a full paper; whether unrecorded 2025 talk material contained closely related numerical calculations remains an irreducible priority risk.

## References
1. A. Sarti, *Log Enriques varieties from Hyperkähler and Calabi-Yau manifolds*, CAGE at Leiden 2025 conference talk, September 19, 2025; official schedule: https://sites.google.com/view/cage-at-leiden/home/schedule and abstract: https://sites.google.com/view/cage-at-leiden/home.
2. R. Hidalgo, P. Hughes, A. Leyton-Álvarez, *Automorphisms of Generalized Fermat manifolds*, arXiv:2010.04628, https://arxiv.org/html/2010.04628v8.
3. S. Billi, A. J. Palomino, A. Sarti, *Quotients of Calabi–Yau Generalized Fermat manifolds and Log Enriques varieties*, arXiv:2610.21752v1, first arXiv posting October 15, 2026; https://arxiv.org/html/2610.21752v1 (supporting later full text, not used as the origin date).
4. *Geometric aspects on Humbert-Edge curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, Glasgow Mathematical Journal, Section 3.1, https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/geometric-aspects-on-humbertedge-curves-of-type-5-kummer-surfaces-and-hyperelliptic-curves-of-genus-2/23885CE33950EFB14ABC6A5C3AAE03AE.
5. M. Ghirlanda, *Calabi-Yau complete intersections in fake weighted projective spaces*, arXiv:2602.13057 (known occurrence of the Hodge pair; does not state the present cubic and Chern package).
6. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301.
