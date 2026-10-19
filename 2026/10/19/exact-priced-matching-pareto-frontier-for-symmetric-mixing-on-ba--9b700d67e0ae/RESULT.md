# Exact priced-matching Pareto frontier for symmetric mixing on balanced complete bipartite graphs

## Finding
Fix an integer \(n\ge3\) and a price \(t>0\). In \(K_{n,n}\), designate one perfect matching. A matching edge has price \(t\) per unit transition probability; every other cross-edge has unit price. A symmetric nonnegative row-stochastic matrix \(P\), supported on these cross-edges and holding loops, has cost \(C(P)=\sum_{\{i,j\}\in E}c_{ij}P_{ij}\), counting **each undirected edge exactly once**, and second-largest eigenvalue modulus \(\mu(P)=\|P-J_{2n}/(2n)\|_2\). For any \(1/3\le\theta<1\), minimize \(C(P)\) subject to \(\mu(P)\le\theta\), without requiring symmetry under vertex permutations in the competing matrices.

Write \(r=1-\theta\), \(t_c=2(n-1)/(n-2)\), and \(\theta_c=n/(3n-4)\). The global minimum is attained by a permutation-invariant matrix with weight \(a\) on each nonmatching edge, weight \(b\) on each matching edge and diagonal \(d=1-(n-1)a-b\). The **complete list of invariant minimizers** is:

1. If \(0<t<t_c\), the single pair \(a=b=r/n\), of cost \(C_*=(n-1+t)r\).
2. If \(t>t_c\) and \(1/3\le\theta<\theta_c\), the single pair
   \[a=\frac{2\theta}{n},\qquad b=\frac{n-(3n-4)\theta}{2n}>0,\qquad C_*=2(n-1)\theta+\frac t2[n-(3n-4)\theta].\]
3. If \(t>t_c\) and \(\theta_c\le\theta<1\), the single pair \(a=r/(n-2)\), \(b=0\), of cost \(C_*=n(n-1)r/(n-2)\).
4. If \(t=t_c\), the complete closed segment
   \[\frac rn\le a\le\min\!\left\{\frac{2\theta}{n},\frac{r}{n-2}\right\},\qquad b=\frac{r-(n-2)a}{2},\qquad C_*=(n-1+t_c)r.\]

For \(\theta<1/3\), the constraint is infeasible. If \(\theta<\theta_c\), every feasible chain (not just invariant chains) must give some positive weight to a matching edge. At \(t>t_c\), matching weights vanish from the globally optimal invariant design exactly when \(\theta\ge\theta_c\). Unrestricted global minimizers need not be unique; the uniqueness and complete-face assertions concern the invariant class only.

Equivalently, for a cost budget \(B\ge0\), the exact global minimum SLEM is \(\mu_*(B)=\min_{C(P)\le B}\mu(P)\). If \(t\le t_c\),
\[\mu_*(B)=\max\!\left\{\frac13,1-\frac{B}{n-1+t}\right\}.\]
For \(t>t_c\), put \(B_c=2n(n-1)/(3n-4)\), \(B_0=2(n-1+t)/3\). Then \(B_c<B_0\), and
\[\mu_*(B)=\begin{cases}1-\dfrac{(n-2)B}{n(n-1)},&0\le B\le B_c,\\[4pt]\dfrac{tn/2-B}{t(3n-4)/2-2(n-1)},&B_c\le B\le B_0,\\[4pt]\dfrac13,&B\ge B_0.\end{cases}\]
The two descriptions are equivalent, including both transition endpoints and the zero-budget identity chain.

## Assumptions and scope
The graph has two labelled vertex classes of size \(n\). For each positive integer \(k\), \(J_k\) denotes the \(k\times k\) all-ones matrix; \(\|\cdot\|_2\) denotes the spectral operator norm. Its distinguished matching pairs equally indexed vertices in the classes; holding probability is free, whereas the cost of every undirected cross-edge is counted once. The diagonal is unrestricted except for entrywise nonnegativity and stochastic row sums. No irreducibility or aperiodicity is imposed, although the optimal chains for \(\theta<1\) are ergodic. The price \(t\) is positive, and the constrained-rate theorem uses \(\theta\in[1/3,1)\). All results concern symmetric transitions and a uniform stationary distribution. They do not address nonreversible chains, arbitrary edge-price patterns or all nonsymmetric optimal allocations.

## Proof
**1. Symmetry reduction without restricting competitors.** The simultaneous permutation group of the \(n\) paired indices, together with swapping the two vertex classes, preserves both the support and the cost. Conjugating any feasible \(P\) by the corresponding permutation matrices leaves its cost fixed. Because \(P\mapsto\|P-J_{2n}/(2n)\|_2\) is convex and invariant under these conjugations, averaging preserves feasibility and cost. Hence a global optimum exists in the invariant class. Every invariant matrix has the form
\[P=\begin{pmatrix}dI_n&a(J_n-I_n)+bI_n\\a(J_n-I_n)+bI_n&dI_n\end{pmatrix},\quad d=1-(n-1)a-b,\quad a,b,d\ge0.\]
Its cost is \(n[(n-1)a+tb]\).

**2. Exact spectral splitting.** On the constant symmetric, constant antisymmetric, zero-sum symmetric, and zero-sum antisymmetric subspaces, respectively, the eigenvalues are
\[1,\quad1-2[(n-1)a+b],\quad1-na,\quad1-(n-2)a-2b.\]
The last two have multiplicity \(n-1\) each, so \(\mu(P)\le\theta\) is precisely the six upper and lower inequalities bounding the last three scalars by \(\theta\), alongside \(a,b,d\ge0\).

**3. Sharp linear-program lower bound.** From the positive side of the zero-sum symmetric eigenvalue constraint, \(a\ge r/n\). From the positive side of the zero-sum antisymmetric constraint, \(b\ge[r-(n-2)a]/2\). Subtracting this antisymmetric lower constraint from the lower bound \(1-2[(n-1)a+b]\ge-\theta\) for the bipartition eigenvalue yields \(a\le2\theta/n\). Thus any feasible invariant design obeys
\[\frac{C(P)}n\ge(n-1)a+t\max\!\left\{0,\frac{r-(n-2)a}{2}\right\},\qquad\frac rn\le a\le\frac{2\theta}{n}.\]
The necessary range is empty for \(\theta<1/3\). When \(\theta\ge1/3\), the construction below shows it is nonempty. The lower envelope is piecewise affine, with slope \((n-1)-t(n-2)/2\) until \(a=r/(n-2)\) and strictly positive slope \(n-1\) after that.

If \(t<t_c\), the first slope is positive; the unique minimizing \(a\) is \(r/n\), and equality in the cost bound forces \(b=r/n\). If \(t>t_c\), the first slope is negative; the minimizing \(a\) is \(\min\{2\theta/n,r/(n-2)\}\), with \(b\) equal to the nonnegative lower bound. The switch between the two cases is exactly \(\theta_c=n/(3n-4)\). If \(t=t_c\), the first segment is flat and its full permitted interval, with the matching lower bound attained, is optimal. These equalities establish both the costs and **all invariant equality cases**, rather than merely a collection of examples.

**4. Sufficiency and boundary values.** For \(a=b=r/n\), the nontrivial eigenvalues are \(2\theta-1\) and \(\theta\) twice. The range \(\theta\ge1/3\) makes them admissible and \(d=\theta\). In the branch \(a=2\theta/n\), \(b=[n-(3n-4)\theta]/(2n)\), the nontrivial eigenvalues are \(-\theta\), \(1-2\theta\), and \(\theta\), while \(d=r/2\). On the branch \(a=r/(n-2)\), \(b=0\), the antisymmetric zero-sum eigenvalue is \(\theta\); the other two lie in \([-\theta,\theta]\) exactly throughout \(\theta\ge\theta_c\) (and \(\theta<1\)). Its diagonal is nonnegative. Every critical-price segment point is a convex combination of the corresponding feasible endpoints. Thus each cost lower bound is attained by an actual stochastic matrix. If every matching edge in an unrestricted feasible \(P\) were zero, its average would have \(b=0\), which is impossible when \(\theta<\theta_c\); this proves the necessity statement even outside the invariant class.

**5. Exact budget inversion.** The cost bound is continuous and strictly decreasing in \(\theta\) until the universal mixing floor \(1/3\). Inverting the three affine pieces gives the displayed budget formulas, with \(B_c=2n(n-1)/(3n-4)\) at \(\theta_c\), and \(B_0=2(n-1+t)/3\) at \(1/3\) for \(t>t_c\). At budget zero, \(P=I\) is the only option and has \(\mu=1\). Above the saturation budget the optimum stays \(1/3\). No additional phases are possible because the lower envelope's only kink is \(a=r/(n-2)\).

## Verification
The standalone Python 3 file `verify.py` uses only standard-library exact fractions. It independently enumerates every vertex of the original nine-half-plane feasible region for \(3\le n\le11\), tests multiple rational target rates and both sides of the critical price, checks all four spectral eigenspaces against full \(2n\times2n\) matrices for \(3\le n\le8\), samples the entire critical-price equality face, and checks the budget inversion. Run `python verify.py`. The actual result was:

`VERIFY_OK 12885 exact rational assertions; n=3..11; full LP vertices, eigenspaces, budget inversion`

The finite checks are corroboration, **not** a proof for arbitrary \(n\); the unlimited-order proof is given above.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao (2007, arXiv:0709.0955v1), especially Sections 3.1.2 and 5.3.1, formulate symmetry reduction and explicitly solve unpriced complete bipartite fastest mixing. Their known formula gives the present baseline \(1/3\) at uniform cost and, by their edge-transitive graph result, the crown-graph threshold \(n/(3n-4)\) when matching edges are forbidden. Those benchmark values are prior knowledge. The present claim concerns a *heterogeneous, matched-versus-unmatched per-edge price*, an exact rate-cost Pareto frontier, the independent critical price \(2(n-1)/(n-2)\), and the entire critical-price optimizer segment.

Gnecco, Morisi and Bemporad (2015) develop sparse regularizations of fastest mixing and general optimality/robustness properties. They study uniform \(\ell_1\)-cost regularization and numerical sparsification, not an explicit closed-form priced-matching transition. These general frameworks enable the formulation but do not contain the present piecewise result. The global optimum here is proved analytically using a two-variable spectral reduction, without asserting an algorithmic novelty claim.

## Limitations
Uniqueness is established only among invariant matrices, not all feasible globally optimal symmetric matrices. No claim is made for nonuniform stationary distributions or arbitrary edge prices. The critical crown threshold and unpriced baseline were known before this result; the price-threshold and full Pareto classification are the assessed contribution. The formula is exact, but no independent mathematical audit has been performed, and mathematically equivalent results may occur in specialized literature that was not located.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, submitted 6 September 2007, Sections 1, 3.1.2, 5.3.1. https://arxiv.org/abs/0709.0955
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI:10.1137/S0036144503423264. https://web.stanford.edu/~boyd/papers/fmmc.html
3. G. Gnecco, R. Morisi and A. Bemporad, *Sparse Solutions to the Average Consensus Problem via Various Regularizations of the Fastest Mixing Markov-Chain Problem*, IEEE Trans. Network Sci. Eng. 2 (2015), 97–111, DOI:10.1109/TNSE.2015.2479086. https://cse.lab.imtlucca.it/~bemporad/publications/papers/ieeetnse-consensus.pdf
