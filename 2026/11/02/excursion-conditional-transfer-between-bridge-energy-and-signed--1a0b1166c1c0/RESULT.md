# Excursion-conditional transfer between bridge energy and signed occupation

## Finding
For every integer \(n\ge1\), let \((S_j)_{j=0}^{2n}\) be a uniform nearest-neighbor bridge with \(S_0=S_{2n}=0\) and increments in \(\{-1,1\}\). Let \(\mathcal M=(M_1,\ldots,M_K)\) be the ordered positive *semilengths* of its successive zero-to-zero excursions, so \(\sum_i M_i=n\). Define its squared-height energy and signed half-time occupation imbalance by
\[
Q=\sum_{j=1}^{2n-1}S_j^2,\qquad
X=\sum_{i=1}^n \operatorname{sgn}(S_{2i-1}).
\]
Every odd-time height is nonzero. The main identity is **conditional on the complete excursion-length vector**:
\[
\boxed{\mathbb E[Q-2X^2\mid\mathcal M]=-n.}\tag{1}
\]
Consequently every real function \(h(\mathcal M)\), for which the moments exist, satisfies
\[
\boxed{\operatorname{Cov}(h(\mathcal M),Q)
=2\operatorname{Cov}(h(\mathcal M),X^2).}\tag{2}
\]
A quantitative application to the natural return count \(K\), including the final return, is
\[
\boxed{\operatorname{Cov}(K,X^2)=-\frac{n(n-1)}{12}\frac{4^n}{\binom{2n}{n}}.}\tag{3}
\]
It is strictly negative for \(n\ge2\), and asymptotic to \(-\sqrt\pi\,n^{5/2}/12\). The first-moment transfer (1), rather than the already accessible return-count/energy covariance alone, is the central contribution.

## Assumptions and scope
A bridge is selected uniformly from the \(\binom{2n}{n}\) balanced sequences of \(n\) upsteps and \(n\) downsteps. The excursion vector \(\mathcal M\) records exact successive zero-free interval lengths divided by two; conditional on \(\mathcal M\), signs and shapes of different excursions are independent, signs are fair, and a positive excursion with semilength \(m\) is uniform over \(C_{m-1}\) primitive positive paths. Here \(C_j=\binom{2j}{j}/(j+1)\). The sigma-field in (1) contains excursion lengths but not excursion signs or internal shapes. The convention for \(Q\) includes interior vertices only (zero endpoint contributions are immaterial), while \(X\) samples heights at odd times, not all discrete time points. Under these normalizations, an excursion of semilength \(m\) contributes \(\pm m\) to \(X\). Conditional on \(S_{2n}=0\), any fixed homogeneous upstep probability in \((0,1)\) gives the same uniform bridge law; no inhomogeneous or non-nearest-neighbor claim is made.

## Proof
Put \(D=z\,d/dz\), \(s(z)=\sqrt{1-4z}\), and
\[
F(z)=\sum_{m\ge1}C_{m-1}z^m=\frac{1-s(z)}2,
\qquad B(z)=\frac1{1-2F(z)}=\frac1{s(z)}.
\]
A signed primitive excursion of semilength \(m\) has \(2C_{m-1}\) possible paths, and a bridge is a unique ordered sequence of such excursions. A bridge chosen uniformly from all balanced step words satisfies
\[
\mathbb E[S_j^2]=\frac{j(2n-j)}{2n-1},\quad
\mathbb E[Q]=\frac{n(2n+1)}3
\quad (n\ge1).
\]
Indeed its increments are a uniformly shuffled multiset of \(n\) signs of each kind, with distinct-increment covariance \(-1/(2n-1)\), and summing over \(1\le j<2n\) yields the displayed energy mean.

Let \(E(z)\) enumerate all *signed primitive* excursions weighted by their energy \(Q\), with one factor \(z\) per semilength. Since energy is additive under concatenation, marking one excursion in a bridge gives
\[
\frac{E(z)}{(1-2F(z))^2}
=\sum_{n\ge1}\binom{2n}{n}\frac{n(2n+1)}3z^n
=\frac{2D^2B(z)+DB(z)}3.
\]
Using \(B=s^{-1}\) and \(F=(1-s)/2\), coefficientwise formal-power-series algebra gives
\[
E(z)=2(2D^2-D)F(z)
=\sum_{m\ge1}2C_{m-1}m(2m-1)z^m.
\]
Thus a uniformly sampled signed primitive excursion of semilength \(m\) has expected energy exactly \(m(2m-1)\). Given \(\mathcal M=(m_1,\ldots,m_k)\), additivity gives
\[
\mathbb E[Q\mid\mathcal M]
=\sum_{i=1}^k m_i(2m_i-1)
=2\sum_{i=1}^k m_i^2-n.
\]
Independently, conditional on \(\mathcal M\), the signs \(\varepsilon_i\) of its excursions are independent fair signs and \(X=\sum_i\varepsilon_i m_i\). Therefore
\[
\mathbb E[X^2\mid\mathcal M]=\sum_i m_i^2,
\]
which proves (1). The tower property applied to \(h(\mathcal M)\) proves (2), with no assumption that \(h\) depends only on the number of excursions.

For completeness, (3) is proved independently using a marked generating function. Let
\[
G(z,u,v)=\left(1-vF(ze^u)-vF(ze^{-u})\right)^{-1}.
\]
The coefficient \([z^n]\,G\) is the exponential generating moment sum for \(X\) over balanced paths, with \(v\) marking \(K\), not a normalized probability. Differentiating as *formal power series* at \(u=0,v=1\) gives
\[
\left.\partial_u^2G\right|_{0,1}=\frac{2D^2F}{s^2},\qquad
\left.\partial_v\partial_u^2G\right|_{0,1}
=\frac{2D^2F}{s^2}+\frac{8F D^2F}{s^3}.
\]
Here \(D^2F=z/s+2z^2/s^3\). Elementary binomial coefficient extraction yields, with \(b_n=4^n/\binom{2n}{n}\),
\[
\mathbb E[X^2]=\frac{n(n+2)}3,\quad
\mathbb E[K]=b_n-1,\quad
\mathbb E[KX^2]=\frac{n(n+3)}4b_n-\frac{n(n+2)}3.
\]
Subtracting the product of the first two means yields (3). Finally Stirling's formula gives \(b_n\sim\sqrt{\pi n}\).

## Verification
The standalone `verify.py` uses exact integer and rational arithmetic. It enumerates every balanced path for \(1\le n\le9\), groups the paths by every possible ordered excursion-length vector, and independently verifies both conditional expectations in (1). It also tests (3), the uniform bridge energy and imbalance means, and the total return-count mean at each size. Separate exact coefficient checks extend through \(n=100\). Running `python3 verify.py` completed with 1,267 exact assertions. These are finite checks of the algebra, not substitutes for the all-\(n\) formal-power-series argument.

## Relationship to prior work
The Catalan first-return decomposition and the Chung–Feller occupation-time law are classical. Lindell and Holst (2007) study joint distributions of ranked excursion lengths in tied-down random walks; their accessible full paper supplies the renewal background but not a conditional transfer between squared-height energy and signed occupation imbalance. Pitman and Tang (arXiv:1307.7952, first posted July 30, 2013), later merged with Lupu into arXiv:1310.3889 (October 15, 2013), analyze Vervaat transforms and bridge/excursion decompositions in both discrete and continuous settings, but do not state this finite conditional second-moment identity. Earlier research on Bernoulli-walk local times by de Vos and Vervaat (1987/1988) is relevant but its complete preprint was not accessible for a decisive comparison. An earlier exact return-count/height-energy covariance for this same model can be recovered as the factor-two corollary of (2) and (3); that older covariance is **not** claimed as a separate new result. The distinct new assertion is (1), which transfers covariance with *every* excursion-length observable.

## Limitations
This is a conditional **expectation** identity, not a pathwise equality, a distributional identity, or a statement about conditioned excursion signs. A finite exhaustive computation does not certify the infinite statement independently; the proof is analytic. Historical priority is qualified by the possibility of equivalent results in older texts on Catalan excursion functionals and tied-down renewal processes. No independent validation or external audit has occurred.

## References
1. A. Lindell and L. Holst, *Distributions of the Longest Excursions in a Tied Down Simple Random Walk and in a Brownian Bridge*, Journal of Applied Probability 44 (2007), 1056–1067, https://doi.org/10.1239/jap/1197908824 (full text inspected).
2. J. Pitman and W. Tang, *On Vervaat transform of Brownian bridges and Brownian motion*, arXiv:1307.7952 (first posted 2013-07-30), https://arxiv.org/abs/1307.7952 (early public precursor; source metadata and abstract inspected).
3. T. Lupu, J. Pitman, and W. Tang, *The Vervaat transform of Brownian bridges and Brownian motion*, arXiv:1310.3889 (first posted 2013-10-15), https://arxiv.org/abs/1310.3889 (accessible full text inspected; primary MSC 60C05).
4. J. C. de Vos and W. Vervaat, *Local Times of Bernoulli Walk*, Statistica Neerlandica 42 (1988), 1–16; 1987 research memorandum, https://doi.org/10.1111/j.1467-9574.1988.tb01516.x (metadata/abstract inspected, complete text unavailable).
5. P. J. Fitzsimmons and R. K. Getoor, *Occupation time distributions for Lévy bridges and excursions*, Stochastic Processes and their Applications 58 (1995), 73–89, https://doi.org/10.1016/0304-4149(95)00008-V (abstract inspected; continuous Lévy bridges rather than finite discrete energy).
