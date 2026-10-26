# Sharp fourth-moment envelope for correlated-turn swimmers in a harmonic trap

## Finding

For an isotropic stationary two-dimensional run-and-tumble swimmer in a harmonic trap, all reflection-symmetric **relative turning-angle laws with the same first angular Fourier coefficient** have the same mean-squared radius but an exactly classifiable interval of fourth radial moments. The lower endpoint comes from fixed-magnitude symmetric turns, and the upper endpoint from forward/reversal-only tumbles. The interval is sharp, strictly nondegenerate, and every intermediate value is attained. In the athermal high-tumble-rate limit, the normalized fourth moment exhibits a second-harmonic crossover between \(2\) and \(3\), despite identical first-mode persistence.

## Assumptions and scope

Let \(\kappa,v,\lambda>0\) and \(D\ge0\). In the plane, consider
\[
dX_t=(-\kappa X_t+v(\cos\Theta_t,\sin\Theta_t))\,dt+\sqrt{2D}\,dB_t.
\]
Here \(B_t\) is standard planar Brownian motion; at rate \(\lambda\), the orientation jumps by an independent angle \(\Psi\) modulo \(2\pi\), sampled from a reflection-symmetric probability law \(\Pi\). The jump law depends only on the turning *increment*, not the absolute direction. Initialize the orientation process with the uniform law on the circle and construct the canonical stationary position by convolution over the entire past. This defines a rotation-invariant joint stationary law, including for atomic turning distributions; no assertion of uniqueness among all orientation laws is needed.

Fix \(\mu_1=\mathbb E_\Pi[\cos\Psi]\in(-1,1)\). Set
\[
s=\lambda(1-\mu_1),\quad \mu_2=\mathbb E_\Pi[\cos(2\Psi)],\quad
 t=\lambda(1-\mu_2),\quad T=2\lambda(1-\mu_1^2).
\]
Define \(m_2=\mathbb E|X|^2\), \(m_4=\mathbb E|X|^4\), and the active second moment \(a_2=v^2/[\kappa(\kappa+s)]\). The admissible second-mode rate is exactly \(0\le t\le T\).

**Exact envelope.** For all turning laws in this class,
\[
 m_2=a_2+\frac{2D}{\kappa},\qquad
 m_4=\frac{2v^4(3\kappa+t)}{\kappa^2(\kappa+s)(3\kappa+s)(2\kappa+t)}
     +\frac{8D}{\kappa}a_2+\frac{8D^2}{\kappa^2}.
\]
Consequently the sharp maximum and minimum of \(m_4\), respectively, are
\[
 m_{4,\max}=\frac{3v^4}{\kappa^2(\kappa+s)(3\kappa+s)}
                 +\frac{8D}{\kappa}a_2+\frac{8D^2}{\kappa^2},
\]
\[
 m_{4,\min}=\frac{2v^4(3\kappa+T)}{\kappa^2(\kappa+s)(3\kappa+s)(2\kappa+T)}
                 +\frac{8D}{\kappa}a_2+\frac{8D^2}{\kappa^2}.
\]
The maximum occurs **only** when \(\Pi=(1+\mu_1)\delta_0/2+(1-\mu_1)\delta_\pi/2\). The minimum occurs **only** when \(\Pi=(\delta_\alpha+\delta_{-\alpha})/2\), where \(\alpha=\arccos\mu_1\). Uniqueness here means uniqueness of the reflection-symmetric probability law modulo angular-period identification. Convex mixtures attain every intermediate value, because they preserve \(\mu_1\) and vary \(t\) continuously.

**High-rate memory crossover.** With \(D=0\), fixed \(\kappa,v>0\), fixed \(\mu_1\in(-1,1)\), and \(\lambda\to\infty\), if \(t=\lambda(1-\mu_2)\to\eta\in[0,\infty]\), then
\[
\lim_{\lambda\to\infty}\frac{m_4}{m_2^2}=
2\frac{3\kappa+\eta}{2\kappa+\eta},
\]
with value \(2\) by continuity when \(\eta=\infty\), and value \(3\) when \(\eta=0\). Every finite \(\eta\) is achievable along an admissible family of turning laws. This is a statement about normalized *fourth moments*, not a claim of distributional convergence to a Gaussian.

**Identifiability.** When the mechanical parameters and \(D\) are known, the measured second radial moment determines \(s\), hence \(\mu_1\). Subtract the thermal contributions to recover the active fourth moment \(a_4\) and set
\[
 C=\frac{a_4\kappa^2(\kappa+s)(3\kappa+s)}{2v^4}.
\]
Then \(t=\kappa(3-2C)/(C-1)\) and \(\mu_2=1-t/\lambda\). Thus the stationary pair \((m_2,m_4)\) distinguishes the first two cosine harmonics of a symmetric turning law, although it does not reconstruct the full law.

## Proof

Write \(z=X_1+iX_2\) and \(u=e^{i\Theta}\). Temporarily set \(D=0\). Let \(a_j=\lambda(1-\mu_j)\), with \(a_0=0\). For integers \(p,q\ge0\), define the rotation-invariant mixed moments
\[
 R_{pq}=\mathbb E[z^p\bar z^q u^{q-p}].
\]
Because the turning-increment law is reflection symmetric, the orientation-jump generator acts on its \(j\)-th Fourier mode by multiplication by \(-a_{|j|}\). Applying the joint stationary generator to the displayed monomial gives, for \(p+q>0\),
\[
 ((p+q)\kappa+a_{|p-q|})R_{pq}
   =v\big(pR_{p-1,q}+qR_{p,q-1}\big),\quad R_{00}=1,
\]
where a term with negative index is omitted. Stationarity is justified by the bounded active coordinate \(|z|\le v/\kappa\), obtained from its exponentially weighted integral representation, and bounded Fourier monomials.

The first relevant steps are
\[
 R_{10}=\frac{v}{\kappa+s},\quad
 R_{11}=\frac{v^2}{\kappa(\kappa+s)},\quad
 R_{20}=\frac{2v^2}{(\kappa+s)(2\kappa+t)},
\]
\[
 R_{21}=\frac{v(2R_{11}+R_{20})}{3\kappa+s},\qquad
 R_{22}=\frac{vR_{21}}{\kappa}.
\]
The last two identities simplify to
\[
 R_{22}=\frac{2v^4(3\kappa+t)}{\kappa^2(\kappa+s)(3\kappa+s)(2\kappa+t)}.
\]
Since \(R_{11}=\mathbb E|z|^2\) and \(R_{22}=\mathbb E|z|^4\), this proves the athermal moment formulas. The recurrence remains valid even for turning laws supported on a finite subgroup, because the initially uniform orientation gives a stationary Haar marginal; rotational invariance selects the stated moments.

For \(D>0\), the full stationary position is the sum of the active integral and an **independent** centered isotropic Gaussian with per-coordinate variance \(D/\kappa\). Expanding the second and fourth squared radii conditionally yields precisely \(2D/\kappa\) in \(m_2\) and \(8(D/\kappa)a_2+8D^2/\kappa^2\) in \(m_4\), proving the thermal formulas.

To optimize over laws, let \(U=\cos\Psi\), so \(\mathbb EU=\mu_1\) and \(\mu_2=2\mathbb EU^2-1\). Jensen and \(|U|\le1\) imply \(2\mu_1^2-1\le\mu_2\le1\), hence \(0\le t\le T\). Equality at the lower \(\mu_2\) endpoint forces \(U\) constant; reflection symmetry therefore gives the stated symmetric fixed-angle law. Equality at the upper endpoint forces \(U\in\{-1,1\}\), with the uniquely determined endpoint weights. The only \(t\)-dependent factor in the active fourth moment is \((3\kappa+t)/(2\kappa+t)\), whose derivative is \(-\kappa/(2\kappa+t)^2<0\). This establishes strictness, both extremizers, and the entire interval.

For \(D=0\), divide the fourth-moment formula by the square of the second-moment formula to obtain
\[
 \frac{m_4}{m_2^2}=
 \frac{2(\kappa+s)(3\kappa+t)}{(3\kappa+s)(2\kappa+t)}.
\]
At fixed \(\mu_1<1\), \(s\to\infty\). Taking \(t\to\eta\), including infinite \(\eta\), proves the crossover. To realize a prescribed finite \(\eta\), for sufficiently large \(\lambda\) take a mixture of the maximal and minimal \(t\) extremizers in proportions giving \(t=\eta\); the admissible upper bound \(T\) grows linearly in \(\lambda\). Algebraic rearrangement of the two moment formulas proves the identifiability statement.

## Verification

The companion standalone program `verify_trapped_turns.py` checks the fourth-order generator recurrence symbolically; compares it with an independently assembled **16-variable real-space Markov stationary moment system on four headings**; and performs exact-event-time numerical sampling of the harmonic convolution for three distinct symmetric turning laws with identical first harmonic. Running `python verify_trapped_turns.py` with Python, NumPy and SymPy passed 21 check groups. In the transparent benchmark \(\kappa=v=\lambda=1\), \(D=0\), \(\mu_1=0\), all laws have \(m_2=1/2\), while symmetric right-angle turns, uniform turns, and forward/reversal turns have \(m_4=5/16,\ 1/3,\ 3/8\), respectively. The code tests finite examples; the above generator proof establishes the continuum claims.

## Relationship to prior work

Britton, Zhang, Han and Bertrand (2026) develop **free-space** dynamics for nonuniform **relative** reorientation and explain higher free-space moments' sensitivity to higher angular Fourier modes. The present analysis extends the question to an isotropic harmonic trap and determines the **sharp entire fourth-moment range at fixed first Fourier mode**, including equality cases and a high-tumbling non-Gaussian moment crossover.

Smith, Le Doussal, Majumdar and Schehr (2022) already solve the special two-dimensional **symmetric right-angle turning** harmonic-trap model, potentially including our \(\mu_1=0\) minimum example; neither its distribution nor that endpoint is claimed as new. Sun, Ye and Podgornik (2024) study finite tumble **durations** with independent direction redraws. Sun and collaborators (2025) treat a two-state active Brownian/tumble process with independent orientation redraws. Guéneau, Majumdar and Schehr (2026) solve the isotropic **independent post-tumble redraw** case, not correlated incremental turning. These works provide crucial related trap theory, but their stated models/results do not supply a sharp comparison over all symmetric correlated turning kernels with the same first harmonic. Algebraic higher-moment recurrences and Jensen's inequality are standard ingredients, not new claims here.

## Limitations

All parameters are fixed strictly positive except optional \(D=0\). The theorem assumes reflection symmetry of relative turns; chiral increments have complex Fourier harmonics and are not included. The law is the rotation-invariant stationary ensemble, even when an atomic jump law leaves the orientation process nonergodic on the entire circle. Only second and fourth radial moments, not the complete stationary density or transient paths, are classified. The high-tumble-rate crossover assumes \(D=0\) and does not establish a central-limit theorem. Exact experimental recovery assumes known coefficients and noiseless moments. The originality assessment is not independent; undiscovered broad moment theorems remain a residual possibility.

## References

1. C. Britton, Z. Zhang, S. Han, T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519v1 (public August 24, 2026), https://arxiv.org/abs/2608.23519.
2. N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (2022), https://arxiv.org/abs/2207.10445.
3. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (2024), https://arxiv.org/abs/2409.00578.
4. A. Sun, D. Wei, Y. Zhang, F. Ye, R. Podgornik, *Moment analysis of two-dimensional active Brownian run-and-tumble particles*, arXiv:2504.20352 (2025), https://arxiv.org/abs/2504.20352.
5. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (2026), https://arxiv.org/abs/2602.08436.
