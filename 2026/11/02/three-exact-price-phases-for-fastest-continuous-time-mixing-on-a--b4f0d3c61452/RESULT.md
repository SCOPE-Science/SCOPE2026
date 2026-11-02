# Three exact price phases for fastest continuous-time mixing on a clique with one pendant leaf

## Finding

For every integer \(k\ge2\) and prices \(P,Q,R>0\), consider the \((k+2)\)-vertex graph obtained by attaching one pendant vertex to a distinguished vertex \(0\) of the complete graph \(K_{k+1}\). Independently assign nonnegative undirected conductances to all existing edges, with price \(P\) on each of the \(k\) edges joining vertex \(0\) to the other clique vertices, price \(Q\) on each of the \(\binom{k}{2}\) edges within the other clique vertices, and price \(R\) on the pendant edge. For every budget \(B>0\), the unique global maximizer of the second-smallest weighted-Laplacian eigenvalue uses constant rates \(a_*B/C_*\) on the first edge class, \(b_*B/C_*\) on the second and \(c_*B/C_*\) on the pendant edge; the maximum gap is exactly \(B/C_*\).

Define the rational function
\[
c(a)=\frac{(k+1)a-1}{(k+2)a-2},\qquad a>\frac{2}{k+2}.
\]
The exact normalized rates and optimal unit-gap cost are the following three regimes.

**All edge classes active.** If \(R<k^2P\) and \(Q<2(k^2P-R)/(k(k-1))\), put \(D=kP-(k-1)Q/2>0\). Then
\[
 a_*=\frac{2+\sqrt{kR/D}}{k+2},\qquad b_*=\frac{1-a_*}{k},\qquad c_*=c(a_*),
\]
\[
 C_*=\frac{k-1}{2}Q+\frac{2D+(k+1)R+2\sqrt{kRD}}{k+2}.
\]
Here \(2/(k+2)<a_*<1\), and all three rates are strictly positive.

**Clique-periphery edges deleted.** If \(R<k^2P\) and \(Q\ge 2(k^2P-R)/(k(k-1))\), then
\[
 a_*=1,\qquad b_*=0,\qquad c_*=1,\qquad C_*=kP+R.
\]
This includes equality in the price threshold.

**Pendant edge expensive.** If \(R\ge k^2P\), independently of \(Q\), then
\[
 a_*=\frac{2+\sqrt{R/P}}{k+2},\qquad b_*=0,\qquad
 c_*=c(a_*),\qquad
 C_*=\frac{2kP+(k+1)R+2k\sqrt{PR}}{k+2}.
\]
At \(R=k^2P\), the last formula reduces to \(a_*=c_*=1\) and agrees continuously with the preceding phase. When \(R>k^2P\), \(a_*>1\). The high-price phase does **not** disconnect the pendant: \(c_*>0\) in all three cases.

## Assumptions and scope

All edges represent symmetric continuous-time jump rates, so the generator is the negative weighted combinatorial Laplacian and the stationary measure is uniform on all \(k+2\) vertices. Edge weights are independently selectable, including zero; all three class prices and the budget are strictly positive. The original graph has all edges of \(K_{k+1}\) and exactly one additional pendant edge. An optimal zero within-periphery rate is allowed by the feasibility model; all hub–periphery and pendant rates remain positive. The objective is \(\lambda_2(L)\), not discrete-time SLEM, normalized-Laplacian gap, mixing time at a specified tolerance, Kirchhoff index or spanning-tree count.

## Proof

**Symmetry reduction and spectrum.** For any admissible assignment, average its Laplacian under all permutations of the \(k\) peripheral clique vertices. Cost does not change, and the minimum Rayleigh quotient on the mean-zero subspace, namely \(\lambda_2\), is concave in edge rates; thus averaging cannot decrease the objective. A class-symmetric optimum therefore exists. Write \(a\) for each hub–periphery rate, \(b\) for each peripheral-pair rate and \(c\) for the single pendant rate. The full eigenvalue multiset is
\[
 \left\{0,\;\underbrace{a+kb,\ldots,a+kb}_{k-1},\;\lambda_-,\lambda_+\right\},
\]
where \(\lambda_-<\lambda_+\) are the roots of
\[
 z^2-[2c+(k+1)a]z+(k+2)ac=0.
\]
This follows by splitting the peripheral zero-sum subspace from the three-dimensional subspace constant over all \(k\) peripheral vertices (the latter has one zero eigenvalue). In particular, \(\lambda_2=\min\{a+kb,\lambda_-\}\).

**Exact unit-gap feasible set.** Homogeneity reduces maximizing \(\lambda_2\) at total cost \(B\) to minimizing positive total cost subject to \(\lambda_2\ge1\). The condition \(\lambda_-\ge1\) is equivalent to
\[
 a>\frac2{k+2},\qquad c\ge c(a).
\]
Indeed, at fixed \(a>0\), \(\lambda_-\) increases strictly with \(c\) and has limiting value \((k+2)a/2\) as \(c\to\infty\); setting the quadratic at \(z=1\) equal to zero gives the stated \(c(a)\). The remaining \(k-1\) modes impose \(b\ge (1-a)_+/k\). Since all prices are positive, every minimum-cost symmetric unit-gap allocation uses equality in both rate lower bounds. Its cost is exactly
\[
 \Phi(a)=kPa+R\frac{(k+1)a-1}{(k+2)a-2}
       +\frac{k-1}{2}Q(1-a)_+,\qquad a>\frac2{k+2}.
\]

**One-dimensional strict convexity and phase boundaries.** Differentiating gives
\[
 \Phi''(a)=\frac{2Rk(k+2)}{((k+2)a-2)^3}>0.
\]
On \(a<1\), the derivative is \(kP-(k-1)Q/2-Rk/((k+2)a-2)^2\); on \(a>1\), it is \(kP-Rk/((k+2)a-2)^2\). At \(a=1\), the right derivative is \(kP-R/k\) and the left derivative is \(kP-(k-1)Q/2-R/k\). The unique minimizer lies below \(1\) exactly if \(R<k^2P\) and \(Q<2(k^2P-R)/(k(k-1))\), equals \(1\) in the intermediate regime, and exceeds \(1\) if \(R>k^2P\). Solving each derivative equation and substituting into \(\Phi\) yields precisely the three expressions in the Finding. The scalar minimizer and every class-symmetric optimum are unique. Positive homogeneity then gives the claimed \(B/C_*\) gap and scaled conductances.

**Uniqueness without a symmetry hypothesis.** Let an arbitrary unrestricted optimum \(w\) be given. Its permutation average is the unique symmetric optimum \(\bar w\). Normalize so their spectral gaps are \(1\). Let \(v\) be a mean-zero eigenvector at eigenvalue \(1\) in the three-dimensional class-constant subspace of \(L(\bar w)\). The three vertex values on hub, peripheral class and pendant are such that both the hub–peripheral difference and hub–pendant difference are nonzero: equality of either pair, by the corresponding eigenvector equation and positive eigenvalue, forces all three values to vanish. Since \(v\) is peripheral-constant, the Rayleigh quotient \(v^TL(w)v\) depends only on the total rates in the two hub-adjacent edge classes. Their averages agree with \(\bar w\), so \(v^TL(w)v=\|v\|^2\). As all mean-zero Rayleigh quotients of \(L(w)\) are at least \(1\), \(v\) itself is a unit-eigenvalue vector of \(L(w)\). Its pendant coordinate forces the pendant rate to equal \(c_*\); each peripheral coordinate forces the individual hub–periphery rate to equal \(a_*\).

If \(b_*=0\), nonnegativity and equality of the averaged peripheral-edge rates force every such edge weight to be zero. If \(b_*>0\), the peripheral zero-sum subspace has dimension \(k-1\). Its compressed Laplacian under \(w\) has every Rayleigh quotient at least \(1\), and its trace is exactly \(k-1\): the trace depends only on the already-fixed \(k\) hub–periphery rates and the sum of peripheral edge rates, which agree with \(\bar w\), and the symmetric optimum has \(a_*+kb_*=1\). Thus every unit vector in that subspace has Rayleigh quotient \(1\); positive semidefiniteness on the mean-zero subspace forces it to be a unit-eigenvector. Consequently the peripheral edge Laplacian is precisely \(kb_*(I-\mathbf1\mathbf1^T/k)\), so every individual peripheral edge has weight \(b_*\). Hence every unrestricted optimum equals the stated symmetric allocation, completing global uniqueness.

## Verification

The included standalone `verify.py` requires Python 3 with SymPy, NumPy and SciPy. Running `python verify.py` verifies the characteristic polynomial symbolically for \(k=2,\ldots,6\), three exact rational representatives of the three support regimes, 54 phase-boundary identities, and 40 independent variable-by-variable constrained numerical optimization comparisons for different sizes and costs. The extracted script was run to completion and reported `ALL CHECKS PASSED`. These finite checks support implementation accuracy; the all-\(k\), all-positive-price theorem rests on the analytic spectrum, strict-convexity and uniqueness arguments above, not on sampling.

For one exact nontrivial all-active example, at \((k,P,Q,R)=(3,1,1,2/3)\) the target-unit-gap rates are \((a_*,b_*,c_*)=(3/5,2/15,7/5)\), and the target-unit-gap cost is \(C_*=47/15\).

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulated the general fastest continuous-time mixing problem as a weighted-Laplacian/semidefinite optimization with edge costs and solved explicit examples including paths and cycles. Ghosh and Boyd (2006) gave a convex-hull symmetry reduction for algebraic-connectivity bounds over graph families, not the present fixed-topology, three-price allocation. Jafarizadeh's study of clique-lifted/lollipop chains supplies closed forms for discrete-time second-largest-eigenvalue-modulus minimization subject to fixed stationary masses and row stochasticity. That formulation cannot be substituted for the present continuous-time unnormalized spectral-gap objective with a separate global linear price budget. The claim here is the explicit all-price phase diagram and **unrestricted uniqueness** for the one-pendant-clique graph, not the general concavity/symmetry technique or the fact that the topology has been studied. These inspected sources do not state this particular result; this does not constitute a comprehensive literature priority certificate.

## Limitations

The theorem assumes identical prices within each of the three edge-orbits and a single pendant leaf. It makes no claims for independently heterogeneous within-class prices, several pendant leaves, arbitrary attached paths, discrete-time mixing, or physical dynamics beyond symmetric continuous-time rates. Some clique edges receive exactly zero optimal weight in two regimes; the result permits nonnegative conductances. The literature search and examination of closely relevant originals cannot eliminate all specialist-priority overlap, and no independent mathematical audit has occurred.

## References

1. A. Ghosh and S. Boyd, “Upper bounds on algebraic connectivity via convex optimization,” *Linear Algebra and its Applications* 418 (2006), 693–707, DOI 10.1016/j.laa.2006.03.006; available online May 5, 2006. Full text: https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf .
2. J. Sun, S. Boyd, L. Xiao and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699, DOI 10.1137/S0036144504443821; electronically published November 2, 2006. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf .
3. M. A. Jafarizadeh, “Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs,” full text: https://arxiv.org/pdf/2501.02421 . Its discrete-time problem is distinct from the present one.
