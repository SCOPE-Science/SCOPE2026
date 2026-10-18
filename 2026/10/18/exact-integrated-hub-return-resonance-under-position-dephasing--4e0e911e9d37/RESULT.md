# Exact integrated hub-return resonance under position dephasing

## Finding

For a finite simple undirected graph with a universal vertex, the integrated normalized excess return probability of a Haken–Strobl quantum walk has a universal closed form, independent of every edge not touching that vertex. More precisely, for an integer \(k\geq2\), take any graph on \(k+1\) vertices with a vertex \(o\) joined to all other \(k\) vertices. With the combinatorial Laplacian as Hamiltonian, unit coherent hopping amplitude, and positive position-dephasing rate \(\gamma\), initialize the density matrix to \(P_o\). Let \(p_{k,\gamma}(t)\) be the probability of occupying \(o\) at time \(t\geq0\), and define

\[
c_{k,\gamma}(t)=\frac{p_{k,\gamma}(t)-1/(k+1)}{1-1/(k+1)}.
\]

Then the entire density-matrix trajectory, and hence the hub return, is independent of the graph induced by the other vertices. Its normalized excess-return Laplace transform is

\[
\int_0^\infty e^{-st}c_{k,\gamma}(t)\,dt
=\frac{(s+\gamma)^2+k^2-1}{s\big((s+\gamma)^2+k^2-1\big)+2(k+1)(s+\gamma)},\qquad \operatorname{Re}s>0.
\]

The signed, integrated return susceptibility converges for every \(\gamma>0\) and equals

\[
\boxed{T_k(\gamma):=\int_0^\infty c_{k,\gamma}(t)\,dt=\frac{\gamma}{2(k+1)}+\frac{k-1}{2\gamma}.}
\]

It has a unique global minimizer and exact minimum

\[
\boxed{\gamma_*(k)=\sqrt{k^2-1},\qquad T_k(\gamma_*)=\sqrt{\frac{k-1}{k+1}}.}
\]

For fixed \(\theta>0\), setting \(\gamma=\theta k\) yields the additional uniform-in-time asymptotic

\[
\sup_{t\geq0}\left|c_{k,\theta k}(t)-\exp\!\left(-\frac{2\theta}{1+\theta^2}t\right)\right|=O_\theta(k^{-1}).
\]

The limiting decay rate \(2\theta/(1+\theta^2)\) has the unique maximum \(1\) at \(\theta=1\), matching the exact finite-degree optimizer asymptotically. The normalization is chosen so that \(c_{k,\gamma}(0)=1\). Its time integral is signed: this theorem does not identify it with a total-variation mixing time or a nonnegative pointwise return probability.

## Assumptions and scope

Let \(G=(V,E)\) be any finite simple undirected graph, \(|V|=k+1\), with a designated universal vertex \(o\). The \(k\) other vertices may have an arbitrary induced simple graph \(F\); no symmetry or regularity of \(F\) is required. In vertex order \(o,1,\ldots,k\), let \(L_G=D_G-A_G\), with unit edge weights. Write \(P_j=|j\rangle\langle j|\). The density matrix is the unique solution of the finite-dimensional Lindblad equation

\[
\dot\rho=-i[L_G,\rho]+\gamma\sum_{j\in V}\left(P_j\rho P_j-\frac12\{P_j,\rho\}\right),\quad \rho(0)=P_o,\quad \gamma>0.
\]

Equivalently, off-diagonal matrix entries decay at rate \(\gamma\) from the dissipator while diagonal entries are unaffected directly. The return probability is \(p_{k,\gamma}(t)=\langle o|\rho(t)|o\rangle\). With the maximally mixed invariant state, \(c_{k,\gamma}\) is also the stationary quantum-regression autocorrelation of \(P_o\), divided by its value at zero: specifically, its unnormalized covariance is \((p_{k,\gamma}(t)-1/(k+1))/(k+1)\). The theorem uses no absorbing sink, no extraction rate, no time-dependent noise, and no measurement of hitting times.

## Proof

**1. A leaf-graph-independent invariant operator space.** Set \(N=k+1\), and let \(J_k\) be the \(k\)-by-\(k\) all-ones matrix. Since any graph Laplacian has vanishing row and column sums,

\[
L_G=\begin{pmatrix}k&-\mathbf1^\top\\-\mathbf1&I_k+L_F\end{pmatrix},\qquad L_F\mathbf1=0,\quad\mathbf1^\top L_F=0.
\]

The real-linear space of Hermitian matrices of the form

\[
\rho=\begin{pmatrix}a&c\mathbf1^\top\\\bar c\mathbf1&bI_k+d(J_k-I_k)\end{pmatrix},
\quad a,b,d\in\mathbb R,\ c=u+iv,\ u,v\in\mathbb R,
\]

is invariant under the Hamiltonian commutator and the position-basis dephasing dissipator: the lower block \(bI_k+d(J_k-I_k)\) commutes with \(L_F\), while \(L_F\mathbf1=0\) annihilates the cross-block products. The dissipator merely multiplies each off-diagonal entry by \(-\gamma\). The initial state \(P_o\) belongs to this space. Uniqueness of the linear initial-value problem proves invariance for all \(t\), including equality of the *full* density matrices for all choices of \(F\) with the same \(k\).

Direct block multiplication gives

\[
\begin{aligned}
\dot a&=2kv,&\dot b&=-2v,&\dot d&=-2v-\gamma d,\\
\dot u&=(k-1)v-\gamma u,&
\dot v&=-(a-b)-(k-1)(u-d)-\gamma v.
\end{aligned}
\]

Because \(a+kb=1\), the normalized return contrast is \(x=a-b=(Na-1)/k=c_{k,\gamma}\). Define \(z=u-d\). Then the closed three-dimensional system is

\[
\frac{d}{dt}\begin{pmatrix}x\\z\\v\end{pmatrix}=
\underbrace{\begin{pmatrix}
0&0&2N\\0&-\gamma&N\\-1&-(k-1)&-\gamma
\end{pmatrix}}_{M_{k,\gamma}}
\begin{pmatrix}x\\z\\v\end{pmatrix},\qquad (x(0),z(0),v(0))=(1,0,0).
\]

**2. Laplace transform and absolute convergence.** Taking a Laplace transform of the three equations, eliminating \(z\) and \(v\), and using \(x(0)=1\) yields the rational expression displayed in the finding. Its denominator is the characteristic polynomial of the displayed matrix,

\[
D(s)=s^3+2\gamma s^2+\big(\gamma^2+N^2\big)s+2N\gamma.
\]

All roots lie in the open left half-plane: the cubic Routh–Hurwitz conditions hold because the coefficients are positive and

\[
(2\gamma)(\gamma^2+N^2)-2N\gamma=2\gamma(\gamma^2+N(N-1))>0.
\]

Thus the reduced matrix exponential decays exponentially for each fixed \(k\geq2\) and \(\gamma>0\). In particular, the defining time integral converges absolutely even if \(x(t)\) changes sign. Evaluating the Laplace transform at \(s=0\) gives

\[
T_k(\gamma)=\frac{\gamma^2+k^2-1}{2N\gamma}
=\frac{\gamma}{2N}+\frac{k-1}{2\gamma}.
\]

**3. Sharp global optimizer.** For \(k\geq2\), both summands are positive and tend to infinity at opposite endpoints of \((0,\infty)\). The derivative is

\[
\frac{dT_k}{d\gamma}=\frac{1}{2N}-\frac{k-1}{2\gamma^2},\qquad
\frac{d^2T_k}{d\gamma^2}=\frac{k-1}{\gamma^3}>0.
\]

Therefore exactly one minimizer exists, \(\gamma^2=N(k-1)=k^2-1\), and substitution yields the claimed minimum. The excluded \(k=1\) boundary instead gives \(T_1(\gamma)=\gamma/4\), with no interior minimizer.

**4. Uniform large-degree law.** For fixed \(\theta>0\), put \(\gamma=\theta k\). The roots of \(D\) split as \(r_0=-2\theta/(1+\theta^2)+O_\theta(k^{-1})\) and \(r_\pm=k(-\theta\pm i)+O_\theta(1)\). This follows by scaling \(s=kz\), where the leading cubic becomes \(z[(z+\theta)^2+1]\), which has three simple zeros; the bounded root is obtained from the order-\(k^2\) balance. In particular, the three roots are distinct for all sufficiently large \(k\). The residues of the rational Laplace transform at these roots satisfy \(A_0=1+O_\theta(k^{-1})\) and \(A_\pm=O_\theta(k^{-1})\). The latter claim follows from cancellation of the degree-\(k^2\) leading terms in the numerator \((r_\pm+\theta k)^2+k^2-1\), whereas the derivative of the denominator at each fast root has order \(k^2\). Consequently,

\[
x(t)=A_0e^{r_0t}+A_+e^{r_+t}+A_-e^{r_-t}.
\]

The fast terms are uniformly \(O_\theta(k^{-1})\) on \(t\geq0\). Since \(r_0\) stays bounded away from zero in the negative real direction, \(\sup_{t\geq0}|e^{r_0t}-e^{-2\theta t/(1+\theta^2)}|=O_\theta(k^{-1})\), proving the uniform assertion. Elementary differentiation proves the unique maximum of the limiting rate. This proof covers fixed \(\theta\in(0,\infty)\), not parameter sequences approaching zero or infinity with \(k\).

## Verification

`verify.py` provides a standalone numerical reconstruction of the full \((k+1)^2\)-dimensional Liouvillian from the graph Laplacian and the site projectors, with no invocation of the three-variable reduction in that reconstruction. It checks agreement with the reduced solution over multiple graph sizes, dephasing rates, leaf-edge sets, and time points; also checks density-matrix equality across distinct induced leaf graphs, trace and positivity, the zero-frequency resolvent, the optimizer and the large-degree exponential law. Run from the directory containing `verify.py` and `requirements.txt` with `python -m pip install -r requirements.txt` followed by `python verify.py`. A successful run prints `VERIFY_OK 970 direct full-Lindblad / resolvent / optimizer / scaling checks`. The all-graph and all-time assertions rest on the analytic proof, not these finitely many tests.

## Relationship to prior work

Razzoli, Bordone and Paris (2022) prove fully-connected-vertex universality for *unitary* Laplacian continuous-time quantum walks. The invariant density-operator reduction here is for a different, position-dephased Lindblad evolution and yields the specific zero-frequency return susceptibility. Bressanini, Benedetti and Paris (2022) investigate position-basis Haken–Strobl noise numerically on star and complete graphs and recognize a nonmonotone dependence of a *different* quantum-classical distance convergence metric on dephasing strength. Adithya L J and collaborators (initial preprint July 23, 2025) further examine noisy star/complete walks, observe coincidence for hub initialization, and study fitted coherence-relaxation times. Their numerical universality observations are antecedents, not new claims here. The exact integrated signed hub-return formula, its optimally tuned rate, extension to arbitrary induced leaf graphs, and uniform large-degree limit were not identified in these inspected texts. Luppi, Benedetti and Smirne (2025/2026) study a two-time Kolmogorov-consistency measure, including Haken–Strobl bounds on complete and cycle graphs, but do not optimize this fixed-hub signed autocorrelation. Boro (September 2026) examines noise-assisted *transport efficiency*, reporting numerical intermediate-rate optima for specific graph families, likewise not the signed universal-hub return functional. The integrated return here is not the sink capture probability, quantum-classical distance, or a worst-case mixing time used elsewhere.

## Limitations

The position basis, graph Laplacian (not adjacency-only Hamiltonian), equal independent site-dephasing rates, hub-localized initial state, and unit coherent hopping amplitude are essential assumptions. The optimizer minimizes a **signed integrated excess-return correlation**, not necessarily an operational mixing time, worst-case distance, coherence measure, or absorption time. For fixed finite \(k\) and \(\gamma>0\), the integral is absolutely convergent; the limit \(\gamma\downarrow0\) is not interchangeable with integration to infinite time. The exponential scaling statement assumes \(\gamma/k\to\theta>0\) with fixed finite \(\theta\). Previously known coherent universal-vertex behavior and previously observed noise nonmonotonicity are not claimed as new. Publication priority cannot be established from finite literature searches, and earlier implicit derivations from known low-dimensional reductions remain possible. No independent external scientific audit is claimed.

## References

1. Adithya L J, J. Nokkala, J. Piilo, and C. Meena, *Stability of Continuous Time Quantum Walks in Complex Networks*, arXiv:2507.17880, first submitted 2025-07-23, https://arxiv.org/abs/2507.17880 ; manuscript https://arxiv.org/pdf/2507.17880 .
2. G. Bressanini, C. Benedetti, and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, Quantum Information Processing 21, 317 (2022), DOI:10.1007/s11128-022-03647-x, https://link.springer.com/article/10.1007/s11128-022-03647-x .
3. L. Razzoli, P. Bordone, and M. G. A. Paris, *Universality of the fully connected vertex in Laplacian continuous-time quantum walk problems*, Journal of Physics A: Mathematical and Theoretical 55, 265303 (2022), DOI:10.1088/1751-8121/ac72d5; author manuscript https://arxiv.org/abs/2202.13824 .
4. P. Luppi, C. Benedetti and A. Smirne, *Temporal nonclassicality in continuous-time quantum walks*, arXiv:2512.18873, first public preprint 2025-12-21, https://arxiv.org/pdf/2512.18873 .
5. B. Boro, *Can Network Topology Control Quantum Transport Under Decoherence?*, preprint, 2026-09, DOI:10.5281/zenodo.22722869; accessible full-text copy https://www.researchgate.net/publication/414258583 .
