# Exact global monostability frontier and critical logarithmic relaxation in logistic threshold networks

## Finding
For every finite nonnegative row-stochastic network, an identical logistic threshold rule has a unique globally attracting equilibrium **exactly outside the closed scalar hysteresis interval** (and at every stimulus when feedback is at most its cusp value). At the cusp, convergence has a sharp topology-independent squared-amplitude envelope. For every irreducible network, all trajectories outside a codimension-one exceptional strong-stable set additionally obey the **same** inverse-square logarithmic asymptotic expansion, including the coefficient \(-8/5\), independent of network size and edge weights.

More precisely, write \(\ell(z)=1/(1+e^{-z})\). For an integer \(N\ge2\), any matrix \(W=(w_{ij})\) with \(w_{ij}\ge0\) and \(\sum_j w_{ij}=1\), \(\beta\ge0\), and \(a\in\mathbb R\), consider the forward flow on \([0,1]^N\)
\[
\dot x_i=-x_i+\ell\!\left(a+\beta\sum_{j=1}^Nw_{ij}x_j\right),\qquad 1\le i\le N. \tag{1}
\]
When \(\beta>4\), set
\[
q_\pm=\frac{1\pm\sqrt{1-4/\beta}}2,\qquad
 a_-=\log\frac{q_+}{1-q_+}-\beta q_+,\quad
 a_+=\log\frac{q_-}{1-q_-}-\beta q_-.
\]
Then \(a_-<a_+\). The following statements are equivalent:

1. The scalar equation \(\dot s=-s+\ell(a+\beta s)\) has exactly one equilibrium in \([0,1]\).
2. For **every** finite nonnegative row-stochastic \(W\), (1) has exactly one equilibrium, which attracts every trajectory from \([0,1]^N\).
3. Either \(0\le\beta\le4\), or \(\beta>4\) and \(a\notin[a_-,a_+]\).

The unique equilibrium in (2) is the constant state \(s_*\mathbf1\). At a parameter on or within the closed interval \([a_-,a_+]\) with \(\beta>4\), **every** network has at least two distinct constant equilibria; in the open interval, it has at least three.

At the critical parameters \((a,\beta)=(-2,4)\), every trajectory converges to \(\tfrac12\mathbf1\), and
\[
\limsup_{t\to\infty}t\,\big\|x(t)-\tfrac12\mathbf1\big\|_\infty^2\le\frac38.\tag{2}
\]
The coefficient \(3/8\) is optimal for each admissible network, as witnessed by every nonstationary constant initial state. If, in addition, \(W\) is irreducible, the equilibrium has a locally defined codimension-one strong-stable manifold. For each initial state not eventually on this manifold, there exists a real constant \(C\) depending on the trajectory such that **simultaneously for all coordinates**
\[
\frac1{(x_i(t)-1/2)^2}=\frac83t-\frac85\log t+C+o(1),\qquad t\to\infty.\tag{3}
\]
The exceptional trajectories instead approach the equilibrium exponentially. On nonexceptional trajectories all coordinate displacements eventually have the same nonzero sign. In particular \(t(x_i(t)-1/2)^2\to3/8\) for every coordinate. Statements (2) and (3) refer to the original continuous physical time of (1), without rescaling.

## Assumptions and scope
Matrix entries may be directed, nonsymmetric, zero, and reducible in the global statements; no connectivity, diagonalizability, or block equitability is assumed. The sharper all-coordinate expansion (3) requires irreducibility, in the Perron–Frobenius sense. All initial states belong to the closed unit cube and all times are forward times \(t\ge0\). The parameters \(a\) and \(\beta\) are common to the nodes, and \(\ell\) is the standard logistic cumulative distribution function with unit scale.

“Globally attracting unique equilibrium” means uniqueness among all equilibria in the closed cube and convergence of every forward orbit to that equilibrium, including nonconstant initial configurations. It does not assert uniform exponential attraction at the cusp.

## Proof
**Step 1: trapping and comparison.** The coordinate vector field at \(x_i=0\) points strictly inward and at \(x_i=1\) points strictly inward. Thus the compact cube is forward invariant and all solutions exist for all \(t\ge0\). The system is cooperative since \(\partial\dot x_i/\partial x_j=\beta w_{ij}\ell'(a+\beta(Wx)_i)\ge0\) for \(i\ne j\).

Let \(u_-(t)\) and \(u_+(t)\) solve the scalar equation \(\dot u=-u+\ell(a+\beta u)\) with initial values \(\min_i x_i(0)\) and \(\max_i x_i(0)\), respectively. Since \(W\mathbf1=\mathbf1\), scalar solutions lift to exact network solutions \(u_\pm(t)\mathbf1\). Order preservation gives
\[
u_-(t)\mathbf1\le x(t)\le u_+(t)\mathbf1\quad (t\ge0).\tag{4}
\]
Every scalar trajectory converges to a scalar equilibrium: the scalar vector field is positive at zero, negative at one, and has only isolated roots; between adjacent roots its sign is constant. If the scalar equilibrium \(s_*\) is unique, both bounds in (4) converge to \(s_*\), proving global convergence of every network trajectory. Equation (4) also implies Lyapunov stability of the synchronized equilibrium from scalar stability. Conversely, every scalar equilibrium yields the network equilibrium \(s\mathbf1\); two scalar equilibria therefore preclude network-wide unique equilibrium for **every** row-stochastic \(W\).

**Step 2: exact scalar frontier.** The scalar equilibrium equation is
\[
G_\beta(s)=a,\qquad G_\beta(s)=\log\frac{s}{1-s}-\beta s,\quad0<s<1.
\]
Its derivative is \(G'_\beta(s)=1/[s(1-s)]-\beta\). For \(\beta\le4\), this is nonnegative and vanishes at most at the single point \(s=1/2\). Thus \(G_\beta\) is strictly increasing from \(-\infty\) to \(+\infty\). For \(\beta>4\), the derivative changes signs at \(q_-\) and \(q_+\), with a local maximum \(G_\beta(q_-)=a_+\) and a local minimum \(G_\beta(q_+)=a_-\). Hence there are three scalar equilibria for \(a_-<a<a_+\), two distinct equilibria at either equality, and one outside the closed interval. Together with Step 1 this proves all equivalences and sharpness.

**Step 3: critical scalar expansion.** At \((a,\beta)=(-2,4)\), set \(u=s-1/2\). The identity \(\ell(4u)=(1+\tanh(2u))/2\) gives the exact scalar vector field
\[
\dot u=-u+\tfrac12\tanh(2u)
=-\tfrac43u^3+\tfrac{32}{15}u^5+O(u^7).\tag{5}
\]
Every nonzero scalar solution keeps its sign, decreases in absolute value toward zero, and has \(t\,u(t)^2\to3/8\). To obtain the next term, put \(z=u^{-2}\). Then
\[
\dot z=\frac83-\frac{64}{15z}+O(z^{-2}).\tag{6}
\]
First \(z/t\to8/3\); substitution into (6) gives \(z(t)=(8/3)t+O(\log t)\). Consequently
\[
\frac{d}{dt}\left[z(t)-\tfrac83t+\tfrac85\log t\right]
=O\!\left(\frac{\log t}{t^2}\right),
\]
which is integrable. Thus every nonzero scalar trajectory has
\[
z(t)=\frac83t-\frac85\log t+C_s+o(1).\tag{7}
\]
The trapping (4), applied to the scalar solutions from the minimum and maximum initial coordinates, implies (2). Constant nonstationary initial data make (2) an equality in the limit, showing its sharpness.

**Step 4: irreducible networks and the shared correction.** At the critical synchronized state the Jacobian of (1) is \(J=W-I\). Irreducibility and row stochasticity imply that the eigenvalue \(1\) of \(W\) is algebraically simple with right eigenvector \(\mathbf1\), and every other eigenvalue \(\lambda\) satisfies \(\Re\lambda<1\). Thus \(J\) has one simple zero eigenvalue and all other eigenvalues have strictly negative real parts. The invariant diagonal \(\{(1/2+u)\mathbf1\}\) is an **exact** smooth one-dimensional center manifold, on which the reduced equation is precisely (5). Its local stable foliation gives an asymptotic-phase decomposition: any sufficiently late piece of any trajectory near the equilibrium is exponentially close, in the same time parameter, to a unique diagonal scalar solution. The exceptional leaf corresponding to the stationary scalar solution is the codimension-one strong-stable manifold and consists exactly of local trajectories with exponential approach.

A trajectory not in this exceptional set therefore has, for some \(\kappa>0\), \(x_i(t)-1/2=u(t)+O(e^{-\kappa t})\) uniformly in \(i\), where \(u(t)\) is a nonzero scalar solution. Since \(|u(t)|\asymp t^{-1/2}\), taking inverse squares changes (7) by only \(O(t^{3/2}e^{-\kappa t})=o(1)\). This proves (3) with **the same constant** \(C=C_s\) for all nodes, and completes the proof.

## Verification
The accompanying file `verify.py` uses exact symbolic series arithmetic to check the cubic and quintic coefficients in (5), the resulting universal inverse-square coefficients, and the fold identities for three feedback strengths. It also integrates two distinct irreducible row-stochastic three-node matrices from several initial states, checking finite-time approach to the predicted leading coefficient and stabilized logarithmic residual. Run it as `python verify.py` with SymPy, NumPy and SciPy available. These computations are illustrative; Steps 1–4 prove the conclusions for every finite admissible network.

## Relationship to prior work
Boudourides, *Collective Hysteresis and Multistability in Threshold Networks* (arXiv:2609.10580, first submitted 2026-09-05), formulates this positive row-stochastic logistic feedback network as a special case, proves unique global attraction under **sufficiently weak feedback**, and analyzes homogeneous folds and network bifurcations. The homogeneous cusp and its location are prior work, **not** claimed as new. The first part of the present theorem replaces the weak-feedback sufficiency with an exact **all-network** criterion that extends to arbitrarily large \(\beta\) outside the closed scalar bistability wedge, and treats equality cases explicitly. The second part gives the sharp network-wide critical physical-time relaxation law, including its nonzero logarithmic correction and exceptional manifold.

Classical order comparison supplies the trapping mechanism, and standard center-manifold stable-foliation theory supplies exponential tracking; neither method is claimed as new. Earlier results on synchronization and contrast contraction for the same threshold-network model control differences of nodes, rather than establishing the exact large-feedback monostability frontier together with the common critical inverse-square logarithm. Analogous logarithmic relaxation results for other dynamical systems do not imply the numerical coefficients for this network family.

## Limitations
The theorem requires **identical** logistic thresholds and feedback gain, as well as nonnegative row sums equal to one. It does not apply directly to signed/competitive coupling, heterogeneous logistic scales, time delays, stochastic switching, or coupling with nonconstant row sums. The logarithmic formula is established under irreducibility; only the sharp envelope is asserted here without that assumption. At feedback strengths inside the closed bistability wedge, the theorem asserts multiple homogeneous equilibria, not a complete census of heterogeneous equilibria or basins. The result has not undergone independent mathematical audit. Priority against unindexed earlier work remains a possibility. The motivating preprint was compared at the level of its full parsed text, including the principal theorems and appendices.

## References
- M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580 (first submission 2026-09-05), https://arxiv.org/abs/2609.10580.
- A. R. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, Journal of The Royal Society Interface **23** (2026), 20260267 (underlying scalar collective threshold model).
- J. Carr, *Center Manifold*, Scholarpedia **1**(12):1826 (2006), https://doi.org/10.4249/scholarpedia.1826.
- F. Collet, *Macroscopic limit of a bipartite Curie–Weiss model: a dynamical approach*, arXiv:1406.4044 (2014), for related two-population symmetry-breaking phase diagrams, not the claimed global threshold-network relaxation law.
