# Two-cluster bifurcation and the universal mobility-two degeneracy in complete-graph chemotaxis

## Finding
For the exponential-preference logistic Keller–Segel ODE on any complete graph with \(N\ge3\) equally weighted vertices, the local nonuniform equilibrium branches lying in any **fixed two-cluster partition** admit a sharp classification. Let the first cluster have \(p\) vertices, the second \(q=N-p\), and write \(a=p/N\), \(b=q/N\). Set \(d=\eta_n/r>0\), \(\tau=\chi\alpha K/[2(\beta+\eta_c/2)]\) and \(\tau_*=1/2+1/d\). The normalized population gap is \(z=(n_H-n_L)/K\), and \(\delta=\tau-\tau_*\). There is a fixed neighborhood of the homogeneous positive equilibrium and a sufficiently small parameter interval where all equilibria in this two-cluster subspace are the homogeneous state and exactly the following nonuniform branches:

1. If \(a\ne1/2\) and \(d\ne2\), for each \(0<|\delta|\) sufficiently small there is exactly one nonzero branch, crossing the homogeneous branch with \(z=-4d\delta/[(1-2a)(d-2)]+O(\delta^2)\). No nonzero equilibrium occurs at \(\delta=0\) inside the chosen neighborhood.
2. If \(d=2\), for **every** partition \(1\le p<N\), exactly two nonzero branches exist for small \(\delta>0\), with \(z_\pm=\pm\sqrt{3\delta}+O(\delta)\); none exists for sufficiently small \(\delta\le0\). The leading square-root coefficient is independent of \(N,p,q\).
3. If \(a=1/2\), for **every** \(d>0\), exactly two nonzero branches exist for small \(\delta>0\), with \(z_\pm=\pm\sqrt{6d^3\delta/(d^3+3d+2)}+O(\delta)\); none exists for sufficiently small \(\delta\le0\). At \(d=2\) this agrees with item 2.

These are local equilibrium counts **inside the specified two-cluster invariant subspace**, not a census of all nearby equilibria of the full \(2N\)-dimensional ODE or a claim about dynamical stability.

## Assumptions and scope
Let \(N\ge3\), \(A_{ij}=1\) for \(i\ne j\), \(A_{ii}=0\), and choose \(r,K,\eta_n,\eta_c,\alpha,\beta>0\) and \(\chi\ge0\). The governing equations are
\[
\dot n_i=\frac{\eta_n}{N}\sum_{j\ne i}\frac{e^{\chi c_i}n_j-e^{\chi c_j}n_i}{e^{\chi c_i}+e^{\chi c_j}}+r n_i(1-n_i/K),\qquad
\dot c_i=\frac{\eta_c}{2N}\sum_{j\ne i}(c_j-c_i)+\alpha n_i-\beta c_i.
\]
The two-cluster subspace is the fixed set of permutations separately within the first \(p\) vertices and within the remaining \(q=N-p\). Its populations are \(n_H=K h\) and \(n_L=K\ell\); the labels \(H,L\) merely distinguish clusters and do not impose an ordering on their densities. The homogeneous positive equilibrium is \(n_i=K\), \(c_i=\alpha K/\beta\). Parameters except \(\chi\) are fixed during each local bifurcation. In the special regime \(d=2\) the mobility equality is imposed exactly, not as a uniform two-parameter normal-form statement.

## Proof
**Stationary reduction.** All within-cluster movements cancel. The two chemical equilibrium equations yield, for \(s=a h+b\ell\) and \(z=h-\ell\),
\[
 c_H=\frac{\alpha K}{\beta}s+\frac{\alpha K b}{\beta+\eta_c/2}z,\qquad
 c_L=\frac{\alpha K}{\beta}s-\frac{\alpha K a}{\beta+\eta_c/2}z.
\]
Thus \(\tanh(\chi(c_H-c_L)/2)=\tanh(\tau z)\). Summing the two population equilibrium equations with multiplicity weights gives the **exact** logistic mass identity \(s(1-s)=ab z^2\). Every stationary state close to the positive homogeneous state therefore has
\[
 s(z)=\frac{1+\sqrt{1-4ab z^2}}2,\qquad h(z)=s(z)+bz,\qquad\ell(z)=s(z)-az.
\]
There is another formal root of the mass quadratic near zero population, but it is not in this neighborhood. For sufficiently small \(|z|\), both densities and both chemical levels are positive. Direct reduction of the first cluster's population balance gives \(zB(z,\tau)=0\), where the removable singularity at \(z=0\) is filled analytically in
\[
 B(z,\tau)=\frac{h(z)(1-h(z))}{z}+bd\left[-\frac12+\frac{h(z)+\ell(z)}{2z}\tanh(\tau z)\right].
\]
The second cluster's population equation follows automatically from the mass identity and antisymmetry of the transfer flux, so the reduction is an **equivalence**, not merely a necessary condition.

**Critical Taylor coefficients.** Expansion at \(z=0\) gives the exact identity \(B(0,\tau)=bd(\tau-\tau_*)\). At the critical parameter,
\[
 \partial_zB(0,\tau_*)=\frac{b(1-2a)(d-2)}4.
\]
If \(d=2\), then \(\tau_*=1\), \(\partial_z B(0,1)=0\), and
\[
 \tfrac12\partial_z^2 B(0,1)=-\frac{2b}{3}<0.
\]
For the balanced case \(a=b=1/2\), one has exactly \(B(-z,\tau)=B(z,\tau)\), and
\[
 \tfrac12\partial_z^2 B(0,\tau_*)=-\frac{d^3+3d+2}{12d^2}<0.
\]
These identities are obtained by ordinary Taylor expansion of the displayed explicit analytic function; the companion checker verifies them symbolically without numerical fitting.

**Counting roots and deriving the coefficients.** For \(a\ne1/2\), \(d\ne2\), the nonzero linear coefficient permits the analytic implicit-function theorem to solve \(B=0\) uniquely as a graph \(z=z(\delta)\); the derivative is the claimed \(-4d/[(1-2a)(d-2)]\). In the mobility-two case, \(B\) has a strictly negative second \(z\)-derivative throughout a sufficiently small rectangle around \((z,\delta)=(0,0)\). Its unique nearby critical point is a strict maximum; the maximum value is \(2b\delta+O(\delta^2)\). It is strictly positive for small \(\delta>0\), zero at the critical point only when \(\delta=0\), and negative for small \(\delta<0\). Strict concavity and continuity of the boundary signs give exactly two roots for \(\delta>0\), none otherwise. Substitution \(z=\sqrt\delta u\) shows \(u_\pm\to\pm\sqrt3\); a smooth analytic blow-up in \((u,\sqrt\delta)\) improves the remainder to \(O(\delta)\).

In the balanced case \(B\) is analytic and even in \(z\), so it is an analytic function of \(w=z^2\). Its derivative with respect to \(w\) at \((w,\delta)=(0,0)\) is strictly negative as displayed. The implicit-function theorem uniquely gives \(w(\delta)=6d^3\delta/(d^3+3d+2)+O(\delta^2)\). The admissible \(w>0\) yields exactly the stated symmetric pair of gaps for positive \(\delta\), and none for nonpositive \(\delta\). The choices of neighborhoods and parameter intervals may depend on the fixed partition and coefficients.

## Verification
Run `python check_two_cluster.py` with SymPy and SciPy installed. The script reconstructs the scalar reduction, checks its first three Taylor coefficients by exact symbolic algebra, and independently substitutes numerically found roots into **every original population and chemical equilibrium equation** for complete graphs with three and four vertices, for both generic and degenerate regimes. The full-ODE residual tolerance in the sampled tests is \(2\times10^{-10}\). All five test groups passed on the packaged files. Numerical root counts on finitely many graphs are consistency checks, **not** the proof of local uniqueness for arbitrary \(N\). The local uniqueness conclusions rest on the analytic reduction, the implicit-function theorem, and strict concavity.

## Relationship to prior work
Kim, Zhang, Zhao and Cooney formulated these exact biased edge-transition equations, determined homogeneous linear-instability thresholds on finite graphs, simulated patterned states, and analyzed selected simple-mode bifurcations in the graphon limit. Their preprint expressly notes that the complete graphon has simultaneously critical modes and cannot be treated by their single-mode weakly nonlinear analysis. The result above builds on their model and critical linear threshold, but adds the complete local **fixed-partition finite-clique equilibrium branch classification** and the exceptional mobility ratio \(\eta_n/r=2\), where unbalanced partitions change from a transcritical-looking crossing to square-root onset. The separate two-patch nonlinear equilibrium classification does not imply the \(p\ne q\) branches possible only for \(N\ge3\). Shemtaga, Shen and Sukhtaiev study related **metric-graph partial differential equations** with continuous densities along edges and a different taxis law; those bifurcations are not the finite-node exponential preference equations treated here.

## Limitations
The theorem is local at the homogeneous positive equilibrium and fixes a chosen two-cluster partition. It does **not** classify fully asymmetric equilibria, stability/attraction of new states, far-from-threshold branches, all graph topologies, or simultaneous variation of \(d\) and \(\tau\). The other solution of the mass quadratic and more distant patterned equilibria may exist outside the specified local neighborhood. Mathematical correctness relies on the analytic proof; neither the symbolic checker nor a literature search constitutes an independent mathematical audit. Historical-priority uncertainty remains regarding other nonlinear equivariant bifurcation analyses, although no covering result was found in the checked sources.

## References
1. Daecheol Kim, Yefei Zhang, Yuxuan Zhao, Daniel B. Cooney, *The Keller–Segel Model for Chemotaxis on Metapopulation Graphs and Graphons*, arXiv:2610.31049v1, first posted 2026-10-22. https://arxiv.org/html/2610.31049v1. Particularly equations (2.2)–(2.3), §3, §5 Remark 5.5, and §5.2.
2. Hewan Shemtaga, Wenxian Shen, Selim Sukhtaiev, *Stability and bifurcation for logistic Keller–Segel models on compact graphs*, arXiv:2310.00756v1, first posted 2023-10-01. https://arxiv.org/abs/2310.00756.
