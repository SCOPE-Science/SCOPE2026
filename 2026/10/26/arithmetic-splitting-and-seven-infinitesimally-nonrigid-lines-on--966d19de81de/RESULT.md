# Arithmetic splitting and seven infinitesimally nonrigid lines on a characteristic-three quartic

## Finding
Let \(X\subset\mathbf P^3_{\mathbf F_3}\) be the quartic
\[
\Psi(x_0,x_1,x_2,x_3)=\Psi(-x_1,x_0,-x_3,x_2),\qquad
\Psi(w,x,y,z)=wz(w^2+wx+x^2+y^2+yz+z^2).
\]
This is the singular characteristic-three quartic model of the Shimada–Shioda 56-line surface described in Veniani's Example 5.4. Its **48 distinct geometric lines** (geometric cardinality established in that example and re-enumerated over \(\mathbf F_9\) here) split into exactly six \(\mathbf F_3\)-rational lines and 21 conjugate pairs, with no larger Frobenius orbit. Consequently, the reduced Hilbert scheme of lines is finite étale over \(\mathbf F_3\) and
\[
\operatorname{Hilb}^{\mathrm{line}}(X)_{\mathrm{red}}
\cong \operatorname{Spec}(\mathbf F_3)^{\sqcup 6}
\sqcup \operatorname{Spec}(\mathbf F_9)^{\sqcup 21}.
\]
The **unreduced** Hilbert scheme has exactly seven nonreduced geometric support points: at each its Zariski tangent space has dimension one. All other 41 points have zero-dimensional tangent space and are reduced. The seven exceptional points consist of one rational point and three conjugate pairs. The associated reduced-scheme line counts and zeta function are
\[
N_n=\begin{cases}6,& n\text{ odd},\\48,&n\text{ even},\end{cases}\qquad
Z_{\mathrm{red}}(T)=\frac{1}{(1-T)^6(1-T^2)^{21}}
\quad(n\ge1).
\]

## Assumptions and scope
The base is precisely \(\mathbf F_3\), and \(X\) is the possibly singular quartic defined above (not the smooth characteristic-three Fermat model arising from the other prime above three in a cyclotomic model). The projective line Hilbert scheme is the closed incidence subscheme of \(\mathrm{Gr}(2,4)\), defined by vanishing of the five coefficients of the quartic restricted to a universal line. Statements about cardinalities count distinct geometric lines; infinitesimal lengths at nonreduced points are not asserted. The zeta function is that of the *reduced* line scheme, not of the entire quartic surface.

## Proof
Work in \(K=\mathbf F_9=\mathbf F_3[\theta]/(\theta^2+1)\). Every \(K\)-line has a unique reduced-row-echelon basis \((u,v)\) for a two-plane in \(K^4\). For pivot columns \(0\le i<j\le3\), set the pivots to one, their other entries in pivot columns to zero, and enumerate every nonpivot free entry. The total number of bases tested is
\[
9^4+9^3+2\cdot9^2+9+1=7462.
\]
Insert \(x=su+tv\) in the displayed quartic and test that all five coefficients of \(s^{4-k}t^k\), for \(0\le k\le4\), vanish. Exact finite-field arithmetic gives 48 satisfying RREF matrices, partitioned by pivot charts as follows: \((0,1):33\), \((0,2):11\), \((0,3):0\), \((1,2):2\), \((1,3):1\), \((2,3):1\). Veniani's independently reported *geometric* cardinality is 48 for the same surface. Since these 48 \(K\)-lines are distinct, this saturates the geometric list: there are no further lines over the algebraic closure. In particular, the line Hilbert scheme has finite, hence zero-dimensional, geometric support.

The cube-power Frobenius applies to every matrix entry and is followed by unique RREF normalization. Exact enumeration returns six fixed matrices and 42 nonfixed matrices paired under Frobenius. Because \(K/\mathbf F_3\) has degree two, every nonfixed orbit has length two. A direct enumeration over \(\mathbf F_3\) also returns six lines. The stated reduced-scheme decomposition follows because a reduced zero-dimensional scheme over a perfect finite field is étale. Its counts for all extensions and zeta function follow by the closed-point Euler product.

For the full line Hilbert scheme, use the same six affine RREF Grassmann charts. In each chart, its local equations are the five polynomial coefficients of the restricted quartic. At each of the 48 solutions, differentiate these five equations with respect to *all* free RREF coordinates. The exact Jacobian rank is one below the chart dimension at four of the 33 solutions on chart \((0,1)\) and three of the 11 on chart \((0,2)\); at all other 41 solutions the rank equals the chart dimension. The two special charts respectively have ambient dimensions four and three, and all seven exceptional points therefore have tangent dimension one. Each point is a point of a zero-dimensional scheme; nonzero tangent dimension is equivalent to a nonreduced local Artin ring. Conversely, zero tangent dimension means the maximal ideal is zero by Nakayama's lemma, hence the point is reduced. Applying Frobenius to these seven points gives one fixed point and three orbits of length two.

## Verification
Run `python verify_fano.py` with `fano48.py` in the same directory (Python 3 standard library only). The checker independently verifies multiplication distributivity in \(K\), all 7,462 distinct RREF matrices, the 48 vanishing restrictions, the six rational lines, the complete Frobenius permutations, and the Jacobian ranks of the five defining equations on all 48 local charts, including the seven nonreduced points. The dual-number coefficient method evaluates the quartic at \(x=su+tv+\varepsilon(s\delta u+t\delta v)\) modulo \(\varepsilon^2\); its \(\varepsilon\)-coefficient is the actual Hilbert-scheme tangent Jacobian.

## Relationship to prior work
Shimada and Shioda introduced the 56-line quartic and studied its reductions. Their special smooth reduction at one prime over three is a different model with 112 lines. Veniani, Example 5.4, wrote the particular singular \(\mathbf F_3\)-equation above, established its eight \(A_1\) singularities, and reported 48 geometric lines. The **48-line count and the surface itself are not new here**. The claim here is the field-of-definition decomposition and the scheme-theoretic distinction between seven infinitesimally nonrigid and 41 rigid line points, including their Frobenius orbits. The available inspected parts of these sources do not state those invariants; this is not a global proof of novelty across all literature.

## Limitations
The geometric completeness relies in part on Veniani's published 48-line count, combined with an independently reproducible exhaustive enumeration of 48 distinct lines over \(\mathbf F_9\). The checker proves the tangent dimensions but does **not** determine the complete local Artin algebra or its length at the seven nonreduced points. There is no claim about arbitrary twists, other reductions, the zeta function of the quartic surface, or an independent scientific audit. Specialized unpublished or less-accessible literature may overlap the arithmetic or infinitesimal statements.

## References
- I. Shimada and T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic*, arXiv:1604.06265 (first posted 2016-04-21), especially Section 5.2 (different primes over three). https://arxiv.org/abs/1604.06265
- D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (first posted 2016-08-15), especially Example 5.4 (explicit model; 48 lines and eight nodes). https://arxiv.org/abs/1608.04209
