# Two co-optimal mutation rates at a two-timescale environmental crossover

## Finding
Consider a trait-structured population facing a slow and a fast oscillation in its optimum trait. At a unique relative spectral intensity \(B_*\in(26,27)\), **two widely separated positive mutation strengths exactly maximize the same long-time, low-density population growth rate**. On either side of this value, only one of the two is globally optimal, and the optimizer changes discontinuously. This is a first-order transition in optimal mutational exploration, not two different equilibrium trait means.

With \(y=2\sqrt D\), the exact rate is
\[
\Lambda_B(D)=r-\frac y2-\frac3{1+y^2}-\frac{900B}{900+y^2}.
\]
For \(B\in[26,27]\), the growth-rate function has precisely two local maxima, respectively in \(y\in(2,3)\) and \(y\in(24,28)\). Their ordering switches **exactly once**; they agree only at \(B_*\). Numerical localization, not used as a proof, gives \(B_*\approx26.8881859300\), \(y_{\rm low}\approx2.2507684177\), \(y_{\rm high}\approx26.4942336721\), corresponding to \(D\approx1.2664896175\) and \(D\approx175.4861044674\).

## Assumptions and scope
On \(\mathbb R\), for \(t\ge0\), let
\[
\partial_tu(t,x)=D\,\partial_{xx}u(t,x)+\bigl[r-(x-z_B(t))^2-\kappa M(t)\bigr]u(t,x),\quad M(t)=\int_{\mathbb R}u(t,x)\,dx,
\]
\[
z_B(t)=\sqrt6\sin t+\sqrt{2B}\sin(30t),\quad D>0,\quad\kappa>0,\quad r\in\mathbb R,\quad B\in[26,27].
\]
The initial profile is any nonzero positive multiple of a Gaussian density with finite mean and strictly positive variance. The objective is the limiting period-averaged *intrinsic* per-capita growth rate (that is, average fitness **before** density-dependent mortality \(-\kappa M\)), not a rate inferred from the eventual saturated population. Set \(y=2\sqrt D\). Both harmonic frequencies are integers, so the forcing has period \(2\pi\).

## Proof
**1. Exact Gaussian closure.** Write \(u=M\,\mathcal N(m,V)\) with a normalized one-dimensional Gaussian. Direct coefficient comparison in the PDE gives
\[
\dot V=2D-2V^2,\qquad\dot m=-2V(m-z_B),\qquad \dot M=M\bigl[r-V-(m-z_B)^2-\kappa M\bigr].
\]
Because \(D,V(0)>0\), the variance remains positive and converges exponentially to \(\sqrt D\). Linear variation of constants then gives exponential convergence of \(m\) to the unique periodic solution of \(\dot m=-y(m-z_B)\). The normalized Gaussian remains a valid positive density, and the scalar logistic equation keeps \(M(t)>0\) for every finite \(t\). No assumption of infinite-dimensional Gaussian attraction is needed.

**2. Spectral averaging.** For forcing \(a\sin(\omega t)\), the stationary lag \(m-z\) has mean square \(a^2\omega^2/[2(y^2+\omega^2)]\). Orthogonality of the distinct integer harmonics removes cross terms. The mean mutation load equals \(\sqrt D=y/2\). Therefore the claimed \(\Lambda_B(D)=r+f_B(y)\) holds, with
\[
f_B(y)=-\frac y2-\frac3{1+y^2}-\frac{900B}{900+y^2},\quad y>0.
\]

**3. Exactly four critical points.** Differentiate:
\[
f_B'(y)=-\frac12+\frac{6y}{(1+y^2)^2}+\frac{1800By}{(900+y^2)^2}.
\]
The critical-point equation is \(B=h(y)\), where
\[
h(y)=\frac{((1+y^2)^2-12y)(900+y^2)^2}{3600y(1+y^2)^2}.
\]
Direct differentiation yields
\[
h'(y)=\frac{(y^2+900)Q(y)}{1200y^2(1+y^2)^3},\qquad Q(y)=y^8-297y^6-897y^4+14384y^3-899y^2-300.
\]
Descartes' rule of signs gives at most three positive zeros of \(Q\). The sign changes of \(Q\) across \((0,1/2)\), \((1/2,4)\) and \((4,20)\) give three distinct zeros, hence exactly three. Consequently any horizontal line intersects \(h\) at most four times. For every \(B\in[26,27]\), the exact signs of \(f_B'\) at \(0,1/5,2,3,9,13,24,28\) are respectively \(-,+,+,-,-,+,+,-\). These signs hold at both \(B=26\) and \(B=27\), and dependence on \(B\) is affine. Therefore there are precisely four simple positive critical points, one each in
\[
(0,1/5),\quad(2,3),\quad(9,13),\quad(24,28).
\]
In order, they are a local minimum, local maximum, local minimum and local maximum. Write the two maximizing branches \(l(B)\in(2,3)\) and \(h_+(B)\in(24,28)\); their simplicity and continuity follow also from the displayed sign bounds and the three-zero count.

**4. The endpoint is not optimal.** Since \(f_B(0)=-3-B\) and \(f_B(2)-f_B(0)=7/5+B/226>0\), the possible limiting endpoint \(y\downarrow0\) loses to an interior point. Also \(f_B(y)\to-\infty\) as \(y\to\infty\). Thus only the two interior local maxima can be global.

**5. Opposite ordering at the two endpoint environments.** At \(B=26\), for all \(24\le y\le28\),
\[
\frac y2+\frac{23400}{900+y^2}>\frac{277}{10}.
\]
After multiplying by the positive \(10(900+y^2)\) and setting \(t=y-25\in[-1,3]\), the difference becomes \(5t^3+98t^2+25t+2200>0\). Indeed \(5t^3\ge-5\) and \(98t^2+25t\ge-625/392>-2\). Hence \(f_{26}(h_+(26))<-277/10\), while \(f_{26}(l(26))\ge f_{26}(2)=-15529/565>-277/10\).

At \(B=27\) and \(2\le y\le3\), \(24300/(900+y^2)\ge27-3y^2/100\). Meanwhile
\[
\frac y2+\frac3{1+y^2}-\frac{3y^2}{100}>\frac{36}{25}.
\]
Multiplying by \(100(1+y^2)\) and setting \(t=y-2\in[0,1]\) reduces positivity to \(-3t^4+26t^3+81t^2-34t+20>0\): the first two terms sum to at least \(23t^3\), while the quadratic \(81t^2-34t+20\) has negative discriminant and positive leading coefficient. Thus \(f_{27}(l(27))<-711/25\), but \(f_{27}(h_+(27))\ge f_{27}(26)=-7581551/266738>-711/25\).

**6. Uniqueness of the crossing.** The branch-height difference \(H(B)=f_B(h_+(B))-f_B(l(B))\) is continuously differentiable, and the stationary-point envelope identity gives
\[
H'(B)=\frac{900}{900+l(B)^2}-\frac{900}{900+h_+(B)^2}>0.
\]
By step 5, \(H(26)<0<H(27)\), hence it has a unique zero \(B_*\in(26,27)\). Strict monotonicity gives the claimed one-sided unique global maximizers and their discontinuous switch. This completes the proof.

## Verification
The accompanying standalone `verify.py` recomputes the exact derivative identity, Descartes sign count, all endpoint derivative signs, rational comparison inequalities and stationary branch crossing numerically to stated tolerances. The infinite claims depend on the analytic steps above, not on numerical sampling.

## Relationship to prior work
Pathiraja and Wacker (arXiv:2412.08178, Section 4.5) explicitly give the tracking lag and population growth under **one** sinusoid, and their Gaussian evolution framework applies to time-varying quadratic landscapes generally. Our Gaussian equations and single-frequency spectral response are applications of that prior method, **not discoveries**. The present additional statement is the rigorous two-frequency *global argmax classification* (exact number of positive stationary points, uniqueness of two co-optima, and a discontinuous optimizer transition), which is not contained in the inspected single-harmonic results. Ardaševa and collaborators (2019) study competition and phenotypic diffusion under a periodically fluctuating nutrient, including high- versus low-mutator advantage; their full open-access article does not state the present two-harmonic degeneracy/uniqueness result. Carrère and Nadin (2020) establish mutation-rate effects under periodic fitness with general Floquet methods; their indexed abstract does not resolve this exact crossing, but complete-text comparison remains a literature risk. Duong, Balabanova and van Rensburg (2026) show a mutation-rate selection principle in a time-changing trait-structured Lotka–Volterra system, motivating study of more than one environmental frequency; they do not specify the two-harmonic extremal classification.

## Limitations
The result concerns a deliberately explicit quadratic-Gaussian model with frequencies \(1\) and \(30\), harmonic amplitudes fixed by \(6\) and \(2B\), and mutation rate ranging over all positive real values. It does not establish frequency-multiplicity transitions for arbitrary spectra, ecological competition between simultaneously present mutator genotypes, or convergence of non-Gaussian trait distributions. The crossing constant is characterized uniquely but not expressed in radicals. The 2024 Gaussian framework is stronger in its evolution-equation coverage and already implies the *rate formula* after frequency superposition; only the nontrivial optimizer-topology conclusion is claimed as additional. A full-text comparison of Carrère–Nadin (2020) and any as-yet-unindexed work could further affect originality.

## References
1. M. H. Duong, N. Balabanova, B. van Rensburg, *Global Dynamics of Trait-Structured Generalised Lotka–Volterra Systems with Trait-Independent Interactions*, arXiv:2607.25573v1, initially public July 28, 2026. https://arxiv.org/abs/2607.25573
2. S. Pathiraja, P. Wacker, *Mathematical description of continuous time and space replicator-mutator equations for quadratic fitness landscapes*, arXiv:2412.08178, Section 4.5. https://arxiv.org/abs/2412.08178
3. A. Ardaševa et al., *Evolutionary dynamics of competing phenotype-structured populations in periodically fluctuating environments*, Journal of Mathematical Biology 80 (2020), 775–807. https://doi.org/10.1007/s00285-019-01441-5
4. C. Carrère, G. Nadin, *Influence of mutations in phenotypically-structured populations in time periodic environment*, DCDS-B 25 (2020), 3609–3630. https://doi.org/10.3934/dcdsb.2020075
