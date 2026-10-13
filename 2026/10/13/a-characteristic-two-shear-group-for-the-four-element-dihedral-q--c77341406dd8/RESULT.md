# A characteristic-two shear group for the four-element dihedral quandle algebra
## Finding
Let \(K\) be any field of characteristic \(2\). Let \(R_4=\mathbb Z/4\mathbb Z\) carry the dihedral quandle operation \(i*j=2j-i\pmod 4\), and let \(E=K[R_4]\) be the four-dimensional, generally nonassociative quandle algebra. Put
\[
u=e_0+e_2,\qquad v=e_1+e_3,\qquad H=Ke_0\oplus Ke_1,\qquad W=Ku\oplus Kv.
\]
The group of \(K\)-linear algebra automorphisms is exactly
\[
\boxed{\operatorname{Aut}_K(E)\cong (M_2(K),+)\rtimes C_2,}
\]
where the nontrivial element of \(C_2\) sends a matrix \(C\) to \(PCP\), with \(P=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). More explicitly, relative to the direct sum \(E=H\oplus W\), every automorphism is *uniquely* one of the block maps
\[
(h,w)\longmapsto (h,Ch+w)\quad\text{or}\quad (h,w)\longmapsto(Ph,Ch+Pw),\qquad C\in M_2(K).
\]
For \(K=\mathbb F_{2^m}\) this gives the exact order \(2^{4m+1}\); in particular, the orders for \(\mathbb F_2,\mathbb F_4,\mathbb F_8\) are \(32,512,8192\).

## Assumptions and scope
Throughout, \(K\) is a commutative field of characteristic \(2\), without any finiteness or perfectness assumption. The multiplication of \(E\) is bilinear extension of \(e_i e_j=e_{2j-i\bmod 4}\), and automorphisms are required to be \(K\)-linear and multiplicative. In the ordered decomposition \(H=Ke_0\oplus Ke_1\), \(W=Ku\oplus Kv\), the matrix \(C\) is an arbitrary \(2\times2\) matrix over \(K\). The group law uses the additive group of this matrix space, not matrix multiplication.

## Proof
1. **Intrinsic two-dimensional ideal and multiplication.** In the specified basis put \(x=ah_0+bh_1+cu+dv\), where \(h_0=e_0\), \(h_1=e_1\). Define \(\alpha(x)=a\), \(\beta(x)=b\) and \(\varepsilon(x)=a+b\). The right translations of \(R_4\) fix one parity pair and exchange the other. As characteristic is \(2\), expanding the multiplication table yields, for all \(x,y\in E\),
\[
xy=\varepsilon(y)x+\alpha(x)\beta(y)u+\beta(x)\alpha(y)v. \tag{1}
\]
In particular \(xw=0\) and \(wx=\varepsilon(x)w\) for every \(w\in W\). Conversely, if \(y\) belongs to the right annihilator of \(E\), then \(uy=\varepsilon(y)u=0\) forces \(\varepsilon(y)=0\). Next \(h_0y=\beta(y)u=0\) and \(h_1y=\alpha(y)v=0\), so \(\alpha(y)=\beta(y)=0\). Hence
\[
W=\operatorname{Ann}_{\mathrm{right}}(E)
\]
is characteristic under all algebra automorphisms. The action of \(E\) on the left of \(W\), namely \(wx=\varepsilon(x)w\), also makes \(\varepsilon\) invariant under every automorphism.

2. **General block form.** Every automorphism therefore has the block form
\[
f(h+w)=Ah+Ch+Bw,
\]
where \(A\in\operatorname{GL}(H)\), \(B\in\operatorname{GL}(W)\), \(C\in\operatorname{Hom}_K(H,W)\), and \(\varepsilon(Ah)=\varepsilon(h)\). Write
\[
m(h,k)=\alpha(h)\beta(k)u+\beta(h)\alpha(k)v.
\]
By (1) the product of \((h,w)\) and \((k,z)\) is
\[
(h,w)(k,z)=\bigl(\varepsilon(k)h,\ \varepsilon(k)w+m(h,k)\bigr).
\]
Comparing \(f((h,w)(k,z))\) with \(f(h,w)f(k,z)\), the terms involving \(C\) cancel identically. Thus *multiplicativity is equivalent to*
\[
B\,m(h,k)=m(Ah,Ak)\qquad\text{for all }h,k\in H. \tag{2}
\]

3. **Only identity or simultaneous swaps.** Relative to \((h_0,h_1)\), write \(A=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\). Since \(m(h_0,h_0)=m(h_1,h_1)=0\), equation (2) yields \(ac(u+v)=bd(u+v)=0\). The independence of \(u,v\) gives \(ac=bd=0\). Invertibility of \(A\) forces it to be diagonal or antidiagonal. The condition \(\varepsilon A=\varepsilon\) forces it to be exactly \(I\) or \(P\). Moreover \(m(h_0,h_1)=u\) and \(m(h_1,h_0)=v\), so (2) uniquely determines \(B=I\) when \(A=I\), and \(B=P\) when \(A=P\). Conversely these pairs obey (2), and every \(C\) is allowed. The displayed block maps are therefore precisely all algebra automorphisms, not just a subgroup.

4. **Group law.** The shear maps \(s_C:(h,w)\mapsto(h,Ch+w)\) form an additive normal subgroup isomorphic to \(M_2(K)\). The involution \(\tau:(h,w)\mapsto(Ph,Pw)\) conjugates \(s_C\) to \(s_{PCP}\). Every automorphism has exactly one expression \(s_C\tau^j\), \(j\in\{0,1\}\), proving the semidirect-product description. For finite \(K\) with \(|K|=2^m\), counting matrices \(C\) gives \(2\,|K|^4=2^{4m+1}\).

## Verification
Run `python3 verify.py` with Python 3 and the standard library. The checker reconstructs the original multiplication \(e_i e_j=e_{2j-i\bmod4}\) independently of the displayed proof. It exhaustively enumerates all \(2^{16}\) binary linear maps, filters to the \(20{,}160\) invertible ones, tests preservation of all \(16\) basis products, and recovers exactly \(32\) automorphisms. These are equal, as a complete set of matrices, to the \(32\) block maps in the theorem. Over genuine extension fields \(\mathbb F_4\) and \(\mathbb F_8\), using polynomial-basis arithmetic, it tests every one of the \(512\) and \(8192\) asserted block maps against all basis products and checks they are distinct. These finite checks support, but do not replace, the symbolic all-fields proof above.

## Relationship to prior work
Sangare and Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (arXiv:2608.01550v1, August 3, 2026), explicitly give complete automorphism groups for trivial and odd-order dihedral quandle algebras and only a partial result for even dihedral order. Their Theorem 4.15 requires characteristic different from \(2\), while the present theorem treats exactly that excluded characteristic for order \(4\) and classifies all automorphisms. Their Theorem 4.2, citing Bardakov, Passi, and Singh, includes the integral computation \(\operatorname{Aut}_{\mathbb Z}(\mathbb Z[R_4])\) of order \(8\); that integral result does not imply the characteristic-two automorphism group, which has order \(32\) already over \(\mathbb F_2\). Earlier work on right ideals of dihedral quandle rings is also distinct from the present classification of algebra automorphisms.

## Limitations
This classifies \(K\)-linear automorphisms for the four-element dihedral quandle only; it does not classify larger even dihedral quandle algebras, arbitrary coefficient rings, or semilinear field-automorphism extensions. The finite verifier checks only fields of orders \(2,4,8\); the all-fields result depends on the proof, not on extrapolation. The literature comparison cannot rule out a historical equivalent stated in different terminology. Independent validation has not been performed.

## References
- B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1, first submitted 2026-08-03, especially Section 4 and Theorems 4.2, 4.13, 4.15. https://arxiv.org/abs/2608.01550
- V. G. Bardakov, I. B. S. Passi, and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (2020). https://arxiv.org/abs/2001.06843
- M. Elhamdadi, N. Fernando, and B. Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908 (2018), on right ideals and general properties. https://arxiv.org/abs/1805.05908
