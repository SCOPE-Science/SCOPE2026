# Sharp first-order stability constant for the silver inequality
## Finding
Let \(p_{\mathrm{sil}}=\log_2(1+\sqrt2)\), \(\rho=1+\sqrt2\), and
\[
F_p(z)=z^p+(1-z)^p+[z(1-z)]^p,\qquad 0\le z\le1.
\]
For \(p>p_{\mathrm{sil}}\), define the sharp normalized slack
\[
C_*(p)=\inf_{0<z<1}\frac{1-F_p(z)}{z(1-z)}.
\]
Then
\[
\lim_{p\downarrow p_{\mathrm{sil}}}\frac{C_*(p)}{p-p_{\mathrm{sil}}}
=8\log 2\,(\rho^{-1}+\rho^{-2})
=3.248289741210747\ldots.
\]
If \(z_p\) is any minimizer for \(C_*(p)\), then \(z_p\to1/2\) as \(p\downarrow p_{\mathrm{sil}}\). Consequently, for the ideal \(c-\varepsilon=1\) case of the slack estimate (52) in Ye--Liu, the coefficient \(1\) is a correct uniform coefficient but is not first-order sharp near the silver exponent: the exact normalized first-order coefficient is the constant above.

## Assumptions and scope
The statement concerns only the scalar silver splitting functional above and exponents \(p\downarrow p_{\mathrm{sil}}\) from above. It uses the silver inequality and its equality classification from Lemma B.8 of Ye--Liu: \(F_{p_{\mathrm{sil}}}(z)\le1\) on \([0,1]\), with equality exactly at \(z=0,1/2,1\). No claim is made about exact finite-horizon constants for gradient descent, about negative stepsizes, or about the perturbed \(c-\varepsilon\ne1\) scalar problem.

## Proof
For \(0<z<1\), set
\[
Q_p(z)=\frac{1-F_p(z)}{z(1-z)}.
\]
Because \(p>1\), the endpoint expansion \(1-(1-z)^p=pz+o(z)\), together with \(z^p=o(z)\), gives \(Q_p(z)\to p\) as \(z\downarrow0\); symmetry gives the same limit at \(z\uparrow1\). Thus \(Q_p\) extends continuously to \([0,1]\) by \(Q_p(0)=Q_p(1)=p\), so a minimizer exists.

At \(p=p_{\mathrm{sil}}\), Lemma B.8 gives \(Q_{p_{\mathrm{sil}}}(z)\ge0\) and its only interior zero is \(z=1/2\). For \(p>p_{\mathrm{sil}}\), every base in \((0,1)\) is raised to a larger exponent, so \(F_p(z)\le F_{p_{\mathrm{sil}}}(z)\) and hence \(Q_p(z)\ge Q_{p_{\mathrm{sil}}}(z)\).

Evaluating at the balanced split gives
\[
Q_p(1/2)=4\bigl(1-2^{1-p}-2^{-2p}\bigr).
\]
Since \(2^{-p_{\mathrm{sil}}}=\rho^{-1}\) and \(2\rho^{-1}+\rho^{-2}=1\), differentiation at \(p_{\mathrm{sil}}\) yields
\[
\left.\frac{d}{dp}Q_p(1/2)\right|_{p=p_{\mathrm{sil}}}
=8\log 2\,(\rho^{-1}+\rho^{-2})=:K.
\]
Therefore \(C_*(p)\le Q_p(1/2)=K(p-p_{\mathrm{sil}})+o(p-p_{\mathrm{sil}})\).

Let \(p_j\downarrow p_{\mathrm{sil}}\) and let \(z_j\) minimize \(Q_{p_j}\). The preceding upper bound and \(Q_{p_j}\ge Q_{p_{\mathrm{sil}}}\) imply \(Q_{p_{\mathrm{sil}}}(z_j)\to0\). Compactness and the equality classification force \(z_j\to1/2\). By the mean value theorem in the exponent, for some \(\xi_j\in(p_{\mathrm{sil}},p_j)\),
\[
Q_{p_j}(z_j)=Q_{p_{\mathrm{sil}}}(z_j)+(p_j-p_{\mathrm{sil}})D_{\xi_j}(z_j),
\]
where
\[
D_p(z)=\frac{-\partial_pF_p(z)}{z(1-z)}.
\]
The first term is nonnegative. Continuity of \(D_p(z)\) near \((p_{\mathrm{sil}},1/2)\) gives
\[
\liminf_{j\to\infty}\frac{C_*(p_j)}{p_j-p_{\mathrm{sil}}}
\ge D_{p_{\mathrm{sil}}}(1/2)=K.
\]
Together with the balanced-split upper bound, this proves the limit and the minimizer localization.

## Verification
The embedded `verify.py` recomputes \(p_{\mathrm{sil}}\), the algebraic identity \(2\rho^{-1}+\rho^{-2}=1\), the constant \(K\), and numerical minimizers of \(Q_p\) for shrinking positive offsets from \(p_{\mathrm{sil}}\). The numerical checks are sanity checks only; the proof above is analytic and does not infer the limit from finite sampling.

## Relationship to prior work
Ye and Liu introduce the silver inequality in Lemma B.8 and prove the perturbed slack estimate (52). In the ideal case \(c-\varepsilon=1\), their bound reads \(F_p(z)\le1-(p-p_{\mathrm{sil}})z(1-z)\). Their proof deliberately uses a uniform derivative lower bound and does not state the sharp first-order normalized constant. Jung--Cho--Yun develop an earlier checkpoint recursion with a different exponent and do not state this silver-slack asymptotic. Liu--Chen--Jiang--Wang prove balanced splitting for a separate recursive-composition Bellman kernel and a dyadic phase law; that result concerns optimized schedule composition rather than the quotient \(Q_p\) above and does not imply this first-order stability constant in the material inspected.

## Limitations
The result is local in the exponent and does not prove that \(z=1/2\) is the exact minimizer for every fixed \(p>p_{\mathrm{sil}}\). It also does not sharpen the full perturbed inequality with \(c-\varepsilon\ne1\), nor does it by itself improve the paper's stated subpolynomial lower-bound loss. A closely related September 2026 recursive-composition preprint was available through its abstract and detailed scientific summary, but its arXiv full text was not retrievable in the present source path; this leaves a residual literature-comparison risk, although its stated theorems concern a different Bellman kernel.

## References
1. Y. Ye and K. Liu, “Silver Rate Is (Almost) Optimal for Gradient Descent,” arXiv:2609.09152v1, 2026. Lemma B.8 and equation (52).
2. Y. Ye and K. Liu, “The Silver Rate Is (Almost) Tight,” public author announcement, 2026-09-07.
3. M. Jung, H. Cho, and C. Yun, “Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent,” arXiv:2609.04032, 2026.
4. Y. Liu, K. Chen, R. Jiang, and T. Wang, “Optimal Recursive Composition and Dyadic Phase Laws for Gradient Descent with Predetermined Stepsizes,” arXiv:2609.11788v1, 2026.
