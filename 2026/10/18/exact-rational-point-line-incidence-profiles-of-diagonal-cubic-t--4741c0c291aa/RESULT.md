# Exact rational point-line incidence profiles of diagonal cubic threefolds over \(\mathbf F_7\)

## Finding
Let \(\mathbf a=(a_0,\ldots,a_4)\in(\mathbf F_7^\times)^5\), and let
\[
X_{\mathbf a}=\left\{[x_0:\cdots:x_4]\in\mathbf P^4_{\mathbf F_7}:\sum_{i=0}^{4}a_ix_i^3=0\right\}.
\]
Every such hypersurface is smooth. There are **exactly seven** projective equivalence classes under \(\operatorname{PGL}_5(\mathbf F_7)\), and the **complete rational point-line incidence profile** for every class is as follows. Write \(m_j\) for the number of rational points of \(X_{\mathbf a}\) lying on exactly \(j\) distinct rational projective lines contained in \(X_{\mathbf a}\). Only nonzero \(m_j\) are shown.

| Coefficient tuple \(\mathbf a\) | Rational points | Rational lines | Complete nonzero point-degree multiplicities |
|:--|--:|--:|:--|
| \((1,1,1,1,1)\) | 435 | 135 | \(m_2=405,\ m_9=30\) |
| \((1,1,1,1,2)\) | 477 | 189 | \(m_2=81,\ m_3=378,\ m_{12}=18\) |
| \((1,1,1,1,3)\) | 288 | 27 | \(m_0=189,\ m_2=81,\ m_3=18\) |
| \((1,1,1,2,2)\) | 309 | 27 | \(m_0=135,\ m_1=162,\ m_3=9,\ m_9=3\) |
| \((1,1,1,2,3)\) | 414 | 81 | \(m_0=135,\ m_2=243,\ m_3=27,\ m_9=9\) |
| \((1,1,1,3,3)\) | 498 | 270 | \(m_3=27,\ m_4=405,\ m_6=54,\ m_9=3,\ m_{12}=9\) |
| \((1,1,2,2,3)\) | 393 | 36 | \(m_0=162,\ m_1=216,\ m_3=12,\ m_{12}=3\) |

Here a rational line is an \(\mathbf F_7\)-defined line and \(F_1(X)(\mathbf F_7)\) parametrizes those lines. **Exactly three** classes, with representatives \((1,1,1,1,1)\), \((1,1,1,1,2)\), and \((1,1,1,3,3)\), have *every rational point lying on a rational line*. The remaining four have, in table order, exactly \(189,135,135,162\) uncovered rational points. The possible rational-line totals are \(27,36,81,135,189,270\), so every smooth diagonal member contains a rational line and the sharp class-specific bounds are \(27\) and \(270\). In particular the two inequivalent \(27\)-line classes have different point-line profiles: a line total does not determine the incidence geometry.

## Assumptions and scope
All statements concern cubics of the displayed diagonal form with **every coefficient nonzero**, over the exact ground field \(\mathbf F_7\). A rational line means an \(\mathbf F_7\)-defined projective line; its geometric points need not all be rational. Equivalence is induced by a projective linear coordinate transformation **defined over \(\mathbf F_7\)**. We do not classify arbitrary cubic threefolds, nor do we claim a classification under unrestricted abstract isomorphism.

## Proof
**Smoothness and classification.** Since the characteristic is \(7\), the partial derivatives are \(3a_ix_i^2\), so they cannot vanish simultaneously at a projective point when all \(a_i\ne0\). The Hessian matrix is \(\operatorname{diag}(6a_0x_0,\ldots,6a_4x_4)\), and therefore its determinant is a nonzero multiple of \(x_0x_1x_2x_3x_4\). Any projective linear equivalence between two such cubics carries one Hessian determinant into a scalar multiple of the other; hence it permutes the five coordinate hyperplanes. It must therefore be monomial (a permutation times a nonzero diagonal matrix).

Nonzero cubes in \(\mathbf F_7\) are exactly \(\{1,6\}\). Thus independent coordinate rescalings reduce the five coefficients to three cube classes, represented by \(1,2,3\). Common multiplication of the equation by a nonzero scalar cyclically shifts these three classes, while permutation of variables acts by permutation. There are \(\binom{7}{2}=21\) multisets of five classes, and no such multiset is fixed by a three-cycle because its size is five. Consequently there are \(21/3=7\) distinct orbits. The seven listed representatives have different orbits, so they exhaust the projective-equivalence classes.

**Complete rational line and incidence census.** Every two-dimensional vector subspace of \(\mathbf F_7^5\) has a unique reduced-row-echelon basis \((u,v)\) with pivot columns \(0\le i<j\le4\). Writing a point of its projective line as \([su+tv]\), restriction of the defining cubic gives
\[
\sum_{k=0}^4 a_k(su_k+tv_k)^3.
\]
It vanishes identically if and only if the following **four** equations hold in \(\mathbf F_7\):
\[
\sum_k a_ku_k^3=0,\quad
\sum_k a_ku_k^2v_k=0,\quad
\sum_k a_ku_kv_k^2=0,\quad
\sum_k a_kv_k^3=0.
\]
Here the factors of \(3\) in the mixed binomial coefficients are invertible. In echelon form we set \(u_i=v_j=1\) and \(u_j=v_i=0\), with all other entries in each row before its pivot zero. The free entries are exactly \(u_k\) for \(k>i, k\ne j\) and \(v_k\) for \(k>j\). Exhausting these finite possibilities visits each rational projective line **once**, for a total of
\[
\left[\begin{matrix}5\\2\end{matrix}\right]_7
=\frac{(7^5-1)(7^4-1)}{(7^2-1)(7-1)}=140050.
\]
The exact enumerator in `verify_lines.py` tests the four equations for all \(140050\) lines and each of the seven forms. For each accepted line it normalizes the eight projective points \([u+tv]\) for \(t\in\mathbf F_7\) and \([v]\); it increments the incidence degree of every one of those points. This yields **all entries of the \(m_j\) table**, not just the line totals. This is an exhaustive finite proof, not an extrapolation from random samples.

**Independent local polar count.** Every rational point of \(\mathbf P^4\) has a unique normalization with its first nonzero coordinate equal to \(1\), yielding \(2801\) normalized rational points. For distinct points \(P,Q\) of \(X_{\mathbf a}(\mathbf F_7)\), their joining line lies on the cubic exactly when its two mixed cubic coefficients vanish:
\[
\sum_k a_k P_k^2 Q_k=0,\qquad \sum_k a_k P_k Q_k^2=0.
\]
Fix \(P\). Each rational line through \(P\) contributes **exactly seven** choices for the other rational point \(Q\), and distinct such lines have no other common rational points. Therefore the number of \(Q\ne P\) satisfying both equations, divided by \(7\), is exactly the incidence degree at \(P\). A **separately implemented point-pair enumeration** computes this number for every rational point and independently reproduces every \(m_j\). It also recovers the line totals, since a rational line supplies \(8\cdot7=56\) *directed* ordered pairs of distinct points. The resulting global pair counts before removing orientations are \(7560,10584,1512,1512,4536,15120,2016\), respectively.

As a check independent of the enumerators' internal representation, each row satisfies the two finite-incidence identities \(\sum_j m_j=\#X_{\mathbf a}(\mathbf F_7)\) and \(\sum_j j m_j=8\#F_1(X_{\mathbf a})(\mathbf F_7)\). These identities hold exactly for every row.

## Verification
From the directory containing `verify_lines.py`, run `python3 verify_lines.py` with Python 3 and no external modules. The program asserts the coefficient-orbit classification, the total Grassmannian line count \(140050\), the direct four-equation line census, and the independently determined **local point-incidence multiplicities** from the polar conditions on point pairs. It prints the seven point-line profiles, asserts both incidence identities per row, and reports `PASS`. Both enumeration methods were executed successfully on the embedded code. No probabilistic test or floating-point calculation enters the result.

## Relationship to prior work
De Frutos Fernández, Garai, Isham, Murayama, and Smith [1] investigate rational linear spaces over finite fields. In Section 3, Tables 1–2, they give random-sample distributions for cubic threefolds over \(\mathbf F_7\), and explicitly leave the universal existence of rational lines for smooth cubics over this field unsettled. Their experiments do not enumerate the diagonal subfamily or determine how its rational lines cover its rational points.

Debarre, Laface, and Roulleau [2] prove a general identity expressing counts of lines through rational point counts over a field and its quadratic extension (their equation (8)), and describe the zeta function of the **untwisted Fermat cubic** and its Fano surface in Section 4.5.1. The Fermat row is therefore closely related to known calculations; their general point-count identity alone does **not determine the distribution of rational lines through individual rational points**. Nor does the Fermat computation enumerate these six twisted-family incidence profiles. Roulleau [3] studies the geometric Fano surface of the Fermat cubic; its complex-geometric configurations do not directly determine the rational point-line incidence distributions for all finite-field twists. The present result classifies the entire rational incidence profile in this natural seven-class family, rather than merely specializing a formula for total point counts.

## Limitations
The incidence tables and the bound \(27\) concern **only** nondegenerate diagonal cubic threefolds over \(\mathbf F_7\). It does not resolve the question whether *every* smooth cubic threefold over \(\mathbf F_7\) contains a rational line. Finite exhaustive enumeration over \(\mathbf F_7\) does not imply a theorem over other fields, over their algebraic closures, or about abstract (non-projective) equivalences. Existing Jacobi-sum methods for twisted Fermat varieties might offer more conceptual derivations of these finite counts; a fully comprehensive bibliography cannot be guaranteed.

## References
[1] M. I. de Frutos Fernández, S. Garai, K. Isham, T. Murayama, G. Smith, *Rational linear subspaces of hypersurfaces over finite fields*, arXiv:2111.10976 (first public version, 2021-11-22), Section 3 and Tables 1–2. https://arxiv.org/abs/2111.10976

[2] O. Debarre, A. Laface, X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, especially Sections 2.3, 4.5.1 and equation (8). https://www.math.ens.psl.eu/~debarre/58.pdf

[3] X. Roulleau, *The Fano surface of the Fermat cubic threefold, the del Pezzo surface of degree 5 and a ball quotient*, arXiv:1001.5111. https://arxiv.org/abs/1001.5111
