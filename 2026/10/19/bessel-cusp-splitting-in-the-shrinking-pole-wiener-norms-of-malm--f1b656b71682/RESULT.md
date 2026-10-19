# Bessel cusp splitting in the shrinking-pole Wiener norms of Malmquist functions

## Finding
For an integer \(n\ge2\), let \(0\le c<n\), \(\lambda=c/n\), and
\[
f_{n,\lambda}(z)=\frac1{1-\lambda z}\left(\frac{z-\lambda}{1-\lambda z}\right)^{n-1}.
\]
Let \(\|f\|_W\) be the sum of the absolute Taylor coefficients of this analytic function. For every fixed \(C>0\), uniformly for \(c\in[0,C]\) as \(n\to\infty\),
\[
\|f_{n,c/n}\|_W = F(c)+O_C(n^{-1}),\qquad
F(c)=\sum_{k\in\mathbb Z}|J_k(2c)|
=|J_0(2c)|+2\sum_{k\ge1}|J_k(2c)|.
\]
The same limit holds for the ratio to the Hardy-space norm, since \(\|f_{n,c/n}\|_{H^2}=(1-c^2/n^2)^{-1/2}\). A precise first-order Fourier expansion is proved below.

The limit \(F\) is real analytic away from the positive half-zeros \(c_{m,r}=j_{m,r}/2\), where \(j_{m,r}\) is the \(r\)-th positive zero of the Bessel function \(J_m\). It is nondifferentiable at every such point, with positive derivative jump
\[
F'_+(c_{m,r})-F'_-(c_{m,r})=
\begin{cases}4|J'_0(2c_{0,r})|,&m=0,\\
8|J'_m(2c_{m,r})|,&m\ge1.
\end{cases}
\]
For every fixed \(m\ge1\) and \(r\ge1\), the two individual Fourier coefficients at signed indices \(m\) and \(-m\) of the centered function \(z^{-(n-1)}f_{n,c/n}(z)\) each have a unique real zero \(c^{(n)}_{+m,r}\), respectively \(c^{(n)}_{-m,r}\), in a sufficiently small fixed neighborhood of \(c_{m,r}\) for all sufficiently large \(n\). Their locations satisfy
\[
c^{(n)}_{k,r}=c_{m,r}+\frac{c_{m,r}(1-k)}{2n}+O_{m,r}(n^{-2}),\quad k\in\{m,-m\},
\]
so the two zero crossings split by the precise amount
\[
c^{(n)}_{-m,r}-c^{(n)}_{+m,r}=\frac{m\,c_{m,r}}n+O_{m,r}(n^{-2}).
\]
At \(m=0\) there is a single zero crossing, located at \(c_{0,r}+c_{0,r}/(2n)+O_r(n^{-2})\).

There is also an explicit rescaled local norm profile at every Bessel cusp, stated in the proof. This is a result about these particular Malmquist–Walsh rational functions, not about the sharp Wiener-to-Hardy embedding constant of an entire rational function class.

## Assumptions and scope
All functions are on the unit circle with its normalized Haar measure; Wiener norm means \(\ell^1\) of Laurent coefficients (or Taylor coefficients for analytic functions), and \(J_k\) denotes the Bessel function of the first kind of integral order. All quoted error terms concern \(n\to\infty\), with bounded \(c\) for the uniform norm statement and fixed \((m,r)\) for the zero-location statement. Set
\[
H_n(c,z)=z^{-(n-1)}f_{n,c/n}(z)
=\frac{(1-(c/n)z^{-1})^{n-1}}{(1-(c/n)z)^n},\quad |z|=1.
\]
This centering preserves the Wiener norm. Here \(c<n\) guarantees the pole remains outside the unit disk.

## Proof
**Step 1: uniform Wiener-algebra expansion.** The Banach algebra \(A(\mathbb T)\) of absolutely summable Laurent series has norm \(\|\sum a_kz^k\|_A=\sum|a_k|\). For any fixed \(C\), \(n>2C\) gives convergent Banach-algebra logarithms, and Taylor's formula (with a uniformly summable remainder) yields
\[
\begin{aligned}
\log H_n(c,z)
&=(n-1)\log(1-(c/n)z^{-1})-n\log(1-(c/n)z)\\
&=c(z-z^{-1})+\frac1n Q_c(z)+O_C(n^{-2})_A,\\
Q_c(z)&=cz^{-1}+\frac{c^2}{2}(z^2-z^{-2}).
\end{aligned}
\]
The exponential is analytic in the Banach algebra; hence
\[
H_n(c,z)=E_c(z)+\frac1n E_c(z)Q_c(z)+O_C(n^{-2})_A,\quad
E_c(z)=e^{c(z-z^{-1})}.
\]
The same expansion can be differentiated any fixed number of times with respect to \(c\) on bounded complex neighborhoods, by the Cauchy estimate or termwise differentiation of the uniformly convergent power series.

**Step 2: Bessel coefficients and norm.** The classical Bessel generating formula gives \(E_c(z)=\sum_{k\in\mathbb Z}J_k(2c)z^k\). Accordingly, for each integer \(k\), if \(h_{n,k}(c)\) is the \(k\)-th Laurent coefficient of \(H_n\), then
\[
h_{n,k}(c)=J_k(2c)+\frac{B_k(c)}n+O_C(n^{-2}),
\quad B_k(c)=cJ_{k+1}(2c)+\frac{c^2}2\bigl(J_{k-2}(2c)-J_{k+2}(2c)\bigr),
\]
with the stronger \(\ell^1(\mathbb Z)\) remainder bound uniform for \(c\in[0,C]\). Taking absolute sums and using the reverse triangle inequality gives the uniform norm assertion. Because multiplication by a power of \(z\) shifts coefficients, \(\|f_{n,c/n}\|_W=\|H_n(c,\cdot)\|_A\). Since the Blaschke factor has unit modulus almost everywhere on the circle, Parseval and the geometric series give \(\|f_{n,c/n}\|_{H^2}^2=(1-c^2/n^2)^{-1}\).

**Step 3: complete limiting cusp classification.** For positive \(c\), each \(J_m(2c)\), \(m\ge0\), has simple zeros, and no distinct nonnegative integral orders share a positive zero (the classical Bourget–Siegel theorem). On a fixed compact interval, all sufficiently high Bessel orders have positive values by their absolutely convergent power series with uniformly dominated tails. Hence the possible nonanalytic points of \(F\) are isolated and occur exactly at the values \(c_{m,r}\), and the remaining Bessel absolute-value series is real analytic there. At \(c_{0,r}\), exactly one Laurent mode vanishes; at \(c_{m,r}\) for \(m\ge1\), exactly the modes \(m,-m\) vanish, since \(J_{-m}=(-1)^mJ_m\). Each absolute value \(|J_k(2c)|\) contributes derivative jump \(4|J'_k(2c_{m,r})|\). Summing the one or two contributions proves both displayed jump formulas.

**Step 4: individual zero crossings and their splitting.** At \(c_0=c_{m,r}>0\), the recurrences \(J_{m-1}+J_{m+1}=(m/c_0)J_m=0\) and \(J_m'=\tfrac12(J_{m-1}-J_{m+1})=-J_{m+1}\) imply
\[
B_m(c_0)=c_0(1-m)J_{m+1}(2c_0),\qquad
B_{-m}(c_0)=(-1)^m c_0(1+m)J_{m+1}(2c_0).
\]
For \(m=0\), the first formula gives \(B_0(c_0)=c_0J_1(2c_0)\). The coefficient maps are real analytic in \((c,1/n)\) near \((c_0,0)\), because the Banach logarithm admits an analytic extension in the small parameter \(1/n\). Their \(c\)-derivatives at that point are \(2J_k'(2c_0)\ne0\). The real analytic implicit-function theorem gives one and only one zero per signed coefficient in a sufficiently small fixed interval, for all sufficiently large \(n\). Implicit differentiation at \(1/n=0\) gives
\[
\frac{d c^{(n)}_{k,r}}{d(1/n)}\Big|_{0}
=-\frac{B_k(c_0)}{2J'_k(2c_0)}=\frac{c_0(1-k)}2.
\]
These identities prove the two explicit locations and the splitting distance. They do not assert that other Fourier coefficients have no zeros elsewhere.

**Step 5: the complete local norm boundary layer.** At any \(c_0=c_{m,r}\) define \(a_k=J_k(2c_0)\), \(d_k=2J'_k(2c_0)\), and \(b_k=B_k(c_0)\). For every fixed real \(s\), the following full series converges absolutely and provides the first-order scaling:
\[
\lim_{n\to\infty} n\bigl(\|f_{n,(c_0+s/n)/n}\|_W-F(c_0)\bigr)
=\sum_{k:a_k\ne0}\operatorname{sgn}(a_k)(s d_k+b_k)
+\sum_{k:a_k=0}|s d_k+b_k|.
\]
Convergence is uniform for \(s\) in compact sets. Indeed \(H_n(c_0+s/n)=E_{c_0}+n^{-1}(s\partial_cE_{c_0}+E_{c_0}Q_{c_0})+O_S(n^{-2})_A\). The directional derivative of the \(\ell^1\) norm is obtained coordinatewise using \(\bigl||a+tb|-|a|\bigr|/t\le|b|\), then dominated convergence. The error term is uniform by the reverse triangle inequality; equicontinuity in \(s\) upgrades pointwise convergence to uniform convergence on compact intervals. For \(m\ge1\), precisely two absolute-value terms remain in the second sum, with kink positions separated by \(m c_0\) in this scaled coordinate. At \(m=0\) only one kink remains.

## Verification
The standalone script `CHECK.py` numerically evaluates the centered boundary Fourier series using an independent discrete Fourier transform and the Bessel limit with SciPy. It checks convergence of Wiener norms at several values of \(c\), first-order coefficients away from Bessel zeros, and the signed Fourier zero shifts for orders \(m=0,1,2,3\) and sample sizes \(n=80,160,320\). These are finite numerical stress tests; the all-order and all-zero claims are proved by the Banach-algebra expansion and implicit-function argument above.

## Relationship to prior work
Auxemery, Borichev and Zarouf (2026) study fixed pole parameters in a rational Nikolskii/Wiener inequality. Their Malmquist–Walsh witness is the precise function used here but is selected for \(\lambda\ge1/2\), while their proof selects a Dirichlet polynomial for \(\lambda\le1/2\). The present shrinking-pole regime \(\lambda=c/n\) supplies a different, finite Wiener-norm limit and resolves the associated Bessel cusp collisions. Szehr and Zarouf (2017) prove fixed-\(\lambda\) coefficient-norm asymptotics for powers of one Blaschke factor; their stated constants depend on \(\lambda\), and their results do not give the above joint scaling or signed zero-displacement formula. The Bessel generating series, zero simplicity, and Bourget–Siegel nonintersection theorem are classical ingredients, not new findings. Existing results establish neither this explicit \(1/n\) boundary layer nor the two signed-mode crossover by direct implication.

## Limitations
This theorem concerns one specified rational test family; it does not optimize over all rational functions, prove a new Nikolskii sharp constant, describe the fixed-positive-pole regime, or control the limit when \(c\to\infty\) with \(n\). Asymptotic uniqueness of the two *specified Fourier-mode* zeros is local; it is not asserted for the union of zero sets of every coefficient. The first-order \(\ell^1\) limit does not imply a uniform second derivative at the kink points. Historical priority for equivalent shrinking-pole identities outside indexed sources remains a risk.

## References
1. B. Auxemery, A. Borichev and R. Zarouf, *Asymptotic sharpness of a Nikolskii type inequality for rational functions in the Wiener algebra*, arXiv:2603.03908v1, 4 March 2026; full text: https://arxiv.org/html/2603.03908v1 .
2. O. Szehr and R. Zarouf, *\(\ell_p\)-norms of Fourier coefficients of powers of a Blaschke factor*, arXiv:1701.02358v1, 9 January 2017; full text: https://arxiv.org/html/1701.02358v1 .
3. NIST Digital Library of Mathematical Functions, §10.21, *Zeros*: https://dlmf.nist.gov/10.21 .
4. NIST Digital Library of Mathematical Functions, §10.12, *Generating Function and Associated Series*: https://dlmf.nist.gov/10.12 .
