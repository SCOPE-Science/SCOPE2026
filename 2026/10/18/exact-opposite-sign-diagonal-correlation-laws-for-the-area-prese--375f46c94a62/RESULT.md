# Exact opposite-sign diagonal correlation laws for the area-preserving baker map

## Finding
Let \(B:[0,1)^2\to[0,1)^2\) be the classical unfolded dyadic baker transformation with Lebesgue invariant probability measure and define its two diagonal half-square sensors \(f_+(x,y)=\mathbf 1_{\{x+y<1\}}\) and \(f_-(x,y)=\mathbf 1_{\{x>y\}}\). For each integer \(n\ge1\), write \(C_\pm(n)=\operatorname{Cov}_\mu(f_\pm,f_\pm\circ B^n)\). Then the exact all-lag laws are
\[
 C_\pm(n)=\frac{1}{6\,2^n}\ \pm\ \frac{n\,2^n}{8(4^n-1)}.
\]
In this notation the plus sign corresponds to the sensor \(x+y<1\), and the minus sign to \(x>y\). Their signs are sharply different: \(C_+(n)>0\) for every \(n\ge1\), whereas \(C_-(1)=0\) and \(C_-(n)<0\) for every \(n\ge2\). The time-one indicators for the latter sensor are independent (since both are Bernoulli with probability \(1/2\)), but subsequent observations are not pairwise independent.

Their exact sum and leading asymptotics are
\[
 C_+(n)+C_-(n)=\frac{1}{3\,2^n},\qquad
 C_\pm(n)=2^{-n}\left(\frac16\pm\frac n8\right)+O(n2^{-3n}).
\]
Consequently each absolute correlation has sharp order \(n2^{-n}\) as \(n\to\infty\), with opposite leading signs.

## Assumptions and scope
Set \(Q=[0,1)^2\) and let \(\mu\) be normalized planar Lebesgue measure on \(Q\). Define
\[
 B(x,y)=\left(2x-\lfloor 2x\rfloor,\frac{y+\lfloor2x\rfloor}{2}\right).
\]
This map preserves \(\mu\): on each of its two half-width vertical strips it is affine with unit absolute Jacobian and its images partition \(Q\) into two disjoint half-height horizontal strips, modulo null boundaries. The two indicator sensors are measurable and each has probability \(1/2\) by triangular area. Boundary conventions, and points with nonunique binary expansions, do not affect the measure-theoretic assertions. This is a two-time covariance theorem under \(\mu\), not a theorem about periodic-orbit action correlations, coarse-graining entropy, or general polygonal sensors.

## Proof
Fix \(n\ge1\) and set \(N=2^n\). Let \(r_n(k)\) be reversal of the \(n\)-digit binary expansion of \(k\in\{0,\dots,N-1\}\). The dynamics, on the vertical strip \(x=(k+u)/N\), with \(0\le u<1\) and \(0\le v=y<1\), satisfies
\[
 B^n\bigl((k+u)/N,v\bigr)=\bigl(u,(r_n(k)+v)/N\bigr).
\]
Indeed each iterate removes the leading binary digit of \(x\) and prepends it to the expansion of \(y\); after \(n\) iterates the prepended block is the digit reversal of \(k\). Every strip has \(\mu\)-mass \(1/N\), with \((u,v)\) independent uniform coordinates conditional on the strip.

Set \(s=k/N\), \(t=r_n(k)/N\). For the plus sensor, put \(a=1-s\), \(b=1-t\). The two simultaneous inequalities reduce to
\[
 0\le v<\min\{a-u/N,\;N(b-u)\}.
\]
The two upper lines intersect at
\[
 u_*=(N^2b-Na)/(N^2-1),\qquad 0\le u_*\le b\le1.
\]
Here \(N b=N-r_n(k)\ge1\ge a\) implies the lower bound, and \(Na=N-k\ge b\) implies the upper bound. Integrating the first line up to \(u_*\) and the second from \(u_*\) to \(b\) yields the conditional joint area
\[
 A_+(s,t)=ab-\frac{b^2}{2N}-\frac{(Na-b)^2}{2N(N^2-1)}.
\]
(Equivalently, integrate the original first line over \([0,b]\) and subtract the triangular wedge cut away by the steeper line.)

For the minus sensor the simultaneous inequalities are
\[
 0\le v<\min\{s+u/N,\;N(u-t)\}.
\]
The second upper bound is nonpositive until \(u=t\), and the two upper lines intersect at
\[
 u_*=(N^2t+Ns)/(N^2-1),\qquad t\le u_*\le1.
\]
The upper bound follows from \(r_n(k)\le N-1\) and \(s\le (N-1)/N\). Integrating the second line on \([t,u_*]\) and the first on \([u_*,1]\) yields
\[
 A_-(s,t)=s(1-t)+\frac{1-t^2}{2N}-\frac{(Ns+t)^2}{2N(N^2-1)}.
\]
These integrations already account for truncation by the unit square because the first upper line always takes values in \([0,1]\) on the interval where the minimum is positive.

It remains to average over the \(N\) strips. Uniformity of the bit-reversal permutation gives
\[
 \mathbb E[s]=\mathbb E[t]=\frac{N-1}{2N},\qquad
 \mathbb E[s^2]=\mathbb E[t^2]=\frac{(N-1)(2N-1)}{6N^2}.
\]
The sole mixed moment is
\[
 \mathbb E[st]=\frac{(N-1)^2}{4N^2}+\frac{n}{8N}.
\]
To prove it, write the binary digits of the uniform random strip label as independent Bernoulli variables \(d_0,\ldots,d_{n-1}\), so \(k=\sum_{j=0}^{n-1}d_j2^j\) and \(r_n(k)=\sum_{j=0}^{n-1}d_j2^{n-1-j}\). Since \(\operatorname{Var}(d_j)=1/4\),
\[
 \operatorname{Cov}(k,r_n(k))
 =\sum_{j=0}^{n-1}\frac{2^j2^{n-1-j}}4
 =\frac{nN}{8}.
\]
Divide by \(N^2\) and add the product of the means.

Substitution into the two conditional area formulas and simplification gives the exact joint probabilities
\[
 \mathbb E[f_\pm(f_\pm\circ B^n)]
 =\frac14+\frac{1}{6N}\pm\frac{nN}{8(N^2-1)}.
\]
Both sensors have mean \(1/2\); subtracting \(1/4\) proves the covariance identities. For \(n\ge2\), negativity of \(C_-(n)\) is equivalent to \(3nN^2>4(N^2-1)\), which follows from \(3n\ge6>4\). For \(n=1\), substitution gives \(C_-(1)=0\). The other sign is manifestly positive. Finally, expansion of \((1-N^{-2})^{-1}\) gives the claimed all-lag asymptotics and sharp orders.

## Verification
The accompanying standalone standard-library Python file `verify_baker.py` enumerates every binary strip for \(1\le n\le12\) and computes the joint-event polygon areas by exact rational integration. It independently constructs the affine inequalities and partitions the integration interval at all line crossings and zeros. For both sensors and all twelve positive lags, the checker exactly reproduces the closed formula and reports `VERIFY_OK`. This finite check verifies implementation and boundary handling only; the proof above establishes the formulas for all positive integer lags. All calculations use exact rational arithmetic, not floating-point fitting.

## Relationship to prior work
The baker transformation and its Lebesgue-invariant dynamics are classical. Tanner's study [1] concerns semiclassical **periodic-orbit action** correlations, which are not the time-separated Lebesgue covariances of diagonal indicator functions here. Tasaki [2] develops general spectral/operator descriptions and relaxation for the same baker map; these can provide an abstract framework for correlation decay but do not supply the evaluated two-triangle all-lag law identified here in the inspected text. The present calculation obtains the explicit coefficient \(n/8\) from binary bit reversal, and the two orientation-dependent signs from planar half-space intersection geometry. It does not claim originality of the baker map, its invariant measure, or general mixing/correlation-decay theory.

## Limitations
The result concerns exactly two diagonal half-square threshold observables and the invariant planar Lebesgue state. The one-lag independence statement does not imply independence at higher lags or a Bernoulli factor. The infinite-lag formula is analytical; the finite checker is not an exhaustive proof. Although the checked prior sources did not identify this explicit pair of formulas, broader spectral descriptions and other uncatalogued literature may contain equivalent evaluations; independent literature assessment has not been performed.

## References
[1] G. Tanner, *Periodic orbit action correlations in the Baker map*, public preprint arXiv:nlin/0001024 (13 January 2000), https://arxiv.org/abs/nlin/0001024.

[2] S. Tasaki, *On Prigogine's approaches to irreversibility: a case study by the baker map*, Discrete Dynamics in Nature and Society (2004), DOI:10.1155/S1026022604312069, https://doi.org/10.1155/S1026022604312069.
