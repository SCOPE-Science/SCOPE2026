# Exact diffusion and large deviations for a staggered quantum stochastic walk

## Finding

For a continuous-time quantum stochastic walk on the integer chain with homogeneous coherent hopping and parity-dependent **directional** incoherent jumps, a common total escape rate yields an exactly solvable, two-sublattice transport law. The result holds for every strictly positive set of the four local directional rates with the same total escape rate, every nonzero real coherent hopping amplitude, and either initially localized parity.

Let \(\gamma_{0,+},\gamma_{0,-},\gamma_{1,+},\gamma_{1,-}>0\) satisfy
\[
\gamma_{0,+}+\gamma_{0,-}=\gamma_{1,+}+\gamma_{1,-}=\Gamma>0.
\]
Put \(d_a=\gamma_{a,+}-\gamma_{a,-}\), \(\bar d=(d_0+d_1)/2\), and \(B=\sqrt{\Gamma^2+16h^2}\). If \(X_t\) denotes the site observed at time \(t\), starting from site zero or any other single localized site, then
\[
\boxed{\lim_{t\to\infty}\frac{\mathbb E X_t-X_0}{t}=\bar d},
\qquad
\boxed{\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{t}
=\Gamma+\frac{4h^2}{\Gamma}-\frac{(d_0-d_1)^2}{2(\Gamma+B)}.}
\]
The asymptotic variance per unit time increases strictly with \(|h|\) for positive \(|h|\), whereas the drift stays fixed. Compared with the purely incoherent walk, coherent hopping weakens the diffusion penalty due to alternating directional bias by the exact factor \(2\Gamma/(\Gamma+B)\).

More strongly, the full scaled cumulant generating function \(\Lambda(\theta)=\lim_{t\to\infty}t^{-1}\log\mathbb E[e^{\theta(X_t-X_0)}]\) is the **unique** real solution \(z>4|h\sinh(\theta/2)|-\Gamma\) of
\[
1-\frac{C_0(\theta)+C_1(\theta)}2\bigl(g_I(\theta,z)-g_J(\theta,z)\bigr)
-C_0(\theta)C_1(\theta)g_I(\theta,z)g_J(\theta,z)=0,
\]
where
\[
C_a(\theta)=\gamma_{a,+}e^{\theta}+\gamma_{a,-}e^{-\theta},\quad
g_I(\theta,z)=\bigl[(z+\Gamma)^2-16h^2\sinh^2(\theta/2)\bigr]^{-1/2},
\]
\[
g_J(\theta,z)=\bigl[(z+\Gamma)^2+16h^2\cosh^2(\theta/2)\bigr]^{-1/2}.
\]
All square roots here are positive real. In particular, the empirical velocity \((X_t-X_0)/t\) satisfies the full large-deviation principle with good convex rate function \(I(v)=\sup_{\theta\in\mathbb R}\{\theta v-\Lambda(\theta)\}\).

## Assumptions and scope

The one-particle Hilbert space is \(\ell^2(\mathbb Z)\) with site basis \(|j\rangle\). Define \(S|j\rangle=|j+1\rangle\) and \(H=h(S+S^\dagger)\) for arbitrary real \(h\ne0\). The density operator obeys the trace-preserving Lindblad equation
\[
\dot\rho=-i[H,\rho]+\sum_{j\in\mathbb Z}\sum_{\sigma\in\{+,-\}}
\left(L_{j,\sigma}\rho L_{j,\sigma}^\dagger-\frac12\{L_{j,\sigma}^\dagger L_{j,\sigma},\rho\}\right),
\]
with \(L_{j,+}=\sqrt{\gamma_{j\bmod2,+}}|j+1\rangle\langle j|\) and
\(L_{j,-}=\sqrt{\gamma_{j\bmod2,-}}|j-1\rangle\langle j|\). The initial state is \(|j_0\rangle\langle j_0|\), where \(j_0\) is any fixed integer. All rates are strictly positive and the total escape rate is identical on both sublattices. There is no additional on-site dephasing, potential, detector, or boundary.

## Proof

**1. Jump-unraveling and coherent parity kernels.** Since \(\sum_{j,\sigma}L_{j,\sigma}^\dagger L_{j,\sigma}=\Gamma\mathbf1\), jump times form a homogeneous Poisson process of rate \(\Gamma\). Between consecutive jumps, the normalized state evolves as \(e^{-iHs}|j\rangle\); a jump measures its occupied site and then shifts it one step. The no-jump site probability is \(J_r(2hs)^2\), starting from a localized site. The Bessel addition theorem gives, for any real \(\theta\),
\[
\sum_{r\in\mathbb Z}e^{\theta r}J_r(2hs)^2=I_0(4hs\sinh(\theta/2)),\quad
\sum_{r\in\mathbb Z}(-1)^re^{\theta r}J_r(2hs)^2=J_0(4hs\cosh(\theta/2)).
\]
Here \(I_0\) and \(J_0\) are the modified and ordinary order-zero Bessel functions. Consequently the displacement-weighted coherent segment kernels with even and odd displacement are, respectively, \(U_\theta(s)=(I_0+J_0)/2\) and \(V_\theta(s)=(I_0-J_0)/2\), with the displayed arguments. Both are nonnegative because each equals a sum of nonnegative weighted probabilities. Their Laplace transforms after multiplying by \(e^{-\Gamma s}\) are
\[
\widehat U=(g_I+g_J)/2,\qquad \widehat V=(g_I-g_J)/2,
\]
using \(\int_0^\infty e^{-qs}I_0(as)\,ds=(q^2-a^2)^{-1/2}\) and \(\int_0^\infty e^{-qs}J_0(as)\,ds=(q^2+a^2)^{-1/2}\) in their convergence domains.

**2. Exact two-parity renewal equation.** Let \(M_a(\theta,t)\) be the displacement-weighted mass ending on parity \(a\), decomposed at the first jump. A coherent segment from parity \(b\) reaches its own parity with kernel \(U\) or the opposite parity with kernel \(V\). An incoherent jump originating at parity \(a\) flips parity and multiplies its tilt weight by \(C_a(\theta)\). Thus the matrix of weighted completed-jump renewal kernels has Laplace transform
\[
K(\theta,z)=\begin{pmatrix}
C_1(\theta)\widehat V&C_1(\theta)\widehat U\\
C_0(\theta)\widehat U&C_0(\theta)\widehat V
\end{pmatrix}.
\]
The remaining final no-jump segment is governed by the same \(U,V\) kernels. Summing any number of completed jumps gives a matrix geometric resolvent \((\mathbf1-K)^{-1}\) multiplied by the final-segment transform. Direct expansion yields \(\det(\mathbf1-K)=1-(C_0+C_1)(g_I-g_J)/2-C_0C_1g_Ig_J\), exactly the claimed equation. The renewal representation gives the full Laplace transform of each parity-resolved moment-generating function; it is not a statement only about a reduced two-state density matrix.

**3. Existence and uniqueness of the dominant exponent.** For real \(\theta\), all \(C_a\) are positive. On \(z>4|h\sinh(\theta/2)|-\Gamma\), every entry of \(K\) is strictly positive for \(h\ne0\). Its Perron root is continuous and strictly decreases from infinity to zero as \(z\) increases from the lower endpoint to infinity, because \(g_I\) diverges at the lower endpoint and all Laplace kernels strictly decrease with \(z\). Hence exactly one \(z=\Lambda(\theta)\) has Perron root one; the other eigenvalue cannot supply an equally dominant positive eigenvector. Multiplying the positive renewal kernels by \(e^{-\Lambda(\theta)t}\), the finite-state nonlattice Markov-renewal theorem applies: the resulting kernels have finite first moments and continuous nonzero densities, so the tilted moment-generating functions have a finite strictly positive leading prefactor. Their logarithmic growth is therefore \(\Lambda(\theta)\). The simple Perron crossing varies analytically near zero, and exponential moments of the segment increments exist in a neighborhood of every real tilt. Analytic renewal perturbation gives the limiting first two cumulant rates as \(\Lambda'(0)\) and \(\Lambda''(0)\). The same positivity, differentiability for all real tilts, and the fact that \(|\Lambda'(\theta)|\to\infty\) at both ends establish the full large-deviation principle by the Gärtner–Ellis theorem.

**4. Derivatives and sharp diffusion law.** Put \(D=(d_0-d_1)/2\) and \(C(\theta)=\Gamma\cosh\theta+\bar d\sinh\theta\). The determinant simplifies exactly to
\[
F(\theta,z)=\bigl(1-C(\theta)g_I\bigr)\bigl(1+C(\theta)g_J\bigr)
+D^2\sinh^2(\theta)g_Ig_J.
\]
At the base point \((\theta,z)=(0,0)\), one has \(g_I=1/\Gamma\), \(g_J=1/B\), \(F=0\), and \(\partial_zF=(1+\Gamma/B)/\Gamma>0\). The factorized equation with \(D=0\) gives the homogeneous tilted root \(\sqrt{C(\theta)^2+16h^2\sinh^2(\theta/2)}-\Gamma\), whose first and second derivatives at zero are \(\bar d\) and \(\Gamma+4h^2/\Gamma\). The extra term \(D^2\sinh^2(\theta)g_Ig_J\) has zero first derivative and second derivative \(2D^2/(\Gamma B)\) at zero. Implicit differentiation therefore changes only the curvature, by exactly \(-2D^2/(\Gamma+B)\). This proves both boxed expressions.

For the purely incoherent comparison \(h=0\), the same root equation reduces to \(\Lambda(\theta)=\sqrt{C_0(\theta)C_1(\theta)}-\Gamma\), with variance rate \(\Gamma-(d_0-d_1)^2/(4\Gamma)\). For nonzero \(h\), the alternating-bias penalty is multiplied by \(2\Gamma/(\Gamma+\sqrt{\Gamma^2+16h^2})\), strictly below one. The additive \(4h^2/\Gamma\) is also strictly increasing with \(|h|\). Thus coherent hopping strictly increases the asymptotic variance rate, but not the drift.

## Verification

The accompanying `verify.py` independently evaluates the unique positive-kernel root and its first two numerical derivatives for six parameter families, including highly asymmetric and near-classical limits. It also directly propagates the full density matrix on a 91-site chain using the unreduced sparse Lindblad superoperator; at two late times the measured slope of the first two position cumulants agrees with the predicted infinite-line drift and variance rate. The verifier does not impose the renewal reduction on the density-matrix calculation. Run it with `python verify.py` after installing the versions in `requirements.txt`. The numerical checks cover finite time and finite chains only; the proof above covers all real tilts, all allowed rates, and arbitrarily long time.

## Relationship to prior work

Rodríguez-Rosario, Whitfield and Aspuru-Guzik (2009) introduced quantum stochastic walks with graph-local Lindblad hopping and studied line transport; their model is the starting point, not claimed as new. Domino and collaborators (first preprint 2016) analyze homogeneous local versus global dissipation, especially spreading exponents, rather than the exact parity-staggered directional-jump diffusivity. Shapira and Cohen (first preprint 2019) study biased quantum transport and spatial disorder using an Ohmic bath formulation and perturbative spectral results. Avnit and Cohen (first preprint 2023), Eq. (31), give the homogeneous biased spectral dispersion, which directly covers the \(d_0=d_1\) limit of the present formula; that case is **not** presented as a new theorem. Their clean dispersion does not directly yield the parity-dependent penalty, which requires the two-sublattice renewal determinant. The 1977 paper by Madhukar and Post on dynamic disorder is conceptually related but was accessible here only at abstract level; it remains a priority-comparison risk rather than evidence of noncoverage.

## Limitations

This is an exact statement for a single particle with homogeneous nearest-neighbor coherent hopping, **strictly positive** parity-periodic local jump rates, equal total escape rate across parity, and an initially localized site. It does not apply directly to arbitrary periodicity, unequal escape totals, Hamiltonian disorder or interactions, partial measurement records, or a thermal bath with additional correlation constraints. The independent numerical implementation checks finite examples and cannot establish the infinite-chain limit or publication priority. An earlier treatment of general spatially inhomogeneous Lindblad transport might imply this specialization; this has not been independently ruled out.

## References

1. C. A. Rodríguez-Rosario, J. D. Whitfield, A. Aspuru-Guzik, *Quantum stochastic walks: A generalization of classical random walks and quantum walks*, arXiv:0905.2942v1 (2009), https://arxiv.org/abs/0905.2942.
2. K. Domino, A. Glos, M. Ostaszewski, Ł. Pawela, P. Sadowski, *Properties of quantum stochastic walks from the asymptotic scaling exponent*, arXiv:1611.01349v1 (2016), https://arxiv.org/abs/1611.01349.
3. D. Shapira, D. Cohen, *Quantum stochastic transport along chains*, arXiv:1907.01993v1 (2019), https://arxiv.org/abs/1907.01993.
4. B. Avnit, D. Cohen, *Quantum walk in stochastic environment*, arXiv:2308.08419v1 (2023), https://arxiv.org/abs/2308.08419.
5. A. Madhukar, W. Post, *Exact Solution for the Diffusion of a Particle in a Medium with Site Diagonal and Off-Diagonal Dynamic Disorder*, Physical Review Letters 39, 1424 (1977), https://doi.org/10.1103/PhysRevLett.39.1424.
