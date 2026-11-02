# Sharp order-two Gevrey smoothing by an oscillatory positive radial Bergman weight

## Finding

Let \(\alpha>-1\), \(\eta>0\), and \(\varepsilon\in\mathbb R\) with \(0<|\varepsilon|<1\). On the unit disk \(\mathbb D\), consider the positive measure
\[
 d\mu(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\left[1+\varepsilon\cos\left(\frac{\eta}{1-|z|^2}\right)\right]dA(z).
\]
Let \(K_\varepsilon(z,w)\) be its holomorphic Bergman reproducing kernel, and put \(s=z\overline w\). Then
\[
 K_\varepsilon(z,w)=(1-s)^{-\alpha-2}+D(s),\qquad D(s)=\sum_{n=0}^\infty d_ns^n.
\]
The entire correction \(D\) extends smoothly to the closed disk (\(D\) is not asserted entire on the complex plane). Its boundary trace \(\theta\mapsto D(e^{i\theta})\) is Gevrey of order \(2\), but is not Gevrey of any order \(1\le\sigma<2\). This conclusion is global on the boundary circle, not a pointwise failure claim.

More precisely, for every fixed allowed parameter triple, as integers \(n\to\infty\),
\[
\boxed{\begin{aligned}
 d_n={}&-\frac{\varepsilon\sqrt\pi\,\eta^{(2\alpha+1)/4}}{\Gamma(\alpha+1)\Gamma(\alpha+2)}\,
 n^{(6\alpha+5)/4}\,e^{-\sqrt{2\eta n}}\\[-1mm]
 &\quad\times\left[\cos\left(\sqrt{2\eta n}+\frac\eta2-\frac{\pi(2\alpha+1)}8\right)
 +O_{\alpha,\eta,\varepsilon}(n^{-1/2})\right].
\end{aligned}}
\]
In particular,
\[
 \limsup_{n\to\infty}\frac{\log|d_n|}{\sqrt n}=-\sqrt{2\eta},
\]
where \(\log0=-\infty\) by convention. The logarithmic rate is independent of \(\alpha\) and \(\varepsilon\), whereas the power and oscillatory phase depend on the parameters.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\); \(dA\) is ordinary planar Lebesgue area. The weighted Bergman space is the closed holomorphic subspace of \(L^2(\mathbb D,d\mu)\), with kernel characterized by point evaluation. The weight is positive and comparable to \((1-|z|^2)^\alpha\), while its relative multiplier \(1+\varepsilon\cos(\eta/(1-|z|^2))\) has no boundary limit. For \(\alpha>0\), the full density still tends to zero, so no claim of nonconvergence of the full density is made. The function \(D\) is a scalar holomorphic function of \(s=z\overline w\); its smooth closed-disk extension also gives a smooth extension of \(K_\varepsilon-K_0\) on the closed bidisk in the separate variables.

For a smooth periodic function \(f\), \(f\in G^\sigma(\mathbb T)\) means there exist constants \(A,C>0\) such that \(\|\partial_\theta^k f\|_\infty\le CA^k(k!)^\sigma\) for every integer \(k\ge0\). This is a global, not pointwise, Gevrey definition. No assertion concerns uniformity as parameters vary or any failure of smoothness of the original kernel's singular term.

## Proof

**1. Exact radial moments.** Rotational invariance makes monomials orthogonal. Their squared norms are
\[
 m_n=(\alpha+1)\int_0^1t^n(1-t)^\alpha\left[1+\varepsilon\cos\left(\frac\eta{1-t}\right)\right]dt,
 \qquad n=0,1,\dots.
\]
Positivity gives \((1-|\varepsilon|)m_n^{(0)}\le m_n\le(1+|\varepsilon|)m_n^{(0)}\), where
\[
 m_n^{(0)}=(\alpha+1)B(n+1,\alpha+1)
 =\frac{\Gamma(\alpha+2)\Gamma(n+1)}{\Gamma(n+\alpha+2)}.
\]
Consequently \(K_\varepsilon=\sum s^n/m_n\) on \(|s|<1\), and \(\sum s^n/m_n^{(0)}=(1-s)^{-\alpha-2}\).

**2. Exact oscillatory transform.** Let
\[
 L_n=\frac{1}{B(n+1,\alpha+1)}\int_0^1(1-u)^nu^\alpha e^{i\eta/u}\,du.
\]
The substitution \(u=1/(1+v)\) and the integral representation of Tricomi's \(U\)-function yield
\[
 \boxed{L_n=\frac{e^{i\eta}\Gamma(n+\alpha+2)}{\Gamma(\alpha+1)}U(n+1,-\alpha,-i\eta).}
\]
For strict positive real part of the last argument, this follows directly from the absolutely convergent \(U\) integral. Passage to \(-i\eta\) is justified by dominated convergence: the transformed amplitude is \(v^n(1+v)^{-n-\alpha-2}=O(v^{-\alpha-2})\) at infinity, integrable precisely because \(\alpha>-1\). Thus no unproved contour deformation is required for this identity.

**3. Large-degree asymptotic.** For fixed \(\alpha\) and \(\eta\), DLMF §13.8(iii), Eq. 13.8.11, supplies the large-first-parameter expansion of \(U(a,b,z)\). With \(a=n+1\), \(b=-\alpha\), \(z=-i\eta\), and its leading coefficient \(p_0=1\), it gives
\[
 U(a,b,z)=\frac{2e^{z/2}}{\Gamma(a)}\left(\frac za\right)^{(1-b)/2}
 K_{b-1}(2\sqrt{az})\left(1+O(a^{-1/2})\right).
\]
Here \(\arg z=-\pi/2\), and the large argument of \(K\) lies on the ray \(\arg\sqrt z=-\pi/4\), within its classical decaying sector. Its leading expansion is
\[
 K_\nu(2\sqrt{az})=\frac{\sqrt\pi}{2(az)^{1/4}}e^{-2\sqrt{az}}
 \left(1+O(a^{-1/2})\right).
\]
The standard gamma-ratio estimate, the principal branches of fractional powers, and \(a=n+1\) give
\[
 L_n=\frac{\sqrt\pi}{\Gamma(\alpha+1)}(-i\eta)^{(2\alpha+1)/4}
 n^{(2\alpha+1)/4}
 e^{i\eta/2-2\sqrt{-i\eta n}}
 \left(1+O(n^{-1/2})\right).
\]
Since \(\sqrt{-i\eta n}=(1-i)\sqrt{\eta n/2}\), this has absolute envelope \(n^{(2\alpha+1)/4}e^{-\sqrt{2\eta n}}\), with oscillation phase
\(\sqrt{2\eta n}+\eta/2-\pi(2\alpha+1)/8\).

**4. Reproducing-kernel coefficients.** Put \(\rho_n=\operatorname{Re}L_n\), so \(m_n=m_n^{(0)}(1+\varepsilon\rho_n)\). Because \(|\rho_n|\le1\), the denominator never vanishes, and exactly
\[
 d_n=-\frac{1}{m_n^{(0)}}\frac{\varepsilon\rho_n}{1+\varepsilon\rho_n}.
\]
We have \((m_n^{(0)})^{-1}=n^{\alpha+1}/\Gamma(\alpha+2)(1+O(n^{-1}))\), while \(\rho_n=O(n^{(2\alpha+1)/4}e^{-\sqrt{2\eta n}})\). Thus the difference between \(-\varepsilon\rho_n/m_n^{(0)}\) and \(d_n\) is exponentially smaller than the announced \(O(n^{-1/2})\) relative envelope. Taking the real part of the expression from step 3 proves the boxed formula.

**5. Smoothness and exact Gevrey order.** There is a fixed \(c=\sqrt{2\eta}>0\) and \(P=(6\alpha+5)/4\) for which \(|d_n|\le C(1+n)^{P}e^{-c\sqrt n}\). Hence for every integer \(k\ge0\), differentiation of \(D(e^{i\theta})\) term by term is absolutely uniform, and
\[
 \|\partial_\theta^kD(e^{i\theta})\|_\infty\le C\sum_{n\ge1}n^{k+P}e^{-c\sqrt n}
 \le C_1A^k(k!)^2.
\]
The last bound follows by the substitution \(x=\sqrt n\), evaluation of a gamma integral, and the factorial estimate \(\Gamma(2k+2P+2)\le C_2A_2^k(k!)^2\) after a finite number of low orders are absorbed. These same coefficient estimates give all derivatives of \(D\) uniformly on \(|s|\le1\).

To prove the order cannot be lowered, define \(\phi(n)=\sqrt{2\eta n}+\eta/2-\pi(2\alpha+1)/8\). For each sufficiently large positive integer \(j\), take \(n_j\) to be the nearest integer to \((2\pi j-\eta/2+\pi(2\alpha+1)/8)^2/(2\eta)\). Then \(\phi(n_j)=2\pi j+O(n_j^{-1/2})\). The coefficient asymptotic gives \(|d_{n_j}|\ge c_0 n_j^P e^{-c\sqrt{n_j}}\). If the boundary trace were \(G^\sigma\) for some \(1\le\sigma<2\), repeated integration by parts and optimization in the derivative order would force its Fourier coefficients to satisfy \(|d_n|\le C'e^{-c'n^{1/\sigma}}\), a contradiction along \(n_j\). The same subsequence and the upper envelope prove the stated logarithmic limsup.

## Verification

A standalone script \(\texttt{checker.py}\) recomputes exact normalized complex moments with Tricomi's \(U\)-function and compares their leading exponential/Bessel asymptotics for multiple fixed parameter families. It also compares exact reproducing-kernel perturbation coefficients with the cosine formula and checks representative near-maximum phase subsequences. Execute \(\texttt{python checker.py}\) with the publicly available Python package \(\texttt{mpmath}\). The completed computation produced **45 successful finite numerical assertions**. The infinite asymptotic and global Gevrey statements are derived in the proof, not inferred from these computations.

## Relationship to prior work

Xiong and Xu, *Semiclassical asymptotics for Bergman projections with Gevrey weights* (first public March 21, 2024, arXiv:2403.14157), derive semiclassical Gevrey-symbol expansions for smooth strictly plurisubharmonic interior exponential weights. The present problem instead fixes the disk, allows a positive radial density with a nonconvergent relative multiplier at the boundary, and classifies the sharp Gevrey regularity of an exact reproducing-kernel **difference**. Its parameter \(n\) is a monomial degree, not a semiclassical inverse Planck constant. Thus the displayed result is not a specialization of their principal theorem.

Hitrik and Stone (arXiv:2105.14402) study semiclassical Bergman projections with smooth weights, again a different geometric and asymptotic regime. Hagger, Liu, Taskinen and Virtanen (arXiv:2011.04699) discuss radial and oscillatory Toeplitz symbols on analytic Bergman spaces; such symbols are operators on a fixed Bergman space and do not determine the inverse-moment correction of the reproducing kernel for the present changed positive measure. Earlier radial Bergman-kernel formulae with nonoscillatory weights, or general Fourier-Gevrey equivalences, provide ingredients rather than the parameter-specific sharp coefficient and its non-improvable Gevrey index.

The exact \(U\)-function asymptotic and the \(K\)-Bessel decay are standard and credited below. A broad priority search did not reveal a decisive previously published formula for this exact oscillatory-positive-weight family; this is not proof of absolute novelty, and uninspected general integral-transform literature could implicitly contain the result.

## Limitations

The result assumes \(\alpha>-1\), \(0<|\varepsilon|<1\), \(\eta>0\) fixed. If \(\varepsilon=0\), the correction vanishes, so its exact Gevrey order is not two. No estimates uniform in parameters are claimed. The singular unperturbed kernel has not been regularized, so the *full* kernel is not smooth at \(s=1\). The non-Gevrey conclusion is a global statement about the boundary circle. The coefficient formula contains an oscillatory cosine and therefore does not supply a pointwise two-sided bound for every degree. The smoothness and Gevrey proofs are analytical; numerical tests do not certify infinitely many degrees. Independent audit and validation have not been performed.

## References

- H. Xiong and H. Xu, *Semiclassical asymptotics for Bergman projections with Gevrey weights*, arXiv:2403.14157 (initial version March 21, 2024), https://arxiv.org/abs/2403.14157 .
- M. Hitrik and M. Stone, *Asymptotics for Bergman projections with smooth weights: a direct approach*, arXiv:2105.14402 (initial version May 30, 2021), https://arxiv.org/abs/2105.14402 .
- R. Hagger, Z. Liu, J. Taskinen and J. A. Virtanen, *Toeplitz Operators on the Unit Ball with Locally Integrable Symbols*, arXiv:2011.04699 (initial version November 9, 2020), https://arxiv.org/abs/2011.04699 .
- NIST Digital Library of Mathematical Functions, §13.8(iii), Eq. 13.8.11 (large-parameter Tricomi \(U\)) and §10.40 (large-argument modified Bessel \(K\)), https://dlmf.nist.gov/13.8 and https://dlmf.nist.gov/10.40 .
