# A universal electric-field threshold for negative fourth cumulants in a dephased quantum walk

## Finding

For the infinite, translation-covariant nearest-neighbor quantum walk specified below, let \(X_t\) be the site obtained by measuring the particle's position at time \(t\) when it began at the origin. Its long-time variance and fourth-cumulant rates are

\[
\begin{aligned}
K_2&=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}t
=2w+\frac{c^2A}{A^2+E^2},\\
K_4&=\lim_{t\to\infty}\frac{\operatorname{cum}_4(X_t)}t
=2w+\frac{c^2\{A(A^2+E^2)+12w(E^2-A^2)\}}{(A^2+E^2)^2}
-\frac{3Ac^4(A^4+10A^2E^2-3E^4)}{(A^2+E^2)^3(A^2+4E^2)},
\end{aligned}
\]

where \(A=\gamma+2w>0\). In particular, set

\[
z_*=\frac{5+2\sqrt7}{3},\qquad e_*=\sqrt{z_*}\simeq1.85216113609.
\]

For **every** \(\gamma,w\ge0\) with \(A>0\), the following sharp classification holds:

* If \(|E|/A\ge e_*\), then \(K_4>0\) for all \(c>0\).
* If \(0\le |E|/A<e_*\), there is a **unique** \(c_*>0\) such that \(K_4>0\) for \(0<c<c_*\), \(K_4=0\) at \(c=c_*\), and \(K_4<0\) for \(c>c_*\).

The crossover is explicit. With \(z=(E/A)^2\), \(s=w/A\in[0,1/2]\), define

\[
B(z,s)=\frac{1+z+12s(z-1)}{(1+z)^2},\qquad
C(z)=\frac{3(1+10z-3z^2)}{(1+z)^3(1+4z)}.
\]

For \(z<z_*\), one has \(C(z)>0\) and

\[
\boxed{\frac{c_*^2}{A^2}=
\frac{B(z,s)+\sqrt{B(z,s)^2+8sC(z)}}{2C(z)}.}
\]

The universal threshold is independent of the separate dephasing and incoherent-jump proportions once their sum \(A\) is fixed. In particular, as \(z\uparrow z_*\) at fixed \(s\),

\[
\frac{c_*}{A}\sim
\sqrt{\frac{B(z_*,s)}{-C'(z_*)}}\,(z_*-z)^{-1/2}.
\]

## Assumptions and scope

Take the one-particle Hilbert space \(\ell^2(\mathbb Z)\) with canonical basis \(|n\rangle\), and set \(\hbar=1\). Assume \(c>0\), \(w,\gamma\ge0\), \(A=\gamma+2w>0\), and any \(E\in\mathbb R\). The tight-binding Stark Hamiltonian and projectors are

\[
H=-\frac c2\sum_{n\in\mathbb Z}(|n+1\rangle\langle n|+|n\rangle\langle n+1|)
+E\sum_{n\in\mathbb Z}n|n\rangle\langle n|,\qquad P_n=|n\rangle\langle n|.
\]

The trace-preserving Lindblad evolution is

\[
\dot\rho=-i[H,\rho]
+\gamma\bigl(\sum_nP_n\rho P_n-\rho\bigr)
+w\sum_{n\in\mathbb Z}\sum_{\epsilon=\pm1}
\bigl(J_{n,\epsilon}\rho J_{n,\epsilon}^\dagger-\tfrac12\{P_n,\rho\}\bigr),
\qquad J_{n,\epsilon}=|n+\epsilon\rangle\langle n|.
\]

Thus each direction has an incoherent jump rate \(w\), off-diagonal coherences decay at rate \(A\), and there is no thermally biased jump term. Set \(\rho(0)=|0\rangle\langle0|\) and \(\mathbb P(X_t=n)=\langle n|\rho(t)|n\rangle\). By inversion symmetry \(X_t\) has mean zero, and \(\operatorname{cum}_4(X_t)=\mathbb E[X_t^4]-3\mathbb E[X_t^2]^2\). The results are about asymptotic growth *per unit time*, not the sign of every finite-time cumulant or a diffusion-based entropy estimate.

## Proof

**1. Exact tilted coherence operator and spectral branch.** Fourier transform the density matrix along simultaneous lattice translations, with a real moment tilt \(k\) obtained by analytic continuation of the spatial wave number. Index the remaining coherences by separation \(r\in\mathbb Z\). The tilted operator on the separation sequence has diagonal entries \(-A-iEr\) when \(r\ne0\), central entry \(2w(\cosh k-1)\), and nearest-neighbor off-diagonal entries of magnitude \(c\sinh(k/2)\) and opposite signs (a harmless phase gauge makes them imaginary). At \(k=0\), the central eigenvalue is isolated at zero, while the other spectrum has real part \(-A\). Bounded analytic perturbation around zero therefore supplies one simple analytic, even branch \(\lambda(k)\) with \(\lambda(0)=0\), separated in real part from the remaining spectrum for sufficiently small real \(k\). The initial delta position has nonzero overlap with this branch. Hence

\[
\lim_{t\to\infty}t^{-1}\log\mathbb E[e^{kX_t}]=\lambda(k)
\]

locally analytically at zero, and the cumulant rates equal the corresponding derivatives of \(\lambda\).

**2. Fourth-order exact expansion.** Write \(h=c\sinh(k/2)\) and \(R_j(\lambda)=(A+\lambda+ijE)^{-1}\). Schur complementation at the central coherence gives, through degree four in \(k\),

\[
\begin{aligned}
\lambda={}&2w(\cosh k-1)
+h^2\{R_1(\lambda)+R_{-1}(\lambda)\}\\
&+h^4\{R_1(\lambda)^2R_2(\lambda)
+R_{-1}(\lambda)^2R_{-2}(\lambda)\}+O(k^6).
\end{aligned}
\]

The remainder estimate follows because a closed separation walk leaving \(r=0\) and reaching \(|r|\ge3\) needs at least six off-diagonal steps; all reduced diagonal resolvents are bounded locally since \(A>0\). Put \(\lambda=a_2k^2+a_4k^4+O(k^6)\) and

\[
\begin{aligned}
S_0&=\frac{2A}{A^2+E^2},\\
S_1&=\frac{2(E^2-A^2)}{(A^2+E^2)^2},\\
T_0&=\frac{2A(A^2-5E^2)}{(A^2+E^2)^2(A^2+4E^2)}.
\end{aligned}
\]

Using \(h^2=c^2(k^2/4+k^4/48)+O(k^6)\), one obtains

\[
a_2=w+\frac{c^2S_0}{4},\qquad
a_4=\frac w{12}+\frac{c^2S_0}{48}
+\frac{c^2a_2S_1}{4}+\frac{c^4T_0}{16}.
\]

Since \(K_2=2a_2\) and \(K_4=24a_4\), substituting and collecting the rational functions proves the two boxed formulas.

**3. Exact global sign diagram.** Let \(y=(c/A)^2>0\) and \(s=w/A\). Factoring gives

\[
\frac{K_4}{A}=2s+B(z,s)y-C(z)y^2.
\]

The polynomial \(1+10z-3z^2\) has exactly one nonnegative root \(z_*=(5+2\sqrt7)/3\). For \(z\ge z_*\), \(C(z)\le0\) and, because \(z_*>1\) and \(s\ge0\), \(B(z,s)>0\). Thus \(K_4>0\) for all positive \(y\). For \(z<z_*\), \(C(z)>0\). The concave quadratic \(2s+By-Cy^2\) is positive for sufficiently small \(y>0\), tends to minus infinity, and has exactly one positive root (for \(s=0\), the other root is zero). Its positive root is the displayed expression. At \(z=z_*\), \(C'(z_*)<0\), while \(B(z_*,s)>0\), yielding the stated divergence by elementary expansion. This proves sharpness and uniqueness, without any assumption that coherent hopping is perturbatively small.

## Verification

The included `verify.py` independently constructs the tilted generator's Taylor eigenvector recursion on a eleven-separation truncation and compares its second- and fourth-order eigenvalue coefficients against the closed expressions. This *does not* use the Schur-complement formula. It also checks the universal sign boundary and the one-positive-root classification across parameter sets. Finally, it separately constructs a finite-chain density-matrix Lindbladian and propagates the physical density matrix to test the predicted negative and positive signs, reporting normalization and boundary mass. It executed successfully with **251 deterministic checks** (NumPy and SciPy). These checks supplement, but do not replace, the analytic proof; finite-volume propagation does not certify an infinite-volume theorem.

## Relationship to prior work

Avnit and Cohen, *Quantum walk in stochastic environment* [1], introduce the minimal Pauli/Lindblad quantum-walk dynamics; their section V, equations (24)–(30), supplies the translation/separation representation. Equation (31) gives an exact zero-potential-gradient dispersion explicitly **excluding the energy bias**; equation (32) treats the nonzero-gradient effective rate perturbatively. The zero-gradient fourth cumulant obtained by differentiating their exact dispersion is therefore **prior-implied** and is not claimed as new. The present mathematical claim is the *finite-gradient* fourth cumulant and the sharp universal sign-transition threshold across all coherent hopping strengths.

Shapira and Cohen [2] develop a broader Ohmic quantum-transport model with a field, current and diffusion results. Its bath-induced bond superoperators differ from the independent Pauli jumps assumed here, and its inspected results do not evaluate this fourth-cumulant sign boundary. Esposito and Gaspard [3] solve a translation-invariant quantum-diffusion spectrum without a nonzero uniform Stark gradient. The exact tilted-operator machinery is classical analytical methodology; neither the method nor the zero-field spectral reduction is claimed as new.

## Limitations

The theorem requires constant parameters, translation-invariant dissipators, Markovian local dephasing, symmetric Poisson jumps, initial localization, and \(A>0\). It concerns the infinite chain and the long-time cumulant growth rates of an endpoint projective position measurement. A uniform field paired with symmetric jumps is not a finite-temperature detailed-balance prescription. The sign of a fourth cumulant is not itself an entropy-production rate or proof of quantum interference, and the result does not imply finite-sample detectability. Wider spectral or full-counting-statistics theories may encompass this specialized exact formula; a comprehensive independent publication-priority determination is not claimed.

## References

1. B. Avnit and D. Cohen, *Quantum walk in stochastic environment*, arXiv:2308.08419 (first posted 16 August 2023), https://arxiv.org/abs/2308.08419. In particular equations (24)–(32) and their statements of field scope.
2. D. Shapira and D. Cohen, *Quantum stochastic transport along chains*, arXiv:1907.01993 (2019), https://arxiv.org/abs/1907.01993. Model, results and supplemental spectral calculations.
3. M. Esposito and P. Gaspard, *Exactly solvable model of quantum diffusion*, Journal of Statistical Physics 121 (2005), https://gaspard.pierre.web.ulb.be/EG.JSP.05.pdf. Translation-covariant zero-gradient spectral methodology.
