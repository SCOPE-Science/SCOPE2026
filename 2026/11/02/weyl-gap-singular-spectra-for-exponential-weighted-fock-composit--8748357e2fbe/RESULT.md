# Weyl-gap singular spectra for exponential weighted Fock composition cross-products

## Finding
Let \(\mathcal F^2\) denote the one-variable Bargmann–Fock Hilbert space, and for \(j=1,2\) let
\[
(W_jf)(z)=h_j e^{u_jz}f(a_jz+b_j),\qquad |a_j|<1,\quad h_j\ne0,
\]
where all displayed parameters are complex. Set
\[
 v_j=\frac{\overline{u_j}+\overline{a_j}b_j}{1-|a_j|^2},\qquad
 w_j=-b_j-a_jv_j,\qquad
 N_j=|h_j|\exp\!\left(\frac{|b_j|^2+(1-|a_j|^2)|v_j|^2}{2}\right),
\]
and put
\[
 r=|a_1a_2|,\qquad
 \kappa=\frac{(1-|a_1|^2)(1-|a_2|^2)}{1-|a_1a_2|^2}.
\]
The two adjoint orders have **complete, explicit singular-value sequences**: for each integer \(k\ge0\),
\[
 \boxed{\begin{aligned}
 s_{k+1}(W_1W_2^*)&=N_1N_2\,e^{-\kappa|w_1-w_2|^2/2}\,r^k,\\
 s_{k+1}(W_1^*W_2)&=N_1N_2\,e^{-\kappa|v_1-v_2|^2/2}\,r^k.
 \end{aligned}}
\]
Here singular values are in decreasing order; if \(r=0\), the operators have rank one and all singular values after the first are zero. Both operators belong to every Schatten class \(\mathcal S_p\), \(p>0\), with exact quasi-norms
\[
\|W_1W_2^*\|_{\mathcal S_p}
=\frac{N_1N_2e^{-\kappa|w_1-w_2|^2/2}}{(1-r^p)^{1/p}},\qquad
\|W_1^*W_2\|_{\mathcal S_p}
=\frac{N_1N_2e^{-\kappa|v_1-v_2|^2/2}}{(1-r^p)^{1/p}}.
\]
The same numerators are their operator norms; the formulas also determine every finite-rank approximation number.

The two phase-space gaps are independent. Fix any real \(0<a<1\), let \(D_a f(z)=f(az)\), and let \(U_t\) be the Weyl unitary defined below. With \(W_1=D_a\), choosing \(W_2=U_tD_a\) gives
\[
\|W_1\|=\|W_2\|=\|W_1W_2^*\|=1,\qquad
\|W_1^*W_2\|=\exp\!\left(-\frac{1-a^2}{2(1+a^2)}|t|^2\right).
\]
Choosing instead \(W_2=D_aU_t\) reverses the two cross-product norm values. Hence, **even with equal slopes and unit-norm factors**, either adjoint order can dominate the other by an arbitrarily large factor.

## Assumptions and scope
Normalize the Fock inner product by
\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
\]
so \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), is an orthonormal basis. Let
\[
 (U_tf)(z)=e^{\overline t z-|t|^2/2}f(z-t).
\]
Each \(U_t\) is unitary and \(U_sU_t\) agrees with \(U_{s+t}\) up to a unimodular scalar. Throughout, the affine slopes are **strictly contractive**; the endpoint \(|a_j|=1\) is not asserted, and the weights are specifically nonzero scalar multiples of exponentials of linear entire functions. All products in the theorem are bounded and compact. If either slope vanishes, the stated geometric progression is interpreted as a rank-one sequence.

## Proof
**Step 1: an exact Weyl–dilation decomposition.** For \(|a|<1\), the Weyl unitaries and the dilation \(D_a\) satisfy
\[
(U_vD_aU_wf)(z)
=e^{(\overline v+a\overline w)z-(|v|^2+|w|^2)/2-av\overline w}
 f(az-av-w).
\]
For a weighted affine operator \(Wf(z)=he^{uz}f(az+b)\), choose
\[
 v=\frac{\overline u+\overline a b}{1-|a|^2},\qquad w=-b-av.
\]
The linear exponential coefficient is then \(u\), and the affine translation is \(b\). Thus \(W=\lambda U_vD_aU_w\) for the nonzero scalar
\[
 \lambda=h\exp\!\left(\frac{|v|^2+|w|^2}{2}+av\overline w\right).
\]
Substituting \(w=-b-av\), taking real parts, and cancelling the cross terms gives
\[
 |\lambda|=|h|\exp\!\left(\frac{|b|^2+(1-|a|^2)|v|^2}{2}\right)=N.
\]
In particular, \(\|W\|=N\) because \(\|D_a\|=1\).

**Step 2: exact displacement penalty for a compressed Weyl unitary.** Let \(|a|,|c|<1\), \(t\in\mathbb C\), and let \(p=a\overline c\). Direct substitution gives
\[
(D_aU_tD_{\overline c}f)(z)
=e^{a\overline t z-|t|^2/2}f(pz-\overline c t).
\]
Apply Step 1 with \(u=a\overline t\) and \(b=-\overline c t\). Writing \(\Delta=1-|ac|^2\), the two displacements become
\[
 V=\frac{\overline a(1-|c|^2)}{\Delta}\,t,\qquad
 H=\frac{\overline c(1-|a|^2)}{\Delta}\,t.
\]
Its scalar factor has modulus
\[
\begin{aligned}
\exp\!\left(\frac{-|t|^2+|c|^2|t|^2+\Delta|V|^2}{2}\right)
&=\exp\!\left(-\frac{(1-|a|^2)(1-|c|^2)}{2\Delta}|t|^2\right)\\
&=e^{-\kappa|t|^2/2}.
\end{aligned}
\]
Consequently \(D_aU_tD_{\overline c}\) is unitarily equivalent on its two sides, up to a scalar of modulus \(e^{-\kappa|t|^2/2}\), to \(D_p\). Its full singular-value sequence is therefore \(e^{-\kappa|t|^2/2}|ac|^k\), \(k\ge0\); this includes the zero-slope case.

**Step 3: the two orders.** Insert the Step 1 factorizations for \(W_1\) and \(W_2\). Weyl multiplication absorbs unimodular phases:
\[
W_1W_2^*=\lambda_1\overline{\lambda_2}\,U_{v_1}D_{a_1}(U_{w_1}U_{w_2}^*)D_{\overline{a_2}}U_{v_2}^*,
\]
where the middle Weyl product is a phase multiple of \(U_{w_1-w_2}\). Step 2 now gives the first sequence. Likewise,
\[
W_1^*W_2=\overline{\lambda_1}\lambda_2\,U_{w_1}^*D_{\overline{a_1}}(U_{v_1}^*U_{v_2})D_{a_2}U_{w_2},
\]
whose middle displacement is \(v_2-v_1\). This gives the second sequence with the same positive \(\kappa\). Raising singular values to the power \(p\) and summing a convergent geometric series proves each Schatten formula. The singular-value sequences of compact operators are their Hilbert-space approximation numbers.

**Step 4: sharp two-sided order reversal at fixed slope.** Take \(W_1=D_a\), where \(a\in(0,1)\). For \(W_2=U_tD_a\), the Weyl data are \((v_1,w_1)=(0,0)\), \((v_2,w_2)=(t,0)\), and \(N_1=N_2=1\). Hence the first cross norm is one and the second has the asserted Gaussian penalty. In contrast, \(W_2=D_aU_t\) has Weyl data \((v_2,w_2)=(0,t)\) and reverses the roles. Both \(W_2\) are of the permitted form: respectively
\[
 (U_tD_af)(z)=e^{\overline t z-|t|^2/2}f(az-at),\qquad
 (D_aU_tf)(z)=e^{a\overline t z-|t|^2/2}f(az-t).
\]
Sending \(|t|\to\infty\) makes the ratio of the two cross-product norms tend to infinity in either prescribed direction. This establishes all statements.

## Verification
The attached standalone `checker.py` uses explicitly derived finite monomial matrices to compare the first five computed singular values in each adjoint order for five distinct parameter pairs, including vanishing slopes and complex affine parameters. It also checks the unit-normalized equal-slope order reversal. All **64** numerical assertions pass. This finite-dimensional test is a consistency check, **not** the proof for infinite-dimensional operators. The universal formulas, exact rank, and Schatten statements follow from the analytical Weyl–dilation factorization above.

## Relationship to prior work
Tian's 2026 work investigates when products of weighted Fock composition operators and their adjoints are compact, invertible, or isometric; those qualitative operator classifications do not specify the two independent Gaussian displacement penalties or the full singular-value sequences here. Fatehi's earlier work gives norm formulas for individual weighted composition operators; such single-factor formulas do not determine cross-product singular values. The unweighted affine composition problem is a strict subfamily of the present theorem; the same-slope, equal-factor-norm reversal is generated by exponential weights and cannot be inferred from unweighted two-product formulas alone. This statement is restricted to one complex dimension and strictly contractive affine symbols.

## Limitations
This is an analytical identity for a specified exponential-weight subfamily, not a claim about every bounded weighted composition operator on Fock space or any symbol with a nonlinear weight. A zero slope produces rank-one products; strictly contractive nonzero slopes produce infinite rank. The finite checker does not independently validate the proof. A broader equivalent Gaussian-semigroup formula might exist in older operator or coherent-state literature under different terminology; bibliographic priority remains subject to further specialist examination.

## References
1. Xianchi Tian, *Weighted composition operators on the Fock space*, arXiv:2610.29786v1 (first public 2026-10-21), https://arxiv.org/abs/2610.29786 .
2. Mahsa Fatehi, *Weighted composition operators on the Fock space*, arXiv:1809.04829v1 (2018), https://arxiv.org/abs/1809.04829 .
3. Trieu Le, *Normal and isometric weighted composition operators on the Fock space*, Bull. Lond. Math. Soc. 46 (2014), 847–856, DOI:10.1112/blms/bdu046.
4. Somdatta Barik, Anirban Sen, and Kallol Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1 (2026), https://arxiv.org/abs/2607.17170 .
