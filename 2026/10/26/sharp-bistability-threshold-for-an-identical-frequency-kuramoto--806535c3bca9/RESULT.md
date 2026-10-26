# Sharp bistability threshold for an identical-frequency Kuramoto ring with one weak bond

## Finding
For each integer \(N\ge5\), let \(m=N-1\) and let an \(N\)-cycle of identical Kuramoto oscillators have positive couplings \(1\) on \(m\) consecutive edges and \(w\) on the remaining edge. Set
\[
w_c(N)=\sin\frac{3\pi}{2m},\qquad f_m(\beta)=\frac{\sin((2\pi-\beta)/m)}{\sin\beta},\quad \frac\pi2<\beta<\pi.
\]
The function \(f_m\) has exactly one minimizer \(\beta_m\), and
\[
0<w_m:=f_m(\beta_m)<w_c(N)<1.
\]
Throughout the **complete weak-bond range** \(0<w\le w_c(N)\), exactly one linearly asymptotically stable equilibrium phase class (modulo uniform rotations) exists when \(0<w\le w_m\): synchrony. When \(w_m<w\le w_c(N)\), exactly three stable classes exist: synchrony and precisely two opposite unit-winding phase classes. For \(w_m<w<w_c(N)\), each nonsynchronous stable phase has \(m\) identical acute consecutive increments \(\alpha=(2\pi-\beta)/m\) and one obtuse weak-bond increment \(\beta\in(\pi/2,\beta_m)\), where \(f_m(\beta)=w\). At \(w=w_c(N)\) the weak phase is \(\pi/2\) and the state is still strictly linearly stable modulo rotation. The fold at \(w=w_m\) is degenerate and is *not* strictly linearly stable.

The exact finite-size critical value satisfies
\[
(N-1)w_m=\sec t_*+O((N-1)^{-2}),
\qquad \tan t_*=\pi+t_*,\quad 0<t_*<\frac\pi2,
\]
where \(\sec t_*=4.603338848751699\ldots\). The weak-bond interval hosting stable obtuse phases has positive width \(w_c-w_m=(3\pi/2-\sec t_*)/(N-1)+O((N-1)^{-3})\).

## Assumptions and scope
The equations in the common co-rotating frame are \(\dot\theta_i=\sum_{j\sim i}K_{ij}\sin(\theta_j-\theta_i)\), with phases in \(\mathbb R/(2\pi\mathbb Z)\), couplings \(K_{ij}=K_{ji}>0\), and \(N\ge5\) distinct vertices. Exactly one edge weight is \(w\), the other \(m\) edge weights are \(1\). The class of a state identifies simultaneous phase translation only; cyclic relocation of the singled-out edge is not additionally quotiented. An equilibrium is *strictly linearly stable modulo rotation* when its Jacobian has exactly one zero eigenvalue due to translation and all other eigenvalues are negative. Winding uses the principal increments in \((-\pi,\pi]\). Endpoint \(w=w_c\) is included; the fold point \(w=w_m\) is excluded from the two additional strictly stable classes. This theorem does not assert classification for \(w>w_c\).

## Proof
**1. Cycle-current constraint and stability signs.** Orient the cycle. At equilibrium the Kirchhoff balance at every vertex shows that all oriented currents are equal, say \(J\). Therefore every ordinary edge satisfies \(\sin\delta_i=J\), and the distinguished edge satisfies \(w\sin\delta_w=J\). The negative Jacobian is the weighted graph Laplacian with conductances \(\cos\delta_i\) on ordinary edges and \(w\cos\delta_w\) on the weak edge. Its quadratic form on edge differences is \(Q=\sum K_i\cos\delta_i\,d_i^2\), subject to \(\sum_i d_i=0\). A stable cycle cannot have two strictly negative conductances: choosing a difference vector supported on just those two edges gives \(Q<0\). More generally its strictly positive-conductance edges must form a connected spanning subgraph; two nonpositive conductances disconnect the positive subgraph and prevent positive definiteness. Every ordinary edge has nonzero conductance because \(|J|\le w\le w_c<1\).

Suppose exactly one ordinary edge is negative. The other ordinary edge conductances have the same positive value \(c=\sqrt{1-J^2}\); the weak conductance must be nonnegative. If it is positive, the positive path connecting the endpoints of the negative ordinary edge has resistance at least \((m-1)/c\), whereas that negative edge has magnitude \(c\). Taking differences \(-\sum d_i\) on the negative edge and otherwise aligned path differences shows stability would require \(1/c>(m-1)/c+1/(w\cos\delta_w)\), impossible for \(m\ge4\). If the weak conductance vanishes, the positive-edge subgraph omitting it and the negative ordinary edge is disconnected, also excluding strict stability. Hence every ordinary edge is acute (strictly positive cosine). Current constancy forces all their principal phase increments to be equal: \(\alpha=\arcsin J\in(-\pi/2,\pi/2)\). The weak increment is the only edge allowed to be obtuse.

**2. Winding exclusion.** Reverse the orientation if necessary so that \(J\ge0\). For \(J>0\), the weak increment \(\beta\) belongs to \((0,\pi)\), \(\alpha\in(0,\arcsin w_c]\), and the winding condition is \(m\alpha+\beta=2\pi q\) for an integer \(q\ge1\). At \(J=0\), all ordinary increments are zero; the weak increment is either zero or \(\pi\) modulo \(2\pi\), and the cycle consistency excludes the latter, leaving synchrony.

If \(q\ge2\), then \(m\alpha=2\pi q-\beta>3\pi\), so \(\alpha>3\pi/m\). When \(m\le6\), this contradicts \(\alpha<\pi/2\). When \(m\ge7\), monotonicity of sine on \((0,\pi/2)\) yields \(w\ge J=\sin\alpha>\sin(3\pi/m)>\sin(3\pi/(2m))=w_c\), also impossible. If \(q=1\) and \(\beta\le\pi/2\), one has \(m\alpha=2\pi-\beta\ge3\pi/2\), whence \(J=\sin\alpha\ge\sin(3\pi/(2m))=w_c\). Since \(J=w\sin\beta\le w\le w_c\), equality can occur only at the endpoint \(w=w_c\), \(\beta=\pi/2\). It follows that every nontrivial strictly stable state in the open range \(w<w_c\) has \(q=1\) and \(\beta>\pi/2\). Its negative-winding reflection accounts for the opposite state.

**3. Scalar branch and sharp stability criterion.** Write \(\alpha=(2\pi-\beta)/m\) and \(\beta\in(\pi/2,\pi)\). The current balance becomes \(w=f_m(\beta)\). Because each of the \(m\) ordinary conductances equals \(c=\cos\alpha>0\), elimination of the weak-edge difference yields
\[
Q=c\sum_{i=1}^{m}d_i^2+w\cos\beta\left(\sum_{i=1}^{m}d_i\right)^2.
\]
The Cauchy inequality shows this form is positive on nonconstant phase differences exactly when
\[
c+m w\cos\beta>0.
\]
Since \(\sin\alpha=w\sin\beta\), this is equivalent to \(\cot\alpha+m\cot\beta>0\). Direct differentiation gives
\[
\frac{f_m'(\beta)}{f_m(\beta)}=-\frac{\cot\alpha}{m}-\cot\beta,
\]
so a branch is strictly stable precisely on the **decreasing** portion of \(f_m\). Moreover
\[
\frac{d^2}{d\beta^2}\log f_m(\beta)=\csc^2\beta-\frac{1}{m^2}\csc^2\alpha>0,
\]
because \(m\sin\alpha\ge m\sin(\pi/m)>1\) for \(m\ge4\), while \(\sin\beta\le1\). Thus \(\log f_m\) is strictly convex. The logarithmic derivative is negative at \(\beta=\pi/2\) and diverges to \(+\infty\) as \(\beta\uparrow\pi\), so it crosses zero once at \(\beta_m\in(\pi/2,\pi)\). Consequently \(f_m\) has a unique nondegenerate minimum \(w_m<f_m(\pi/2)=w_c\). For every \(w_m<w<w_c\), the decreasing branch yields exactly one strictly stable positive-winding phase, the increasing branch a saddle. At \(w=w_m\) the branch has one additional zero Jacobian eigenvalue; at \(w=w_c\) its weak conductance is zero but its remaining positive edges form a connected path, so strict stability holds. Synchrony is always strictly stable since all physical couplings are positive. This completes the claimed exhaustive count.

**4. Sharp large-ring scale.** Uniformly over compact subsets of \((\pi/2,\pi)\),
\[
m f_m(\beta)=\frac{2\pi-\beta}{\sin\beta}+O(m^{-2}),
\]
and the unique minimizing points stay in a compact interior interval (the right endpoint diverges and the derivative at the left endpoint remains negative). Put \(\beta=\pi-t\). The limiting objective is \((\pi+t)/\sin t\), strictly minimized at the unique solution \(t_*\in(0,\pi/2)\) of \(\tan t_*=\pi+t_*\), since \(\tan t-t\) is strictly increasing from zero to infinity on that interval. At the minimum the objective equals \(\sec t_*\). Uniform smooth perturbation at a nondegenerate minimum gives \(m w_m=\sec t_*+O(m^{-2})\). Finally \(m w_c=3\pi/2+O(m^{-2})\), and \(3\pi/2>\sec t_*\) (for example the objective at \(t=2\pi/5\) is \((7\pi/5)/\sin(2\pi/5)<3\pi/2\)), establishing the stated positive interval width.

## Verification
Execute `python verify.py` in an environment with NumPy. The standalone script computes the scalar fold for every \(5\le N\le42\), reconstructs equilibrium currents and winding, assembles the full Jacobian-equivalent weighted cycle Laplacian, checks stable and unstable branches, the right endpoint, and the large-\(N\) constant. It prints `VERIFY_OK n_range=5..42 checks= 1447 constant= 4.603338848751704`. These are finite floating-point corroborations, not a substitute for the proof above. There is no exhaustive numerical enumeration of arbitrary equilibria.

## Relationship to prior work
The sine-current and winding-number framework, and the possibility of stable one-obtuse-edge configurations, were established in earlier Kuramoto-cycle work. Bronski, DeVille and Ferguson derive the signed-cycle stability criterion and analyze a different **uniform-weight, frequency-selected** long-edge optimization. Delabays, Coletta and Jacquod study single-loop winding and transition from short to one-long-link states under homogeneous edge capacities with nonuniform injections. Zelazo and Bürger give general effective-resistance definiteness criteria; later work on weighted topological states addresses general weighted winding-to-equilibrium correspondences. Those results motivate and substantially support the method but do not, in the inspected relevant sections, present the exact weak-bond onset parameter \(w_m\), its uniqueness and exhaustive stable-state count in the identical-frequency one-defect family, or the limiting \(\tan t_*=\pi+t_*\) threshold. The contribution is a **sharp specialized family classification**, not a new general graph-Laplacian stability theorem or a claim that one-obtuse-edge stability was previously unknown.

## Limitations
Only identical natural frequencies and a *single* edge-weight defect are treated, and the exhaustive classification is restricted to \(0<w\le w_c(N)\). Neutral and unstable equilibria are not exhaustively enumerated, and no basin estimates or global convergence rates are asserted. Strict linear asymptotic stability is always modulo the neutral uniform phase shift. Numerical eigenvalues have finite precision. Historical priority may be affected by unlocated equivalent single-defect calculations or a direct corollary stated in another source; no claim of independently certified priority is made.

## References
1. D. Zelazo and M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance*, arXiv:1408.2187 (first submitted 2014-08-10), https://arxiv.org/abs/1408.2187.
2. J. C. Bronski, L. DeVille and T. Ferguson, *Graph Homology and Stability of Coupled Oscillator Networks*, arXiv:1508.01507 (first submitted 2015-08-06), https://arxiv.org/abs/1508.01507.
3. R. Delabays, T. Coletta and P. Jacquod, *Multistability of Phase-Locking and Topological Winding Numbers in Locally Coupled Kuramoto Models on Single-Loop Networks*, arXiv:1512.04266 (first submitted 2015-12-14), https://arxiv.org/abs/1512.04266.
4. T. Ferguson, *Topological States in the Kuramoto Model*, arXiv:1704.02294 (first submitted 2017-04-07), https://arxiv.org/abs/1704.02294.
