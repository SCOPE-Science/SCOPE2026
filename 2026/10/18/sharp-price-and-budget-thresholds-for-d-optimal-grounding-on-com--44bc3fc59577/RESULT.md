# Sharp price and budget thresholds for D-optimal grounding on complete bipartite networks

## Finding

Let \(p\ge q\ge1\) be integers, \(B>0\), and \(t>0\). On the unit-edge complete bipartite graph \(K_{p,q}\), choose independent nonnegative vertex-grounding conductances \(g_v\) with unit price on the \(p\)-vertex class and price \(t\) on the \(q\)-vertex class, subject to total cost \(B\). The **unique unrestricted maximizer** of
\[
 \det\bigl(L+\operatorname{diag}(g)\bigr)
\]
assigns a common gain \(a_*\) to every vertex in the class of size \(p\) and a common gain \(b_*\) to every vertex in the class of size \(q\).

Define
\[
 t_{\mathrm{hi}}=\frac{B^2+Bp(q+1)+p^2q}{p^2(B+q)},
\qquad
 Q(t)=pq^2t^2+q\bigl(B(p+1)-pq\bigr)t+B(B-q^2).
\]
If \(0<B<q^2\), let \(t_{\mathrm{lo}}>0\) be the unique positive zero of \(Q\). If \(B\ge q^2\), set \(t_{\mathrm{lo}}=0\). Then \(0\le t_{\mathrm{lo}}<t_{\mathrm{hi}}\), and the full solution is:

* When \(0<t\le t_{\mathrm{lo}}\), the optimum is \(a_*=0\) and \(b_*=B/(tq)\). This regime is empty when \(B\ge q^2\).
* When \(t_{\mathrm{lo}}<t<t_{\mathrm{hi}}\), both gains are strictly positive. The value \(a_*\) is the unique root in \((0,B/p)\) of \(\Phi(a)=0\), with \(b_*=(B-pa_*)/(tq)\), where \(\Phi\) is defined in the proof.
* When \(t\ge t_{\mathrm{hi}}\), the optimum is \(a_*=B/p\) and \(b_*=0\).

At equal prices \(t=1\), the second class is entirely ungrounded exactly when \(p\ge q+2\) and \(0<B\le p(p-q-1)\); otherwise **both classes** receive strictly positive gains. In particular, the star \(K_{m,1}\), for \(m\ge3\), has a sharp threshold at \(B=m(m-2)\).

## Assumptions and scope

The graph has \(p+q\) vertices, all \(pq\) bipartite edges have conductance one, and \(L\) is the usual combinatorial Laplacian. Each \(g_v\) may be chosen independently, including zero. The budget is saturated because the log determinant is strictly increasing in every gain. The strictly positive budget makes \(L+\operatorname{diag}(g)\) positive definite. The objective is D-optimal (inverse-volume) grounding, **not** trace-inverse minimization, spectral-gap maximization, or discrete leader selection. The parameters \(p,q,B,t\) range over all stated values, with no large-graph or small-budget approximation.

One interpretation appends a new ground vertex and assigns conductance \(g_v\) to its connection with vertex \(v\). The determinant is then the weighted spanning-tree count of the augmented graph, equivalently a rooted-forest partition function of the original graph. Alternatively, if \(L+\operatorname{diag}(g)\) is the precision matrix of a Gaussian network model, maximizing its determinant minimizes the volume of the covariance confidence ellipsoid.

## Proof

**1. Positive definiteness and unrestricted uniqueness.** Connectivity and \(\sum_v g_v>0\) give
\[
 x^{\mathsf T}(L+\operatorname{diag}g)x=\sum_{\{u,v\}\in E}(x_u-x_v)^2+\sum_v g_vx_v^2>0
\]
for every nonzero real vector \(x\). The log determinant is strictly concave in the **entire gain vector**: in each nonzero direction \(d\), its second derivative is
\[
 -\operatorname{tr}\left[(M^{-1/2}\operatorname{diag}(d)M^{-1/2})^2\right]<0,
 \qquad M=L+\operatorname{diag}(g).
\]
The compact budget simplex therefore has one maximizer. Invariance under permutations within each bipartition class forces it to have two common values \(a,b\); this conclusion does not restrict the original optimization problem.

**2. Exact determinant.** On the two zero-sum subspaces within each class, \(M\) acts by \(q+a\) and \(p+b\), with multiplicities \(p-1\) and \(q-1\). The residual two-dimensional block is
\[
 \begin{pmatrix}q+a&-\sqrt{pq}\\-\sqrt{pq}&p+b\end{pmatrix}.
\]
Consequently
\[
 F(a,b)=\det M=(q+a)^{p-1}(p+b)^{q-1}\bigl((q+a)(p+b)-pq\bigr).
\]
This formula also holds for \(p=1\) or \(q=1\). Write \(b(a)=(B-pa)/(tq)\), with \(0\le a\le B/p\), and \(D(a)=(q+a)(p+b(a))-pq\). Strict concavity makes \(f(a)=\log F(a,b(a))\) strictly concave.

**3. Both endpoint derivatives.** Direct differentiation yields
\[
 \Phi(a):=f'(a)=\frac{p-1}{q+a}-\frac{p(q-1)}{tq(p+b(a))}
 +\frac{p+b(a)-\frac{p}{tq}(q+a)}{D(a)}.
\]
With \(Q\) as above and
\[
 R(t)=p^2(B+q)t-\bigl(B^2+Bp(q+1)+p^2q\bigr),
\]
one obtains the **exact rational identities**
\[
 \Phi(0)=\frac{p Q(t)}{Bq(B+pqt)},
 \qquad
 \Phi(B/p)=\frac{R(t)}{Bt(B+pq)}.
\]
All denominators are positive. The right-endpoint derivative is nonnegative precisely for \(t\ge t_{\mathrm{hi}}\). For \(0<B<q^2\), \(Q(0)<0\) and its leading coefficient is positive, so \(Q\) has exactly one positive root. For \(B\ge q^2\), \(Q(t)>0\) at every \(t>0\): all coefficients are nonnegative, and the positive linear and quadratic coefficients are strict because \(p\ge q\ge1\). Hence \(\Phi(0)\le0\) precisely for \(0<t\le t_{\mathrm{lo}}\) in the low-budget regime.

Strict concavity implies \(\Phi(0)>\Phi(B/p)\); at the low-price boundary \(\Phi(0)=0\) the right derivative is strictly negative, proving \(t_{\mathrm{lo}}<t_{\mathrm{hi}}\). If the left derivative is nonpositive, the unique maximum is the left endpoint; if the right derivative is nonnegative, it is the right endpoint. Otherwise strict monotonicity of \(\Phi\) provides one and only one interior stationary point, and that point is the global maximum. All threshold equalities are included by strict concavity, so no additional optimizer appears at a boundary.

**4. Equal-price corollary.** Exact factorization at \(t=1\) gives
\[
 Q(1)=B\bigl(B+q(p+1-q)\bigr)>0,
 \qquad R(1)=B\bigl(p(p-q-1)-B\bigr).
\]
The first class therefore always receives positive gain at equal prices. The second class is ungrounded if and only if \(p\ge q+2\) and \(B\le p(p-q-1)\). This completes the proof.

## Verification

The standalone `VERIFY.py` reproduces symbolic endpoint-derivative identities, the equal-price factorization, exact full-matrix determinants for small \(p,q\), and a broad deterministic grid of independent direct-matrix and numerical optimization checks. Run `python VERIFY.py` in an environment with Python, SymPy, NumPy and SciPy. The program returned `PASS: 6682 symbolic, matrix, and finite optimization checks`. The proof of the infinite parameter family is the symbolic argument above, not the finite grid.

For example, \((p,q,B)=(4,2,1)\) gives
\[
 t_{\mathrm{lo}}=\frac{3+\sqrt{57}}{16}\approx0.6593646522,
 \qquad t_{\mathrm{hi}}=\frac{15}{16}.
\]
At price \(t=4/5\), the unique optimum has \(a_*\approx0.1205041474\) and \(b_*\approx0.3237396315\), with determinant approximately \(48.17353716\), versus \(46.25\) and \(45.5625\) for the two endpoint allocations.

## Relationship to prior work

Chebotarev and Shamis established matrix-forest determinant identities, which underlie the rooted-forest interpretation. Joshi and Boyd developed general convex D-optimal sensor-selection and experiment-design techniques. Khosoussi, Sukhatme, Huang and Dissanayake studied log-determinant weighted-spanning-tree optimization under edge-selection constraints. The present model can be encoded as adding edges to a virtual ground vertex, so these frameworks explain the concavity and computability of the problem; they do **not themselves supply the explicit two-price-boundary classification** for arbitrary \(K_{p,q}\), including the small-budget activation cutoff. Zhou and collaborators optimize a slowest-eigenvalue pinning-speed objective rather than this determinant objective.

The theorem is also distinct from trace-inverse (A-optimal) grounding designs on the same bipartite graph: a trace-inverse support transition cannot be substituted for the log-determinant transition. An algebraically equivalent classification in unindexed work remains possible.

## Limitations

The graph has unit bipartite edge conductances and two uniform cost levels, although gains are independently adjustable. The theorem does not classify arbitrary graphs, arbitrary vertexwise prices, or discrete zero-one selection. The interior allocation is specified by a unique scalar root rather than a simple radical expression. This is a self-contained analytic result with computational cross-checks, not an independent external certification. Literature searches cannot establish absolute novelty; an unindexed equivalent formula would weaken the originality claim.

## References

1. P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575, first publicly posted 25 February 2006, Theorems 5–7. https://arxiv.org/abs/math/0602575
2. S. Joshi and S. Boyd, *Sensor Selection via Convex Optimization*, IEEE Transactions on Signal Processing 57 (2009), 451–462, DOI:10.1109/TSP.2008.2007095. https://web.stanford.edu/~boyd/papers/pdf/sensor_selection.pdf
3. K. Khosoussi, G. S. Sukhatme, S. Huang, G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, first publicly posted 5 April 2016. https://arxiv.org/abs/1604.01116
4. M.-Y. Zhou et al., *Enhancing speed of pinning synchronizability: low-degree nodes with high feedback gains*, Scientific Reports 5, 17459 (2015), DOI:10.1038/srep17459. https://www.nature.com/articles/srep17459
