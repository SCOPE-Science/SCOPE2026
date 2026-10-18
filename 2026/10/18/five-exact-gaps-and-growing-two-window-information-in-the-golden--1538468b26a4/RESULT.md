# Five exact gaps and growing two-window information in the golden Sturmian rotation

## Finding

Let \(r=(\sqrt5-1)/2\), \(\alpha=r^2\), and let \(F_1=F_2=1\), \(F_{j+1}=F_j+F_{j-1}\). Fix an integer \(k\ge6\), write \(n=F_k\), and place the following \(2n+2\) points on the unit circle:

\[
\mathcal E_k=\{\{j\alpha\}:0\le j\le n\}\cup\{\{j\alpha\}:2n\le j\le3n\}.
\]

Braces inside the set denote fractional part; all points are distinct. The exact histogram of clockwise gaps between consecutive points is

\[
\begin{array}{c|ccccc}
\text{gap length}&r^{k+2}&r^{k+1}&r^k&r^{k-1}&2r^k\\\hline
\text{multiplicity}&F_{k-2}+1&F_{k-1}+1&1&2F_{k-2}&F_{k-3}-1.
\end{array}
\]

All five lengths occur for every \(k\ge6\), and their multiplicities sum to \(2F_k+2\). In contrast, the single block \(\{\{j\alpha\}:0\le j\le n\}\) has the exact three-gap histogram

\[
\begin{array}{c|ccc}
\text{gap length}&r^{k-2}&r^{k-1}&r^k\\\hline
\text{multiplicity}&F_{k-1}-1&F_{k-2}+1&1.
\end{array}
\]

For the Haar-stationary rotation \(R_\alpha(x)=x+\alpha\pmod1\), define the Sturmian observations \(Z_j(x)=\mathbf 1_{[1-\alpha,1)}(R_\alpha^j x)\). Denote the two separated observation words of length \(n\) by \(A_k=(Z_0,\ldots,Z_{n-1})\) and \(B_k=(Z_{2n},\ldots,Z_{3n-1})\). Let

\[
\mathcal H\bigl((c_i,\ell_i)_{i=1}^s\bigr):=-\sum_{i=1}^{s}c_i\ell_i\log\ell_i.
\]

Write \(\mathcal L_k\) and \(\mathcal J_k\) for the respective count/length pairs in the three-gap and five-gap tables. In natural logarithm units, the exact two-word mutual information is

\[
I(A_k;B_k)=2\mathcal H(\mathcal L_k)-\mathcal H(\mathcal J_k).
\]

In particular,

\[
I(A_k;B_k)=\log F_k+C+o(1),
\]

where the explicit finite constant is

\[
C=\log\sqrt5+\frac{4/r+2r^4+r^2}{\sqrt5}\log r+\frac{2r^3}{\sqrt5}\log2
=-0.5867552564501619\ldots.
\]

Thus the information shared by two observation blocks of Fibonacci length, separated by one entire block of the same length, grows logarithmically even though the system has zero entropy rate.

## Assumptions and scope

Everything above concerns the specified irrational angle \(\alpha=(3-\sqrt5)/2\), integer Fibonacci orders \(k\ge6\), the indicated two index intervals, Lebesgue/Haar initial distribution, and the canonical binary Sturmian partition. Mutual information and entropy are measured in nats. No assertion is made for different separations, arbitrary irrational angles, or finite-state Markov approximations. Endpoints have measure zero and do not affect distributions.

## Proof

**Quadratic identities and the single-block circle order.** Fibonacci induction and \(r^2=1-r\) give

\[
F_k\alpha=F_{k-2}+(-1)^k r^k,
\qquad
F_{k-1}r^{k-2}+F_{k-2}r^{k-1}=1.
\]

We first take even \(k\), put \(p_j=\{j\alpha\}\) for \(0\le j\le n\), and write \(\varepsilon=r^k\). All intervals below are clockwise. Define a successor of each index by

\[
s(0)=n,\qquad
s(j)=\begin{cases}
j+F_{k-2},&1\le j<F_{k-1},\\
j-F_{k-1},&F_{k-1}\le j\le n.
\end{cases}
\]

The displacement from \(p_j\) to \(p_{s(j)}\), taken clockwise, is respectively \(\varepsilon\), \(r^{k-2}\), and \(r^{k-1}\). Indeed, the stated Fibonacci identity evaluates each displacement modulo one, and all three values lie strictly between zero and one. The successor permutation is obtained from addition by \(F_{k-2}\) modulo \(F_k\) by subdividing its edge out of zero with the intermediate vertex \(n\). Since \(\gcd(F_{k-2},F_k)=1\), it is a single cycle. The total length of its proposed arcs is

\[
\varepsilon+(F_{k-1}-1)r^{k-2}+(F_{k-2}+1)r^{k-1}=1.
\]

A positive-length cyclic polygonal walk of total winding length one cannot skip an intervening vertex. Hence the successors are exactly the clockwise neighbors and yield the three-gap table. For odd \(k\), reflect the circle \(x\mapsto-x\), so the Fibonacci error changes sign; the same successor computation then applies with clockwise orientation in the reflected coordinate. Reflection preserves all gap lengths.

**Insertion of the second block.** In the reflected coordinate when needed, \(\{(2n+j)\alpha\}=p_j+2\varepsilon\pmod1\). Thus the second block is a copy of the first translated clockwise by \(2\varepsilon\). Since \(\varepsilon<2\varepsilon<r^{k-2}=\varepsilon/r^2\), each translated point lies within the same base long gap or, when following a shorter gap, within the next base gap. The complete subdivision of the base gaps is as follows, with every listed length implicitly multiplied by \(\varepsilon\):

* The unique short gap starting at \(p_0\) is split into lengths \(r^2\), \(r\).
* The medium gap starting at \(p_n\) is split into lengths \(1\), \(r\).
* The other \(F_{k-2}\) medium gaps are not split; each retains length \(1/r\).
* Each of the \(F_{k-2}\) long gaps starting at an index \(1\le j\le F_{k-2}\) contains two translated points. The ordered pieces have lengths \(r^2\), \(1/r\), \(r\).
* Each of the remaining \(F_{k-3}-1\) long gaps contains one translated point and is cut into lengths \(2\), \(r\).

For completeness, the translated point of index \(F_{k-1}\) enters the short gap with residual displacement \((2-1/r)\varepsilon=r^2\varepsilon\); the translated point of index zero enters the medium gap starting at \(p_n\) with residual \(\varepsilon\). For \(1\le j\le F_{k-2}\), the translated points of indices \(j+F_{k-1}\) and \(j\) enter the long gap at \(p_j\) at displacements \(r^2\varepsilon\) and \(2\varepsilon\), respectively. The remaining translated points enter the remaining long gaps at displacement \(2\varepsilon\). The identities \(2-r^2=1/r\) and \(1/r^2-2=r\) verify the subdivisions, and these assignments exhaust exactly \(n+1\) translated points. Counting the pieces proves the five-gap histogram. Its distinct lengths obey \(r^2\varepsilon<r\varepsilon<\varepsilon<\varepsilon/r<2\varepsilon\).

**From gap lengths to the full joint distribution.** For the canonical Sturmian partition, the length-\(n\) observation words form \(n+1\) distinct interval cylinders, bounded by the points \(\{-j\alpha\}\) with \(0\le j\le n\). This also follows directly by refining the two interval atoms under the rotation and checking which single boundary is introduced at each step. The later block's cylinders have endpoints at indices \(2n\) through \(3n\). Reflection of the circle maps the two endpoint sets to the two sets in \(\mathcal E_k\), preserving lengths.

Each single-block atom has length at most \(r^{k-2}<1/2\). Any intersection of two circular arcs each of length less than \(1/2\) is connected whenever nonempty: two disconnected intersection components would force the two arcs together to cover the full circle. Therefore no pair of distinct component intervals has the same ordered pair of length-\(n\) words. The \(2n+2\) intervals in the five-gap table are precisely the positive-probability joint-word cylinders. Their Lebesgue probabilities are their lengths. The two marginal word entropies are each \(\mathcal H(\mathcal L_k)\), the joint entropy is \(\mathcal H(\mathcal J_k)\), and the asserted exact mutual-information formula follows.

**Asymptotic information constant.** Binet's formula yields \(F_k r^k\to 1/\sqrt5\) and \(F_{k-j}/F_k\to r^j\) for each fixed \(j\). Multiplying each interval length in the tables by \(F_k\), and dividing each count by \(F_k\), gives the limiting one-block normalized mass/length pairs

\[
(r,1/(\sqrt5r^2)),\quad(r^2,1/(\sqrt5r)),
\]

and limiting joint pairs

\[
(r^2,r^2/\sqrt5),\quad(r,r/\sqrt5),\quad(2r^2,1/(\sqrt5r)),\quad(r^3,2/\sqrt5).
\]

The isolated count-one gap contributes \(o(1)\) to centered entropy. Substituting the remaining four and two limiting pairs into \(-\sum c_i\ell_i\log\ell_i\), and using \(r^2+r=1\), produces the stated \(C\). In particular, each entropy equals \(\log F_k\) plus its corresponding finite limiting correction; subtracting gives \(I=\log F_k+C+o(1)\).

## Verification

The accompanying standalone `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt5)\), with exact sign comparisons, to enumerate and check the one- and two-window cyclic gap histograms for Fibonacci orders \(6\le k\le14\). For \(6\le k\le11\), it independently checks that all \(2F_k+2\) joint observation words correspond bijectively to the refined rotation cells. It also compares the information asymptotic with direct finite table evaluations. Executed result: `VERIFY_OK: exact field gap histograms at 9 Fibonacci orders, 6 joint-word partitions, entropy limit -0.586755256450162`. These finite tests independently corroborate the formulas; the all-order proof is the exact successor and subdivision argument above.

## Relationship to prior work

The Sturmian partition and its usual consecutive refinements, including the three-length theorem, are classical. Kupsa and Starosta's *On the partitions with Sturmian-like refinements* (first public preprint 2013-03-14, arXiv:1303.3387), in particular Section 1, Theorem 1, and Section 2.1, studies refinements of fixed Sturmian-measurable partitions, describes single consecutive-block rotation intervals, and develops eventual injectivity. It does not identify the present exact gap histogram for two disjoint Fibonacci-length index windows, their word-pair probabilities, or the resulting two-window information constant.

Liang's *A short proof of the 3d distance theorem* (1979), and the open full text of Mishra and Philip's *A generalization of the 3d distance theorem* (arXiv:1910.00865, Theorem 1.1), explain why unions of two arithmetic progressions admit an absolute bound of six gap lengths. A six-length upper bound alone does not determine that exactly five values arise for this specified family, much less their multiplicities and Shannon information. The present formula refines this general finite-distance phenomenon in a natural golden-rotation two-window case.

## Limitations

Only the stated golden angle, Fibonacci times, and separation \(2F_k\) are analyzed. No uniform statement in arbitrary lags or slopes follows. Although complete accessible preprints and relevant indexed comparisons were examined, priority against every historical publication cannot be certified. In particular, the full text of Liang (1979) was not available for comparison, and classical interval-exchange/three-distance literature could contain an implicit equivalent special case. The proof does not require any unverified numerical step; no independent scientific audit has been performed.

## References

1. M. Kupsa and Š. Starosta, *On the partitions with Sturmian-like refinements*, arXiv:1303.3387, first submitted 14 March 2013, later DCDS-A 35 (2015), 3483–3501. https://arxiv.org/html/1303.3387v2
2. M. Mishra and A. B. Philip, *A generalization of the 3d distance theorem*, arXiv:1910.00865, first submitted 2 October 2019. https://arxiv.org/html/1910.00865v2
3. F. M. Liang, *A short proof of the 3d distance theorem*, Discrete Mathematics 28 (1979), 325–326. DOI: 10.1016/0012-365X(79)90140-7 (bibliographic metadata inspected; full text inaccessible).
4. F. Chung and R. Graham, *On the set of distances determined by the union of arithmetic progressions*, Ars Combinatoria 1 (1976), 57–76 (general background; not inspected in full).
