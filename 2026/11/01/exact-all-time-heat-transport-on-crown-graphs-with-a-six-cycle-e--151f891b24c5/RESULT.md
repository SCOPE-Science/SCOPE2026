# Exact all-time heat transport on crown graphs, with a six-cycle exception

## Finding
For each integer \(n\geq3\), let \(G_n\) be the unweighted **crown graph** obtained from the complete bipartite graph on \(\{A_1,\ldots,A_n\}\) and \(\{B_1,\ldots,B_n\}\) by deleting all matching edges \(A_iB_i\). Let \(L=D-\mathcal A\) be its combinatorial graph Laplacian and \(H_t=e^{-tL}\). All transport distances below use the original shortest-path distance on \(G_n\).

For \(t\geq0\), put
\[
 w=e^{-(n-2)t},\qquad v=e^{-nt},\qquad u=e^{-2(n-1)t}.
\]
For distinct vertices \(x,y\), every possible graph-distance class has the following **exact** heat-kernel Wasserstein-\(1\) distance:
\[
 W_1(H_t(x,\cdot),H_t(y,\cdot))=
 \begin{cases}
 (4w-u)/3, & n=3,\ x=A_i,\ y=B_j,\ i\ne j,\\[2pt]
 \dfrac{2(n-2)}{n}w-\dfrac{n-4}{n}u,&n\ge4,\ x=A_i,\ y=B_j,\ i\ne j,\\[6pt]
 2w,&x=A_i,\ y=A_j\ \text{or}\ x=B_i,\ y=B_j,\ i\ne j,\\[3pt]
 \dfrac{4(n-1)}n w-\dfrac{n-4}n u,&x=A_i,\ y=B_i.
 \end{cases}
\]
In particular, \(G_3\cong C_6\) and \(G_4\cong Q_3\). The graph distances in these three cases are respectively \(1\), \(2\), and \(3\). Exchanging \(x\) and \(y\) leaves the formulas unchanged. These cases exhaust all unordered distinct-vertex pairs.

The induced operator seminorm on real graph-Lipschitz functions, modulo constants, is attained and equals the first case:
\[
 \boxed{\ \|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
 =\begin{cases}
 (4e^{-t}-e^{-4t})/3,& n=3,\\[3pt]
 \dfrac{2(n-2)}n e^{-(n-2)t}-\dfrac{n-4}n e^{-2(n-1)t},&n\ge4.
 \end{cases}\ }
\]
For \(n=3\) the derivative at zero is \(0\), whereas for every \(n\ge4\) it is \(-2\). In either case the seminorm is strictly smaller than \(1\) at every \(t>0\). For \(n\ge4\), the triangle inequality along the shortest path from \(A_i\) through \(A_j\) to \(B_i\) is an equality for the **heat-kernel** transport metric:
\[
W_1(H_t(A_i,\cdot),H_t(B_i,\cdot))
= W_1(H_t(A_i,\cdot),H_t(A_j,\cdot))
+W_1(H_t(A_j,\cdot),H_t(B_i,\cdot)),\quad i\ne j.
\]
For \(n=3\), the right-hand side exceeds the left by exactly \(2(w-u)/3\), strictly positive when \(t>0\). Remarkably, the spectral mode \(e^{-nt}\) cancels from **all** the optimal-transport answers although it is present in the heat kernel.

## Assumptions and scope
Every edge has length \(1\), the measure at each vertex is counting measure, and the generator is the **unnormalized** Laplacian. The graph has degree \(n-1\) and is connected precisely for the relevant \(n\ge3\). For a real-valued function \(f\), define
\[
\|f\|_{\mathrm{Lip}}=\max_{A_iB_j\in E(G_n)}|f(A_i)-f(B_j)|.
\]
This is a seminorm on functions, a norm modulo constants. For probability laws \(\mu,\nu\) on vertices,
\[
 W_1(\mu,\nu)=\max_{\|f\|_{\mathrm{Lip}}\le1}\sum_x f(x)(\mu(x)-\nu(x)).
\]
By graph-metric Kantorovich duality, the edge constraints are equivalent to global \(1\)-Lipschitz continuity. All statements include \(t=0\) and all integer \(n\ge3\), without asymptotic or numerical qualifications.

## Proof
**1. Spectral heat kernel.** Write \(J\) for the \(n\)-by-\(n\) all-ones matrix, \(R=I-J/n\), and order vertices by their two bipartition classes. The four mutually orthogonal projectors
\[
P_0={1\over 2n}\begin{pmatrix}J&J\\J&J\end{pmatrix},\quad
P_s={1\over 2n}\begin{pmatrix}J&-J\\-J&J\end{pmatrix},\quad
P_+={1\over2}\begin{pmatrix}R&R\\R&R\end{pmatrix},\quad
P_-={1\over2}\begin{pmatrix}R&-R\\-R&R\end{pmatrix}
\]
have respective Laplacian eigenvalues \(0\), \(2(n-1)\), \(n\), and \(n-2\). Indeed the bipartite adjacency block is \(J-I\), and applying it to constant and zero-sum vectors verifies each eigenvalue. Thus
\[
 H_t=P_0+uP_s+vP_++wP_-.
\]
In particular, for \(1\le i,j\le n\),
\[
H_t(A_i,A_j)={1+u\over2n}+{v+w\over2}(\mathbf 1_{i=j}-1/n),\quad
H_t(A_i,B_j)={1-u\over2n}+{v-w\over2}(\mathbf 1_{i=j}-1/n),
\]
with the two remaining blocks determined by symmetry.

**2. Adjacent vertices.** By index permutation symmetry take \(x=A_1\), \(y=B_2\). Set
\[
\gamma={u-w\over n}\le0,\quad
\alpha=\gamma+{v+w\over2}>0,\quad
\beta=\gamma+{w-v\over2}\ge0.
\]
The row difference \(H_t(x,\cdot)-H_t(y,\cdot)\) on the \(A\)-vertices has coefficients \(\alpha\) at \(A_1\), \(\beta\) at \(A_2\), and \(\gamma\) at each other \(A\)-vertex. Its coefficients on \(B\)-vertices are the negatives after swapping indices \(1\) and \(2\). The sign conditions follow from \(u\le v\le w\) and, for \(z=e^{-t}\in[0,1]\),
\[
 \beta=w\left[{1-z^2\over2}-{1-z^n\over n}\right]\ge0,
\]
because \(\sum_{k=0}^{n-1}z^k/n\le(1+z)/2\) for every \(n\ge2\).

Averaging an admissible dual potential over the permutation symmetry of indices \(3,\ldots,n\), and antisymmetrizing under the automorphism exchanging \(A_i\leftrightarrow B_{\pi(i)}\), where \(\pi\) swaps \(1\) and \(2\), preserves the objective and feasibility. It leaves values \(a,b,c\) on \(A_1,A_2,A_k\) (\(k\ge3\)) and \(-b,-a,-c\) on \(B_1,B_2,B_k\). The objective is exactly
\[
2\bigl(\alpha a+\beta b+(n-2)\gamma c\bigr).
\]
The edges \(A_1B_2\) and \(A_2B_1\) impose \(|a|,|b|\le1/2\).

If \(n\ge4\), two distinct generic indices have an edge between their \(A\) and \(B\) vertices, so also \(|c|\le1/2\). Since \(\alpha,\beta\ge0\ge\gamma\), the objective is at most \(\alpha+\beta-(n-2)\gamma\), attained by \(a=b=1/2,c=-1/2\). This potential obeys *every* edge constraint, and substitution gives
\[
\alpha+\beta-(n-2)\gamma
={2(n-2)\over n}w-{n-4\over n}u.
\]
For \(n=3\) there is only one generic index, so no edge bounds \(|c|\) directly. The remaining constraints are \(|a+c|\le1\), \(|b+c|\le1\). The coefficient of \(c\) is nonpositive, hence its minimizing feasible value is \(c=-1-\min(a,b)\). The resulting objective is nondecreasing in both \(a,b\), and is maximized at \(a=b=1/2,c=-3/2\). It equals \(\alpha+\beta-3\gamma=(4w-u)/3\). The displayed witnesses remain feasible at endpoint cases with zero coefficients.

**3. Same-side pairs.** For \(x=A_1\), \(y=A_2\), antisymmetrize under swapping indices \(1\) and \(2\). The dual potential may be taken to be \(a,-a\) on the two selected \(A\)-vertices, \(b,-b\) on the corresponding \(B\)-vertices, and zero elsewhere. The heat-row difference then pairs to
\[
 (v+w)a+(v-w)b.
\]
The edge constraints imply \(|a|\le1\) and \(|b|\le1\); since \(0\le v\le w\), the objective is at most \(2w\). It is attained by \(a=1,b=-1\), with all other values zero. The same formula holds on the \(B\)-side.

**4. Deleted-matching antipodes.** For \(x=A_1\), \(y=B_1\), antisymmetrize under exchanging the two classes and average over the other indices. The potential has values \(a,-a\) on \(A_1,B_1\) and \(c,-c\) on every remaining matched pair. The constraints are
\[
 |c|\le1/2,\qquad |a+c|\le1.
\]
The heat-row pairing is
\[
 2\bigl[(w+\gamma)a+(n-1)\gamma c\bigr].
\]
Here \(w+\gamma>0\) and \((n-2)\gamma-w<0\). Consequently choose \(a=1-c\), then \(c=-1/2\); the extremizing values are \(a=3/2,c=-1/2\). Evaluating gives
\[
3w+(4-n)\gamma={4(n-1)\over n}w-{n-4\over n}u.
\]
All the asserted equalities are therefore attained by explicit feasible dual potentials, not merely bounded above.

**5. Operator norm, comparison, and time law.** Graph edges form one automorphism orbit, and the Lipschitz seminorm of \(H_tf\) is the maximum of its output edge differences. Duality implies the operator seminorm equals the maximal \(W_1\) distance between adjacent heat rows, so Step 2 is sharp. At \(t=0\), each transport formula reduces to the corresponding graph distance. The algebraic difference between the Step 4 formula and the sum of Steps 2 and 3 is \(0\) when \(n\ge4\), and equals \(-2(w-u)/3\) when \(n=3\). For \(n=3\), differentiating \((4e^{-t}-e^{-4t})/3\) gives initial derivative zero and strict decrease on \(t>0\). For \(n\ge4\), differentiating the edge formula gives derivative \(-2\) at zero; factoring its derivative by \(e^{-(n-2)t}\) and using \(u/w\le1\) proves the derivative stays negative for all nonnegative time. In each formula the \(v\) contribution cancels exactly.

## Verification
A standalone, dependency-free exact-rational checker is provided as `verify_crown.py`. It constructs the four-projector heat kernel independently in rational arithmetic by substituting \(z=e^{-t}\in\{1,1/2,2/3,3/4\}\), for \(3\le n\le8\). It checks symmetry, positivity, row sums, each displayed formula, and explicit feasible attaining potentials. For \(3\le n\le5\) it additionally enumerates all anchored **integer** edge-Lipschitz potentials, and checks that their maxima equal the formulas. The finite-graph Lipschitz polytope has integral vertices because its oriented edge-difference constraint matrix is totally unimodular; therefore the integer search is an exhaustive check of the relevant linear programs for those sizes. The analytic argument above, not finite testing, establishes the theorem for every \(n\ge3\) and every real \(t\ge0\).

Command: `python3 verify_crown.py`. Verified output:

`CERTIFICATE_OK rational_matrices=24 transport_witnesses=72 exhaustive_integer_potentials=2359`

## Relationship to prior work
Ollivier introduced the Markov-kernel transport curvature framework and its \(W_1\) viewpoint. Lin, Lu, and Yau studied local graph Ricci curvature and included cycle and cube examples. Münch and Wojciechowski established general links between graph heat flow, curvature and gradient estimates. Klee and Stamps explicitly calculated the crown-graph Laplacian characteristic polynomial, recovering the known eigenvalues \(0\), \(n-2\), \(n\), and \(2(n-1)\); the spectrum itself is **not** claimed as new. Those results motivate asking for sharp transport profiles, but their general bounds or local-curvature evaluations do **not**, without further graph-specific optimization, imply the three exact all-time formulas here. Earlier analyses of complete bipartite and complete multipartite graph heat flow concern different graph families: deleting a perfect matching from \(K_{n,n}\) produces a distance-three crown graph which, for \(n\ge3\), is not complete multipartite. The first-order curvature behavior of the six-cycle and cube, and familiar hypercube heat contraction principles, are background rather than assertions of priority; the new statement is the simultaneous sharp three-orbit classification for the entire crown family. A search of published mathematical records revealed crown-graph coloring and sequence-spectrum statements, but not this heat-transport calculation. Absence from checked sources does not establish exhaustive publication priority.

## Limitations
The result is for finite unweighted crown graphs, counting measure, the combinatorial heat generator, the original shortest-path metric, and Wasserstein-\(1\). It does not address degree-normalized or weighted generators, higher Wasserstein exponents, or arbitrary graph families. The novelty comparison is limited by the indexed and accessible literature: an earlier unindexed equivalent calculation is possible. No independent audit has been performed.

## References
- Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (initial public version, 2007-01-30), https://arxiv.org/abs/math/0701886.
- Yong Lin, Linyuan Lu, and Shing-Tung Yau, *Ricci curvature of graphs*, Tohoku Mathematical Journal **63** (2011), 605–627, DOI:10.2748/tmj/1325886283.
- Steven Klee and Matthew T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669 (first posted 2020-08-04), Proposition 8, https://arxiv.org/abs/2008.01669.
- Florentin Münch and Radosław Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017-12-04), https://arxiv.org/abs/1712.00875.
