# Lower moment thresholds for independent-coordinate high-dimensional random walks
## Finding
Fix \(p\in(1,\infty)\) and let \(d=d(n)\to\infty\). Let \((\xi_{j,i})_{j,i\ge1}\) be iid real random variables with
\[
\mathbb E\xi_{1,1}=0,\qquad \mathbb E\xi_{1,1}^2=\sigma^2\in(0,\infty),\qquad \mathbb E|\xi_{1,1}|^{r_p}<\infty,
\]
where
\[
r_p=\max\{2,2p-2\}.
\]
For each dimension \(d\), define
\[
X_j^{(d)}=d^{-1/p}(\xi_{j,1},\ldots,\xi_{j,d}),\qquad S_k^{(d)}=\sum_{j=1}^kX_j^{(d)},
\]
and let \(\mathcal Z_n^{(d)}=\{S_0^{(d)},\ldots,S_n^{(d)}\}\). If \(M_p=\mathbb E|N(0,1)|^p\), then
\[
\left(n^{-1/2}\mathcal Z_n^{(d)},\|\cdot\|_p\right)\xrightarrow{P}_{GH}
\left([0,1],\sigma M_p^{1/p}\sqrt{|t-s|}\right).
\]
Hence independent coordinates allow Jin's finite \(2p\)-moment assumption to be replaced by finite variance for \(1<p\le2\), and by a finite \((2p-2)\)-moment for \(p>2\), without imposing a relation between \(n\) and \(d(n)\). The \(p=2\) case is prior; the new range is \(p\ne2\).

## Assumptions and scope
The coordinates are independent, not merely uncorrelated. This strengthening is essential to the proof because it replaces the bivariate \(2p\)-moment estimate used for fixed-time concentration by a triangular weak law across coordinates. The time increments are iid, and the scalar coordinate law does not depend on \(d\). The theorem concerns Gromov--Hausdorff convergence of the random walk path as a finite metric space; it does not claim a functional limit in a fixed ambient \(\ell_p\) space.

For \(1<p<2\), the assumption is only \(\mathbb E\xi_{1,1}^2<\infty\). For \(p=2\), it again reduces to finite variance. For \(p>2\), the required order is \(2p-2\), strictly below Jin's \(2p\).

## Proof
Write \(\widehat S_{m,i}=\sum_{j=1}^m\xi_{j,i}\). For fixed \(t\in[0,1]\),
\[
n^{-p/2}\|S_{\lfloor nt\rfloor}^{(d)}\|_p^p
=\frac1d\sum_{i=1}^d n^{-p/2}|\widehat S_{\lfloor nt\rfloor,i}|^p.
\]
The scalar central limit theorem together with convergence of absolute \(p\)-moments gives
\[
\mathbb E\left|n^{-1/2}\widehat S_{\lfloor nt\rfloor,1}\right|^p
\longrightarrow t^{p/2}\sigma^pM_p.
\]
For \(1<p<2\), finite variance suffices for this moment convergence; for \(p\ge2\), it follows from the finite \(p\)-moment, which is implied by the assumed \(r_p\)-moment. The random variables
\[
Y_n(t)=n^{-p/2}|\widehat S_{\lfloor nt\rfloor,1}|^p
\]
are therefore uniformly integrable for each fixed \(t\). Since the coordinate copies are iid, a truncation argument yields the triangular weak law
\[
\frac1d\sum_{i=1}^dY_{n,i}(t)-\mathbb EY_n(t)\xrightarrow{P}0
\]
for every sequence \(d=d(n)\to\infty\): truncate at a fixed level \(K\), use variance at most \(K^2/d\) for the bounded part, and then let \(K\to\infty\) using uniform integrability. Thus the fixed-time norm limit holds under the reduced moment assumption.

To obtain uniformity in time, use Jin's convexity decomposition
\[
\|S_m^{(d)}\|_p^p=T_m^{(d)}+Q_m^{(d)},
\]
where \(T_m^{(d)}\) is nondecreasing and
\[
Q_m^{(d)}=p\sum_{i=1}^d\sum_{j=1}^m X_{j,i}^{(d)}S_{j-1,i}^{(d)}|S_{j-1,i}^{(d)}|^{p-2}
\]
is a martingale. Coordinate independence and temporal independence eliminate all cross terms in its second moment. Put \(q=2p-2\). For \(q\ge2\), the Marcinkiewicz--Zygmund bound gives
\[
\mathbb E|\widehat S_{m,1}|^q\le C_p m^{q/2}\mathbb E|\xi_{1,1}|^q.
\]
For \(0<q<2\), finite variance gives the same power bound by Lyapunov's inequality,
\[
\mathbb E|\widehat S_{m,1}|^q\le (m\sigma^2)^{q/2}.
\]
After inserting the factor \(d^{-1/p}\) from each coordinate of \(X_j^{(d)}\), these estimates imply
\[
\mathbb E|Q_n^{(d)}|^2\le C_p\frac{n^p}{d}.
\]
Consequently
\[
n^{-p}\mathbb E|Q_n^{(d)}|^2\to0,
\]
and Doob's inequality gives
\[
n^{-p/2}\max_{0\le m\le n}|Q_m^{(d)}|\xrightarrow{P}0.
\]
The fixed-time limit for \(\|S_m^{(d)}\|_p^p\) therefore transfers to \(T_m^{(d)}\). Its monotonicity upgrades fixed-time convergence on a finite grid to
\[
\sup_{t\in[0,1]}\left|n^{-p/2}\|S_{\lfloor nt\rfloor}^{(d)}\|_p^p-t^{p/2}\sigma^pM_p\right|\xrightarrow{P}0.
\]

The same argument applies to every translated block of increments. Following the finite-grid and short-block decomposition used for Jin's uniform metric theorem, stationarity gives convergence on a fixed time grid. For a block of length at most \(n/m\), monotonicity of \(T^{(d)}\) controls the convex part, while Doob's inequality and the bound above give, for fixed \(m\),
\[
m\,n^{-p}\mathbb E|Q_{\lfloor n/m\rfloor}^{(d)}|^2\le \frac{C_p}{d\,m^{p-1}}\longrightarrow0.
\]
Letting first \(n\to\infty\) and then \(m\to\infty\) yields
\[
\sup_{0\le s\le t\le1}
\left|n^{-1/2}\|S_{\lfloor nt\rfloor}^{(d)}-S_{\lfloor ns\rfloor}^{(d)}\|_p-
\sigma M_p^{1/p}\sqrt{t-s}\right|\xrightarrow{P}0.
\]
The standard correspondence that pairs the walk point \(S_{\lfloor nt\rfloor}^{(d)}\) with \(t\in[0,1]\) has distortion at most twice this supremum. The asserted Gromov--Hausdorff convergence follows.

## Verification
The critical exponent in the martingale calculation is \(2p-2\), not \(2p\): squaring the derivative term \(S|S|^{p-2}\) produces \(|S|^{2p-2}\). The dimension powers cancel to \(d^{-1}\): one factor \(d\) comes from summing coordinates, while the squared increment and the \((2p-2)\)-power of the partial sum contribute \(d^{-2/p}\) and \(d^{-(2p-2)/p}\), respectively. Thus the martingale variance is of order \(n^p/d\).

The fixed-time step is independently checked by the triangular truncation lemma: if \((Y_n)\) is uniformly integrable and \(Y_{n,1},\ldots,Y_{n,d(n)}\) are iid copies with \(d(n)\to\infty\), then their empirical mean minus \(\mathbb EY_n\) converges to zero in probability. No second moment of \(Y_n\) is needed.

## Relationship to prior work
Jin's theorem assumes identically distributed, centered, pairwise uncorrelated coordinates with a finite \(2p\)-moment and proves the same Gromov--Hausdorff limit. The present result trades stronger coordinate structure--full independence--for a weaker tail requirement. The paper itself notes at \(p=2\) that its fourth-moment assumption is stronger than the finite second moment available in the earlier Wiener-spiral theorem.

Kabluchko and Marynych already prove the \(p=2\) iid-coordinate case under finite second moment, so that specialization is not new. Their theorem is Hilbertian and does not imply the non-Hilbert \(p\ne2\) statement. Targeted searches for the non-Hilbert independent-coordinate theorem with the \(2p-2\) threshold did not identify a prior statement.

## Limitations
The result does not prove that \(r_p=\max\{2,2p-2\}\) is necessary or optimal. It also does not weaken Jin's moment condition under mere pairwise uncorrelatedness; independence is used materially. For \(p=2\), the conclusion under finite variance is prior work, and no originality is claimed for that specialization.

## References
1. B. Jin, “Convergence of Random Walks in \(\ell_p\)-Spaces of Growing Dimension,” arXiv:2512.03873v1, first public 2025-12-03; Modern Stochastics: Theory and Applications 13 (2026), 375--385, DOI 10.15559/26-VMSTA299.
2. Z. Kabluchko and A. Marynych, “Random Walks in the High-Dimensional Limit I: The Wiener Spiral,” arXiv:2211.08538; Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 60 (2024), 2945--2974, DOI 10.1214/23-AIHP1406.
