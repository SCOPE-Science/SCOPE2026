# Exact critical-bias crossover for probabilistic parking preferences

## Finding

Let \(Q_{n,p}\) denote the conditional law of the last car's preferred spot when \(n\) initially independent uniform preferences on \(\{1,\ldots,n\}\) are processed by the probabilistic parking protocol: a car whose preferred spot is occupied scans to the right with probability \(p\), and otherwise scans to the left; unsuccessful scans cause failure. Condition on all cars parking successfully. Let \(U_n\) be uniform on \(\{1,\ldots,n\}\).

**Theorem.** For any fixed real \(\lambda\), put \(p_n=1/2+\lambda/\sqrt n\) (for all sufficiently large \(n\), so \(p_n\in[0,1]\)). Then
\[
\boxed{\displaystyle\lim_{n\to\infty} n\,\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}=\frac{1+\sqrt{1+32\lambda^2/\pi}}2.}
\]
In particular the unbiased coefficient is exactly one; the nontrivial transition occurs at bias of order \(n^{-1/2}\), and its limiting coefficient is an explicit nonlinear function of the rescaled bias.

A structural refinement yields the result. Regard the signed measure
\[
\nu_n=n\sum_{j=1}^n\bigl(Q_{n,p_n}(j)-1/n\bigr)\,\delta_{j/n}.
\]
It converges weakly as a finite signed measure on \([0,1]\) to
\[
\nu_\lambda=\tfrac12\delta_0+\tfrac12\delta_1+\biggl[-1+\frac{4\lambda(1-2x)}{\sqrt{2\pi x(1-x)}}\biggr]dx,
\]
and the total-variation norms of these signed measures also converge. Consequently the limit stated above follows by integration.

## Assumptions and scope

The parking protocol, conditioning event, and law \(Q_{n,p}\) are precisely those in Durmić–Han–Harris–Ribeiro–Yin, *Probabilistic Parking Functions* (2022 preprint; 2023 journal publication). Each choice of left/right direction uses the same parameter \(p\); failure means leaving the finite row without finding a vacant spot in the selected direction. The statement concerns a fixed \(\lambda\in\mathbb R\) while \(n\to\infty\); it does not assert uniform convergence over growing \(\lambda\). Total variation between discrete probability measures is half the sum of absolute mass differences. Signed-measure variation here is the full absolute mass, without the factor one-half.

## Proof

**1. Exact source identity.** Put \(s=n-j\), with \(s=0,\ldots,n-1\), and define the nonnegative symmetric coefficients
\[
a_{n,s}=\frac{\binom{n-1}{s}(n-s)^{n-s-2}(s+1)^{s-1}}{(n+1)^{n-1}},
\qquad
D_{n,s}=\sum_{t<s}a_{n,t}-\sum_{t>s}a_{n,t}.
\]
All bases are positive, so negative integer powers at the endpoints are unambiguous. Theorem 3 of the cited 2022 work, with its exact normalization, is equivalent to
\[
Q_{n,p}(j)=\frac1{n+1}+\frac{a_{n,n-j}}2+(p-\tfrac12)D_{n,n-j}.
\tag{1}
\]
Also \(a_{n,s}=a_{n,n-1-s}\) and \(\sum_{s=0}^{n-1}a_{n,s}=2/(n+1)\). The latter follows either from normalization of (1) at \(p=1/2\), or directly from the finite Abel convolution in the source.

**2. Uniform local asymptotics and endpoint bounds.** With \(k=s+1\), \(\ell=n-s\) and \(N=n+1=k+\ell\), exactly
\[
a_{n,s}=\binom Nk\frac{k^{k-1}\ell^{\ell-1}}{nN^{N-1}}.
\tag{2}
\]
Uniform Stirling estimates on every closed subinterval of \((0,1)\) yield
\[
n^{5/2}a_{n,\lfloor ny\rfloor}\longrightarrow\frac{1}{\sqrt{2\pi}[y(1-y)]^{3/2}}.
\tag{3}
\]
The upper/lower Stirling inequalities, including their endpoint versions, moreover give an absolute constant \(C\) such that, for all \(n\ge2\),
\[
0\le a_{n,s}\le\frac{C\sqrt n}{[(s+1)(n-s)]^{3/2}}
\le\frac{C'}{n\min(s+1,n-s)^{3/2}}.
\tag{4}
\]
Symmetry implies \(D_{n,s}=-D_{n,n-1-s}\) and \(D_{n,s+1}-D_{n,s}=a_{n,s}+a_{n,s+1}\). Summing from the midpoint, (3) gives, uniformly for \(y\) in compact subsets of \((0,1)\),
\[
n^{3/2}D_{n,\lfloor ny\rfloor}\longrightarrow
\frac{4(2y-1)}{\sqrt{2\pi y(1-y)}}.
\tag{5}
\]
The same midpoint summation with (4) proves
\[
|D_{n,s}|\le \frac{C''}{n\sqrt{\min(s+1,n-s)}}.
\tag{6}
\]
For clarity, differentiating the right side of (5) gives exactly \(2/[\sqrt{2\pi}\{y(1-y)\}^{3/2}]\), the continuum increment of \(n^{3/2}D\); symmetry sets its value to zero at \(y=1/2\). Thus the normalization constant in (5) is fixed, not inferred numerically.

**3. Bulk and boundary.** Since \(p_n-1/2=\lambda/\sqrt n\), (1), (3), and (5) imply on compact subintervals of \((0,1)\) that
\[
n^2\bigl(Q_{n,p_n}(\lfloor nx\rfloor)-1/n\bigr)
\longrightarrow h_\lambda(x):=-1+\frac{4\lambda(1-2x)}{\sqrt{2\pi x(1-x)}}.
\tag{7}
\]
The constant \(-1\) comes from the exact difference \(1/(n+1)-1/n=-1/[n(n+1)]\). The contribution of \(a_{n,s}/2\) vanishes in the bulk at this scaling.

For the endpoints, the positive measures \(n\sum_j (a_{n,n-j}/2)\delta_{j/n}\) have total mass \(n/(n+1)\). By symmetry and bound (4), their mass off every fixed endpoint collar vanishes, so they converge to \((\delta_0+\delta_1)/2\). The baseline \(-1/[n(n+1)]\) contributes \(-dx\). The bias measure is \(\lambda\sqrt n\sum_jD_{n,n-j}\delta_{j/n}\); by (5) it converges in the interior to \(4\lambda(1-2x)/\sqrt{2\pi x(1-x)}\,dx\). Its total absolute mass within collars of width \(\varepsilon\) is at most \(C|\lambda|\sqrt\varepsilon\), by (6), so there are no hidden boundary atoms. This proves weak convergence to \(\nu_\lambda\).

To establish **convergence of variation**, apply the elementary bound \(\bigl||u+v|-|u|\bigr|\le|v|\) separately to the endpoint collars: (4) and symmetry show that the positive \(a\)-contribution there has total mass approaching one as the collar width then tends to zero, while the baseline absolute mass is at most \(2\varepsilon+o(1)\), and the bias absolute mass is \(O(|\lambda|\sqrt\varepsilon)\). In the complement, uniform convergence (7) gives the Riemann-integral limit of the absolute values. Letting \(\varepsilon\downarrow0\) yields
\[
\lim_{n\to\infty}2n\|Q_{n,p_n}-U_n\|_{\mathrm{TV}}
=1+\int_0^1|h_\lambda(x)|\,dx.
\tag{8}
\]
This step ensures that weak convergence alone is not incorrectly used to infer norm convergence.

**4. Closed-form integral.** The integral is even in \(\lambda\) by reflection \(x\mapsto1-x\). For \(\lambda>0\), the function \(h_\lambda\) changes sign exactly once, at
\[
x_\lambda=\frac12\left(1-\sqrt{\frac{\pi}{\pi+32\lambda^2}}\right).
\]
Using \(\int_0^x(1-2t)/\sqrt{t(1-t)}\,dt=2\sqrt{x(1-x)}\), direct integration gives
\[
\int_0^1|h_\lambda(x)|\,dx
=\sqrt{1+32\lambda^2/\pi}.
\]
At \(\lambda=0\) the integral is one. Substitute into (8) to obtain the theorem for all real \(\lambda\).

## Verification

Run `python verify_parking_crossover.py` in an environment with Python, NumPy, and SciPy. The checker reconstructs the distribution independently by exact rational enumeration of all preference vectors and coin branches for \(2\le n\le5\) and five rational coin biases. It compares the result with formula (1) and tests exact symmetry and mass normalization. It then checks convergence toward the claimed coefficient numerically at three increasing sizes for five critical-window biases. The program prints `PASS: 43 exact and asymptotic reproducibility checks` on successful execution. The finite enumerations and asymptotic numerical checks corroborate but do not prove the infinite limit; the proof is in Steps 1–4.

## Relationship to prior work

Durmić, Han, Harris, Ribeiro, and Yin's original Theorem 3 supplies the exact last-preference formula; their Theorems 5–6 establish only order-of-magnitude total-variation rates for fixed \(p=1/2\) and fixed \(p\ne1/2\). Their source does not give the critical sequence \(p_n=1/2+\lambda/\sqrt n\), its explicit crossover constant, or the signed bulk/endpoint decomposition. Harris, Ribeiro, and Yin (2025) derive further inequalities for \((m,n)\)-parking functions, including the strictly underfilled regime; their Theorem 3.3 gives bounds rather than the claimed critical-limit identity. Bellin's work concerns initial entries of uniform classical parking functions rather than the same coin-bias critical crossover. The new claim is a nontrivial uniform asymptotic consequence of the existing exact law, **not a new finite distribution formula**. Historical priority is not asserted absolutely.

## Limitations

This statement requires exactly as many cars as spaces, conditional successful parking, and a fixed real critical parameter \(\lambda\). It does not cover the underfilled \(m/n\to c<1\) regime, convergence rates for the displayed limit, or biases outside the \(n^{-1/2}\) critical window. The original finite probability identity is prior literature. Numerical tests alone cannot establish the limiting theorem. Independent verification of the mathematical proof or research priority has not been performed.

## References

1. I. Durmić, A. Han, P. E. Harris, R. Ribeiro, M. Yin, *Probabilistic Parking Functions*, arXiv:2211.00536 (first posted 2022-11-01); *Electronic Journal of Combinatorics* 30 (2023), P3.18. Theorems 3, 5, 6 and their proofs. https://arxiv.org/abs/2211.00536
2. P. E. Harris, R. Ribeiro, M. Yin, *Probabilistic (m,n)-Parking Functions*, arXiv:2502.00269 (first posted 2025-02-01); *Electronic Journal of Combinatorics* 32 (2025), P4.39. Sections 2–3, especially Theorem 3.3. https://arxiv.org/abs/2502.00269
3. E. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, *Journal of Applied Probability* 60 (2023), 1201–1218. https://doi.org/10.1017/jpr.2022.131
