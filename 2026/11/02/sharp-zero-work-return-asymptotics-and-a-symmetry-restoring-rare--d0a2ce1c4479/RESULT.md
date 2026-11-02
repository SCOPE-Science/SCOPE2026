# Sharp zero-work return asymptotics and a symmetry-restoring rare trajectory for a lazy quantum engine

## Finding

For the discrete work process of the lazy qubit measurement engine in [1], let \(0<p<1/2\) be the measurement jump probability and \(0<q<1\) the probability of ignoring the outcome. Write \(N_n\) for the net signed number of extracted work quanta after \(n\) cycles, starting with \(N_0=0\) and outgoing heading \(+\). With the matrix entries \(a,b,c,d\) defined below, put

\[
L=\sqrt{ad}+\sqrt{bc},\qquad V=\sqrt{\frac{ad}{bc}},\qquad S=\sqrt{\frac{ac}{bd}}.
\]

Then \(L<1\), every odd-cycle zero-work probability vanishes, and the exact *even-cycle* local asymptotic is

\[
\boxed{\Pr(N_n=0)=\frac{1+S}{\sqrt{2\pi Vn}}L^n(1+o(1))\qquad(n\to\infty,\ n\ \text{even}).}
\]

The corresponding positive exponential decay rate is \(I_0=-\log L\). More finely, fix \(p\in(0,1/2)\). For any sequence of even positive integers \(n\to\infty\), \(q_n=1-\varepsilon_n\in(0,1]\), \(\varepsilon_n\geq0\), and \(\varepsilon_n\sqrt n\to u\in[0,\infty)\),

\[
\boxed{\sqrt n\,\Pr_{p,q_n}(N_n=0)\longrightarrow\sqrt{\frac{2p}{\pi(1-p)}}\exp\!\left(-\frac{u^2}{8p(1-p)}\right).}
\]

The parity constraint is essential. The rare zero-current event has a precise dynamical mechanism: among irreducible stationary two-state transition kernels with zero mean signed displacement, the **unique** minimizer of relative-entropy rate with respect to the original kernel is the symmetric chain

\[
Q_* =\begin{pmatrix}1-\phi_*&\phi_*\\\phi_*&1-\phi_*\end{pmatrix},\qquad
\phi_* =\frac{\sqrt{bc}}{\sqrt{ad}+\sqrt{bc}},
\]

and its minimum relative-entropy rate equals \(I_0\). This matrix is exactly the Doob-driven kernel of the zero-current exponential tilt. The result identifies a symmetry-restoring rare-event mechanism and a weak-feedback risk window of order \((1-q)^{-2}\).

## Assumptions and scope

The stationary output of each quantum-engine cycle is reduced to its work increment \(U_k\in\{+1,-1\}\). Let \(p=p_j\in(0,1/2)\), \(q=p_l\in(0,1)\), and \(U_0=+1\). Conditional on \(U_{k-1}\), the next sign has the Markov transition matrix (rows and columns ordered \(+,-\))

\[
T=\begin{pmatrix}a&c\\b&d\end{pmatrix},\quad
a=1-pq,\ c=pq,\ b=1-(1-p)q,\ d=(1-p)q.
\]

The normalized *gross extracted work* over \(n\) cycles is \(N_n=\sum_{k=1}^{n}U_k\), and the physical gross work is \(W_n=W_\theta N_n\), where \(W_\theta>0\) is the single-cycle work quantum [1]. The word *gross* matters: information-erasure cost is not subtracted. The analysis assumes this protocol ordering, independent measurement/feedback randomness between cycles as encoded by \(T\), a fixed initial positive sign, and no external thermal noise. The statement about a zero-current minimizing kernel uses stationary, irreducible two-state Markov competitors with exactly zero mean sign, not arbitrary non-Markov path laws.

## Proof

**1. Positive drift and exact tilted eigenstructure.** The finite matrix \(T\) is strictly positive. Since \(b-c=1-q>0\), its invariant probability of \(+\) exceeds one-half. For \(\theta\in\mathbb R\), weight each *new* sign by \(e^{\theta U_k}\). Its tilted matrix is

\[
T_\theta=\begin{pmatrix}ae^\theta&ce^{-\theta}\\be^\theta&de^{-\theta}\end{pmatrix},\qquad
\mathbb E[e^{\theta N_n}]=e_+^\top T_\theta^n\mathbf1.
\]

The Perron eigenvalue \(\lambda(\theta)\) has a unique zero-slope saddle at \(\theta_*=(1/2)\log(d/a)\). Indeed, the trace is \(ae^\theta+de^{-\theta}\), the determinant is \(ad-bc\), and at \(\theta_*\) the diagonal entries both equal \(A=\sqrt{ad}\), while the off-diagonal product is \(B^2=bc\). The Perron eigenvalue is \(L=A+B\), and the other eigenvalue is \(A-B\). Since the original invariant drift is strictly positive, strict convexity of \(\log\lambda\) and \(\lambda(0)=1\) give \(0<L<1\). Its centered tilted variance curvature is

\[
(\log\lambda)''(\theta_*)=A/B=V>0.
\]

The right eigenvector of \(T_{\theta_*}\) can be chosen as \(r=(1,h)^\top\), with \(h=e^{\theta_*}\sqrt{b/c}\). A left eigenvector is \(\ell=(1,h^{-1})^\top\), so the spectral amplitude at the saddle is

\[
C=\frac{(e_+^\top r)(\ell^\top\mathbf1)}{\ell^\top r}=\frac{1+1/h}{2}=\frac{1+S}{2}.
\]

**2. Lattice Fourier inversion with both saddles.** The integer-valued sum has the exact inversion

\[
\Pr(N_n=0)=\frac1{2\pi}\int_{-\pi}^{\pi}e_+^\top T_{\theta_*+it}^{\,n}\mathbf1\,dt,
\]

because the exponential tilt multiplies the Fourier coefficient at displacement zero by one. Near \(t=0\), analytic perturbation of the simple Perron root gives

\[
\log\lambda(\theta_*+it)=\log L-\frac V2t^2+O(t^3),\qquad C(t)=C+O(t).
\]

Strict positivity of the tilted kernel gives a uniform spectral-radius gap away from \(t\equiv0\pmod\pi\): equality in the entrywise comparison \(|T_{\theta_*+it}|=T_{\theta_*}\) forces the two diagonal phase factors to be identical, hence \(t\in\pi\mathbb Z\). At \(t=\pi\) the entire matrix is \(-T_{\theta_*}\), so for even \(n\) its second saddle contributes exactly the same Gaussian amplitude as the first. The non-Perron eigenvalue has smaller modulus. Standard Gaussian rescaling \(t=O(n^{-1/2})\), with the spectral gap controlling the complement, therefore yields

\[
\Pr(N_n=0)\sim\frac{2CL^n}{\sqrt{2\pi Vn}}.
\]

For odd \(n\) the two saddle contributions cancel; more directly, a sum of an odd number of signs \(\pm1\) cannot be zero. This proves the first formula and its exact amplitude.

**3. Weak-feedback crossover.** Put \(\varepsilon=1-q\). Direct Taylor expansion of the two square roots, for fixed \(0<p<1/2\), gives

\[
L(p,1-\varepsilon)=1-\frac{\varepsilon^2}{8p(1-p)}+O(\varepsilon^3).
\]

As \(\varepsilon\downarrow0\), \(S\to1\) and \(V\to(1-p)/p\). The positive entries and separated non-Perron eigenvalue remain uniformly separated in a neighborhood of \(q=1\). The two-saddle analytic Gaussian argument of step 2 is thus *uniform* for \(q\to1\). If \(\varepsilon_n\sqrt n\to u\), then \(n\log L\to-u^2/[8p(1-p)]\), yielding the boxed crossover formula. The endpoint \(q=1\) appears only in this limiting statement, not in the fixed-\(q\) exponential-decay assertion.

**4. Unique zero-current dynamics.** A stationary, irreducible two-state Markov chain with equal stationary masses \(1/2\) has transition matrix \(Q_\phi\) with the two flip probabilities both equal to \(\phi\in(0,1)\); equal masses are equivalent to zero stationary mean signed increment. Its entropy rate relative to \(T\) equals

\[
J(\phi)=(1-\phi)\log\frac{1-\phi}{\sqrt{ad}}+
\phi\log\frac\phi{\sqrt{bc}}.
\]

Since \(J''(\phi)=1/[\phi(1-\phi)]>0\), the unique minimizer is \(\phi_*=B/(A+B)\), where substitution gives \(J(\phi_*)=-\log(A+B)=I_0\). Finally the Doob transform \(Q_{ij}=T_{\theta_*,ij}r_j/(Lr_i)\) directly equals \(Q_{\phi_*}\), showing the minimizing dynamics also arise from the exact zero-current exponential tilt.

## Verification

`verify.py` implements direct finite-time propagation of the two-state signed-work chain without relying on transformed propagators. It checks the parity obstruction, the large-even-cycle prefactor across several values of \((p,q)\), the relative-entropy minimum, the weak-feedback rate coefficient, and the double-scaling profile. Run `python3 verify.py` using Python 3; no third-party dependencies are required. These finite-time tests support the derivation but do not replace its spectral and asymptotic arguments.

## Relationship to prior work

Bresque, Das and Roldán [1] derive precisely this lazy quantum engine's two-state work propagators, finite-time work moments, and selected first-passage distributions (including the special cases of fully informative and fully lazy feedback). The transition kernel and its basic exact propagator are *not* new. The result here instead isolates the physically interpretable fixed-cycle **zero-net-work** event, proves the leading lattice-prefactor and decay rate, identifies the corresponding entropy-minimizing driven trajectory, and resolves the delicate weak-feedback crossover. These statements are not explicitly given in the examined main text or supplementary analysis of [1], although its exact generating functions provide the starting point from which they could also be derived.

Willaert, Cleuren and Van den Broeck [2] derive fluctuation symmetries and large-deviation functions for a different continuous-time two-state *exchange-current* process. Their framework illustrates the relevance of tilted eigenvalues but does not give the lattice local return prefactor, its initial-positive-state amplitude or the weak-feedback scaling for [1]. Generic Markov-additive local limit methods could provide alternative proofs, so novelty is limited to these explicit model-specific quantitative and structural conclusions.

## Limitations

The asymptotics concern gross work before any feedback-information processing cost. For each fixed \(0<q<1\), the zero-work event is exponentially rare; the formula is not uniform as \(p\to0\) or \(q\to0\). The weak-feedback crossover is uniform for fixed \(p\) near \(q=1\), not for simultaneous changes to \(p\). The zero-current driven chain is an exact entropic and Doob-transform identification; no general conditional functional limit theorem, full work large-deviation function, stopping-time formula, or experimental inference claim is asserted. The original source's complete finite-time propagators and general Markov-additive large-deviation theory remain close antecedents; independent priority assessment is warranted.

## References

[1] L. Bresque, D. Das and É. Roldán, *Run-and-tumble exact work statistics in a lazy quantum measurement engine: stochastic information processing*, arXiv:2410.18783v1, publicly available October 24, 2024. https://arxiv.org/html/2410.18783v1

[2] T. Willaert, B. Cleuren and C. Van den Broeck, *Fluctuation symmetry in a two-state Markov model*, arXiv:1404.3479v1, April 14, 2014. https://arxiv.org/html/1404.3479v1
