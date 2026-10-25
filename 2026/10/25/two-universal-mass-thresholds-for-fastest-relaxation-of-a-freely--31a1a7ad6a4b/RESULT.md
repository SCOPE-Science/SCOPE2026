# Two universal mass thresholds for fastest relaxation of a freely translating damped dimer

## Finding

Two freely translating masses joined by a spring, with viscous damping applied to just the first mass, admit a complete and unique optimal-damping law. The dimensionless fraction \(\theta=m_1/(m_1+m_2)\) separates three distinct mechanisms at \(\theta=1/9\) and \(\theta=1/5\). The first threshold corresponds to a defective triple nonzero eigenvalue; below it the optimal configuration is a defective double eigenvalue; between the thresholds all three decay rates coincide without an eigenvalue collision; above the second threshold the slow complex pair reaches its own maximal decay rate.

Put \(\omega=\sqrt{k(1/m_1+1/m_2)}\), \(g=\gamma/(m_1\omega)\), and \(P_{g,\theta}(s)=s^3+gs^2+s+\theta g\). Define the dimensionless asymptotic nontranslation decay exponent
\[
R(g,\theta)=-\max\{\operatorname{Re}s:P_{g,\theta}(s)=0\}.
\]
For every \(0<\theta<1\) there is exactly one global maximizer \(g_*(\theta)>0\). Its value and optimal exponent are as follows.

For \(0<\theta<1/9\), let
\[
u_-={1-3\theta-\sqrt{(1-\theta)(1-9\theta)}\over2},\qquad r_-=\sqrt{u_-}.
\]
Then
\[
g_*={1+3u_-\over2r_-},\qquad R_*=r_-.
\]
For \(1/9\leq\theta\leq1/5\), put \(r_c=\sqrt{(1-3\theta)/2}\). Then
\[
g_*=3r_c,\qquad R_*=r_c.
\]
For \(1/5\leq\theta<1\),
\[
g_*={1+\theta\over2\sqrt\theta},\qquad R_*={1-\theta\over4\sqrt\theta}.
\]
Both formulas at \(\theta=1/5\) agree. At \(\theta=1/9\) the first formula agrees with the middle formula and \(P_{g_*,1/9}(s)=(s+1/\sqrt3)^3\). In physical units the optimized decay exponent is \(\omega R_*\), and the optimal physical damping is \(\gamma_*=m_1\omega g_*\).

## Assumptions and scope

Take \(m_1,m_2,k,\gamma>0\) and the autonomous linear equations
\[
m_1\ddot x_1=-k(x_1-x_2)-\gamma\dot x_1,\qquad m_2\ddot x_2=k(x_1-x_2).
\]
The only fixed point freedom is a uniform translation of both masses. We optimize the spectral exponential decay of deviations modulo that translation, not maximal transient amplification, vibration energy at a fixed time, decay under forcing, or an arbitrary matrix of damping coefficients. At a defective optimum the decay can include a polynomial prefactor, so the spectral exponent is the supremal asymptotic exponential rate rather than a bound with a fixed constant at the exact exponent.

## Proof

**Reduction and stability.** With \(y=x_1-x_2\) and \(v_i=\dot x_i\), the nontranslation state satisfies
\[
\dot y=v_1-v_2,\quad\dot v_1=-{k\over m_1}y-{\gamma\over m_1}v_1,\quad\dot v_2={k\over m_2}y.
\]
Scaling time by \(\omega\) gives characteristic polynomial \(P_{g,\theta}\). The four-dimensional displacement formulation adds exactly one zero root, associated with common translation. The cubic is Hurwitz: all coefficients are positive and \(g>\theta g\) because \(0<\theta<1\).

**Real-root parameterization.** Every cubic has a real negative root \(-r\) for \(r>0\). Substitution yields
\[
g=G(r)={r(1+r^2)\over r^2+\theta},\qquad G'(r)={r^4+(3\theta-1)r^2+\theta\over(r^2+\theta)^2}.
\]
For such a root the other two roots have sum \(-2\alpha(r)\), where
\[
\alpha(r)={G(r)-r\over2}={r(1-\theta)\over2(r^2+\theta)}.
\]
When those roots form a conjugate pair, their decay exponent is \(\alpha(r)\), and the full spectral exponent is \(\min\{r,\alpha(r)\}\). The function \(\alpha\) strictly increases to its unique maximum at \(r=\sqrt\theta\), then decreases. Equality \(r=\alpha(r)\) is equivalent to \(r^2=(1-3\theta)/2\), which is possible only for \(\theta<1/3\). At the equality, the other two roots are nonreal precisely for \(\theta>1/9\): their squared imaginary part is \((9\theta-1)/2\).

**No real-spectrum interval for \(\theta>1/9\).** The discriminant is
\[
\Delta=-4\theta g^4+(1+18\theta-27\theta^2)g^2-4.
\]
The discriminant of this quadratic in \(g^2\) is \((1-\theta)(1-9\theta)^3\), which is negative for \(\theta>1/9\). Consequently there is a single simple real negative root and a nonreal conjugate pair for every \(g>0\). Also \(G'(r)>0\). If \(1/9<\theta<1/5\), the crossing \(r_c=\sqrt{(1-3\theta)/2}\) lies strictly above \(\sqrt\theta\). Thus the minimum \(\min\{r,\alpha(r)\}\) increases up to \(r_c\) and decreases thereafter; its unique maximum is \(r_c\) at \(G(r_c)=3r_c\). If \(1/5\le\theta<1\), the universal bound \(R\le\alpha(r)\le\alpha(\sqrt\theta)\) is attained uniquely at \(r=\sqrt\theta\), because \(\alpha(\sqrt\theta)\le\sqrt\theta\) is exactly \(\theta\ge1/5\). This yields the final regime. At \(\theta=1/9\), \(G\) remains strictly increasing (its derivative only vanishes at one point); the same monotonic bottleneck analysis shows the unique optimum at \(r=1/\sqrt3\), with the stated triple root.

**The low-mass-fraction regime.** For \(0<\theta<1/9\), the numerator of \(G'\) vanishes at exactly two positive squared roots
\[
u_{\pm}={1-3\theta\pm\sqrt{(1-\theta)(1-9\theta)}\over2},\qquad 0<u_-<1/3<u_+.
\]
As \(g\) increases from zero, the cubic has one real root and a nonreal pair, then passes through a *fast-pair* collision associated with \(u_+\), enters a three-real-root interval, and leaves it through a *slow-pair* collision associated with \(u_-\). The orientation follows from the double-root factorization: if \(-r\) is a double root then the third root is \(-(1-r^2)/(2r)\); the double root is faster than the third one exactly when \(r^2>1/3\). In the first underdamped interval the unique real root is the slow mode (already true as \(g\downarrow0\), and real-part equality with the complex pair would require a negative squared imaginary part \((9\theta-1)/2\)); it grows strictly in decay rate since \(G'>0\) on its root branch. In the three-real interval the least-magnitude real negative root also grows strictly until it collides with the middle root at \(u_-\). Beyond this second collision the remaining simple real root is the fast mode, with magnitude \(r>1/\sqrt3>\sqrt\theta\); since \(G'>0\) on that branch, \(\alpha(r)\) strictly decreases. Hence the unique global maximum is the slow-pair collision \(r=\sqrt{u_-}\). The double-root equation \(G'(r)=0\) yields \(g=(1+3u_-)/(2\sqrt{u_-})\), as claimed.

**Multiplicity.** Every nonzero eigenvalue of the reduced three-dimensional system has a one-dimensional eigenspace: its eigenvector is fixed by its nonzero displacement difference \(y\). Therefore every algebraically repeated nonzero root is defective. At \(\theta=1/9\) the triple root is a single Jordan block of size three, rather than three independent modes. The proof also establishes uniqueness of each listed maximizer over *all* \(g>0\).

## Verification

The accompanying reproducible `check.py` checks the characteristic polynomial, derivative identities, discriminant and branch formulas symbolically, then compares both the cubic eigenvalues and the original physical four-state matrix numerically over independent parameter samples. Numerical checks test examples and guard against algebraic/transcription mistakes; the branch arguments above, not finite computation, establish the continuum result. Invoke `python check.py` after installing the versions specified in `requirements.txt`.

## Relationship to prior work

The general minimization of spectral abscissa under unrestricted damping matrices is classical; Freitas and Lancaster, *On the Optimal Value of the Spectral Abscissa for a System of Linear Oscillators* (1999), consider a different optimization domain. Cox and Overton (1996) studied critical damping and defective spectra of wave operators. Main and Krenk (2005) investigate viscous-damper tuning for discrete structures, while Dolfo and Vigué (2018) discuss coupled oscillators with a distinct anelastic damping law. Arnold, Gendelman, and Zharnitsky (2026) study optimal multiple eigenvalues for general two-degree-of-freedom stiffness and damping matrices. None of the accessible, materially inspected portions of these sources establishes the one-grounded-dashpot free-dimer classification and both sharp mass fractions above. This is a bounded priority assessment, not a proof that no equivalent treatment exists.

## Limitations

The mechanics are linear, damping is strictly positive and viscous relative to ground at one mass only, and the masses and spring are strictly positive. The translation zero mode is intentionally excluded from the rate. No result is claimed about an optimal damping matrix, robustness of eigenvalue collisions to parameter noise, or uniformly attained time-domain decay at defective points. Full access to all potentially relevant historic damping-design articles was unavailable; prior derivations of an equivalent specialized phase diagram remain a material residual originality risk. Independent validation has not been performed.

## References

- S. J. Cox and M. L. Overton, *Perturbing the Critically Damped Wave Equation*, SIAM J. Appl. Math. 56 (1996), 1353–1362. DOI: 10.1137/S0036139994277403.
- P. Freitas and P. Lancaster, *On the Optimal Value of the Spectral Abscissa for a System of Linear Oscillators*, SIAM J. Matrix Anal. Appl. 21 (1999), 195–208. DOI: 10.1137/S0895479897331850.
- J. A. Main and S. Krenk, *Efficiency and tuning of viscous dampers on discrete systems*, Journal of Sound and Vibration (2005). DOI: 10.1016/j.jsv.2004.09.022.
- A. Dolfo and J. Vigué, *Damping of coupled harmonic oscillators*, European Journal of Physics 39 (2018), 025005. DOI: 10.1088/1361-6404/aa9ec6.
- M. D. Arnold, O. V. Gendelman and V. Zharnitsky, *Critical damping in linear system with two degrees of freedom: surprises and pitfalls*, arXiv:2608.08656 (2026).
