# Two optimal radii for sparse first-jet sampling of Gaussian Fock monomials

## Finding

In the classical Bargmann–Fock space, consider the span of both evaluation and first-derivative representers at the vertices of a regular polygon. Its ability to approximate a single high-degree normalized monomial has an exact conditional-Poisson formula and a sharp sparse-orbit law.

Write \(e_N(z)=z^N/\sqrt{N!}\). For positive integers \(m\) and \(N\) and squared radius \(\lambda>0\), let \(V_{m,\sqrt\lambda}\) be the joint span of the value and first-derivative reproducing kernels at \(\sqrt\lambda\exp(2\pi i k/m)\), \(0\le k<m\). Define
\[
E_{N,m}(\lambda)=\|P_{V_{m,\sqrt\lambda}}e_N\|_{\mathcal F}^2.
\]
Let \(a\in\{0,\dots,m-1\}\) satisfy \(a\equiv N\pmod m\), and let the positive weights \(w_j=\lambda^j/j!\) range over \(j\ge0\) with \(j\equiv a\pmod m\). With
\[
S=\sum w_j,\qquad \mu=S^{-1}\sum j w_j,\qquad
v=S^{-1}\sum(j-\mu)^2w_j>0,
\]
**the exact formula for all \(N\ge0,m\ge1,\lambda>0\)** is
\[
\boxed{ E_{N,m}(\lambda)=\frac{\lambda^N}{N!S}
 \left(1+\frac{(N-\mu)^2}{v}\right). }
\]
If \(m=m_N\ge1\) is any sequence satisfying \(m_N=o(\sqrt N)\), then
\[
\boxed{\lim_{N\to\infty}\frac{\sqrt N}{m_N}\sup_{\lambda>0}E_{N,m_N}(\lambda)
=\frac{2}{\sqrt{2\pi e}}.}
\]
For every fixed real \(y\), with convergence uniform on compact \(y\)-intervals,
\[
\boxed{\lim_{N\to\infty}\frac{\sqrt N}{m_N}E_{N,m_N}(N+y\sqrt N)
=\frac{(1+y^2)e^{-y^2/2}}{\sqrt{2\pi}}.}
\]
The limiting profile has exactly two global maximizing arguments, \(y=-1\) and \(y=1\). More sharply, if a choice \(\lambda_N>0\) satisfies
\[
E_{N,m_N}(\lambda_N)\big/\sup_{\lambda>0}E_{N,m_N}(\lambda)\longrightarrow1,
\]
then
\[
\operatorname{dist}\!\left((\lambda_N-N)/\sqrt N,\{-1,1\}\right)\longrightarrow0.
\]
Both \(\lambda=N-\sqrt N\) and \(\lambda=N+\sqrt N\) achieve the optimal asymptotic value. In terms of geometric radius the two asymptotically optimal branches are \(r=\sqrt N\mp\tfrac12+o(1)\).

## Assumptions and scope

The Gaussian Fock space is the Hilbert space of entire functions with
\[
\|f\|_{\mathcal F}^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
\]
where \(dA\) is planar Lebesgue measure and the monomials \(e_j(z)=z^j/\sqrt{j!}\) are orthonormal. The finite nodes are exactly the regular-polygon orbit, with both complex-linear bounded functionals \(f\mapsto f(z_k)\) and \(f\mapsto f'(z_k)\) at each nonzero node. The projection is orthogonal and does not incorporate additional point weights. The sparse-orbit conclusion allows arbitrary integer sequences \(m_N=o(\sqrt N)\), including fixed \(m\). There is no assertion about arbitrary node sets, higher-order derivatives, or global sampling of all polynomials.

## Proof

**1. Cyclic reduction and exact projection.** Rotation by \(2\pi/m\) decomposes \(\mathcal F\) orthogonally into the residue sectors \(\mathcal F_a=\overline{\operatorname{span}}\{e_j:j\equiv a\pmod m\}\). A discrete Fourier transform across the orbit reduces all \(2m\) value/derivative functionals to the span of two coefficient vectors within each sector. In the sector containing \(e_N\), after the harmless common diagonal phase and power factors are removed, these vectors have coordinates
\[
\left(\sqrt{w_j}\right)_{j\equiv a},\qquad
\left(j\sqrt{w_j}\right)_{j\equiv a}.
\]
Their Gram matrix is
\[
\begin{pmatrix}S&S\mu\\S\mu&S(\mu^2+v)\end{pmatrix}
\]
and has determinant \(S^2v>0\), since infinitely many residue indices carry strictly positive weight. Inverting it against the target coordinate \(\sqrt{w_N}(1,N)\) yields
\[
E_{N,m}(\lambda)=\frac{w_N}{S}\left(1+\frac{(N-\mu)^2}{v}\right),
\]
including the cases \(N=0\) and \(m=1\).

**2. Uniform residue equidistribution away from the origin.** Put \(R_N=(N/m^2)^{1/4}\to\infty\) and \(\lambda_0=m^2R_N=o(N)\). By the roots-of-unity filter, for any residue \(a\),
\[
S=\frac{e^\lambda}{m}\sum_{\ell=0}^{m-1}
\omega^{-a\ell}e^{\lambda(\omega^\ell-1)},\qquad \omega=e^{2\pi i/m}.
\]
The corresponding first and second raw moments are obtained by replacing \(e^{\lambda\omega^\ell}\) by \(\lambda\omega^\ell e^{\lambda\omega^\ell}\) and \(((\lambda\omega^\ell)^2+\lambda\omega^\ell)e^{\lambda\omega^\ell}\), respectively. The elementary estimates
\[
1-\cos(2\pi\ell/m)\ge c\,\operatorname{dist}(\ell,m\mathbb Z)^2/m^2,
\qquad |\omega^\ell-1|\le C\,\operatorname{dist}(\ell,m\mathbb Z)/m
\]
imply, for \(k=0,1,2\) and \(\lambda/m^2\ge R_N\),
\[
\sum_{\ell=1}^{m-1}|\omega^\ell-1|^k
 e^{-\lambda(1-\cos(2\pi\ell/m))}
\le C_km^{-k}e^{-c_0\lambda/m^2}.
\]
The estimate holds for \(m=1\) with an empty sum. Dividing the roots-of-unity moment formulas, and using the cancellation that the Poisson variance is \(\lambda\), gives uniformly on \(\lambda\ge\lambda_0\)
\[
S=\frac{e^\lambda}{m}(1+o(1)),\quad
\frac{|\mu-\lambda|}{\sqrt\lambda}=o(1),\quad
\frac v\lambda=1+o(1).
\]
Indeed the mean error is at most \(C(\lambda/m)e^{-c_0\lambda/m^2}\), and the relative variance error at most \(C(1+\lambda/m^2)e^{-c_0\lambda/m^2}\); after replacing \(c_0\) by a smaller positive constant both vanish uniformly because \(\lambda/m^2\ge R_N\to\infty\). Thus uniformly in \(N\) and \(\lambda\ge\lambda_0\),
\[
E_{N,m}(\lambda)=(1+o(1))\,m\frac{e^{-\lambda}\lambda^N}{N!}
\left(1+\frac{(N-\lambda)^2}{\lambda}\right). \tag{1}
\]
This is uniform even when \(|N-\lambda|\) is large: the error in the standardized mean is \(o(1)\) and the relative variance error is \(o(1)\), so the two positive quadratic brackets are uniformly comparable.

**3. Exclusion of tiny radii.** Write
\[
T=\sum_{j\equiv a}w_j(j-N)^2,\qquad
D=\sum_{\substack{j<k\\j\equiv k\equiv a}}w_jw_k(k-j)^2.
\]
The Gram-inverse identity also gives \(E=w_NT/D\). For sufficiently large \(N\), \(b=a+m\) satisfies \(N>a+b\), because \(m=o(\sqrt N)\). The two terms \(j=a,k=b\) yield \(D\ge m^2w_aw_b\), while the full Poisson sum bounds \(T\le e^\lambda[(N-\lambda)^2+\lambda]\). Consequently for \(0<\lambda\le\lambda_0\),
\[
E\le\frac{a!b!}{m^2N!}e^\lambda\lambda^{N-a-b}
\big((N-\lambda)^2+\lambda\big).
\]
Since \(a+b<2m=o(\sqrt N)\) and \(\lambda_0=o(N)\), elementary Stirling bounds imply that the right side is \(o(m/\sqrt N)\), uniformly over this interval. This proves the small-radius region is irrelevant to the optimum, including when \(\lambda\downarrow0\).

**4. Exact scalar optimization and the two shells.** Let
\[
H_N(\lambda)=e^{-\lambda}\frac{\lambda^N}{N!}
\left(1+\frac{(N-\lambda)^2}{\lambda}\right).
\]
For \(N>1\), direct differentiation gives the exact sign factorization
\[
H_N'(\lambda)=-\frac{e^{-\lambda}\lambda^{N-2}}{N!}
(\lambda-N)\big((\lambda-N)^2-N\big).
\]
There are two local maxima at \(N\pm\sqrt N\), one local minimum at \(N\), and the endpoints have limit zero. Stirling's formula yields
\[
\sqrt N H_N(N\pm\sqrt N)\longrightarrow\frac2{\sqrt{2\pi e}}.
\]
Therefore the global supremum of \(H_N\), and by steps 2–3 that of \(E_{N,m}/m\), has the asserted asymptotic. Stirling applied at \(\lambda=N+y\sqrt N\) gives the locally uniform Gaussian profile. Finally, the exact scalar monotonicity intervals together with Stirling (including its Poisson large-deviation bounds outside central windows) show that a sequence whose \(H_N\) values approach its global maximum must satisfy \(y\to\pm1\) in the distance-to-set sense. Uniform approximation (1) and step 3 transfer this assertion to \(E_{N,m}\). No uniqueness or exact finite-\(N\) equality of the two maximum heights is claimed.

## Verification

The standalone stdlib-Python checker `checker.py` reconstructs the cyclic Gram matrices from truncated Fock series without using the displayed moment inversion as its Gram-computation method. It checks projection against a separately calculated conditional moment formula for sample degrees, orbit sizes and radii; tests positivity and normalization; and tests the limiting two-shell profile against numerical examples. Running `python3 checker.py` produces the recorded `check_output.txt`. The checker executes 119 finite assertions. Those finite checks supplement, rather than replace, the uniform analytical proof above.

## Relationship to prior work

Escudero, Haimi and Romero (first publicly available 2020-04-27) establish multiple sampling/interpolation density theorems in weighted Fock spaces, with derivative data. Their global density criteria neither calculate the single-monomial projection for a finite polygon nor imply a sparse-orbit optimized constant. General coherent-state circle constructions by Janszky and collaborators provide a related orbit perspective; the full historical articles were not accessible for decisive formula-by-formula comparison. The new statement isolates a finite first-jet orbit and an optimally chosen radius, yielding the two off-center shells and the exact gain factor \(2/\sqrt e\) relative to the value-only leading coefficient.

## Limitations

The conclusion is only for a **regular polygon** at a common radius, with value and first-derivative data; it does not assert optimality among arbitrary node placements or simultaneous approximation of a band of monomials. The two optimal radii are asymptotically rather than exactly equal in performance. The rate of the relative \(o(1)\) remainder is not optimized. An inaccessible historical coherent-state article or a Poisson–Charlier polynomial treatment might contain an equivalent formulation, so independent priority review remains appropriate.

## References

1. L. A. Escudero, A. Haimi, J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, arXiv:2004.12922v1 (posted 2020-04-27); *Complex Analysis and Operator Theory* 15 (2021), article 35, doi:10.1007/s11785-020-01065-4.
2. L. D. Abreu and K. Gröchenig, *Banach Gabor Frames with Hermite Functions: Polyanalytic Spaces from the Heisenberg Group*, arXiv:1012.4283 (2010). Distinct global polyanalytic sampling setting.
3. P. Domokos, P. Adam, J. Janszky, *One-dimensional coherent-state representation on a circle in phase space*, *Physical Review A* 50 (1994), 4293, doi:10.1103/PhysRevA.50.4293 (accessible abstract only).
4. J. Janszky and collaborators, *Coherent states on a circle and quantum interference*, *Physical Review A* 48 (1993), 2213, doi:10.1103/PhysRevA.48.2213 (accessible abstract only).
