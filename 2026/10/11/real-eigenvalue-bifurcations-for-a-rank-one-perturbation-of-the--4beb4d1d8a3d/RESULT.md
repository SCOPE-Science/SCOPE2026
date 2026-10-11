# Real-eigenvalue bifurcations for a rank-one perturbation of the normal Cesàro operator
## Finding
Let \(H=L^2(0,1;\mathbb C)\), with Lebesgue measure, and define the bounded Cesàro integral operator
\[
(Cf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt,\qquad 0<x<1.
\]
Let \(e(x)=1\), let \(Pf=\langle f,e\rangle e=(\int_0^1 f(t)\,dt)e\) be the orthogonal projection onto constants, and let \(T_\tau=C+\tau P\) for real \(\tau\). Define
\[
\tau_-=-\frac8{\pi^2-4},\qquad \tau_+=\frac8{\pi^2+4}.
\]
Then the **entire real point spectrum** of \(T_\tau\) is classified as follows, with all indicated off-circle eigenvalues unique:

- If \(\tau<-2\), there is exactly one real eigenvalue in \(( -\infty,0)\), and no other real eigenvalue.
- If \(\tau=-2\), the only real eigenvalue is \(0\), with eigenspace \(\operatorname{span}\{1-x\}\). It is embedded in the essential spectrum.
- If \(-2<\tau<\tau_-\), there is exactly one real eigenvalue in \((0,2)\), and no other real eigenvalue.
- If \(\tau>\tau_+\), there is exactly one real eigenvalue in \((2,\infty)\), and no other real eigenvalue.
- For every other real \(\tau\), the real point spectrum is empty. In particular, neither transition value \(\tau_-\) nor \(\tau_+\) yields an eigenvalue at \(2\).

Every eigenvalue away from the unperturbed spectral circle has both geometric and algebraic multiplicity one. The Fredholm essential spectrum remains
\[
\sigma_{\mathrm{ess}}(T_\tau)=\Gamma:=\{z\in\mathbb C:|z-1|=1\}.
\]
Writing \(\lambda(\tau)\) for the real eigenvalue on either side of the crossing at \(\tau=-2\), one has the same sharp first-order law from both sides:
\[
\lambda(\tau)=\tfrac32(\tau+2)+O((\tau+2)^2),\qquad \tau\to-2,\quad\tau\ne-2.
\]
Thus a real eigenvalue passes through the essential-spectrum point \(0\), whereas the other two branches meet the essential spectral point \(2\) only as limiting, non-eigenvalue thresholds.

## Assumptions and scope
All statements concern the specified operator \(C\) on the complex Hilbert space \(L^2(0,1)\), the **canonical** rank-one orthogonal projection \(P\), and real coupling \(\tau\). The classical Fourier spectral model, normality, empty point spectrum, and circle \(\Gamma\) for the unperturbed \(C\) are established in Belli–Gül–Ross–Siskakis (2026). The theorem determines **real** eigenvalues only; it does not classify nonreal eigenvalues for \(T_\tau\). The essential spectrum uses the Fredholm definition. The terms 'unique eigenvalue' and 'multiplicity one' for \(\lambda\notin\Gamma\) refer to the isolated eigenvalue; at \(0\) only geometric simplicity is claimed.

## Proof
**1. Spectral representation and rank-one secular equation.** In the cited Fourier model, \(C\) is unitarily equivalent to multiplication by
\[
m(s)=\frac1{1/2-is},\qquad s\in\mathbb R,
\]
while the normalized constant vector \(e\) has spectral probability measure
\[
d\nu(s)=\frac\pi2\operatorname{sech}^2(\pi s)\,ds.
\]
For \(z\notin\Gamma\) set
\[
G(z)=\langle(zI-C)^{-1}e,e\rangle
=\int_{\mathbb R}\frac{d\nu(s)}{z-m(s)}.
\]
If \(\tau\ne0\), the rank-one resolvent equation \((zI-C)f=\tau\langle f,e\rangle e\) shows that \(z\) is an eigenvalue of \(T_\tau\) if and only if \(\tau G(z)=1\). Its eigenspace is then spanned by \((zI-C)^{-1}e\). For real \(z\ne0,2\), symmetry under \(s\mapsto-s\) makes \(G(z)\) real.

**2. Exact Laplace forms.** The Fourier transform of \(\nu\), with the convention \(\int e^{ist}\,d\nu(s)\), is
\[
h(t)=\frac{t}{2\sinh(t/2)},\qquad t>0,\qquad h(0)=1.
\]
For completeness, putting \(v=e^{2\pi s}\) gives \(d\nu(s)=dv/(1+v)^2\). With \(a=t/(2\pi)\), Euler's beta and reflection identities yield
\[
\int_0^\infty\frac{v^{ia}}{(1+v)^2}\,dv
=\Gamma(1+ia)\Gamma(1-ia)=\frac{\pi a}{\sinh(\pi a)},
\]
which proves the transform identity, including its \(t=0\) limit by continuity.

For real \(z\notin\{0,2\}\), write \(w=1/z\). The exact identity
\[
\frac1{z-m(s)}=w+\frac{w^2}{(1/2-w)-is}
\]
and the Laplace formula for the reciprocal of \((1/2-w)-is\), with its sign chosen according to the sign of \(1/2-w\), give the three expressions below. Define, for \(t>0\),
\[
q(t)=\frac{t}{e^t-1},\qquad p(t)=\frac{t}{1-e^{-t}}=t+q(t).
\]
Both extend continuously to \(1\) at the origin. Direct differentiation yields
\[
q''(t)=\frac{e^t\big((t-2)e^t+t+2\big)}{(e^t-1)^3}>0.
\]
Indeed \(H(t)=(t-2)e^t+t+2\) satisfies \(H(0)=H'(0)=0\) and \(H''(t)=t e^t>0\) for positive \(t\). Thus \(q'\) strictly increases from \(-1/2\) to \(0\), while \(p'=1+q'\) strictly increases from \(1/2\) to \(1\).

When \(z<0\), putting \(x=-1/z>0\) and integrating by parts gives
\[
G(z)=x\int_0^\infty e^{-xt}q'(t)\,dt
=\int_0^\infty e^{-u}q'(u/x)\,du.
\]
When \(0<z<2\), putting \(x=1/z>1/2\) gives
\[
G(z)=-x\int_0^\infty e^{-xt}p'(t)\,dt
=-\int_0^\infty e^{-u}p'(u/x)\,du.
\]
When \(z>2\), putting \(w=1/z\in(0,1/2)\) gives
\[
G(z)=w+w^2\int_0^\infty e^{wt}q(t)\,dt.
\]
All these integrals converge absolutely in their stated domains. The integrations by parts have vanishing exponential boundary terms, since \(q\) is bounded and \(p\) grows at most linearly.

**3. Strict ranges.** For negative \(z\), the parameter \(x=-1/z\) strictly increases with \(z\). Since \(q'\) is strictly increasing, the displayed exponential expectation is strictly decreasing in \(z\), with endpoint limits
\[
G(( -\infty,0))=(-1/2,0).
\]
For \(0<z<2\), the parameter \(x=1/z\) strictly decreases as \(z\) increases. Since \(p'\) is strictly increasing, the second expectation is again strictly decreasing in \(z\), with
\[
G((0,2))=\left(\frac12-\frac{\pi^2}{8},-\frac12\right).
\]
For \(z>2\), all terms in the last integral are positive, so \(G\) is strictly increasing in \(w=1/z\), hence strictly decreasing in \(z\), with
\[
G((2,\infty))=\left(0,\frac12+\frac{\pi^2}{8}\right).
\]
Here open intervals denote ranges, not sets of values at their endpoints. The endpoint values at \(0\) follow from \(q'(0)=-1/2\) and \(p'(0)=1/2\) by exponential-kernel concentration. For both sides of \(2\), expand the convergent geometric series to obtain
\[
\int_0^\infty e^{-t/2}p(t)\,dt
=\int_0^\infty e^{t/2}q(t)\,dt
=\sum_{k=0}^\infty\frac1{(k+1/2)^2}=\frac{\pi^2}{2};
\]
substitution into the two formulas for \(G\) gives respectively \(\frac12-\frac{\pi^2}{8}\) and \(\frac12+\frac{\pi^2}{8}\). The sum equals \(4\sum_{k\ge0}(2k+1)^{-2}=\pi^2/2\).

**4. Couplings, boundary points, and multiplicity.** On each of the three real components of \(\mathbb R\setminus\{0,2\}\), the secular equation \(G(z)=1/\tau\) therefore has exactly one solution precisely when \(1/\tau\) belongs to its computed open range. Translating these inequalities gives the four nonzero-off-circle cases in the statement and the exact couplings \(\tau_-\) and \(\tau_+\).

The points \(0,2\) lie on \(\Gamma\) and require direct checks. Since \(C(1-x)=1\) and \(P(1-x)=1/2\), one has \(T_{-2}(1-x)=0\). Conversely, \(Cf=a\cdot1\) implies \(f=a(1-x)\) (differentiate the defining indefinite integral); hence \(T_\tau f=0\) with \(f\ne0\) forces \(\tau=-2\), and the eigenspace is one-dimensional. At \(2\), in the Fourier model the equation \((2I-C)f=c e\) with \(c\ne0\) would require a multiple of \(\sqrt{\pi/2}\operatorname{sech}(\pi s)/(2-m(s))\) in \(L^2(\mathbb R)\). Because \(2-m(s)=-4is+O(s^2)\) and the numerator is nonzero at \(s=0\), this quotient is not locally square-integrable. If \(c=0\), the original \(C\) has no eigenvalue \(2\). Thus \(2\) is never an eigenvalue of any \(T_\tau\).

More precisely, differentiating the three integral expressions under the integral sign gives \(G'(z)<0\) throughout each interval: in the first two intervals the derivative is a strictly negative integral of \(q''(t)=p''(t)>0\) times positive factors, while in the third the displayed expression is strictly increasing in \(w=1/z\). Thus the scalar rank-one resolvent denominator has a simple zero at each real secular root outside \(\Gamma\); the corresponding isolated eigenvalue has algebraic as well as geometric multiplicity one. Rank-one \(P\) is compact and the unperturbed multiplication operator has precisely the essential range \(\Gamma\), with no isolated finite-multiplicity spectral points, so compact-perturbation invariance gives \(\sigma_{\mathrm{ess}}(T_\tau)=\Gamma\).

**5. The embedded-eigenvalue crossing.** Expanding the exact derivatives at the origin gives \(q'(t)=-1/2+t/6+O(t^2)\) and \(p'(t)=1/2+t/6+O(t^2)\). The exponential integral formulas, with exponentially small tails, imply from both sides of zero
\[
G(z)=-\frac12-\frac z6+O(z^2),\qquad z\to0,\quad z\in\mathbb R\setminus\{0\}.
\]
Meanwhile \(1/\tau=-1/2-(\tau+2)/4+O((\tau+2)^2)\). Their equality at the unique real secular root yields \(\lambda(\tau)=\frac32(\tau+2)+O((\tau+2)^2)\). This completes the proof.

## Verification
A standalone standard-library program, `verify_rank_one_cesaro.py`, computes the real spectral integral directly and independently evaluates the three Laplace formulas. It compares twelve representative real spectral parameters (including values near \(0\) and \(2\)), tests the exact constants \(G(1)=1-\pi^2/6\) and the two limiting \(2\)-values, tests strict sample monotonicity, and numerically checks the slope \(3/2\) of the eigenvalue at the coupling \(-2\). Successful execution prints `RANK_ONE_REAL_CESARO_BIFURCATION_NUMERICAL_CHECKS_OK`. These are finite consistency checks; the universal theorem rests on the preceding analytic argument.

## Relationship to prior work
Belli, Gül, Ross and Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, give the crucial Fourier multiplier, normality, spectral measure of the constant vector, and unperturbed resolvent. Their theorems concern \(C\) itself; none of the inspected operator or spectral theorems states a rank-one coupling-phase classification. The same authors' *Crescents and the Real Variable Cesàro Operator* analyzes the unperturbed family on \(L^p\) (norms, spectra, cyclicity, invariant subspaces), and likewise does not treat \(C+\tau P\). The rank-one secular equation is a classical general identity and is **not** claimed as new. The contribution is the complete *evaluated* real-eigenvalue diagram, its exact two \(\pi^2\)-thresholds, and the embedded crossing through zero.

## Limitations
The theorem does not exclude or classify nonreal eigenvalues of \(T_\tau\). It does not extend automatically to complex coupling, different rank-one vectors, or higher-rank perturbations. The embedded eigenvalue at zero is only asserted geometrically simple, not an isolated algebraically simple eigenvalue. The analytical statements, not the finite checker, constitute the proof. Earlier or unindexed equivalent calculations under alternative perturbation terminology cannot be ruled out solely by bibliographic searches.

## References
1. Anıl Belli, Uğur Gül, William T. Ross, and Aristomenis G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691v1 (first public 2026-04-21), sections 1–4; available revised text arXiv:2604.19691v2, https://arxiv.org/html/2604.19691v2 .
2. The same authors, *Crescents and the Real Variable Cesàro Operator*, arXiv:2606.08600v1 (first public 2026-06-07), later *Integral Equations and Operator Theory* 98, article 42 (2026), https://doi.org/10.1007/s00020-026-02865-7 .
