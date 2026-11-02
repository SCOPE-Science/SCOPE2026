# Exact Lipschitz norm and three-phase geometry of Moore-graph spectral filters

## Finding
Let \(G\) be a finite connected simple \(d\)-regular graph of diameter two and girth five, with \(d\ge2\), and let \(A\) be its adjacency matrix. Give the vertices their unweighted shortest-path metric. On the real vertex-functions modulo constants, use the Lipschitz norm
\[
\|f\|_{\mathrm{Lip}}=\max_{xy\in E(G)}|f(x)-f(y)|.
\]
For **every pair of real scalars** \(\alpha,\beta\), the exact induced operator norm is
\[
\boxed{\|\alpha I+\beta A\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\max\big\{|\alpha-d\beta|,\;|\alpha+(2d-3)\beta|,\;2(d-1)|\beta|\big\}.}
\]
All three displayed terms are essential: as \(\alpha/\beta\) varies for \(\beta>0\), the dominating terms are respectively \(d\beta-\alpha\) on \(\alpha\le(2-d)\beta\), \(2(d-1)\beta\) on \((2-d)\beta\le\alpha\le\beta\), and \(\alpha+(2d-3)\beta\) on \(\alpha\ge\beta\). In particular, the norm on the two-dimensional adjacency-filter space has an **exact three-phase, six-facet polyhedral unit ball**; the phase boundaries and every supporting functional are explicit. No vertex-transitivity or edge-transitivity assumption is required.

More generally, let \(q\) be any real polynomial (or any real spectral function of \(A\)). Set
\[
\Delta=\sqrt{4d-3},\qquad r=\frac{-1+\Delta}{2},\quad s=\frac{-1-\Delta}{2},\qquad
\beta_q=\frac{q(r)-q(s)}\Delta,\quad
\alpha_q=\frac{r q(s)-s q(r)}\Delta.
\]
The induced Lipschitz norm of \(q(A)\) is **exactly** the boxed expression with \(\alpha=\alpha_q\) and \(\beta=\beta_q\), independently of the constant-eigenspace multiplier \(q(d)\). Thus this formula gives the sharp norm of *every real adjacency spectral filter*, including signed and nonpositive kernels.

As a concrete consequence for heat flow, put \(L=dI-A\), \(P_t=e^{-tL}\), and let \(\mathcal C_G(t)\) denote the sharp graph-distance \(W_1\) Lipschitz/Wasserstein coefficient of \(P_t\), over all probability-measure pairs. With \(\lambda_1=d-r\), \(\lambda_2=d-s\), one has for every \(t\ge0\)
\[
\mathcal C_G(t)=\frac{(2d-3-s)e^{-\lambda_1t}-(2d-3-r)e^{-\lambda_2t}}\Delta.
\]
For the Hoffman--Singleton graph of degree seven,
\[
\boxed{\mathcal C_G(t)=\frac{14e^{-5t}-9e^{-10t}}5,\quad
\max_{t\ge0}\mathcal C_G(t)=\frac{49}{45}\text{ at }t=\frac15\log\frac97.}
\]
It strictly amplifies \(W_1\) for \(0<t<\frac15\log\frac95\); its instantaneous logarithmic contraction rate is strictly increasing thereafter and before the peak as well. All general formulas apply conditionally to a diameter-two Moore graph of degree \(57\), should one exist; no existence assertion is made.

## Assumptions and scope
A diameter-two Moore graph is a finite connected simple \(d\)-regular graph of girth five meeting the diameter-two Moore bound, hence having \(d^2+1\) vertices. The known examples are the five-cycle (degree two), Petersen graph (degree three), and Hoffman--Singleton graph (degree seven). The degree-57 existence problem remains unresolved. Every edge has length one. All scalars, spaces and functions are real. The operator \(\alpha I+\beta A\) preserves constant functions, so it induces a well-defined linear map on the quotient by constants even when it is not positive or Markovian. The Wasserstein corollary uses the continuous-time unnormalized Laplacian (each incident edge jumped along at rate one), not the normalized random walk.

## Proof
**1. Graph-distance geometry without transitivity.** A radius-two breadth-first count around any vertex gives \(1+d+d(d-1)=d^2+1\) distinct vertices, because girth five rules out triangles and squares. Consequently every nonadjacent pair has exactly one common neighbor and adjacent vertices have none. The adjacency relation satisfies
\[
A^2=(d-1)I-A+J,
\]
where \(J\) is the all-ones matrix. In particular the two eigenvalues on the mean-zero subspace solve \(z^2+z-(d-1)=0\), so they are precisely \(r,s\) defined above.

Fix any edge \(xy\) and define \(X=N(x)\setminus\{y\}\), \(Y=N(y)\setminus\{x\}\). Both have size \(d-1\). Their members are disjoint and all cross-distances \(d(a,b)\) for \(a\in X,b\in Y\) equal two; moreover \(d(y,a)=d(x,b)=2\). These facts follow from girth five and diameter two and require no automorphism assumption.

**2. Exact dual optimization for a signed filter.** The norm on graph Lipschitz functions is determined by edges. For an arbitrary real one-Lipschitz function \(f\), the image difference across \(xy\) is
\[
(\alpha-\beta)(f(x)-f(y))
+\beta\left(\sum_{a\in X}f(a)-\sum_{b\in Y}f(b)\right).
\]
Put \(f(y)=0\), \(u=f(x)\), \(v=(d-1)^{-1}\sum_{a\in X}f(a)\), and \(w=(d-1)^{-1}\sum_{b\in Y}f(b)\). Pairwise Lipschitz constraints imply
\[
-1\le u\le1,\quad |v-u|\le1,\quad |w|\le1,\quad |v-w|\le2,
\quad |v|\le2,\quad |u-w|\le2.
\]
Conversely, any triple satisfying these inequalities is realizable on the four supports by assigning the constant values \(v\) on \(X\), \(w\) on \(Y\), \(u\) at \(x\), zero at \(y\). The resulting potential is one-Lipschitz on this set and extends to all graph vertices by the McShane formula. Therefore the exact edge objective is a three-variable linear program with no hidden global feasibility constraints.

Assume first \(\beta\ge0\). For fixed \(u\in[-1,1]\), the greatest feasible difference \(v-w\) is \(\min\{2,u+2\}\). Indeed, \(v-w\le2\) by the cross-distance and \(v-w\le(u+1)-(-1)=u+2\) by the other two inequalities. Equality is achieved when \(-1\le u\le0\) by \(v=u+1,w=-1\), and when \(0\le u\le1\) by \(v=u+1,w=u-1\). Hence the maximum edge difference equals the maximum, over \(u=-1,0,1\), of
\[
(\alpha-\beta)u+\beta(d-1)\min\{2,u+2\},
\]
namely
\[
\max\{-\alpha+d\beta,\;2(d-1)\beta,\;\alpha+(2d-3)\beta\}.
\]
This is the maximum *absolute* edge difference, since the class of Lipschitz potentials is symmetric under \(f\mapsto-f\), so maximizing the signed objective already computes the absolute supremum. If \(\beta<0\), replace \((\alpha,\beta)\) by \((-\alpha,-\beta)\); the operator norm is unchanged. The two cases combine into the boxed max-of-three-absolute-linear-forms formula. The three regions are genuinely nonempty for every \(d\ge2\) (take respectively \(\alpha/\beta\) sufficiently negative, between \(2-d\) and \(1\), and greater than \(1\)); this establishes the sharp phase diagram and the nonredundancy of the six supporting facets.

**3. Spectral completeness.** On mean-zero functions, \(A\) has only the two eigenvalues \(r,s\). Lagrange interpolation on these two distinct values gives \(q(A)=\alpha_qI+\beta_qA\) *on the quotient by constants*. The possible additional rank-one term on constant functions vanishes on quotient norms. Thus Step 2 applies to every real adjacency spectral multiplier, not just Markov or nonnegative ones.

**4. Heat-flow example and transient amplification.** On the mean-zero subspace \(P_t\) has eigenvalues \(e^{-\lambda_1t}\) and \(e^{-\lambda_2t}\). Therefore
\[
\alpha(t)=\frac{r e^{-\lambda_2t}-s e^{-\lambda_1t}}\Delta,
\qquad \beta(t)=\frac{e^{-\lambda_1t}-e^{-\lambda_2t}}\Delta\ge0.
\]
Moreover \(\alpha(t)-\beta(t)=[(r+1)e^{-\lambda_2t}-(s+1)e^{-\lambda_1t}]/\Delta>0\), because \(r+1>0>s+1\). Hence Step 2's third linear branch is exactly the norm, giving the stated two-exponential expression. By Kantorovich–Rubinstein duality it equals the sharp \(W_1\) contraction/amplification coefficient of the Markov kernel \(P_t\), over arbitrary probability-measure pairs. Every edge pair of Dirac masses realizes it; transporting along shortest paths controls other pairs. Writing the norm as \(a e^{-\lambda_1t}-b e^{-\lambda_2t}\), where \(a=(2d-3-s)/\Delta\), \(b=(2d-3-r)/\Delta\), yields \(a>b>0\), \(a-b=1\), and
\[
-\frac{d}{dt}\log \mathcal C_G(t)\text{ has derivative }
\frac{ab(\lambda_2-\lambda_1)^2e^{-(\lambda_1+\lambda_2)t}}{\mathcal C_G(t)^2}>0.
\]
Its initial value is \(3-d\), and its limit is \(\lambda_1\). For degree seven, setting \(z=e^{-5t}\) reduces the coefficient to \((14z-9z^2)/5\), with exact maximum \(49/45\) at \(z=7/9\) and positive-time return to one at \(z=5/9\). The degree-three Petersen case is \((5e^{-2t}-2e^{-5t})/3\); degree two is similarly strictly contracting for every positive time.

## Verification
The standalone standard-library `checker.py` constructs the pentagon, Petersen, and Hoffman--Singleton graphs, verifies the Moore common-neighbor identity and every relevant four-support distance exactly, checks all three signed-norm phase branches on rational parameters, and replays the exact rational heat and peak certificates. Run `python3 checker.py` from the package directory. The optional `lp_check.py` independently solves full vertex-Lipschitz linear programs for positive and signed multipliers, using NumPy and SciPy. Its computations sample all three graph orders and many edges and parameters; the proof for every qualifying graph and every real multiplier is Steps 1--4, not the samples.

## Relationship to prior work
Münch and Wojciechowski [1, Theorem 3.8] connect lower Ollivier curvature bounds to graph heat-semigroup Lipschitz norms. Bonini and collaborators [2, Theorem 1.4] determine normalized infinitesimal curvature \(3/d-1\) for strongly regular girth-five graphs and develop exact lazy-step transport at high idleness. Together with standard Moore-graph spectral identities, their results can provide a short independent derivation of the positive heat-branch *corollary* in this paper; neither source by itself warrants claiming priority for that branch or the infinitesimal curvature. The main result here is instead the **full signed two-parameter Lipschitz operator norm and complete sharp phase fan for arbitrary real adjacency spectral filters**, including the two non-Markovian branches. These signed regimes are not covered by the positive high-idleness curvature formulas. Cushing and collaborators [3] study graph curvature and girth-four distance-regular cases, not signed spectral-filter norms. Faber and Keegan [4] address degree-57 existence, not analytic operator norms. The exact graph-filter classification is not identified in these checked texts or in the targeted searches reported separately, but an older equivalent calculation may exist.

## Limitations
The theorem uses the real graph-distance Lipschitz norm, unweighted diameter-two girth-five Moore graphs, and operators in the real adjacency spectral algebra. It does not extend automatically to weighted, directed, non-Moore strongly regular graphs or other norms. It does not claim a degree-57 Moore graph exists. The heat-flow formula is a consequence of the broader signed theorem and independently approachable using prior curvature results; no novelty is attributed to the previously known initial curvature. Prior literature searches cannot certify historical originality, and no independent external mathematical audit has been performed.

## References
[1] F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first posted 2017-12-04), Theorem 3.8, https://arxiv.org/abs/1712.00875.

[2] V. Bonini, C. Carroll, U. Dinh, S. Dye, J. Frederick and E. Pearse, *Condensed Ricci Curvature of Complete and Strongly Regular Graphs*, arXiv:1907.06733 (first posted 2019-07-15), Theorem 1.4, https://arxiv.org/abs/1907.06733.

[3] D. Cushing, S. Kamtue, R. Kangaslampi, S. Liu and N. Peyerimhoff, *Curvatures, graph products and Ricci flatness*, Journal of Graph Theory 96 (2021), 522--553, first online 2020-10-12, https://doi.org/10.1002/jgt.22630.

[4] V. Faber and J. Keegan, *Existence of a Moore graph of degree 57 is still open*, arXiv:2210.09577 (first posted 2022-10-18), https://arxiv.org/abs/2210.09577.

[5] A. E. Brouwer, *The Hoffman--Singleton graph*, database entry, https://aeb.win.tue.nl/drg/graphs/Hoffman-Singleton.html.
