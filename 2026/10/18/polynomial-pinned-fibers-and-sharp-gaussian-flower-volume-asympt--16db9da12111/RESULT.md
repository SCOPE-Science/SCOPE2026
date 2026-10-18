# Polynomial pinned fibers and sharp Gaussian flower-volume asymptotics for Boolean quadric cycle polytopes

## Finding
For every integer \(\ell\ge3\), the pinned-coordinate fiber-volume function of the Boolean quadric polytope of a cycle is an **even polynomial of degree at most \(2\ell-2\)** on its entire domain, despite the non-polynomial pieces in the corresponding relaxation and missing-volume fibers. In particular, exact expressions below determine the full pinned fiber, not only its central value. For a flower graph consisting of \(k\) copies of this cycle meeting at precisely one vertex, the exact-to-relaxation volume ratio has the sharp asymptotic
\[
\frac{\operatorname{vol}(P(F_{k,\ell}))}{\operatorname{vol}(Q(F_{k,\ell}))}
=\rho_\ell^k\sqrt{\frac{b_{Q,\ell}}{b_{P,\ell}}}\left(1+O_\ell(k^{-1})\right),\quad k\to\infty.
\]
Here \(P\) is the Boolean quadric (correlation) polytope, \(Q\) is its standard edgewise McCormick relaxation, and the explicit positive constants satisfy \(0<b_{P,\ell}<b_{Q,\ell}\). The factor preceding the exponential is greater than one, and is \(\sqrt5/2\) for triangles and \(\sqrt{18/17}\) for four-cycles.

## Assumptions and scope
For a finite simple graph \(G=(V,E)\), work in the standard ambient coordinates \((x_i,y_{ij})_{i\in V,ij\in E}\), with
\[
P(G)=\operatorname{conv}\{(z_i,z_i z_j):z\in\{0,1\}^V\},
\]
and \(Q(G)\) defined by \(0\le x_i\le1\) and \(\max(0,x_i+x_j-1)\le y_{ij}\le\min(x_i,x_j)\) on every edge. Volumes are ordinary ambient Lebesgue coordinate volumes. Fix any vertex \(v\) of the length-\(\ell\) cycle \(C_\ell\), and write \(p_\ell(u)\), \(q_\ell(u)\) for the \((2\ell-1)\)-dimensional sections \(x_v=1/2+u\), \(-1/2\le u\le1/2\), with original remaining coordinates. Define \(d_\ell=q_\ell-p_\ell\), and
\[
\lambda_j=\bigl((j-\tfrac12)\pi\bigr)^{-2},\qquad
S_r=\sum_{j=1}^\infty\lambda_j^r
=\frac{(2^{2r}-1)\zeta(2r)}{\pi^{2r}}.
\]
For \(a=1-2|u|\) the complete fiber formulas are
\[
\boxed{q_\ell(u)=2^{1-\ell}\sum_{j=1}^\infty\lambda_j^\ell
\sin^2\bigl((j-\tfrac12)\pi a\bigr),\qquad
 d_\ell(u)=\frac{2^{-\ell}}{((\ell-1)!)^2}\int_{2|u|}^1(s^2-4u^2)^{\ell-1}\,ds.}
\]
The second formula can be evaluated as a finite sum; both expressions are interpreted continuously at the endpoints. Put \(\alpha_\ell=d_\ell(0)/q_\ell(0)\), \(\rho_\ell=1-\alpha_\ell\), and
\[
\alpha_\ell=\frac{\binom{2\ell-2}{\ell-1}}{A_{2\ell-1}},\quad
b_{Q,\ell}=4\frac{S_{\ell-1}}{S_\ell},\quad
b_{D,\ell}=\frac{4(\ell-1)(2\ell-1)}{2\ell-3},\quad
b_{P,\ell}=\frac{b_{Q,\ell}-\alpha_\ell b_{D,\ell}}{1-\alpha_\ell},
\]
where \(A_{2\ell-1}\) is the positive Euler zigzag (tangent) number, defined equivalently by \(q_\ell(0)=A_{2\ell-1}/[2^\ell(2\ell-1)!]\). No assertion is made for variable \(\ell\) as \(k\to\infty\).

## Proof
**Relaxation fiber.** Write \(t_i=x_i-1/2\), \(a_i=1-2|t_i|\), and on each edge substitute \(z_{ij}=x_i+x_j-2y_{ij}\), of Jacobian absolute value \(2\). The allowed \(z_{ij}\)-interval has length \(\min(a_i,a_j)\) in the \(z\)-coordinate. Integrating all \(y\)'s therefore contributes \(2^{-\ell}\prod_{ij\in E}\min(a_i,a_j)\). Each free change \(x_i\mapsto a_i\) has two branches of derivative magnitude \(1/2\), so contributes unit Lebesgue measure on \([0,1]\). Thus
\[
q_\ell(u)=2^{-\ell}(K^\ell)(a,a),\quad K(s,t)=\min(s,t),
\]
where the right side is the diagonal of the trace-class integral kernel. The classical Dirichlet--Neumann eigenbasis \(\sqrt2\sin((j-1/2)\pi s)\) gives the displayed series. It converges absolutely for \(\ell\ge3\).

**Excluded odd-cycle simplices.** The exact cycle inequality theorem for Boolean quadric polytopes gives one excluded simplex for each of the \(2^{\ell-1}\) odd edge-labelings; their interiors do not overlap. Boolean switching sends each labeling to the same cross-section volume, possibly reversing the sign of \(u\). In the transformed edge coordinates, set nonnegative slacks \(w_i\ge|h_i|\), with \(\sum_i w_i\le1\), and the signed cycle consistency \(\sum_i h_i=2u\). The original edge-coordinate Jacobian is \(2^{-\ell}\). Let \(a_i=(w_i+h_i)/2\ge0\), \(b_i=(w_i-h_i)/2\ge0\). The volume over these slacks is the \(2\ell\)-simplex slice satisfying \(\sum(a_i+b_i)\le1\), \(\sum(a_i-b_i)=2u\), with the induced coordinate Jacobian supplied by the cycle constraint. Integrating the two group sums by the elementary simplex formula \(\operatorname{vol}\{r_i\ge0,\sum r_i=t\}=t^{\ell-1}/(\ell-1)!\) gives precisely
\[
d_\ell(u)=\frac{2^{-\ell}}{((\ell-1)!)^2}
\int_{2|u|}^1(s^2-4u^2)^{\ell-1}\,ds.
\]
The normalization can also be independently fixed at \(u=0\), where the published central-slice formula gives \(d_\ell(0)=\binom{2\ell-2}{\ell-1}/[2^\ell(2\ell-1)!]\); the integral has exactly this value. The full formula agrees with the independently published triangle fiber \(p_3(u)=(1-4u^2)^2/96\).

**Polynomial cancellation.** Write the Fourier cosine term in the relaxation series as \(C_\ell(a)=\sum_j\lambda_j^\ell\cos((2j-1)\pi a)\). The ordinary Bernoulli-polynomial cosine series gives the *finite polynomial identity*
\[
C_\ell(a)=\frac{(-1)^{\ell+1}2^{4\ell-1}}{(2\ell)!}
\left[B_{2\ell}(a/2)-2^{-2\ell}B_{2\ell}(a)\right],
\quad q_\ell(u)=2^{-\ell}[S_\ell-C_\ell(1-2|u|)].
\]
Bernoulli symmetry makes \(B_{2\ell}(1/2-|u|)\) even, while \(B_{2\ell}(1-2|u|)\) has only one odd power, \(|u|^{2\ell-1}\). Its coefficient in \(q_\ell\) equals \((-1)^\ell\ell 2^{3\ell-2}/(2\ell)!\). Evaluating the lower endpoint in the missing-fiber integral gives exactly the same coefficient in \(d_\ell\): use \(\int_0^1(1-s^2)^{\ell-1}\,ds=2^{2\ell-1}\ell!(\ell-1)!/(2\ell)!\). Consequently \(p_\ell=q_\ell-d_\ell\) has no odd powers, and is an even polynomial in \(u\) of degree at most \(2\ell-2\). For illustration,
\[
p_3(u)=\frac{(1-4u^2)^2}{96},\qquad
p_4(u)=\frac1{320}-\frac{7u^2}{240}+\frac{u^4}{12}-\frac{u^6}{15}.
\]

**Strict quadratic peak and prefactor.** At zero, differentiation gives the constants \(b_Q,b_D,b_P\) above. The log-convexity of the positive moment sequence \((S_j)\) gives \(b_{Q,\ell}\le b_{Q,3}=10\), while \(b_{D,\ell}\ge40/3\); hence \(b_P<b_Q\). To verify \(b_P>0\), it is explicit for \(\ell=3\). For \(\ell\ge4\), \(b_Q\ge\pi^2\), whereas
\[
\alpha_\ell b_D\le\frac{\pi^{2\ell}}{8(2\ell-1)!}(4\ell+4)<\pi^2.
\]
The first bound uses \(S_\ell\ge(4/\pi^2)^\ell\) and \(\binom{2\ell-2}{\ell-1}\le4^{\ell-1}\); the strict bound holds at \(\ell=4\) and decreases thereafter by elementary consecutive ratios. Existing cycle-fiber unimodality, together with this strict quadratic behavior and polynomial analyticity, gives a unique global maximum at \(u=0\). Because flower-cycle fibers factor over their common pinned coordinate, exact volume ratio is
\[
R_{k,\ell}=\frac{\int_{-1/2}^{1/2}p_\ell(u)^k\,du}{\int_{-1/2}^{1/2}q_\ell(u)^k\,du}.
\]
Standard one-dimensional Laplace expansion around the two strictly quadratic maxima gives the displayed relative error \(O_\ell(k^{-1})\). Under normalized Lebesgue measure on either flower polytope, the scaled common coordinate \(\sqrt{k}(x_v-1/2)\) converges in distribution (indeed in total variation at the density level) to the centered normal distribution of variance \(1/(2b_{P,\ell})\) or \(1/(2b_{Q,\ell})\), respectively. This proves the associated Gaussian fluctuation assertion and the strict excess of the prefactor over one.

## Verification
Run `python CHECK.py` with SymPy installed. It checks exact Bernoulli-series conversion, cancellation of odd powers, both central-normalization identities, and the quadratic constants through multiple cycle lengths; it also independently numerically compares the sharp asymptotic to one-dimensional quadrature in the triangular case. This finite checker is supplementary; the proof of arbitrary \(\ell,k\) is the analytical argument above.

## Relationship to prior work
Jon Lee's 2026 work establishes the cycle-fiber unimodality, the general flower fiber-factorization principle, the exact central ratio \(\rho_\ell\), and the triangle's complete fiber, together with bounds containing a factor growing linearly in \(k\). The present calculation supplies the full all-\(u\) missing-slice integral, polynomiality of each exact cycle fiber, the sharp constant prefactor and the conditional central-limit law for *every fixed cycle length*. Lee and Skipper (2017) discuss exact overall volumes of sparse Boolean quadric relaxations, not the pinned-fiber polynomial and sharp flower prefactor. Jha and Nechita (2024/2025) compute fixed-all-marginals correlation-polytope volume ratios; those conditioned fibers have different variables held fixed and do not imply the volume law here.

## Limitations
The asymptotics hold for fixed cycle length \(\ell\ge3\), not a joint limit with growing \(\ell\). The standard McCormick relaxation and the ordinary Euclidean coordinate-volume normalization are essential. Published central ratios and triangle formulas are not claimed as new. A comparable result could exist under the terminology of conditional correlation polytope volumes or Brownian-kernel powers; bibliographic non-duplication is based on the inspected literature, not a proof of global priority. No independent audit has been performed.

## References
1. Jon Lee, *Exact volume computation for Boolean quadric polytopes of series-parallel graphs*, arXiv:2610.00734, first posted September 30, 2026; especially cycle-fiber results in Section 8.
2. Jon Lee and Daphne Skipper, *Volume computation for sparse Boolean quadric relaxations*, arXiv:1703.02444, 2017.
3. A. Jha and I. Nechita, *On random classical marginal problems with applications to quantum information theory*, arXiv:2406.14153, first posted June 2024; especially fixed-marginal cycle inequalities.
