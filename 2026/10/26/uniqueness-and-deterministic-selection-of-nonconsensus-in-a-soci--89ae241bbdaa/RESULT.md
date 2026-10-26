# Uniqueness and deterministic selection of nonconsensus in a social-pressure Pólya network

## Finding

Let \(W\) be the row-normalized weighted adjacency matrix of a finite connected undirected nonbipartite graph (self-loops permitted), with nonnegative symmetric edge weights and all weighted degrees positive. Given \(\gamma_i>0\), write \(\Gamma=\operatorname{diag}(\gamma_1,\ldots,\gamma_n)\ne I\) and
\[
 F_i(x)=f((Wx)_i,\gamma_i),\qquad
 f(s,\gamma)=\frac{\gamma s}{1+(\gamma-1)s},\qquad x\in[0,1]^n.
\]
Define \(r_0=\rho(\Gamma W)\) and \(r_1=\rho(\Gamma^{-1}W)\). Then:

**(i)** The entire fixed-point set consists of \(\mathbf0\), \(\mathbf1\), and at most one point \(x_*\in(0,1)^n\). Such \(x_*\) exists **if and only if** \(r_0>1\) and \(r_1>1\).

**(ii)** When it exists, \(x_*\) is the limit of the *auxiliary fixed-point iteration* \(x^{(k+1)}=F(x^{(k)})\) for **every** \(x^{(0)}\in(0,1)^n\). The iteration is a way to compute the equilibrium; it is **not** the expected time evolution of the urn process.

**(iii)** Under the strictly positive compatible initial counts stipulated in Tang–Adler–Ajorlou–Jadbabaie [1], their stochastic time-averaged declared-opinion vector \(\beta(t)\) converges almost surely to **the same deterministic vector** \(x_*\) whenever both spectral inequalities are strict. If \(r_0\le1\), then \(\beta(t)\to\mathbf0\) almost surely; if \(r_1\le1\), then \(\beta(t)\to\mathbf1\) almost surely. The two weak inequalities cannot hold simultaneously under these assumptions (already proved in [1]). Therefore these cases exhaust the parameter space.

The genuinely new component is the uniqueness of the interior equilibrium on arbitrary connected nonbipartite weighted networks and the resulting identification of the nonconsensus stochastic limit with one nonrandom vector. The endpoint tests, existence obstruction at their boundary, and convergence toward equilibria in [1] are prior results or closely follow them.

## Assumptions and scope

The number of agents is finite, \(n\ge2\). A positive entry \(W_{ij}\) means an active edge. The undirected support is connected and contains an odd cycle (where a self-loop is an odd cycle of length one). As in [1], no assumption is made that biases are all on the same side of one; neutral individual biases \(\gamma_i=1\) are allowed, but not every bias may be neutral. All fixed-point assertions concern the closed cube \([0,1]^n\).

The stochastic assertion uses *the specific independently sampled, synchronous, binary-declaration process and its compatible, strictly positive initial pseudo-counts* in [1, Sec. II]. It concerns the time average of past declarations, not the eventual constancy of individual declarations; individual declarations may continue changing indefinitely. We use the asymptotic assertions of [1, Theorems 3 and 4], not a new stochastic approximation theorem.

## Proof

**1. Boundary.** If \(x_i=0\) at a fixed point, then \(f((Wx)_i,\gamma_i)=0\) forces \((Wx)_i=0\). Nonnegativity forces every positive-weight neighbor to have value zero; connectivity propagates this to every vertex. The case \(x_i=1\) is analogous. Thus no nontrivial mixed-boundary fixed point is possible; this observation also appears in [1, Lemma 2].

**2. Necessity of the strict Perron inequalities.** Set \(o(s)=s/(1-s)\), strictly convex for \(0<s<1\). At an interior fixed point \(x\), the identity
\[
 o(x_i)=\gamma_i\,o((Wx)_i)
\]
and Jensen's inequality give the componentwise comparison
\[
 u\le\Gamma Wu,\qquad u_i=o(x_i)>0.
\]
For the positive left Perron vector \(\pi\) of \(\Gamma W\), one obtains \(r_0\ge1\). Equality would force equality in every row's Jensen inequality. Strict convexity implies all neighbors of each vertex have equal \(x\)-values. In a connected undirected nonbipartite graph, any two vertices can be joined by an even-length walk; equality along two successive edges then forces \(x_i\) to be constant. An interior constant \(x\) solves \(x_i=f(x_i,\gamma_i)\) only if all \(\gamma_i=1\), excluded here. Thus \(r_0>1\). Apply the same argument to \(\mathbf1-x\), using \(1-f(s,\gamma)=f(1-s,\gamma^{-1})\), to get \(r_1>1\). This necessity and the equality obstruction are consistent with the established boundary proof in [1, Theorem 4].

**3. Existence and constructive attraction.** Assume both spectral radii exceed one. Let \(a,b>0\) be right Perron vectors of \(\Gamma W\) and \(\Gamma^{-1}W\). By differentiability of \(F\) at \(\mathbf0\),
\[
 F(\varepsilon a)=\varepsilon r_0 a+O(\varepsilon^2),
\]
so \(F(\varepsilon a)>\varepsilon a\) componentwise for sufficiently small \(\varepsilon>0\). Complement symmetry gives \(F(\mathbf1-\varepsilon b)<\mathbf1-\varepsilon b\). Choose \(\varepsilon\) such that
\(\mathbf0<\ell=\varepsilon a< h=\mathbf1-\varepsilon b<\mathbf1\).
The map \(F\) is continuous and coordinatewise nondecreasing. Therefore the iterates from \(\ell\) increase, the iterates from \(h\) decrease, and both converge to fixed points strictly inside \((0,1)^n\). Uniqueness in step 4 implies their limits coincide. Any strictly interior initial state is sandwiched between such barriers after choosing \(\varepsilon\) sufficiently small; order preservation proves the global convergence claimed in (ii).

**4. Interior uniqueness (critical step).** Suppose distinct interior fixed points \(x,y\) exist. Possibly interchange them so that
\[
 R=\max_i\frac{o(x_i)}{o(y_i)}>1.
\]
Define \(T_R(s)=Rs/[1+(R-1)s]\). It is strictly increasing and **strictly concave** on \((0,1)\), with \(o(T_R(s))=R\,o(s)\). The choice of \(R\) says \(x_j\le T_R(y_j)\) for every vertex. Consequently, for every vertex \(i\),
\[
 (Wx)_i\le\sum_jW_{ij}T_R(y_j)
 \le T_R\!\left(\sum_j W_{ij}y_j\right).
\]
The second inequality is Jensen's inequality. At a maximizing vertex \(i\), the fixed-point odds identity gives
\[
 \frac{o((Wx)_i)}{o((Wy)_i)}
 =\frac{o(x_i)}{o(y_i)}=R,
\]
so \((Wx)_i=T_R((Wy)_i)\). Hence **both** displayed inequalities are equalities. The first equality forces every positive-weight neighbor \(j\) of \(i\) also to attain the maximal ratio \(R\). The strict Jensen equality forces all their \(y_j\)-values to agree. By connectivity, propagation of maximality makes every vertex a maximizing vertex; strict Jensen equality then holds at every vertex. Hence \(y_j\) is constant along every even-length walk, and nonbipartiteness implies \(y\) is constant on the graph. But a strictly interior constant fixed point would force \(\gamma_i=1\) for every \(i\), contradiction. This proves uniqueness without assuming that interior equilibria are comparable in coordinate order.

**5. Almost-sure selection.** Theorem 3 of [1] establishes that the stochastic \(\beta(t)\) approaches the closed equilibrium set almost surely. Theorem 4 of [1] proves that an endpoint has probability zero of being the limit when its linearization has Perron radius greater than one. The endpoint Jacobians are \(\Gamma W\) and \(\Gamma^{-1}W\), respectively. By steps 1–4, the equilibrium set in the strict–strict case is precisely \(\{\mathbf0,x_*,\mathbf1\}\). For completeness, approach to a finite set and increments tending to zero imply convergence to one of its elements: take disjoint neighborhoods of these three points, note that eventually every iterate is in their union and every step is smaller than the separation needed to switch neighborhoods; then shrink the neighborhood radii to zero. Since the stochastic urn step satisfies \(\|\beta(t+1)-\beta(t)\|_\infty\le1/(t+1)\), this argument applies. Theorem 4 eliminates both endpoints almost surely, leaving \(x_*\). If either Perron radius is at most one, [1, Theorem 4] already yields the stated endpoint limit. This proves (iii).

## Verification

The included `verify.py` uses only Python's standard-library exact fractions. It checks the explicit three-agent nonconsensus witness below, both strict positive Perron *sub-eigenvector certificates*, the complement symmetry, and several algebraic consequences. The proof above—not these finite checks—establishes the all-network theorem.

Take the loop-free triangle \(W_{ij}=1/2\) when \(i\ne j\), \(W_{ii}=0\), with \(\gamma=(5,1/5,1)\). Direct evaluation gives the exact interior equilibrium
\[
 x_*=(3/4,\,1/4,\,1/2),\qquad Wx_*=(3/8,\,5/8,\,1/2).
\]
For \(a=(4,1/5,3/2)\), the vector \(\Gamma Wa-a=(1/4,7/20,3/5)\) has strictly positive entries. Swapping the first two coordinates yields a corresponding strictly positive certificate for \(\Gamma^{-1}W\). Collatz–Wielandt therefore verifies both spectral radii are strictly above one without floating-point eigenvalues. All three biases are admissible, including one neutral agent.

To reproduce: `python3 verify.py`. A successful execution prints `PASS: exact rational witness and spectral certificates`. No external package is required.

## Relationship to prior work

Tang, Adler, Ajorlou and Jadbabaie [1] derive the same model map, identify boundary equilibria, show almost-sure approach to the equilibrium **set**, and establish both spectral conditions for endpoint consensus. Their original and subsequently available preprint versions explicitly leave the isolation and uniqueness of interior equilibria on arbitrary networks open (Section V and the discussion following Theorem 3). The strict Perron obstruction in proof step 2 closely parallels their Theorem 4 and is **not** separately claimed as new. Their later work [2] studies estimators for agents' inherent beliefs and bias parameters, and discusses trajectories approaching interior equilibria; it does not state the all-network uniqueness proved in step 4. The original model [3] works mainly on complete graphs. General order-preserving nonlinear-map convergence frameworks such as [4] are broader in another direction, but neither formulate this exact graph-and-bias equilibrium classification nor identify the stochastic Pólya process's nonrandom limit.

## Limitations

The support must be connected and nonbipartite and the bias matrix must not equal the identity. The theorem does not claim uniqueness for arbitrary disconnected or bipartite supports, nor does it supply a rate of stochastic convergence, concentration inequalities, or outcomes for changing networks or other declaration kernels. The spectral existence criterion partly consolidates known boundary-obstruction results; the principal new result is uniqueness and deterministic selection in the nonconsensus regime. A broader theorem of nonlinear monotone dynamics might furnish a different proof of uniqueness, and publication priority beyond the inspected sources has not been independently certified. No independent scientific audit has been carried out.

## References

[1] Jennifer Tang, Aviv Adler, Amir Ajorlou, and Ali Jadbabaie, *Stochastic Opinion Dynamics under Social Pressure in Arbitrary Networks*, arXiv:2308.09275 (first public 2023-08-18); freely available PDF: https://arxiv.org/pdf/2308.09275.

[2] Jennifer Tang, Aviv Adler, Amir Ajorlou, and Ali Jadbabaie, *Estimating True Beliefs in Opinion Dynamics with Social Pressure*, arXiv:2310.17171 (first public 2023-10-26), https://arxiv.org/pdf/2310.17171.

[3] Ali Jadbabaie, Anuran Makur, Elchanan Mossel, and Rabih Salhab, *Inference in Opinion Dynamics under Social Pressure*, arXiv:2104.11172 (first public 2021-04), https://arxiv.org/pdf/2104.11172.

[4] Brian Lins, *Convergence of Iterates in Nonlinear Perron–Frobenius Theory*, arXiv:2207.14098 (first public 2022-07), https://arxiv.org/pdf/2207.14098.
