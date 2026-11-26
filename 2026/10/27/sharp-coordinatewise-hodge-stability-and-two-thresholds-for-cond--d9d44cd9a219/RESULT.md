# Six rim vertices are necessary and sufficient for a weighted-wheel Hodge projection to amplify by more than two

## Finding

Consider a wheel with \(n\ge3\) rim vertices, rim conductances one, and a common spoke conductance \(t>0\). Represent each oriented edge difference \(y_e\) by the conductance-normalized coordinate \(\sqrt{c_e}y_e\). Let \(P_{n,t}\) be the Euclidean orthogonal projector onto potential-gradient flows in these coordinates. Then
\[
\bigl(\exists\,t>0:\|P_{n,t}\|_{\infty\to\infty}>2\bigr)
\quad\Longleftrightarrow\quad n\ge6.
\]
In fact all weights give a strict bound below two for \(3\le n\le5\), whereas the single weight \(t=1/4\) gives a norm above two for every \(n\ge6\). At \(n=6,t=1/4\) the norm equals \(2292/1105\).

## Assumptions and scope

The graph is finite and simple. The norm measures perturbations in the stated normalized coordinates, not on raw edge differences. Orientations may be arbitrary: flipping an orientation conjugates the projector by a coordinate sign change. The threshold concerns whether amplification above two is possible at a given size as the common spoke conductance is varied; it does not locate the optimal conductance or classify the amplifying weights at each size.

## Proof

Use the published exact row-sum formulas [1, 2]. With \(a=\sqrt{t(t+4)}\), \(r=(t+2-a)/2\in(0,1)\), \(m=\lfloor n/2\rfloor\) and \(g_j=(r^j+r^{n-j})/[a(1-r^n)]\), the norm is the larger of the rim row sum \(R_n=2(1-tg_0)+2\sqrt t(g_0-g_m)\) and the spoke row sum \(S_n=1+2\sqrt t(g_0-g_m)\).

For fixed \(t\), \(g_0\) strictly decreases with \(n\). Also
\[
a(g_0-g_m)=H(r^m,r^{n-m}),\qquad H(x,y)=\frac{(1-x)(1-y)}{1-xy}.
\]
On \((0,1)^2\), \(H<1\) and \(\partial_xH=-(1-y)^2/(1-xy)^2<0\), with the symmetric formula for \(\partial_yH\). Increasing \(n\) increments one exponent, so \(g_0-g_m\) strictly increases. Hence \(R_n\) strictly increases with \(n\), whereas \(S_n<1+2/\sqrt{t+4}<2\) for all \(n,t\).

It remains to show that \(R_5<2\) for all \(t>0\) and to find a witness for \(n=6\). Put \(u=\sqrt r\in(0,1)\), so \(\sqrt t=(1-u^2)/u\). Multiplying the inequality \(R_5<2\) by positive factors reduces it to
\[
(1-u^2)(1+u^{10})-u(1-u^4)(1-u^6)=(1-u^4)p(u)>0,
\]
where \(p(u)=1-u-u^2+u^4-u^6+u^7+u^8\). For \(0<u\le1/2\) one has \(p(u)\ge1-u-u^2-u^6\ge15/64\). For \(1/2\le u<1\), let \(v=(2u-1)/(1-u)\ge0\). Exact expansion gives
\[
(v+2)^8p\!\left(\frac{v+1}{v+2}\right)=v^8+6v^7+11v^6+v^5+v^4+89v^3+224v^2+219v+79>0.
\]
Thus \(R_5<2\). At \(n=6,t=1/4\), the periodic Green column has entries \((1188,784,576,512,576,784)/1105\), verified by \((9/4)g_j-g_{j-1}-g_{j+1}=\mathbf1_{j=0}\). Substitution gives \(R_6=2292/1105>2>S_6\). Strict monotonicity of the rim row in \(n\) completes both size comparisons.

## Verification

Run `python3 verify.py` with Python 3 to check the polynomial identities and the rational Green column and row sums with exact arithmetic. The all-weight inequality follows from the positive-coefficient certificate and the analytic comparison across sizes.

## Relationship to prior work and limitations

The exact norm, its rim–spoke crossover, its fixed-conductance large-size limit, and its global supremum are not claims of this result. They are covered by the published weighted-wheel findings [1, 2], which use either the same or reciprocal conductance ratio. Here the question is the first size where the norm can be larger than two. The crossing example alone would not show sharpness: the size-five certificate rules out **every** positive common spoke conductance for all smaller wheels. No exhaustive historical-priority claim is made.

## References

1. *Sharp endpoint Hodge stability and logarithmic contrast tuning on weighted wheel graphs*, published record `3efd9f463ccd`, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-sharp-endpoint-hodge-stability-and-logarithmic-contrast-tuning-o--3efd9f463ccd .
2. *A moving conductance threshold for sharp cut–cycle projection norms on weighted wheels*, published record `169e544dd2d8`, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-moving-conductance-threshold-for-sharp-cut-cycle-projection-no--169e544dd2d8 .
