# Geometric singular values and a heat-spectrum boundary for quadratic Fock weighted compositions

## Finding
Let \(\mathcal F^2\) be the Bargmann–Fock space of entire functions with norm
\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
For \(a,b\in\mathbb C\) with \(0<|a|<1\), define on polynomials
\[
(T_{a,b}f)(z)=e^{b z^2/2}f(az),\qquad \rho=|a|,\quad \beta=|b|,\quad c=1-\rho^2.
\]
**Quadratic weighted-composition spectral phase diagram.** The following statements hold.

1. \(T_{a,b}\) extends boundedly to \(\mathcal F^2\) exactly when \(\beta\le c\). It is compact exactly when \(\beta<c\).
2. When \(0\le\beta<c\), put
\[
Q=1-\beta^2+\rho^4,\qquad
\Delta=\sqrt{\big(c^2-\beta^2\big)\big((1+\rho^2)^2-\beta^2\big)},\qquad
r=\frac{Q-\Delta}{2\rho^2}.
\]
Then \(0<r<1\) and all the singular values, indexed from \(n=0\), are precisely
\[
s_n(T_{a,b})=\rho^{-1/2}r^{(2n+1)/4}\qquad(n=0,1,2,\ldots).
\]
In particular, for every \(p>0\),
\[
\|T_{a,b}\|_{\mathcal S_p}^p
=\frac{\rho^{-p/2}r^{p/4}}{1-r^{p/2}}.
\]
3. At \(\beta=c\), \(T_{a,b}\) is bounded but not compact. Its modulus \(|T_{a,b}|\) is unitarily equivalent to
\[
\rho^{-1/2}\exp(-cP^2/2),
\]
where \(P\) is the self-adjoint momentum operator on \(\mathcal F^2\), unitarily equivalent to \(-i\,d/dx\) on \(L^2(\mathbb R)\). Consequently \(|T_{a,b}|\) has purely absolutely continuous spectrum \([0,\rho^{-1/2}]\), no eigenvalues, and every approximation number of \(T_{a,b}\) equals \(\rho^{-1/2}\).

The transition also has the exact asymptotic: for fixed \(\rho\in(0,1)\), \(p>0\), and \(\varepsilon=c-\beta\downarrow0\),
\[
\|T_{a,b}\|_{\mathcal S_p}^p\sim
\frac{\sqrt2}{p\sqrt c}\,\rho^{1-p/2}\varepsilon^{-1/2}.
\]

## Assumptions and scope
The normalized monomials \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), form an orthonormal basis of \(\mathcal F^2\). The compact-case sequence \((s_n)_{n\ge0}\) lists eigenvalues of \(|T_{a,b}|\) in descending order, with multiplicity. For a bounded possibly noncompact operator, its \(k\)-th approximation number is the distance to operators of rank smaller than \(k\); thus the boundary statement says \(a_k(T_{a,b})=\rho^{-1/2}\) for every \(k\ge1\). The parameters with \(a=0\) are excluded (there the operator has rank at most one). Phase factors of \(a\) and \(b\) do not alter singular values or the spectral type of the modulus: unitary rotations of the Fock variable and unitary right multiplication reduce to \(a=\rho>0\), \(b=\beta\ge0\).

## Proof
**1. Boundedness and its sharp edge.** Reduce by unitary rotations to positive real parameters \(a=\rho\), \(b=\beta\). For \(\beta\le c\), the change of variables \(w=\rho z\) gives
\[
\|Tf\|^2=\rho^{-2}\frac1\pi\int_{\mathbb C}|f(w)|^2e^{-|w|^2}
\exp\!\left(\frac{-(c-\beta)(\operatorname{Re}w)^2-(c+\beta)(\operatorname{Im}w)^2}{\rho^2}\right)dA(w)
\le\rho^{-2}\|f\|^2.
\]
If \(\beta\ge1\), then \(T1=e^{\beta z^2/2}\notin\mathcal F^2\). For \(c<\beta<1\), the normalized coherent states \(k_w(z)=e^{z\bar w-|w|^2/2}\) satisfy, along positive real \(w\),
\[
\|Tk_w\|^2=(1-\beta^2)^{-1/2}
\exp\!\left(\left(\frac{\rho^2}{1-\beta}-1\right)w^2\right)\longrightarrow\infty.
\]
Thus no bounded extension exists above the edge.

**2. Positive Gaussian kernel.** For \(\beta<1\), evaluating the Gaussian integral for \(A=T^*T\) gives the Bargmann kernel
\[
K_A(z,\bar w)=h\exp\!\left(\alpha z\bar w+
\frac\gamma2(z^2+\bar w^2)\right),
\quad h=(1-\beta^2)^{-1/2},\quad
\alpha=\frac{\rho^2}{1-\beta^2},\quad
\gamma=\frac{\rho^2\beta}{1-\beta^2}.
\]
Here \((Af)(z)=\pi^{-1}\int_{\mathbb C}K_A(z,\bar w)f(w)e^{-|w|^2}\,dA(w)\). In the strict region \(\alpha+\gamma=\rho^2/(1-\beta)<1\), and \(T\) is Hilbert–Schmidt, with the exact trace
\[
\operatorname{Tr}(A)=\sum_{n\ge0}\|Te_n\|^2
=\frac1\pi\int_{\mathbb C}e^{\beta\operatorname{Re}z^2-c|z|^2}\,dA(z)
=\frac1{\sqrt{c^2-\beta^2}}.
\]

**3. Complete geometric diagonalization.** For \(\beta>0\), let \(t\in(0,1)\) be the smaller solution of
\[
t=\gamma+\frac{\alpha^2t}{1-\gamma t};
\]
for \(\beta=0\), set \(t=0\). Existence and uniqueness of the root in \([0,1)\) follow from \(\alpha+\gamma<1\): the polynomial \((t-\gamma)(1-\gamma t)-\alpha^2t\) is negative at zero and positive at one, with the second root outside \((0,1)\). Put
\[
d=1-\gamma t,\qquad r=\alpha/d\in(0,1),\qquad
H=-\frac\gamma{d(1-r^2)},\qquad
F_u(z)=\exp\!\left(\frac t2z^2+uz+\frac H2u^2\right).
\]
Each \(F_u\) belongs to \(\mathcal F^2\). The elementary complex Gaussian identity
\[
\frac1\pi\int_{\mathbb C}e^{-|w|^2+(t/2)w^2+(\gamma/2)\bar w^2+u w+v\bar w}\,dA(w)
=\frac1{\sqrt d}\exp\!\left(\frac{tv^2+2uv+\gamma u^2}{2d}\right)
\]
implies, with \(v=\alpha z\),
\[
A F_u=\lambda_0 F_{ru},\qquad
\lambda_0=h/\sqrt d=\sqrt r/\rho.
\]
Taking successive \(u\)-derivatives at zero supplies nonzero pairwise orthogonal eigenvectors with eigenvalues \(\lambda_0r^n\), \(n\ge0\). Eliminating \(t\) yields
\[
\rho^2r^2-(1-\beta^2+\rho^4)r+\rho^2=0;
\]
its root below one is the stated \(r\). This relation also gives
\[
\frac{\lambda_0}{1-r}
=\frac1{\sqrt{c^2-\beta^2}}
=\operatorname{Tr}(A).
\]
Since \(A\) is positive trace class and these eigenvalues exhaust its trace, they exhaust all its nonzero eigenvalues. As \(T\) is injective, no missing zero-eigenvalue subspace occurs. Taking square roots proves the exact singular-value list and the Schatten formula.

**4. The boundary as heat flow.** Set \(\beta=c=1-\rho^2\); then the kernel parameters simplify to
\[
h=\frac1{\rho\sqrt{1+c}},\qquad
\alpha=\frac1{1+c},\qquad
\gamma=\frac c{1+c}.
\]
On the polynomial core let \(P=(\partial_z-z)/(i\sqrt2)\). The Weyl translations
\[
(W_s f)(z)=e^{sz-s^2/2}f(z-s)
\]
are unitary and satisfy \(W_s=e^{-i\sqrt2sP}\). Gaussian averaging gives
\[
e^{-cP^2}=\frac1{\sqrt{2\pi c}}\int_{\mathbb R}e^{-s^2/(2c)}W_s\,ds,
\]
whose Fock kernel is
\[
K_{e^{-cP^2}}(z,\bar w)
=\frac1{\sqrt{1+c}}\exp\!\left(
\frac{z\bar w}{1+c}+\frac c{2(1+c)}(z^2+\bar w^2)\right).
\]
Comparison with \(K_A\) gives the exact bounded-operator identity \(T^*T=\rho^{-1}e^{-cP^2}\). Under the standard unitary Segal–Bargmann transform
\[
(\mathcal Bh)(z)=\pi^{-1/4}\int_{\mathbb R}
 e^{-x^2/2+\sqrt2xz-z^2/2}h(x)\,dx,
\]
\(P\) corresponds to \(-i\,d/dx\). Hence \(A\) becomes multiplication by \(\rho^{-1}e^{-c\xi^2}\) after the Fourier transform, and \(|T|\) becomes multiplication by \(\rho^{-1/2}e^{-c\xi^2/2}\). This multiplier has purely absolutely continuous spectrum filling \([0,\rho^{-1/2}]\) and has no point eigenvalues. Its essential norm equals its norm, \(\rho^{-1/2}\). The same is true of \(T\), hence all approximation numbers have that value.

**5. Threshold asymptotic.** If \(\varepsilon=c-\beta\downarrow0\), direct expansion of the quadratic root gives
\[
1-r=\frac{\sqrt{2c}}{\rho}\sqrt\varepsilon+O(\varepsilon).
\]
Insert this into \(\rho^{-p/2}r^{p/4}/(1-r^{p/2})\) to obtain the displayed sharp \(\varepsilon^{-1/2}\) divergence, for each fixed \(p>0\).

## Verification
The accompanying `verify.py` is a Python standard-library check of finite monomial Gram coefficients against the Gaussian kernel, the quadratic-root and trace identities, and the boundary heat-kernel coefficients. Run `python3 verify.py` in the directory containing the script. Its expected terminal line is `QUADRATIC_FOCK_GAUSSIAN_SPECTRAL_IDENTITIES_OK`. These finite computations are not proofs of completeness, continuous spectrum, or the asymptotic; those are established analytically above.

## Relationship to prior work
Barik, Sen, and Paul [1], publicly available from July 19, 2026, characterize bounded, compact, and Hilbert–Schmidt weighted composition operators on weighted Fock spaces and give essential-norm estimates. Those qualitative classifications encompass part of the phase-boundary setting, but their accessible abstract does not state the exact singular-value sequence, critical absolutely continuous modulus, or sharp Schatten blow-up coefficient; the full manuscript was not accessible for a decisive comparison. Johnson [2] proves boundedness and compactness criteria for pullback operators between quadratic-weight Bargmann spaces and shows compact pullbacks have exponentially decaying singular values in one complex dimension; the accessible complete paper gives no exact geometric parameter or critical heat-spectrum identification for the present family. Fatehi [3] studies weighted Fock composition operators, normality, closed range, and selected norms, not this full singular-value transition. The classical Mehler/Hermite Gaussian diagonalization and Segal–Bargmann correspondence are established background; their use here does not assert novelty of those general tools.

## Limitations
The theorem concerns Gaussian quadratic entire weights and strict contractions \(0<|a|<1\) on the **one-variable** classical Fock Hilbert space. It does not classify arbitrary entire weights, general affine symbols, or the spectrum of the nonnormal operator \(T\) itself. At the compactness boundary it classifies the modulus \(|T|\), not \(T\). The full July 2026 weighted-Fock manuscript and certain broad Gaussian-operator sources were not available for line-by-line originality comparison; independent examination may reveal prior equivalent formulations. The embedded script provides only finite checks, not an independent audit.

## References
[1] S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170 (first public July 19, 2026), https://arxiv.org/abs/2607.17170.

[2] R. Johnson, *Pullback operators on Bargmann spaces*, arXiv:2403.13227v2 (2024), https://arxiv.org/html/2403.13227v2.

[3] M. Fatehi, *Weighted composition operators on the Fock space*, arXiv:1809.04829 (2018), https://arxiv.org/html/1809.04829v1.

[4] I. Chalendar, J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, Acta Sci. Math. 89 (2023), 93–108, DOI:10.1007/s44146-023-00056-z.

[5] M. Putinar, J. E. Tener, *Singular values of weighted composition operators and second quantization*, arXiv:1612.03970 (2016), concerning Hardy spaces rather than the Fock family considered here.
