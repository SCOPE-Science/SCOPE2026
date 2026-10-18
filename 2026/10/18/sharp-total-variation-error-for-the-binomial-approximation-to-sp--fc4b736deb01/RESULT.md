# Sharp total-variation error for the binomial approximation to spillage laws

## Finding
Fix an integer \(k\ge1\) and a real number \(\phi>0\). For every integer \(R\ge0\), let \(N_R\) have the spillage law with parameters \(n=R+k\), \(k\), and \(\phi\):
\[
\Pr(N_R=r)=\frac{\binom{R+k}{k+r}\phi^{R-r}S(k+r,k)}{\sum_{j=0}^{R}\binom{R+k}{k+j}\phi^{R-j}S(k+j,k)},\qquad 0\le r\le R,
\]
where \(S(j,k)\) denotes the Stirling number of the second kind. Put \(q=k/(k+\phi)\). Then, as \(R\to\infty\) with \(k,\phi\) fixed,
\[
\boxed{\sqrt R\,d_{\mathrm{TV}}\!\left(\mathcal L(N_R),\operatorname{Bin}(R,q)\right)\longrightarrow\sqrt{\frac{k\phi}{2\pi}}.}
\]
Here \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_{r\in\mathbb Z}|P\{r\}-Q\{r\}|\). The positive constant shows that the root-\(R\) error rate is sharp. For example, \(k=\phi=1\) gives limit \(1/\sqrt{2\pi}\).

An exact binomial-mixture representation is a key intermediate step. It also yields, when \(R\ge2\), strict overdispersion relative to the binomial law with the *same exact mean*; this structural observation is not needed to interpret the displayed asymptotic claim.

## Assumptions and scope
The theorem is restricted to \(k\in\{1,2,\ldots\}\) fixed and \(\phi\in(0,\infty)\) fixed while \(R=n-k\to\infty\). It does not assert a uniform rate when either parameter varies with \(R\). The endpoint cases \(\phi=0\), \(\phi=\infty\), and \(k=0\) are not covered by the positive-constant asymptotic. The spillage normalization and notation are those of O'Neill [1].

## Proof
**1. Exact continuous mixing.** Let \(U_1,\dots,U_k\) be independent uniform random variables on \([0,1]\), and put \(Z=\sum_i U_i\). The classical Stirling exponential generating function, equivalently the Irwin–Hall moment identity in [3], gives
\[
\mathbb E Z^r=\frac{S(k+r,k)}{\binom{k+r}{k}},\qquad r\ge0.
\]
Indeed, \(\mathbb E e^{tZ}=((e^t-1)/t)^k\), and comparing coefficients with \((e^t-1)^k/k!=\sum_{j\ge k}S(j,k)t^j/j!\) proves the identity. Because
\[
\binom{R+k}{k+r}S(k+r,k)
=\binom{R+k}{k}\binom Rr\mathbb E Z^r,
\]
normalization of the spillage probabilities yields
\[
\Pr(N_R=r)=\frac{\binom Rr\phi^{R-r}\mathbb E Z^r}{\mathbb E(\phi+Z)^R}.
\]
Define a tilted probability measure \(\pi_R\) on \(Z\in[0,k]\) by
\[
\mathrm d\pi_R(z)=\frac{(\phi+z)^R}{\mathbb E(\phi+Z)^R}\,\mathrm d\mathcal L(Z)(z),
\qquad Q(z)=\frac{z}{\phi+z}.
\]
Then the *entire* spillage law is the mixture \(N_R\mid Z=z\sim\operatorname{Bin}(R,Q(z))\) with \(Z\sim\pi_R\).

**2. Endpoint concentration and parameter moments.** Set \(A=k+\phi\) and \(V=k-Z\), so that the tilt has density proportional to \((A-v)^R\) times the density of \(V\). Since \(V\) is also a sum of \(k\) independent uniforms, its density is exactly \(v^{k-1}/(k-1)!\) for \(0<v<1\). On every fixed region \(v\ge\delta>0\), the tilted contribution is exponentially small relative to the total, because \((A-v)^R\le(A-\delta)^R\), while a neighborhood of zero contributes at least a fixed multiple of \(A^R R^{-k}\). Comparing the integrals over \((0,\delta)\) with complete beta integrals therefore gives, for every fixed integer \(j\ge0\),
\[
\mathbb E_{\pi_R}V^j
=A^j\frac{(k)_j}{(R+k+1)_j}+O(e^{-cR})
=A^j(k)_jR^{-j}+O(R^{-j-1}),
\]
where \((a)_j=a(a+1)\cdots(a+j-1)\) is the rising factorial, with \((a)_0=1\), and \(c>0\) may depend on the fixed parameters. In the first equality, the exponentially small bound is for the difference from the beta-integral ratio; it remains true after adjusting the positive exponent \(c\). In particular,
\[
\mathbb E_{\pi_R}V=\frac{Ak}{R}+O(R^{-2}),\quad
\operatorname{Var}_{\pi_R}(V)=\frac{A^2k}{R^2}+O(R^{-3}),\quad
\mathbb E_{\pi_R}V^3=O(R^{-3}).
\]
Because
\[
Q=\frac{k-V}{A-V}=q-\frac{\phi V}{A(A-V)},
\]
Taylor expansion near \(V=0\), together with the exponentially small complement, implies
\[
q_R:=\mathbb E_{\pi_R}Q=q-\frac{k\phi}{AR}+O(R^{-2}),\qquad
\operatorname{Var}_{\pi_R}(Q)=\frac{k\phi^2}{A^2R^2}+O(R^{-3}).
\]

**3. Removing random mixing to second order.** Write \(b_{R,r}(p)=\binom Rr p^r(1-p)^{R-r}\). For every fixed compact interval \(I\subset(0,1)\), the binomial score identity and its derivative show
\[
\sup_{p\in I}\sum_{r=0}^R|\partial_p^2b_{R,r}(p)|=O(R).
\]
Explicitly, writing \(B\sim\operatorname{Bin}(R,p)\), the second derivative divided by \(b_{R,r}(p)\) is
\[
\frac{(r-Rp)^2}{p^2(1-p)^2}-\frac r{p^2}-\frac{R-r}{(1-p)^2};
\]
the expectation of its absolute value is at most \(2R/[p(1-p)]\). Fix \(I\) containing \(q\) in its interior. The tilted event \(Q\notin I\) has exponentially small probability by the endpoint estimate. Using the uniform \(O(R)\) bound on the good event, the crude global \(O(R^2)\) derivative bound on the negligible complement, Taylor's theorem, and \(\mathbb E(Q-q_R)=0\), we obtain
\[
\sum_{r=0}^R\left|\mathbb E_{\pi_R}b_{R,r}(Q)-b_{R,r}(q_R)\right|
=O\bigl(R\operatorname{Var}_{\pi_R}(Q)\bigr)+O(R^2e^{-cR})=O(R^{-1}).
\]
Consequently,
\[
d_{\mathrm{TV}}\!\left(\mathcal L(N_R),\operatorname{Bin}(R,q_R)\right)=O(R^{-1}).
\]

**4. Sharp first-order displacement.** Uniformly near \(q\), the same second-derivative estimate gives
\[
\sum_{r=0}^R|b_{R,r}(q_R)-b_{R,r}(q)|
=|q_R-q|\sum_{r=0}^R|\partial_pb_{R,r}(q)|+O(R|q_R-q|^2).
\]
The first derivative has the exact norm
\[
\sum_{r=0}^R|\partial_pb_{R,r}(q)|
=\frac{\mathbb E|B_R-Rq|}{q(1-q)},\qquad B_R\sim\operatorname{Bin}(R,q).
\]
The binomial central limit theorem and uniform integrability of the standardized counts (their second moments equal one) imply
\[
\frac{\mathbb E|B_R-Rq|}{\sqrt R}\longrightarrow\sqrt{\frac{2q(1-q)}\pi}.
\]
Substituting \(|q_R-q|=k\phi/(AR)+O(R^{-2})\) yields
\[
\sqrt R\,d_{\mathrm{TV}}(\operatorname{Bin}(R,q_R),\operatorname{Bin}(R,q))
\longrightarrow\frac{k\phi/A}{\sqrt{2\pi q(1-q)}}=\sqrt{\frac{k\phi}{2\pi}}.
\]
The difference between this distance and the claimed one is at most \(O(R^{-1})\) by step 3 and the reverse triangle inequality. This completes the proof.

**5. Exact dispersion observation.** The same mixture gives
\[
\operatorname{Var}(N_R)=R q_R(1-q_R)+R(R-1)\operatorname{Var}_{\pi_R}(Q).
\]
For \(R\ge2\) the last term is strictly positive because \(Q\) has a nondegenerate tilted distribution. Thus this family has positive binomial dispersion at its own exact mean, a point not needed for the total-variation limit. The leading variance correction also follows:
\[
\operatorname{Var}(N_R)=R\frac{k\phi}{A^2}+\frac{k^2\phi}{A^2}+o(1).
\]

## Verification
The standalone script `verify.py` recomputes Stirling numbers by their defining recurrence, checks the exact transformation to Irwin–Hall moment weights and the mixture-implied positive dispersion in 150 rational parameter cases, and independently evaluates the total-variation distances for four fixed parameter pairs at \(R=200,500,1000\). The numerical comparisons approach the proved constants. These finite checks are diagnostic, not a replacement for the proof of the limit. Run the script with `python3 verify.py` using a standard Python 3 installation; it requires no third-party packages.

## Relationship to prior work
O'Neill [1] defined the spillage law, proved the normalization, moment formulas, and asymptotic moments, and evaluated a different numerical approximation based on Stirling-number asymptotics. The later paper [2] treats spillage among three extended occupancy distributions. Gismatullin and Tardivel [3] derive the classical Stirling–Irwin–Hall moment identity used in step 1 (published online in 2024). The exact moment identity, spillage law, and leading binomial parameters are **prior ingredients**, not new assertions. The contribution proved here is the sharp *total-variation* constant for the ordinary \(\operatorname{Bin}(R,k/(k+\phi))\) approximation, with a second-order mixture argument explaining its origin. The inspected portions of [1]–[3] do not give this constant or the claimed total-variation limit.

## Limitations
The result does not provide a uniform estimate over growing \(k\), changing \(\phi\), or boundary regimes. It does not establish an exact finite-\(R\) expression for total variation or an optimal approximation over all binomial parameters. Standard asymptotic theorems are used in the proof but the rate and leading constant are established for the stated fixed-parameter limit. Novelty is assessed relative to the specifically inspected sources, not independently certified against every historical publication.

## References
[1] B. O'Neill, *An examination of the spillage distribution*, arXiv:2201.03126, first publicly posted 2022-01-10. https://arxiv.org/abs/2201.03126

[2] B. O'Neill, *Three Distributions in the Extended Occupancy Problem*, *Methodology and Computing in Applied Probability*, DOI 10.1007/s11009-023-10053-y. https://doi.org/10.1007/s11009-023-10053-y

[3] J. Gismatullin and P. Tardivel, *Beta distribution and associated Stirling numbers of the second kind*, *Probability and Mathematical Statistics* 44 (2024), 119–132, DOI 10.37190/0208-4147.00156, published online 2024-09-20. https://doi.org/10.37190/0208-4147.00156
