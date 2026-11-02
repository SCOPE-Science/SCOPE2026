# A single diagonal obstruction and a uniform high-degree law for sixth-order Gauss positivity on bicliques

## Finding

Consider sixth-order Gauss–Legendre time stepping of graph diffusion on a uniformly weighted complete bipartite network. For every pair of positive integers \(p\le q\) with \(p+q\ge3\), there is exactly one finite step-size cutoff. **Every off-diagonal entry stays strictly positive at every positive step size; only diagonal entries can obstruct positivity.** At the cutoff the diagonal of the smaller vertex class is zero, and beyond it those diagonals are negative. The cutoff is the unique root of an explicit scalar rational equation. Moreover, its product with the maximum vertex degree tends uniformly to a universal constant, independently of the ratio of the two class sizes.

Precisely, let \(K_{p,q}\) have unit-edge graph Laplacian \(L\), let each edge have conductance \(c>0\), and define
\[
 r(z)=\frac{120-60z+12z^2-z^3}{120+60z+12z^2+z^3},\qquad P(h)=r(chL).
\]
The matrix \(P(h)\) is the sixth-order three-stage Gauss–Legendre, or \([3/3]\) Padé, endpoint update for \(\dot u=-cLu\). Put \(N=p+q\). Define
\[
 F_{p,q}(s)=\frac1N+\frac{p-1}{p}r(qs)+\frac{q}{pN}r(Ns).
\]
There is a unique \(s_{p,q}>0\) with \(F_{p,q}(s_{p,q})=0\), and
\[
 P(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le \frac{s_{p,q}}c.
\]
If \(p<q\), only the diagonal entries at the \(p\) vertices of the smaller class first become zero. If \(p=q\), all diagonal entries reach zero simultaneously. All off-diagonal entries are strictly positive for every \(h>0\), including beyond the positivity horizon. In the exceptional two-vertex case \(p=q=1\), \(P(h)\) is strictly positive for all finite \(h>0\).

Let \(z_0\) be the unique positive root of \(120-60z+12z^2-z^3=0\) (numerically \(z_0\approx4.64437070925217\)). Uniformly over integers \(1\le p\le q\), as \(q\to\infty\),
\[
 cq\,\frac{s_{p,q}}c=q s_{p,q}=z_0+O(q^{-1}),\qquad
 h_{p,q}=\frac{z_0+O(q^{-1})}{cq}.
\]
Thus the sharp step restriction is asymptotically \(z_0\) divided by the maximum continuous-time exit rate \(cq\), uniformly from stars through balanced bicliques.

## Assumptions and scope

All graphs are finite, undirected, and complete bipartite with two nonempty classes. Edges have one common strictly positive conductance \(c\). The update is the endpoint matrix of the three-stage Gauss–Legendre method for the autonomous linear system \(\dot u=-cLu\), not positivity of its internal stage vectors or of arbitrarily perturbed graphs. Entrywise nonnegativity means every entry of \(P(h)\) is nonnegative. There is no killing term, so the zero Laplacian eigenvalue is retained and all row sums of the update equal one. The graph sizes \(p,q\) are positive integers and, except where specified, \(p+q\ge3\).

## Proof

**1. Scalar monotonicity.** Set \(D(z)=z^3+12z^2+60z+120\). Direct differentiation gives
\[
 r'(z)=-\frac{24(z^4-30z^2+600)}{D(z)^2}
 =-\frac{24((z^2-15)^2+375)}{D(z)^2}<0
 \quad(z\ge0).
\]
Also define the divided decrement
\[
 \phi(z)=\frac{1-r(z)}z=\frac{2(z^2+60)}{D(z)}\quad(z>0).
\]
Another exact differentiation yields
\[
 \phi'(z)=-\frac{2(z^4+120z^2+1200z+3600)}{D(z)^2}<0.
\]
Therefore \(r\) strictly decreases from \(1\) to \(-1\), and \(\phi\) strictly decreases on positive arguments. Since the scalar Padé denominator has strictly positive coefficients, its spectral evaluation at \(chL\) is everywhere well defined for \(h\ge0\).

**2. Complete spectral decomposition.** Write \(s=ch\). The eigenvalues of \(L\) are \(0\) (once), \(q\) (with multiplicity \(p-1\)), \(p\) (with multiplicity \(q-1\)), and \(N\) (once). Let \(A\) denote the class of size \(p\) and \(B\) the class of size \(q\). Their update diagonal entries are respectively
\[
 F_{p,q}(s)=\frac1N+\frac{q}{pN}r(Ns)+\frac{p-1}{p}r(qs),
\quad G_{p,q}(s)=\frac1N+\frac{p}{qN}r(Ns)+\frac{q-1}{q}r(ps).
\]
For two distinct vertices in \(A\), the entry equals
\[
 \frac1N+\frac{q}{pN}r(Ns)-\frac1p r(qs)
 =\frac{sq}{p}\,[\phi(qs)-\phi(Ns)]>0.
\]
For two distinct vertices in \(B\), it equals
\[
 \frac1N+\frac{p}{qN}r(Ns)-\frac1q r(ps)
 =\frac{sp}{q}\,[\phi(ps)-\phi(Ns)]>0.
\]
For vertices in opposite classes, the entry is \([1-r(Ns)]/N>0\). These identities apply to existing vertex pairs; when a class has one vertex there is no within-class off-diagonal pair. They establish strict positivity of all off-diagonal entries whenever \(s>0\).

**3. Identify the unique first failing diagonal.** Since \(r\) strictly decreases, both \(F_{p,q}\) and \(G_{p,q}\) strictly decrease on \((0,\infty)\); their nonconstant spectral weights are positive. Each equals \(1\) at zero and tends to \(2/N-1<0\) at infinity, so each has one simple positive zero. For \(p\le q\), the exact identity
\[
 G_{p,q}(s)-F_{p,q}(s)
 =\frac{q-1}{q}[r(ps)-r(qs)]
 +\frac{q-p}{pq}[r(qs)-r(Ns)]\ge0
\]
holds for every \(s\ge0\), with strict inequality when \(p<q\) and \(s>0\). Thus \(F_{p,q}\) reaches zero first, at the unique \(s_{p,q}\) above, and its sign alone determines the complete entrywise-positivity interval. The endpoint matrix always has row sum one because \(r(0)=1\). For \(K_{1,1}\), the diagonals are \([1+r(2s)]/2>0\) and the off-diagonals are \([1-r(2s)]/2>0\) for every finite \(s>0\), explaining the exception.

**4. Uniform high-degree law.** Put \(t=qs\). For each compact \(0\le t\le T\), write the exact identity
\[
 F_{p,q}(t/q)-r(t)=\frac{1-r(t)}N
 +\frac{q}{pN}\left[r\left(t\left(1+\frac pq\right)\right)-r(t)\right].
\]
The first term has magnitude at most \(2/N\). By the mean value theorem, the second has magnitude at most \(tM_T/N\), with \(M_T=\max_{0\le z\le2T}|r'(z)|\), uniformly for \(1\le p\le q\). Hence \(F_{p,q}(t/q)=r(t)+O(1/q)\) uniformly in both \(p\) and \(t\) on each compact interval. The strictly decreasing \(r\) crosses zero once at \(z_0\). Bracketing the unique zero of \(F_{p,q}\), then using \(r'(z_0)<0\), gives \(qs_{p,q}=z_0+O(1/q)\) uniformly in \(1\le p\le q\). This completes the proof.

## Verification

The accompanying `verify.py` independently builds Laplacians and their rational matrix functions from the full matrices, rather than using the spectral formulas to generate test matrices. It checks three scalar symbolic identities, \(4100\) exact rational matrix entries over \(K_{p,q}\) with \(1\le p\le5\), \(p\le q\le6\) and four rational timestep values, and \(310\) floating-point positivity-horizon cases over larger bicliques, plus representative uniform-scaling checks. The exact algebraic proof, not the finite tests, establishes the result for all admissible orders and all real timesteps.

For a concrete numerical instance, \(K_{2,3}\) with unit conductance has \(s_{2,3}\approx4.6757919618411\). The cutoff is unique, and the next larger step makes precisely the smaller-class diagonal entries negative first.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland, and Shorten (2010, full accessible conference paper) establish general sufficient criteria and demonstrate that diagonal Padé methods need not preserve positivity. Their Theorem 3 is a sufficient condition on matrix entries, not an exact positivity interval for \([3/3]\) stepping on the present graph family. Their extended treatment in *Essentially Negative News About Positive Systems* (preprint deposited 2012; especially the positivity section and Theorem 3) likewise gives general positivity conditions and counterexamples, not this classification. Wade (2004) studies positivity-preserving Padé-based smoothing schemes for parabolic problems; its abstract does not assert the biclique result, but its full text was not available in the inspected sources, leaving a limited historical coverage risk. These works provide the relevant established framework rather than the stated cutoff. The theorem also differs from the known fourth-order \([2/2]\) Padé positivity results: the rational update, its high-step limit and its obstruction are different.

## Limitations

The theorem concerns uniform-edge undirected bicliques, the \([3/3]\) endpoint update and entrywise positivity, not higher stages, nonuniform conductances, directed generators, or arbitrary graph families. The asymptotic error term is uniform over integer bipartition sizes but only for this graph class. Source comparisons do not establish publication priority; additional specialized earlier literature may contain equivalent formulations. No independent mathematical review has been carried out.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” *19th International Symposium on Mathematical Theory of Networks and Systems* (2010), accessible manuscript deposited October 15, 2010: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf.
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially Negative News About Positive Systems,” preprint deposited June 19, 2012 (later journal version *Linear Algebra and its Applications* 436 (2012), 3425–3442): https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
3. B. A. Wade, “Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data,” *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573, first published online September 29, 2004: https://doi.org/10.1002/num.20039.
4. MSC2020 numerical ODE classification 65L06, “Multistep, Runge-Kutta and extrapolation methods”: https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=65-00.
