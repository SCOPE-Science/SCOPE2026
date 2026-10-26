# A sharp hub-versus-base budget transition in continuous-time mixing on graph cones

## Finding
Let \(H\) be a finite connected, simple, vertex- and edge-transitive graph with \(n\ge3\) vertices and regular degree \(d\ge2\). Its unweighted combinatorial Laplacian is \(L_H\), and \(g=\lambda_2(L_H)>0\). Put \(\beta=2g/d\). Form the **cone** \(G=K_1\vee H\), adjoining one new hub connected to all vertices of \(H\).

Give each undirected edge of \(G\) an arbitrary nonnegative symmetric continuous-time jump rate \(w_e\). Impose the common edge-rate budget \(\sum_{e\in E(G)}w_e=B\), where \(B>0\). The optimum of the Laplacian spectral gap \(\lambda_2(L_w)\) is **exactly**
\[
\Lambda_H(B)=\begin{cases}
B/n,& 0<\beta\le1,\\[3pt]
(n+1)\beta B/[n(n+\beta)],&\beta>1.
\end{cases}
\]
More precisely, among automorphism-invariant assignments, every spoke (hub-to-base edge) has rate \(s\) and every base edge has rate \(t\), with
\[
(s,t)=\begin{cases}
(B/n,0),&0<\beta<1,\\[3pt]
(s,(2/d)(B/n-s)),\quad B/[n(n+1)]\le s\le B/n,&\beta=1,\\[3pt]
(\beta B/[n(n+\beta)],\,2B/[d(n+\beta)]),&\beta>1.
\end{cases}
\]
For \(\beta\ne1\) the displayed invariant optimizer is unique **within the invariant class**. Furthermore, when \(\beta<1\), **every** globally optimal (possibly asymmetric) allocation has zero rate on all base edges; this does not assert uniqueness of spoke rates without additional argument.

For wheels \(K_1\vee C_n\), the threshold is \(n=6\): \(\beta=4\sin^2(\pi/n)\), hence rim rates must vanish in every optimum for \(n\ge7\), whereas both rim and spokes receive positive rates in the unique invariant optimum for \(3\le n\le5\); at \(n=6\) an interval of invariant optimal allocations exists. For the hypercube family \(K_1\vee Q_k\) with \(k\ge2\), the corresponding threshold is \(k=4\): \(\beta=4/k\), so all cube-edge rates vanish in every optimum for \(k\ge5\).

## Assumptions and scope
All graphs are undirected, loopless, and finite. Vertex- and edge-transitivity are both assumed: they ensure that the automorphism group has exactly one spoke orbit and one base-edge orbit after adding the hub. The underlying base graph is connected; \(n\ge3\), \(d\ge2\). Edge rates are nonnegative; zero rates are allowed. The budget is the sum of rates over **undirected edges once**, not the sum over oriented transitions, the maximum weighted degree, or a per-vertex budget. The generator is \(-L_w\); the uniform stationary measure is preserved. The objective is the continuous-time spectral gap \(\lambda_2\), **not** the discrete-time second-largest eigenvalue modulus.

## Proof
**Step 1: averaging is lossless.** For each edge-rate vector \(w\),
\[
\lambda_2(L_w)=\min_{x\perp\mathbf1,\,\|x\|_2=1}x^{\mathsf T}L_wx.
\]
Being the pointwise minimum of linear forms in \(w\), this is a concave function. Each base automorphism extends by fixing the hub. Averaging any feasible allocation over this finite group retains the sum \(B\), nonnegativity, and the objective **at least as large**. Vertex-transitivity makes all spokes identical and edge-transitivity makes all base edges identical. Thus at least one global optimizer has rates \(s\) on all \(n\) spokes and \(t\) on all \(nd/2\) base edges, with
\[
ns+(nd/2)t=B,\qquad s,t\ge0.
\]

**Step 2: exact cone spectrum.** With the hub listed first,
\[
L_{s,t}=\begin{pmatrix}ns&-s\mathbf1^{\mathsf T}\\-s\mathbf1&sI_n+tL_H\end{pmatrix}.
\]
Its eigenvectors split into (i) the global constant vector, with eigenvalue zero; (ii) the hub-versus-base constant contrast, with eigenvalue \((n+1)s\); and (iii) vectors whose hub coordinate is zero and whose base coordinates are orthogonal to \(\mathbf1\), with eigenvalues \(s+t\lambda_j(L_H)\), \(2\le j\le n\). Consequently,
\[
\lambda_2(L_{s,t})=\min\{(n+1)s,\,s+tg\}.
\]

**Step 3: solve the exact two-line maximization.** Put \(\beta=2g/d\) and eliminate \(t=(2/d)(B/n-s)\). For \(0\le s\le B/n\),
\[
f(s)=\min\{(n+1)s,\,\beta B/n+(1-\beta)s\}.
\]
When \(\beta<1\) both affine branches increase strictly with \(s\), and the unique invariant maximizer is \(s=B/n\), with value \(B/n\) and \(t=0\). When \(\beta=1\), the second branch is the constant \(B/n\): equality is attained precisely when \((n+1)s\ge B/n\). When \(\beta>1\), one branch increases and the other decreases, so their unique intersection is optimal: \(s=\beta B/[n(n+\beta)]\). Substituting into the budget identity gives \(t=2B/[d(n+\beta)]\) and the stated gap.

**Step 4: every optimizer discards base edges in the strict low-\(\beta\) regime.** Let \(w\) be any global optimum with \(\beta<1\). Its automorphism average is invariant and also globally optimal. Step 3 forces the average base-edge rate to be zero. Every base-edge rate of \(w\) is nonnegative, and transitivity makes the average base-edge rate their arithmetic mean; therefore **each** original base-edge rate must be zero.

**Step 5: two exact families.** The cycle Laplacian gap is \(g=2-2\cos(2\pi/n)=4\sin^2(\pi/n)\), with \(d=2\), giving \(\beta=4\sin^2(\pi/n)\). This exceeds one exactly for \(3\le n\le5\), equals one at \(n=6\), and is below one for \(n\ge7\). The \(k\)-dimensional cube has \(n=2^k\), degree \(d=k\), and Laplacian gap \(g=2\), giving \(\beta=4/k\), with the indicated integer phase regimes. These spectral facts follow directly from Fourier eigenvectors on cyclic groups and characters on \(\{0,1\}^k\).

## Verification
The self-contained code `cone_verify.py` constructs cycle, cube and clique Laplacians; calculates the predicted invariant optimal rates, checks their total budget and their spectral gap against a direct symmetric eigensolver, and checks the scalar objective on a 1001-point grid. Sample coverage: cycles with \(3\le n\le14\), cubes in dimensions \(2\le k\le6\), and the complete graph on eight base vertices. Numerical checks confirm these instances to tolerance \(10^{-9}\) but **do not prove** the global theorem; the proof is Steps 1–5.

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006), *The Fastest Mixing Markov Process on a Graph*, formulated precisely the continuous-time optimization of \(\lambda_2\) under a linear sum-of-edge-rates constraint and derived a general semidefinite-programming and dual framework. Its inspected full text develops the general problem and examples but does **not** state the orbit-spectral threshold \(\beta=2\lambda_2(L_H)/d\), the all-optima base-edge extinction theorem for graph cones, or the wheel/hypercube integer phase transitions. Boyd's 2006 survey explains the convex graph-Laplacian optimization setting and reports that some discrete-time optimal edge rates vanish; it does not give the present criterion. Ghosh and Boyd (2006) address **selection of new edges**, a different discrete decision problem. Kirkland and Pati (2002) address absolute algebraic connectivity and cut-vertex extremizers; the cone of a connected base has no cut vertex (for a base with at least two vertices), so their recorded pendant-clique extremizer does not imply this cone theorem. The result is a structural closed-form solution within the established continuous-time framework, not a claim to invent the framework or spectral symmetrization.

## Limitations
Rates are allowed to vanish, so the optimal graph can be a strict subgraph of the allowed cone. The exact threshold requires vertex- and edge-transitivity of the base; a merely regular or vertex-transitive base with several edge orbits requires additional parameters. The proof classifies invariant optimizers completely, and all (possibly asymmetric) optima's **base-edge support** only when \(\beta<1\); it does not classify all asymmetric optimizers at or above the threshold. It does not optimize discrete-time SLEM, mixing constants independent of the spectral gap, resistances, or nodewise rate budgets. The originality assessment is based on the inspected primary literature and indexed comparisons, not exhaustive coverage of all spectral-graph sources; broader unstated equivalences remain possible. Independent audit has not been performed.

## References
1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. Public version: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf . First electronically public November 2, 2006, per the article.
2. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings ICM 2006, Vol. 3, 1311–1319. Author version: https://stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf .
3. A. Ghosh, S. Boyd, *Growing Well-Connected Graphs*, IEEE CDC (2006), 6605–6611. Public record: https://stanford.edu/~boyd/papers/growing_fast_graphs.html .
4. S. Kirkland, S. Pati, *On Vertex Connectivity and Absolute Algebraic Connectivity for Graphs*, Linear and Multilinear Algebra (2002). DOI: 10.1080/03081080290025453. This concerns a different extremal family and is not asserted to be completely inspected.
