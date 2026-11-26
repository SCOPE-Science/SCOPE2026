# Smoothly glued Chebyshev maps with fair observations and arbitrarily biased maximal entropy

## Finding
Let \(m,n\ge 2\) be integers with \(m\equiv n\equiv2\pmod4\). Define \(F_{m,n}:[-1,1]\to[-1,1]\) by \(F_{m,n}(x)=T_m(x)\) for \(0\le x\le1\) and \(F_{m,n}(x)=T_n(x)\) for \(-1\le x<0\), where \(T_d(\cos\theta)=\cos(d\theta)\). This is a continuous \(C^1\) interval map. It has a unique absolutely continuous invariant probability \(\mu(dx)=dx/(\pi\sqrt{1-x^2})\). Relative to \(\mu\), the sign observations \(S_j=+\) for \(F_{m,n}^{j}(x)>0\) and \(S_j=-\) otherwise are independent and fair at all nonnegative times.

The topological entropy, metric entropy of \(\mu\), and their difference are exactly
\[
h_{\mathrm{top}}(F_{m,n})=\log\frac{m+n}{2},\qquad
h_\mu(F_{m,n})=\frac{\log m+\log n}{2},\qquad
h_{\mathrm{top}}-h_\mu=\log\frac{m+n}{2\sqrt{mn}}.
\]
There is a unique invariant maximal-entropy measure \(\nu\). Under \(\nu\), the same signs are independent with probabilities \(\nu(S_j=+)=m/(m+n)\) and \(\nu(S_j=-)=n/(m+n)\). When \(m\ne n\), \(\mu\) and \(\nu\) are mutually singular, and their entropy gap is strictly positive. Along \(m=2\), \(n=4k+2\) as \(k\to\infty\), this gap diverges. Thus a common arcsine invariant density and fair independent observations coexist with an arbitrarily large gap between the metric and topological entropies. The density is smooth on \((-1,1)\) and has integrable singularities at the two endpoints.

## Assumptions and scope
Only positive integers \(m,n\) congruent to \(2\) modulo \(4\) are considered. The map is iterated in discrete nonnegative time. The convention for the sign at zero is immaterial under the two measures in the finding, since the set of points with a zero iterate has measure zero for both. Entropies use natural logarithms. Absolutely continuous refers to ordinary Lebesgue measure on \([-1,1]\), and uniqueness of a maximal-entropy measure is among all invariant Borel probabilities. The case \(m=n\) is included.

## Proof
**1. Smooth gluing and conjugacy.** For even \(d\equiv2\pmod4\), \(T_d(0)=-1\) and \(T'_d(0)=0\). The two polynomial restrictions therefore join with equal value and derivative; elsewhere they are smooth. Set \(H(t)=\cos(\pi t)\) for \(0\le t\le1\). Then \(H\) is a homeomorphism to \([-1,1]\) reversing orientation and \(G=H^{-1}\circ F_{m,n}\circ H\) equals
\[
G(t)=\frac1\pi\arccos(\cos(d\pi t)),\quad
 d=\begin{cases}m,&0\le t\le\tfrac12,\\ n,&\tfrac12<t\le1.\end{cases}
\]
This is a continuous triangular-wave map with piecewise constant derivative of magnitude \(m\) or \(n\). Its turning points on the left occur at the grid \(t=j/m\); those on the right occur at \(t=j/n\). Since \(m/2\) and \(n/2\) are odd integers, both grids meet the interface \(1/2\), which is a turning point with common image \(1\). Every consecutive grid interval inside its corresponding half is a monotone branch of \(G\) **onto the entire interval** \([0,1]\). There are \(m/2\) branches on the left and \(n/2\) on the right, hence \(N=(m+n)/2\) full branches total. Their inverse contractions have respective ratios \(1/m\) and \(1/n\), bounded above by \(1/2\).

**2. Symbolic dynamics and both invariant measures.** Label the \(N\) monotonic full branches separately. A length-\(r\) branch word determines a compact cylinder with diameter at most \(2^{-r}\). The cylinders have disjoint interiors and each is mapped by \(G^r\) monotonically onto \([0,1]\). By continuity, adjacent cylinders have opposite orientations, so they give exactly \(N^r\) laps, and the lap-growth formula gives \(h_{\mathrm{top}}(G)=\log N\). Inverse-branch compositions give a continuous factor coding from the one-sided full \(N\)-shift onto \(G\). Let \(E\) be the union of all iterated preimages, including time zero, of the branch boundaries. These boundaries map to \(\{0,1\}\), which lies in the boundary set, so \(G^{-1}(E)=E\). The set \(E\) is countable, and the coding is one-to-one off \(E\).

The uniform \(N\)-symbol Bernoulli measure projects to a nonatomic invariant probability: a point lies in at most two cylinders at each depth \(r\), giving projected point mass at most \(2N^{-r}\) for every \(r\). The projection thus avoids \(E\) and preserves its entropy \(\log N\). To see uniqueness, an invariant probability assigning positive mass \(a\) to \(E\) decomposes into its invariant restrictions to \(E\) and to its complement, omitting the second component if \(a=1\). The normalized restriction to the countable set is atomic and has zero entropy. By affinity of metric entropy and the topological entropy bound on the complementary restriction, the total entropy is at most \((1-a)\log N<\log N\). Every maximizing measure therefore avoids \(E\), lifts by its unique branch itinerary with the same entropy, and must be the projection of the full shift's unique maximizing measure, the uniform Bernoulli measure.

Lebesgue measure \(\lambda\) on \([0,1]\) is invariant under \(G\): the full inverse branches contribute a constant Perron transfer of
\[
\frac{m/2}{m}+\frac{n/2}{n}=1.
\]
For every length-\(r\) branch word \((b_0,\ldots,b_{r-1})\), its Lebesgue cylinder measure is exactly \(\prod_{j=0}^{r-1}1/d(b_j)\), where \(d(b)=m\) on a left branch and \(d(b)=n\) on a right branch. The branch itinerary under \(\lambda\) is consequently an independent sequence with branch probabilities \(1/m\) (left) and \(1/n\) (right); these sum to one. The inverse-branch diameters tend to zero, so the branch partition generates the Borel sigma algebra modulo null sets. Its iid tail is trivial; therefore \(G\) is exact relative to \(\lambda\). Exactness implies uniqueness of an absolutely continuous invariant probability (the Perron operator converges in \(L^1\) to constants). Pushing \(\lambda\) through \(H\) gives the stated arcsine density. Any absolutely continuous invariant probability for \(F_{m,n}\) pulls back to one for \(G\), since the Lipschitz map \(H\) sends Lebesgue null sets to Lebesgue null sets. This proves uniqueness for \(F_{m,n}\).

**3. Signs and entropies.** Under \(\lambda\), each sign corresponds to \(m/2\) left branches or \(n/2\) right branches, with probabilities \((m/2)(1/m)=(n/2)(1/n)=1/2\). Because the underlying branch labels are independent, all sign observations are independent fair signs. The generating branch partition gives
\[
h_\mu(F_{m,n})=-\frac m2\frac1m\log\frac1m-\frac n2\frac1n\log\frac1n
=\frac12(\log m+\log n).
\]
Under the uniform full-shift maximal-entropy measure, each branch label has probability \(1/N\), so the sign probabilities are \((m/2)/N=m/(m+n)\) and \(n/(m+n)\), again independently over all times. The interface \(1/2\) is a branch boundary, so both laws are unaffected by the sign convention on points that ever visit it. For \(m\ne n\), their almost-sure limiting positive-sign frequencies are different, proving mutual singularity. The displayed entropy difference follows directly and is strictly positive by arithmetic-geometric mean. For fixed \(m=2\), as \(n=4k+2\to\infty\), it equals \(\tfrac12\log n+O(1)\), hence is unbounded. This establishes all assertions.

## Verification
The independently runnable `verify.py` enumerates exact rational full branches for five admissible degree pairs, checks their number and inverse-width mass conservation, computes finite independent-sign probabilities through length six, and verifies the claimed topological/metric entropy gap and sign bias. The original recorded output was `VERIFY_OK` for all five pairs and 630 rational sign-word checks. The finite tests support but do not replace the all-degree full-branch proof. The uniqueness argument accounts for the countable set where branch coding may be ambiguous.

## Relationship to prior work
Integer-degree Chebyshev polynomials and the arcsine measure are classical. Related work includes the Chebyshev invariant-measure study of Boyarsky and Góra and the Chebyshev bit-sequence work of Kohda and Tsuneda. Adler gives a general account of symbolic Markov coding. Byers, Góra and Boyarsky study when absolutely continuous invariant measures maximize entropy for piecewise linear Markov transformations; the present family is compatible with those general slope criteria, and its general Markov-theoretic ingredients are not asserted to be novel. The focus here is the simultaneous \(C^1\) gluing, common arcsine invariant density, fair sign process, biased maximal-entropy sign process, and arbitrarily large entropy gap in this explicit family. An equivalent construction under other terminology remains a priority risk.

## Limitations
No claim is made for mismatched congruence classes, general noninteger degrees, other observing partitions, or a \(C^2\) join at zero when \(m\ne n\). The topological entropy and invariant probabilities are not presented as new general theorems on full-branch expanding maps. Prior work on general Markov slope criteria gives a framework for the maximality question; whether an earlier explicit version of this exact two-degree family exists has not been conclusively settled.

## References
- A. Boyarsky and P. Góra, *Invariant measures for Chebyshev maps*, Journal of Applied Mathematics and Stochastic Analysis 14 (2001), 257–264. DOI: 10.1155/S1048953301000211. First online publication 2000-11-01.
- R. L. Adler, *Symbolic Dynamics and Markov Partitions*, arXiv:math/9607214 (1996).
- W. Byers, P. Góra, and A. Boyarsky, *Maximal absolutely continuous invariant measures for piecewise linear Markov transformations*, Ergodic Theory and Dynamical Systems 10 (1990), 645–656. DOI: 10.1017/S0143385700005824.
- Y. Kohda and A. Tsuneda, *Explicit Evaluations of Correlation Functions of Chebyshev Binary and Bit Sequences Based on Perron–Frobenius Operator*, IEICE Transactions E77-A (1994), 1794–1800 (limited comparison).
