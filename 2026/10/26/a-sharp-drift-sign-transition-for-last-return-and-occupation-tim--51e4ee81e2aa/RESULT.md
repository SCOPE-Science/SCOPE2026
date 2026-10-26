# A sharp drift-sign transition for last-return and occupation-time covariance

## Finding
For a nearest-neighbor random walk with independent upward-step probability \(p\in(0,1)\), the sign of the covariance between the last zero and positive occupation time is **opposite to the drift** at every finite nontrivial horizon. Precisely, for every integer \(n\ge1\),
\[
\operatorname{sgn}\operatorname{Cov}(K_n,U_n)=\operatorname{sgn}(1/2-p).
\]
The conclusion strengthens to an exact monotonicity of the conditional mean. The equality at \(p=1/2\) is a classical symmetric boundary phenomenon and is **not** claimed as new. The contribution is the sharp strict all-horizon sign law for nonzero drift and its signed-meander likelihood-ratio mechanism.

## Assumptions and scope
Let \(\xi_1,\ldots,\xi_{2n}\) be independent random signs, with \(\Pr(\xi_i=+1)=p\) and \(q=1-p\). Put \(S_0=0\), \(S_j=\sum_{i=1}^j\xi_i\),
\[
K_n=\frac12\max\{j\in\{0,2,\ldots,2n\}:S_j=0\},\qquad U_n=\frac12\sum_{j=1}^{2n}\mathbf{1}\{S_{j-1}+S_j>0\}.
\]
Each excursion contributes an even number of positive-midpoint steps, so \(U_n\in\{0,\ldots,n\}\). Parity forces every return to occur at an even time, so \(K_n\in\{0,\ldots,n\}\). Every value of \(K_n\) has positive probability when \(0<p<1\).

## Proof
Write \(m=n-k\). When \(K_n=k<n\), the initial \(2k\) steps form a bridge and the last \(2m\) steps form a strictly positive or strictly negative meander, with no return to zero. The bridge law conditional on its endpoint zero is uniform over all bridges, even for \(p\ne q\), because every length-\(2k\) bridge has exactly \(k\) up-steps and \(k\) down-steps. The Chung–Feller bridge theorem therefore makes its positive semiduration \(J_k\) exactly uniform on \(\{0,\ldots,k\}\), independent of the meander's sign. If the meander is positive it contributes \(m\) to \(U_n\), and otherwise zero.

For integers \(1\le r\le m\), the ballot count of paths of length \(2m\) which stay strictly positive at all positive times and end at \(2r\) is
\[
b_{m,r}=\frac rm\binom{2m}{m-r}.
\]
Define the positive and negative no-return probabilities
\[
A_m^+=\sum_{r=1}^m b_{m,r}p^{m+r}q^{m-r},\qquad A_m^-=\sum_{r=1}^m b_{m,r}p^{m-r}q^{m+r},
\quad w_m=\frac{A_m^+}{A_m^++A_m^-}.
\]
Consequently, conditional on \(K_n=k<n\),
\[
U_n\ \overset d=\ J_k+mB_m,\quad J_k\sim\operatorname{Unif}\{0,1,\ldots,k\},\quad B_m\sim\operatorname{Bernoulli}(w_m),
\]
with independence. At \(k=n\), \(U_n\) is uniform on \(\{0,\ldots,n\}\). This is a full finite-horizon joint law, since
\[
\Pr(K_n=k)=\binom{2k}k(pq)^k(A_m^++A_m^-)\ (k<n),\quad\Pr(K_n=n)=\binom{2n}n(pq)^n.
\]
In particular,
\[
\mu_k:=\mathbb E[U_n\mid K_n=k]=\frac n2+(n-k)(w_{n-k}-1/2)\quad(k<n),\qquad\mu_n=\frac n2.
\]

We prove a strict likelihood-ratio fact. Assume \(p>q\), set \(a=p/q>1\), and for \(m\ge1\) introduce a probability measure on \(\{1,\ldots,m\}\) with weights proportional to \(b_{m,r}a^{-r}\). The odds satisfy
\[
\frac{A_m^+}{A_m^-}=\frac{\sum_r b_{m,r}a^r}{\sum_r b_{m,r}a^{-r}}=\mathbb E_m[a^{2R}].
\]
For \(1\le r\le m\), the successive ballot-number ratio is
\[
\frac{b_{m+1,r}}{b_{m,r}}=\frac m{m+1}\frac{(2m+2)(2m+1)}{(m+1)^2-r^2},
\]
which strictly increases in \(r\). The support at time \(m+1\) adds the positive value \(r=m+1\). Hence these weighted laws strictly increase in monotone likelihood-ratio (and stochastic) order. Since \(a^{2r}\) is strictly increasing, \(A_m^+/A_m^-\), and thus \(w_m\), increases strictly with \(m\); also \(w_m>1/2\) for all \(m\ge1\). Therefore \(m(w_m-1/2)\) is strictly increasing for \(m\ge0\) if its value at \(m=0\) is set to zero. As \(k\) increases, \(m=n-k\) decreases, so \(\mu_k\) strictly decreases in \(k\). Reflection of all increments proves strict increase for \(p<1/2\). For \(p=1/2\), \(w_m=1/2\), so \(\mu_k=n/2\) at every \(k\).

Finally, for an independent copy \(K_n'\),
\[
2\operatorname{Cov}(K_n,U_n)=\mathbb E[(K_n-K_n')(\mu_{K_n}-\mu_{K_n'})].
\]
The right side has the asserted strict sign when \(p\ne1/2\), since the law of \(K_n\) has at least two support points; it vanishes exactly in the symmetric case. This proves the theorem.

## Verification
The standalone `verify_lastzero.py` enumerates all \(4^n\) sign paths for every \(n=1,\ldots,7\), evaluates exact rational path probabilities for five step biases, checks each cell of the analytical joint law, and checks the strict covariance sign (35 parameter combinations). The argument above proves the theorem for arbitrary \(n\) and real \(0<p<1\); finite checks do not replace the proof.

## Relationship to prior work
Chung and Feller's theorem gives uniform positive occupation time for a bridge; Lachal establishes and extends the exact biased-walk sojourn marginal and bridge laws (Theorem 6.2). The Hartmann–Majumdar Brownian calculation gives the *drift-free continuous-time* joint last-zero/occupation distribution and its zero covariance (2025, Section III.A); that result is not the biased Bernoulli finite-horizon theorem. The present strict drift-dependent sign and meander-odds likelihood-ratio result are the additions, rather than the classical bridge law or symmetric zero-covariance case.

## Limitations
This is for independent identically distributed nearest-neighbor signs and even horizons; it does not establish the sign for arbitrary skip-free processes, position-dependent transition probabilities, or a particular scaling of drift in a Brownian limit. Classical walk literature is extensive; a historically equivalent biased joint identity remains a priority risk.

## References
1. K.-L. Chung and W. Feller, “On fluctuations in coin-tossings,” *PNAS* **35** (1949), 605–608.
2. A. Lachal, “Sojourn time in \(\mathbb Z^+\) for the Bernoulli random walk on \(\mathbb Z\),” arXiv:1003.5009, first posted 2010-03-25; *ESAIM: Probability and Statistics* **16** (2012), 324–351. https://doi.org/10.1051/ps/2010013.
3. A. K. Hartmann and S. N. Majumdar, “Exact joint distributions of three global characteristic times for Brownian motion,” *Physical Review E* **111** (2025), 044134. https://doi.org/10.1103/PhysRevE.111.044134.
