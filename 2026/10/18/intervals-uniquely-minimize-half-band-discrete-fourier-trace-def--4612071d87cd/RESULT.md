# Intervals uniquely minimize half-band discrete Fourier trace defect, with a sharp component penalty

## Finding
Let \(S=[-1/4,1/4]\subset\mathbb T=\mathbb R/\mathbb Z\). For every integer \(N\ge2\) and every \(N\)-element set \(\Omega\subset\mathbb Z\), define \(T_{\Omega,S}=P_\Omega B_SP_\Omega\) on \(\ell^2(\Omega)\) and \(D(\Omega)=\operatorname{tr}(T_{\Omega,S}-T_{\Omega,S}^2)\), where \(B_S\) is the Fourier projection to \(S\). Then, with \(I_N=\{0,1,\ldots,N-1\}\),

\[
D(\Omega)\ge D(I_N)=\frac N4-\frac2{\pi^2}\sum_{\substack{1\le d<N\\ d\ \mathrm{odd}}}\frac{N-d}{d^2}.
\]

Equality holds **if and only if** \(\Omega\) is an integer translate of \(I_N\). If \(c(\Omega)\) denotes the number of maximal nearest-neighbor runs in \(\Omega\), then the stronger quantitative inequality

\[
D(\Omega)-D(I_N)\ge\frac{16}{9\pi^2}\bigl(c(\Omega)-1\bigr)
\]

holds for every \(N\ge2\). Its component coefficient is best possible **uniformly in** \(N\), since equality holds for \(N=2\) and \(\Omega=\{0,3\}\). The statement is about the trace defect, not about individual concentration eigenvalues. For \(N=1\) the defect is \(1/4\) for every singleton, which is already an interval.

## Assumptions and scope
The Fourier transform is normalized by \(\widehat f(\xi)=\sum_{n\in\mathbb Z}f(n)e^{-2\pi in\xi}\) and Haar measure on \(\mathbb T\) has total mass one. The frequency band is exactly half the torus, and the spatial set may be disconnected or arbitrarily separated. The scalar \(c(\Omega)\) is the number of connected components in the integer nearest-neighbor graph; no bounded diameter or regularity hypothesis is made.

## Proof
The Fourier kernel is \(K_S(0)=1/2\) and, for nonzero integer \(k\), \(K_S(k)=\sin(\pi k/2)/(\pi k)\). In particular, \(|K_S(k)|^2=1/(\pi^2k^2)\) for odd \(k\), and zero for nonzero even \(k\). Using \(\operatorname{tr}T_{\Omega,S}=N/2\) and \(\operatorname{tr}T_{\Omega,S}^2=\sum_{x,y\in\Omega}|K_S(x-y)|^2\) yields the exact identity

\[
D(\Omega)=\frac N4-\frac2{\pi^2}E(\Omega),\qquad E(\Omega)=\sum_{\substack{x,y\in\Omega,\ x<y\\ y-x\ \mathrm{odd}}}\frac1{(y-x)^2}.
\]

**Finite-distance edge inequality.** For each integer \(r\ge0\), let \(e_r(A)\) count unordered pairs of distinct elements of a finite integer set \(A\) whose absolute difference belongs to \(\{1,3,\ldots,2r+1\}\). We prove by induction on \(N=|A|\) that

\[
e_r(A)\le e_r(I_N)=\sum_{j=0}^r\max\{N-(2j+1),0\}.
\]

The assertion is immediate for \(N=1\). For an arbitrary \(N\)-point set \(A\), write \(m=\min\{r+1,\lfloor N/2\rfloor\}\). There is always a vertex of degree at most \(m\) in the graph whose edges connect sites with differences \(1,3,\ldots,2r+1\). If \(r+1\le\lfloor N/2\rfloor\), choose the leftmost site: it has at most one right neighbor at each of the \(r+1\) permitted distances, hence degree at most \(r+1=m\). Otherwise choose a vertex in the more numerous of the two parity classes: all neighbors have opposite parity, so its degree is at most \(\lfloor N/2\rfloor=m\). Remove that vertex, apply the induction hypothesis to the \(N-1\) remaining sites, and note that the new rightmost point of \(I_N\) has precisely \(m\) neighbors in \(I_{N-1}\) at the permitted odd distances. This proves the inequality for all \(N,r\).

**Weighted summation.** Put \(w_j=(2j+1)^{-2}\) and \(\delta_j=w_j-w_{j+1}>0\), so \(\sum_{r=j}^\infty\delta_r=w_j\). A finite sum can be interchanged with the convergent nonnegative series to give

\[
E(A)=\sum_{r=0}^{\infty}\delta_r e_r(A).
\]

Every edge inequality therefore implies \(E(\Omega)\le E(I_N)\). Because \(I_N\) has \(N-d\) pairs at each distance \(1\le d<N\), the displayed exact minimum follows.

**Equality and sharp stability.** The first edge count satisfies \(e_0(\Omega)=N-c(\Omega)\), while \(e_0(I_N)=N-1\). Since every deficit \(e_r(I_N)-e_r(\Omega)\) is nonnegative and \(\delta_0=1-1/9=8/9\),

\[
E(I_N)-E(\Omega)\ge\frac89\bigl(c(\Omega)-1\bigr).
\]

Multiplication by \(2/\pi^2\) proves the claimed penalty. If \(\Omega\) is not an interval, then \(c(\Omega)\ge2\), so strictness follows. Conversely each translate of \(I_N\) gives equality by translation invariance. At \(N=2\), \(E(\{0,1\})=1\), \(E(\{0,3\})=1/9\), and \(c(\{0,3\})=2\), proving that the numerical penalty coefficient cannot be increased for a theorem uniform in \(N\).

## Verification
A standalone, standard-library-only script `verify.py` checks the exact pair kernel, the finite-distance edge inequalities, the sharp gap and equality characterization for all distinct subsets of a finite test grid of several sizes, using rational arithmetic for \(E\) and every \(e_r\). The infinite theorem is proven by induction and positive-series summation, not by finite enumeration. A direct two-site trace check separately confirms the normalization.

## Relationship to prior work
Mayeli, *Trace-defect bounds for discrete Fourier concentration operators* (arXiv:2609.12226, first publicly posted September 10, 2026), provides the general trace-defect identity (Proposition 4.1), upper bounds under fractional translation assumptions, and critical logarithmic sharpness for box models (Proposition 9.3). The identity is used here, but the **all-finite-cardinality minimizing spatial shape, unique equality classification, and sharp fragmentation penalty** are separate statements and are not established by those generic bounds. Barber and Erde's *Isoperimetry in integer lattices* (arXiv:1707.04411), and Strachan and Swanepoel's *Edge isoperimetry of lattices* (arXiv:2503.09591), provide adjacent unweighted Cayley-graph isoperimetric context; their results concern asymptotic or differently specified edge boundaries, not the simultaneous exact inequalities for all truncated odd-distance graphs coupled to the inverse-square Fourier weights. Briggs and Wells (arXiv:2402.14087) show that arbitrary one-dimensional Cayley graph isoperimetric families can exhibit phase transitions, which makes the exact interval structure for this special nested family nonautomatic.

## Limitations
The optimal shape theorem is for the half-torus spectral band and the trace defect only, with the numerical component constant sharp uniformly across cardinalities but not asserted optimal for each fixed cardinality. Other spectral arcs, higher dimensions, nonconstant finite frequency weights, higher Schatten defects and individual eigenvalue orderings are not addressed. Literature-priority searches and accessible text inspection cannot exclude an unindexed equivalent rearrangement lemma or a stronger earlier theorem.

## References
1. A. Mayeli, *Trace-defect bounds for discrete Fourier concentration operators*, arXiv:2609.12226 (initial version September 10, 2026), Proposition 4.1, Section 9.
2. B. Barber and J. Erde, *Isoperimetry in integer lattices*, arXiv:1707.04411 (2017), asymptotic Cayley-graph edge isoperimetry.
3. C. Strachan and K. Swanepoel, *Edge isoperimetry of lattices*, arXiv:2503.09591 (2025), Introduction and main results.
4. J. Briggs and C. Wells, *Phase transitions in isoperimetric problems on the integers*, arXiv:2402.14087 (2024), one-dimensional Cayley-graph context.
