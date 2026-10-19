# A sharp vanishing-tie consensus transition in a friend-of-friend social network

## Finding

**Theorem (complete homogeneous-response classification).** Fix an integer \(N\ge2\). In the symmetric friend-of-friend (FOAF) adaptive-network opinion model of Nugent, Gomes and Wolfram, set the interaction function to the constant \(\phi(r)\equiv c\), where \(0<c<1\). Let each diagonal social weight be one, let every off-diagonal initial weight be in \([0,1]\), and let initial opinions lie in \([-1,1]\). The initial positive-weight edges define an undirected graph \(G_0\). Write
\[
c_*(N)=\frac{N}{2(N+1)}.
\]
For every initial condition, the following classification holds **separately on every connected component of \(G_0\)**.

1. **Subcritical, \(0<c<c_*(N)\).** Every off-diagonal edge weight decays exponentially, and every opinion converges. Within each original connected component, the limiting opinions are all equal **if and only if** the initial opinions on that component were already all equal. Thus a positive constant propensity to interact does not ensure consensus when the coupled ties die too quickly.
2. **Critical, \(c=c_*(N)\).** Every off-diagonal weight tends to zero. Every pair of distinct vertices in the same original connected component has weight \(\Theta((1+t)^{-1})\), including pairs whose edge was initially absent. Nevertheless, all opinions in each original connected component converge to a common limit, at least at a polynomial rate. Links between different original components remain identically zero.
3. **Supercritical, \(c>c_*(N)\).** Every pair of distinct vertices in the same original connected component has eventually a weight bounded below by a positive constant; opinions in each component converge exponentially to consensus. No links form between different original components.

The threshold is sharp for every \(N\ge2\), and is **not** the logistic-edge threshold \(1/2\). At the critical point of a two-agent connected system, edge decay and opinion relaxation are both exactly inverse-linear in time.

## Assumptions and scope

Let \(W(t)=(w_{ij}(t))_{i,j=1}^N\) be symmetric. We impose \(w_{ii}(t)=1\), \(0\le w_{ij}(0)\le1\) for \(i\ne j\), and \(x_i(0)\in[-1,1]\). Set \(k_i(t)=\sum_jw_{ij}(t)\), so \(k_i(t)\ge1\). The system is exactly the constant-interaction specialization of the source's opinion equation (8a) and FOAF edge equation (14):
\[
\dot x_i=\frac{c}{k_i}\sum_{j\ne i}w_{ij}(x_j-x_i),\qquad
\dot w_{ij}=c\left(w_{ij}+\frac{(W^2)_{ij}}{N}\right)(1-w_{ij})-(1-c)w_{ij}\quad(i\ne j).
\]
The diagonal weights do not evolve. Here \((W^2)_{ij}=\sum_{\ell=1}^Nw_{i\ell}w_{\ell j}\). The model is deterministic, continuously weighted, and finite-dimensional. A connected component means a component of the positive-support graph at **time zero**, not a graph formed by thresholding later weights. An initially isolated singleton is trivially at consensus; no statement requires different initial components to agree.

## Proof

**1. Invariance and component separation.** The polynomial weight field preserves symmetry, the interval \([0,1]\), and the unit diagonal: at zero the off-diagonal derivative is nonnegative, and at one it is negative. The opinion system is a cooperative averaging flow, so the initial opinion convex hull is invariant. If two groups have zero weights between them initially, then the cross-block entries of \(W^2\) are also zero. Uniqueness preserves these zeros. Thus distinct connected components of \(G_0\) never interact. Conversely, a positive edge stays positive at every finite time because its derivative is at least a bounded negative multiple of itself. If two vertices are connected by an initial path, the FOAF source \(\sum_{\ell\ne i,j}w_{i\ell}w_{\ell j}\) becomes positive, successively, along paths of length two, three, and so on. Iterating the positive-source integral formula shows that **every pair in one original component has positive weight at every time \(t>0\)**. This statement concerns finite times, not a positive limiting weight.

**2. Two exact comparison inequalities.** Put
\[
A_N=1+\frac2N,\qquad B_N=\frac{N-2}{N},\qquad r_N(c)=c\left(2+\frac2N\right)-1.
\]
For \(i\ne j\), let \(z=w_{ij}\) and \(S_{ij}=\sum_{\ell\ne i,j}w_{i\ell}w_{\ell j}\ge0\). Because the diagonal entries are one, \((W^2)_{ij}=2z+S_{ij}\). Hence the **exact** edge equation is
\[
\dot z=r_N(c)z-cA_Nz^2+\frac{c}{N}S_{ij}(1-z),
\]
and in particular
\[
\dot w_{ij}\ge r_N(c)w_{ij}-cA_Nw_{ij}^2. \tag{1}
\]
Let \(m(t)=\max_{i<j}w_{ij}(t)\). At any maximizing edge, \(S_{ij}\le(N-2)m^2\). Therefore its upper right Dini derivative obeys
\[
D^+m\le r_N(c)m-\frac{4c}{N}m^2-cB_Nm^3. \tag{2}
\]
The sign of \(r_N(c)\) changes exactly at \(c_*(N)=N/[2(N+1)]\). All comparisons below use the actual complete \(N\)-vertex normalization, even when an original connected component is smaller.

**3. Subcritical ties have finite total influence.** If \(r_N(c)<0\), (2) implies \(m(t)\le m(0)e^{r_N(c)t}\). The opinion evolution is \(\dot x=Q(t)x\), with nonnegative off-diagonal entries \(Q_{ij}(t)=c w_{ij}(t)/k_i(t)\), row sums zero, and \(\int_0^\infty\lVert Q(t)\rVert\,dt<\infty\). The fundamental matrix \(U(t,0)\) is row-stochastic and converges to \(U_\infty\), because \(\dot U=QU\) is integrable. Liouville's determinant identity gives
\[
\det U_\infty=\exp\left(\int_0^\infty\operatorname{tr}Q(t)\,dt\right)>0.
\]
Thus \(U_\infty\) is invertible. It is block diagonal on initial components and maps each component's constant vector to itself. Hence a vector of limit opinions is constant on a component precisely when its initial restriction is constant there: invertibility precludes collapse of any nonconstant opinion profile to a common value. This establishes the asserted **if and only if**, not merely a counterexample.

**4. Critical weights vanish, but their total influence diverges.** If \(r_N(c)=0\) and \(m(0)>0\), (2) implies
\[
m(t)\le\frac{m(0)}{1+4cm(0)t/N}.
\]
For each edge with \(w_{ij}(t_0)>0\), (1) gives, for \(t\ge t_0\),
\[
w_{ij}(t)\ge\frac{w_{ij}(t_0)}{1+cA_Nw_{ij}(t_0)(t-t_0)}.
\]
By step 1, every within-component pair admits \(t_0>0\) with positive weight. The upper and lower bounds therefore prove \(w_{ij}(t)=\Theta(t^{-1})\) for every such pair; between components weights are always zero. Now change time by \(s=\log(1+t)\). The rescaled opinion generator is \(\widetilde Q(s)=(1+t)Q(t)\). Its off-diagonal rates are uniformly bounded above, since \((1+t)m(t)\) is bounded; along every edge of the original component they are eventually bounded below by a **uniform positive** number, because \(k_i\le N\) and the preceding inverse-linear lower bound holds. Thus, for every component and every sufficiently late unit interval of \(s\)-time, the transition matrix has each entry bounded below by the same \(\varepsilon>0\). Indeed, for any ordered pair of vertices take an original graph path of length at most \(N-1\), and lower-bound the event of taking those jumps in order while making no other jump; bounded total exit rates give a positive lower bound depending only on the component and the rate bounds. The resulting stochastic-matrix contraction reduces the opinion diameter by a fixed factor on each such unit interval. Hence the diameter tends to zero exponentially in \(s\), i.e. polynomially in \(1+t\). Monotonicity of maximum and minimum opinions establishes convergence of every opinion to one shared limit within each component.

**5. Supercritical persistence and consensus.** If \(r_N(c)>0\), inequality (1) compares any positive edge with the logistic equation \(\dot y=r_N(c)y-cA_Ny^2\). Consequently,
\[
\liminf_{t\to\infty}w_{ij}(t)\ge\frac{r_N(c)}{cA_N}>0
\]
for every edge already positive at a finite time. By step 1 this applies to every pair within each original component. The opinion generator therefore has all within-component off-diagonal rates eventually bounded below by a positive number, so the same pathwise stochastic-matrix contraction, now in ordinary time, gives exponential consensus. Distinct components remain dynamically independent.

**6. Exact two-agent critical illustration.** For \(N=2\) and \(c=c_*(2)=1/3\), writing \(w=w_{12}\) and \(d=x_2-x_1\), one obtains
\[
w(t)=\frac{w_0}{1+\frac23w_0t},\qquad
d(t)=\frac{d_0}{1+\frac{2w_0}{3(1+w_0)}t}.
\]
Thus \(w(t)\to0\) while \(d(t)\to0\) at the same critical inverse-linear order whenever \(w_0>0\). This calculation is illustrative, not a substitute for the all-\(N\) proof.

## Verification

The standalone file `verify_foaf_threshold.py` reproduces the edge identity, comparison bounds, and the location of the critical parameter by exact rational arithmetic for several finite system sizes and sampled symmetric matrices. It executes **10,080 exact rational comparisons**. It additionally integrates the full coupled ODE in **nine** independently constructed numerical examples, including the two-agent exact critical solution. The program requires Python 3, and optionally NumPy and SciPy for the ODE integrations. Execute `python verify_foaf_threshold.py` after extracting this file. The mathematical proof, including all infinite-time claims and all-population quantifiers, is analytic and does not rely on these finite checks.

## Relationship to prior work

Nugent, Gomes and Wolfram [1] introduced the continuous-time coevolving model, including exactly the FOAF term \((W^2)_{ij}/N\), and analyzed social polarization and consensus via numerical case studies and other conditions. Their general setup supplies the present system; the new result is the **complete, exact constant-response FOAF phase classification**, not the model itself. Their stated FOAF experiments use bounded-confidence or exponentially distance-dependent responses rather than the present constant-response threshold theorem.

Nugent, Calatayud Fernandez and Gomes [2] establish qualitative clustering statements for positive-response adaptive networks and discuss FOAF. Their theorem that cross-cluster weights vanish does **not** give a critical interaction constant, an all-edges-extinct-yet-consensual regime, or a guarantee of nonconsensus for every initially nonconstant component below threshold. They mainly provide explicit consensus guarantees for different edge dynamics. Their FOAF commentary involving \(\phi(0)=1\) does not subsume the \(0<c<1\) specialization here.

Martin and Girard [3] and Hendrickx and Tsitsiklis [4] provide general persistent-connectivity and cut-balance consensus criteria. These can supply an alternative **second step** to deduce consensus from the present critical inverse-linear weight bounds, but do not establish the **model-specific threshold, exact tie bounds, and subcritical invertibility obstruction**. The distinction between an existing general convergence criterion and its sharp verification in a new nonlinear coevolving network is essential to the claim's scope.

## Limitations

This theorem concerns **constant positive response**, symmetric weights, unit self-loops, the FOAF mechanism exactly as printed in [1], and deterministic finite populations. It does not establish equivalent cutoffs for distance-dependent response, asymmetric initial networks, stochastic tie evolution, or alternative normalization of the FOAF term. The consensus value need not equal the unweighted initial mean because the instantaneous row-normalized generator need not be column-balanced. It gives polynomial convergence at criticality without claiming an optimal exponent for general graphs. A general consensus theorem proves the final convergence when its hypotheses apply, but the new proof identifies exactly when those hypotheses arise in this specific FOAF system. Independent publication-priority verification remains outstanding, including comparison with a related doctoral thesis whose full text was not accessible.

## References

[1] A. J. Nugent, S. N. Gomes and M.-T. Wolfram, *On evolving network models and their influence on opinion formation*, arXiv:2305.09483v1 (first public version 2023-05-16), https://arxiv.org/abs/2305.09483 . FOAF equations (13)–(14), model equation (8), and Sections 3–4.

[2] A. J. Nugent, C. Calatayud Fernandez and S. N. Gomes, *Emergent structures in coupled opinion and network dynamics*, arXiv:2602.03738v1, https://arxiv.org/abs/2602.03738 . Section 3, Theorem 3.1 and FOAF discussion.

[3] S. Martin and A. Girard, *Continuous-time consensus under persistent connectivity and slow divergence of reciprocal interaction weights*, arXiv:1105.2755, https://arxiv.org/abs/1105.2755 .

[4] J. M. Hendrickx and J. N. Tsitsiklis, *A new condition for convergence in continuous-time consensus seeking systems*, IEEE CDC 2011, DOI:10.1109/CDC.2011.6160231, https://doi.org/10.1109/CDC.2011.6160231 .
