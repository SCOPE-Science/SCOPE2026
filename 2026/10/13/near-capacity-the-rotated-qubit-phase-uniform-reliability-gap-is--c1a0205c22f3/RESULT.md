# Near capacity, the rotated-qubit phase-uniform reliability gap is cubic

## Finding
Fix \(0<p<1/2\). Let
\[
h(x)=-x\log x-(1-x)\log(1-x),\qquad C=h(p),\qquad A=p(1-p),\qquad L=\log\frac{1-p}{p}>0.
\]
For the rotated binary pure-state classical-quantum channel in arXiv:2610.01941v1, define \(t_R\in(0,p)\) by \(h(t_R)=R\). The source proves a phase-uniform converse with exponent
\[
U_p(R)=D(t_R\|p),
\]
and gives the channel-aware exponent
\[
E_{\mathrm{aware}}(R)=\sup_{0\le s\le1}\left\{-\log\left[(1-p)^{1+s}+p^{1+s}\right]-sR\right\}.
\]
If \(\delta=C-R\downarrow0\), then
\[
U_p(C-\delta)
=\frac{\delta^2}{2AL^2}
+\frac{(1-2p)L-3}{6A^2L^4}\,\delta^3
+O(\delta^4),
\]
while
\[
E_{\mathrm{aware}}(C-\delta)
=\frac{\delta^2}{2AL^2}
+\frac{1-2p}{6A^2L^3}\,\delta^3
+O(\delta^4).
\]
Consequently,
\[
\boxed{E_{\mathrm{aware}}(C-\delta)-U_p(C-\delta)
=\frac{\delta^3}{2A^2L^4}+O(\delta^4)}.
\]
In particular, the two exponents agree through quadratic order and the strict separation proved in the source first appears at cubic order near capacity. Equivalently,
\[
\frac{E_{\mathrm{aware}}(C-\delta)-U_p(C-\delta)}{E_{\mathrm{aware}}(C-\delta)}
=\frac{\delta}{AL^2}+O(\delta^2).
\]

## Assumptions and scope
The parameter \(p\) is fixed in \((0,1/2)\), all logarithms are natural, and \(R<C=h(p)\) approaches capacity from below. Because \(h\) is strictly increasing on \((0,1/2)\), the equation \(h(t_R)=R\) has a unique solution \(t_R\in(0,p)\). The source's proof of its uniform-phase no-go bound retains binomial weights with entropy below \(R\) and then approaches the boundary \(h(t_R)=R\), yielding \(D(t_R\|p)\). The claim concerns this explicit source converse and the source's channel-aware exponent. It does not claim a new coding construction, a low-rate formula, or a uniform expansion as \(p\to0\) or \(p\to1/2\).

## Proof
Put \(u=p-t_R\). Taylor expansion at \(p\) gives
\[
C-R=h(p)-h(p-u)
=Lu+\frac{u^2}{2A}+\frac{1-2p}{6A^2}u^3+O(u^4),
\]
and
\[
D(p-u\|p)
=\frac{u^2}{2A}+\frac{1-2p}{6A^2}u^3+O(u^4).
\]
Reversion of the first series through the order needed for a cubic expansion, followed by substitution into the second, yields
\[
D(t_R\|p)
=\frac{\delta^2}{2AL^2}
+\frac{(1-2p)L-3}{6A^2L^4}\delta^3+O(\delta^4).
\]

For the channel-aware side, write
\[
\Phi(s)=-\log\left[(1-p)^{1+s}+p^{1+s}\right].
\]
At \(s=0\), direct differentiation gives
\[
\Phi'(0)=C,\qquad
\Phi''(0)=-AL^2,\qquad
\Phi'''(0)=A(1-2p)L^3.
\]
Therefore, at rate \(R=C-\delta\),
\[
\Phi(s)-sR
=\delta s-\frac{AL^2}2s^2+\frac{A(1-2p)L^3}6s^3+O(s^4).
\]
The objective is strictly concave near \(s=0\). Its maximizing point is interior for all sufficiently small positive \(\delta\) and satisfies
\[
s_*(\delta)=\frac{\delta}{AL^2}+O(\delta^2).
\]
Substitution into the displayed expansion gives
\[
E_{\mathrm{aware}}(C-\delta)
=\frac{\delta^2}{2AL^2}+\frac{1-2p}{6A^2L^3}\delta^3+O(\delta^4).
\]
Subtracting the two cubic coefficients cancels the \(p\)-dependent skew term and leaves exactly
\[
\frac{1}{2A^2L^4}.
\]
This coefficient is positive for every fixed \(0<p<1/2\).

## Verification
The proof uses only Taylor's theorem, local series inversion with nonzero linear coefficient \(L\), and one-dimensional strict concavity of the source's variational formula. The source equations were checked against arXiv:2610.01941v1: its binary rotated channel and capacity are in Eq. (7), the channel-aware exponent is Eq. (9), and the phase-averaged binomial converse plus the \(D(t\|p)\) strict comparison are Eqs. (11)-(12). The identity in Eq. (12), together with the entropy boundary used in the proof of Eq. (10), corresponds to \(h(t_R)=R\). No finite numerical experiment is used as an infinite proof.

As an algebra check, the cubic terms can be recomputed from derivatives alone: \(h'(p)=L\), \(h''(p)=-1/A\), \(h'''(p)=(1-2p)/A^2\); the first two nonzero derivatives of \(D(t\|p)\) at \(t=p\) are \(1/A\) and \((2p-1)/A^2\); and the derivatives of \(\Phi\) displayed above are the first three cumulants of the two-point log-probability variable with the appropriate signs.

## Relationship to prior work
Watanabe, Hayashi, Matsuura, and Cheng prove that universality can strictly reduce high-rate reliability for classical-quantum channels and give the explicit rotated-qubit formulas used here. Their proof establishes strict inequality, but the inspected statement and proof do not give its near-capacity order or coefficient. Cheng and Liu establish the channel-aware high-rate reliability formula for general classical-quantum channels, providing the Petz-Rényi side used by the recent source. Chubb, Tan, and Tomamichel analyze moderate deviations near classical-quantum capacity and identify the quadratic dispersion scale. That quadratic theory is consistent with, but does not imply, the cubic separation here: the present calculation shows why a second-order near-capacity analysis cannot detect this particular universality loss.

## Limitations
The result is a local asymptotic refinement of one explicit noncommuting rotated-qubit family. It does not show that every noncommuting family has a cubic penalty, does not identify a universal third-order invariant for arbitrary channels, and does not alter the source's low-rate caveats. The coefficient is not uniform in \(p\) near the endpoints \(0\) and \(1/2\). The originality assessment is based on focused searches and inspection of the closest primary literature; differently phrased unpublished or newly posted work could still contain the same expansion.

## References
1. K. Watanabe, M. Hayashi, T. Matsuura, and H.-C. Cheng, “Universality Sacrifices Reliability in Classical-Quantum Channel Coding,” arXiv:2610.01941v1 (first public 2026-10-01).
2. H.-C. Cheng and P.-C. Liu, “Error Exponents for Quantum Packing Problems via An Operator Layer Cake Theorem,” arXiv:2507.06232v4.
3. C. T. Chubb, V. Y. F. Tan, and M. Tomamichel, “Moderate deviation analysis for classical communication over quantum channels,” arXiv:1701.03114v3; Communications in Mathematical Physics 355 (2017), 1283–1315.
