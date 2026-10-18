# A sharp logarithmic-tail and oversampling law for bilateral Gaussian singular gaps

## Finding

Let integers \(s,t\geq2\) be fixed, and let \(G\in\mathbb R^{s\times2}\) and \(H\in\mathbb R^{t\times2}\) have mutually independent standard real Gaussian entries. For every \(0<\varepsilon<1\), set
\[
B_\varepsilon=G\operatorname{diag}(1,\varepsilon)H^{\mathsf T},\qquad
D_\varepsilon=\frac{\sigma_2(B_\varepsilon)}{\varepsilon\sigma_1(B_\varepsilon)}.
\]
Here \(\sigma_1\geq\sigma_2>0\) are the two positive singular values, almost surely. The normalized **observed singular-gap ratio** \(D_\varepsilon\) has the following almost-sure and distributional limit as the underlying matrix approaches rank one:
\[
D_\varepsilon\longrightarrow W_{s,t}=T_s T_t,\qquad
T_d\overset{\mathrm d}=\frac{\chi_{d-1}}{\chi_d},
\]
where each displayed chi variable is independent of the others. The ratio \(T_d\) has density
\[
f_d(x)=\frac{2\Gamma(d-\tfrac12)}{\Gamma((d-1)/2)\Gamma(d/2)}
\frac{x^{d-2}}{(1+x^2)^{d-1/2}},\qquad x>0,
\]
and survival-tail constant
\[
 c_d=\frac{2\Gamma(d-\tfrac12)}{d\,\Gamma((d-1)/2)\Gamma(d/2)},\qquad
\mathbb P(T_d>x)\sim c_dx^{-d}.
\]
Write
\[
 M_d(p)=\frac{\Gamma((d-1+p)/2)\Gamma((d-p)/2)}{\Gamma((d-1)/2)\Gamma(d/2)}
 \quad(0<p<d).
\]
The **exact leading singular-gap failure tails** of the limit are
\[
\mathbb P(W_{s,t}>x)\sim
\begin{cases}
 c_sM_t(s)x^{-s},&s<t,\\
 c_tM_s(t)x^{-t},&t<s,\\
 s c_s^2 x^{-s}\log x,&s=t.
\end{cases}
\qquad(x\to\infty).
\]
Every positive moment satisfies
\[
 \mathbb E W_{s,t}^p= M_s(p)M_t(p)<\infty
 \quad\Longleftrightarrow\quad 0<p<\min(s,t).
\]
In particular, finite limiting mean-square singular-gap distortion occurs **exactly when both sketch dimensions are at least three**, and then
\[
 \mathbb EW_{s,t}^2=\frac{(s-1)(t-1)}{(s-2)(t-2)}.
\]
For the critical smallest sketches, the distinction is sharp:
\[
 \mathbb P(W_{2,2}>x)\sim\frac{\log x}{2x^2},\qquad
 \mathbb P(W_{2,3}>x)\sim\frac1{x^2},\qquad
 \mathbb EW_{3,3}^2=4.
\]
For any fixed \(\varepsilon>0\), the measured ratio is bounded by \(D_\varepsilon\leq\varepsilon^{-1}\) and all its moments are finite. Nevertheless, for every \(p\geq\min(s,t)\),
\[
 \liminf_{\varepsilon\downarrow0}\mathbb E D_\varepsilon^p=+\infty.
\]
Thus the moment obstruction concerns uniform weak-gap accuracy, not an infinite expectation at a fixed nonzero spectral gap.

## Assumptions and scope

All matrices and Gaussian variables are **real**. The dimensions \(s,t\ge2\) remain fixed as \(\varepsilon\downarrow0\). The two random sketches are independent. Singular-value ratios make any deterministic positive scalar normalizations of the Gaussian sketches irrelevant. For any fixed rank-two matrix with nonzero singular values \(1,\varepsilon\), independent Gaussian maps restricted to its left and right singular subspaces give this model by rotational invariance. There is no claim of an optimal choice of practical sketch dimensions for an arbitrary spectrum, nor of a finite-\(\varepsilon\) tail asymptotic uniform in the failure threshold.

## Proof

**Exact rank-two identity and limit.** Write the two columns of \(G\) as \(g_1,g_2\) and of \(H\) as \(h_1,h_2\). Almost surely they have rank two. Put
\[
 a=\|g_1\|^2\|h_1\|^2,\quad b=(g_1^{\mathsf T}g_2)(h_1^{\mathsf T}h_2),\quad c=\|g_2\|^2\|h_2\|^2,
\]
\[
 \Delta_G=\|g_1\|^2\|g_2\|^2-(g_1^{\mathsf T}g_2)^2,\qquad
 \Delta_H=\|h_1\|^2\|h_2\|^2-(h_1^{\mathsf T}h_2)^2.
\]
Direct expansion yields \(\|B_\varepsilon\|_F^2=a+2\varepsilon b+\varepsilon^2c\). The squared product of its two nonzero singular values is exactly \(\varepsilon^2\Delta_G\Delta_H\), by the Gram determinant/Cauchy–Binet identity for the rank-two factorization. Consequently,
\[
 D_\varepsilon=\frac{\sqrt{\Delta_G\Delta_H}}{\sigma_1(B_\varepsilon)^2}.
\]
Since \(B_\varepsilon\to g_1h_1^{\mathsf T}\), continuity of singular values gives \(\sigma_1(B_\varepsilon)^2\to a>0\) almost surely. Decomposing each second column orthogonally to the first gives
\[
D_\varepsilon\to
\frac{\|P_{g_1^\perp}g_2\|}{\|g_1\|}
\frac{\|P_{h_1^\perp}h_2\|}{\|h_1\|}.
\]
Given \(g_1\), Gaussian rotational invariance makes \(\|P_{g_1^\perp}g_2\|\) a \(\chi_{s-1}\) variable with a conditional distribution not depending on \(g_1\). It is therefore independent of \(\|g_1\|\sim\chi_s\). The same argument applies independently to \(H\). This proves the claimed product law, including almost-sure convergence on the Gaussian coupling.

**Density and moments.** For independent \(U\sim\chi_{d-1}\), \(V\sim\chi_d\), use their gamma-integral densities and the substitution \((U,V)=(xv,v)\) with Jacobian \(v\). Integrating over \(v>0\) yields the stated \(f_d\). Separating the numerator and denominator before integration yields
\[
 \mathbb ET_d^p=\mathbb E U^p\mathbb EV^{-p}=M_d(p).
\]
The inverse-chi integral converges at zero precisely for \(p<d\); it diverges for \(p\ge d\), including equality. Independence gives the full product-moment assertion. At \(p=2\) the chi-square mean and inverse mean give \(\mathbb ET_d^2=(d-1)/(d-2)\) for \(d>2\).

**Sharp tails.** The explicit density has \(f_d(x)\sim d c_dx^{-d-1}\), so integration gives \(\mathbb P(T_d>x)\sim c_dx^{-d}\). If \(s<t\), condition on \(T_t\): the bound \(\mathbb P(T_s>y)\leq C_sy^{-s}\) holds for all positive \(y\), and \(\mathbb ET_t^s<\infty\). Dominated convergence applied to \(x^s\mathbb P(T_s>x/T_t)\) gives \(c_sM_t(s)\). The other unequal case is symmetric. If \(s=t=d\), split the conditioning integral into \(T_d<1\), \(1\leq T_d\leq x/K\), and \(T_d>x/K\). For any fixed large \(K\), the middle portion has leading value
\[
 c_dx^{-d}\int_1^{x/K}u^d f_d(u)\,du
 \sim d c_d^2x^{-d}\log x,
\]
while the two outer portions are \(O_K(x^{-d})\), and the approximation on the middle portion has relative error tending to zero as \(K\to\infty\). This proves the logarithm and its coefficient. In particular \(c_2=1/2\), \(M_3(2)=2\), giving the explicit critical examples.

**Moments of finite-gap ratios.** Since \(\sigma_2\leq\sigma_1\), \(0<D_\varepsilon\leq\varepsilon^{-1}\) and every finite-\(\varepsilon\) moment exists. Almost-sure convergence followed by Fatou's lemma for any sequence \(\varepsilon\downarrow0\) forces divergent limiting expected \(p\)-th powers when \(\mathbb EW_{s,t}^p=\infty\). No claim of convergence of the finite-\(\varepsilon\) moments to \(M_s(p)M_t(p)\) is made in the integrable regime.

## Verification

The standalone standard-library-only program `verify.py` checks the exact rank-two singular-value/Gram identity and its small-gap limit on seeded Gaussian examples, the gamma-function tail constants, finite second-moment constants, and the \((2,2)\) log-tail coefficient by independent numerical integration. Run `python3 verify.py`; its successful test count is 1520. These are finite falsification tests. All asymptotics and moment thresholds follow from the mathematical proof above, not the test count.

## Relationship to prior work

Meier and Nakatsukasa, *Fast randomized numerical rank estimation for numerically low-rank matrices* (arXiv:2105.07388, first submitted 2021-05-16), motivate two-sided sketches and singular-gap detection. Their full-text §§3.2, 4, 5 and appendix discuss bounds, algorithmic oversampling and estimated singular values, not the explicit rank-two Gaussian weak-gap law, moment boundary or equal-dimension logarithmic tail. In particular their recommended practical algorithms intentionally oversample; this theorem analyzes a minimal rank-two benchmark and does not contradict that advice.

Akemann, Ipsen and Kieburg, *Products of Rectangular Random Matrices: Singular Values and Progressive Scattering* (arXiv:1307.7560), derive finite-dimensional product singular-value formulae for **complex** Gaussian matrices with no deterministic near-rank-one diagonal deformation of the form here. Their explicitly inspected §§I–II and conclusions do not state the real weak-gap product-chi limit; related random-product theory is relevant prior mathematical machinery, not claimed as new. Burda et al. (arXiv:1007.3594) study large-dimensional singular-value limits for undeformed rectangular Gaussian products. Their abstract alone is insufficient to rule out other formulations; priority risk remains. The elementary gamma and regularly varying tail manipulations used in the proof are standard and are not claimed independently original.

## Limitations

The result is for a **fixed rank-two signal**, independent real Gaussian sketches, fixed output dimensions, an infinitesimal positive trailing singular value, and a **ratio of two sketched singular values**. It does not give the finite-threshold accuracy of a rank estimator, make a claim about singular values individually, or extend without proof to complex, non-Gaussian, dependent, multi-rank, or growing-dimensional sketches. The distributional limit cannot be substituted into divergent moments without the Fatou argument; even in the finite-moment region no convergence of moments for finite-gap ratios is asserted. Independent scientific or priority validation has not been performed.

## References

1. M. Meier and Y. Nakatsukasa, *Fast randomized numerical rank estimation for numerically low-rank matrices*, arXiv:2105.07388 (original preprint 2021-05-16; revision 2024-01-05).
2. G. Akemann, J. R. Ipsen and M. Kieburg, *Products of Rectangular Random Matrices: Singular Values and Progressive Scattering*, arXiv:1307.7560 (2013).
3. Z. Burda, A. Jarosz, G. Livan, M. A. Nowak and A. Swiech, *Eigenvalues and Singular Values of Products of Rectangular Gaussian Random Matrices*, arXiv:1007.3594 (2010).
