# A fixed-step rescue frontier for an isolated stiff spectral band

## Finding

Fix a first, deliberately overlarge explicit Euler step of size \(K>0\). Suppose the positive eigenvalues of a symmetric positive-definite matrix \(A\) in a stiff cluster are known only to lie in \([\alpha,\beta]\), with \(2<K\alpha<K\beta\). Follow the first step by a freely chosen *positive* Euler step \(h\). Write \(x=K\alpha>2\), \(y=K\beta>x\), and \(\theta=h/K>0\). The two-step amplification on a scaled eigenvalue \(z=K\lambda\) is \(p_\theta(z)=(1-z)(1-\theta z)\). Define the robust cluster amplification \(M_*(x,y)=\min_{\theta>0}\max_{z\in[x,y]}|p_\theta(z)|\).

**Theorem (complete fixed-first-step minimax classification).** Put \(c=\sqrt2-1\) and \(x_c=1+c(y-1)\). The minimizer is unique. If \(2<x\le x_c\), put \(d=c(y-1)\); then
\[
 \theta_*={1\over1+2d},\qquad M_*(x,y)={d^2\over1+2d}.
\]
If \(x_c\le x<y\), put \(D=x(x-1)+y(y-1)\); then
\[
 \theta_*={x+y-2\over D},\qquad
 M_*(x,y)={(x-1)(y-1)(y-x)\over D}.
\]
At \(x=x_c\) the two expressions coincide. In every case \(1/y<\theta_*<1/x<1/2\).

The lower-edge-independent first branch exhibits a sharp **absolute-stability barrier**: it has \(M_*\le1\) if and only if \(y\le4+2\sqrt2\). Moreover, for each fixed \(\Delta>0\),
\[
 \lim_{y\to\infty} M_*(y-\Delta,y)={\Delta\over2}.
\]
Thus arbitrarily high but sufficiently narrow normalized stiff clusters admit stable rescue by one step, whereas clusters of fixed normalized width greater than two cannot be uniformly rescued by just one step once the upper frequency is sufficiently large.

If the remaining eigenvalues of \(A\) additionally lie in \((0,2/K]\), the optimal correction is nonexpansive on this slow group: \(|p_{\theta_*}(K\lambda)|\le1\) for every such eigenvalue. Hence whenever \(M_*\le1\), the complete two-stage map is a Euclidean nonexpansion on every symmetric positive-definite matrix whose spectrum lies in \((0,2/K]\cup[\alpha,\beta]\). This is a robust sufficient statement, not a necessity assertion for a particular finite spectrum.

## Assumptions and scope

The setting is the linear dissipative initial-value problem \(u'(t)=-Au(t)\), \(A=A^{\mathsf T}\succ0\), under exact arithmetic. The operator-norm guarantee concerns an interval uncertainty model in which every real normalized eigenvalue in \([x,y]\) must be handled. The first Euler step \(K\) is fixed in advance, and only the single second step \(h>0\) is optimized. Neither stage is assumed to be contractive separately; on the stiff band the first stage has amplification magnitude strictly greater than one. A zero eigenvalue is not included, although the scalar formula extends continuously to zero with multiplier one. There are no assumptions on spectral multiplicity or matrix dimension.

## Proof

For \(z>1\), set \(f_\theta(z)=(z-1)(1-\theta z)=-p_\theta(z)\). It is a strictly concave quadratic in \(z\), and for every fixed \(z>1\) it is strictly decreasing in \(\theta\). If \(\theta\le1/y\), the whole interval has \(f_\theta\ge0\), so increasing \(\theta\) strictly decreases its maximal absolute value. If \(\theta\ge1/x\), the whole interval has \(f_\theta\le0\), so decreasing \(\theta\) strictly decreases its maximal absolute value. Every minimizer therefore lies in \((1/y,1/x)\).

Within that interval, \(f_\theta(x)>0>f_\theta(y)\). Its most negative value is \(f_\theta(y)\); its positive maximum is attained at either \(x\) or the interior vertex \(v_\theta=(1+\theta)/(2\theta)\). As \(\theta\) increases, the positive maximum decreases strictly (as long as it is positive), whereas \(-f_\theta(y)=(y-1)(\theta y-1)\) increases strictly. Consequently their crossing exists and is the unique global minimizer.

If the vertex lies inside the interval at the crossing, let \(s=v_\theta-1\), so \(\theta=1/(1+2s)\) and \(f_\theta(v_\theta)=s^2/(1+2s)\). Equating this with \(-f_\theta(y)\) gives \(s^2=(y-1)(y-1-2s)\), whose unique positive solution satisfying the interior geometry is \(s=(\sqrt2-1)(y-1)=d\). The vertex is at \(x_c=1+d\), and it is admissible precisely when \(x\le x_c\). This proves the first branch, including uniqueness.

Otherwise the positive maximum lies at \(x\). Equate the two endpoints:
\[
 (x-1)(1-\theta x)=-(y-1)(1-\theta y).
\]
Solving yields \(\theta=(x+y-2)/D\), and direct substitution gives \(M_*=(x-1)(y-1)(y-x)/D\). The vertex does not exceed \(x\) exactly for \(x\ge x_c\), as follows by substituting this expression into \(v_\theta\le x\), or by continuity and the uniqueness of the monotone crossing. Equality of the branch expressions holds at \(x=x_c\). Since the crossing was strictly between \(1/y\) and \(1/x\), the step inequalities follow; \(x>2\) implies \(\theta_*<1/2\).

In the first branch, \(M_*=d^2/(1+2d)\). Since \(d>0\), the inequality \(M_*\le1\) is equivalent to \(d\le1+\sqrt2\), or \(y\le4+2\sqrt2\), using \(d=(\sqrt2-1)(y-1)\). For fixed \(\Delta>0\), the condition \(x=y-\Delta\ge x_c\) holds for all sufficiently large \(y\), so the second formula applies. Dividing its numerator and denominator by \(y^2\) gives the limit \(\Delta/2\).

Finally, on \(0\le z\le2\) we have \(|1-z|\le1\), and \(0<\theta_*<1/2\) gives \(0<1-\theta_*z\le1\). Thus \(|p_{\theta_*}(z)|\le1\). Orthogonal diagonalization of \(A\) transfers the scalar bounds to its Euclidean operator norm. This completes the proof.

## Verification

The accompanying standalone `verify_rescue.py` uses Python's standard library, checks the formula for 1,600 representative uncertainty bands and the exact continuous-interval quadratic maximum, compares 19,200 alternative second steps, and verifies 1,200 endpoint equioscillation identities with exact rational arithmetic. It also checks the first-branch stability boundary and representative large-frequency bandwidth limits. Run `python verify_rescue.py`; the deterministic expected status begins `VERIFY_OK`. These finite checks are supplementary; the argument above proves the universally quantified theorem for all real \(2<x<y\).

## Relationship to prior work

Eriksson, Johnson, and Logg (2003), *Explicit Time-Stepping for Stiff ODEs*, derive stabilizing small-step packets following large unstable explicit steps. In their §2, the basic scalar factor is \((1-k\lambda)^m(1-K\lambda)\), with a sufficient number of corrections for a given stiff frequency. Their §§3–4 discuss stiff spectral separation, polynomial stabilization, and computational costs. The present result fixes \(m=1\) and optimizes its only free correction against *all frequencies in a specified continuous high-frequency interval*, supplying an exact lower-edge-independent regime, its transition to endpoint equioscillation, and a sharp robustness boundary. It does not claim to invent the stabilization mechanism.

Van Leer, Tai, and Powell (1989) analyze optimally smoothing multistage schemes for the Euler equations using complex Fourier symbols and freely chosen predictor-stage parameters. Their analyzed stability sets and free-parameter problems do not state the present fixed-first-Euler-factor real interval minimax formula. The published note *Sharp stagewise-safe Richardson frontier and a no-acceleration barrier* (2026) requires **both** factors to be individually nonexpansive and optimizes **both** steps; that condition excludes the present prescribed, unstable first factor \(K\). Classical Chebyshev theory optimizes more general polynomial factors and provides context but does not by itself give the two-case fixed-root formula without solving this constrained problem.

## Limitations

The result concerns real positive eigenvalues, a symmetric positive-definite operator, exact arithmetic, and a predetermined oversized first step. It is not an error-versus-work comparison or a floating-point stability analysis, and is not a guarantee for nonnormal operators, complex spectra, time-dependent coefficients, or nonlinear equations. Optimality is *interval-robust*: a known finite set of discrete eigenvalues may permit a better tailored correction. The bound \(M_*\le1\) ensures nonexpansion, not a strict reduction at every frequency if equality occurs. Historical priority cannot be guaranteed from the checked sources, particularly less-indexed fixed-root approximation literature.

## References

1. K. Eriksson, C. Johnson, and A. Logg, “Explicit Time-Stepping for Stiff ODEs,” *SIAM Journal on Scientific Computing* **25** (2003), 1142–1157. DOI: https://doi.org/10.1137/S1064827502409626 ; freely accessible version: https://arxiv.org/abs/1205.2751 . The original journal article states an electronic publication date of 2003-12-05.
2. B. van Leer, C.-H. Tai, and K. G. Powell, “Design of Optimally Smoothing Multi-Stage Schemes for the Euler Equations,” technical paper, 1989. https://ntrs.nasa.gov/citations/19890014641 .
3. G. H. Golub and R. S. Varga, “Chebyshev semi-iterative methods, successive overrelaxation iterative methods, and second order Richardson iterative methods,” *Numerische Mathematik* **3** (1961), Parts I–II. https://doi.org/10.1007/BF01386013 and https://doi.org/10.1007/BF01386014 .
4. “Sharp stagewise-safe Richardson frontier and a no-acceleration barrier,” published mathematical note (2026): https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-stagewise-safe-two-step-richardson-frontier--31fff666d705 .
