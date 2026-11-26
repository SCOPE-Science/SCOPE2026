# Sharp amplification tail for random three-node quadratic quadrature

## Finding

Let \(x<y<z\) be the order statistics of three independent uniform draws from \([0,1]\). Let \(W_x,W_y,W_z\) be the unique quadrature weights exact for polynomials of degree at most two with respect to Lebesgue measure on \([0,1]\). The operator norm on the three sampled values with the sup norm is \(L=|W_x|+|W_y|+|W_z|\). Then
\[
\lim_{t\to\infty}\frac{t}{\log t}\Pr(L>t)=2.
\]
In particular, for real \(q>0\), \(\mathbb E L^q<\infty\) if and only if \(q<1\). For any fixed \(\delta>0\), the portion of the tail with at least one adjacent spacing at least \(\delta\) is \(O_\delta(t^{-1})\); thus the coefficient at logarithmic order comes from simultaneous smallness of both spacings.

## Assumptions and scope

The nodes are almost surely distinct, so the quadratic Vandermonde system is invertible. The result uses independent uniform nodes, the unmodified interpolatory rule, and exact real arithmetic. It quantifies amplification of bounded perturbations of the sampled values, not error for a specified integrand or conditioning of the entire Vandermonde solve.

## Proof

Define \(F(a,b)=ab-(a+b)/2+1/3\) and \(g(a)=F(a,a)=a^2-a+1/3\). Integrating the Lagrange cardinal polynomials gives
\[
W_x=\frac{F(y,z)}{(x-y)(x-z)},\quad
W_y=\frac{F(x,z)}{(y-x)(y-z)},\quad
W_z=\frac{F(x,y)}{(z-x)(z-y)}.
\]
Their sum is one by exactness on constants. The norm formula follows from the triangle inequality, with equality on data given by the signs of the weights.

Set \(p=y-x\), \(r=z-y\). The joint density of \((x,p,r)\) is six on the simplex \(x,p,r>0\), \(x+p+r<1\). Fix \(0<\delta<1/24\). When \(p,r<\delta\), each weight numerator is positive: \(F(a,b)=g(a)+(b-a)(a-1/2)\), \(g(a)\ge1/12\), and the three node differences are at most \(2\delta\). Only the middle weight is negative there; hence
\[
L=1+\frac{2F(x,x+p+r)}{pr},\qquad |F(x,x+p+r)-g(x)|\le\delta.
\]
For \(0<\varepsilon<\delta^2\), integration first in \(r\) gives
\[
\operatorname{area}\{(p,r)\in(0,\delta)^2:pr<\varepsilon\}
=\varepsilon\left(1+\log\frac{\delta^2}{\varepsilon}\right).
\]
For an upper bound within the spacing square, use \(0\le x\le1\) and this identity with \(\varepsilon=2(g(x)+\delta)/(t-1)\). For a lower bound use \(0\le x\le1-2\delta\), which makes the entire spacing square feasible, and \(\varepsilon=2(g(x)-\delta)/(t-1)\). For fixed \(\delta\), both thresholds are positive and less than \(\delta^2\) for all sufficiently large \(t\), uniformly in \(x\). After multiplication by \(t/\log t\), the resulting lower and upper bounds tend respectively to \(12\int_0^{1-2\delta}(g(x)-\delta)\,dx\) and \(12\int_0^1(g(x)+\delta)\,dx\). This follows uniformly from the area identity because the numerators of the thresholds are bounded above and bounded away from zero.

Outside the spacing square, if \(p\ge\delta\) then the bounded numerators and the three weight denominators give \(L\le C_\delta(1+1/r)\) for a finite constant \(C_\delta\). Thus the event \(L>t\) forces \(r=O_\delta(1/t)\), and bounded joint density on a bounded domain gives probability \(O_\delta(t^{-1})\). Interchanging the spacings handles \(r\ge\delta\). Letting \(\delta\downarrow0\) in the bounds leaves \(12\int_0^1g(x)\,dx=2\). Finally \(q\int_0^\infty t^{q-1}\Pr(L>t)\,dt\) converges at infinity exactly for \(q<1\); it is finite near zero for all \(q>0\). This proves the moment assertion.

## Relationship to prior work

The three-node sign partition is not claimed here. In *Exact random-node feasibility and a two-mechanism phase transition for positive quadratic quadrature* (Resultary record `03159ea86990`), the two disjoint feasibility obstructions and their exact densities specialize to the middle-negative and either-endpoint-negative events after mapping the interval affinely to \([-1,1]\) and using target second moment \(1/3\). The same work gives the all-positive probability.

Van den Bos et al. (arXiv:1809.09842) construct positive quadrature rules by selecting or reweighting sampled points. Such constructions are different from the square, unmodified interpolatory rule considered here. The nearby Resultary record *A logarithmic collision tail for three-node random quadratic interpolation* (`31e79eafd4fb`) addresses the Euclidean norm of fixed-point interpolation weights. Integrating the signed weight vector over evaluation points and then taking its \(\ell^1\) norm does not transfer that fixed-point probability law to quadrature. The claim here is the leading tail constant for the quadrature norm and its moment threshold, not a new conditioning measure or a novelty claim for the collision-area calculation itself.

## Reproducibility and limitations

The proof uses an explicit planar area calculation and the exact integral \(\int_0^1(x^2-x+1/3)\,dx=1/6\); no simulation is needed to establish the limit. It does not identify higher-order tail terms, other node laws or counts, or the error of quadrature on any fixed smooth function. Historical priority is limited to the sources compared.
