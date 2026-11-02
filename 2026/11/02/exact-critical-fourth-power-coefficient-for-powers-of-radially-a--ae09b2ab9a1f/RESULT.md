# Exact critical fourth-power coefficient for powers of radially aligned finite Blaschke products

## Finding
For every fixed positive integer \(m\), nonnegative integer \(q\), and real parameters \(a_j\in(0,1)\), form
\[
B(z)=z^q\prod_{j=1}^m\frac{z-a_j}{1-a_jz},\qquad
B(z)^n=\sum_{k=0}^{\infty}c_{n,k}z^k.
\]
Define two strictly positive endpoint-curvature quantities
\[
U=\sum_{j=1}^m\frac{2a_j(1+a_j)}{(1-a_j)^3},\qquad
V=\sum_{j=1}^m\frac{2a_j(1-a_j)}{(1+a_j)^3}.
\]
Then for integers \(n\to\infty\),
\[
\boxed{\sum_{k\ge0}|c_{n,k}|^4
=\frac{\log n}{2\pi^2n}\left(\frac1U+\frac1V\right)+O_B(n^{-1}).}
\]
The explicit leading constant is exact, not merely a comparability constant. The same formula holds after rotating all nonzero zeros by a common angle, since such a rotation only changes Taylor coefficient phases.

For the single zero \(a_1=1/2\), the coefficient is \(41/(12\pi^2)\). For two distinct zeros \(a_1=1/5\) and \(a_2=1/2\), the coefficient is \(637/(414\pi^2)\).

## Assumptions and scope
The zeros and their multiplicities, the number \(m\), and the monomial order \(q\) are fixed as \(n\) grows. Repeated nonzero zeros are permitted. At least one nonzero root is required; if every root is zero, powers are monomials and the fourth-power sum equals one instead of following the stated law. The notation \(O_B(n^{-1})\) allows a constant dependent on the fixed product; it is not uniform in degenerating zero configurations. The Taylor coefficients are normalized in the conventional Hardy-space basis of monomials, so \(\sum_k|c_{n,k}|^2=1\).

## Proof
**Step 1 (boundary phase and its two curvatures).** Because \(B\) is a finite inner function, there is a real smooth phase lift \(\phi\) with \(B(e^{i\theta})=e^{i\phi(\theta)}\), and
\[
P(\theta):=\phi'(\theta)=q+\sum_{j=1}^m\frac{1-a_j^2}{1+a_j^2-2a_j\cos\theta}.
\]
All summands increase strictly with \(\cos\theta\). Hence \(P\) is even, strictly decreasing on \((0,\pi)\), and strictly increasing on \((\pi,2\pi)\). Differentiating the rational terms directly gives
\[
P''(0)=-U,\qquad P''(\pi)=V.
\]
The quantities \(U,V\) are positive. A monomial factor adds the constant \(q\) to \(P\), so it does not influence these derivatives or the fourth-power sum (the coefficient sequence is shifted by \(qn\)).

**Step 2 (autocorrelation form of the fourth moment).** Define
\[
A_n(t)=\frac1{2\pi}\int_0^{2\pi}
 e^{in[\phi(\theta+t)-\phi(\theta)]}\,d\theta.
\]
Orthogonality of the nonnegative Fourier modes of \(B^n\) yields the *exact* identity
\[
A_n(t)=\sum_{k\ge0}|c_{n,k}|^2e^{ikt},\qquad
\sum_{k\ge0}|c_{n,k}|^4=\frac1{2\pi}\int_0^{2\pi}|A_n(t)|^2\,dt.
\]
Absolute convergence of the autocorrelation series follows from \(\sum_k|c_{n,k}|^2=1\). In particular, \(|A_n(t)|\le1\) and \(|A_n(2\pi-t)|=|A_n(t)|\).

**Step 3 (all stationary points and uniform estimates).** Let \(F_t(\theta)=\phi(\theta+t)-\phi(\theta)\). For \(0<t<2\pi\), the equation \(\partial_\theta F_t=0\) says \(P(\theta+t)=P(\theta)\). Strict monotonicity in \(\cos\theta\) shows that its *only* solutions modulo \(2\pi\) are
\[
\theta_1=-t/2,\qquad\theta_2=\pi-t/2.
\]
The second derivatives are \(F_t''(\theta_1)=2P'(t/2)<0\) and \(F_t''(\theta_2)=2P'(\pi+t/2)>0\). As \(t\downarrow0\), their absolute values equal \(Ut+O_B(t^3)\) and \(Vt+O_B(t^3)\), respectively.

For a fixed sufficiently small \(\delta>0\), write
\[
G_t(\theta)=\frac{F_t(\theta)}t=\int_0^1P(\theta+st)\,ds.
\]
This is smooth down to \(t=0\), where \(G_0=P\); both its stationary points remain uniformly nondegenerate for \(0\le t\le\delta\). The ordinary one-dimensional stationary-phase theorem with parameter \(nt\) therefore gives, uniformly for \(K/n\le t\le\delta\), with any fixed sufficiently large \(K>0\),
\[
A_n(t)=\sum_{j=1}^{2}
 \frac{\exp\{inF_t(\theta_j)+i\pi\operatorname{sgn}(F_t''(\theta_j))/4\}}
 {\sqrt{2\pi n|F_t''(\theta_j)|}}+O_B((nt)^{-3/2}).
\]
Uniformity follows from compactness, a fixed partition of unity around the two critical points, and uniform separation from stationary points on the remaining arcs. On \([\delta,\pi]\), the usual stationary-phase estimate instead gives \(|A_n(t)|=O_B(n^{-1/2})\) uniformly.

**Step 4 (logarithmic diagonal and bounded interference).** Squaring the expansion, the two nonoscillatory diagonal terms in \(|A_n(t)|^2\) are
\[
\frac1{2\pi n}\left(\frac1{|2P'(t/2)|}+\frac1{|2P'(\pi+t/2)|}\right)
 =\frac1{2\pi nt}\left(\frac1U+\frac1V\right)+O_B(n^{-1}).
\]
The difference between the two stationary phases is
\[
D(t)=F_t(-t/2)-F_t(\pi-t/2),\qquad
D'(t)=P(t/2)-P(\pi+t/2).
\]
For sufficiently small fixed \(\delta\), this derivative is bounded below by a positive constant, because \(P(0)>P(\pi)\). The complex cross term has amplitude \(O_B((nt)^{-1})\) and an amplitude derivative \(O_B((nt^2)^{-1})\). A single integration by parts in \(e^{inD(t)}\) shows that its integral over \([K/n,\delta]\) is \(O_B(n^{-1})\), including both endpoint terms. The integrated stationary-phase remainder contributes \(O_B(n^{-1})\): its cross term with the main expansion is \(O_B((nt)^{-2})\), whose integral begins at \(t=K/n\).

The initial interval \([0,K/n]\) contributes \(O_B(n^{-1})\) because \(|A_n|\le1\). The fixed interior \([\delta,\pi]\) contributes \(O_B(n^{-1})\). Thus
\[
\int_0^\pi|A_n(t)|^2\,dt
=\frac{\log n}{2\pi n}\left(\frac1U+\frac1V\right)+O_B(n^{-1}).
\]
Reflecting around \(\pi\) and applying the exact Parseval identity of Step 2 yields the asserted factor \(1/(2\pi^2)\), concluding the proof.

## Verification
The curvature formulas follow by two differentiations of the displayed Poisson kernels. The companion script `check.py` independently reconstructs truncated rational Taylor series, tests the exact autocorrelation/Fourier fourth-power identity, and checks special-value curvatures and finite-parameter examples. Numerical truncation and finite experiments provide supplementary consistency evidence only: the theorem for all positive powers and all allowed zero configurations rests on Steps 1–4.

## Relationship to prior work
Szehr and Zarouf (2017) established the critical fourth-power *order* for a single Blaschke factor, corresponding to \(\ell^4\)-norm of order \((\log n/n)^{1/4}\), without the explicit coefficient here. Borichev, Fouchet, and Zarouf (2021) developed asymptotics for *individual* Taylor coefficients of a single factor, a potentially useful route toward a critical sum; their treatment does not directly state this fourth-power constant. Borichev, Fouchet, and Zarouf (2024) studied sharp \(\ell^\infty\) decay for general finite Blaschke products, not this exact \(\ell^4\) coefficient. The present result supplies both an explicit constant and an aligned multi-zero extension, with a direct autocorrelation argument.

## Limitations
This theorem does not cover arbitrary noncollinear zero configurations, which can produce additional stationary points and interference. It does not give an error uniform over zeros approaching the origin or unit circle. The related single-factor asymptotic formulas could imply its single-zero specialization after additional summation; no priority claim is made for that indirect deduction. An independent audit of the new statement and its historical novelty has not been performed.

## References
1. O. Szehr and R. Zarouf, *\(\ell_p\)-norms of Fourier coefficients of powers of a Blaschke factor*, arXiv:1701.02358 (first public 2017-01-09), https://arxiv.org/abs/1701.02358.
2. A. Borichev, K. Fouchet, and R. Zarouf, *On the Fourier coefficients of powers of a Blaschke factor and strongly annular functions*, arXiv:2107.00405 (first public 2021-07-01), https://arxiv.org/abs/2107.00405.
3. A. Borichev, K. Fouchet, and R. Zarouf, *On the Fourier coefficients of powers of a finite Blaschke product*, arXiv:2401.17520 (first public 2024-01-31), https://arxiv.org/abs/2401.17520.

