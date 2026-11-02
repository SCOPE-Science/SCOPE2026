# Sharp sixth-order local stability of the Chang–Marshall extremizer orbit

## Finding

For every integer \(m\geq1\), the best local stability exponent in the normalized Chang–Marshall inequality on the Dirichlet unit sphere of functions vanishing to order at least \(m\) is six. More precisely, put
\[
\mathcal D_m=\left\{f(z)=\sum_{n\geq m}a_nz^n:\ D(f):=\sum_{n\geq m}n|a_n|^2<\infty\right\},\quad
J(f)=\int_{\mathbb T}\exp(|f|^2)\,d\mu,
\]
where \(\mu\) is normalized circular measure, and let \(\mathcal M_m=\{e^{i\theta}z^m/\sqrt m:\theta\in\mathbb R\}\). Define the Dirichlet distance \(d_m(f)=\inf_{g\in\mathcal M_m}\sqrt{D(f-g)}\). Then
\[
\boxed{\displaystyle
\lim_{\rho\downarrow0}\ \inf_{\substack{f\in\mathcal D_m,\ D(f)=1\\0<d_m(f)<\rho}}
\frac{e^{1/m}-J(f)}{d_m(f)^6}
=\frac{e^{1/m}}{24m(m+1)^3}.}
\]
In particular, for \(m=1\), the sharp local constant is \(e/192\) in the full infinite-dimensional Dirichlet space; the exponent six cannot be reduced. The constant is approached by the explicit four-mode family displayed below. This is a local stability statement, not a global sixth-power inequality.

## Assumptions and scope

All functions are complex analytic in the open unit disk and have almost-everywhere radial boundary values. The Hilbert norm is exactly \(\|f\|_{\mathcal D}^2=D(f)=\int_{\mathbb D}|f'(z)|^2\,dA(z)/\pi\). All comparisons are on \(D(f)=1\); no compactness assumption, finite-degree bound, or coefficient reality assumption is imposed. The source's sharp inequality \(J(f)\leq e^{D(f)/m}\) for \(D(f)\leq1\) and vanishing order at least \(m\) ensures the deficit is nonnegative. The result concerns the approach to the phase orbit \(\mathcal M_m\) in this norm.

## Proof

**1. An analytic chart and the full Hessian.** Using the phase symmetry, choose the coefficient of \(z^m\) positive. Near \(z^m/\sqrt m\), there is a unique chart
\[
F(t,w)(z)=\frac{z^m/\sqrt m+t z^{m+1}+w(z)}{\sqrt{1+(m+1)|t|^2+\|w\|_{\mathcal D}^2}},\qquad
w(z)=\sum_{j\geq2}w_jz^{m+j}.
\]
This satisfies \(D(F(t,w))=1\). Write \(\Phi(t,w)=e^{-1/m}J(F(t,w))\). The functional is real analytic near the chart origin in the complex Dirichlet Hilbert topology, interpreted as a real Hilbert space. Indeed, for small Dirichlet perturbations \(h\), the critical Chang–Marshall estimate applied to a rescaling of \(h\) bounds \(\int\exp(C|h|^2)\,d\mu\) uniformly for a fixed \(C>1\). Hölder's inequality controls the remaining bounded monomial and linear terms; the exponential power series and all local Fréchet derivatives consequently converge normally on a sufficiently small Hilbert ball. The chart denominator is analytic there as well.

At \(t=0\), the constant, linear, and quadratic Fourier coefficients of the integrand give
\[
\Phi(0,w)=1-\frac1m\sum_{j\geq2}(j-1)|w_j|^2+O(\|w\|_{\mathcal D}^3).
\]
Since \((j-1)/(m(m+j))\geq1/[m(m+2)]\) for \(j\geq2\), the Hessian on the closed stable subspace \(\{w\}\) is boundedly invertible and uniformly negative. The real-analytic implicit-function theorem therefore supplies a unique small analytic branch \(w=W(t)\), critical in every stable direction, and constants \(\epsilon,\gamma>0\) such that
\[
\Phi(t,w)\leq\Phi(t,W(t))-\gamma\|w-W(t)\|_{\mathcal D}^2
\]
whenever \(|t|+\|w\|_{\mathcal D}<\epsilon\). This follows by integrating the negative-definite Hessian along the line segment from \(W(t)\) to \(w\); hence it holds in the infinite-dimensional space, not only among polynomials.

**2. Symmetry and the precise normal form.** Disk rotations \(z\mapsto e^{i\theta}z\), followed by a compensating constant phase, act on the chart by \(t\mapsto e^{i\theta}t\), \(w_j\mapsto e^{ij\theta}w_j\). Uniqueness of \(W\), together with complex conjugation, implies that each real-analytic coefficient \(W_j(t)\) is a sum of terms \(t^j|t|^{2k}\) with real coefficients. In particular,
\[
W_2(t)=c_m t^2+O(|t|^4),\qquad
W_3(t)=d_m t^3+O(|t|^5),\qquad
W_j(t)=O_j(|t|^j)\ \ (j\geq4),
\]
and the sum of all modes of index at least four has Dirichlet norm \(O(|t|^4)\), by the Hilbert-valued analytic expansion. The values of \(c_m,d_m\) follow from the exact sixth-order Fourier calculation below. For real \(t,c,d\), consider
\[
F_{m,t,c,d}(z)=\frac{z^m/\sqrt m+t z^{m+1}+ct^2z^{m+2}+dt^3z^{m+3}}{\sqrt{1+(m+1)t^2+(m+2)c^2t^4+(m+3)d^2t^6}}.
\]
Let \(c_m=(2m+1)/(2\sqrt m)\) and \(d_m=m+5/4+1/(3m)\). Directly multiply the finite Fourier series for \(|F_{m,t,c,d}|^2-1/m\), expand its exponential to sixth order, and take the zero Fourier coefficient. This yields the exact coefficients
\[
e^{-1/m}J(F_{m,t,c,d})
=1-\frac{(c-c_m)^2}{m}t^4+O(t^6),
\]
and, on the unique fourth-order critical branch \(c=c_m\),
\[
e^{-1/m}J(F_{m,t,c_m,d})
=1-\left(\frac{1}{24m}+\frac2m(d-d_m)^2\right)t^6+O(t^8).
\]
The coefficients can be checked by the supplied exact Fourier-series program. The stable critical equation forces \(W_2\)'s leading coefficient to equal \(c_m\), and then \(W_3\)'s to equal \(d_m\). Terms of \(W_j\) with \(j\geq4\) first influence the zero Fourier coefficient at order eight; the order-four correction to \(W_2\) also first influences it at order eight because the fourth-order square is already minimized at \(c_m\). Consequently,
\[
\Phi(t,W(t))=1-\frac{|t|^6}{24m}+O(|t|^8).
\]
(The weighted-Hilbert analytic expansion justifies these remainder estimates uniformly and all higher-mode exclusions.)

**3. Conversion to sharp Hilbert distance.** The chosen phase of \(F(t,w)\) is optimal when measuring distance to the monomial orbit. With \(s=(m+1)|t|^2+\|w\|_{\mathcal D}^2\), one has the exact identity
\[
d_m(F(t,w))^2=2\left(1-\frac1{\sqrt{1+s}}\right).
\]
Along \(w=W(t)\), this is \((m+1)|t|^2+O(|t|^4)\). The previous steps imply the lower deficit bound
\[
e^{1/m}-J(F(t,w))\geq e^{1/m}\left(\frac{|t|^6}{24m}+O(|t|^8)+\gamma\|w-W(t)\|_{\mathcal D}^2\right).
\]
To justify the claimed infimum, consider any sequence approaching \(\mathcal M_m\). If the deficit-to-sixth-distance quotient tends to infinity, it is irrelevant to the lower limit. Otherwise the displayed bound forces \(\|w-W(t)\|_{\mathcal D}=O(d_m(F(t,w))^3)\). Using \(\|W(t)\|_{\mathcal D}=O(|t|^2)\), the exact distance identity then implies \(d_m(F(t,w))^2=(m+1)|t|^2+O(d_m(F(t,w))^4)\). The preceding lower bound gives the required \(\liminf\) of \(e^{1/m}/[24m(m+1)^3]\).

For the reverse inequality, set \(c=c_m\), \(d=d_m\) in \(F_{m,t,c,d}\) and let real \(t\to0\). The sixth-order coefficient and distance expansion give the same ratio in the limit, proving optimality simultaneously for every \(m\geq1\). This explicit family also rules out any local positive stability bound with exponent strictly below six. \(\square\)

## Verification

The included standard-library Python program `verify.py` reconstructs the exponential Fourier zero-mode series up to degree six with exact rational arithmetic, after choosing square indices to make \(\sqrt m\) rational. It checks vanishing quadratic and fourth-order terms at \(c_m\), the coefficient \(-1/(24m)\), and exact quadratic response under unit changes of the optimizing coefficients. A successful run prints `CHECK_OK`. All-degree coefficient identities are provided analytically above; the finite checks do not certify the infinite-dimensional implicit-function step, which is supplied by the proof.

## Relationship to prior work

Frank and Ivanisvili (2026), arXiv:2610.15378v1, proved the sharp global Chang–Marshall inequality and identified all monomial equality cases for every vanishing order. Their result is used as a critical exponential integrability estimate; their theorem does not quantify the local deficit at sixth order. Andreev and Matheson (1994) studied extremal functions and local maximality near the first monomial, but the inspected arguments do not provide the present all-order sharp infinite-dimensional stability limit. The novelty asserted here is the complete sharp lower bound, together with the exact stable-mode reduction; it is not a claim to have first identified the extremizers or the general second-variation method.

## Limitations

The result is local as the Dirichlet distance tends to zero and gives no global modulus of stability, uniformity in \(m\), explicit neighborhood size, or nonlinear dynamics. The coefficient \(e^{1/m}/[24m(m+1)^3]\) is sharp only with the specified Dirichlet normalization and phase-orbit metric. The real-analytic implicit-function reduction is nonconstructive outside the displayed leading coefficients. Historical priority beyond the inspected literature and independent expert validation remain open.

## References

1. Rupert L. Frank and Paata Ivanisvili, *The sharp constant in the Chang–Marshall inequality*, arXiv:2610.15378v1 (first made public October 11, 2026), https://arxiv.org/abs/2610.15378 .
2. Valentin Andreev and Alec Matheson, *Extremal functions and the Chang–Marshall inequality*, Pacific Journal of Mathematics 162 (1994), 233–246, https://msp.org/pjm/1994/162-2/pjm-v162-n2-p02-s.pdf .
