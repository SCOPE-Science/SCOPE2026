# A three-phase price law for complete-bipartite spectral-gap design

## Finding

Let \(p\ge3\), \(m\ge p\), \(t=p-1\), and let \(K_{p,m}\) have one designated vertex in its \(p\)-vertex part. Each edge incident to that vertex costs \(P>0\) per unit conductance; every other edge costs \(Q>0\). All \(pm\) edge conductances are independently adjustable and nonnegative, subject to total expenditure at most \(B>0\). The objective is to maximize \(\lambda_2(L)\), the second-smallest eigenvalue of the unnormalized weighted combinatorial Laplacian.

Define
\[
\beta=\frac{m+2t+\sqrt{m^2-4t}}{2t(m+p)},\qquad
\mathcal R=\left(\frac{m^2+m\sqrt{m^2-4t}-2t}{2t}\right)^2,\qquad r=\frac PQ.
\]
The **exact unrestricted optimum** is \(\lambda_2^*=B/C_*\), with
\[
C_*=\begin{cases}
(m-t)P+tQ,&0<r<1,\\
m\bigl[P(1-t\beta)+tQ\beta\bigr],&1\le r\le\mathcal R,\\
\displaystyle\frac{(m+t)P+t(m+1)Q+2t\sqrt{PQ}}{m+p},&r>\mathcal R.
\end{cases}
\]
For an optimal allocation, assign normalized conductance \(a\) to each edge from the distinguished vertex and \(b\) to each of the other \(tm\) edges, where
\[
(a,b)=\begin{cases}
\left(1-\frac tm,\frac1m\right),&r<1,\\
\left(1-t\beta,\beta\right),&1\le r\le\mathcal R,\\
\left(\frac{m+t+t/\sqrt r}{m(m+p)},\frac{m+1+\sqrt r}{m(m+p)}\right),&r>\mathcal R.
\end{cases}
\]
Multiply both conductances by \(B/C_*\). Every exhibited conductance is strictly positive. The optimizer is unique **within the two-class symmetric family** for \(r\ne1\). At \(r=1\), every two-class optimum has \(a=1-tb\) with \(1/m\le b\le\beta\); the interval degenerates when \(m=p\). No uniqueness claim is made among all possibly asymmetric optimal allocations.

For fixed \(p\) and \(m\to\infty\), the second transition has the sharp scale
\[\mathcal R\sim \frac{m^4}{(p-1)^2}.\]
In the strongly imbalanced regime \(r>\mathcal R\), the normalized Fiedler eigenvalue is simple. The threshold is an exact change in the active spectral constraint, not a heuristic allocation rule.

## Assumptions and scope

The graph is simple, undirected and complete bipartite. The distinguished vertex belongs to the smaller or equal part, with integers \(m\ge p\ge3\). Edges within either part are absent. All conductances can be zero, although the exhibited optimal allocation is strictly positive. Costs are constant within each of the two prescribed price classes and strictly positive. The Laplacian is the **unnormalized** operator \(L=D-A\); neither stochastic-normalized eigenvalues nor effective-resistance objectives are being optimized. The budget scales all edge weights linearly.

## Proof

**1. Unrestricted-to-symmetric reduction.** On the subspace orthogonal to the all-ones vector, \(\lambda_2(L)=\min_{\|x\|=1,\,x\perp\mathbf1}x^TLx\) is concave in the independent edge conductances. Average any feasible allocation over permutations of the \(m\) vertices in the second part and of the \(t\) equal-price vertices in the first part. This preserves cost and feasibility, and cannot decrease the objective. Thus some global optimum has exactly the two edge classes \(a,b\). This proves that optimizing over them yields the **unrestricted optimal value**, without assuming that all asymmetric optimizers are symmetric.

**2. Exact spectrum.** For the two-class graph, leaf-difference vectors in the \(m\)-vertex part have eigenvalue \(S=a+tb\), with multiplicity \(m-1\); differences among the \(t\) equal-price hub vertices have eigenvalue \(mb\), with multiplicity \(t-1\). The constant-on-each-class quotient, in coordinates (designated hub, mean ordinary hub, mean leaf), has matrix
\[
\begin{pmatrix}
ma&0&-ma\\0&mb&-mb\\-a&-tb&a+tb
\end{pmatrix}.
\]
Its eigenvalues are zero and the two roots \(\lambda_-\le\lambda_+\) of
\[
\lambda^2-\bigl[(m+1)a+(m+t)b\bigr]\lambda+m(m+p)ab=0.
\]
Hence \(\lambda_2(L)=\min\{a+tb,mb,\lambda_-\}\), with multiplicities interpreted separately at coincidences.

**3. Exact unit-gap feasibility.** By positive homogeneity, minimize \(m(Pa+tQb)\) subject to \(\lambda_2\ge1\). Necessarily \(b\ge1/m\), and \(a+tb\ge1\). Put
\[
d(b)=m(m+p)b-(m+1),\qquad g(b)=\frac{(m+t)b-1}{d(b)}.
\]
For \(b\ge1/m\), the denominator is at least \(t\ge2\), so it is strictly positive. The condition that both roots of the displayed quadratic are at least one is equivalent to
\[
f(a,b)=m(m+p)ab-(m+1)a-(m+t)b+1\ge0
\quad\Longleftrightarrow\quad a\ge g(b).
\]
Indeed, for \(a\ge g(b)\) the sum of the two roots is at least two: at \(a=g(b),b=1/m\), the sum is \(2+p/m>2\), and its derivative along this boundary is
\[
(m+t)-\frac{t(m+1)}{d(b)^2}>0.
\]
Thus \(f\ge0\) cannot conceal two roots below one. The complete unit-gap feasible region is exactly
\[
b\ge1/m,\qquad a\ge\max\{1-tb,g(b)\}.
\]

**4. The two boundary branches.** Along \(a=1-tb\), the quadratic-root condition becomes
\[
f(1-tb,b)=m\bigl[-t(m+p)b^2+(m+2t)b-1\bigr].
\]
Its upper root is precisely \(\beta\). Because \(m\ge p\), \(f(1-t/m,1/m)=t(m-p)/m\ge0\), so \(\beta\ge1/m\). The lower root is no larger than \(1/m\). Therefore the minimum feasible \(a\) is \(1-tb\) on \([1/m,\beta]\) and \(g(b)\) on \([\beta,\infty)\). The function \(g\) satisfies
\[
g'(b)=-\frac t{d(b)^2}<0,\qquad
 g''(b)=\frac{2tm(m+p)}{d(b)^3}>0.
\]
Consequently the unit-gap expense as a function of \(b\) is strictly convex on the second branch, while on the first its slope is \(mt(Q-P)\). If \(P<Q\), the minimizing endpoint is \(b=1/m\); when \(P=Q\), all of \([1/m,\beta]\) minimizes. When \(P>Q\), expense decreases to \(\beta\) on the first branch. On the second branch its derivative is
\[
mtQ\left(1-\frac{r}{d(b)^2}\right).
\]
Since \(d(\beta)^2=\mathcal R\), the minimum stays at \(\beta\) for \(1<r\le\mathcal R\), and otherwise occurs uniquely at \(d(b)=\sqrt r\), giving
\[
b=\frac{m+1+\sqrt r}{m(m+p)},\qquad
 a=g(b)=\frac{m+t+t/\sqrt r}{m(m+p)}.
\]
Substitution yields exactly the three displayed cost formulas. Scaling by \(B/C_*\) proves the optimum for arbitrary budget.

**5. Transition geometry.** For \(m=p\), \(\beta=1/m\) and \(\mathcal R=t^2\). For \(m>p\), the first branch has positive length, making the price boundary \(r=1\) a genuine allocation transition. Above \(\mathcal R\), the leaf and ordinary-hub eigenvalues are strictly greater than one and only \(\lambda_-\) is active; at \(r=\mathcal R\), the leaf eigenvalue and \(\lambda_-\) coincide at one. Finally \(\sqrt{m^2-4t}=m-2t/m+O(m^{-3})\) establishes \(\mathcal R\sim m^4/t^2\).

## Verification

The companion script `verify.py` constructs the full weighted graph matrices independently and verifies the characteristic-polynomial factorization exactly on representative parameter grids, checks the rational-envelope identities symbolically, compares the predicted optimum with full-matrix eigenvalues for many parameters, and runs independent constrained numerical optimizations over the two symmetric variables. Execute `python3 verify.py` with Python 3, NumPy, SymPy and SciPy. The recorded successful execution performed 1,716 deterministic assertions and 26 successful independent numerical constrained optimizations. These finite checks do not replace the proof for all integers and price ratios.

## Relationship to prior work

Sun–Boyd–Xiao–Diaconis formulate weighted-cost algebraic-connectivity maximization as a semidefinite program, and give examples involving paths, cycles and small graphs; their inspected results do not supply this two-price, all-\(p,m\) closed form. Boyd–Diaconis–Parrilo–Xiao give general symmetry reduction and discrete-time complete-bipartite spectral blocks, but optimize the second-largest **absolute** transition eigenvalue rather than this continuous-time Laplacian gap with heterogeneous costs. Shakeri and coauthors examine one-to-one interlayer edges between two fixed networks and budget transitions, not all freely variable edges of these complete bipartite graphs. Prior two-hub price formulas do not imply the \(p\ge3\) case, whose additional ordinary-hub eigenspace and leaf constraint produce distinct transitions. A historical equivalence elsewhere in spectral network design cannot be excluded.

## Limitations

The theorem assumes \(m\ge p\ge3\) and exactly two edge-price classes determined by a single distinguished hub. The full value is optimized over independent individual edge weights, but uniqueness is proved only within the symmetric two-class family. It does not cover arbitrary per-edge prices, normalized Laplacians, stochastic transition matrices or Kirchhoff-index objectives. Numerical tests are finite consistency checks; independent proof review has not been performed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (electronic publication November 2, 2006).
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (September 6, 2007), https://arxiv.org/abs/0709.0955.
3. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (October 22, 2015), https://arxiv.org/abs/1510.06785.
