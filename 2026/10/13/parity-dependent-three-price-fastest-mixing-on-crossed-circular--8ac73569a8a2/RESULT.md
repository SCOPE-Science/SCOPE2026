# Parity-dependent three-price fastest mixing on crossed circular ladders

## Finding

For every integer \(n\ge5\), consider the undirected graph with vertices \((j,\ell)\), where \(j\in\mathbb Z/n\mathbb Z\) and \(\ell\in\{0,1\}\). Its five edge classes per cyclic index comprise two same-layer cycle edges, one vertical rung, and two crossed diagonals:

\[
(j,\ell)\leftrightarrow(j+1,\ell),\qquad
(j,0)\leftrightarrow(j,1),\qquad
(j,\ell)\leftrightarrow(j+1,1-\ell).
\]

Each same-layer edge costs one per unit conductance, each rung costs \(t>0\), and each crossed diagonal costs \(s>0\). All \(5n\) edge conductances can be chosen **independently and nonnegatively**; their weighted total expenditure is exactly one. Let \(L\) be the ordinary weighted combinatorial Laplacian and maximize \(\lambda_2(L)\), including disconnected allocations for which this second-smallest eigenvalue is zero.

Put

\[
\mu=4\sin^2(\pi/n),\quad U=1/\mu,\quad
\beta=\begin{cases}4,&n\text{ even},\\4\cos^2(\pi/(2n)),&n\text{ odd},\end{cases}\quad
\delta=4-\beta,\quad z=\frac{1-\delta U}{\beta-\delta}.
\]

The following finite collection of *unit-gap edge-class triples* \((a,b,c)\) is well-defined and nonnegative; the coordinates refer respectively to same-layer, rung and crossed-diagonal conductance:

| Label | \(a\) | \(b\) | \(c\) |
| --- | ---: | ---: | ---: |
| A | \(U\) | \(1/2\) | \(0\) |
| C | \(0\) | \((1-\delta U)/2\) | \(U\) |
| M1 | \(z\) | \(0\) | \(U-z\) |
| M2 | \(U-1/4\) | \(0\) | \(1/4\) |
| D (odd \(n\) only) | \(0\) | \(0\) | \(1/\delta\) |

For each listed triple \(v=(a,b,c)\), define \(J(v)=2a+t b+2s c\). If \(J_*\) is the minimum of these four costs for even \(n\), or five costs for odd \(n\), then the exact global optimum is

\[
\boxed{\displaystyle \max_{w\ge0,\ \mathrm{cost}(w)=1}\lambda_2(L(w))=\frac1{nJ_*}.}
\]

For every cost-minimizing listed triple, assigning the common class rates \((a,b,c)/(nJ_*)\) on all edges of the respective classes attains the global optimum. **Every class-symmetric global optimizer** is obtained by applying the same normalization to a convex combination of the cost-minimizing listed triples. This classification is not asserted for all nonsymmetric optimal edge assignments.

The minimizing vertices have the following sharp strict-price regimes (equality gives ties resolved by the preceding minimum-and-convex-hull statement):

* If \(s>1\), vertex A wins for \(t<s-1\), and vertex M2 wins for \(t>s-1\), for either parity.
* If \(0<s<1\) and \(n\) is even, vertex C wins for \(t<1-s\), and M1 wins for \(t>1-s\).
* If \(n\) is odd and \(0<s<\delta/\beta\), vertex C wins for \(t<4s/\delta\), and D wins for \(t>4s/\delta\).
* If \(n\) is odd and \(\delta/\beta<s<1\), vertex C wins for \(t<4(1-s)/(\beta-\delta)\), and M1 wins for \(t>4(1-s)/(\beta-\delta)\).

At \(s=1\), M1 and M2 both minimize cost for every \(t>0\), with their entire joining segment optimal. At the odd-size crossover \(s=\delta/\beta\), the threshold is \(t=4/\beta\): C is optimal below it, M1 and D are both optimal above it, and C, M1, D all tie at it. Boundary lines elsewhere are interpreted as convex hulls of their tying vertices.

A qualitative parity effect follows: sufficiently cheap diagonals and expensive rungs make an **all-diagonal network optimal for odd cycle length**, whereas an all-diagonal allocation is disconnected for even cycle length and can never be optimal. The diagonal-only graph is one cycle of length \(2n\) for odd \(n\), but two disjoint cycles of length \(n\) for even \(n\).

## Assumptions and scope

The result applies to each integer \(n\ge5\) and all positive real prices \(s,t\). The graph is the strong product \(C_n\boxtimes K_2\) with three separately priced graph-edge orbits. The total budget is imposed on conductance itself, not on resistance or discrete-time transition probability. Edges with zero rate are allowed, but \(\lambda_2\) is always the **second-smallest eigenvalue including zero multiplicity**, not the smallest strictly positive eigenvalue in a disconnected graph. Rates and costs are symmetric between the two directions of each undirected edge.

## Proof

**1. Global symmetrization.** For any feasible independent assignment \(w\), cyclic rotations, reflection of the cycle, and exchange of the two layers preserve both the graph and every edge price. Averaging \(w\) over these automorphisms produces weights \((a,b,c)\) constant on each of the three classes while preserving the expenditure. The Rayleigh representation

\[
\lambda_2(L(w))=\min_{\substack{x\perp\mathbf1\\\|x\|_2=1}}\sum_{\{i,j\}}w_{ij}(x_i-x_j)^2
\]

is concave in \(w\). As the eigenvalue is invariant under vertex relabeling, the averaged assignment has spectral gap at least the original gap. Thus optimizing the three class rates determines the **unrestricted** optimal value and constructs unrestricted global optimizers.

**2. Exact three-mode spectral reduction.** For class rates \(a,b,c\), use Fourier modes \(e^{2\pi i kj/n}\) tensored with the layer-symmetric or layer-antisymmetric vector. With \(\sigma_k=4\sin^2(\pi k/n)\), the complete \(2n\)-eigenvalue multiset is

\[
\lambda_{k,+}=\sigma_k(a+c),\qquad
\lambda_{k,-}=\sigma_k a+(4-\sigma_k)c+2b,
\qquad 0\le k<n.
\]

The smallest positive \(\sigma_k\) is \(\mu\), and the largest is \(\beta\). The antisymmetric eigenvalues depend affinely on \(\sigma_k\); hence their minimum occurs at the endpoints \(0,\beta\). Consequently the exact spectral gap, including the disconnected case, is

\[
\boxed{\lambda_2=\min\bigl\{\mu(a+c),\;4c+2b,\;\beta a+\delta c+2b\bigr\}.}
\]

**3. Exact cost polygon.** Scale any class-symmetric design to spectral gap at least one. The feasible polyhedron is

\[
\mathcal P=\{a,b,c\ge0:\ a+c\ge U,\ 4c+2b\ge1,\ \beta a+\delta c+2b\ge1\}.
\]

For \(n\ge5\), \(U>1/2\), \(\beta>\delta\ge0\), \(0\le\delta U<1\), and \(U-z>1/4\). If a vertex of \(\mathcal P\) had all three coordinates positive, all three spectral inequalities would have to bind; the latter two force \(a=c=U/2\), and the rung coordinate would equal \((1-2U)/2<0\), impossible. Thus every vertex has a zero coordinate.

For \(a=0\), the first inequality forces \(c\ge U\) and makes the second automatic; the resulting feasible polygon has vertex C, and, only if \(\delta>0\), vertex D. For \(c=0\), the second inequality forces \(b\ge1/2\), so the unique vertex is A. For \(b=0\), the intersections of the first and third, and of the first and second, inequalities give M1 and M2; the additional possible nonnegative vertex is D for \(\delta>0\). The remaining intersections violate \(a+c\ge U\) or positivity. Hence the listed four or five triples are **all** vertices of \(\mathcal P\).

**4. Rescaling and completeness.** Minimize \(J=2a+t b+2s c\) over \(\mathcal P\). Since every coefficient is strictly positive, a minimum is attained at a vertex and the minimizing face is precisely the convex hull of its minimum-cost vertices. The unscaled unit-gap design costs \(nJ_*\). Scaling its weights by \(1/(nJ_*)\) makes the budget one and spectral gap \(1/(nJ_*)\). Conversely a better unit-budget gap would, by positive homogeneity, yield a unit-gap design with cost strictly below \(nJ_*\), a contradiction. The concavity step yields the same bound for arbitrary individual edge weights.

**5. Price regions and parity.** Direct evaluation gives

\[
\begin{aligned}
J_A&=2U+t/2,\\
J_C&=2sU+t(1-\delta U)/2,\\
J_{M1}&=2sU+2(1-s)z,\\
J_{M2}&=2U+(s-1)/2,\\
J_D&=2s/\delta\quad(n\text{ odd only}).
\end{aligned}
\]

Comparing these affine functions proves the price regions above. For odd \(n\), the trigonometric identity \(\mu=\beta\delta\) yields \(\delta U=1/\beta\), and the crossover at \(s=\delta/\beta\); the other thresholds follow by equating the relevant costs. The exact finite-vertex minimum also handles every boundary without exclusions. The parity statement follows independently by traversing consecutive diagonals: each move switches layer and advances the cycle index once, closing after \(2n\) moves when \(n\) is odd and after \(n\) moves when \(n\) is even.

## Verification

The accompanying `verify.py` requires Python 3 and NumPy and runs with `python3 verify.py`. It independently enumerates all feasible intersections of triples of bounding planes, verifies that the analytic candidate lists are exhaustive for ten sizes, compares all candidate costs across 850 positive-price instances, compares 130 direct full-Laplacian eigenspectra to the Fourier formulas, tests 430 irregular unit-budget individual-edge allocations against the asserted optimum, and checks 640 price-region classifications. The observed output is:

`VERIFY_OK vertices=45 independent_min_costs=850 full_spectra=130 nonsymmetric_budget_comparisons=430 phase_checks=640`

The experiments are finite numerical checks and neither establish the universal theorem nor exclude undiscovered published equivalences. The exact proof above supplies the universal quantifiers.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate the continuous-time fastest-mixing spectral-gap optimization with arbitrary positive edge costs and give the semidefinite dual; they do not give these strong-prism three-price vertex formulas. Sayama (2015) studies estimating Laplacian spectra of general direct and strong graph products rather than solving this exact constrained optimization. Pan and Li (2019) analyze **this same underlying strong-prism graph** with unit weights, derive its Laplacian block spectra and calculate Kirchhoff and spanning-tree invariants; their theorems do not allocate three independently priced edge classes to maximize the second eigenvalue. Tavasoli, Shakeri, Ardjmand and Rahman (2024) study allocation of interlayer edge weights with fixed intralayer Laplacians, not joint reweighting of all three price classes. The present optimization is consistent with these general methods and specializes to their known unit-weight spectral decomposition when \(a=b=c\), but the parity-dependent arbitrary-price optimal allocation is not supplied by those inspected statements.

## Limitations

The theorem determines the optimum over all individual edge weights and classifies **only** the edge-class-symmetric optimal assignments. It does not assert uniqueness of arbitrary nonsymmetric optimizers. It addresses the continuous-time symmetric Laplacian, not discrete-time second-largest-eigenvalue modulus, nonreversible chains, arbitrary stationary distributions, or cost models nonlinear in conductance. This finding has not undergone independent external mathematical audit. Although the relevant identified works were compared at statement and proof level, an equivalent specialized historical result outside the inspected sources remains possible.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI 10.1137/S0036144504443821. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published electronically 2006-11-02).
2. H. Sayama, *Estimation of Laplacian spectra of direct and strong product graphs*, arXiv:1507.03030 (2015). https://arxiv.org/abs/1507.03030.
3. Y. Pan, J. Li, *Resistance distance-based graph invariants and spanning trees of graphs derived from the strong product of \(P_2\) and \(C_n\)*, arXiv:1906.04339 (2019). https://arxiv.org/abs/1906.04339.
4. A. Tavasoli, H. Shakeri, E. Ardjmand, S. Rahman, *The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks*, Network Science **12** (2024), 261–288, DOI 10.1017/nws.2024.9. https://doi.org/10.1017/nws.2024.9.
