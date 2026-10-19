# Complete dissipation fibers for balanced three-state stochastic oscillators

## Finding
Fix arbitrary real numbers \(s>0\) and \(0<\omega<s/\sqrt3\). Among all continuous-time three-state Markov generators with six strictly positive transition rates, uniform stationary distribution \(\pi=(1/3,1/3,1/3)\), and complete spectrum \(\{0,-s+i\omega,-s-i\omega\}\), the **exact attainable set** of stationary entropy-production rates is
\[
\boxed{\left[\frac{2\omega}{\sqrt3}\log\!\frac{s+\sqrt3\omega}{s-\sqrt3\omega},\ \infty\right).}
\]
The left endpoint is attained only by a homogeneous biased cycle (up to orientation and permutation). For **every** finite entropy-production value above it, a strictly bidirectional generator with this same complete spectrum, stationary distribution, and stationary mean jump activity \(2s/3\) exists. In particular, no upper bound on entropy production follows from those spectral and stationary observations, even within this smallest oscillatory model.

The lower-end inequality and its equality case are compatible with, and can be deduced from, the previously established affinity/eigenvalue bounds for unicyclic generators. The distinct contribution here is the **complete spectral-fiber image**: all finite values occur, and no upper bound exists at *every* admissible complex eigenpair.

## Assumptions and scope
States are labeled cyclically \(1,2,3\). The jump rate from state \(i\) to state \(j\) is \(k_{ij}>0\), with each of the six off-diagonal rates finite. The row generator has off-diagonal entry \(k_{ij}\) and diagonal entry the negative row sum. Uniform stationarity means both row and column sums vanish; irreducibility follows from strict positivity.

Define the standard stationary Schnakenberg entropy-production rate using natural logarithms:
\[
\sigma=\sum_{i<j}(\pi_i k_{ij}-\pi_j k_{ji})\log\!\frac{\pi_i k_{ij}}{\pi_j k_{ji}}.
\]
This is an entropy-production **rate**, in inverse-time units with dimensionless entropy. It is not the cycle affinity and is not the per-period entropy without multiplying by the period. The stationary mean jump activity is \(\mathcal A=\sum_i\pi_i\sum_{j\ne i}k_{ij}\).

## Proof
**1. Exhaustive parametrization.** Since the stationary probability is uniform, current conservation requires the three oriented edge-current differences to be equal. Possibly reverse the cyclic orientation so that the common half-difference \(\kappa>0\). Every admissible generator can therefore be written uniquely in the form
\[
\begin{array}{lll}
k_{12}=a+\kappa,&k_{21}=a-\kappa,&
k_{23}=b+\kappa,\\
k_{32}=b-\kappa,&k_{31}=c+\kappa,&k_{13}=c-\kappa,
\end{array}
\]
with \(a,b,c>\kappa>0\). A complex spectral pair implies \(\kappa\ne0\), as follows below. Its row generator is
\[
Q=\begin{pmatrix}
-a-c&a+\kappa&c-\kappa\\
a-\kappa&-a-b&b+\kappa\\
c+\kappa&b-\kappa&-b-c
\end{pmatrix}.
\]

**2. Spectral invariants.** Put \(S=a+b+c\) and \(\Delta=a^2+b^2+c^2-ab-bc-ca=\tfrac12[(a-b)^2+(b-c)^2+(c-a)^2]\ge0\). Direct expansion gives
\[
\det(zI-Q)=z\bigl[(z+S)^2-\Delta+3\kappa^2\bigr].
\]
Hence the required nonzero eigenvalues imply
\[
S=s,\qquad \omega^2=3\kappa^2-\Delta,
\qquad \kappa\ge\omega/\sqrt3.
\]
Positivity imposes \(\kappa<\min(a,b,c)\le s/3\), so necessarily \(0<\omega<s/\sqrt3\). Conversely, every pair in that open region is realized by the homogeneous rates \(a=b=c=s/3\), \(\kappa=\omega/\sqrt3\). For every generator in the fiber, the stationary jump activity is
\[
\mathcal A=\tfrac13\bigl(2(a+b+c)\bigr)=2s/3.
\]

**3. Lower endpoint and rigidity.** The common oriented stationary edge current is \(2\kappa/3\). Therefore
\[
\sigma=\frac{2\kappa}{3}\left[\log\frac{a+\kappa}{a-\kappa}+\log\frac{b+\kappa}{b-\kappa}+\log\frac{c+\kappa}{c-\kappa}\right].
\]
For fixed \(\kappa>0\), the function \(f_\kappa(v)=\log[(v+\kappa)/(v-\kappa)]\) on \(v>\kappa\) is strictly convex, because
\[
f_\kappa''(v)=\frac{4\kappa v}{(v^2-\kappa^2)^2}>0.
\]
Jensen's inequality, with \(a+b+c=s\), gives
\[
\sigma\ge2\kappa\log\frac{s/3+\kappa}{s/3-\kappa}.
\]
The right-hand side is strictly increasing on \(0<\kappa<s/3\); since \(\kappa\ge\omega/\sqrt3\), this is at least the displayed lower endpoint. Equality in Jensen requires \(a=b=c\); the spectral identity then forces \(\kappa=\omega/\sqrt3\). The homogeneous cycle indeed realizes the lower endpoint.

**4. A fixed-spectrum path to divergent entropy production.** Set \(A=s/3\) and
\[
u_* =\frac{\sqrt{3A^2-2\omega^2/3}-A}{2}.
\]
Since \(0<\omega<s/\sqrt3\), one has \(0<u_*<A\). For every \(0\le u<u_*\), define
\[
a(u)=A+2u,\quad b(u)=c(u)=A-u,\quad
\kappa(u)=\sqrt{\omega^2/3+3u^2}.
\]
The defining quadratic identity for \(u_*\) is
\[
(A-u_*)^2=\omega^2/3+3u_*^2.
\]
For \(0\le u<u_*\), \(b(u)=c(u)>\kappa(u)>0\), and \(a(u)>\kappa(u)\); thus all six rates remain strictly positive. Direct substitution gives \(S=s\) and \(\Delta=9u^2\), so \(3\kappa(u)^2-\Delta=\omega^2\) identically. Uniform stationarity and activity are also unchanged.

At \(u=0\), the homogeneous cycle attains the lower endpoint. As \(u\uparrow u_*\), the two reverse rates \(b(u)-\kappa(u)\) and \(c(u)-\kappa(u)\) decrease to zero, whereas \(\kappa(u)\to A-u_*>0\). The two corresponding logarithmic contributions to \(\sigma\) consequently diverge to \(+\infty\). Since \(\sigma(u)\) is continuous on the connected interval \([0,u_*)\), takes its global minimum at \(u=0\), and is unbounded above, its image is **exactly** the whole half-line stated in the finding. This is an existence result for every finite target, not merely a limiting sequence.

## Verification
Run `python3 verify.py` using the Python standard library. The program checks exact rational generator identities for \(1029\) cases, \(16885\) heterogeneous oscillatory examples, \(399\) saturating homogeneous parameter choices, and \(9980\) fixed-spectrum fiber points (\(28293\) groups total). Its checks reproduce the constant spectrum and activity along the explicit path and the predicted entropy bounds. Finite checks support but do not replace the general inequalities and limiting arguments above.

## Relationship to prior work
J. Gu's 2026 dissipation-coherence theorem gives a general lower bound with an eigenvector-uniformity factor and studies homogeneous and heterogeneous rings; it does not identify the full image of entropy production at fixed complex eigenvalues, uniform stationary law, and activity. Kolchinsky–Ohga–Ito's 2026 cycle-affinity localization theorem supplies a sharp **lower** bound on cycle affinity at fixed spectral location, with equality for homogeneous rings. Together with elementary current constraints, that theorem already implies the lower-end bound above; the lower bound alone is **not claimed as new**. Neither source establishes the present continuous isospectral path with divergent entropy production or the resulting exact half-line of attainable rates. Shiraishi's general 2026 eigenvalue/entropy counterexamples do not assert this precise uniformly stationary three-state classification.

## Limitations
The classification is specific to **exactly three states**, strict bidirectionality, uniform stationary law, and a **nonreal** nonzero eigenvalue pair. No conclusion is made for general stationary weights, reversible real-spectrum fibers, higher-state networks, bounded-away-from-zero reverse rates, or entropy production inferred from full transition matrices. The divergent limit approaches but never reaches a zero backward rate; every individual realizing generator retains strictly positive finite rates. Oscillatory eigenvalues need not correspond to many observable cycles before relaxation.

## References
1. Jie Gu, *Dissipation-coherence tradeoff for stochastic oscillations*, arXiv:2606.05498v1, first public 2026-06-03, https://arxiv.org/html/2606.05498v1 .
2. Artemy Kolchinsky, Naruo Ohga, Sosuke Ito, *Cycle affinity and winding localize eigenvalues of Markov generators*, arXiv:2605.15884v1, first public 2026-05-15; inspected v3 2026-10-08, https://arxiv.org/pdf/2605.15884 .
3. Naoto Shiraishi, *Second largest eigenvalue does not bound stationary entropy production*, arXiv:2609.34352v1, first public 2026-09-28, https://arxiv.org/abs/2609.34352 .
4. A. Kolchinsky, N. Ohga, S. Ito, *Thermodynamic bounds on spectral perturbations, with applications to oscillations and relaxation dynamics*, Physical Review Research 6, 013082 (2024), https://arxiv.org/abs/2304.01714 .
