# Exact Wasserstein heat-flow amplification on equal-blade windmill graphs

## Finding

For integers \(r\geq2\), \(m\geq1\), let \(G_{r,m}=K_1\vee(rK_m)\) be the graph whose \(r\) disjoint \(m\)-vertex cliques are all connected to one common hub. Equip its vertices with unweighted shortest-path distance \(d\). Let \(L=\operatorname{diag}(\deg)-A_G\) be the **unnormalized** combinatorial Laplacian, and \(P_t=e^{-tL}\) its continuous-time Markov semigroup, for \(t\geq0\). Define the optimal Wasserstein-one amplification coefficient by

\[
\mathcal C_{r,m}(t)=\sup_{\mu\neq\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)},
\]

where the supremum ranges over all probability measures on the vertex set and \(W_1\) uses \(d\). Then, **for every \(t\geq0\)**,

\[
\boxed{\mathcal C_{r,m}(t)=\frac{2(r-1)}r e^{-t}-\frac{r-2}{r}e^{-(rm+1)t}.}
\]

The coefficient is realized by a Dirac pair at the hub and any leaf of a clique; this assertion includes \(t=0\). Its instantaneous logarithmic contraction curvature is

\[
\boxed{\kappa_{r,m}=-\mathcal C'_{r,m}(0)=1-m(r-2).}
\]

The semigroup is Wasserstein-one nonexpansive for **all** \(t\geq0\) if and only if \(r=2\) or \((r,m)=(3,1)\). In both cases it is strictly contractive for every \(t>0\). In every other case the coefficient first increases above one, has a **unique** positive-time global maximum, and then decreases to zero. In the amplifying regime the unique maximizing time and maximal coefficient are

\[
\boxed{t_* =\frac1{rm}\log\frac{(r-2)(rm+1)}{2(r-1)},\qquad
\mathcal C_{r,m}(t_*)=\frac{2(r-1)m}{rm+1}\left(\frac{2(r-1)}{(r-2)(rm+1)}\right)^{1/(rm)}.}
\]

For fixed \(r\geq3\), increasing the clique size makes the maximal amplification approach \(2(r-1)/r\). For fixed \(m\geq1\), allowing \(r\to\infty\) makes that maximum approach \(2\). This transient transport amplification occurs although each graph is finite, connected, reversible for counting measure, and has spectral gap \(1\).

## Assumptions and scope

The graph has \(1+rm\) vertices. Each of the \(r\) outer blocks contains \(m\) vertices; distinct outer blocks have no edges between them, whereas every outer vertex is joined to the hub. The initial probability measures may be arbitrary; there are no uniformity assumptions on their masses. Jump rate **one along each edge** is essential: replacing the unnormalized Laplacian by the degree-normalized generator changes the conclusion. All times in the formula are nonnegative real numbers.

For any zero-sum signed measure \(\eta\) on a finite metric space, write \(\|\eta\|_{W_1}=\sup_{\operatorname{Lip}(f)\leq1}\sum_v\eta(v)f(v)\). By Kantorovich--Rubinstein duality, this is the transportation norm of the signed difference between two probabilities. The graph distance is the minimal number of edges on a path, not resistance distance or communicability distance.

## Proof

**1. Three nonconstant eigenspaces.** Write \(o\) for the hub, \(I_j\) for the sum of Dirac masses over block \(j\), and \(U=\sum_{j=1}^r I_j\). All identities below concern signed mass vectors indexed by vertices. The Laplacian has mutually orthogonal invariant subspaces consisting of the constants (eigenvalue \(0\)), block-constant mean-zero outer vectors (eigenvalue \(1\)), within-block sum-zero outer vectors (eigenvalue \(m+1\)), and the radial hub-versus-outer vector (eigenvalue \(rm+1\)). These subspaces exhaust \(1+rm\) coordinates; the within-block component is zero when \(m=1\). The eigenvalues themselves are established in the literature on windmill graph spectra; they are included here only as a verified ingredient.

Fix any outer vertex \(x\) in block \(1\), and abbreviate \(A=e^{-(m+1)t}\), \(B=e^{-t}\), and \(C=e^{-(rm+1)t}\). The spectral decomposition of \(\delta_o-\delta_x\), evolved by \(P_t\), is exactly

\[
\eta_t:=\delta_o P_t-\delta_xP_t
=C\left(\delta_o-\frac{U}{rm}\right)
-B\left(\frac{I_1}{m}-\frac{U}{rm}\right)
-A\left(\delta_x-\frac{I_1}{m}\right).
\]

In particular, \(\eta_t(o)=C\); every outer vertex in a block other than block \(1\) has mass \((B-C)/(rm)\geq0\). For a vertex \(y\neq x\) in block \(1\),

\[
\eta_t(y)=\frac{A-B}{m}+\frac{B-C}{rm}.
\]

To check its sign for **every** \(t\geq0\), put \(z=e^{-mt}\in(0,1]\); then \(A=Bz\), \(C=Bz^r\) and

\[
rm\,\eta_t(y)=B\bigl(rz-(r-1)-z^r\bigr)\leq0.
\]

Indeed, the bracket has value zero at \(z=1\) and nonnegative derivative \(r(1-z^{r-1})\) throughout \([0,1]\). The value at \(x\) equals this hypothetical other-block-\(1\) value minus \(A\), hence is also nonpositive (including when \(m=1\), for which no distinct \(y\) exists).

**2. Matching transport bounds.** Thus all positive mass in \(\eta_t\) is at the hub and in blocks \(2,\ldots,r\), and all negative mass lies in block \(1\). Any hub-to-block-\(1\) transfer has cost \(1\), while any outer-block-to-block-\(1\) transfer has cost \(2\). Sending the positive part to the negative part therefore gives a coupling whose cost is

\[
C+2\frac{r-1}{r}(B-C)=\frac{2(r-1)}r B-\frac{r-2}{r}C.
\]

For the reverse inequality, take the explicit \(1\)-Lipschitz potential \(f\) equal to \(0\) on block \(1\), \(1\) at the hub and \(2\) on every other block. Its pairing with \(\eta_t\) is **exactly** the displayed coupling cost. Consequently

\[
W_1(\delta_oP_t,\delta_xP_t)=\frac{2(r-1)}r B-\frac{r-2}{r}C.
\]

**3. Global operator norm.** For two different outer vertices \(x,y\) in the *same* block, their difference lies wholly in the eigenvalue-\(m+1\) subspace. Hence \(\delta_xP_t-\delta_yP_t=A(\delta_x-\delta_y)\), so their Wasserstein-one distance is \(A\), provided \(m\geq2\). Every edge of the graph is either hub-to-outer or within one block. For a finite graph with shortest-path metric, the Lipschitz seminorm of any function is the maximum of its absolute increments on edges. Kantorovich--Rubinstein duality therefore yields

\[
\mathcal C_{r,m}(t)=\max_{uv\text{ an edge}}W_1(\delta_uP_t,\delta_vP_t).
\]

For clarity, the corresponding bound for arbitrary initial probabilities can also be obtained by transporting each pair in an optimal initial coupling separately and averaging the resulting couplings. The hub-to-leaf value dominates every within-block value because

\[
\frac{2(r-1)}rB-\frac{r-2}{r}C-B=\frac{r-2}{r}(B-C)\geq0,
\qquad B\geq A.
\]

This proves the all-time formula, with no reliance on a finite sample of times.

**4. Sharp dynamical phase diagram.** Let \(\alpha_r=2(r-1)/r\), \(\beta_r=(r-2)/r\). For \(r=2\), the formula reduces to \(e^{-t}\). For \(r\geq3\),

\[
\mathcal C'_{r,m}(t)=e^{-t}\left(-\alpha_r+\beta_r(rm+1)e^{-rm t}\right).
\]

The bracket is strictly decreasing in \(t\). Its initial value equals \(m(r-2)-1\). For positive initial value the bracket crosses zero once, giving the stated \(t_*\); substituting the critical-point relation \(\beta_r(rm+1)C=\alpha_rB\) gives the stated peak. A nonpositive initial bracket implies strict decrease at every positive time (even when equality holds at zero). The only integer pairs with nonpositive initial bracket are \(r=2\) with arbitrary \(m\), and \((r,m)=(3,1)\). The asymptotic peak limits follow directly from \(t_*=O(\log(rm)/(rm))\) in the amplifying regimes. Since eigenvalue \(1\) occurs with positive multiplicity for \(r\geq2\), the spectral gap is \(1\).

## Verification

The accompanying standalone script `CHECK.py` constructs these graphs independently from their edge sets, diagonalizes the graph generator through dense matrix exponentiation, and solves the finite transportation problem by linear programming. It checks all possible types of graph edges for multiple values of \(r,m,t\), compares independently computed global Dirac-pair ratios with the claimed coefficient, tests arbitrary probability measures, and checks the analytic maximizing-time formula against numerical optimization. These finite checks are **not** substituted for the proof for arbitrary integers and real times.

A concrete amplifying example is \(G_{3,2}\), consisting of three triangles sharing one common hub. The exact coefficient is \(\frac43e^{-t}-\frac13e^{-7t}\); its peak occurs at \(t_*=\log(7/4)/6\approx0.093269298\), with maximum \(\mathcal C_{3,2}(t_*)\approx1.041083601\). For \(G_{3,1}\), the first derivative vanishes but \(\mathcal C_{3,1}(t)=1-2t^2+O(t^3)\), so it contracts strictly for every positive time.

## Relationship to prior work

Münch and Wojciechowski (arXiv:1712.00875, first publicly available 2017-12-04) give the general equivalence of graph Ollivier curvature bounds and exponential Lipschitz heat-flow bounds and characterize curvature through the *initial derivative* of Wasserstein transport. These results justify the curvature interpretation but do **not** themselves give the exact time profile here. Pedrotti (arXiv:2308.00516, first publicly available 2023-08-01) develops continuous-time coupling and curvature methods, including heat-flow Wasserstein contraction estimates for specific Markov chains, but does not identify this windmill all-time coefficient.

The windmill Laplacian spectrum is **known**: Kooij's *On generalized windmill graphs* (online 2018-11-26; DOI 10.1016/j.laa.2018.11.025) gives it as a special case of Theorem 8. The decomposition in the present proof is not proposed as an independently new spectral result. Kooij's full paper treats clustering, spectra, robustness and path-length metrics, not the exact Wasserstein-one heat operator norm. Lin and You (arXiv:2410.21887, first publicly available 2024-10-29) classify some friendship graphs by positive *degree-normalized* Lin--Lu--Yau curvature; that different generator and an initial-time curvature classification neither yields nor contradicts the all-time **unnormalized** result above. This last paper is a later comparison, not the motivating source date.

The new mathematical claim is precisely the all-time transport formula and its sharp dynamical phase transition and peak. No assertion of a first discovery of windmill spectra, graph curvature duality, or Wasserstein coupling is made. The historical-priority comparison is bounded by the inspected sources; an older equivalent formula under another graph or coupling terminology cannot be ruled out categorically.

## Limitations

The theorem requires equal-size outer cliques, one common hub, uniform unit edge rates, graph shortest-path cost and Wasserstein exponent one. It does not address heterogeneous blocks, degree-normalized random walks, different edge weights, \(W_p\) for \(p\neq1\), or infinite graphs. The exact spectral gap does not quantify the total-variation or \(W_p\) mixing time. No claim of independently certified originality or independent proof audit is made.

## References

1. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first posted 2017-12-04), Theorems 3.8 and 5.8. https://arxiv.org/html/1712.00875v1
2. R. Kooij, *On generalized windmill graphs*, *Linear Algebra and its Applications* 565 (2019), 25–46; first publicly available online 2018-11-26, Theorem 8. DOI:10.1016/j.laa.2018.11.025. https://pure.tudelft.nl/ws/portalfiles/portal/102441316/1_s2.0_S0024379518305482_main.pdf
3. F. Pedrotti, *Contractive coupling rates and curvature lower bounds for Markov chains*, arXiv:2308.00516 (first posted 2023-08-01), Section 5. https://arxiv.org/abs/2308.00516
4. H. Lin and Z. You, *Graphs with positive Lin–Lu–Yau curvature without quadrilaterals*, arXiv:2410.21887 (first posted 2024-10-29), Sections 1–3. https://arxiv.org/abs/2410.21887
