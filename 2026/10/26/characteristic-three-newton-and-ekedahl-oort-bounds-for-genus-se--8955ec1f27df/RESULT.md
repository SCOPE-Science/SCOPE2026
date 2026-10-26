# Characteristic-three Newton and Ekedahl–Oort bounds for genus-seventeen generalized Fermat curves

## Finding
Let \(k\) be algebraically closed of characteristic \(3\), and let \(B\subset\mathbb P^1(k)\) be six distinct points. The maximal elementary abelian double cover \(C_B\to\mathbb P^1\) branched precisely at \(B\) is a smooth generalized Fermat curve of type \((2,5)\) and genus \(17\). Define \(h(B)\) as the number of four-element subsets of \(B\) with harmonic cross-ratio. Define \(H_B\) as the genus-two double cover branched at all six points, and write \(r(B)\) for its Jacobian's \(3\)-rank.

**Theorem.** Exactly the following six pairs \((h(B),r(B))\) occur:
\[
(0,0),\ (0,1),\ (0,2),\ (1,2),\ (2,2),\ (3,2).
\]
The Jacobian of \(C_B\) has \(3\)-rank
\[
f_3(J(C_B))=15-h(B)+r(B),
\]
so **its complete rank spectrum is \(\{14,15,16,17\}\)**. Its \(a\)-number is
\[
a(J(C_B))=h(B)+\mathbf1_{r(B)<2}.
\]
Thus rank \(15\) occurs with either \(a=1\) or \(a=2\). All six profiles occur over finite extensions of \(\mathbb F_3\).

The Newton slopes, listed with multiplicity, are
\[
0^{\times f_3},\quad (1/2)^{\times (34-2f_3)},\quad 1^{\times f_3}.
\]
The formula for slopes in this case follows from the elliptic/genus-two factorization and the fact that any genus-two Jacobian of \(3\)-rank zero is supersingular.

## Assumptions and scope
Only algebraically closed fields of characteristic \(3\), and *six pairwise distinct branch points*, are considered. In normalized affine coordinates
\[
B=\{\infty,0,1,a,b,c\},\quad a,b,c\notin\{0,1\},\quad a,b,c\text{ distinct},
\]
the curve can be defined as the smooth projective normalization of
\[
k(x)\bigl(\sqrt{x},\sqrt{x-1},\sqrt{x-a},\sqrt{x-b},\sqrt{x-c}\bigr).
\]
The sixth branch point is at infinity. The field extension has degree \(32\), Galois group \((\mathbb Z/2)^5\), and inertia index two at each of six branch points. Riemann–Hurwitz gives
\[
2g-2=32(-2)+6\cdot16=32,
\]
so \(g=17\). A four-subset is *harmonic* when any ordering has cross-ratio \(-1\); in characteristic three all six cross-ratio transforms of \(-1\) equal \(-1\). Its elliptic double cover is supersingular precisely when the quadruple is harmonic.

## Proof
**1. Tame character decomposition.** Every nontrivial character of the deck group corresponds to a nonempty even subset \(S\subset B\). The associated quadratic quotient is branched at the points in \(S\), so it has genus \((|S|-2)/2\) for \(|S|\ge2\). The \(15\) subsets of size four yield elliptic curves \(E_S\); the unique six-subset yields the genus-two curve \(H_B\). The subsets of size two yield genus-zero curves. Orthogonal character idempotents in the group algebra have denominators dividing \(32\), which is invertible in characteristic three. Pullback/norm maps therefore give an isogeny whose kernel is killed by a power of two:
\[
J(C_B)\sim_{2\text{-power}}\Bigl(\prod_{|S|=4}E_S\Bigr)\times J(H_B).
\]
In particular, this isogeny identifies \(3\)-divisible groups and preserves the Newton polygon, \(3\)-rank and \(a\)-number.

**2. Harmonic quadruples.** An elliptic double cover of four points has vanishing Hasse invariant in characteristic three precisely when the cross-ratio equals \(-1\). For any three distinct base points, there is exactly one point completing them to a harmonic quadruple. Thus two distinct harmonic four-subsets of the six-point set cannot share three points. Their complements are two-subsets of \(B\), and these complementary pairs must be disjoint. At most three disjoint pairs exist: \(0\le h(B)\le3\).

**3. New genus-two compatibility.** Suppose \(h(B)>0\). Move one harmonic quadruple by a projective transformation to \(\{\infty,0,1,-1\}\); denote the other points by \(u,v\), with \(u,v\notin\{0,1,-1\}\) and \(u\ne v\). A model of the genus-two quotient is
\[
H_B:\ y^2=(x^3-x)(x-u)(x-v).
\]
Writing \(s=u+v\) and \(p=uv\), its monic quintic is \(x^5-sx^4+(p-1)x^3+sx^2-px\). In the basis \(dx/y,x\,dx/y\), a Cartier–Manin matrix, or its transpose for the dual Hasse–Witt convention, is
\[
M=\begin{pmatrix}s&-p\\1&-s\end{pmatrix},\qquad
\det M=p-s^2=-(u-v)^2\ne0.
\]
Thus the genus-two quotient is ordinary: \(r(B)=2\) whenever \(h(B)\ge1\). This rules out all other \((h,r)\) pairs.

**4. Rank and \(a\)-number.** Each harmonic elliptic factor has \(3\)-rank zero and \(a\)-number one; each other elliptic factor is ordinary. The displayed prime-to-three isogeny gives \(f_3=15-h+r\). For a monic squarefree quintic \(f(x)=\sum_{j=0}^{5}c_jx^j\), with its branch point at infinity, a Cartier–Manin matrix of \(y^2=f(x)\) in characteristic three is
\[
M_f=\begin{pmatrix}c_2&c_1\\c_5&c_4\end{pmatrix},\qquad c_5=1.
\]
The supersingularity criterion uses \(M_fM_f^{(3)}=0\), as in Howe (2006), where \(M_f^{(3)}\) is entrywise cubing. Its rank is at least one, hence \(a(J(H_B))\le1\). For genus-two curves \(a=0\) exactly when the \(3\)-rank is two; therefore \(a(J(H_B))=\mathbf1_{r<2}\). In dimension two, when \(r=0\) all Newton slopes are \(1/2\), while when \(r=1\) the remaining two slopes are \(1/2\). This proves the Newton and \(a\)-number formulas.

**5. Attainment of every profile.** Let \(\alpha\in\mathbb F_{27}\) satisfy \(\alpha^3-\alpha-1=0\), and encode \(z_0+z_1\alpha+z_2\alpha^2\) as \(z_0+3z_1+9z_2\), with digits \(z_i\in\{0,1,2\}\). For normalized \(B=\{\infty,0,1,a,b,c\}\), the exact triples

| \((h,r)\) | \((a,b,c)\) in \(\mathbb F_{27}\) encoding | Resulting \(3\)-rank | \(a\)-number |
|---|---|---|---|
| \((0,0)\) | \((3,19,25)\) | \(15\) | \(1\) |
| \((0,1)\) | \((3,7,14)\) | \(16\) | \(1\) |
| \((0,2)\) | \((3,4,9)\) | \(17\) | \(0\) |
| \((1,2)\) | \((2,3,4)\) | \(16\) | \(1\) |
| \((2,2)\) | \((2,3,6)\) | \(15\) | \(2\) |

are verified by field arithmetic and Cartier matrices. For \((h,r)=(3,2)\), take \(\beta^2+1=0\) in \(\mathbb F_9\), with digit encoding \(z_0+3z_1\) for \(z_0+z_1\beta\), and choose \((a,b,c)=(2,3,6)\). The corresponding rank is \(14\) and \(a\)-number is \(3\). These six explicit witnesses prove every listed possibility occurs. The code in `verify.py` reproduces their profiles.

## Verification
Run `python3 verify.py` using only the Python standard library. It performs independent exact arithmetic in \(\mathbb F_9\) and \(\mathbb F_{27}\), computes harmonic quadruples and the genus-two Cartier–Manin matrices, and asserts the six witness profiles. It additionally enumerates every \(\binom{7}{3}=35\) normalized branch triple over \(\mathbb F_9\) and every \(\binom{25}{3}=2300\) normalized branch triple over \(\mathbb F_{27}\). The output ends in `VERIFY_OK`. The finite enumerations establish existence and check bounded samples; the isogeny, compatibility lemma and universal rank bound have algebraic proofs above.

## Relationship to prior work
Carvacho, Hidalgo and Quispe (2015), Section 5.3 and Theorem 5.3, give the genus-seventeen complex Jacobian decomposition into fifteen elliptic quotients and one genus-two quotient; their work is the starting point, not a new claim. Hidalgo and collaborators (2014) describe generalized Fermat curves in arbitrary characteristic prime to the covering degree. Yamauchi (2008) constructs special number-field families with split Jacobians. The new assertion here is the **characteristic-three interaction** between harmonic four-subsets and the ordinarity of the residual genus-two quotient, producing the exhaustive six-profile \(3\)-rank and \(a\)-number classification for the entire three-parameter family. Neither the source decomposition nor general Cartier theory is claimed as new.

## Limitations
This theorem concerns the stated type \((2,5)\) family in characteristic three, not all genus-seventeen curves. The prime-to-three isogeny does not assert preservation of integral polarizations. The statements do not count geometric isomorphism classes of curves, nor classify the individual isomorphism types of all elliptic quotient factors. The six-profile theorem and explicit examples are reviewed here, but independent scientific validation has not occurred. An equivalent earlier formulation in specialized generalized-Fermat or finite-characteristic literature may exist, particularly because the complex decomposition is established.

## References
- M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1 (first publicly posted 2015-07-10), Section 5.3, Theorem 5.3. https://arxiv.org/abs/1507.02903
- R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez, P. Paramantzoglou, *Automorphisms of generalized Fermat curves*, arXiv:1409.3063 (2014). https://arxiv.org/abs/1409.3063
- T. Yamauchi, *On Curves with Split Jacobians*, Communications in Algebra 36 (2008), 1419–1425, doi:10.1080/00927870701866622.
- D. Harvey, A. V. Sutherland, *Computing Hasse–Witt matrices of hyperelliptic curves in average polynomial time*, arXiv:1402.3246 (2014), for standard Hasse–Witt computational context.
- E. W. Howe, *Supersingular genus-two curves over fields of characteristic three*, arXiv:math/0604413v1 (2006), Section 2, especially the exact criterion for \(MM^{(3)}=0\). https://arxiv.org/abs/math/0604413
- G. Martínez-Núñez, *Decomposition of Jacobians of generalized Fermat curves*, arXiv:2303.18056 (2023), for later work over complex numbers on decomposition of generalized Fermat Jacobians.
