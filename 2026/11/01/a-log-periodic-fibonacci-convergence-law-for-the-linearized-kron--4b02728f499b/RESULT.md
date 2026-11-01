# A log-periodic Fibonacci convergence law for the linearized Kronecker Steiner process

## Finding

Put \(\varphi=(1+\sqrt5)/2\), \(\beta=\varphi^{-1}\), and fix \(\sigma>0\). Linearize successive planar Steiner symmetrizations about the unit disk along the Kronecker directions of angles \(j\pi\beta\), for \(j=1,2,\ldots\). Restrict to the zero-mean, translation-free radial Fourier perturbations \(f(\theta)=\sum_{m\ge2}(a_m\cos m\theta+b_m\sin m\theta)\), with analytic Fourier norm
\[
\|f\|_{\mathcal A_\sigma}=\sum_{m\ge2}e^{\sigma m}\sqrt{a_m^2+b_m^2}.
\]
Give the range the norm \(\|g\|_2=(\pi^{-1}\int_0^{2\pi}|g(\theta)|^2\,d\theta)^{1/2}\). Denote by \(T_N\) the composition of the first \(N\) first-variation operators. For each \(N\ge2\), its exact norm is
\[
M_N(\sigma):=\|T_N\|_{\mathcal A_\sigma\to L^2}
=\max_{k\ge3}\left[e^{-\sigma F_k}\cos^{N-1}(\pi\varphi^{-k})\right],
\]
where \(F_1=F_2=1\) and \(F_{k+1}=F_k+F_{k-1}\). Every maximizing perturbation may be chosen as a single Fibonacci-frequency harmonic, aligned with the first symmetrization axis. In particular, no non-Fibonacci harmonic can outperform a preceding Fibonacci harmonic in this operator norm.

Set \(t=(N-1)^{1/3}\), \(s=\{\log_\varphi t\}\), \(a=\sigma/\sqrt5\), and \(b=\pi^2/2\). The continuous, nonconstant, period-one function
\[
H_\sigma(s)=\min_{j\in\mathbb Z}\left(a\varphi^{j-s}+b\varphi^{-2(j-s)}\right)
\]
is the exact limiting oscillation envelope:
\[
\frac{-\log M_N(\sigma)}{(N-1)^{1/3}}
=H_\sigma\bigl(\{\log_\varphi((N-1)^{1/3})\}\bigr)
+O_\sigma(N^{-2/3}).
\]
Consequently the set of subsequential limits of the left-hand side is exactly the nondegenerate interval
\[
\left[3\left(\frac{a^2b}{4}\right)^{1/3},\;2(a^2b)^{1/3}\right].
\]
Its endpoint ratio is exactly \(2^{5/3}/3>1\), independent of \(\sigma\). Thus the sharp analytic linearized convergence exponent is \(1/3\), but its normalized leading constant does not converge: it oscillates periodically with the logarithm of the iteration count.

## Assumptions and scope

The operation is ordinary planar **Steiner symmetrization**, not Minkowski averaging. The result concerns only the derivative at the unit disk, **not** a uniform nonlinear convergence rate for finite-amplitude convex bodies. For a smooth radial perturbation \(K_\varepsilon=\{r e^{i\theta}:0\le r\le1+\varepsilon f(\theta)\}\), the first variation is obtained for each fixed smooth \(f\) as \(\varepsilon\to0\), followed by extension of the resulting linear operators to \(\mathcal A_\sigma\). The source of the symmetrization sequence is the exactly specified angle increment \(\pi/\varphi\), not the distinct Kakutani–Fibonacci point-ordering algorithm. The mean and first Fourier harmonic are excluded so that only shape anisotropy is measured. The phase-space norms are fixed as displayed, with no unspecified Fourier normalization.

## Proof

**1. Differential of one Steiner step.** Rotate coordinates so the chord directions are vertical and denote reflection about the horizontal axis by \(J(\theta)=-\theta\). At horizontal coordinate \(x=\cos\theta\), \(0<\theta<\pi\), the two perturbed endpoints have ordinate variations \(f(\theta)/\sin\theta\) and \(-f(-\theta)/\sin\theta\), respectively. Centering their chord replaces the upper ordinate variation by \((f(\theta)+f(-\theta))/(2\sin\theta)\). Radial displacement at the circle is this variation times \(\sin\theta\). The continuous endpoint limits agree, and the shape differential is therefore \(P_0f=(f+f\circ J)/2\). Rotating back gives \(P_\gamma f(\theta)=[f(\theta)+f(2\gamma-\theta)]/2\), where \(\gamma\) is the symmetry-axis angle perpendicular to the chord direction. The calculation establishes the derivative for smooth convex radial perturbations; by Fourier density it specifies the bounded linearized map on \(\mathcal A_\sigma\).

**2. Exactly one multiplier per angular transition.** In the real coefficient plane of each frequency \(m\), \(P_\gamma\) is the orthogonal rank-one projection onto the line making angle \(m\gamma\). Projections for two axes differing by \(\pi\beta\) have nonzero singular value \(|\cos(m\pi\beta)|\). Therefore \(N\) projections, \(N\ge2\), have norm \(|\cos(m\pi\beta)|^{N-1}\) on this frequency. The input \(\ell^1\)-sum of weighted Euclidean coefficient lengths and the normalized output Fourier \(\ell^2\)-norm imply, with equality at a single aligned frequency,
\[
M_N(\sigma)=\sup_{m\ge2}e^{-\sigma m}|\cos(m\pi\beta)|^{N-1}.
\]
The supremum is attained since the analytic weight decays exponentially.

**3. Fibonacci resonance is exactly optimal.** For \(\beta=\varphi^{-1}=[0;1,1,1,\ldots]\), the convergent denominators are \(F_k\). The standard best-approximation property of continued fractions says that for \(F_k\le m<F_{k+1}\), \(\|m\beta\|_{\mathbb R/\mathbb Z}\ge\|F_k\beta\|_{\mathbb R/\mathbb Z}\). As \(x\mapsto\cos(\pi x)\) decreases on \([0,1/2]\), the spectral factor for each \(m\) in this interval is no larger than that for \(F_k\), while \(e^{-\sigma m}\le e^{-\sigma F_k}\). Binet's formula yields the exact identity \(|F_k\beta-F_{k-1}|=\varphi^{-k}\). For \(k\ge3\), the cosine is positive. This proves the finite-\(N\) Fibonacci maximum claimed above.

**4. Uniform asymptotic phase law.** With \(t=(N-1)^{1/3}\), the negative logarithm of the \(k\)-th Fibonacci candidate is
\[
L_{N,k}=\sigma F_k-t^3\log\cos(\pi\varphi^{-k}).
\]
For \(k=\lfloor\log_\varphi t\rfloor+j\), Binet's formula and \(-\log\cos z=z^2/2+O(z^4)\) give
\[
L_{N,k}/t=a\varphi^{j-s}+b\varphi^{-2(j-s)}+O_\sigma(t^{-2})
\]
uniformly for every fixed bounded integer \(j\). A competitor with \(\varphi^k/t\) very large has excessive \(\sigma F_k/t\); one with \(\varphi^k/t\) very small has excessive \(t^2\varphi^{-2k}\). Thus both the exact and limiting minima lie in a common bounded range of \(j\), independent of large \(t\). Taking minima preserves the uniform \(O_\sigma(t^{-2})\) remainder, proving the phase formula.

**5. Exact endpoint constants and all accumulation values.** Write \(G(x)=ax+b/x^2\). The phase function minimizes \(G\) over one multiplicative lattice of ratio \(\varphi\). The continuous minimizer \(x_*=(2b/a)^{1/3}\) can be placed on the lattice by varying \(s\); hence \(\min_s H_\sigma(s)=G(x_*)=3(a^2b/4)^{1/3}\). Its maximum occurs when adjacent lattice options tie, at \(x_0^3=b(1-\varphi^{-2})/[a(\varphi-1)]=b/a\), using \(\varphi^2=\varphi+1\). At this switch \(G(x_0)=G(\varphi x_0)=2(a^2b)^{1/3}\), and monotonicity of \(G\) on either side of \(x_*\) shows there is no larger phase value. The minimum envelope is continuous and nonconstant. Finally \(\{\log_\varphi((N-1)^{1/3})\}\) has every phase as a subsequential limit: choose integers \(N\) nearest to \(1+\varphi^{3(k+s)}\). Continuity gives precisely the stated full interval.

## Verification

The accompanying `verify.py` performs 75 deterministic high-precision checks: Fibonacci identities, best-resonance inequalities in finite ranges, complete finite-mode comparisons for multiple parameter pairs, and the analytically predicted phase endpoints. It also exhibits quantitative convergence of four distinct phase subsequences to their nonidentical envelope values. The output is printed by running `python verify.py` with `mpmath` installed. Finite tests do not replace the continued-fraction and uniform-expansion arguments above.

## Relationship to prior work

Bianchi, Burchard, Gronchi, and Volčič (2012) prove convergence of every Kronecker-direction Steiner process for compact planar seeds, but do not provide the present linearized spectral norm or limiting phase constants. Carbone and Volčič (2026) prove qualitative convergence along the different Kakutani–Fibonacci direction ordering. Sun and Sun (2026) study a distinct **Minkowski fixed-rotation averaging** operator and obtain analytic stretched-exponential upper bounds with subsequential sharpness under Diophantine assumptions. That linear averaging problem has closely related Fourier multipliers; it does not, in its accessible stated results, provide the Fibonacci-only **exact finite-step minimizer**, full log-periodic profile, or both closed-form sharp envelope endpoints for the specified Steiner first variation. The accessible abstract of Sun and Sun is not a substitute for a full-text exclusion: see the limitations below.

## Limitations

The theorem does not estimate any finite-amplitude nonlinear Steiner iteration uniformly in \(N\). Its analytic input and Hilbert output norms are specified and essential. The oscillation uses the golden-ratio rotation and may take another form for other irrational rotations. Historical priority is limited by access to the full text of Sun and Sun (2026); their abstract explicitly covers the broad stretched-exponential order for a closely related linear averaging process. The claimed contribution must therefore be understood as the exact Fibonacci phase law and endpoints **in the Steiner linearization**, not as discovery of stretched-exponential smoothing in general. The results have not undergone independent mathematical validation.

## References

1. G. Bianchi, A. Burchard, P. Gronchi, A. Volčič, *Convergence in shape of Steiner symmetrizations*, Indiana University Mathematics Journal 61 (2012), 1695–1710; arXiv:1206.2041v1. https://arxiv.org/html/1206.2041v1
2. I. Carbone, A. Volčič, *Steiner symmetrization with respect to the Kakutani-Fibonacci sequence of directions*, arXiv:2603.00034v1 (first public 2026-02-05). https://arxiv.org/html/2603.00034v1
3. Y. Sun, B. Sun, *Fixed-rotation Minkowski averaging: classification and sharp rates*, Bulletin of the Australian Mathematical Society 114 (2026), 170–181, https://doi.org/10.1017/S0004972725100816
4. A. Ya. Khinchin, *Continued Fractions*, Dover edition (1997), for convergent best approximations and Fibonacci denominators.
