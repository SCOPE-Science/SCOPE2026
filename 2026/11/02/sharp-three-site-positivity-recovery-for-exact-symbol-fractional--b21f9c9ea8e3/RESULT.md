# Sharp three-site positivity recovery for exact-symbol fractional diffusion

## Finding

Let \(0<\alpha\leq 2\) and \(h>0\). For \(k=0,1,2\), set
\[
c_k(\alpha)=\frac1\pi\int_0^\pi\theta^\alpha\cos(k\theta)\,d\theta,
\qquad a=c_0(\alpha),\quad b=-c_1(\alpha),\quad g=c_2(\alpha).
\]
Consider the three-interior-site, zero-exterior (principal Toeplitz) restriction of the exact Fourier-symbol fractional Laplacian:
\[
L_{\alpha,h}=h^{-\alpha}
\begin{pmatrix}a&-b&g\\-b&a&-b\\g&-b&a\end{pmatrix},
\qquad P_{\alpha,h}(t)=\exp(-tL_{\alpha,h}).
\]
Here the symbol on the infinite uniform grid is exactly \(|\xi|^\alpha\), not the symbol of the fractional power of the standard nearest-neighbour difference Laplacian.

**Theorem.** The matrix \(L_{\alpha,h}\) is positive definite for all the stated parameters. If \(0<\alpha\leq1\), every entry of \(P_{\alpha,h}(t)\) is strictly positive for every \(t>0\). If \(1<\alpha\leq2\), define
\[
\Delta=\sqrt{2b^2+g^2/4}.
\]
There is a **unique** positive number \(\tau_*(\alpha)\) solving
\[
\boxed{\quad\cosh(\Delta\tau)-\frac{g}{2\Delta}\sinh(\Delta\tau)
=\exp(3g\tau/2).\quad}
\]
The set of times for which \(P_{\alpha,h}(t)\) is entrywise nonnegative is **exactly**
\[
\boxed{\quad\{0\}\ \cup\ [h^\alpha\tau_*(\alpha),\infty).\quad}
\]
At all positive earlier times the two extreme-site entries, \((1,3)\) and \((3,1)\), are strictly negative, while all other entries are strictly positive. At the positive threshold only those two entries vanish; afterwards every entry is strictly positive.

Write
\[
Z=\gamma_{\mathrm E}+\log(2\pi)-\operatorname{Ci}(2\pi)
=\int_0^{2\pi}\frac{1-\cos u}{u}\,du>0,
\]
where \(\gamma_{\mathrm E}\) is the Euler--Mascheroni constant and \(\operatorname{Ci}\) the cosine integral. As \(\alpha\downarrow1\),
\[
\boxed{\quad\tau_*(\alpha)=\frac{\pi Z}{8}(\alpha-1)
+O((\alpha-1)^2).\quad}
\]
The strictly negative extreme-site excursion also has an exact leading constant:
\[
\boxed{\quad\min_{t\geq0}\big(P_{\alpha,h}(t)\big)_{13}
=-\frac{Z^2}{128}(\alpha-1)^2+o((\alpha-1)^2),\quad}
\]
and its minimizing time is
\[
t_{\min}=h^\alpha\left(\frac{\pi Z}{16}(\alpha-1)
+o(\alpha-1)\right).
\]
At the ordinary second-derivative endpoint \(\alpha=2\), the onset satisfies \(\tau_*(2)=0.261185173260985\ldots\). This is a statement about the stated exact-symbol three-site matrix only.

## Assumptions and scope

The order belongs to \((0,2]\); the mesh width is any positive real number; the state space consists of the three consecutive interior grid sites with values fixed at zero at all other grid sites. Time is continuous and the matrix exponential is exact, not an Euler or Runge--Kutta approximation. Positivity means preservation of the coordinatewise nonnegative cone, equivalently entrywise nonnegativity of the evolution matrix. At time \(t=0\), the identity is nonnegative but not entrywise strictly positive. The result is not a claim about the infinite-grid semigroup or the spectral fractional power of a finite Dirichlet Laplacian.

## Proof

**1. Operator and coefficient signs.** The restriction is symmetric, and Fourier orthogonality gives, for every nonzero real \(v=(v_0,v_1,v_2)\),
\[
v^\mathsf{T}(h^\alpha L_{\alpha,h})v
=\frac1\pi\int_0^\pi\theta^\alpha
\left|v_0+v_1e^{i\theta}+v_2e^{2i\theta}\right|^2d\theta>0.
\]
Integration by parts (the boundary terms vanish for positive \(\alpha\)) gives
\[
b=\frac\alpha\pi\int_0^\pi\theta^{\alpha-1}\sin\theta\,d\theta>0,
\qquad
g=-\frac\alpha{2\pi}\int_0^\pi\theta^{\alpha-1}\sin(2\theta)\,d\theta.
\]
Pairing the first and second half of the sine integral proves \(g<0\) for \(\alpha<1\), \(g=0\) for \(\alpha=1\), and \(g>0\) for \(\alpha>1\). In the latter range,
\[
b-g=\frac\alpha\pi\int_0^\pi\theta^{\alpha-1}
\sin\theta(1+\cos\theta)\,d\theta>0.
\]
Thus \(0<g<b\) for \(\alpha>1\), which implies \(\Delta>3g/2\).

If \(\alpha\leq1\), the off-diagonal entries of \(-L_{\alpha,h}\) are nonnegative and its nearest-neighbour entries are strictly positive. By shifting the diagonal to obtain a nonnegative irreducible matrix and using the exponential power series (a positive path connects each pair of sites), \(P_{\alpha,h}(t)\) is strictly positive for every positive time.

**2. Exact entrywise exponential.** Put \(\tau=t/h^\alpha\). In the orthonormal basis given by the symmetric outer-site vector, the middle-site vector, and the antisymmetric outer-site vector, the dimensionless matrix is the direct sum of
\[
\begin{pmatrix}a+g&-\sqrt2b\\-\sqrt2b&a\end{pmatrix}
\quad\text{and the scalar }a-g.
\]
A direct two-by-two exponential calculation yields
\[
\begin{aligned}
P_{13}(t)&=\frac{e^{-a\tau}}2\left[e^{-g\tau/2}
\left(\cosh(\Delta\tau)-\frac{g}{2\Delta}\sinh(\Delta\tau)\right)
-e^{g\tau}\right],\\
P_{12}(t)&=P_{23}(t)
=e^{-a\tau-g\tau/2}\frac{b}{\Delta}\sinh(\Delta\tau)>0.
\end{aligned}
\]
All diagonal entries are positive because the matrix exponential of a real symmetric matrix is positive definite. By symmetry, only \(P_{13}=P_{31}\) could be negative.

**3. Unique positive recovery time.** For \(\alpha>1\), set \(q=g/(2\Delta)\), so \(0<q<1\), and write
\[
H(\tau)=\frac{1-q}{2}\exp((\Delta-3g/2)\tau)
+\frac{1+q}{2}\exp(-(\Delta+3g/2)\tau)-1.
\]
Its sign equals that of \(P_{13}(t)\). The inequalities \(\Delta>3g/2\) and \(0<q<1\) imply
\[
H(0)=0,\qquad H'(0)=-2g<0,\qquad H''(\tau)>0,
\qquad\lim_{\tau\to\infty}H(\tau)=+\infty.
\]
Consequently there is exactly one zero in \((0,\infty)\), with \(H<0\) before it and \(H>0\) afterwards. The already-positive remaining entries give the precise positivity-time set, including its isolated point \(t=0\).

**4. Exact near-boundary constants.** At \(\alpha=1\) the Fourier integrals yield \(b=2/\pi\) and \(g=0\). Differentiating under the integral and integrating by parts gives
\[
g'(1)=\frac1\pi\int_0^\pi\theta\log\theta\cos(2\theta)\,d\theta
=\frac{\gamma_{\mathrm E}+\log(2\pi)-\operatorname{Ci}(2\pi)}{4\pi}
=\frac Z{4\pi}>0.
\]
Let \(\varepsilon=\alpha-1\). On bounded \(s\)-intervals, the exact matrix exponential uniformly satisfies
\[
P_{13}(h^\alpha\varepsilon s)
=\varepsilon^2\left(-\frac Z{4\pi}s+\frac{2}{\pi^2}s^2\right)
+O(\varepsilon^3).
\]
The positive zero of the displayed quadratic is \(s=\pi Z/8\), and its unique minimizer is \(s=\pi Z/16\), with value \(-Z^2/128\). The exact zero equation, strict convexity in Step 3 and the local expansion imply convergence of the unique positive zero to the quadratic zero. Moreover, \(P_{13}\) has positive second derivative on the shrinking negative interval for all sufficiently small \(\varepsilon\), so its global negative minimum occurs at the local quadratic minimum. This proves the two asymptotic formulas. For \(\alpha=2\), \(a=\pi^2/3\), \(b=2\), \(g=1/2\), and the exact root equation reduces to
\[
\cosh(\sqrt{129}\,\tau/4)-\frac1{\sqrt{129}}\sinh(\sqrt{129}\,\tau/4)
=e^{3\tau/4},
\]
whose unique positive root has the numerical value stated above.

## Verification

The standalone `verify.py` independently evaluates the defining Fourier integrals with adaptive quadrature and compares the closed-form exponential against a general-purpose matrix exponential across positive orders, mesh sizes and times. It tests sign changes on both sides of each computed threshold, the \(\alpha=2\) closed form, positive definiteness and the near-boundary coefficients. The program reported **461 successful check groups**. Reproduce using `python -m pip install -r requirements.txt` and `python verify.py` in this package. These finite numerical checks corroborate, but do not replace, the analytical all-parameter proof above.

## Relationship to prior work

Huang and Oberman (2016), Section 4.1 and its adjacent discussion, already give the same exact Fourier-symbol weights, including their signs at \(\alpha=1,2\) and the loss of nonnegative coefficients for \(\alpha>1\). Those coefficient facts and the resulting failure of short-time positivity are prior knowledge, not claimed as discoveries here. Zhou and Zhang (2023), Section 2, describe the corresponding exact-symbol discretization. Antil, Dondl and Striet (2020/2021) treat sinc-based approximations on finite domains. Noutsos and Tsatsomeros (2008) already define the general exponential positivity index and give numerical examples; Daners, Glück and Kennedy (2015), especially their finite-dimensional eventual-positivity theorem, establish general spectral criteria for eventual positivity; Chen and collaborators (2020) provide related signed-Laplacian criteria. Such general spectral criteria can establish eventual positivity in this setting, but the inspected sources do not state this particular finite three-site **unique recovery time**, its exact scalar equation, or the linear-onset/quadratic-dip constants. General matrix-exponential identities are elementary background rather than a novelty claim. A specialized earlier treatment of this exact three-site family could still subsume the result.

## Limitations

No extension to arbitrary numbers of sites, arbitrary Fourier or Grünwald stencils, higher dimension, nonuniform grids, nonlinear problems, explicit time-stepping, or floating-point implementations is proved. The three-site restricted evolution is not asserted to conserve mass. The positive-operator time set includes isolated time zero, so saying it is merely a closed ray would be false. The asymptotic negative excursion is an exact mathematical small-order result, not a guarantee that its amplitude is practically significant at a given precision. Independent scientific review and a conclusive publication-priority audit remain outstanding.

## References

1. Y. Huang and A. Oberman, *Finite difference methods for fractional Laplacians*, arXiv:1611.00164 (first public November 1, 2016), Sections 2, 4.1, 4.2 and 5. https://arxiv.org/abs/1611.00164
2. S. Zhou and Y. Zhang, *A novel and simple spectral method for nonlocal PDEs with the fractional Laplacian*, arXiv:2311.07814 (first public November 14, 2023), Sections 2–3. https://arxiv.org/abs/2311.07814
3. D. Daners, J. Glück and J. B. Kennedy, *Eventually Positive Semigroups of Linear Operators*, arXiv:1511.09020 (2015), Sections 5–6. https://arxiv.org/abs/1511.09020
4. W. Chen et al., *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581 (2020), Section VI. https://arxiv.org/abs/2009.03581
5. H. Antil, P. Dondl and L. Striet, *Approximation of Integral Fractional Laplacian and Fractional PDEs via sinc-Basis*, arXiv:2010.06509 (2020), Section 2. https://arxiv.org/abs/2010.06509
6. D. Noutsos and M. J. Tsatsomeros, *Reachability and Holdability of Nonnegative States*, SIAM J. Matrix Anal. Appl. 30 (2008), 700–712, Sections 2–4. https://doi.org/10.1137/070693850
