# Exact adiabatic migration bias in a two-deme Moran flow

## Finding

Consider the deterministic death–birth Moran frequency equations below with equal deme sizes, equal unit death rates, resident birth rate one, and mutant birth rates \(3/2\) and \(1/2\) in the two demes. Let bidirectional in-phase migration have instantaneous probability \(m(t)=q\cos^2(\pi t/T)\), where \(T>0\) is the period.

**Theorem.** There exists \(q_0>0\) such that, for every \(q\in(0,q_0)\) and every \(T>0\), the forced equations have a unique attracting \(T\)-periodic solution in a fixed small forward-invariant rectangle near \((1,0)\). This solution belongs to the physical interior and attracts all solutions in that rectangle. If \(\bar F_T(q)\) denotes its period-averaged fraction of mutants across both demes, then

\[
\lim_{T\to\infty}\bar F_T(q)=\frac{1}{2\sqrt{1-q}}.
\]

At constant migration probability equal to the seasonal *mean*, \(m=q/2\), the corresponding locally attracting equilibrium has mean mutant fraction \(F_{\mathrm{mean}}(q)=1/[2(1-q/2)]\). Constant migration at the seasonal *maximum*, \(m=q\), instead has \(F_{\mathrm{peak}}(q)=1/[2(1-q)]\). Therefore, for every \(0<q<q_0\),

\[
\boxed{\quad
\frac{1}{2(1-q/2)}
<\frac{1}{2\sqrt{1-q}}
<\frac{1}{2(1-q)}.\quad}
\]

The strictly positive long-season excess over the *equal-mean* constant-migration baseline is exactly

\[
\Delta_\infty(q)=\frac12\left(\frac1{\sqrt{1-q}}-\frac1{1-q/2}\right)
=\frac{q^2}{16}+O(q^3)\quad(q\downarrow0).
\]

Thus temporal variation **increases**, rather than suppresses, mutant abundance relative to the physically matched constant-mean comparison on this specific small-migration branch. This is not a statement about all fitness regimes or all migration amplitudes.

## Assumptions and scope

Write \(x,y\in[0,1]\) for mutant frequencies in demes one and two, respectively. In the symmetric in-phase case, each offspring remains in its parental deme with probability \(1-m\) and migrates with probability \(m\). At equal unit death rates, the source model's transition probabilities (its Appendix B) reduce exactly to

\[
\begin{aligned}
\dot x&=\frac12\left(\frac{3(1-m)x+my}{2+(1-m)x-my}-x\right),\\
\dot y&=\frac12\left(\frac{(1-m)y+3mx}{2+mx-(1-m)y}-y\right).
\end{aligned}
\tag{1}
\]

The migration probability is \(m=q\cos^2(\pi t/T)\). Choose \(q_0\) sufficiently small, in particular \(q_0<1/2\), so all denominators in (1) are positive on the physical square. The result concerns the locally selected periodic orbit near the stable isolated-deme state \((1,0)\); no globally unique periodic attractor is claimed. The deterministic mean-field limit, not stochastic finite-population fixation, is the object of the theorem.

## Proof

**1. Frozen stable branch.** Let \(f=(f_1,f_2)\) denote the right-hand side of (1) at fixed \(m\). At \(m=0\), \((x,y)=(1,0)\) is an equilibrium, with

\[
D_{(x,y)}f(1,0;0)=\begin{pmatrix}-1/6&0\\0&-1/4\end{pmatrix}.
\]

The implicit function theorem gives a unique analytic equilibrium branch \(z_*(m)=(X(m),Y(m))\) near \((1,0)\) for all sufficiently small \(m\ge0\). Direct series substitution yields \(X(m)=1-2m+4m^2+O(m^3)\) and \(Y(m)=3m-3m^2+O(m^3)\). In particular, \(0<X(m),Y(m)<1\) for small positive \(m\), and \(X(m)\ne Y(m)\).

**2. Exact equilibrium sum.** Multiplying the two stationary equations by their respective positive denominators and removing a common factor gives the polynomial numerators

\[
\begin{aligned}
P(x,y,m)&=(m-1)x^2+mxy-3mx+my+x,\\
Q(x,y,m)&=-mxy+3mx+(1-m)y^2-my-y.
\end{aligned}
\]

They satisfy the exact algebraic identity

\[
P+Q=(x-y)\bigl[1-(1-m)(x+y)\bigr].
\]

On the near-\((1,0)\) branch \(P=Q=0\) and \(X\ne Y\), hence

\[
\boxed{X(m)+Y(m)=\frac1{1-m}},\qquad F(m)=\frac{X(m)+Y(m)}2=\frac1{2(1-m)}.
\]

This is an exact nonlinear equilibrium balance, not a truncation. For completeness, substitution of \(Y=1/(1-m)-X\) into the first stationary equation yields

\[
(1-m)X^2-(1-2m)^2X-m=0,
\]

whose positive root continuous from \(X(0)=1\) is

\[
X(m)=\frac{(1-2m)^2+\sqrt{(1-2m)^4+4m(1-m)}}{2(1-m)},
\qquad Y(m)=\frac1{1-m}-X(m).
\]

The chosen branch remains hyperbolic and locally attracting on a sufficiently small nonnegative migration interval by continuity of the Jacobian.

**3. The forced attracting orbit.** Fix a sufficiently small \(\delta>0\). At zero migration, the rectangular box \(R=[1-\delta,1]\times[0,\delta]\) is positively invariant: the vector field points inward at \(x=1-\delta\) and \(y=\delta\) and is tangent to the physical faces \(x=1\), \(y=0\). The inward signs at the first two faces persist uniformly for all \(0\le m\le q_0\), by continuity. On the physical faces the general replacement probabilities in (1) ensure \(\dot x\le0\) at \(x=1\) and \(\dot y\ge0\) at \(y=0\). Thus \(R\) is invariant for any forcing taking values in \([0,q_0]\). Shrinking \(\delta,q_0\) further ensures that the symmetric part of \(D_{(x,y)}f\) is bounded above by \(-\lambda I\), for some \(\lambda>0\), throughout \(R\) and \(0\le m\le q_0\): this follows from the diagonal matrix in step 1 and uniform continuity.

Consequently the time-\(T\) map contracts distances in \(R\) by at most \(e^{-\lambda T}\). The contraction mapping theorem supplies one and only one periodic solution in \(R\), attracting every solution starting there. For \(q>0\), migration is positive except at isolated instants, so the physical faces \(x=1\) and \(y=0\) are strictly inward on a set of positive times. The periodic solution therefore cannot remain on or touch either face; it lies in \((0,1)^2\).

**4. Adiabatic estimate.** The branch \(z_*(m)\) lies in \(R\) and has bounded derivative with respect to \(m\). As \(|m'(t)|\le\pi q/T\), the difference between the periodic solution \(z_T(t)\) and the moving equilibrium \(z_*(m(t))\) obeys the differential inequality

\[
\frac{d}{dt}\lVert z_T-z_*\rVert
\le-\lambda\lVert z_T-z_*\rVert+Cq/T
\]

(where the upper Dini derivative is understood at zero). Both motions are defined and bounded for all time. Integrating this inequality backward on the periodic solution gives the uniform estimate

\[
\sup_t\lVert z_T(t)-z_*(m(t))\rVert\le\frac{Cq}{\lambda T}.
\]

It follows that

\[
\lim_{T\to\infty}\bar F_T(q)
=\frac1\pi\int_0^\pi F(q\cos^2\theta)\,d\theta
=\frac1{2\pi}\int_0^\pi\frac{d\theta}{1-q\cos^2\theta}
=\frac1{2\sqrt{1-q}}.
\]

The last equality follows by symmetry and the substitution \(u=\tan\theta\) on a half-period, reducing the integral to \(2\int_0^\infty du/(u^2+1-q)=\pi/\sqrt{1-q}\).

**5. Strict comparison.** Since \((1-q/2)^2-(1-q)=q^2/4>0\) and all factors are positive, \(1-q/2>\sqrt{1-q}\), proving that the adiabatic mean strictly exceeds the equal-mean constant-migration equilibrium. Conversely \(\sqrt{1-q}>1-q\), proving that the adiabatic mean is strictly below the full-amplitude constant-migration equilibrium. Taylor expansion at \(q=0\) gives the displayed \(q^2/16\) leading gap. All inequalities are valid for every \(0<q<q_0\).

## Verification

The accompanying `verify.py` reconstructs the transition-probability equations, checks the exact polynomial identity and Jacobian with symbolic algebra, verifies the analytic equilibrium branch and \(q^2/16\) coefficient, and numerically integrates selected forced solutions. Its algebraic checks pass. At amplitude \(q=0.05\), it reports constant-mean mutant fraction approximately \(0.512820512821\), slow-period limit approximately \(0.512989176043\), period-100 mean \(0.513031239651\), and period-400 mean \(0.512992746477\). These finite-time approximations are consistency checks; existence and the infinite-period limit are proved in steps 1–5 independently of numerical integration.

## Relationship to prior work

Masoumi, Kaveh, and Ejtehadi (2026) introduced the same two-deme Moran death–birth model and the symmetric in-phase cosine-squared migration schedule. Their Sections 2–4 and Appendices A–C study finite-period mean frequencies numerically and discuss contraction toward neutrality and a full-amplitude constant-migration interpretation of long seasons. The present claim concerns the exact small-amplitude attracting branch and its genuinely adiabatic time average: on that branch the long-season value lies strictly **between** the equal-mean and peak-amplitude constant-migration values. It therefore supplies a specific noncontracting comparison to the equal-mean baseline, without disputing the numerical outcomes for the paper's selected parameters.

Aubrée, Lac, Mailleret, and Calcagno (2023) investigated pulsed migration in a distinct mainland–island fixation model, including cases in which pulsedness increases gene flow. Their fixation-probability results neither give the stationary balance \(X+Y=1/(1-m)\) for this symmetric two-deme deterministic flow nor imply its exact sinusoidal adiabatic average. Standard contraction, implicit-function, and slow-tracking tools used in the proof are not claimed as new.

## Limitations

The theorem guarantees a nonempty but not explicitly optimized small-amplitude interval \((0,q_0)\); it does not assert that the interior branch persists for arbitrary migration amplitude. It classifies one locally attracting solution near the separated-deme state, not every invariant set of the full physical square. The sharp mean comparison concerns the \(T\to\infty\) limit; no inequality for all finite \(T\) is claimed. Demographic noise, fixation probabilities for finite population size, other mutant birth rates, asymmetric migration, and out-of-phase forcing require separate analysis. The chosen fitness rates have arithmetic mean equal to the resident rate; the result concerns population mutant abundance rather than a universal reversal of local selection.

## References

1. Mohammad Amin Masoumi, Kamran Kaveh, and Mohammad Reza Ejtehadi, *Effects of Periodic Migration on Selection in Subdivided Populations*, arXiv:2610.08160v1, first public October 6, 2026. Model, Table 1 Scenario A, equation (1), and Appendix B, equations (B1)–(B7). https://arxiv.org/abs/2610.08160 ; full HTML: https://arxiv.t3mt.com/html/2610.08160v1 .
2. Flora Aubrée, Baptiste Lac, Ludovic Mailleret, and Vincent Calcagno, *Migration pulsedness alters patterns of allele fixation and local adaptation in a mainland-island model*, *Evolution* 77 (2023), 718–730, doi:10.1093/evolut/qpac067. https://academic.oup.com/evolut/article/77/3/718/6960904 .
