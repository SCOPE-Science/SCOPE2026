# Sharp disconnected network Turing windows with strict local prey and predator biomass loss

## Finding

Let \(G\) be a finite connected, simple, undirected graph on \(n\ge2\) vertices, with combinatorial Laplacian \(L=D-A\). For \(t,r>0\), consider
\[
\dot u_i=u_i(-u_i^2+3u_i-1-v_i)-t(Lu)_i,\qquad
\dot v_i=v_i(4u_i-3v_i-1)-rt(Lv)_i. \tag{1}
\]
There are two strictly positive spatially uniform equilibria: \((u_i,v_i)=(1,1)\) and \((2/3,5/9)\). All stability and bifurcation assertions below refer to **\((1,1)\)**.

For \(0<r<9\), \((1,1)\) is linearly exponentially stable for all \(t>0\). At \(r=9\), it has no exponentially growing mode and is nonhyperbolic exactly at \(t=1/(3\lambda)\) for the positive eigenvalues \(\lambda\) of \(L\). For \(r>9\), write
\[
z_\pm=\frac{r-3\pm\sqrt{(r-1)(r-9)}}{2r},\qquad 0<z_-<z_+<1.
\]
There is an exponentially growing mode exactly for
\[
t\in\bigcup_{\lambda>0}\left(\frac{z_-}{\lambda},\frac{z_+}{\lambda}\right). \tag{2}
\]
Linear exponential stability holds exactly outside the union of the corresponding closed intervals. Every modal endpoint \(t=z_\pm/\lambda\) has a zero eigenvalue, including endpoints inside another mode's instability interval.

Fix \(r>9\) and a modal endpoint \(t_*=z_\pm/\lambda\) with \(\lambda\) simple, and assume no other eigenvalue of \(L\) has a zero modal determinant at \(t_*\). For a real nonzero eigenvector \(L\phi=\lambda\phi\), there is a locally unique smooth branch of nonuniform, strictly positive stationary states, up to scalar parametrization, with
\[
u_i(s)=1+s\phi_i+O(s^2),\qquad v_i(s)=1+hs\phi_i+O(s^2),\qquad t(s)=t_*+O(s),\quad h=1-z_\pm. \tag{3}
\]
Writing bars for vertex means and \(\sigma^2=n^{-1}\sum_i\phi_i^2>0\), both means are strictly less than one at every sufficiently small nonzero branch point:
\[
\bar u(s)=1-(7h-3h^2)\sigma^2s^2+o(s^2),\qquad
\bar v(s)=1-(8h-3h^2)\sigma^2s^2+o(s^2). \tag{4}
\]
The predator's mean deficit exceeds the prey's by \(h\sigma^2s^2+o(s^2)\). At **every** stationary configuration of (1), putting \(U_i=u_i-1\), \(V_i=v_i-1\), and writing \(\langle\cdot\rangle\) for the vertex mean, one has the exact balances
\[
\bar u-1=-7\langle UV\rangle+3\langle V^2\rangle-3\langle U^3\rangle,\qquad
\bar v-1=-8\langle UV\rangle+3\langle V^2\rangle-4\langle U^3\rangle. \tag{5}
\]
The exact balances alone do not imply strict negativity for all stationary states.

**Separated windows on paths.** For every \(n\ge3\), the path \(P_n\) has simple positive eigenvalues \(\lambda_j=2-2\cos(j\pi/n)\), \(1\le j\le n-1\). Choosing \(r>9\) sufficiently near 9 so that
\[
z_+/z_-<\min_{1\le j<n-1}\lambda_{j+1}/\lambda_j \tag{6}
\]
gives exactly \(n-1\) disjoint open instability intervals with stable gaps. Each of the \(2(n-1)\) endpoints gives a branch with the mean deficits (4). For \(n=2\), there is one window for any \(r>9\) and a branch at each endpoint. Thus no graph-independent finite bound exists on the number of stability losses and recoveries as \(t\) varies. For instance, on \(P_3\) with \(r=91/10\), the roots are \(2/7,5/13\), and the windows are \((2/21,5/39)\) and \((2/7,5/13)\).

## Assumptions and scope

Both species diffuse on the same undirected, unweighted, connected graph, with constant rates in ratio \(r\). Nonnegative initial states stay nonnegative since the corresponding reaction vanishes at each zero coordinate and the diffusion contribution there is nonnegative. In the absence of predators the prey per-capita growth \(-u^2+3u-1\) gives a strong Allee effect. These are the specified polynomial kinetics, not an exact reduction of a weak-Allee model with hyperbolic predator mortality. Equations (3)–(4) require an isolated simple zero with \(r>9\). They assert neither attraction of the patterns nor global persistence; (5) does not establish the sign of the means for arbitrary distant equilibria.

## Proof

**Uniform states and spectrum.** At a positive uniform equilibrium, diffusion vanishes, and stationarity requires \(v=(4u-1)/3=-u^2+3u-1\). Hence \((3u-2)(u-1)=0\), giving exactly the two listed equilibria. At \((1,1)\), the Jacobian in the Laplacian eigenmode \(\lambda\), with \(z=t\lambda\), is
\[
M(z)=\begin{pmatrix}1-z&-1\\4&-3-rz\end{pmatrix},\qquad
\operatorname{tr}M=-2-(1+r)z,\qquad \det M=1-(r-3)z+rz^2.
\]
The trace is strictly negative, including for the uniform mode \(\lambda=0\). A negative determinant gives one positive eigenvalue, a positive determinant gives two eigenvalues with negative real parts, and a zero determinant gives one zero eigenvalue. For \(r\le3\) the determinant is positive on \(z\ge0\); for \(3<r<9\) its discriminant \((r-1)(r-9)\) is negative. At \(r=9\) it equals \((1-3z)^2\). For \(r>9\) the roots are simple, positive, and their sum \(1-3/r\) is less than one. The determinant is negative only strictly between the roots. Orthogonal Laplacian mode decomposition now proves all linear assertions.

**Isolated thresholds.** The stationary map is polynomial and vanishes on the trivial branch \((u,v)=(\mathbf1,\mathbf1)\). At an indicated simple threshold its state derivative has one-dimensional kernel with mode vector \((1,h)\), and a one-dimensional left null space with mode row \((4,-h)\). Indeed \(h(3+rz_\pm)=4\). The range has codimension one and the parameter derivative of the modal state derivative obeys
\[
(4,-h)\,\partial_t M(t\lambda)\,(1,h)^\mathsf{T}
=\lambda(-4+rh^2)=-\lambda h\,[2rz_\pm-(r-3)]\ne0.
\]
The simple-eigenvalue bifurcation theorem therefore yields the unique local nontrivial branch and the tangent in (3). The vector \(\phi\) is orthogonal to \(\mathbf1\), so nontrivial points are nonuniform for small nonzero \(s\); positivity follows by continuity.

**Vertex means.** About \((1,1)\), the two local reactions expand exactly as \(U_i-V_i-U_iV_i-U_i^3\) and \(4U_i-3V_i+4U_iV_i-3V_i^2\). Since \(\mathbf1^\mathsf{T}L=0\), their averages vanish at any stationary state. Thus with \(a=\bar u-1\), \(b=\bar v-1\), one has \(a-b=\langle UV\rangle+\langle U^3\rangle\) and \(4a-3b=-4\langle UV\rangle+3\langle V^2\rangle\). Solving gives (5). On (3), these three moments are \(h\sigma^2s^2+o(s^2)\), \(h^2\sigma^2s^2+o(s^2)\) and \(O(s^3)\), respectively. Substitution gives (4), whose two deficit coefficients are positive for \(0<h<1\).

**Path separation.** The cosine vectors with entries \(\cos((i-1/2)j\pi/n)\) satisfy the endpoint and interior Laplacian equations, giving the stated strictly increasing eigenvalues. The smallest ratio in (6) exceeds one for every fixed \(n\ge3\), while \(z_+/z_-\to1\) as \(r\downarrow9\). Inequality (6) orders the consecutive bands with strict gaps, makes every endpoint isolated, and gives the branch conclusion. The case \(P_2\) has only \(\lambda=2\); the example follows from the two roots and the positive spectrum \(1,3\) for \(P_3\).

## Verification

The accompanying `verify.py` (Python 3, SymPy, NumPy) checks modal and mean identities for \((1,1)\), the exact small-path example, and path spectra and interval separation for \(2\le n\le40\). The general spectrum and nonlinear branch claims follow from the analytic proof, not from the finite checks; the second uniform equilibrium follows from the quadratic factorization above.

## Relationship to prior work

Nakao and Mikhailov established the general network-Laplacian modal method for activator–inhibitor systems. Ye and Zhou analyze a Turing instability interval in a different predator–prey model with weak Allee effect and hyperbolic mortality; Shi, Zhou and Ye extend that model to multiplexes. Here the substantive findings are the exact coefficient-level two-species mean balance and strict local mean deficits at the simple thresholds of the specified polynomial model, and the separated path-scale windows exhibiting those deficits. Neither general modal theory nor the simple-eigenvalue bifurcation theorem is claimed as new. This does not establish literature priority beyond the available statement comparisons.

## References

1. Y. Ye and J. Zhou, *Pattern formation in a predator-prey model with Allee effect and hyperbolic mortality on networked and non-networked environments*, https://arxiv.org/html/2306.11818v2.
2. L. Shi, J. Zhou and Y. Ye, *Pattern Formation in a Predator-Prey Model with Allee Effect and Hyperbolic Mortality on Multiplex Networks*, https://www.preprints.org/manuscript/202306.1868.
3. H. Nakao and A. S. Mikhailov, *Turing patterns in network-organized activator-inhibitor systems*, https://arxiv.org/abs/1005.1986.
4. X. Luo et al., *The relationship between clustering and networked Turing patterns*, Chaos 34, 073114 (2024), doi:10.1063/5.0195450.
