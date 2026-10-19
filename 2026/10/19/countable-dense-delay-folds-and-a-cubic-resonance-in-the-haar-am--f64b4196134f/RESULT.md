# Countable dense delay folds and a cubic resonance in the Haar ambiguity function

## Finding

Let \(h=\mathbf 1_{[-1,0]}-\mathbf 1_{[0,1]}\) (endpoint values are immaterial) and define its symmetric narrowband self-ambiguity function by
\[
 A(\tau,\nu)=\int_{\mathbb R}h(t+\tau/2)h(t-\tau/2)e^{-2\pi i\nu t}\,dt.
\]
The following classification holds for real \(0<\tau<2\) and \(\nu\in\mathbb R\), with multiplicity always taken in the Doppler variable \(\nu\) at fixed \(\tau\).

**Theorem.** For \(2/3<\tau<2\), all Doppler zeros are simple. At \(\tau=2/3\), the entire Doppler zero set is \(\{3k/2:k\in\mathbb Z\}\); the zero at \(\nu=0\) has order two, every nonzero zero \(\nu=3k\), \(k\in\mathbb Z\setminus\{0\}\), has order three, and each zero \(\nu=3(2k+1)/2\) has order one. For \(0<\tau<2/3\), every Doppler zero is simple or double, and the set
\[
 \mathcal D=\{\tau\in(0,2/3):\text{some }\nu\ne0\text{ is a double Doppler zero of }A(\tau,\cdot)\}
\]
is **countable and dense** in \((0,2/3)\). Every double zero is a nondegenerate fold of the delay projection of the nodal curve. Despite these dense projected folds and the cubic Doppler resonances, the real zero set \(\{(\tau,\nu):0<\tau<1, A(\tau,\nu)=0\}\) is a smooth one-dimensional real-analytic submanifold with no joint singularities.

Thus the smallest sign-alternating rectangular waveform has dense parameter values at which two Doppler nulls merge, while its full two-variable nodal set never crosses itself in the interior strip. These are **high-frequency** fold values: density does not assert any finite-band density for a fixed frequency cutoff.

## Assumptions and scope

The waveform has two equal-length, opposite-sign rectangular halves and is not normalized to unit \(L^2\) norm; scaling by a nonzero constant changes no zero location or multiplicity. We use the negative-exponential Fourier convention. The delay is positive by symmetry in \(\tau\), and the theorem concerns the open overlap region \(0<\tau<2\). The boundary \(\tau=1\) is continuous but need not be differentiable as a function of delay because the waveform has jumps. The theorem's joint real-analytic regularity is restricted to \(0<\tau<1\); no statement is made about the exterior region \(|\tau|\ge2\), where the ambiguity function vanishes identically by disjoint support.

For \(0\le\tau\le1\), direct integration over the two equal-sign edge intervals and the opposite-sign central interval gives, for \(\nu\ne0\),
\[
 A(\tau,\nu)=\frac{\sin(\pi\nu(2-\tau))-2\sin(\pi\nu\tau)}{\pi\nu},
 \qquad A(\tau,0)=2-3\tau.
\]
For \(1\le\tau<2\),
\[
 A(\tau,\nu)=-\frac{\sin(\pi\nu(2-\tau))}{\pi\nu},
 \qquad A(\tau,0)=-(2-\tau),
\]
with continuous interpretations at \(\nu=0\). Hence the zeros in \(1\le\tau<2\) are exactly \(\nu=k/(2-\tau)\) for nonzero integers \(k\), all simple.

## Proof

### 1. Reduce fixed-delay multiplicity to a two-frequency sine sum.

For \(0<\tau<1\), set \(r=(2-\tau)/\tau>1\) and \(T=\pi\tau\nu\). At \(\nu\ne0\), multiplication by the nonvanishing factor \(\pi\nu\) preserves the Doppler vanishing order. The numerator becomes
\[
 F(r,T)=\sin(rT)-2\sin T.
\]
A nonzero Doppler zero is multiple precisely when
\[
 \sin(rT)=2\sin T,\qquad r\cos(rT)=2\cos T. \tag{1}
\]
Squaring and adding yields the necessary identity
\[
 4\left(\sin^2T+r^{-2}\cos^2T\right)=1. \tag{2}
\]
If \(1<r<2\), its left side is at least \(4/r^2>1\), so multiple zeros are impossible. This corresponds to \(2/3<\tau<1\).

If \(r>2\), equation (2) at a multiple zero forces
\[
 \sin^2T=\frac{r^2-4}{4(r^2-1)}\in(0,1/4).
\]
Thus \(\sin T\ne0\) and \(\cos T\ne0\); equation (1) also gives \(\cos(rT)\ne0\). Moreover,
\[
 F_{TT}=-r^2\sin(rT)+2\sin T
       =-2(r^2-1)\sin T\ne0,
\]
so every multiple zero for \(r>2\) has **exactly order two**.

At \(r=2\), equivalently \(\tau=2/3\),
\[
 F(2,T)=2\sin T(\cos T-1).
\]
It has simple zeros at odd integer multiples of \(\pi\) and exact order-three zeros at even integer multiples. Here \(T=2\pi\nu/3\), giving the stated Doppler lattice. For \(\nu\ne0\) division by \(\pi\nu\) preserves these orders. At \(\nu=0\) division removes one order: explicitly
\[
 A(2/3,\nu)=-\frac{8\pi^2}{27}\nu^2+O(\nu^4),
\]
so the origin-frequency zero is exactly quadratic. The formula for \(1\le\tau<2\) above finishes the all-delay Doppler multiplicity classification.

### 2. Joint nodal regularity and nondegenerate folds.

The map \((\tau,\nu)\mapsto(r,T)\) is a real-analytic local diffeomorphism when \(0<\tau<1\): its two diagonal derivatives satisfy \(\partial_\tau r=-2/\tau^2\ne0\) and \(\partial_\nu T=\pi\tau\ne0\). At any \(T\ne0\) where \(F_T\ne0\), the zero set is regular. At any multiple zero for \(r>2\), the previous step gives
\[
 F_r=T\cos(rT)\ne0,\qquad F_{TT}\ne0.
\]
At any nonzero cubic zero for \(r=2\), the same derivative equals \(T\ne0\). Thus the full gradient never vanishes on \(F=0\) with \(T\ne0\). For \(\nu=0\), the only zero is \(\tau=2/3\), where \(\partial_\tau A=-3\ne0\). Since multiplication by \(1/(\pi\nu)\) causes no loss away from zero, all nodal points are regular in \(0<\tau<1\).

At a double zero, solve \(F(r(T),T)=0\) locally: \(r'(T)=0\) and
\[
 r''(T)=-F_{TT}/F_r\ne0.
\]
Since \(\tau=2/(r+1)\) is a smooth monotone function of \(r\), the projection of that nodal branch onto the delay axis has a genuine nondegenerate fold.

### 3. The fold-delay set is countable.

Double zeros with positive \(\nu\) correspond exactly to solutions of \(F=F_T=0\) with \(r>2\), \(T>0\). At any such solution,
\[
 \det\frac{\partial(F,F_T)}{\partial(r,T)}=F_r F_{TT}\ne0.
\]
The simultaneous solution set is therefore discrete in the second-countable open quadrant. Every such discrete subset is countable (for example, cover it by rational balls, each isolating one point). Its image under \(r\mapsto2/(r+1)\) is countable. The same conclusions apply to negative Doppler frequencies by evenness.

### 4. The fold-delay set is dense.

Fix any **irrational** \(r_0>2\). Choose angles \(0<\theta<\pi/6\) and \(0<\phi<\pi/2\) by
\[
 \sin^2\theta=\frac{r_0^2-4}{4(r_0^2-1)},\qquad
 \sin\phi=2\sin\theta,\qquad
 \cos\phi=\frac{2}{r_0}\cos\theta.
\]
Both definitions of \(\phi\) are compatible because their squared sum is one. They give
\[
 \sin\phi-2\sin\theta=0,\qquad
 r_0\cos\phi-2\cos\theta=0. \tag{3}
\]
Since \(r_0\) is irrational, the linear flow \(T\mapsto (T,r_0T)\bmod2\pi\) is dense on the two-torus. In particular, there are \(T_j\to+\infty\) such that
\[
 T_j\bmod2\pi\longrightarrow\theta,\qquad
 r_0T_j\bmod2\pi\longrightarrow\phi.
\]
Seek an exact double zero with \(T=T_j+u\) and \(r=r_0+\delta/T_j\). Its two equations, in unknowns \((u,\delta)\), converge in \(C^1\) near \((0,0)\) to
\[
 G_1(u,\delta)=\sin(\phi+r_0u+\delta)-2\sin(\theta+u),
\]
\[
 G_2(u,\delta)=r_0\cos(\phi+r_0u+\delta)-2\cos(\theta+u).
\]
By (3), \((0,0)\) is a zero of the limiting map. Its Jacobian, with columns in the order \((u,\delta)\), is
\[
 \begin{pmatrix}
 0 & \cos\phi\\
 -2(r_0^2-1)\sin\theta & -r_0\sin\phi
 \end{pmatrix},
\]
with nonzero determinant. Stability of a nondegenerate zero under small \(C^1\) perturbations (the inverse-function theorem with parameters) therefore provides exact solutions \((u_j,\delta_j)\to(0,0)\) for all sufficiently large \(j\). The corresponding \(r_j=r_0+\delta_j/T_j>2\) satisfy \(r_j\to r_0\) and have a nonzero double zero at \(T_j+u_j>0\).

Every irrational \(r_0>2\) is thus a limit of double-zero parameters. Irrationals are dense in \((2,\infty)\), and the change of variables \(\tau=2/(r+1)\) maps that interval onto \((0,2/3)\). Hence \(\mathcal D\) is dense there. Combining with Step 3 proves the countable-dense theorem.

## Verification

The standalone `CHECKER.py` computes the transform independently by integrating the signed overlapping intervals and compares that with the closed sine formula at seven representative delay-frequency pairs. It also solves \(F=F_T=0\) at three high-precision nondegenerate folds, checks \(F_rF_{TT}\ne0\), and verifies cubic-jet identities for five nonzero resonances at \(\tau=2/3\). Run `python3 CHECKER.py` with the `mpmath` package. Its actual output is provided in `CHECKER_OUTPUT.txt`.

As examples, numerically resolved double-zero delays include \(0.5110836871699035799\ldots\), \(0.6012599278591204236\ldots\), and \(0.5058126797306419795\ldots\). These computations do not prove density; Step 4 does. No general numerical root enumeration is used in the proof.

## Relationship to prior work

The symmetric ambiguity transform and its time-frequency interpretation are classical. Bonami, Garrigós and Jaming (arXiv:math/0509031v1, first submitted 2 September 2005) analyze ambiguity partners and inverse uniqueness for Hermite and pulse-type signals. Their Section 4 studies pulse-type phase-retrieval rigidity, not the Doppler-zero multiplicity and delay-caustic classification here. Jaming's *Uncertainty principles for radar ambiguity functions and moments* establishes general moment-based zero-free regions and local uncertainty estimates, rather than high-frequency coalescences in the Haar self-ambiguity transform. Flandrin's *Ambiguity functions* reviews symmetric conventions, time-frequency interpretation and general identities, not the present fold-delay density theorem.

The elementary overlap formula is a starting identity, not itself asserted to be new. The claimed contribution is the complete multiplicity threshold, countable-dense fold-delay theorem with its torus-recurrence proof, unique infinite cubic resonance family, and distinction between Doppler-sectional and joint nodal regularity. A potentially equivalent treatment in specialized two-frequency exponential-polynomial or radar null-pattern literature remains a publication-priority risk.

## Limitations

The density statement is topological density in delay, **not** positive measure, nor density below any fixed Doppler cutoff; the fold set is countable. Smoothness of the full zero set is asserted on the open strip \(0<\tau<1\), not at its nonsmooth pulse-overlap boundary or the trivial exterior support zeros. The result gives a complete multiplicity classification but not an explicit enumeration of all double-zero delays. Independent expert review and independent publication-priority verification have not been performed.

## References

1. A. Bonami, G. Garrigós and P. Jaming, *Discrete radar ambiguity problems*, arXiv:math/0509031v1 (2 September 2005), Sections 1 and 4, https://arxiv.org/html/math/0509031v1.
2. P. Jaming, *Uncertainty principles for radar ambiguity functions and moments*, HAL preprint hal-00080459, version 2 dated 13 December 2006, https://www.researchgate.net/publication/228563572_UNCERTAINTY_PRINCIPLES_FOR_RADAR_AMBIGUITY_FUNCTIONS_AND_MOMENTS.
3. P. Flandrin, *Ambiguity functions*, chapter on time-frequency analysis, Sections 0.1.1–0.1.4, https://perso.ens-lyon.fr/patrick.flandrin/PF_ambiguity.pdf. Publication date not used to determine the cohort.
