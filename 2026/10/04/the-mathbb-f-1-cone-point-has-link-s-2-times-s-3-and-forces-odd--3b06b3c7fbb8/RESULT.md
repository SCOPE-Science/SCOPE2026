# The \(\mathbb F_1\)-cone point has link \(S^2\times S^3\) and forces odd Euler characteristic
## Finding
Let \(X_C\) be the compact Calabi--Yau threefold of Wuebben associated with the \(7\)-vertex reflexive polytope \(\Delta_C\). Its unique singular point \(p\) is analytically the anticanonical cone over the first Hirzebruch surface \(\mathbb F_1\), and its smooth maximal projective crepant partial resolution \(\widehat X_C\) has
\[
(h^{1,1},h^{2,1})=(4,108).
\]

The link \(L_p\) of the singularity is diffeomorphic to
\[
L_p\cong S^2\times S^3.
\]
In particular
\[
H^i(L_p,\mathbf Z)\cong
\begin{cases}
\mathbf Z,&i=0,2,3,5,\\
0,&i=1,4.
\end{cases}
\]
Thus \(p\) is not a rational homology-manifold point.

The ordinary topological Euler characteristic of the singular compact threefold is
\[
\chi_{\mathrm{top}}(X_C)=-211.
\]
This is odd. Hence \(X_C\) is not homotopy equivalent to a closed oriented \(6\)-manifold and, more generally, does not satisfy rational Poincaré duality in formal dimension \(6\).

## Assumptions and scope
All spaces are considered over \(\mathbf C\), and links are taken in the classical topology. The result concerns Wuebben's specific compact threefold \(X_C\) and the ordinary topological Euler characteristic, not intersection cohomology or stringy Euler numbers.

Write \(S\) for the negative section and \(F\) for a fibre of \(\mathbb F_1\). Then
\[
S^2=-1,\qquad S\cdot F=1,\qquad F^2=0,
\]
and
\[
K_{\mathbb F_1}=-2S-3F.
\]

## Proof
The affine anticanonical cone over \(\mathbb F_1\) is obtained by contracting the zero section of the canonical line bundle
\[
K_{\mathbb F_1}\longrightarrow \mathbb F_1.
\]
Therefore its link is the unit-circle bundle
\[
S(K_{\mathbb F_1})\longrightarrow \mathbb F_1
\]
with Euler class
\[
e=c_1(K_{\mathbb F_1})=-2S-3F.
\]

First compute the fundamental group. Since \(\mathbb F_1\) is simply connected, the homotopy exact sequence of the circle bundle contains
\[
\pi_2(\mathbb F_1)\longrightarrow \pi_1(S^1)\longrightarrow \pi_1(L_p)\longrightarrow 0.
\]
Evaluation of \(e\) on the standard curve classes gives
\[
e\cdot S=-1,\qquad e\cdot F=-2.
\]
Because these integers generate \(\mathbf Z\), the first map is surjective. Hence
\[
\pi_1(L_p)=0.
\]

Next use the integral Gysin sequence. The map
\[
H^0(\mathbb F_1,\mathbf Z)\xrightarrow{\smile e}H^2(\mathbb F_1,\mathbf Z)
\]
sends \(1\) to the primitive class \((-2,-3)\), so its cokernel is \(\mathbf Z\). Thus
\[
H^2(L_p,\mathbf Z)\cong\mathbf Z.
\]
The map
\[
H^2(\mathbb F_1,\mathbf Z)\xrightarrow{\smile e}H^4(\mathbb F_1,\mathbf Z)
\]
is the row
\[
(-1,-2)
\]
in the basis \((S,F)\), hence is surjective with kernel of rank \(1\). Therefore
\[
H^3(L_p,\mathbf Z)\cong\mathbf Z,\qquad H^4(L_p,\mathbf Z)=0.
\]
Together with connectedness and orientation this gives the displayed integral cohomology groups.

The tangent bundle of the total circle bundle splits stably into the pullback of \(T\mathbb F_1\) and a trivial real line. Hence
\[
w_2(L_p)=\pi^*w_2(\mathbb F_1).
\]
For the complex surface \(\mathbb F_1\),
\[
w_2(\mathbb F_1)\equiv c_1(\mathbb F_1)\equiv -K_{\mathbb F_1}\equiv e\pmod 2.
\]
But the Euler class pulls back to zero on its own circle bundle, so
\[
w_2(L_p)=0.
\]
Thus \(L_p\) is a simply connected spin \(5\)-manifold with torsion-free \(H_2\cong\mathbf Z\). The Smale--Barden classification of simply connected smooth \(5\)-manifolds therefore yields
\[
L_p\cong S^2\times S^3.
\]

For the global Euler characteristic, Wuebben gives
\[
(h^{1,1},h^{2,1})(\widehat X_C)=(4,108),
\]
so the smooth Calabi--Yau threefold \(\widehat X_C\) has
\[
\chi_{\mathrm{top}}(\widehat X_C)=2(4-108)=-208.
\]
The crepant resolution is an isomorphism away from \(p\), and over \(p\) it replaces the cone vertex by the zero section \(\mathbb F_1\). Since
\[
\chi_{\mathrm{top}}(\mathbb F_1)=4,
\]
additivity of Euler characteristic gives
\[
\chi_{\mathrm{top}}(X_C)
=
\chi_{\mathrm{top}}(\widehat X_C)-\chi_{\mathrm{top}}(\mathbb F_1)+1
=
-208-4+1
=
-211.
\]

Finally, a rational Poincaré-duality space of formal dimension \(6\) has
\[
b_i=b_{6-i},
\]
and its middle pairing on \(H^3\) is alternating and nondegenerate, so \(b_3\) is even. Therefore its Euler characteristic is even. Since \(\chi_{\mathrm{top}}(X_C)=-211\), \(X_C\) cannot be such a space.

## Verification
The accompanying `verify.py` checks the intersection arithmetic on \(\mathbb F_1\), primitivity and surjectivity in the two Gysin maps, the parity calculation for \(w_2\), and the Euler-characteristic arithmetic. Its stored replay output ends in `VERIFY_OK`.

The verifier does not prove the Smale--Barden classification, Wuebben's construction, or the identification of the local crepant model with the canonical bundle of \(\mathbb F_1\); those are mathematical inputs explained above and cited below.

## Relationship to prior work
Wuebben proves that \(X_C\) has a unique singularity equal to the anticanonical cone over \(\mathbb F_1\), that every reduced deformation preserves this germ, and that the smooth maximal projective crepant partial resolution has Hodge numbers \((4,108)\), hence Euler number \(-208\). Gross's earlier work identifies \(\mathbb F_1\) as one of the exceptional divisor types in primitive type-II contractions for which smoothing may fail.

The inspected sources do not state the diffeomorphism type of the link as \(S^2\times S^3\), the ordinary Euler characteristic \(-211\) of this compact singular threefold, or the resulting failure of rational Poincaré duality. Targeted searches for these equivalent formulations did not locate a covering statement.

## Limitations
The result determines the topology of the local link and one global additive invariant. It does not compute the full ordinary cohomology ring of \(X_C\), its intersection cohomology, or the mixed Hodge structure on ordinary cohomology.

The link calculation is a standard consequence of the topology of an anticanonical cone once Wuebben's local analytic identification is known. The new content here is its explicit application to this compact extremal example together with the odd-Euler and Poincaré-duality consequences. Unindexed or differently phrased prior computations remain a residual originality risk.

## References
1. B. J. Wuebben, *Non-smoothable Calabi--Yau threefolds from reflexive polytopes*, arXiv:2609.28499v1, 2026; Theorem 5.6.
2. M. Gross, *Deforming Calabi--Yau Threefolds*, Math. Ann. 308 (1997), 187--220; arXiv:alg-geom/9506022.
3. S. Smale, *On the structure of 5-manifolds*, Ann. of Math. 75 (1962), 38--46.
4. D. Barden, *Simply connected five-manifolds*, Ann. of Math. 82 (1965), 365--385.
