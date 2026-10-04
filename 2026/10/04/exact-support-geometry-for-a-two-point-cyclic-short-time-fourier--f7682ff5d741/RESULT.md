# Exact support geometry for a two-point cyclic short-time Fourier window
## Finding
Let \(N\ge 3\), let \(a\in\mathbb Z_N\setminus\{0\}\), and use the two-point window \(g_a=\delta_0+\delta_a\). Write \(d=\gcd(a,N)\) and \(L=N/d\), so translation by \(a\) decomposes \(\mathbb Z_N\) into \(d\) cycles of length \(L\).

For every nonempty \(S\subseteq\mathbb Z_N\), define \(A_a(S)\) to be the number of \(x\) such that \(\{x,x+a\}\cap S\neq\varnothing\), and \(E_a(S)\) to be the number of \(x\) such that \(x,x+a\in S\). When \(L\) is odd, let \(Q_a(S)\) be the number of complete step-\(a\) cycles contained in \(S\); when \(L\) is even, set \(Q_a(S)=0\). Then
\[
\min_{\operatorname{supp}f=S}|\operatorname{supp}V_{g_a}f|
= N A_a(S)-d\bigl(E_a(S)-Q_a(S)\bigr).
\]

In particular, the global minimum over nonzero \(f\) equals \(N\) when \(L=2\), and equals \(2N\) when \(L\neq2\). In the first case equality is attained exactly on one full step-\(a\) two-cycle, with the ratio of the two nonzero coefficients equal to \(1\) or \(-1\). In the second case the support geometry attaining the minimum is exactly a singleton.

## Assumptions and scope
The short-time Fourier transform is taken in the convention
\[
V_gf(x,k)=N^{-1/2}\sum_{t\in\mathbb Z_N} f(t)\overline{g(t-x)}e^{-2\pi i kt/N}.
\]
Only support cardinality matters, so the normalization factor does not affect the result. The theorem concerns the canonical equal-weight two-point window \(g_a\); unequal two-point weights are not claimed here.

## Proof
For \(g_a=\delta_0+\delta_a\), factoring the common phase in the frequency variable gives
\[
V_{g_a}f(x,k)=N^{-1/2}e^{-2\pi i kx/N}\left(f(x)+f(x+a)e^{-2\pi i ka/N}\right).
\]
As \(k\) ranges over \(\mathbb Z_N\), the factor \(e^{-2\pi i ka/N}\) ranges over all \(L\)-th roots of unity, each exactly \(d\) times.

Fix \(x\). If neither \(x\) nor \(x+a\) lies in \(S\), the entire frequency slice vanishes. If exactly one lies in \(S\), all \(N\) entries of the slice are nonzero. If both lie in \(S\), the two-term expression has either no zero or exactly \(d\) zeros; it has \(d\) zeros exactly when
\[
-f(x)/f(x+a)
\]
is an \(L\)-th root of unity. Call the directed edge \(x\to x+a\) good in this latter case. Thus, for fixed support \(S\), minimizing the total STFT support is equivalent to maximizing the number of good internal directed edges.

On every proper occupied path component of a step-\(a\) cycle, all internal edges can be made good simultaneously: choose a nonzero initial coefficient and alternate signs along the path. On a completely occupied even cycle the same alternating assignment makes every edge good. On a completely occupied odd cycle, however, all \(L\) edges cannot be good. Indeed, if all were good, multiplying their ratios would give \((-1)^L=-1\) as a product of \(L\)-th roots of unity, impossible for odd \(L\). Conversely, alternating signs around the first \(L-1\) edges makes exactly those \(L-1\) edges good, so the loss of one good edge is sharp. Therefore the maximum possible number of good internal edges is exactly \(E_a(S)-Q_a(S)\), proving the formula.

For the global minimum, a nonempty proper occupied component with \(k\) vertices contributes
\[
(N-d)k+(N+d)
\]
when it is a single component, hence at least \(2N\), with equality only for \(k=1\). A full step-\(a\) cycle contributes \(N(L-1)\) for even \(L\), and \(N(L-1)+d\) for odd \(L\). This is below \(2N\) only when \(L=2\), where it equals \(N\). The stated equality cases follow.

## Verification
The accompanying script `verify_two_point_stft.py` implements the orbit statistics and the explicit sign construction using integer arithmetic only. It exhaustively checks every nonempty support for every \(3\le N\le12\) and every nonzero \(a\), totaling \(81{,}855\) support cases. It also checks the global-minimum corollary from the proved component formulas for all \(3\le N\le5000\) and all nonzero \(a\), totaling \(12{,}497{,}499\) parameter pairs. The replay output is `VERIFY_OK`.

## Relationship to prior work
Krahmer, Pfander, and Rashkov prove the universal finite-group bound \(|\operatorname{supp}V_gf|\ge |G|\), derive stronger support-size bounds, and in prime cyclic groups give a sharp estimate in terms of the support sizes of \(f\) and \(g\). Their prime result implies the \(2N\) lower bound for a two-point window when \(N\) is prime, but it does not give the prescribed-support formula above or the composite-order cycle obstruction. Fernández, Galbis, and Martínez characterize the minimum-support extremals under a different support-size hypothesis and study localization operators. Nicola later completely classifies equality in the universal \(N\)-point bound; this subsumes the \(L=2\) equality branch, but does not determine the fixed-window minima above the universal bound or the exact value for every prescribed support \(S\).

## Limitations
The result is specific to the equal-weight window \(\delta_0+\delta_a\). It determines support cardinalities but not amplitudes, phases, norms, or stability under perturbation. The literature comparison cannot exclude an unindexed result stated in substantially different terminology.

## References
1. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first posted 2006-11-16; published in *Applied and Computational Harmonic Analysis* 25 (2008), 209–225.
2. C. Fernández, A. Galbis, and J. Martínez, *Localization Operators and an Uncertainty Principle for the Discrete Short Time Fourier Transform*, *Abstract and Applied Analysis* 2014, Article 131459, doi:10.1155/2014/131459.
3. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176; *Journal of Functional Analysis* 284 (2023), 109924.
