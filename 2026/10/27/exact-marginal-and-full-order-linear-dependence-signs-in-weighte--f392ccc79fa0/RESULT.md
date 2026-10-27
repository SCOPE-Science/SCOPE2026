# Exact marginal and full-order linear dependence signs in weighted edge covers of \(K_{2,n}\)

## Finding
For every integer \(n\ge2\) and every real \(0<p<1\), independently retain each of the \(2n\) edges of \(K_{2,n}\) with probability \(p\), and condition on the retained edges covering all \(n+2\) vertices. Let \(X_{rj}\) indicate retention of the edge from the left vertex \(r\in\{1,2\}\) to right vertex \(j\in\{1,\ldots,n\}\). Let \(\Sigma=\operatorname{Cov}((X_{rj})_{r,j})\) and \(Q=\Sigma^{-1}\).

**Complete sign law.** The covariance matrix is positive definite. For any two *distinct* edge indicators, their marginal covariance and their full-order *linear partial correlation* \(-Q_{ef}/\sqrt{Q_{ee}Q_{ff}}\) are strictly negative when the edges share an endpoint, and strictly positive when they are vertex-disjoint. There are no zero cases in the stated domain.

All covariance and precision entries have the following closed forms. Define
\[
 t=\frac{1-p}{2-p},\quad h=t^n,\quad z=1-2h,\quad u=1-2t,\quad A=t-nh,\quad B=A+2(n-1)th.
\]
All of \(t,h,z,u,A,B\) are strictly positive. Write \(\mu=(1-t-h)/z\). Then every diagonal covariance entry equals \(v=\mu(1-\mu)\); the three distinct-edge covariance entries are
\[
 a=-\frac{(t-h)^2}{z^2}\quad (\text{same right endpoint}),\qquad
 b=\frac{h\{h-(1-2t+2t^2)\}}{z^2}\quad (\text{same left endpoint}),
\]
\[
 c=\frac{h\{2t(1-t)-h\}}{z^2}\quad (\text{vertex-disjoint}).
\]
The corresponding distinct-edge entries of \(Q\) are
\[
 q_a=z\left(\frac1u-\frac{(n-1)h^2}{AB}\right),\qquad
 q_b=\frac{zh}{2t}\left(\frac1A+\frac1B\right),\qquad
 q_c=-\frac{z(n-1)h^2}{AB},
\]
and every diagonal precision entry is
\[
 q_0=\frac{z}{2t}\left(1+\frac1u\right)
       +\frac{zh}{2t}\left(\frac1A+\frac1B\right).
\]
In particular, \(a<0,b<0,c>0\) while \(q_a>0,q_b>0,q_c<0\), which proves both sign statements.

## Assumptions and scope
The retained edge set is weighted by \(p^{|S|}(1-p)^{2n-|S|}\) before conditioning on being an edge cover; equivalently, conditional weights are proportional to fugacity \(\lambda^{|S|}\), \(\lambda=p/(1-p)>0\). Isolated vertices are forbidden, but cycles and disconnected covering subgraphs are allowed. Here 'linear partial correlation' means the correlation between least-squares residuals after projection on the linear span of all the other edge indicators; it is **not** conditional independence or nonlinear partial correlation. The theorem covers every \(n\ge2\) and every finite positive fugacity. The limiting deterministic regimes \(p=0\) and \(p=1\) are excluded.

## Proof
**Step 1: independent columns and row exclusions.** Initially condition only on each right vertex having positive degree. The \(n\) resulting columns are independent, with possible local states \((1,0),(0,1),(1,1)\) having respective probabilities \(t,t,u\), where \(t=(1-p)/(2-p)\) and \(u=1-2t\). The two remaining forbidden events are the all-\((1,0)\) and all-\((0,1)\) configurations, each of probability \(h=t^n\). They are disjoint, so their complement has probability \(z=1-2h>0\). Every required edge cover is obtained by imposing this final conditioning.

**Step 2: the moment formulas.** The conditional one-edge probability is \(\mu=(1-t-h)/z\). For two edges in the same column, the conditional joint probability is \(u/z\). For two edges in different columns but the same row it is \(((1-t)^2-h)/z\). For two edges in different columns and different rows it is \((1-t)^2/z\). Subtracting \(\mu^2\) in these three cases and simplifying yields \(a,b,c\) as stated. Since \(0<t<1/2\) and \(0<h\le t^2\), we have \(t-h>0\), \(1-2t+2t^2-h>0\), and \(2t(1-t)-h>0\). Therefore \(a<0,b<0,c>0\).

**Step 3: four exact covariance eigenvalues.** In column \(j\), transform to symmetric and antisymmetric coordinates \((X_{1j}+X_{2j})/\sqrt2\) and \((X_{1j}-X_{2j})/\sqrt2\). On each of the two resulting \(n\)-dimensional spaces the covariance is an exchangeable matrix. Decompose each into the constant-vector line and its \(n-1\)-dimensional orthogonal complement. The respective eigenvalues, by inserting the four moment types from Step 2 and simplifying, are
\[
 \lambda_{+,0}=\frac{uB}{z^2},\qquad
 \lambda_{+,1}=\frac{ut}{z},\qquad
 \lambda_{-,0}=\frac{A}{z},\qquad
 \lambda_{-,1}=\frac{t}{z}.
\]
For \(n\ge2\), \(n t^{n-1}<1\): indeed \(t<1/2\) and \(n/2^{n-1}\le1\), with strictness at \(t<1/2\). Hence \(A=t(1-nt^{n-1})>0\), and \(B>A>0\). Every eigenvalue is positive, proving \(\Sigma\succ0\).

**Step 4: exact precision and strict signs.** Invert the four eigenvalues. A symmetric-column or antisymmetric-column precision block has diagonal equal to \(1/\lambda_{\pm,1}+(1/\lambda_{\pm,0}-1/\lambda_{\pm,1})/n\), and off-diagonal equal to \((1/\lambda_{\pm,0}-1/\lambda_{\pm,1})/n\). The off-diagonal constants simplify respectively to
\[
 \beta_+=\frac{zh}{tB},\qquad \beta_-=\frac{zh}{tA}.
\]
Undoing the orthogonal row transformation yields exactly \(q_0,q_a,q_b,q_c\) in the Finding. All terms in \(q_b\) are positive and \(q_c<0\). To prove \(q_a>0\), compute
\[
 AB-(n-1)uh^2=A^2+(n-1)h\{2tA-uh\}.
\]
The bracket is strictly positive because
\[
 2tA-uh=t^2\left[2-t^{n-2}\{1+2(n-1)t\}\right]>0.
\]
For \(n=2\), the expression subtracted from \(2\) is \(1+2t<2\); for \(n\ge3\), it is at most \(n/2^{n-2}\le3/2<2\). Thus \(AB>(n-1)uh^2\), and \(q_a=z(AB-(n-1)uh^2)/(uAB)>0\). Finally, because \(Q_{ee}=q_0>0\), the full-order linear partial correlation \(-Q_{ef}/q_0\) has precisely the asserted sign. This completes the proof.

## Verification
The standard-library checker `checker.py` independently enumerates all \(2^{2n}\) labeled edge subsets for \(2\le n\le6\), filters exact covers, and uses exact rational weights at \(p\in\{1/5,1/2,4/5\}\). It reconstructs each covariance entry directly and checks every entry of the claimed inverse by exact matrix multiplication. In the completed run it passed 2250 exact assertions (`EXACT_OK assertions=2250`). These finite checks do not certify infinitely many cases; the all-parameter claims follow from Steps 1–4.

## Relationship to prior work
The weighted-edge-cover Gibbs model and its sampling problem are established in Chen–Liu–Vigoda (2021), Eppstein–Frishberg (2021), and Chen–Gu (2023). Their results concern zero-free regions, spectral independence, or Glauber-chain mixing, not this explicit exact covariance/precision sign classification for the unbounded-degree family \(K_{2,n}\). In particular, an influence/spectral norm bound does not imply signs of individual entries of the inverse covariance matrix. The occupied-box precision sign theorem for iid occupancy indicators concerns a different conditioning event and different variables; neither assertion is an immediate specialization of the other. The present closed moments and inverse are derived independently by direct column conditioning and orthogonal decomposition; no sampling theorem is treated as a new result.

## Limitations
This is a finite-graph, weighted-edge-cover result specialized to one part of size two. It does not prove conditional independence, positive/negative association for all increasing observables, or any corresponding sign law for \(K_{m,n}\) with \(m\ge3\) or for arbitrary graphs. The claim includes no previously unreported priority guarantee: an earlier application of known edge-cover partition functions or general correlation identities might yield the same formulas. No independent mathematical audit has been performed.

## References
1. Z. Chen, K. Liu, and E. Vigoda, *Spectral Independence via Stability and Applications to Holant-Type Problems*, arXiv:2106.03366, first public 2021-06-07, https://arxiv.org/abs/2106.03366 .
2. D. Eppstein and D. Frishberg, *Rapid mixing for the hardcore Glauber dynamics and other Markov chains in bounded-treewidth graphs*, arXiv:2111.03898, first public 2021-11-06, https://arxiv.org/abs/2111.03898 .
3. Z. Chen and Y. Gu, *Fast Sampling of b-Matchings and b-Edge Covers*, arXiv:2304.14289, first public 2023-04-27, https://arxiv.org/abs/2304.14289 .
