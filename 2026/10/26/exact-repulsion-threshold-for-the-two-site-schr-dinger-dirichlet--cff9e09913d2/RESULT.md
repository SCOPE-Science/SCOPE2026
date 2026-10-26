# Exact repulsion threshold for the two-site Schrödinger–Dirichlet boson sector

## Finding

**Theorem (complete constrained ground-state classification and matching linear instability).** Let \(p\ne q\) be two bosonic sites, and consider the normalized two-particle family
\[
|\psi\rangle=x|p^2\rangle+y|pq\rangle+z|q^2\rangle,
\qquad |x|^2+|y|^2+|z|^2=1.
\]
Take repulsion \(U>0\), nonlinear coupling \(g>0\), and real chemical potential \(\mu\). The untempered Schrödinger–Dirichlet energy on this invariant sector, as given in Fransson–Sowa [1, Eq. (51) and its displayed Hamiltonian], is
\[
\begin{aligned}
\mathcal E(x,y,z)={}&(U/2-\mu)(|x|^2+|z|^2)-\mu|y|^2\\
&-g\left[\frac{|x|^4+|y|^4+|z|^4}{4}
+|x|^2|y|^2+|y|^2|z|^2+|x|^2|z|^2
+\operatorname{Re}(\bar x y^2\bar z)\right].
\end{aligned}
\]
Its exact global constrained minimum is
\[
\boxed{\min_{\|\psi\|=1}\mathcal E=-\mu-\frac g4-
\frac{(2g-U)_+^2}{14g},\qquad (r)_+:=\max\{r,0\}.}
\]
For \(U\ge 2g\), the only minimizing ray is \(|pq\rangle\). For \(0<U<2g\), all and only the minimizers have
\[
\boxed{|x|^2=|z|^2=\frac{2g-U}{7g},\qquad
|y|^2=\frac{3g+2U}{7g},\qquad
2\arg y\equiv\arg x+\arg z\pmod {2\pi}.}
\]
Here phases are interpreted modulo \(2\pi\); the latter case has nonzero amplitudes, so all three arguments are defined. Every such choice of phases attains the minimum. The parameter \(\mu\) only shifts the energy and does not affect these states.

As a separate dynamical characterization of the **same** threshold, linearization of the source's three-amplitude Hamiltonian ODE about the orbit of \(|pq\rangle\), in a co-rotating frame and with \(\hbar=1\), has transverse mode eigenvalues
\[
\boxed{\lambda_\pm=\pm\sqrt{U(U-2g)}}
\]
for the equation \(i\dot v=Mv\). Thus the pure mixed-occupation orbit has exponential linear instability with growth exponent \(\sqrt{U(2g-U)}\) for \(0<U<2g\), while its linearized eigenvalues are real for \(U>2g\), and the two modes meet at zero at \(U=2g\). No assertion of nonlinear asymptotic stability follows from the real eigenvalues.

With the two sites regarded as distinct tensor factors, the minimizing state's one-site reduced density matrix is diagonal with eigenvalues \((a,b,a)\), where \(a=(2g-U)/(7g)\) and \(b=1-2a\) for \(U<2g\), whereas for \(U\ge 2g\) it has eigenvalues \((0,1,0)\). The site-mode entanglement entropy in natural units is exactly
\[
S=-2a\log a-b\log b,
\]
with the convention \(0\log0=0\). In particular, as \(\delta=2g-U\downarrow0\) from the lower-repulsion side,
\[
S=\frac{2\delta}{7g}\left[1-\log\left(\frac\delta{7g}\right)\right]
+O\left((\delta/g)^2\right).
\]
This entropy is between the **site occupation modes**, not a separately claimed particle-entanglement entropy.

## Assumptions and scope

The states \(|p^2\rangle,|pq\rangle,|q^2\rangle\) represent the orthonormal occupation vectors \(|2,0\rangle,|1,1\rangle,|0,2\rangle\) for two distinct sites and exactly two particles. The energy is the **untempered**, finite-dimensional restriction of the source's nonlinear functional, not the spectrum of a linear Bose–Hubbard hopping Hamiltonian. We optimize over every normalized complex triple and every relative phase, with \(U>0\), \(g>0\), \(\mu\in\mathbb R\). The zero-repulsion \(U=0\) minimizer was already established in [1, Appendix VII.C] and is not claimed as a new endpoint. This theorem makes no assertion about the unrestricted infinite-site ground-state existence question or the source's separately tempered energy.

## Proof

Write \(a=|x|^2\), \(b=|y|^2\), \(c=|z|^2\), so \(a,b,c\ge0\) and \(a+b+c=1\), and put \(r=\sqrt{ac}\). Let \(V\) denote the quartic expression in square brackets in \(\mathcal E\). If \(br>0\), define \(\theta=2\arg y-\arg x-\arg z\); otherwise the phase-bearing term vanishes. In either case, the identity \(\operatorname{Re}(\bar x y^2\bar z)=br\cos\theta\) is interpreted by the actual real part. Set
\[
V_*(b)=\frac38(1-b)^2+\frac14b^2+\frac32b(1-b)
=\frac38+\frac34b-\frac78b^2.
\]
**Exact deficit identity:** a direct expansion using \(a+c=1-b\) gives
\[
\boxed{V_*(b)-V=\frac{(a-c)^2}{8}
+\frac b2(\sqrt a-\sqrt c)^2
+\left(b\sqrt{ac}-\operatorname{Re}(\bar x y^2\bar z)\right)\ge0.}
\]
The last parenthesis is nonnegative by the triangle inequality, as is every other summand. If \(0<b<1\), equality forces \(a=c=(1-b)/2>0\) and phase matching \(2\arg y\equiv\arg x+\arg z\pmod{2\pi}\), and conversely these conditions give equality. For \(b=1\), equality holds at \(x=z=0\). Consequently the global constrained energy problem is **exactly** the one-variable minimization
\[
\mathcal E\ge E_*(b):=-\mu+\frac U2-\frac{3g}{8}
-\left(\frac U2+\frac{3g}{4}\right)b+\frac{7g}{8}b^2,
\qquad 0\le b\le1,
\]
with equality attainable for **each** \(b\) by taking balanced outer amplitudes and aligned phases. Since \(E_*''(b)=7g/4>0\), its unconstrained vertex is
\[
b_0=\frac{3g+2U}{7g}>0.
\]
For \(0<U<2g\), \(b_0<1\), so its unique minimizer is \(b=b_0\), giving \(a=c=(1-b_0)/2=(2g-U)/(7g)\). For \(U\ge2g\), \(b_0\ge1\), so the strictly convex polynomial on \([0,1]\) uniquely minimizes at \(b=1\). Completing the square around its vertex or computing the endpoint energy difference yields
\[
\min_{0\le b\le1}E_*(b)
=E_*(1)-\frac{7g}{8}\,(1-b_0)_+^2
=-\mu-\frac g4-\frac{(2g-U)_+^2}{14g}.
\]
Together with the exact deficit's equality conditions, this proves all global minimizers and excludes boundary competitors. The energy has continuous first derivative in \(U\), but its second derivative changes from \(-1/(7g)\) for \(U<2g\) to zero for \(U>2g\); hence \(U=2g\) is the sharp onset of the nonzero outer occupation.

For the dynamical statement, [1, Eq. (51)] gives, in units \(\hbar=1\),
\[
\begin{aligned}
i\dot x&=(U-2\mu)x-g[(|x|^2+2|y|^2+2|z|^2)x+\bar z y^2],\\
i\dot y&=-2\mu y-g[(2|x|^2+|y|^2+2|z|^2)y+2x\bar y z],\\
i\dot z&=(U-2\mu)z-g[(2|x|^2+2|y|^2+|z|^2)z+\bar x y^2].
\end{aligned}
\]
The pure mixed-occupation solution is \(x=z=0\), \(y(\tau)=e^{i(2\mu+g)\tau}\). Write \(x=e^{i(2\mu+g)\tau}X\) and \(z=e^{i(2\mu+g)\tau}Z\). Terms linear in \(X,Z\) yield
\[
i\frac d{d\tau}\begin{pmatrix}X\\\bar Z\end{pmatrix}
=\underbrace{\begin{pmatrix}U-g&-g\\g&-(U-g)\end{pmatrix}}_M
\begin{pmatrix}X\\\bar Z\end{pmatrix}.
\]
Its characteristic polynomial is \(\lambda^2-U(U-2g)\). When \(0<U<2g\), the corresponding evolution generator \(-iM\) has one positive real eigenvalue \(\sqrt{U(2g-U)}\), proving exponential *linear* instability. At the crossing \(U=2g\), the transverse block is nilpotent. This derivation is independent of the static energy minimization.

Finally, partial trace over site \(q\) kills off-diagonal terms because the three Fock basis components have distinct site-\(q\) occupations, leaving eigenvalues \((a,b,c)\). Substitution of the minimizing populations gives the stated entropy formula. With \(a=\delta/(7g)\), Taylor expansion of \(-(1-2a)\log(1-2a)\) gives \(2a+O(a^2)\) and proves the entropy onset.

## Verification

The included standalone \(\texttt{verification.py}\) uses only the Python standard library. Running \(\texttt{python3 verification.py}\) with the embedded deterministic seed gives **PASS: 5742 independent finite checks**. These check the exact quartic deficit and lower bound on random normalized complex triples, energy attainment and phase-matching families over independent parameter samples, the critical scaling identity, and the rotating-frame transverse linearization. In particular, the tests compare the nonlinear right-hand side before linearization against its first-order expression. Numerical tests are not an exhaustive search over the continuum; the preceding algebraic identities and strict convexity prove the quantified theorem for every admissible parameter and state.

## Relationship to prior work

Fransson and Sowa [1] introduced the Schrödinger–Dirichlet model, wrote the exact invariant three-amplitude equations and their quartic Hamiltonian in Eq. (51), and established the **\(U=0\)** two-site/two-particle optimizing state in Appendix VII.C. Neither that calculation nor their existence result for the separately **tempered** infinite-site functional evaluates the positive-repulsion phase boundary or the matched transverse dynamical soft mode given here. The contribution is confined to the exact all-positive-coupling minimizer classification, its sharp \(U=2g\) boundary, its site-mode entropy profile, and the associated linear-instability exponent; no zero-repulsion optimizer is presented as new.

Berezowski, Sowa and Fransson [2] consider a **linear** two-site Bose–Hubbard hopping operator and its spectral cat-state structures. Their linear spin-matrix eigenvectors do not entail the quartic nonlinear energy minimization above. The spin-1 condensate analysis of Huang and collaborators [3] likewise has an analogous three-component spin-mixing setting but a different interaction energy and magnetic-field constraints. These comparisons reduce, but cannot eliminate, the possibility that a broader unpublished or unlocated quartic spin-mixing classification subsumes this specialization.

## Limitations

The theorem proves the exact **restricted two-site, two-particle untempered** optimization and a linearized instability of one distinguished orbit. It does not prove unrestricted infinite-array minimizer existence, a many-body phase transition in a thermodynamic limit, nonlinear orbital stability or instability of all stationary solutions, robustness to added hopping/potentials, or experimentally realized entanglement generation. The word "threshold" refers to the precise finite-dimensional constrained energy diagram. Site-mode entropy is not particle entanglement. The linked mathematical literature was checked on a best-knowledge basis; priority requires independent expert assessment.

## References

[1] J. Fransson and A. P. Sowa, *Entanglement-Inducing Quantum Markov Processes*, arXiv:2609.21438v1, first public 2026-09-18. Source passages: Sec. IV.A Eq. (51) and displayed Hamiltonian, Sec. V.A discussion of finite-array minima, Appendix VII.C Eqs. (103)–(120), Sec. V.D tempered-functional Theorem 2. https://arxiv.org/abs/2609.21438

[2] A. Berezowski, A. P. Sowa and J. Fransson, *Two-site Bose-Hubbard hopping and Schrödinger cat states*, arXiv:2605.04598 (2026), Sec. II and the tridiagonal hopping operator. https://arxiv.org/abs/2605.04598

[3] Y. Huang, W. Zhong, Z. Sun and Z.-D. Hu, *Phase diagram and spin mixing dynamics in spinor condensates with a microwave dressing field*, *Scientific Reports* **5**, 14464 (2015), https://doi.org/10.1038/srep14464.
