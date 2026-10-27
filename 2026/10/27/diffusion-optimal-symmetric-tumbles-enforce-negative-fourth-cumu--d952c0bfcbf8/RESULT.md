# Diffusion-optimal symmetric tumbles enforce negative fourth-cumulant growth in chiral active motion

## Finding

**Theorem.** For the planar chiral active particle specified below, the unique symmetric-tumble rate optimizing long-time mean-square spreading always makes the limiting fourth-cumulant growth of any Cartesian displacement **strictly negative**. This remains true for every symmetric relative-angle turning distribution, whether discrete or continuous. Nevertheless, positive fourth-cumulant growth is possible at nonoptimal tumble rates, so the sign restriction reflects optimization rather than an unconditional property of the model.

Put \(\Omega=|\omega|\), \(c_j=\int\cos(j\alpha)\,\nu(d\alpha)\) for \(j=1,2\), and
\[
a=d+\lambda(1-c_1),\qquad b=4d+\lambda(1-c_2).
\]
For every fixed nonnegative \(\lambda\), the exact second- and fourth-cumulant **growth rates** of the Cartesian displacement \(Z_T\) are
\[
S_2=\lim_{T\to\infty}\frac{\kappa_2(Z_T)}T=\frac{v^2a}{a^2+\Omega^2},
\]
\[
S_4=\lim_{T\to\infty}\frac{\kappa_4(Z_T)}T=
\frac{3v^4\big[a^4b-2a^3b^2-12a^3\Omega^2+2ab^2\Omega^2+4a\Omega^4-b\Omega^4\big]}
{(a^2+\Omega^2)^3(b^2+4\Omega^2)}.
\]
The unique maximizing rate of \(S_2\) over \(\lambda\ge0\) is
\[
\lambda_* = \frac{(\Omega-d)_+}{1-c_1},\qquad
b_*=4d+\lambda_*(1-c_2).
\]
At this optimum, the fourth cumulant obeys
\[
S_4(\lambda_*)=\begin{cases}
-\displaystyle\frac{3v^4}{\Omega(b_*^2+4\Omega^2)}, & \Omega>d,\\[6pt]
-\displaystyle\frac{3v^4d^3(7d^2-5\Omega^2)}{(d^2+\Omega^2)^3(4d^2+\Omega^2)}, & 0\le\Omega\le d.
\end{cases}
\]
Both branches are negative and agree at \(\Omega=d\). For the dimensionless one-coordinate excess kurtosis \(G_T=\mathbb E[Z_T^4]/(\mathbb E[Z_T^2])^2-3\), we also have
\[
\lim_{T\to\infty}T G_T=\begin{cases}
-\displaystyle\frac{12\Omega}{b_*^2+4\Omega^2},&\Omega>d,\\[6pt]
-\displaystyle\frac{3d(7d^2-5\Omega^2)}{(d^2+\Omega^2)(4d^2+\Omega^2)},&0\le\Omega\le d.
\end{cases}
\]
The interior-optimum diffusion coefficient depends only on \(\Omega\), whereas the magnitude of its first non-Gaussian correction retains information about \(c_2\), the *second* angular Fourier moment of the turn law.

## Assumptions and scope

Take \(v>0\), angular diffusion \(d>0\), fixed chirality \(\omega\in\mathbb R\), and a Poisson clock with constant rate \(\lambda\ge0\). Between clock rings, \(d\theta_t=\omega\,dt+\sqrt{2d}\,dB_t\) modulo \(2\pi\); at each ring independently add a circular angle drawn from a symmetric Borel probability measure \(\nu\), so \(\nu(E)=\nu(-E)\) modulo \(2\pi\). The position starts from zero, evolves as \(dX_t=v(\cos\theta_t,\sin\theta_t)\,dt\), and has no independent translational Brownian term. Initially \(\theta_0\) is uniform on the circle and independent of future noise and jumps. Define \(Z_T\) as its first coordinate. A fixed coordinate rotation has the same law because the heading process is rotation equivariant. Assume \(c_1<1\), excluding turns that are almost surely invisible; otherwise optimizing the rate is nonunique. The fourth cumulant is \(\kappa_4(Z_T)=\mathbb E[Z_T^4]-3(\mathbb E[Z_T^2])^2\), since the mean is zero. All limits hold for fixed parameters as \(T\to\infty\).

## Proof

**1. Spectral gap and analytic cumulants.** The angular backward generator acting on smooth periodic functions is
\[
Lf=d f''+\omega f'+\lambda\int\big[f(\theta+\alpha)-f(\theta)\big] \nu(d\alpha).
\]
On the Fourier mode \(e^{in\theta}\) it acts as multiplication by \(-\mu_n\), where
\[
\mu_n=n^2d+\lambda(1-c_n)-in\omega,\quad c_n=\int\cos(n\alpha)\nu(d\alpha).
\]
Symmetry makes each \(c_n\) real, \(\mu_{-n}=\overline{\mu_n}\), and \(\Re\mu_n\ge n^2d\). In particular, \(0\) is a simple isolated eigenvalue; all nonzero modes have real part at most \(-d\). The Feynman–Kac operator \(L+k v\cos\theta\) is a bounded analytic perturbation in real \(k\). Its simple eigenvalue \(\Lambda(k)\) emanating from zero is analytic near \(k=0\). For uniform initial heading, its associated spectral projection has nonzero analytic coefficient equal to one at \(k=0\). Consequently the cumulant-generating function satisfies \(\log\mathbb E e^{kZ_T}=T\Lambda(k)+O_k(1)+O_k(e^{-cT})\) locally in \(k\), including four derivatives at zero, for some \(c>0\). This proves \(\kappa_j(Z_T)/T\to\Lambda^{(j)}(0)\) for \(j=2,4\). The evenness in \(k\) follows from invariance under rotating heading by \(\pi\).

**2. Fourth-order perturbation.** Normalize the perturbed eigenfunction so its zeroth Fourier coefficient is one, and denote its other coefficients by \(u_n(k)\). They satisfy
\[
(\mu_n+\Lambda)u_n=\frac{kv}{2}(u_{n-1}+u_{n+1}),\quad n\ne0,
\qquad \Lambda=\frac{kv}{2}(u_{-1}+u_1).
\]
Write \(\mu_1=a-i\omega\), \(\mu_2=b-2i\omega\). The small-\(k\) recursions give
\[
u_1=\frac{kv}{2\mu_1}+\frac{(kv)^3}{8\mu_1^2\mu_2}-\frac{kv\,\Lambda}{2\mu_1^2}+O(k^5),\qquad
u_2=\frac{(kv)^2}{4\mu_1\mu_2}+O(k^4).
\]
It follows that
\[
\Lambda(k)=\frac{v^2}{2}\Re\!\left(\frac1{\mu_1}\right)k^2+
 v^4\left[\frac18\Re\!\left(\frac1{\mu_1^2\mu_2}\right)-\frac14\Re\!\left(\frac1{\mu_1}\right)\Re\!\left(\frac1{\mu_1^2}\right)\right]k^4+O(k^6).
\]
The third angular harmonic cannot enter at order four because reaching mode \(\pm3\) and returning to mode zero requires at least six nearest-neighbor Fourier steps. Multiplying the coefficients by \(2!\) and \(4!\) gives the displayed \(S_2\) and \(S_4\). Straight rationalization yields the polynomial formula; the original complex-resolvent expression is also an exact certificate against algebraic sign errors.

**3. Optimization and sign.** Since \(1-c_1>0\), \(a\) is a strictly increasing affine function of \(\lambda\) ranging from \(d\) to infinity. Differentiating \(a/(a^2+\Omega^2)\) shows it is increasing until \(a=\Omega\) and then decreasing, giving the unique optimizer. When \(\Omega>d\), substitute \(a=\Omega\) into the complex-resolvent expression (equivalently, the rationalized expression) to obtain \(S_4=-3v^4/[\Omega(b_*^2+4\Omega^2)]\). Its denominator is positive. When \(\Omega\le d\), \(\lambda_*=0\), hence \(a=d\) and \(b=4d\), producing the second branch. Here \(7d^2-5\Omega^2\ge2d^2>0\). At \(\Omega=d\), both branches equal \(-3v^4/(20d^3)\). Since \(S_2>0\), the definition of cumulants gives \(G_T=\kappa_4(Z_T)/\kappa_2(Z_T)^2\), and thus \(TG_T\to S_4/S_2^2\), as stated.

**4. Positive nonoptimal comparison.** To see the sign is not automatically negative, take \(v=d=1\), \(\omega=2\), and an equal mixture of the four turning angles \(\pm\pi/12\) and \(\pm11\pi/12\). Then \(c_1=0\), \(c_2=\sqrt3/2\), and \(\lambda_*=1\). Direct substitution into the exact formula gives \(S_4(\lambda_*)\approx-0.0453312637\), whereas \(S_4(20)\approx2.07067327\times10^{-5}>0\). No claim is made that \(\lambda=20\) is statistically optimal.

## Verification

The standalone `check.py` recomputes the rational fourth-cumulant formula from the Fourier resolvents using exact symbolic simplification; checks both optimizing branches and matching boundary; numerically extracts the quartic eigenvalue coefficient from independent five-mode Feynman–Kac matrices at high precision; and tests the optimizer and sign on 350 deterministic admissible parameter draws. At the time of assessment it passed 2,822 assertions. Finite-dimensional matrices independently test the Taylor coefficients through order four because the neglected third and higher harmonics cannot contribute at that order; these computations corroborate, but do not substitute for, the spectral proof. Run `python check.py` with `sympy` and `mpmath` installed.

## Relationship to prior work

Olsen and Löwen (arXiv:2405.14326, 2024) established the generalized chiral-tumble model and optimized its effective diffusivity using first-harmonic orientation correlations, including the universal optimum for symmetric turns. Their derivations concern first and second displacement moments; they do not derive the fourth-cumulant sign at this optimum. Villa-Torrealba and collaborators (arXiv:2002.02872, 2020) calculated fourth moments and excess kurtosis of planar run-and-tumble swimmers with relative-angle turns without chiral drift, and separately examined direction reversals with angular diffusion. Their work demonstrates that some nonoptimal strategies exhibit positive kurtosis; it does not address simultaneous nonzero chirality, optimized tumble rate, and the universal sign conclusion proved here. Pattanayak and collaborators (arXiv:2404.09650, 2024) derived fourth moments for chiral active Brownian motion without Poisson relative-angle turns. These analyses motivate the present cross-parameter result but do not directly state its optimization–fluctuation implication. Broader spectral perturbation identities for additive functionals are mathematically related; priority against every possible general formulation has not been independently determined.

## Limitations

No sign assertion is made for arbitrary finite observation time, for nonsymmetric turn distributions, for a turn law depending on the current orientation, for non-Poisson tumble intervals, or for zero rotational diffusion. The current formula assumes no translational Brownian displacement; adding an independent Brownian component leaves the fourth-cumulant growth unchanged but modifies the displayed normalized excess-kurtosis coefficient. The exact general fourth-rate expression uses two angular cosine moments, but the new sign restriction depends on tuning the rate to optimize the *second*-cumulant growth. Originality assessment is based on the cited primary literature and targeted searches, not on an exhaustive priority certificate.

## References

1. K. S. Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326 (first public 2024-05-23), Phys. Rev. E **110**, 064606 (2024), DOI:10.1103/PhysRevE.110.064606.
2. A. Villa-Torrealba, C. Chávez-Raby, P. de Castro, and R. Soto, *Run-and-tumble bacteria slowly approaching the diffusive regime*, arXiv:2002.02872 (first public 2020-02-07), Phys. Rev. E **101**, 062607 (2020), DOI:10.1103/PhysRevE.101.062607.
3. A. Pattanayak, A. Shee, D. Chaudhuri, and A. Chaudhuri, *Impact of chirality on active Brownian particle: Exact moments in two and three dimensions*, arXiv:2404.09650 (first public 2024-04-15), New J. Phys. **26**, 083024 (2024), DOI:10.1088/1367-2630/ad6a32.
