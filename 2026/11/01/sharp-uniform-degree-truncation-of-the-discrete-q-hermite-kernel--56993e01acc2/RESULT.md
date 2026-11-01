# Sharp uniform degree truncation of the discrete \(q\)-Hermite kernel

## Finding

Fix \(0<q<1\). Let \(h_0(x;q)=1\), \(h_1(x;q)=x\), and let the **monic discrete \(q\)-Hermite I polynomials** satisfy
\[
h_{n+1}(x;q)=x h_n(x;q)-q^{n-1}(1-q^n)h_{n-1}(x;q)\quad(n\ge1).
\]
Write
\[
w_q(x)=\prod_{j=1}^{\infty}(1-q^{2j}x^2),\qquad C_q=\prod_{j=1}^{\infty}(1-q^{2j})>0.
\]
For \(N\ge0\) define the **unclipped, unnormalized polynomial-feature kernel**
\[
K_{q,N}(x,y)=w_q(x)w_q(y)\sum_{n=0}^{N}h_n(x;q)h_n(y;q),\qquad x,y\in[-1,1].
\]
Then \(K_{q,N}\) has a uniformly convergent limit \(K_{q,\infty}\) on \([-1,1]^2\). Its **sharp, global degree-truncation error** is
\[
\boxed{\lim_{N\to\infty}N\max_{x,y\in[-1,1]}|K_{q,\infty}(x,y)-K_{q,N}(x,y)|=\frac{C_q^4}{e}.}
\]
For all sufficiently large \(N\), the diagonal truncation error has exactly two global maximizers \(\pm x_{q,N}\), with \(x_{q,N}\in(0,1)\), and
\[
\boxed{x_{q,N}=1-\frac1{2N}+O_q(N^{-2}).}
\]
The unweighted polynomial basis obeys the additional sharp norm law
\[
\boxed{\lim_{n\to\infty}n\max_{|x|\le1}|h_n(x;q)|=\frac{2C_q}{e}.}
\]
The positive norm-maximizers have \(1-x\sim n^{-1}\); every global maximizer of the kernel-tail diagonal has \(1-|x|\sim(2N)^{-1}\).

## Assumptions and scope

All limits keep \(q\in(0,1)\) **fixed**. The product defining \(w_q\) is not numerically truncated or replaced by a clipped weight. The coefficient of each polynomial feature is exactly one; these are not orthonormalized features. The uniform norm of a kernel is taken over the full real square \([-1,1]^2\), and the degree sum runs over \(0\le n\le N\). Neither a joint limit in \(q,N\) nor the empirically clipped kernel is covered.

## Proof

**1. Exact polynomial expansion.** Let \((a;r)_k=\prod_{j=0}^{k-1}(1-ar^j)\). The standard discrete \(q\)-Hermite I coefficient formula (DLMF 18.27.21) is
\[
h_n(x;q)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{(-1)^kq^{k(k-1)}(q;q)_n}{(q^2;q^2)_k(q;q)_{n-2k}}x^{n-2k}.
\tag{1}
\]
It also follows directly by substitution in the stated three-term recurrence (a finite coefficient check is given in `CHECK.py`). Fix \(\delta=(1+q)/2\), so \(q<\delta<1\). Define
\[
F_q(x)=(x^{-2};q^2)_\infty=\prod_{k=0}^{\infty}(1-q^{2k}/x^2),\quad \delta\le x\le1.
\]
Euler's \(q\)-binomial identity gives
\[
F_q(x)=\sum_{k\ge0}\frac{(-1)^kq^{k(k-1)}}{(q^2;q^2)_k}x^{-2k}.
\tag{2}
\]
Set \(R_{n,k}=(q;q)_n/(q;q)_{n-2k}=\prod_{j=0}^{2k-1}(1-q^{n-j})\) for \(k\le n/2\). For \(0\le k\le n/4\),
\[
0\le1-R_{n,k}\le\sum_{j=0}^{2k-1}q^{n-j}\le\frac{q^{n/2}}{1-q}.
\tag{3}
\]
For \(k>n/4\), the factor \(q^{k(k-1)}\) dominates every exponential factor \(\delta^{-2k}\). Splitting (1) and (2) at \(n/4\) therefore shows, for some \(0<\rho_q<1\) and constants \(B_{q,r}\),
\[
\sup_{\delta\le x\le1}\left|\partial_x^r\big(h_n(x;q)-x^nF_q(x)\big)\right|
\le B_{q,r}\rho_q^n,\quad r=0,1,2.
\tag{4}
\]
Differentiation only introduces polynomial factors in \(n\), absorbable by taking \(\rho_q>\sqrt q\). On \(0\le x\le\delta\), split (1) instead into \(k\le n/4\), where \(x^{n-2k}\le\delta^{n/2}\), and \(k>n/4\), where \(q^{k(k-1)}\) is superexponentially small. Thus
\[
\sup_{0\le x\le\delta}|h_n(x;q)|\le B_q\rho_q^n
\tag{5}
\]
with a possibly enlarged \(\rho_q<1\). Parity, \(h_n(-x;q)=(-1)^nh_n(x;q)\), treats negative \(x\).

**2. The endpoint layer and uniform summability.** Since \(\delta>q\), the factors of \(F_q\) after the first are positive on \([\delta,1]\). Thus its only zero there is simple, and
\[
F_q(x)=-(2C_q+O_q(1-x))(1-x),\qquad w_q(x)=C_q+O_q(1-x).
\tag{6}
\]
For \(s\ge0\) fixed, (4) and (6) yield, uniformly for \(s\) in bounded intervals,
\[
n h_n(1-s/n;q)\longrightarrow-2C_q s e^{-s}.
\tag{7}
\]
The polynomial sequence is exponentially small on \([0,\delta]\) by (5); on \([\delta,1]\), (4), (6), and \(x^n\le e^{-n(1-x)}\) control the range \(n(1-x)\to\infty\) by a constant times \(n(1-x)e^{-n(1-x)}\). The unique maximum of \(s e^{-s}\) is at \(s=1\). This proves the sharp polynomial norm law and \(\|h_n\|_{\infty}=O_q(n^{-1})\). Consequently the series defining \(K_{q,\infty}\) converges absolutely and uniformly on \([-1,1]^2\).

**3. Uniform approximation of the tail.** Define
\[
E_{q,N}(x)=K_{q,\infty}(x,x)-K_{q,N}(x,x)
=w_q(x)^2\sum_{n>N}h_n(x;q)^2\ge0.
\]
Squaring (4), summing the geometrically small cross terms, and using the geometric series gives, uniformly for \(\delta\le x\le1\),
\[
E_{q,N}(x)=x^{2N+2}G_q(x)+O_q(\rho_q^N),
\qquad G_q(x)=\frac{w_q(x)^2F_q(x)^2}{1-x^2}.
\tag{8}
\]
At \(x=1\), define \(G_q(1)=0\) by continuity. The remainder in (8) also holds after one or two derivatives on any fixed neighborhood of \(x=1\) contained in \((\delta,1]\): differentiate the summably small terms in (4). By (5), \(E_{q,N}(x)=O_q(\rho_q^N)\) for \(0\le x\le\delta\). Equation (6) implies
\[
G_q(x)=2C_q^4(1-x)+O_q((1-x)^2).
\tag{9}
\]
Set \(s=N(1-x)\). On compact \(s\)-intervals, (8)--(9) give
\[
N E_{q,N}(1-s/N)\longrightarrow2C_q^4 s e^{-2s}.
\tag{10}
\]
For \(x\in[\delta,1]\), the bound \(G_q(x)\le B_q(1-x)\), combined with \(x^{2N+2}\le e^{-2N(1-x)}\), proves that all regions with \(s\to\infty\) contribute negligibly after multiplication by \(N\). By (5), the remaining interior contributes negligibly as well. The unique maximum of \(s e^{-2s}\) is at \(s=1/2\), with value \(1/(2e)\). Hence
\[
\max_{x\in[-1,1]}E_{q,N}(x)=\frac{C_q^4}{eN}+o_q(N^{-1}).
\tag{11}
\]

**4. Sharp two-variable error and location.** The kernel difference is a Gram kernel of the real feature tails \((w_q(x)h_n(x;q))_{n>N}\). Cauchy--Schwarz shows
\[
|K_{q,\infty}(x,y)-K_{q,N}(x,y)|\le\sqrt{E_{q,N}(x)E_{q,N}(y)}\le\max_u E_{q,N}(u).
\]
Equality is attained when \(x=y\) is a diagonal maximizer. Thus (11) is the claimed global sharp constant.

For eventual uniqueness, on a sufficiently short fixed interval immediately to the left of \(1\), write \(G_q(x)=(1-x)V_q(x)\), where \(V_q\) is positive with bounded first two derivatives. The logarithmic second derivative of the main term in (8) is
\[
-\frac{2N+2}{x^2}-\frac1{(1-x)^2}+(\log V_q)''(x)<0
\]
for all large \(N\). The global maximizing region is contained in \(1-x\in[b/N,a/N]\) for any fixed \(0<b<1/2<a\) eventually, by the strict maximum in (10) and the tail bounds. There the second derivative of the main term is strictly negative of order \(N\); the \(C^2\) error in (8) is exponentially small. Therefore \(E_{q,N}\) is strictly concave on that region and has a unique positive global maximizer. At its critical point, (8) and the logarithmic derivative of the main term imply
\[
\frac{2N+2}{x}-\frac1{1-x}+(\log V_q)'(x)=O_q(N\rho_q^N),
\]
which gives \(1-x=1/(2N)+O_q(N^{-2})\). Parity gives precisely the two diagonal maximizers \(\pm x_{q,N}\).

## Verification

The self-contained `CHECK.py` uses exact rational arithmetic to compare (1) against the recurrence for degrees zero through twenty and three rational values of \(q\); it also checks the endpoint identity \(h_n(1;q)=q^{n(n-1)/2}\) and the finite-product factorization of the weight. Independent floating-point recurrence calculations for several fixed \(q\) and increasing \(N\) compare the measured scaled tail to \(C_q^4/e\) and the maximizing location to \(N(1-x)=1/2\). The numerical checks are supplementary: the infinite-dimensional uniform limits and extremal assertions follow from (3)--(11), not from finite sampling. Run `python CHECK.py` with Python 3.9 or later.

## Relationship to prior work

The unscaled feature kernel and its discrete \(q\)-Hermite I recurrence appear in Sánchez-Paniagua Ríos, Llerena, Lastra, Torrado and Huertas (2026), equations (10), (13)--(14), and their finite-degree boundedness discussion. Their Proposition 1 gives an upper bound that grows exponentially with the degree and does not imply the sharp polynomial decay or any optimal infinite-degree truncation rate. Their finite-degree positivity argument alone likewise does not imply convergence of the infinite series. DLMF 18.27.21 supplies the known explicit coefficient formula (1), a premise rather than the new asymptotic conclusion. Alwhishi, Sevinik Adıgüzel and Turan (2019), Sections 2--3, study the degeneration as \(q\) tends to one, not the fixed-\(q\), degree-to-infinity kernel limit. Cao's 2025 Poisson kernels concern multivariable \(q\)-3D Hermite families and weighted generating sums, not the unweighted monic discrete \(q\)-Hermite I kernel tail on \([-1,1]^2\). The decisive additional steps here are the uniform exterior-to-endpoint approximation (4), its boundary-layer optimization, and reduction of the full kernel uniform norm to the diagonal.

## Limitations

The assertion is for fixed \(q\in(0,1)\), on the entire real interval \([-1,1]\), and uses the **unclipped** exact bivariate product weight. It does not address the degree-dependent or joint \(q\uparrow1\) regime, nor the separately clipped practical variant mentioned in the motivating paper. The infinite-feature kernel is positive definite, but no claim about classifier performance, learning rates or Mercer eigenvalue decay is made. Independent mathematical audit remains unperformed. Earlier unindexed boundary-layer or q-Mehler specializations might contain an equivalent statement; this remains a literature risk.

## References

1. Á. Sánchez-Paniagua Ríos, J. P. Llerena, A. Lastra, N. Torrado, E. J. Huertas, *Beyond the Gegenbauer Paradigm: q-Orthogonal Kernels for Machine Learning*, arXiv:2608.03482, first publicly posted 2026-08-04, equations (10), (13)--(14), Proposition 1, Sections 3--4. https://arxiv.org/abs/2608.03482
2. NIST Digital Library of Mathematical Functions, §18.27(vii), equation 18.27.21 (discrete q-Hermite I coefficients). https://dlmf.nist.gov/18.27.E21
3. J. Cao, *Poisson kernels of q-3D Hermite polynomials expansion for functions of several variables via generalized q-heat equations*, Transactions of the London Mathematical Society 12 (2025), e70015, https://doi.org/10.1112/tlm3.70015
4. S. Alwhishi, R. Sevinik Adıgüzel and M. Turan, *On the limit of discrete q-Hermite I polynomials*, Communications Faculty of Sciences University of Ankara 68 (2019), 2272--2282, https://doi.org/10.31801/cfsuasmas.529703
