# Gaussian jamming fluctuations on complete split graphs

## Finding

Let \(0<\alpha<1\) be fixed. For each integer \(N\), form the complete split graph on \(N\) vertices: an independent set of size \(A_N=\lfloor\alpha N\rfloor\), a clique of size \(B_N=N-A_N\), and every edge between the two sets. Assign independent continuous identically distributed priorities to all graph edges. Process edges in increasing priority order and accept a dimer precisely when both endpoints are unoccupied. Write \(U_N\) for the total number of unoccupied vertices after no further deposition is possible.

Put
\[
L=\frac{1-\alpha}{\alpha},\qquad
r=\alpha e^{-L},\qquad
v=r\left[4-(L+2)^2e^{-L}\right].
\]
Then \(r>0\), \(v>0\), and
\[
\frac{U_N}{N}\xrightarrow{\mathbb P}r,\qquad
\sqrt N\left(\frac{U_N}{N}-r\right)
\xrightarrow{\mathrm d}\mathcal N(0,v).
\]
Also \(\mathbb E[U_N/N]\to r\). At \(\alpha=1/2\), the limiting unmatched fraction is \(1/(2e)\) and the Gaussian variance constant is \(\tfrac{1}{2e}[4-9/e]=0.126750107778\ldots\). Yet for even \(N\) with \(A_N\le B_N\), this graph admits a perfect matching. Thus the macroscopic vacancies are a kinetic jamming effect, not an obstruction to the existence of perfect matchings.

## Assumptions and scope

The graph is finite and simple, with every independent-set-to-clique edge and every clique internal edge present; there are no edges within the independent set. The priority law is arbitrary continuous i.i.d.; ties therefore have probability zero. The limit holds for each fixed \(\alpha\in(0,1)\), not uniformly in sequences approaching the endpoints. The normalized count \(U_N/N\) includes vacant vertices of both types. The variance \(v\) is the asymptotic variance of \(\sqrt N(U_N/N-r)\), not the variance per initially occupied particle.

## Proof

**Exact stochastic representation.** Assign independent exponential clocks of rate \(1/N\) to all allowed edges. Their order is a uniform permutation, so they reproduce the priority process exactly. Let \(A(t)\) and \(B(t)\) count vacant independent-set and vacant clique vertices. Conditional on the counts, there are \(AB\) acceptable cross-edges and \(\binom B2\) acceptable clique edges. Thus the only jumps and their rates are
\[
(A,B)\mapsto(A-1,B-1)\text{ at rate }AB/N,
\qquad
(A,B)\mapsto(A,B-2)\text{ at rate }B(B-1)/(2N).
\]
Write \(a=A/N\), \(b=B/N\). For smooth functions the scaled generator is
\[
(\mathcal L_N f)(a,b)=Nab\left[f(a-N^{-1},b-N^{-1})-f(a,b)\right]
+\frac N2b(b-N^{-1})\left[f(a,b-2N^{-1})-f(a,b)\right].
\]
Every jump is bounded by \(2/N\). Its drift is exactly \((-ab,-ab-b^2+b/N)\), which converges uniformly on the unit square to \(F(a,b)=(-ab,-ab-b^2)\). Martingale maximal inequalities and Gronwall's lemma, using this Lipschitz drift, yield uniform-on-compact-time convergence in probability to
\[
\dot a=-ab,\qquad\dot b=-ab-b^2,
\qquad a(0)=\alpha,\ b(0)=1-\alpha.
\]

**First integral and terminal state.** Define \(h(a,b)=a\exp(-b/a)\), for \(a>0\), with the continuous extension \(h(0,b)=0\). Its derivatives are
\[
h_a=e^{-b/a}(1+b/a),\qquad h_b=-e^{-b/a}.
\]
Direct substitution gives \(\nabla h\cdot F=0\). Hence \(h(a(t),b(t))=r=\alpha e^{-(1-\alpha)/\alpha}\) for all \(t\ge0\). In particular \(a(t)\ge r\), while \(\dot b\le-rb\); thus \(b(t)\to0\) and \(a(t)\to r\), with \(b=a\log(a/r)\).

Choose a sufficiently large fixed \(T\) such that \(a(T)-b(T)>r/2\). By finite-horizon convergence, with probability tending to one, \(A(T)-B(T)>rN/3\). Each cross-edge deposition leaves \(A-B\) unchanged, while each clique-edge deposition increases it by two. Therefore, on this event, \(A(t)\ge rN/3\) for all \(t\ge T\) and every surviving clique vertex has a cross-edge available. Consequently all clique vertices eventually vanish, and if \(\tau_N\) is the time of the last deposition, then \(U_N=A(\tau_N)\). The cross-edge rate \(AB/N\) is at least \((r/3)B\) on this event, so comparison with successive exponential holding times gives \(\tau_N-T=O_{\mathbb P}(\log N)\). Further, \(B_N(T)/N\to b(T)\), and since future changes in \(A\) are bounded by the number of remaining \(B\) vertices, the terminal limit is \(U_N/N\to r\) by first letting \(N\to\infty\), then \(T\to\infty\). Boundedness implies convergence of expectations.

**Fluctuation martingale.** On the region \(a\ge r/3\), Taylor's theorem, uniformly bounded second derivatives of \(h\), and the first-integral identity give \(\mathcal L_N h=O(1/N)\). Define the stopped martingale
\[
M_N(t)=h(a(t\wedge\tau_N),b(t\wedge\tau_N))-h(a(0),b(0))
-\int_0^{t\wedge\tau_N}(\mathcal L_Nh)(a(s),b(s))\,ds.
\]
The \(O(1/N)\) bound applies on the high-probability event above after \(T\), and on every fixed pre-\(T\) interval with high probability because \(a(t)\ge r\). Since \(\tau_N-T=O_{\mathbb P}(\log N)\), the integrated generator drift is \(O_{\mathbb P}(\log N/N)=o_{\mathbb P}(N^{-1/2})\). Moreover, \(h(a(0),b(0))=r+O(N^{-1})\), and at the terminal state \(b(\tau_N)=0\), so \(h(a(\tau_N),0)=U_N/N\), except on an event of vanishing probability. Therefore
\[
\sqrt N\left(U_N/N-r\right)=\sqrt N M_N(\tau_N)+o_{\mathbb P}(1).
\]

**Quadratic variation and its tail.** The two first-order increments of \(h\) are respectively \(-N^{-1}(h_a+h_b)=-N^{-1}e^{-b/a}(b/a)\) and \(-2N^{-1}h_b=2N^{-1}e^{-b/a}\). Thus on finite horizons the predictable bracket of \(\sqrt N M_N\) converges, by the fluid limit, to the integral of
\[
Q(a,b)=e^{-2b/a}\left(\frac{b^3}{a}+2b^2\right).
\]
The difference between the actual bracket density and \(Q\) is \(O(1/N)\) uniformly in the relevant compact region; all jumps of \(\sqrt NM_N\) are \(O(N^{-1/2})\), so the finite-horizon martingale central limit theorem applies. On the high-probability region \(a\ge r/3\), the bracket density is bounded by \(Cb\), where \(C\) depends only on \(r\). The exact drift of \(b\) is at most \(-(r/3)b\), so conditional integration yields
\[
\mathbb E\left[\int_T^{\tau_N}b(s)\,ds\,\big|\,\mathcal F_T\right]
\le \frac{3}{r}b(T)
\]
on the event of positive separation (and analogously for the stopped process). Since \(b(T)\to0\) as \(T\to\infty\), the scaled martingale's post-\(T\) bracket is asymptotically negligible, uniformly after taking \(N\to\infty\). Doob's inequality gives the same conclusion for the martingale tail. Hence \(\sqrt N M_N(\tau_N)\) converges to a centered normal variable of variance \(\int_0^\infty Q(a(t),b(t))\,dt\).

**Explicit variance.** Parameterize the fluid curve by \(u=\log(a/r)\), so that \(a=re^u\), \(b=re^uu\), and \(du/dt=-b=-re^u u\). As \(t\) increases, \(u\) decreases from \(L=(1-\alpha)/\alpha\) to zero. Substituting into the bracket integral gives
\[
\int_0^\infty Q(a(t),b(t))\,dt
=r\int_0^L e^{-u}(u^2+2u)\,du
=r\left[4-(L+2)^2e^{-L}\right]=v.
\]
The integrand is strictly positive on \((0,L)\), hence \(v>0\) for \(0<\alpha<1\). The central limit theorem follows by Slutsky's theorem.

## Verification

The accompanying standalone `split_graph_verify.py` requires only the Python standard library. Run `python split_graph_verify.py`. It compares the independent count-chain rational moments against exhaustive enumeration of all allowed edge orders for three small split graphs (including 362,880 orders for a five-vertex graph), checks 35 exact moment states against an independent recurrence implementation, and compares finite-size moments at 12 parameter/size combinations with the asymptotic formulas. Four independent Riemann-sum checks confirm the closed-form quadratic-variation integral. These finite checks test modeling, signs, and normalization; the infinite-size conclusions rely on the martingale proof above.

## Relationship to prior work

Random sequential adsorption and random greedy matching are established stochastic models. Pippenger (1989) studies vertex and edge adsorption on regular graph families with controlled short cycles, whereas complete split graphs contain many triangles and strongly unequal vertex classes. Dyer and Frieze (1991) analyze randomized greedy matching more generally; the full text was not accessible for detailed theorem-by-theorem comparison. Dyer, Frieze, and Pittel (1993) analyze performance on random graph ensembles, distinct from this deterministic dense two-class geometry. Blelloch, Fineman, and Shun (2012, arXiv:1202.3205) analyze the parallel dependency depth of a random edge-priority maximal matching procedure, not its jammed vacancy distribution. Arnosti's accessible work on greedy matching in bipartite random graphs (2021) has different graph structure and distributional goals. Standard fluid-limit and martingale-CLT methods supply proof tools, but fixed-time Gaussian approximations do not by themselves give this terminal nonzero-vacancy limit or its explicit variance. Specialized prior dense-graph adsorption literature may contain an equivalent law; the accessible sources do not establish such an implication.

## Limitations

The result is asymptotic with fixed \(0<\alpha<1\); no Berry–Esseen rate, endpoint-uniform estimate, or large-deviation law is proved. The terminal Gaussian law concerns the random-priority deposition mechanism and not an equilibrium dimer ensemble or uniformly chosen maximal matchings. The full texts of two older plausible works were unavailable; originality remains subject to that bounded literature risk. No independent external validation is claimed.

## References

1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: 10.1137/0402034.
2. M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* **2** (1991). DOI: 10.1002/rsa.3240020104.
3. M. Dyer, A. Frieze and B. Pittel, “The average performance of the greedy matching algorithm,” *Annals of Applied Probability* **3** (1993). DOI: 10.1214/aoap/1177005436.
4. G. Blelloch, J. Fineman and J. Shun, “Greedy Sequential Maximal Independent Set and Matching are Parallel on Average,” arXiv:1202.3205, first public 2012-02-15.
5. N. Arnosti, “Greedy Matching in Bipartite Random Graphs,” 2021, author's publicly available manuscript.
