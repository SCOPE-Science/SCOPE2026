# Wheel arboreal-gas spoke limits are determinantal renewal processes

## Finding

**Theorem (finite spoke law and infinite-volume identification).** For every integer \(n\ge3\) and every edge fugacity \(x>0\), let \(W_n=K_1+C_n\), and sample an unrooted spanning forest \(F\subseteq E(W_n)\) with probability proportional to \(x^{|F|}\). Write \(S_j=\mathbf1\{\text{the spoke from the hub to rim vertex }j\text{ belongs to }F\}\), with rim indices modulo \(n\). Define
\[
\Delta=\sqrt{1+2x+5x^2},\quad
\lambda_\pm=\frac{1+3x\pm\Delta}{2},\quad
q=\frac{\lambda_-}{\lambda_+},\quad
\eta=\frac{x}{\lambda_+},\quad
\rho=\frac{x}{\Delta}.
\]
All of these are real, \(0<q<1\), \(0<\eta<1\), and \(\rho>0\). The exact forest partition function is
\[
Z_n(x)=\lambda_+^n+\lambda_-^n-2x^n.
\]
If \(H\) is any nonempty selection of \(k\) distinct spokes, in cyclic order, and \(d_1,\ldots,d_k\) are its positive successive clockwise rim gaps (\(\sum_jd_j=n\)), then
\[
\boxed{\mathbb P_{n,x}(S_h=1\ \forall h\in H)
 =\frac{\rho^k\prod_{j=1}^k(1-q^{d_j})}{1+q^n-2\eta^n}.}
\tag{1}
\]
For a singleton \(H\), the only gap is \(n\).

For every fixed finite collection \(t_1<\cdots<t_k\) of integer indices, the spoke field on \(W_n\), embedded locally in \(\mathbb Z\), converges in finite-dimensional law as \(n\to\infty\) to the translation-invariant determinantal point process with correlation kernel
\[
\boxed{K_x(i,j)=\rho\,q^{|i-j|/2},\qquad i,j\in\mathbb Z.}\tag{2}
\]
In particular, its inclusion probabilities are
\[
\boxed{\mathbb P(S_{t_1}=\cdots=S_{t_k}=1)
 =\rho^k\prod_{j=1}^{k-1}(1-q^{t_{j+1}-t_j})
 =\det[K_x(t_i,t_j)]_{i,j=1}^k.}\tag{3}
\]
The same limit is a stationary renewal process: conditional on a spoke at the origin, consecutive gaps are independent with probability mass function
\[
\boxed{p_d=\frac{x((1+x)^d-x^d)}{\lambda_+^d},\qquad d=1,2,\ldots,\quad
\mathbb E[d]=\frac{\Delta}{x}.}\tag{4}
\]
For every finite wheel, all pairs of distinct spokes have *strictly negative* covariance. For distinct spokes at clockwise separation \(r\), where \(1\le r<n\), the joint inclusion probability is strictly increasing in the shorter circular separation \(\min(r,n-r)\). For each fixed positive integer \(r\),
\[
\boxed{\lim_{n\to\infty}\operatorname{Cov}_{n,x}(S_0,S_r)=-\rho^2q^r.}\tag{5}
\]

## Assumptions and scope

A spanning forest is an acyclic edge subset retaining every vertex, including isolated vertices. Each edge has the *same* positive fugacity \(x\), and the probability of a forest is \(x^{|F|}/Z_n(x)\). The edges consist of the \(n\) rim edges and the \(n\) hub spokes; \(W_3\) is the simple complete graph on four vertices. All finite identities hold for every \(n\ge3\) and \(x>0\). The limit fixes \(x\) and finitely many spoke positions while the rim size increases. There is no claim here about the joint field of rim edges or arbitrary edge-specific fugacities.

## Proof

**1. Decomposition into rim gaps.** Suppose the *exact* chosen spoke set is nonempty. Between two consecutive chosen spokes with clockwise gap \(d\), an acyclic configuration cannot contain all \(d\) intervening rim edges, because they would form a cycle through the hub. Conversely, excluding at least one rim edge in every such gap prevents all cycles: the occupied rim-edge components are paths, and each has at most one spoke attachment to the hub. The total fugacity for this gap, counting the spoke at its beginning, is therefore
\[
a_d=x\big((1+x)^d-x^d\big),\qquad d\ge1.
\]
The generating series is
\[
A(z)=\sum_{d\ge1}a_dz^d=\frac{xz}{(1-(1+x)z)(1-xz)}.
\]
When two endpoint spokes are forced but intermediate spokes are optional, sum over every positive composition of their clockwise separation. The total contribution of that interval is the coefficient \(u_d=[z^d]U(z)\), where
\[
U(z)=A(z)+A(z)^2+\cdots
=\frac{xz}{1-(1+3x)z+x(1+x)z^2}.
\]
Because \(\lambda_++\lambda_-=1+3x\), \(\lambda_+\lambda_-=x(1+x)\), and \(\lambda_+-\lambda_-=\Delta\), partial fractions yield
\[
u_d=\frac{x}{\Delta}(\lambda_+^d-\lambda_-^d),\qquad d\ge1.
\]
For a fixed nonempty *forced* spoke set \(H\) with cyclic gaps \(d_1,\ldots,d_k\), every forest containing those spokes is uniquely decomposed over its \(k\) intervals. Its unnormalized weight is thus \(\prod_{j=1}^ku_{d_j}\), including the singleton case with one gap of size \(n\).

**2. Partition function.** With no selected spokes, the rim must be a proper edge subset of the cycle, giving weight \((1+x)^n-x^n\). With \(k\ge1\) selected spokes, counting the choice of one marked spoke and then dividing by \(k\), the total weight is \(\frac nk[z^n]A(z)^k\). The sum over all \(k\) therefore gives
\[
Z_n(x)=(1+x)^n-x^n+n[z^n]\big(-\log(1-A(z))\big).
\]
Now
\[
1-A(z)=\frac{(1-\lambda_+z)(1-\lambda_-z)}{(1-(1+x)z)(1-xz)},
\]
so the displayed logarithm identity, valid as formal power series at the origin, yields
\[
Z_n(x)=\lambda_+^n+\lambda_-^n-2x^n.
\]
Dividing the forced-spoke weight by \(Z_n(x)\), and factoring \(\lambda_+^n\), proves (1). Positivity follows from the underlying forest enumeration. Explicitly \(\lambda_->0\) since \(\lambda_+\lambda_-=x(1+x)>0\) and \(\lambda_++\lambda_->0\), and \(\lambda_+>1+x>x\), establishing the parameter bounds.

**3. Local limit and determinant.** For fixed integer positions \(t_1<\cdots<t_k\) on increasingly large rims, the final wrapping gap tends to infinity, whereas the other gaps remain \(t_{j+1}-t_j\). Since \(0<q,\eta<1\), formula (1) tends to the first product in (3). Let \(a=\sqrt q\). The symmetric matrix with entries \(a^{|t_i-t_j|}\) is the covariance matrix of a stationary unit-variance Gaussian Markov chain restricted to the listed times. Sequential conditional variances are \(1-a^{2(t_{j+1}-t_j)}\); equivalently, Gaussian elimination gives
\[
\det[a^{|t_i-t_j|}]_{i,j=1}^k
=\prod_{j=1}^{k-1}(1-a^{2(t_{j+1}-t_j)}).
\]
Scaling by \(\rho\) proves the determinant identity (3). This is a genuine determinantal kernel: the Toeplitz operator on \(\ell^2(\mathbb Z)\) has Fourier multiplier
\[
\widehat K_x(\theta)=\rho\frac{1-q}{1-2\sqrt q\cos\theta+q}>0,
\]
whose maximum equals
\[
\rho\frac{1+\sqrt q}{1-\sqrt q}
=\frac{x}{1+3x-2\sqrt{x(1+x)}}<1.
\]
The strict inequality reduces to \(1+2x>2\sqrt{x(1+x)}\), whose squared difference is exactly \(1\). Hence \(0<K_x<I\) as a bounded operator, and its principal-minor correlation functions specify a DPP. Finite inclusion probabilities determine every finite joint \(0/1\) law by inclusion-exclusion; convergence of all such probabilities establishes finite-dimensional distribution convergence.

**4. Renewal representation.** Let \(p_d=a_d\lambda_+^{-d}\). The equation \(1-A(\lambda_+^{-1})=0\) shows \(\sum_{d\ge1}p_d=1\); all terms are positive. Differentiation of \(A\), or differentiation of its denominator at \(\lambda_+^{-1}\), gives
\[
\sum_{d\ge1}d p_d=\lambda_+^{-1}A'(\lambda_+^{-1})=\frac{\Delta}{x}=\rho^{-1}.
\]
Thus a stationary renewal process with these gaps has intensity \(\rho\). The renewal mass function for reaching a second spoke \(d\) steps later is
\[
[z^d]\frac{A(z/\lambda_+)}{1-A(z/\lambda_+)}
=\frac{u_d}{\lambda_+^d}=\rho(1-q^d).
\]
Its multi-point inclusion probabilities therefore factor as \(\rho\prod_j\rho(1-q^{t_{j+1}-t_j})\), precisely (3). These inclusion functions determine the law, proving (4), including independence of successive gaps under Palm conditioning.

**5. Finite-volume strict correlation and distance law.** Put \(D_n=1+q^n-2\eta^n\). By (1),
\[
\mathbb P(S_0=1)=\frac{\rho(1-q^n)}{D_n},\qquad
\mathbb P(S_0=S_r=1)=\frac{\rho^2(1-q^r)(1-q^{n-r})}{D_n}.
\]
Write \(u=q^r\), \(v=q^{n-r}\), so \(uv=q^n\) and \(0<u,v<1\). Since \(0<D_n<1+uv\), it suffices to show
\[
(1-uv)^2>(1+uv)(1-u)(1-v).
\]
Their difference is \((1+uv)(u+v)-4uv\), which is bounded below by
\[
2\sqrt{uv}(1-\sqrt{uv})^2>0
\]
by arithmetic–geometric mean. This proves strict negative covariance. Moreover \((1-q^r)(1-q^{n-r})=1+q^n-q^r-q^{n-r}\) increases strictly while \(r\) increases from \(1\) toward \(\lfloor n/2\rfloor\): the expression \(q^r+q^{n-r}\) strictly decreases until the midpoint. Taking \(n\to\infty\) with fixed \(r\) yields (5).

## Verification

The standalone standard-library program `check_wheel.py` enumerates all acyclic edge subsets on \(W_n\) for \(3\le n\le7\), at each fugacity \(x\in\{1/2,1,2\}\). It verifies every forced-spoke subset against the gap formula, all spoke-pair strict negative covariances and the circular-distance ordering: **822 exact rational assertions**. Independently it verifies the exponential Toeplitz determinant factorization on all subsets of at most five indices among nine positions, at three rational kernel bases: **1143 exact assertions**. It reports `PASS 822 exact wheel-forest inclusion and covariance tests; 1143 exact Toeplitz determinant tests`.

These are bounded checks only. Statements for all wheel sizes, fugacities and infinite-volume convergence rely on the analytic proof above; the code alone does not certify them.

## Relationship to prior work

Bauerschmidt, Crawford, Helmuth and Swan (2019 preprint) establish the general arboreal-gas setting and discuss the broader edge-negative-correlation conjecture. Erickson (2010) proves the forest Rayleigh property for series-parallel graphs; wheel graphs already contain a \(K_4\) minor and fall outside that theorem. Çiçeksiz and Ravichandran (2026) study general-graph correlations at sufficiently large fugacity and other settings, without a stated all-fugacity wheel-spoke limit.

**Essential overlap acknowledgement:** Bado, *Negative edge correlation for uniform random forests on wheel graphs* (published online in 2026), already proves all edge-pair strict negative correlations for the **uniform** \(x=1\) wheel forest and the \(x=1\) specialization of the partition-function formula, using a multivariate transfer matrix. Those are not claimed as new. The present finding is the all-positive-fugacity, all-order spoke inclusion law and its explicit stationary renewal/determinantal infinite-volume identification. The accessible Bado abstract does not state this process-level conclusion; its full paper text was unavailable for complete comparison. A transfer-matrix derivation may contain related finite identities, so historical priority of parts of (1) remains a material residual risk. The other cited works and the available research-result catalog did not identify an equivalent infinite-volume theorem.

## Limitations

Only hub-spoke indicators are characterized, not arbitrary rim-edge or mixed edge sets. Fugacity is common to all edges and fixed with \(n\), and the local limit is for finitely many fixed spoke coordinates. The finite spoke distribution is **not** asserted to be determinantal. The correlation statement concerns pairs of spokes only; it neither proves all-edge negative correlation at arbitrary fugacity nor complete negative association. The 2026 wheel-forest paper's full text was not available for exhaustive overlap inspection. Independent review and historical-priority certification are not claimed.

## References

1. R. Bauerschmidt, N. Crawford, T. Helmuth and A. Swan, *Random spanning forests and hyperbolic symmetry*, arXiv:1912.04854, first publicly posted 2019-12-10, https://arxiv.org/html/1912.04854v2 ; *Communications in Mathematical Physics* 381 (2021), https://doi.org/10.1007/s00220-020-03921-y .
2. A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660, 2010, https://ar5iv.labs.arxiv.org/html/1008.3660 .
3. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlation for Forests and the q<1 Random-Cluster Model*, arXiv:2610.00549, first posted 2026-09-30, https://arxiv.org/html/2610.00549v1 .
4. I. O. Bado, *Negative edge correlation for uniform random forests on wheel graphs*, *Statistics and Probability Letters* 241 (2027 issue; online 2026), https://doi.org/10.1016/j.spl.2026.110960 ; abstract https://eurekamag.com/research/110/454/110454088.php .
5. F. Bencs and P. Csikvári, *Upper bound for the number of spanning forests of regular graphs*, arXiv:2105.06801, first posted 2021-05-14, https://arxiv.org/html/2105.06801v3 .
