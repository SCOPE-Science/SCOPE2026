# Projective-tensor ODP for arbitrary diffuse von Neumann preduals

## Result

Let \(\mathcal M\) be an arbitrary diffuse complex von Neumann algebra, with no semifiniteness assumption, and let \(Y\neq\{0\}\) be a complex Banach space. Then
\[
\mathcal M_*\widehat\otimes_\pi Y
\]
has the operator Daugavet property (ODP). In fact, the witnesses can be chosen in the following stronger form: for every finite set \(z_1,\ldots,z_n\in S_{\mathcal M_*\widehat\otimes_\pi Y}\), every slice
\[
S(B_{\mathcal M_*\widehat\otimes_\pi Y},G,\alpha)
\]
and every \(\varepsilon>0\), there is an elementary tensor \(x=k\otimes y_0\) in that slice such that, for every \(z'\in B_{\mathcal M_*\widehat\otimes_\pi Y}\), there is a contraction \(\Phi_{z'}\) satisfying
\[
\Phi_{z'}x=z',\qquad \|\Phi_{z'}z_i-z_i\|<\varepsilon\quad(1\le i\le n).
\]

Consequently, for an arbitrary complex von Neumann algebra \(\mathcal M\), the following are equivalent:

1. \(\mathcal M\) is diffuse;
2. \(\mathcal M_*\widehat\otimes_\pi Y\) has ODP for every nonzero complex Banach space \(Y\);
3. \(\mathcal M_*\) has ODP.

The recent theorem of Qi--Liu--Li proves the tensor conclusion when \(\mathcal M\) is diffuse semifinite and is represented as \(L_1(\mathcal M,\tau)\). Huang--Nessipbayev--Sukochev--Xu prove that the predual of an arbitrary atomless von Neumann algebra has ODP. The argument below combines the rectangular-corner geometry behind the latter theorem with the tensor replacement mechanism of the former, but uses no trace.

## Definitions and notation

The predual \(\mathcal M_*\) is an \(\mathcal M\)-bimodule under
\[
(a\omega b)(x)=\omega(bxa).
\]
For projections \(d,r\in\mathcal M\), put \(q_d=1-d\), \(q_r=1-r\), and define
\[
B\omega=d\omega r,\qquad C\omega=q_d\omega q_r.
\]
We use the standard isometric duality
\[
(\mathcal M_*\widehat\otimes_\pi Y)^*\cong \mathcal L(\mathcal M_*,Y^*).
\]

## 1. A trace-free two-corner inequality

For every \(\omega\in\mathcal M_*\),
\[
\boxed{\ \|B\omega\|+\|C\omega\|\le \|\omega\|.\ }
\]
Indeed, if \(P=B+C\), then its adjoint on \(\mathcal M=(\mathcal M_*)^*\) is
\[
P^*a=rad+q_ra q_d=\frac12\bigl(a+s_ra s_d\bigr),
\]
where \(s_r=q_r-r\) and \(s_d=q_d-d\) are self-adjoint unitaries. Hence \(\|P\|\le1\). Moreover, \(B\omega\in d\mathcal M_*r\) and \(C\omega\in q_d\mathcal M_*q_r\), so the orthogonal rectangular-corner norm additivity of Huang--Nessipbayev--Sukochev--Xu gives
\[
\|P\omega\|=\|B\omega\|+\|C\omega\|.
\]

It follows directly from the definition of the projective norm that, for every Banach space \(Y\) and every \(z\in\mathcal M_*\widehat\otimes_\pi Y\),
\[
\boxed{\ 
\|(B\otimes I_Y)z\|_\pi+\|(C\otimes I_Y)z\|_\pi\le\|z\|_\pi.
\ }
\tag{1}
\]

This is the exact analogue of the two-corner estimate used in the semifinite \(L_1\) proof, but it is intrinsic to the predual and requires no trace.

## 2. Trace-free localization inside a tensor slice

Let \(G\in S_{\mathcal L(\mathcal M_*,Y^*)}\), let \(\alpha>0\), let \(F\subset\mathcal M_*\) be finite, and let \(\eta>0\). We claim that there exist \(y_0\in S_Y\), nonzero projections \(d,r\in\mathcal M\), and \(k\in d\mathcal M_*r\) with \(\|k\|=1\), such that
\[
\operatorname{Re}G(k)(y_0)>1-\alpha,
\tag{2}
\]
and
\[
\|d\omega\|<\eta,\qquad \|\omega r\|<\eta\qquad(\omega\in F).
\tag{3}
\]

Choose \(0<\rho<1\) so that \((1-\rho)^2>1-\alpha\). Since \(\|G\|=1\), choose \(y_0\in S_Y\) such that the scalar functional
\[
\omega\longmapsto G(\omega)(y_0)
\]
corresponds to an element \(a\in\mathcal M\) with \(\|a\|>1-\rho\). Put \(b=a/\|a\|\) and write the polar decomposition \(b=u|b|\). The spectral projection
\[
p=e^{|b|}(1-\rho,1]
\]
is nonzero and satisfies \(p\le u^*u\).

Huang--Nessipbayev--Sukochev--Xu, Lemma 7.3, applies to the finite family \(F\): there exists a nonzero \(d\le p\) such that, with
\[
r=udu^*,
\]
(3) holds. Since \(d\le p\),
\[
\|rbd\|=\|d|b|d\|>1-\rho.
\]
The rectangular-corner duality \((d\mathcal M_*r)^*=r\mathcal M d\) therefore gives \(k\in d\mathcal M_*r\), \(\|k\|=1\), whose phase may be chosen so that
\[
\operatorname{Re}k(b)>1-\rho.
\]
Consequently
\[
\operatorname{Re}G(k)(y_0)=\operatorname{Re}k(a)>(1-\rho)^2>1-\alpha,
\]
which proves the claim.

Two estimates will be used below. From (3),
\[
\|B\omega\|=\|d\omega r\|<\eta,
\tag{4}
\]
and
\[
\|\omega-C\omega\|
=\|d\omega+q_d\omega r\|
<2\eta
\tag{5}
\]
for \(\omega\in F\).

## 3. ODP of the projective tensor product

Set
\[
Z=\mathcal M_*\widehat\otimes_\pi Y.
\]
Fix \(z_1,\ldots,z_n\in S_Z\), a slice \(S(B_Z,G,\alpha)\), and \(\varepsilon>0\). Approximate each \(z_i\) by a finite tensor
\[
w_i=\sum_j\omega_{ij}\otimes y_{ij}
\]
so closely that the final approximation error is below \(\varepsilon\). Let \(F\) consist of all coefficients \(\omega_{ij}\). Apply the localization above with \(\eta\) sufficiently small. Equations (4)--(5), summed against the finitely many \(\|y_{ij}\|\), give
\[
\|((I-C)\otimes I_Y)w_i\|_\pi
+
\|(B\otimes I_Y)w_i\|_\pi
<\delta
\tag{6}
\]
for any prescribed \(\delta>0\).

Let \(k\in d\mathcal M_*r\) and \(y_0\in S_Y\) be the localized elements. Then
\[
x=k\otimes y_0\in S(B_Z,G,\alpha),\qquad \|x\|_\pi=1.
\]
Choose \(y_0^*\in S_{Y^*}\) with \(y_0^*(y_0)=1\), and choose \(\psi\in(d\mathcal M_*r)^*\) with \(\|\psi\|=1\) and \(\psi(k)=1\). Define \(H\in Z^*\) on elementary tensors by
\[
H(\omega\otimes y)=\psi(d\omega r)y_0^*(y).
\]
Then
\[
|H(z)|\le \|(B\otimes I_Y)z\|_\pi,
\qquad H(x)=1.
\tag{7}
\]

For an arbitrary target \(z'\in B_Z\), define
\[
\Phi_{z'}z=(C\otimes I_Y)z+H(z)z'.
\tag{8}
\]
By (1) and (7),
\[
\|\Phi_{z'}z\|
\le
\|(C\otimes I_Y)z\|_\pi+\|(B\otimes I_Y)z\|_\pi
\le\|z\|_\pi.
\]
Thus \(\Phi_{z'}\) is a contraction. Since \(Bk=k\), \(Ck=0\), and \(H(x)=1\),
\[
\Phi_{z'}x=z'.
\]
Finally,
\[
\|\Phi_{z'}z_i-z_i\|
\le
\|((C-I)\otimes I_Y)z_i\|_\pi
+
\|(B\otimes I_Y)z_i\|_\pi.
\]
Equation (6), together with the arbitrarily close finite-tensor approximation and \(\|B\|,\|C\|\le1\), makes this smaller than \(\varepsilon\), uniformly in \(z'\in B_Z\). This proves ODP, with contractive witnesses and an elementary witnessing tensor.

## 4. Characterization of diffuseness

If \(\mathcal M\) is diffuse, the theorem applies for every nonzero \(Y\). Conversely, taking \(Y=\mathbb C\) gives \(\mathcal M_*\widehat\otimes_\pi\mathbb C\cong\mathcal M_*\). ODP implies the Daugavet property, and Oikhberg's theorem says that a von Neumann predual has the Daugavet property exactly when the von Neumann algebra is non-atomic. Hence the three conditions in the statement are equivalent.

In particular, the projective-tensor ODP theorem holds for diffuse type III von Neumann algebras, which lie outside the semifinite hypothesis of the recent \(L_1(\mathcal M,\tau)\) theorem.

## Relation to prior work and originality boundary

Huang--Nessipbayev--Sukochev--Xu prove ODP for \(\mathcal M_*\) when \(\mathcal M\) is an arbitrary atomless von Neumann algebra, and their Lemmas 7.3--7.4 supply the trace-free small-corner and corner-additivity facts used above. Qi--Liu--Li prove ODP for \(L_1(\mathcal M,\tau)\widehat\otimes_\pi Y\) when \(\mathcal M\) is diffuse semifinite, using finite-trace localization. The present result replaces that trace localization by normal-functional localization and thereby removes semifiniteness from the tensor theorem.

Older tensor results do not make this automatic from ODP alone. In particular, the projective-tensor stability theorem for the weak operator Daugavet property requires both factors to have WODP, while known arbitrary-second-factor consequences under WODP are weaker diameter-two conclusions. Thus the conclusion for arbitrary nonzero \(Y\) uses the special rectangular-corner geometry of von Neumann preduals rather than a generic permanence principle.

Originality is asserted only to the best of our knowledge. Exact and synonymous searches around operator Daugavet property, von Neumann preduals, projective tensor products, nonsemifinite/type III algebras, and the two recent source papers did not reveal a prior statement covering the theorem above. A residual risk remains that a very recent or differently phrased tensor-geometric result contains an equivalent argument.

## Limitations

- The result is stated for complex von Neumann algebras and complex Banach spaces; no real analogue is proved here.
- No generic theorem is claimed saying that \(X\) having ODP forces \(X\widehat\otimes_\pi Y\) to have ODP for arbitrary \(Y\).
- The proof gives contractive witnesses but does not address additional operator-space or completely bounded structure.
- No quantitative invariant beyond the norm-one witness bound is introduced.

## References

1. J. Huang, Y. Nessipbayev, F. Sukochev, R. Xu, *The Daugavet property in symmetric operator spaces*, arXiv:2608.30491v1 (2026), especially Section 7. https://arxiv.org/abs/2608.30491
2. J. Qi, Q. Liu, Y. Li, *The Operator Daugavet Property in Semifinite Noncommutative L1-Spaces*, arXiv:2609.18044v1 (2026). https://arxiv.org/abs/2609.18044
3. M. Martín, A. Rueda Zoca, *Daugavet property in projective symmetric tensor products of Banach spaces*, Banach J. Math. Anal. 16 (2022), 35. https://doi.org/10.1007/s43037-022-00186-6
4. A. Rueda Zoca, *Weak operator Daugavet property and weakly open sets in tensor product spaces*, Rev. Mat. Complut. (2025). https://doi.org/10.1007/s13163-025-00531-x
5. T. Oikhberg, *The Daugavet property of C*-algebras and non-commutative Lp-spaces*, Positivity 6 (2002), 59--73. https://doi.org/10.1023/A:1012023526639
