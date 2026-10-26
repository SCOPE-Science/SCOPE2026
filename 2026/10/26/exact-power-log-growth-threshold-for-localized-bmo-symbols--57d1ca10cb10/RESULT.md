# Exact power-log growth threshold for localized BMO symbols

## Finding

For \(L_\alpha=-\Delta+|x|^{2\alpha}\) on \(\mathbb R^n\), \(n\ge3\) and \(\alpha>0\), the critical radius satisfies \(\rho_\alpha(x)\asymp(1+|x|)^{-\alpha}\) and \(i(\rho_\alpha)=\alpha\). For \(0<\theta<1/(1+\alpha)\), \(\gamma>0\), and \(\beta\in\mathbb R\), the symbol
\[
b_{\gamma,\beta}(x)=(1+|x|)^\gamma[\log(e+|x|)]^\beta
\]
belongs to \(\mathrm{BMO}^{\log}_{\rho_\alpha,\theta}(\mathbb R^n)\) if and only if \(\gamma<\theta\), or \(\gamma=\theta\) and \(\beta\le0\). In this membership region, the endpoint theorem of Bui, Duong, and Ky gives boundedness of \([b_{\gamma,\beta},R_j^{L_\alpha}]\) on \(H_{L_\alpha}^1(\mathbb R^n)\), where \(R_j^{L_\alpha}=\partial_jL_\alpha^{-1/2}\). The statement does not assert failure of commutator boundedness outside this class.

## Assumptions and scope

Fix \(n\ge3\), \(\alpha>0\), \(L_\alpha=-\Delta+V_\alpha\), and \(V_\alpha(x)=|x|^{2\alpha}\). Also fix \(0<\theta<1/(1+\alpha)\), \(\gamma>0\), and \(\beta\in\mathbb R\). Define the critical radius by
\[
\rho_\alpha(x)=\sup\left\{r>0:r^2\frac{1}{|B(x,r)|}\int_{B(x,r)}|y|^{2\alpha}\,dy\le1\right\}.
\]
Comparable normalizations of this radius give equivalent membership conditions. Write
\[
\operatorname{MO}(b,B)=\frac1{|B|}\int_B|b-b_B|\,dx,\qquad
b_B=\frac1{|B|}\int_B b\,dx.
\]
The logarithmic localized mean-oscillation class is defined by finiteness of
\[
\sup_{B(x,r)}
\frac{\log(e+\rho_\alpha(x)/r)}{(1+r/\rho_\alpha(x))^\theta}
\operatorname{MO}(b,B(x,r)).
\]
The result classifies this specific radial symbol family for the power-potential family \(V_\alpha\); it does not characterize all symbols in the space.

## Proof

For every ball \(B(x,r)\), scaling and translation give
\[
\frac1{|B(x,r)|}\int_{B(x,r)}|y|^{2\alpha}\,dy
\asymp (|x|+r)^{2\alpha},
\]
with constants depending only on \(n\) and \(\alpha\). Thus the defining condition for \(\rho_\alpha\) is equivalent, up to constants, to
\(r^2(|x|+r)^{2\alpha}\lesssim1\), yielding
\[
\rho_\alpha(x)\asymp(1+|x|)^{-\alpha}.
\]

The admissibility index is \(i(\rho_\alpha)=\alpha\). The admissibility inequality holds with exponent \(\alpha\): using \(\rho_\alpha(y)\asymp(1+|y|)^{-\alpha}\), its right-hand side is comparable to
\[
(1+|y|)^\alpha
\bigl(1+|x-y|(1+|y|)^\alpha\bigr)^\alpha,
\]
which dominates a constant multiple of \((1+|x|)^\alpha\). Conversely, setting \(y=0\) and letting \(|x|\to\infty\) forces every admissibility exponent \(k_0\) to satisfy \(k_0\ge\alpha\).

For necessity, let \(B_R=B(0,R)\). Since \(\gamma>0\), scaling the radial integral, or comparing an inner ball with an outer annulus, gives
\[
\operatorname{MO}(b_{\gamma,\beta},B_R)\asymp
R^\gamma(\log R)^\beta\qquad(R\to\infty).
\]
Also \(\rho_\alpha(0)\asymp1\), so the logarithmic numerator in the class norm is bounded above and below by positive constants for \(R\ge1\), while the denominator is comparable to \(R^\theta\). The class norm can therefore be finite only if
\[
R^{\gamma-\theta}(\log R)^\beta=O(1).
\]
This is equivalent to \(\gamma<\theta\), or \(\gamma=\theta\) with \(\beta\le0\).

For sufficiency, put \(R=1+|x|\) and \(L_R=\log(e+R)\). Away from a fixed bounded region,
\[
|\nabla b_{\gamma,\beta}(x)|\lesssim R^{\gamma-1}L_R^\beta.
\]
Split balls into three ranges.

If \(r\le\rho_\alpha(x)\asymp R^{-\alpha}\), the gradient estimate and
\(r\log(e+\rho_\alpha(x)/r)\lesssim\rho_\alpha(x)\) bound the weighted oscillation by
\(C R^{\gamma-1-\alpha}L_R^\beta\), which is bounded because
\(\gamma\le\theta<1/(1+\alpha)<1+\alpha\).

If \(\rho_\alpha(x)\le r\le R/2\), then
\(\operatorname{MO}(b,B(x,r))\lesssim rR^{\gamma-1}L_R^\beta\). The logarithmic factor is bounded in this range and \(1+r/\rho_\alpha(x)\gtrsim rR^\alpha\), so the class quotient is at most
\(C R^{\gamma-(1+\alpha)\theta}L_R^\beta\). This is bounded because \(\gamma\le\theta\) and \(\alpha\theta>0\).

If \(r\ge R/2\), the growth estimate gives
\(\operatorname{MO}(b,B(x,r))\lesssim r^\gamma[\log(e+r)]^\beta\). Hence the quotient is at most
\[
C R^{-\alpha\theta}r^{\gamma-\theta}[\log(e+r)]^\beta.
\]
This is bounded when \(\gamma<\theta\), for every fixed \(\beta\), and when \(\gamma=\theta\) precisely for \(\beta\le0\). Bounded-radius cases are absorbed into the constants. This proves the claimed if-and-only-if criterion.

Finally, \(V_\alpha(x)=|x|^{2\alpha}\) belongs to every reverse-Hölder class \(RH_q\), \(1<q<\infty\), because averages of \(|y|^{2\alpha q}\) and \(|y|^{2\alpha}\) over a ball are comparable to the corresponding powers of \(|x|+r\). Thus \(\tau(V_\alpha)=\infty\). The endpoint commutator theorem for stratified groups, specialized to \(\mathbb R^n\), requires
\[
0\le\theta<
\min\left\{\frac{2-n/\tau(V_\alpha)}{i(\rho_\alpha)+1},
\frac1{i(\rho_\alpha)+1}\right\}=\frac1{1+\alpha}.
\]
The membership result therefore places exactly the stated family members within the theorem's sufficient symbol class and gives the asserted boundedness on \(H_{L_\alpha}^1\).

## Verification

The critical-radius scale follows from the ball-average comparison for the power potential. The admissibility index was bounded above and below from its defining inequality. Necessity uses large centered balls; sufficiency treats small, intermediate, and large radii separately. No numerical experiment or finite computation is used as a proof. The commutator statement is an application of the cited published theorem, not a new proof of that theorem.

## Relationship to prior work

Bui, Duong, and Ky define \(\mathrm{BMO}^{\log}_{\rho,\theta}\) and prove endpoint commutator results for this class, including applications to Schrödinger Riesz transforms in their Theorem 4.2. Their full text supplies the operator implication but does not state the explicit \((\gamma,\beta,\theta)\) classification proved here. Chen and Wang study the broader localized \(\mathrm{BMO}_{\rho,\theta}\) and Lipschitz scales in the Schrödinger setting; the inspected abstract and definitions do not provide the logarithmic power-symbol threshold. The inspected literature does not state the same radial symbol family and exact logarithmic boundary. The contribution is the explicit necessary-and-sufficient growth criterion and its direct endpoint application, not a new general commutator theorem.

## Limitations

The result is restricted to \(V_\alpha(x)=|x|^{2\alpha}\), \(n\ge3\), \(\alpha>0\), \(\gamma>0\), and \(0<\theta<1/(1+\alpha)\). It does not decide whether commutators may be bounded for symbols outside \(\mathrm{BMO}^{\log}_{\rho_\alpha,\theta}\), nor does it assert that the general endpoint theorem is optimal. The exact family classification is a model-specific application of the defining oscillation norm; an unindexed prior treatment of this exact family remains a residual originality risk.

## References

1. T. A. Bui, X. T. Duong, and L. D. Ky, “Endpoint estimates for commutators of singular integral operators associated with admissible functions,” arXiv:2609.23662v1 (first public 2026-09-20), especially Definition 1.1, Theorem 1.2, and Theorem 4.2.
2. C. Chen and H. Wang, “Some characterizations of BMO and Lipschitz spaces in the Schrödinger setting,” arXiv:2311.03407v1 (first public 2023-11-06), for background on localized BMO spaces.
