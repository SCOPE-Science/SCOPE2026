# Exact prime-period sampling, discrepancy and transport for the full tent map

## Finding
Let \(T:[0,1]\to[0,1]\) be the full tent map \(T(x)=2\min\{x,1-x\}\). For each **prime integer** \(p\ge2\), let \(P_p\) be the finite set of points whose **least** period under \(T\) is exactly \(p\), and let \(\mu_p=|P_p|^{-1}\sum_{x\in P_p}\delta_x\). Put \(N=2^p\) and \(r_p=2/(N+1)\).

Then \(|P_p|=N-2\), and all three natural spatial errors are **exactly** \(r_p\):
\[
\sup_{0\le t\le1}\left|\mu_p([0,t])-t\right|
= W_\infty(\mu_p,\operatorname{Leb}_{[0,1]})
=\sup_{z\in[0,1]}\operatorname{dist}(z,P_p)
=\frac{2}{2^p+1}.
\]
Here the first quantity is one-dimensional star discrepancy, the second is bottleneck optimal transport for Euclidean distance, and the third is covering radius. The common lower bound is forced by the missing left endpoint: the smallest member of \(P_p\) is \(r_p\), and the discrepancy supremum is approached immediately to its left. For every odd prime \(p\), the largest gap between **consecutive** members of \(P_p\) is exactly \(2/(2^p-1)\), attained where the nonzero fixed point has been removed.

Consequently, for every \(L\ge0\), the minimax worst-case sup-norm error of recovering an arbitrary real-valued \(L\)-Lipschitz function on \([0,1]\) from its complete, noiseless values on \(P_p\) is **exactly** \(Lr_p\). The theorem concerns exact-period point locations and function sampling, not recovery of an unknown map from unordered periodic orbits.

## Assumptions and scope
We use Euclidean distance and normalized Lebesgue probability on \([0,1]\). The \(\infty\)-Wasserstein distance \(W_\infty(\nu,\eta)\) is the infimum, over all couplings \(\pi\), of the essential supremum of \(|x-y|\) under \(\pi\). Define \(D^*(P)=\sup_{t\in[0,1]}||P|^{-1}\#\{x\in P:x\le t\}-t|\). The exact prime period \(p\) means \(T^p(x)=x\) and \(T^q(x)\ne x\) for every integer \(1\le q<p\). No claim is made for the uniform measure on only one selected periodic orbit, or for arbitrary composite periods.

## Proof
**1. The complete finite period grid.** Write \(N=2^p\). On each dyadic interval \([j/N,(j+1)/N]\), \(0\le j<N\), the iterate \(T^p\) is linear: it equals \(Nx-j\) for even \(j\) and \(j+1-Nx\) for odd \(j\). Thus there is exactly one solution to \(T^p(x)=x\) in each interval, namely
\[
 a_j=\begin{cases}j/(N-1),&j\text{ even},\\(j+1)/(N+1),&j\text{ odd} .\end{cases}
\]
The values \(a_0<a_1<\cdots<a_{N-1}\) are distinct (interior crossings), so there are exactly \(N\) points fixed by \(T^p\). Since \(p\) is prime, the only points among them not of least period \(p\) are the fixed points of \(T\), namely \(0\) and \(2/3\). Thus \(|P_p|=N-2\). In particular \(a_1=2/(N+1)\) is the first member of \(P_p\).

**2. Exact discrepancy for odd primes.** Assume \(p\ge3\), hence \(N\ge8\), \(N\equiv2\pmod3\), and \(q=(2N-1)/3\) is an odd integer at least five. The removed fixed point \(2/3\) is precisely \(a_q\). Enumerate the surviving points as \(y_k\), \(1\le k\le M=N-2\). For a survivor \(a_j\), its rank is \(k=j\) if \(1\le j<q\), and \(k=j-1\) if \(q<j<N\).

For any ordered \(M\)-point set with points \(y_k\), inspection of the empirical cumulative distribution on the open intervals between jumps yields
\[
 D^*=\max_{1\le k\le M}\max\left\{\frac{k}{M}-y_k,\ y_k-\frac{k-1}{M}\right\}.
\]
Put \(r=2/(N+1)\). We establish both inequalities in each of the four rank/parity cases. First \(a_j\ge j/(N+1)\) always. For \(1\le j<q\),
\[
 \frac{k}{M}-a_j\le\frac{3j}{(N-2)(N+1)}\le r,
\]
since \(j\le q-1=2(N-2)/3\). For \(j>q\),
\[
 \frac{k}{M}-a_j\le\frac{3j-(N+1)}{(N-2)(N+1)}\le r,
\]
since \(j\le N-1\).

For the complementary discrepancy \(a_j-(k-1)/M\), if \(j<q\) is odd, it is
\[
 \frac{2N-1-3j}{(N+1)(N-2)}\le r,
\]
with equality at \(j=1\). If \(j<q\) is even, it is
\[
 \frac{N-1-j}{(N-1)(N-2)}\le\frac1{N-2}\le r.
\]
If \(j>q\) is odd, it equals
\[
 \frac{3(N-j)}{(N+1)(N-2)}\le r,
\]
because \(j\ge q+1\ge(N+4)/3\). Finally, for even \(j>q\), it equals
\[
 \frac{2(N-1)-j}{(N-1)(N-2)}\le r,
\]
because \(j\ge6>6(N-1)/(N+1)\). These exhaust all survivors. The lower bound \(D^*\ge r\) follows from the jump immediately before the first point \(y_1=r\). Hence \(D^*=r\). For \(p=2\), the exact-period set \(P_2=\{2/5,4/5\}\) gives the same formula directly.

**3. Transport and covering.** For any equally weighted sorted set \(\{y_1<\cdots<y_M\}\), couple a uniform variable \(U\) on \([0,1]\) with \(Y=y_k\) whenever \((k-1)/M<U\le k/M\). This coupling has maximal displacement exactly
\[
 \max_k\max\left\{\left|y_k-\frac{k-1}{M}\right|,\left|y_k-\frac{k}{M}\right|\right\}=D^*.
\]
It is optimal for the bottleneck cost: in any coupling with displacement at most \(d\), at least \(k/M\) mass must originate at or to the left of \(y_k+d\), and at least \((M-k+1)/M\) mass must originate at or to the right of \(y_k-d\). Thus \(y_k+d\ge k/M\) and \(y_k-d\le(k-1)/M\); consequently \(d\ge D^*\). It follows that \(W_\infty=D^*=r\). The explicit quantile coupling also shows every point of \([0,1]\) is at distance at most \(r\) from some member of \(P_p\). Conversely, the endpoint zero is at distance exactly \(r\) from \(P_p\), proving its covering radius is \(r\).

For completeness, if \(p\ge3\), two consecutive grid points \(a_j,a_{j+1}\) have differences \(2(N-1-j)/(N^2-1)\) for even \(j\), and \(2(j+1)/(N^2-1)\) for odd \(j\), both no greater than \(2/(N+1)\). Deleting \(a_q=2/3\) joins its two neighboring even-indexed grid points; their gap is \(a_{q+1}-a_{q-1}=2/(N-1)\), strictly larger than every undeleted gap. This gives the sharp largest-interior-gap claim.

**4. Minimax recovery.** Given values \(g(y)\), \(y\in P_p\), of an unknown \(L\)-Lipschitz function, define the lower and upper envelopes
\[
 g_-(x)=\max_{y\in P_p}\{g(y)-L|x-y|\},\qquad
 g_+(x)=\min_{y\in P_p}\{g(y)+L|x-y|\}.
\]
Every admissible function lies between them, and the midpoint \((g_-+g_+)/2\) has error at most \(L\operatorname{dist}(x,P_p)\le Lr\). Conversely, the two admissible functions \(\pm L\operatorname{dist}(x,P_p)\) have identical zero samples, while their values at zero are \(\pm Lr\); no reconstruction rule can have worst-case error below \(Lr\). Therefore the minimax error is exactly \(Lr\).

## Verification
The standalone pure-Python file `verify_prime_tent.py` evaluates the iterate and every exact least period using rational arithmetic; independently enumerates the fixed grid; evaluates the star-discrepancy maximum, interval covering radius, interior gap and individual inequality margins for primes \(p\in\{2,3,5,7,11,13\}\); and computes composite-period controls \(n\in\{4,6,8\}\). The completed execution passed 41,669 exact assertions. In particular, at composite \(n=6\), the discrepancy is \(2/63\) rather than \(2/65\), demonstrating why a prime-only theorem is mathematically substantive. These finite computations do not establish the general prime theorem; the preceding exhaustive symbolic proof does.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi (2026) prove qualitative rigidity of topologically mixing interval maps from their complete orbit spectra, and show that the union of prime-period points is decisive for rigidity. The theorem here instead determines the exact finite-stage spatial resolution of **one complete least-prime-period point set** for the full tent map, its empirical probability transport, and minimax sampling precision. Their rigidity result neither gives nor implies the exact rate \(2/(2^p+1)\); conversely, the present theorem does not establish rigidity from finitely many unordered orbits.

Gauthier and Vigny (2025) establish quantitative periodic-point equidistribution for complex rational maps and smooth observables. This broad result does not supply a sharp one-dimensional discrepancy, optimal-transport, or covering-radius identity for the nonrational piecewise-linear tent map. A 2019 review by Kumar and Gopalakrishnan explicitly records the count of fixed points of tent-map iterates, while classical descriptions give the affine geometry used in Step 1; that enumeration is not claimed as new. The novelty assessed here is its exact least-prime-period discrepancy/transport/covering conjunction and optimal finite sampling consequence. Historical priority under alternate discrepancy or symbolic sampling terminology remains a limitation.

## Limitations
The theorem is specific to the full-slope tent map on \([0,1]\), normalized Lebesgue measure, exact prime periods, and noiseless sampling. The covering/transport equality is not claimed for composite periods, individual prime orbits, other tent-map parameters, or arbitrary perturbations. Composite period \(n=6\) explicitly violates the displayed star-discrepancy formula. The Lipschitz recovery statement concerns observables whose values are known at every sample point; it does not recover maps from unlabeled orbit sets. No independent mathematical or bibliographic audit has been performed.

## References
1. G. Fuhrmann, M. Gröger, A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1, first public 2026-10-05. https://arxiv.org/abs/2610.07435
2. T. Gauthier, G. Vigny, *Quantitative equidistribution of periodic points for rational maps*, arXiv:2505.02608v1, first public 2025-05-05. https://arxiv.org/abs/2505.02608
3. M. Denesh Kumar, S. Gopalakrishnan, *Periodicity of the Tent Map* (2019), https://sriramgkn.github.io/reports/Tent_map_report.pdf (classical iterate fixed-point counts, §§2–3).
4. E. W. Weisstein, *Tent Map*, Wolfram MathWorld, https://mathworld.wolfram.com/TentMap.html (general map definition).
