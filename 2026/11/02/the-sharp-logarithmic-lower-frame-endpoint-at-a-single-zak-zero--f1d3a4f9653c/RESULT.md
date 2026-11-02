# The sharp logarithmic lower-frame endpoint at a single Zak zero

## Finding

For the unnormalized Gaussian \(g(t)=e^{-\pi t^2}\), define the critical-density Gabor atoms
\[
g_{m,n}(t)=e^{2\pi int}g(t-m),\qquad(m,n)\in\mathbb Z^2.
\]
Choose any deleted lattice atom \((a,b)\in\mathbb Z^2\). For \((m,n)\ne(a,b)\), put
\[
R_{m,n}=\sqrt{(m-a)^2+(n-b)^2},\qquad
c_{m,n}^{(\beta)}=\sqrt{1+R_{m,n}^2}\,[\log(e+R_{m,n})]^\beta.
\]

**Sharp theorem.** For every real \(\beta\), the family
\[
\{c_{m,n}^{(\beta)}g_{m,n}:(m,n)\in\mathbb Z^2\setminus\{(a,b)\}\}
\]
is a Riesz–Fischer sequence in \(L^2(\mathbb R)\), and hence a complete lower semi-frame, **if and only if \(\beta\ge1\)**. Precisely, there exists \(A_\beta>0\) such that every finitely supported family of complex scalars satisfies
\[
\left\|\sum_{(m,n)\ne(a,b)}u_{m,n}c_{m,n}^{(\beta)}g_{m,n}\right\|_2^2
\ge A_\beta\sum_{(m,n)\ne(a,b)}|u_{m,n}|^2
\]
exactly in the stated parameter range.

The threshold is not peculiar to the Gaussian. The same conclusion holds for **every** \(g\in L^2(\mathbb R)\) whose Zak transform \(\phi=Zg\) satisfies
\[
0<c\,\operatorname{dist}_{\mathbb T^2}(x,p)
\le |\phi(x)|\le
C\,\operatorname{dist}_{\mathbb T^2}(x,p)
\qquad\text{for a.e. }x\in\mathbb T^2
\]
for one point \(p\) and positive constants \(c,C\). Thus a single quantitatively simple Zak zero forces the critical logarithmic power \(1\) for these radial polynomial-logarithmic weights.

## Assumptions and scope

The torus \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\) carries normalized Lebesgue measure, and \(\operatorname{dist}_{\mathbb T^2}\) denotes its flat geodesic distance. The Zak transform convention is
\[
Zg(x,\xi)=\sum_{k\in\mathbb Z}g(x-k)e^{2\pi i k\xi},
\quad
Zg_{m,n}(x,\xi)=e^{2\pi i(nx-m\xi)}Zg(x,\xi).
\]
The transform is unitary from \(L^2(\mathbb R)\) onto \(L^2([0,1)^2)\). Only the modulus of its quasi-periodic representative is treated as a function on the torus.

The sharpness assertion concerns the specified family of weights, not arbitrary choices or pointwise-minimal individual weights. The Gaussian's unique simple Zak zero at \(p=(1/2,1/2)\), including its first-order theta expansion, is a known source theorem, not a newly proved property here.

## Proof

**1. Fourier reformulation.** By conjugating with a lattice time-frequency shift, it suffices to delete \((a,b)=(0,0)\), with weights indexed by the displacement from that point. Let
\[
\phi=Zg,\quad E_{m,n}(x,\xi)=e^{2\pi i(nx-m\xi)},\quad
w_{m,n}=\sqrt{1+m^2+n^2}[\log(e+\sqrt{m^2+n^2})]^\beta.
\]
For a finite polynomial \(F=\sum_{(m,n)\ne(0,0)}v_{m,n}E_{m,n}\), one has \(\int F=0\). Zak unitarity changes the Riesz–Fischer synthesis inequality into
\[
\tag{1}
\sum_{(m,n)\ne(0,0)}\frac{|v_{m,n}|^2}{w_{m,n}^2}
\le B\int_{\mathbb T^2}|\phi F|^2.
\]
Define the logarithmic Sobolev norm of a trigonometric polynomial \(\psi\) by
\[
\|\psi\|_{H_\beta}^2=
\sum_{k\in\mathbb Z^2}(1+|k|^2)[\log(e+|k|)]^{2\beta}
|\widehat\psi(k)|^2.
\]
The lower inequality (1) is equivalent, by Hilbert-space duality, to the **point-remainder Hardy inequality**
\[
\tag{2}
\int_{\mathbb T^2}
\frac{|\psi(x)-\psi(p)|^2}{|\phi(x)|^2}\,dx
\le B'\|\psi\|_{H_\beta}^2
\quad\text{for all trigonometric polynomials }\psi.
\]
Here is a proof of the equivalence, including its otherwise important constant. Given (2), subtract \(\psi(p)\) from \(\psi\), apply Cauchy–Schwarz to \(\int F\overline\psi\), and dualize the Fourier weights to obtain (1). Conversely, if (1) holds, then \(F\mapsto\int F\overline\psi\) is a bounded linear functional on the image space of mean-zero polynomials under multiplication by \(\phi\). Riesz representation supplies \(h\in L^2\) with controlled norm such that \(\overline\phi h=\psi-d\) for a constant \(d\), since the annihilator of mean-zero characters consists exactly of constants. Because \(|\phi(x)|\le C\operatorname{dist}(x,p)\) and \(\psi\) is continuous, the quotient \((\psi-d)/\phi\) can lie in \(L^2(\mathbb T^2)\) only when \(d=\psi(p)\): otherwise its squared modulus has a nonintegrable \(\operatorname{dist}(x,p)^{-2}\) singularity. Thus the representative is exactly \((\psi-\psi(p))/\phi\), proving (2) with the same uniform norm bound. This argument does not assume a priori that \(\psi(p)\) is a bounded trace on the unweighted critical Sobolev space.

**2. Endpoint sufficiency.** By the two-sided zero hypothesis, it is enough to prove
\[
\tag{3}
\int_{\mathbb T^2}\frac{|\psi(x)-\psi(p)|^2}{\operatorname{dist}(x,p)^2}\,dx
\lesssim \|\psi\|_{H_1}^2.
\]
Decompose the nonconstant Fourier part of \(\psi\) into dyadic square-frequency shells \(\psi_j\) supported where \(2^j\le|k|_\infty<2^{j+1}\), \(j\ge0\), and set \(a_j=2^j\|\psi_j\|_2\). Since such a shell has \(O(2^{2j})\) frequencies, Cauchy–Schwarz gives
\[
\|\psi_j\|_\infty\lesssim a_j,
\qquad
\|\nabla\psi_j\|_\infty\lesssim 2^j a_j.
\]
On the spatial annulus \(\operatorname{dist}(x,p)\asymp2^{-i}\), therefore,
\[
|\psi(x)-\psi(p)|
\lesssim\sum_{j\le i}2^{j-i}a_j+\sum_{j>i}a_j.
\]
Every annulus has uniformly bounded integral of \(\operatorname{dist}(x,p)^{-2}\). Young's convolution inequality gives
\[
\sum_i\left(\sum_{j\le i}2^{j-i}a_j\right)^2\lesssim\sum_j a_j^2.
\]
The classical discrete Hardy inequality, in its adjoint form, yields
\[
\sum_i\left(\sum_{j>i}a_j\right)^2\le4\sum_{j\ge1}j^2a_j^2.
\]
Consequently the left side of (3) is bounded by \(C\sum_j(1+j)^2a_j^2\), which is bounded by \(C'\|\psi\|_{H_1}^2\). This proves (1) at \(\beta=1\). Larger exponents increase the Fourier weights, hence also satisfy (1).

**3. Endpoint necessity.** For each \(j\ge1\), let
\[
\Lambda_j=\{(u,v)\in\mathbb Z^2:2^j\le u,v<2^{j+1}\},
\qquad
P_j(x)=2^{-2j}\sum_{(u,v)\in\Lambda_j}e^{2\pi i(u(x_1-p_1)+v(x_2-p_2))}.
\]
Thus \(P_j(p)=1\), \(|P_j(x)|\le1\), and the Fourier supports are disjoint. Write \(\psi_N=\sum_{j=1}^N P_j\). Each shell contains \(2^{2j}\) equal Fourier coefficients of size \(2^{-2j}\), so
\[
\tag{4}
\|\psi_N\|_{H_\beta}^2\asymp_\beta
\sum_{j=1}^N(1+j)^{2\beta}=o(N^3)
\qquad\text{if }\beta<1.
\]
For every sufficiently small \(x-p\), the normalized geometric-sum bound
\[
\left|2^{-j}\sum_{u=2^j}^{2^{j+1}-1}e^{2\pi iu(x_\ell-p_\ell)}\right|
\lesssim\min\{1,2^{-j}/|x_\ell-p_\ell|\}
\]
shows that on the square annulus \(2^{-i-2}\le|x-p|_\infty\le2^{-i-1}\), every \(P_j\) with \(j\ge i+K\) obeys \(|P_j(x)|\le1/2\), for one universal integer \(K\). Furthermore \(\operatorname{Re}(1-P_j(x))\ge0\) for every \(j\). Hence, for \(4\le i\le N-K\),
\[
|\psi_N(p)-\psi_N(x)|
\ge\operatorname{Re}(\psi_N(p)-\psi_N(x))
\ge\tfrac12(N-i-K+1).
\]
Those annuli are disjoint and each has a fixed strictly positive integral of \(|x-p|^{-2}\). Using \(|\phi(x)|\le C|x-p|\) gives
\[
\tag{5}
\int_{\mathbb T^2}\frac{|\psi_N(x)-\psi_N(p)|^2}{|\phi(x)|^2}\,dx
\gtrsim\sum_{i=4}^{N-K}(N-i-K+1)^2\gtrsim N^3.
\]
Equations (4)–(5) contradict (2) whenever \(\beta<1\). Thus \(\beta=1\) is the exact critical endpoint, not merely a sufficient cutoff.

**4. Completeness and the Gaussian.** For the general one-zero window, \(|\phi|^{-1}\notin L^2\) in two dimensions, while \((E_{m,n}-E_{m,n}(p))/\overline\phi\in L^2\) for every nonzero index. These functions provide biorthogonals, establishing minimality; the nonintegrability of \(1/\phi\) proves completeness after deletion by the Fourier annihilator argument. By the standard complete-Riesz–Fischer/lower-semi-frame equivalence, the same sharp threshold governs the lower semi-frame property. For the unnormalized Gaussian, the theta-function expansion around \(p=(1/2,1/2)\) is
\[
Zg(p+(u,v))=-\pi\theta_1'(0,e^{-\pi})(u+iv)+O(u^2+v^2),
\quad\theta_1'(0,e^{-\pi})\ne0.
\]
Together with the known uniqueness of this zero in one fundamental cell, it gives \(|Zg(x)|\asymp\operatorname{dist}_{\mathbb T^2}(x,p)\), so every preceding step applies. Arbitrary lattice-atom deletion is transferred to deletion of the origin by a unitary time-frequency shift, preserving the distance-based weights.

## Verification

The critical input is inequality (3), proved by explicit dyadic-frequency \(L^\infty\) and gradient estimates and the classical adjoint discrete Hardy bound. Sharpness is checked independently by the explicit block-polynomial sequence in equations (4)–(5). Both bounds are uniform for all trigonometric polynomials and every integer \(N\) in the counterfamily. No finite computation is used to certify any infinite-dimensional assertion. The proof separately verifies the duality constant and the nonintegrability of a nonzero point remainder in two dimensions.

## Relationship to prior work

Zikkos (2026) proved that suitable unspecified positive weights make the one-atom-deleted critical Gaussian Gabor system a complete Riesz–Fischer sequence and lower semi-frame. His summability sufficient condition concerns individual biorthogonal norms, not necessity of a polynomial-logarithmic weight threshold. The publicly archived result *Sharp logarithmic asymptotics of critical Gaussian Gabor biorthogonals* (2026) proves that those squared dual norms grow logarithmically, giving Zikkos's sufficient criterion for the present weights only when \(\beta>1\). The theorem here covers the **critical missing equality \(\beta=1\)** and proves failure for all \(\beta<1\); neither conclusion follows from that sufficient condition.

Hart, Heil, Katz and Northington (2025) supplied the full Zak-transform description and exactness of the one-atom-deleted system, including the Gaussian's unique simple zero. Their treatment concerns reproducing pairs, completeness and Schauder bases, not this polynomial-logarithmic Riesz–Fischer endpoint. The more general 1999 Nyquist-density Gabor summability paper of Lyubarskii and Seip is a significant potential overlap source; its accessible abstract discusses sharp summability in Hilbert scales but does not identify the present explicit weight criterion. Its full text was not available for comparison, so implicit prior coverage there remains an acknowledged risk.

## Limitations

The sharp parameter classification is for radial weights of the displayed polynomial-logarithmic form and windows whose Zak-transform modulus is globally comparable to distance from **one** zero. It does not characterize all possible weighting schemes, multiple or degenerate Zak zeros, or arbitrary lattice density. No independent validation has been performed. General endpoint Hardy inequalities may be classical in another normalization; the contribution under assessment is their sharp necessary-and-sufficient application to the concrete lower-frame weights and the single-zero window class.

## References

1. E. Zikkos, *The Gaussian Gabor system at the critical density is a weighted lower semi frame*, arXiv:2606.00764v1, first public 30 May 2026. https://arxiv.org/abs/2606.00764 .
2. L. Hart, C. Heil, I. Katz, M. Northington V, *Overcomplete Reproducing Pairs*, Journal of Fourier Analysis and Applications **31** (2025), article 58; DOI 10.1007/s00041-025-10190-7. https://doi.org/10.1007/s00041-025-10190-7 .
3. *Sharp logarithmic asymptotics of critical Gaussian Gabor biorthogonals* (2026), public mathematical research record. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-logarithmic-asymptotics-of-critical-gaussian-gabor-biortho--9a4e258e09c2 .
4. Yu. I. Lyubarskii and K. Seip, *Convergence and summability of Gabor expansions at the Nyquist density*, Journal of Fourier Analysis and Applications **5** (1999), 127–157; DOI 10.1007/BF01261606.
