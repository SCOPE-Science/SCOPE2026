# Sharp strong two-window STFT thresholds in prime-period Floquet sectors

## Finding

For every odd prime \(p\ge3\), integer \(q\ge2\), and \(N=pq\), consider the exponential band window \(g_m\) on \(\mathbb Z_N\) given by \(g_m(j)=2^j\) for \(0\le j\le m\) and zero elsewhere, where \(1\le m\le p-1\). Write \(\widehat g_m\) for the length-\(N\) discrete Fourier transform. For each \(r\in\{0,\ldots,q-1\}\), introduce the translation-eigenvalue subspace

\[
E_r=\{f\in\mathbb C^{\mathbb Z_N}: f(j+p)=e^{2\pi i r/q}f(j)\text{ for all }j\}.
\]

A signal is *phase retrievable with a window* when equality of its complete short-time Fourier transform (STFT) magnitudes with those of an arbitrary length-\(N\) complex signal forces equality up to one global unit scalar. The comparison signals are not assumed to lie in \(E_r\). Define

\[
M(p,q)=\max\{m\in\{1,\ldots,p-1\}:m+2\lfloor m/q\rfloor\le p-1\}.
\]

**Theorem.** For each fixed \(r\), *every* nonzero \(f\in E_r\) is phase retrievable with **at least one** of the two windows \(g_m\) and \(\widehat g_m\) exactly when \(m>M(p,q)\). For every \(1\le m\le M(p,q)\), at least one nonzero signal in *each* \(E_r\) fails phase retrievability for both windows separately.

For an explicit closed form, write \(p-1=(q+2)a+b\) with \(0\le b<q+2\). Then

\[
\boxed{M(p,q)=qa+\min\{b,q-1\}.}
\]

For example, when \(q=2\), the transition is \(M(p,2)=(p-1)/2\). In particular, on the order-\(2p\) cycle, the prime-period eigenvalue sectors are covered for every \(m\ge(p+1)/2\), while the general composite-dimension sufficient condition from the motivating paper requires \(m>(2p-1)/3\).

## Assumptions and scope

Use the unnormalized Fourier convention

\[
\widehat f(k)=\sum_{j=0}^{N-1}f(j)e^{-2\pi i jk/N},\qquad
V_g f(a,b)=\sum_{j=0}^{N-1}f(j)\overline{g(j-a)}e^{-2\pi i jb/N}.
\]

All indices are cyclic. The complete magnitude array \(\{|V_g f(a,b)|:0\le a,b<N\}\) is available. The window \(g_m\) is known, and the choice of which of the two full arrays achieves injectivity may depend on \(f\). The assertion concerns *strong* two-window phase retrieval, not the weaker problem of combining the two arrays or comparing signals only inside the symmetry sector. The fixed prime and repetition multiplier are arbitrary within the stated ranges.

## Proof

**1. The band-window support graph.** Because \(N\ge2m+2\), the ambiguity function \(V_{g_m}g_m(a,b)\) vanishes exactly when the cyclic representative of \(a\) lies outside \([-m,m]\). For each \(|a|\le m\), its nonzero overlap is a finite geometric progression whose consecutive-term modulus ratio is \(4\), so its sum cannot vanish at any modulation \(b\): a complex geometric series with ratio of modulus different from \(1\) has nonzero sum. Fourier inversion of the intensity identities therefore recovers precisely the diagonal products \(f(j)\overline{f(j-a)}\) with cyclic displacement \(|a|\le m\), as well as the coordinate moduli. Nonzero entries joined by a displacement of length at most \(m\) have recoverable relative phases; a disconnected support graph permits independent component phase rotations without changing any measured products. Thus a nonzero signal fails phase retrieval with \(g_m\) **if and only if** its cyclic support has at least two distinct zero gaps, each consisting of at least \(m\) consecutive zero coordinates. This is also the connected-support characterization in Bartusel, Theorem 2.4.

The Fourier covariance of the STFT gives an equivalent criterion for \(\widehat g_m\): \(f\) is retrievable with \(\widehat g_m\) if and only if \(\widehat f\) is retrievable with \(g_m\). This is Bartusel's Lemma 2.5 applied to individual signals.

**2. Reduce a translation sector to a prime cyclic group.** Multiplication by the character \(e^{2\pi i rj/N}\) preserves the cyclic zero-gap patterns of a signal and merely translates those of its Fourier transform. It therefore suffices to prove the assertion for \(r=0\). Every \(f\in E_0\) has the form \(f(j)=u(j\bmod p)\) for a nonzero \(u\in\mathbb C^{\mathbb Z_p}\). A direct geometric sum gives

\[
\widehat f(k)=0\quad(k\not\equiv0\pmod q),\qquad
\widehat f(q\ell)=q\widehat u(\ell).
\]

Let \(S=\operatorname{supp}u\), \(T=\operatorname{supp}\widehat u\), and \(h=\lfloor m/q\rfloor\). If the repeated \(f\) is not retrievable with \(g_m\), one of its repeated periodic zero gaps has length at least \(m\); hence \(|S|\le p-m\). If \(\widehat f\) is not retrievable with \(g_m\), it has at least two distinct frequency zero gaps of length at least \(m\). A frequency gap containing exactly \(v\) unoccupied sites of the \(q\)-spaced frequency sublattice contains exactly \(q(v+1)-1\) zero coordinates of the full cycle. Consequently \(v\ge\lfloor m/q\rfloor=h\) for each of two disjoint gaps, so \(|T|\le p-2h\) (a valid, if weak, bound when \(h=0\)). Tao's sharp prime-order uncertainty inequality yields

\[
p+1\le |S|+|T|\le2p-m-2h,
\]

or equivalently \(m+2\lfloor m/q\rfloor\le p-1\). Therefore, whenever \(m>M(p,q)\), the two recovery failures cannot occur simultaneously.

**3. Sharp witnesses at every smaller band.** Assume \(1\le m\le M(p,q)\), let \(h=\lfloor m/q\rfloor\), set \(\omega=e^{2\pi i/p}\), and define the two separated frequency blocks

\[
R=\{1,\ldots,h\}\cup\{h+2,\ldots,2h+1\},\qquad
P(z)=\prod_{\ell\in R}(z-\omega^{-\ell}).
\]

The empty product is \(1\). Write \(P(z)=\sum_{j=0}^{2h}u_jz^j\), extend \(u\) by zero on the remaining indices of \(\mathbb Z_p\), and set \(f(j)=u_{j\bmod p}\). Because \(m+2h\le p-1\), every period has at least \(p-2h-1\ge m\) consecutive zeros following the coefficient interval, and there are \(q\ge2\) such gaps. Hence \(f\) fails recovery under \(g_m\), even if some of the interior polynomial coefficients also vanish.

On the other hand,

\[
\widehat u(\ell)=P(\omega^{-\ell}),
\]

so \(\widehat u\) vanishes **exactly** at the \(2h\) distinct indices of \(R\), as the polynomial has degree \(2h<p\). The full Fourier support occupies the indices \(q\ell\) with \(\ell\notin R\). The two blocks of missing lattice sites produce two distinct full-cycle zero gaps, each of length \(q(h+1)-1\ge m\), separated by nonzero frequency entries. When \(h=0\), all \(p\) sublattice sites are nonzero and each pair of consecutive ones is separated by \(q-1\ge m\) zeros. In either case \(\widehat f\) also fails recovery under \(g_m\); by Fourier covariance, \(f\) fails recovery under \(\widehat g_m\). Modulating \(f\) by \(e^{2\pi irj/N}\) places an equally valid witness in every \(E_r\).

**4. Closed threshold.** The function \(m\mapsto m+2\lfloor m/q\rfloor\) increases strictly. Writing \(p-1=(q+2)a+b\), \(0\le b<q+2\), the largest feasible \(m\) is \(qa+\min(b,q-1)\), which proves the closed form.

## Verification

The standalone, standard-library Python script `verify_periodic.py` checks the closed-form threshold, explicit complex-root polynomial constructions, the full length-\(pq\) discrete Fourier transforms, the two requisite cyclic support disconnections, and finite support-pattern implications of the prime uncertainty inequality. The observed execution yielded `VERIFY_OK constructed_witnesses=135 polynomial_roots=202 prime_support_bounds_p=3,5,7`. The finite computations are diagnostic only: the argument above establishes all primes, multipliers, sector characters, and valid band widths.

## Relationship to prior work

Bartusel (2026) introduced this *strong* two-window criterion, proved the connected-support characterization, exhibited the exponential band windows, and obtained a general composite-order sufficient threshold together with a sharp prime-order result. Those ingredients and the established Tao prime uncertainty theorem are used here. What differs is a sharp, necessary-and-sufficient classification **in every prime-period translation eigensector of a composite cycle**, with its arithmetic dependence on the repetition multiplier and explicit witnesses at every failed bandwidth. Bartusel's results do not state this period-resolved threshold, and the general composite sufficient theorem does not yield it. Chen, Lu, Sun and Zhao (2026) concern sampled STFT measurements of continuous periodic or quasi-periodic signals with other windows; their setting does not give the present finite-cycle, globally compared, strong two-window threshold.

## Limitations

The theorem is restricted to the specified translation-eigenvalue sectors, to an odd prime fundamental period, and to the exact exponential band windows (or any window with the same full ambiguity-support band). It does not classify all composite-length signals, establish numerical stability under perturbation/noise, or demonstrate independent mathematical validation. The sharp threshold is a property of signal families and **does not imply** that a fixed individual window recovers every signal. Historical priority outside the inspected closest published sources remains a possible risk.

## References

1. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first posted May 29, 2026. In particular Theorem 2.4, Lemma 2.5, Theorem 2.6, Corollary 2.8, and Example 2.9.
2. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first posted August 29, 2003; Theorem 1.1.
3. T. Chen, H. Lu, W. Sun, Y. Zhao, *STFT Phase Retrieval with Two Window Functions*, arXiv:2602.05210, February 5, 2026 (distinct continuous and sampled measurement setting).
