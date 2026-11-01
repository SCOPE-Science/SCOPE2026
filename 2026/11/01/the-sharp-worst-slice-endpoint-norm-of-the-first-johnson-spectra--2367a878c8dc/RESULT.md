# The sharp worst-slice endpoint norm of the first Johnson spectral projection

## Finding
For integers \(n\ge2\) and \(1\le k\le n-1\), let \(\Omega_{n,k}=\{A\subseteq\{1,\ldots,n\}:|A|=k\}\) have uniform probability measure. Let \(P_{n,k}\) be the orthogonal projector in \(L^2(\Omega_{n,k})\) onto the \((n-1)\)-dimensional space of degree-one harmonic functions
\[
\mathcal H_{n,k}^{(1)}=\left\{A\longmapsto\sum_{i\in A}c_i:\sum_{i=1}^n c_i=0\right\}.
\]
Write \(\Lambda_{n,k}=\|P_{n,k}\|_{\ell^\infty\to\ell^\infty}\). The first Johnson primitive idempotent has the exact, attained norm
\[
\Lambda_{n,k}=\frac{2(n-1)(k-b)^2}{k(n-k)}\frac{\binom{k}{b}\binom{n-k}{k-b}}{\binom nk},\qquad b=\left\lfloor\frac{k^2}{n}\right\rfloor.
\]
The central new assertion is the sharp **optimization over all slice widths**:
\[
\boxed{\lim_{n\to\infty}\frac1{\sqrt n}\max_{1\le k<n}\Lambda_{n,k}=\sqrt{\frac2e}.}
\]
If \(k_n\) is any maximizing width, then necessarily
\[
\boxed{\frac{\min\{k_n,n-k_n\}}{\sqrt n}\longrightarrow\frac1{\sqrt2}.}
\]
Conversely, any sequence with \(\min\{k_n,n-k_n\}/\sqrt n\to1/\sqrt2\) attains the limiting maximum. Thus the worst first-harmonic endpoint amplification occurs on *thin* slices, not balanced ones. The universal balanced/bulk constant is instead \(\sqrt{2/\pi}<\sqrt{2/e}\).

The crossover profile is explicit: if \(\min\{k_n,n-k_n\}/\sqrt n\to c>0\), then
\[
\frac{\Lambda_{n,k_n}}{\sqrt n}\to F(c^2),\qquad
F(t)=\frac{2t^{\lfloor t\rfloor+1/2}e^{-t}}{\lfloor t\rfloor!}.
\]
The function \(F\) is continuous, has a strict local minimum at every positive integer, and has a strict local maximum at every positive half-integer. These local maxima decrease strictly; the unique global maximum is \(F(1/2)=\sqrt{2/e}\).

## Assumptions and scope
Everything is finite, real or complex valued, and equipped with uniform normalized counting measure. For operator norms \(\ell^\infty\) means the maximum coordinate modulus; \(\ell^1\) is the corresponding normalized counting norm. The first harmonic excludes constants. The maximum is over the full sequence of Johnson schemes with fixed ground-set cardinality \(n\), and the optimizer is characterized asymptotically, not claimed unique for each finite \(n\). Complementation of subsets identifies \(\Lambda_{n,k}\) and \(\Lambda_{n,n-k}\).

## Proof
**Kernel.** For \(A\in\Omega_{n,k}\), set \(z_A=\mathbf1_A-(k/n)\mathbf1\), a vector in the zero-sum subspace of \(\mathbb R^n\). By exchangeability, the covariance operator \(\mathbb E(z_Bz_B^{\mathsf T})\) is \(k(n-k)/[n(n-1)]\) times the identity on that subspace. Consequently the projection kernel (with respect to *normalized* measure) is
\[
K_{n,k}(A,B)=\frac{n(n-1)}{k(n-k)}\left(|A\cap B|-\frac{k^2}{n}\right).
\]
This also gives \(K_{n,k}(A,A)=n-1\), as required for a rank-\((n-1)\) projector. Permutation symmetry makes every row have the same absolute sum. For independent uniform \(A,B\), the intersection size \(J=|A\cap B|\) has mass
\[
p_j=\frac{\binom{k}{j}\binom{n-k}{k-j}}{\binom nk},\quad \max(0,2k-n)\le j\le k,\qquad \mu=\mathbb EJ=\frac{k^2}{n}.
\]
Thus \(\Lambda_{n,k}=n(n-1)\mathbb E|J-\mu|/[k(n-k)]\). Signs of one kernel row provide attaining real inputs.

**Exact boundary collapse.** Extend the masses by zero outside their support and set \(u_j=(k-j)^2p_j\). The adjacent-binomial identity gives, for every integer \(j\),
\[
(k-j+1)^2p_{j-1}=j(n-2k+j)p_j,
\qquad u_{j-1}-u_j=n(j-\mu)p_j.
\]
With \(b=\lfloor\mu\rfloor\), telescoping from the lowest support index through \(b\) gives \(\mathbb E|J-\mu|=2(k-b)^2p_b/n\); when \(\mu\) is integral, its zero-deviation atom is harmless. This proves the finite formula. This collapse is related to established identities for hypergeometric mean absolute deviation; it is used here as the input to the new *width optimization*.

**All scaling regimes.** Complementation permits \(k\le n/2\). First, if \(k/\sqrt n\to0\), then \(b=0\) eventually and the exact expression gives
\[
0\le\frac{\Lambda_{n,k}}{\sqrt n}\le\frac{2(n-1)k}{(n-k)\sqrt n}\longrightarrow0.
\]
If \(k/\sqrt n\to c\in(0,\infty)\), the factorial moments \(\mathbb E(J)_r=(k)_r^2/(n)_r\to c^{2r}\) imply convergence of \(J\) to Poisson with mean \(t=c^2\). Hence \(p_b\to e^{-t}t^{\lfloor t\rfloor}/\lfloor t\rfloor!\). Even if \(t\) is an integer and \(b\) oscillates between adjacent integers, the limiting two masses coincide. The rational prefactor divided by \(\sqrt n\) tends to \(2c\), proving the stated \(F(t)\).

If \(k/\sqrt n\to\infty\), write \(\sigma^2=\operatorname{Var}(J)=k^2(n-k)^2/[n^2(n-1)]\). Here \(\sigma\to\infty\) and \(b-\mu\in[-1,0]\). The four factorial arguments in
\[
p_b=\frac{k!^2(n-k)!^2}{n!\,b!\,(k-b)!^2\,(n-2k+b)!}
\]
all tend to infinity, the smallest being \(b\asymp k^2/n\). Applying \(\log(m!)=(m+1/2)\log m-m+\tfrac12\log(2\pi)+O(1/m)\) and expanding about \(b=\mu\) gives the uniform local estimate \(p_b=(1+o(1))/(\sqrt{2\pi}\sigma)\). Since \(k-b=k(n-k)/n+O(1)\), substitution in the exact expression yields
\[
\frac{\Lambda_{n,k}}{\sqrt n}\longrightarrow\sqrt{\frac2\pi}.
\]
These three cases cover every subsequence of the possible rescaled widths.

**Unique maximum of the crossover.** On each interval \(m<t<m+1\), \(m\in\mathbb Z_{\ge0}\), one has \(F'(t)/F(t)=(m+1/2)/t-1\). The unique interior maximum is at \(a_m=m+1/2\), with height \(H_m=2a_m^{a_m}e^{-a_m}/m!\). At an integer the neighboring expressions agree because adjacent Poisson masses agree, but their one-sided derivatives are negative and positive, giving a strict cusp minimum. To compare the heights, let \(a=m+1/2\). Direct calculation shows
\[
\log\frac{H_{m+1}}{H_m}=(a+1)\log(a+1)-a\log a-1-\log(a+1/2)=:h(a).
\]
Moreover \(h'(a)=\int_a^{a+1}dt/t-1/(a+1/2)>0\) by strict convexity of \(t\mapsto1/t\), while \(h(a)\to0\) as \(a\to\infty\). Hence \(h(a)<0\) and the successive heights decrease strictly. The unique global maximum is \(H_0=\sqrt{2/e}\).

**Maximizing widths.** Choosing integer widths nearest \(\sqrt{n/2}\) proves the lower bound for the normalized maximum. For any maximizing sequence, complement to \(k_n\le n/2\) and pass to a subsequence on which \(k_n/\sqrt n\) converges in \([0,\infty]\) (allowing \(\infty\)). The three asymptotic cases bound the limiting coefficient by \(0\), \(F(c^2)\), or \(\sqrt{2/\pi}\). Since \(\sqrt{2/\pi}<\sqrt{2/e}\), equality is possible only at \(c=1/\sqrt2\). All subsequences obey the same restriction, proving both the sharp limit and the asserted localization.

## Verification
`verify.py` uses exact fractions to compare the collapsed formula against the direct hypergeometric absolute sum for every \(2\le n\le100\) and every width. It also forms entire projection kernel rows independently for \(2\le n\le9\), checks the telescoping identity term by term, and checks the elementary crossover stationary-point inequalities. It reports `PASS 100553 exact-rational or elementary numerical comparisons`. The executable tests corroborate the proof; no finite range is used to infer the universal or asymptotic statements. Reproduce with `python3 verify.py`.

## Relationship to prior work
Filmus (2014 preprint; 2016 publication) identifies the Johnson harmonic decomposition and gives explicit orthogonal bases; Scarabotti and Tolli (2007 preprint) provide the general homogeneous-space projection framework. Krebs and Shaheen (2008) explain Eberlein/Johnson spectral data. The hypergeometric mean-absolute-deviation boundary collapse, and hence the *finite-width formula* above once the kernel is known, is not claimed as a new general probability identity: Elezović (2026) studies that identity and fixed-proportion asymptotic expansions. The present claimed addition is the sharp optimization simultaneously over all Johnson slice widths, the sparse Poisson-to-Gaussian competition, the unique worst-width scale and its strict scalloped crossover profile. A separate degree-two Johnson endpoint norm addresses the next primitive idempotent and does not imply this cross-width first-harmonic extremum.

## Limitations
The theorem concerns only the first nonconstant Johnson component and normalized counting measure. The limiting optimizer has two complementary representatives; no finite-\(n\) uniqueness is asserted. It does not determine norms of higher Johnson components or arbitrary nonuniform slice weights. The finite-width identity is known in probability form. A recent paper on hypergeometric deviations could not be inspected in full; although its abstract specifies fixed-proportion asymptotics rather than this width optimization, equivalent hidden coverage remains a residual literature risk.

## References
1. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (first posted 2014-06-01); Electronic Journal of Combinatorics 23 (2016), #P1.23, DOI 10.37236/4567.
2. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533 (first posted 2007-01-19), Proc. London Math. Soc. 100 (2010), 348–376.
3. M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra 17 (2008), DOI 10.13001/1081-3810.1256.
4. N. Elezović, *The mean absolute deviation of the classical discrete distributions: collapse identities, complete asymptotic expansions, and enveloping series*, arXiv:2608.06232 (2026), abstract consulted; full text not inspected.
5. J. Ai and C. Pelekis, *On lower bounds for hypergeometric tails*, arXiv:2601.09485 (2026), abstract consulted.
