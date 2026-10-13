# The square-price transition for fastest mixing on a weighted star

## Finding
For every integer \(m\ge3\) and every relative price \(t>0\), the fastest-mixing symmetric continuous-time Markov process on a star with \(m\) leaves, one priced edge, and a unit total edge-cost budget has a **unique** allocation. Write \(w\) for the distinguished edge rate and \(u_2,\ldots,u_m\) for the remaining rates. The budget is
\[
 tw+\sum_{j=2}^{m}u_j=1,\qquad w,u_j\ge0.
\]
The maximum algebraic connectivity and all the optimal rates are as follows.

If \(0<t\le(m-1)^2\), the unique optimum is uniform:
\[
 w=u_2=\cdots=u_m=\frac1{m-1+t},\qquad
 \max\lambda_2=\frac1{m-1+t}.
\]
If \(t>(m-1)^2\), put \(h=\sqrt t\) and \(B=mt+2(m-1)(h+1)\). The unique optimum is
\[
 w=\frac{m(h+1)-1}{hB},\qquad
 u_2=\cdots=u_m=\frac{h+2}{B},\qquad
 \max\lambda_2=\frac{m+1}{B}.
\]
The rates are strictly positive even when \(t\) is arbitrarily large. The uniform-to-nonuniform transition is exactly \(t=(m-1)^2\); the ratio of the optimal rate to the all-equal-rate value tends to \((m+1)/m\) as \(t\to\infty\). At \(m=3,t=9\), for instance, the optimum is \(w=11/129\), \(u_2=u_3=5/43\), with mixing gap \(4/43\), compared with \(1/11\) for the uniform allocation.

## Assumptions and scope
The vertices are one hub \(0\) and \(m\) leaves \(1,\ldots,m\), where the edge \(0\!\! -\!\!1\) has price \(t\) and other edges have price one. The symmetric weighted Laplacian has entries \(L_{00}=\sum_{j=1}^m w_j\), \(L_{0j}=L_{j0}=-w_j\), \(L_{jj}=w_j\), and all other off-diagonal entries zero, where \(w_1=w\) and \(w_j=u_j\) for \(j\ge2\). The continuous-time generator is \(-L\); its uniform invariant distribution has asymptotic relaxation rate \(\lambda_2(L)\). We maximize this gap over *all* nonnegative feasible individual edge rates, including asymmetric choices among the ordinary leaves. Disconnected boundary choices yield zero gap and cannot maximize it.

## Proof
**1. A symmetric maximizer exists.** For \(n=m+1\), the variational identity
\[
 \lambda_2(L)=\min_{x\perp\mathbf1,\ \lVert x\rVert_2=1}x^{\mathsf T}Lx
\]
expresses the gap as an infimum of linear functions of the edge weights. Hence it is concave in those weights. The feasible simplex and the objective are invariant under every permutation of the \(m-1\) ordinary leaves. Averaging any maximizer over this finite group cannot decrease the gap, and yields a maximizer with \(u_2=\cdots=u_m=u\). Such a maximizer exists by compactness. As a strictly positive feasible allocation gives positive gap, every maximizer has strictly positive weights, because deleting any star edge disconnects the graph.

**2. Exact spectral reduction.** With one rate \(w\) and \(m-1\) ordinary rates \(u\), the Laplacian characteristic polynomial is
\[
 \det(XI-L)=X(X-u)^{m-2}\left[X^2-(2w+mu)X+(m+1)wu\right].
\]
The factor \((X-u)^{m-2}\) comes from the sum-zero contrasts of ordinary leaves; the remaining cubic quotient consists of the hub, distinguished leaf, and the common ordinary-leaf coordinate. Let \(\lambda_-\) denote the smaller root of the quadratic. If \(0<w<u\), then \(0<\lambda_-<u\), so the gap is \(\lambda_-\) and is simple; when \(w\ge u\) the gap equals \(u\). In particular at \(w=u\), the eigenvalue \(u\) has multiplicity \(m-1\).

**3. The one-dimensional maximization.** Set \(r=w/u>0\). The budget forces \(u=1/(m-1+tr)\). For \(r\ge1\), the gap equals \(u\), strictly decreasing in \(r\). Its best point in this region is \(r=1\), the uniform allocation. For \(0<r\le1\), write \(z=\lambda_-/u\in(0,1]\). Substituting into the quadratic above gives
\[
 r=\frac{z(m-z)}{m+1-2z},\qquad
 \lambda_2(z)=\frac{z(m+1-2z)}{(m-1)(m+1-2z)+tz(m-z)}.
\]
The function \(r(z)\) increases strictly from zero to one because
\[
 \frac{dr}{dz}=\frac{(m+1)(m-2z)+2z^2}{(m+1-2z)^2}>0
\]
for \(m\ge3\) and \(0<z\le1\). Differentiation of the gap shows that its derivative has the sign of
\[
 (m-1)\left[(m+1-2z)^2-tz^2\right].
\]
Since \(m+1-2z>0\) on this domain, the derivative is positive before and negative after \(z=(m+1)/(2+\sqrt t)\). This point lies within \((0,1)\) precisely when \(\sqrt t>m-1\). Consequently, at \(t\le(m-1)^2\) the unique symmetric maximizer is \(z=1\), while above that price the unique symmetric maximizer is \(z=(m+1)/(2+\sqrt t)\). Direct substitution gives exactly the advertised formulas for \(w,u\), and \(\lambda_2\). This also proves the rate-ratio limit and strict positivity.

**4. Uniqueness among all, including asymmetric, allocations.** Let any globally optimal allocation have expensive-edge rate \(w\) and ordinary rates \(v_2,\ldots,v_m\). Averaging ordinary rates preserves cost and, by step 1, produces a symmetric global optimum. Step 3 identifies that symmetric optimum uniquely. Thus \(w\) and the ordinary mean \(\bar u\) are fixed to their advertised values.

For \(t>(m-1)^2\), the symmetric optimum satisfies \(0<w<\bar u\), and its gap is a simple eigenvalue with eigenvector whose hub, distinguished-leaf, and ordinary-leaf coordinates are respectively \(b,a,c\). The coordinate difference \(c-b\) is nonzero: if \(c=b\), the ordinary-leaf eigen-equation with positive eigenvalue implies \(c=b=0\); the hub eigen-equation then forces \(a=0\), a contradiction. With the same \(w\) and ordinary-edge sum, this eigenvector has *the same Rayleigh quotient* on any asymmetric candidate as on the symmetric optimum, because its ordinary-leaf differences are all \(c-b\). Therefore a genuinely optimal asymmetric candidate must also have this vector as an eigenvector (its Rayleigh quotient reaches the global minimum). The ordinary-leaf eigen-equations \(v_j(c-b)=\lambda_2c\) force \(v_2=\cdots=v_m\).

For \(0<t\le(m-1)^2\), the symmetric optimum has all rates \(a=1/(m-1+t)\). Every putative asymmetric optimum has distinguished rate \(a\) and ordinary rates \(a+\delta_j\) with \(\sum_{j=2}^m\delta_j=0\). Let \(P=I-\mathbf1\mathbf1^{\mathsf T}/(m+1)\). Optimality of the asymmetric candidate implies \(L-aP\succeq0\). For each ordinary leaf \(j\), test the vector with hub coordinate zero, distinguished-leaf coordinate \(-1\), leaf \(j\) coordinate \(+1\), and all remaining coordinates zero. This vector is orthogonal to \(\mathbf1\), and its quadratic-form value under \(L-aP\) is precisely \(\delta_j\). Thus every \(\delta_j\ge0\), and their zero sum implies all vanish. The unique optimum follows at and below the threshold as well.

## Verification
The accompanying standalone `star_optimum_check.py` runs in Python with SymPy and prints `VERIFY_OK 58 exact cases`. It symbolically verifies the derivative and closed-form substitutions, exactly checks the spectrum for \(m=3,\ldots,8\), and verifies eigenvalue semidefinite bounds and explicit asymmetric perturbations across 40 rational parameter instances. The proof above, not these finite experiments, establishes all integer \(m\ge3\) and all real \(t>0\). A reproducible command is `python star_optimum_check.py`.

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis formulate fastest-mixing *continuous-time* symmetric Markov processes with arbitrary positive linear edge costs as a semidefinite program, and give path and cycle solutions. Their general SDP contains this star instance, but the inspected examples do not state the exact all-size square-price threshold, the explicit starred allocation, or full uniqueness for individually variable rates. Ghosh and Boyd supply the general eigenvalue-concavity and symmetry-reduction methods for graph Laplacians; those tools alone do not produce the present closed-form optimized conductances. Boyd's 2006 ICM exposition formulates the unit-cost continuous-time gap maximization. Shakeri and coauthors find a *different* weight-distribution transition for one-to-one couplings between two connected graph layers, not for a one-hub star with a priced bridge. No assertion is made that the general semidefinite program itself is new.

## Limitations
The classification is restricted to stars with at least three leaves, exactly one distinct positive edge price, a linear equality cost budget, freely selectable nonnegative rates, symmetric continuous-time diffusion, and the Euclidean/uniform-stationary spectral gap. It does not treat arbitrary tree edge prices, nonsymmetric or discrete-time Markov kernels, or fastest mixing under upper bounds on vertex exit rates. Finite tests do not certify the infinite parameter domain; the analytical argument does. A specialized earlier closed-form star result could exist outside the inspected publications, so originality remains subject to further literature review; independent validation has not been performed.

## References
1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, doi:10.1137/S0036144504443821. Freely accessible author PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. A. Ghosh and S. Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra and its Applications 418 (2006), 693–707, doi:10.1016/j.laa.2006.03.006. First available online 2006-05-05. Author PDF: https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf.
3. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians (2006). Author PDF: https://web.stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf.
4. H. Shakeri et al., *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785v1 (2015-10-22), https://arxiv.org/abs/1510.06785.
