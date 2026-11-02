# A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map

## Finding
For each \(a>0\), consider the real-plane map from Soula, Jahanshahi, Al-Barakati and Moroz (2023),
\[
F_{a,b}(x,y)=\bigl(f_a(x)+b(y-x),\ f_a(y)+b(x-y)\bigr),\qquad
f_a(t)=at(1-t^2)e^{-t^2},\qquad b\in\mathbb R.
\]
A **common compact absorbing set** means a compact set \(K\subset\mathbb R^2\) such that each initial condition has an iterate in \(K\), and all subsequent iterates remain in \(K\). Then a common compact absorbing set exists **if and only if**
\[
\boxed{-\tfrac12\le b<\tfrac12.}
\]
For \(|b|>1/2\), a nonempty open set of initial conditions escapes to infinity geometrically. For \(b=1/2\), a nonempty open set instead escapes subgeometrically. More strongly, **every unbounded orbit** at this endpoint obeys the exact law
\[
\boxed{\left(\frac{x_n-y_n}{2}\right)^2
=\log n+2\log\log n+\log(2a)+o(1)},\qquad n\to\infty,
\]
and its average coordinate \((x_n+y_n)/2\) decays exponentially once the escape region is entered. Thus the two endpoints are genuinely asymmetric: \(b=-1/2\) remains globally absorbing; \(b=1/2\) admits universal logarithmically corrected escape.

## Assumptions and scope
The parameters satisfy \(a>0\) and \(b\in\mathbb R\). All initial conditions are finite real points \((x_0,y_0)\in\mathbb R^2\), and the dynamics is the exact, unrounded smooth map above. The logarithms are natural. Define mean and half-difference coordinates
\[
s=(x+y)/2,\qquad d=(x-y)/2,
\]
and the finite bound
\[
M=M_a:=\sup_{t\in\mathbb R}|f_a(t)|.
\]
For explicit computation, writing \(t_\pm=(5\pm\sqrt{17})/4\), differentiation gives
\[
M_a=a\max_{\sigma\in\{-,+\}}
\sqrt{t_\sigma}\,|1-t_\sigma|e^{-t_\sigma}.
\]
Here \(M_a>0\), and \(f_a(t)\) has the opposite sign from \(t\) whenever \(|t|>1\).

## Proof
**1. Exact coordinate reduction.** The iteration becomes
\[
s_{n+1}=\frac{f_a(s_n+d_n)+f_a(s_n-d_n)}2,
\qquad
d_{n+1}=\frac{f_a(s_n+d_n)-f_a(s_n-d_n)}2-2b d_n.
\]
Write \(g(s,d)=[f_a(s+d)-f_a(s-d)]/2\). Then \(|s_n|\le M\) for every \(n\ge1\), \(|g(s,d)|\le M\), and
\[
|d_{n+1}|\le 2|b|\,|d_n|+M.
\]
Because \(f_a\) is odd,
\[
g(s,d)=\frac{f_a(d+s)+f_a(d-s)}2.
\]

**2. Strict interior.** If \(q=2|b|<1\), choose any \(R>M/(1-q)\). The rectangle \(|s|\le M\), \(|d|\le R\) is forward invariant; the bound \(|d_n|\le q^{n-1}|d_1|+M(1-q^{n-1})/(1-q)\) forces every orbit into it in finite time.

**3. The absorbing endpoint.** Set \(b=-1/2\) and \(R=M+1\). For every \(|s|\le M\) and \(|d|>R\), the numbers \(d+s\) and \(s-d\) have opposite signs and both have modulus greater than one. Therefore \(g(s,d)\) has the sign opposite to \(d\). As \(|g|\le M<|d|\), the map \(d\mapsto d+g(s,d)\) strictly decreases \(|d|\), preserving its sign, outside \(|d|\le R\).
The rectangle
\[
K_-:=\{(s,d):|s|\le M,\ |d|\le 2M+1\}
\]
is forward invariant: inside \(|d|\le R\), the next modulus is at most \(R+M\); outside it strictly decreases. Every orbit eventually enters \(K_-\): otherwise, after the first iterate its \(|d_n|>R+M\) would decrease to a finite limit. On the compact set between that limit and the first such modulus, with \(|s|\le M\), the continuous function \(|g(s,d)|\) has a strictly positive minimum by the sign argument, contradicting convergence. This proves the closed left endpoint.

**4. Escape away from the endpoints.** If \(q=2|b|>1\), then
\[
|d_{n+1}|\ge q|d_n|-M.
\]
For any iterate with \(|d_n|>D:=M/(q-1)\), induction yields
\[
|d_{n+k}|-D\ge q^k(|d_n|-D)\to\infty.
\]
Such points form a nonempty open set of initial conditions (for instance, any sufficiently large initial half-difference). Hence no common compact absorbing set exists for \(|b|>1/2\).

**5. The escaping endpoint.** If \(b=1/2\), then \(d_{n+1}=-d_n+g(s_n,d_n)\). For \(n\ge1\), \(|s_n|\le M\). Whenever \(|d_n|>R=M+1\), the sign computation in step 3 gives
\[
|d_{n+1}|=|d_n|+|g(s_n,d_n)|>|d_n|.
\]
This increasing modulus cannot converge to a finite value: on any hypothetical compact range of limiting moduli larger than \(R\), \(|g|\) has a positive minimum. Hence it tends to infinity. Moreover, any unbounded orbit must eventually cross \(R\), after which its half-difference diverges monotonically in modulus. The preimage of the outer region contains a nonempty open set, so the escaping set has nonempty interior.

**6. Critical escape law for every escaping orbit.** For such an orbit write \(u_n=|d_n|\to\infty\) and \(s_n\in[-M,M]\). From oddness and the mean-value theorem,
\[
|s_{n+1}|\le |s_n|\,
\sup_{|t|\ge u_n-M}|f_a'(t)|.
\]
Since \(f_a'(t)=ae^{-t^2}(1-5t^2+2t^4)\to0\), eventually \(|s_{n+1}|\le |s_n|/2\). Meanwhile \(u_{n+1}\le u_n+M\), so \(u_n=O(n)\) and \(u_ns_n\to0\). The explicit expression for \(f_a\) therefore gives, for either sign of \(d_n\),
\[
\frac{g(s_n,d_n)}{f_a(d_n)}
=\frac{f_a(d_n+s_n)+f_a(d_n-s_n)}{2f_a(d_n)}\longrightarrow1.
\]
It follows that
\[
u_{n+1}-u_n=a u_n(u_n^2-1)e^{-u_n^2}(1+o(1)).
\]
With \(r_n=u_n^2\), this yields \(r_n\to\infty\) and
\[
r_{n+1}-r_n=2a r_n(r_n-1)e^{-r_n}(1+o(1))\to0.
\]
Define \(H(r)=e^r/(2ar^2)\) for sufficiently large \(r\). By the mean-value theorem and \(H'(r)=H(r)(1-2/r)\),
\[
H(r_{n+1})-H(r_n)\longrightarrow1.
\]
Summation implies \(H(r_n)/n\to1\). Taking logarithms,
\[
r_n-2\log r_n-\log(2a)=\log n+o(1).
\]
First this implies \(r_n/\log n\to1\), and substitution gives
\[
r_n=\log n+2\log\log n+\log(2a)+o(1).
\]
The exponential decay of the mean coordinate was proved above. Together the six steps establish all assertions.

## Verification
The included standalone script `verify.py` performs finite implementation cross-checks: 84 direct-coordinate identities, 60 interior bounded-orbit trials, 12,000 negative-endpoint invariant-state steps, 480 geometric-escape inequalities, and critical-endpoint ratio comparisons at two observation lengths for three positive gains. Run with `python3 verify.py` using the Python standard library. No finite run is used to establish the universal theorem or the asymptotic coefficient; those follow from the complete analytic argument in the proof.

## Relationship to prior work
Soula, Jahanshahi, Al-Barakati and Moroz introduced this exact diffusive-coupling map and studied numerical bifurcation regions, critical curves, chaotic synchronization and basin geometry [1]. The present result instead determines the global absorbing/escaping parameter boundary for **all** real initial conditions and the universal non-geometric escape law precisely at its positive endpoint. Ordinary bounded-forcing estimates account for the strict interior and strict exterior but not the asymmetric endpoint conclusion or the logarithmic correction. The precursor study of coupled sine maps [2] and Ding–Yang's earlier nonlinear output-coupled system [3] involve different map laws; neither cited formulation directly implies these endpoint results.

## Limitations
This theorem does not classify finite attractors or their basins inside the absorbing region, nor does it establish uniform entrance times into a compact set over all unbounded initial data. It does not apply to negative gain \(a\), different coupling functions, finite-precision arithmetic, or nonautonomous forcing. The literature comparison is limited by incomplete access to some related older full texts; a general unindexed theorem could affect publication priority. Numerical calculations are consistency checks, not an independent certification.

## References
[1] Y. Soula, H. Jahanshahi, A. A. Al-Barakati and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics **11** (2023), 1517, published 21 March 2023, DOI: 10.3390/math11061517.

[2] Y. Soula, A. K. Taha, D. Fournier-Prunaret and N.-E. Hamri, *Bifurcations and Dynamical Behavior of 2D Coupled Chaotic Sine Maps*, Applied and Computational Mathematics **11** (2022), 18–30, DOI: 10.11648/j.acm.20221101.12.

[3] M. Ding and W. Yang, *Observation of intermingled basins in coupled oscillators exhibiting synchronized chaos*, Physical Review E **54** (1996), 2489–2494, DOI: 10.1103/PhysRevE.54.2489.
