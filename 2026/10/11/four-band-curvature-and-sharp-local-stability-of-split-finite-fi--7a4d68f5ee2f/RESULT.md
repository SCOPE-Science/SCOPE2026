# Four-band curvature and sharp local stability of split finite-field Fourier extension

## Finding

Let \(q\ge3\) be any odd prime power, and let \(\psi:\mathbb F_q\to\mathbb C\) be a nontrivial additive character. For \(f:\mathbb F_q^2\to\mathbb C\), write
\[
\mathcal E_qf(X,Y,T)=\frac1{q^2}\sum_{u,v\in\mathbb F_q}f(u,v)\psi(Xu+Yv+Tuv),
\qquad
m(f)=\frac1{q^2}\sum_{u,v}|f(u,v)|^2.
\]
The sharp extension deficit is
\[
\mathfrak D_q(f)=\left(1+\frac1q-\frac1{q^2}\right)m(f)^2-
\sum_{X,Y,T\in\mathbb F_q}|\mathcal E_qf(X,Y,T)|^4.
\]
The established sharp extension inequality states \(\mathfrak D_q(f)\ge0\). The present result determines the **entire real quadratic variation** of this deficit at a constant extremizer.

Write \(h=a+ib\), with real functions \(a,b\), and use the normalized Fourier transform
\[
\widehat a(k)=q^{-2}\sum_{u,v}a(u,v)\overline{\psi(k_1u+k_2v)},
\quad k=(k_1,k_2)\in\mathbb F_q^2
\]
(and similarly for \(b\)). Then, for real \(t\to0\),
\[
\mathfrak D_q(1+t h)
=t^2\sum_{k\ne(0,0)}
\bigl(\lambda_R(k)|\widehat a(k)|^2+
\lambda_I(k)|\widehat b(k)|^2\bigr)+O_h(t^3),
\]
where
\[
\begin{array}{c|cc|c}
\text{frequency type}&\lambda_R&\lambda_I&\text{number of nonzero frequencies}\\ \hline
k_1k_2=0&2-4/q+4/q^2&2&2(q-1)\\
k_1k_2\ne0&2-2/q+4/q^2&2-2/q&(q-1)^2.
\end{array}
\]
Here each number of frequencies is also the **real** multiplicity of each corresponding real-amplitude or imaginary-phase curvature band. The constant real and imaginary directions give the remaining two zero eigenvalues. The coefficient of \(t^2\), rather than the second derivative itself, is the reported curvature normalization; the Hessian eigenvalues in the usual second-derivative convention are twice these numbers.

The smallest positive curvature equals
\[
\boxed{\lambda_{\min}=2-\frac4q+\frac4{q^2}.}
\]
It is attained precisely when \(h\) is real, mean-zero and has Fourier support on the two punctured coordinate axes, equivalently when \(h(u,v)=r(u)+s(v)\) for real mean-zero functions \(r,s\). In particular, for each fixed \(q\) and every \(\varepsilon>0\), there is a \(\rho(q,\varepsilon)>0\) such that all mean-zero complex \(h\) with \(\|h\|_{L^2(q^{-2})}<\rho\) satisfy
\[
\mathfrak D_q(1+h)\ge(\lambda_{\min}-\varepsilon)\|h\|_{L^2(q^{-2})}^2.
\]
This leading constant cannot be increased. Multiplication by any phase \(\psi(\alpha u+\beta v+\gamma uv)\) transports the full quadratic-form statement to the corresponding unit-modulus extremizer.

## Assumptions and scope

The field has odd characteristic, but is not required to be prime. Both the physical and frequency spaces use their full finite-field additive groups. The \(L^2\) norm on the frequency parameter plane uses normalized counting measure; the output \(L^4\) fourth power uses unnormalized counting measure. A nontrivial additive character is arbitrary. There is no claim of a global deficit-to-distance inequality, nor of a radius uniform as \(q\to\infty\).

## Proof

**1. Convolution fibers and exact normalization.** Orthogonality of additive characters gives
\[
\sum_{X,Y,T}|\mathcal E_q f(X,Y,T)|^4
=q^{-5}\sum_{S\in\mathbb F_q^3}|F_f(S)|^2,
\]
where \(F_f(S)\) sums \(f(u,v)f(u',v')\) over all **ordered** pairs constrained by
\(u+u'=S_1\), \(v+v'=S_2\), \(uv+u'v'=S_3\). Set
\[
(u,v)=(S_1/2+x,S_2/2+y),\quad
(u',v')=(S_1/2-x,S_2/2-y),\quad
w=(S_3-S_1S_2/2)/2.
\]
The constraint becomes \(xy=w\), with fiber cardinality
\[
r(w)=q-1+q\,\mathbf 1_{\{w=0\}}.
\]
Thus \(q^{-5}\sum_{S}r(w)^2=1+q^{-1}-q^{-2}\), exactly the stated sharp constant.

**2. Quadratic variation.** Put \(f_t=1+t h\). For each \(S\), expand
\[
F_{f_t}(S)=r(w)+tG_S+t^2H_S,
\]
where \(G_S=2\sum_{xy=w}h(S_1/2+x,S_2/2+y)\) and
\(H_S=\sum_{xy=w}h(S_1/2+x,S_2/2+y)h(S_1/2-x,S_2/2-y)\).
Let \(C_q=1+q^{-1}-q^{-2}\). For mean-zero \(h\), the \(t^2\) coefficient is
\[
B(h)=2C_q q^{-2}\sum|h|^2-q^{-5}
\left(\sum_S|G_S|^2+2\Re\sum_Sr(w)H_S\right).
\]
There is no linear term because the constant function is a sharp maximizer. Mean directions can be discarded: the global inequality makes \(B\) nonnegative, while \(\mathfrak D_q(c\mathbf1)=0\) for all complex \(c\), so both constant real directions belong to the kernel of this positive-semidefinite quadratic form and have zero mixed terms.

**3. Fourier diagonalization.** For a frequency \(k=(k_1,k_2)\), put
\[
K_k(w)=\sum_{xy=w}\psi(k_1x+k_2y).
\]
If \(k\ne0\), its finite-field Fourier transform in \(w\) equals \(0\) at dual frequency zero and has modulus \(q\) at every nonzero dual frequency: summing first in one of \(x,y\) yields the value \(q\psi(-k_1k_2/t)\) at dual frequency \(t\ne0\). Plancherel implies
\[
\sum_w|K_k(w)|^2=q(q-1),\qquad
\sum_S|G_S|^2=4q^3(q-1)\sum_{k\ne0}|\widehat h(k)|^2.
\]
The sum over \((S_1,S_2)\) also forces opposite frequencies in the mixed quadratic term. Its coefficient at \(k\ne0\) is
\[
T_k=q^2\sum_{x,y}r(xy)\psi(2k_1x+2k_2y)
=q^3\Bigl(q\bigl(\mathbf1_{\{k_1=0\}}+\mathbf1_{\{k_2=0\}}\bigr)-1\Bigr),
\]
because the constant part of \(r\) cancels and the union of the two coordinate axes has character sum
\(q\mathbf1_{\{k_1=0\}}+q\mathbf1_{\{k_2=0\}}-1\).
Write \(h=a+ib\) with real \(a,b\). Reality gives
\(\Re(\widehat h(k)\widehat h(-k))=|\widehat a(k)|^2-|\widehat b(k)|^2\).
Substitution into \(B\) yields
\[
\lambda_R(k)=2C_q-4(q-1)/q^2-2T_k/q^5,\quad
\lambda_I(k)=2C_q-4(q-1)/q^2+2T_k/q^5,
\]
which simplifies to the four coefficients asserted above.

**4. Spectral gap and equality directions.** Every nonzero Fourier mode belongs to precisely one of the two geometric classes. Since \(q\ge3\), the four positive values satisfy
\[
2-4/q+4/q^2<2-2/q<2-2/q+4/q^2<2.
\]
Orthogonality and Parseval prove the multiplicities, the exact least Rayleigh quotient and the classification of its equality directions. The quartic polynomial \(\mathfrak D_q(1+h)\) has higher-order terms uniformly bounded by a constant times \(\|h\|_2^3\) on a fixed finite-dimensional space, giving the stated local estimate. The character modulation \(f(u,v)\mapsto\psi(\alpha u+\beta v+\gamma uv)f(u,v)\) translates the output variables, preserving the full deficit and all eigenvalues.

## Verification

The accompanying `hessian_check.py` independently constructs all ordered additive-pair fibers, expands the full quartic deficit to second order, and compares it against direct finite-field Fourier coefficients. Run `python3 hessian_check.py`. It performs 88 tests in \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\), including random complex perturbations and pure real/imaginary axis/mixed Fourier modes. The \(\mathbb F_9\) test uses an explicit irreducible quadratic model, not integer arithmetic modulo nine. These finite tests corroborate but do not replace the general field-theoretic proof.

## Relationship to prior work

González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, Theorem 1.4, established the best endpoint constant and all extremizers of the finite-field hyperbolic paraboloid. Their equation (7.1) already provides the two-valued convolution-fiber sizes used here. The new statement is the **complete real Hessian spectrum, including four distinct curvature bands, exact multiplicities, sharp transverse local gap and least-stable directions**. Those assertions are not given by the sharp-constant or phase-classification theorem itself. More recent cone and moment-curve extension work concerns different surfaces; it is not a substitute for the split hyperbolic calculation.

## Limitations

The estimate is local around a fixed extremizer for each fixed field size. It does not provide a uniform neighborhood, a global stability estimate, or any corresponding inequality in characteristic two or for Euclidean hyperbolic surfaces. The proof and verifier establish no classification of higher-order terms beyond their analytically bounded contribution. An equivalent second-variation formula in unindexed literature cannot be ruled out.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first publicly available 2024-05-26), especially Theorem 1.4, equations (1.12), (1.13), (7.1), and Section 7.
2. C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600 (different surfaces; background only).
