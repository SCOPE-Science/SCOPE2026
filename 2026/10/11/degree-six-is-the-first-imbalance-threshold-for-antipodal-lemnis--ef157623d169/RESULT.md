# Degree six is the first imbalance threshold for antipodal lemniscate area

## Finding
For integers \(n\ge1\) and \(0\le k\le n\), set
\[
p_{n,k}(z)=(z-1)^k(z+1)^{n-k},\qquad
A_{n,k}=\operatorname{Area}\{z\in\mathbb C:|p_{n,k}(z)|<1\}.
\]
This is the exact two-site specialization of the polynomial-lemniscate area minimization problem, where the only permitted zeros are the antipodal points \(-1\) and \(1\), with repetitions allowed. The allocation \(k\) is called balanced when \(k\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\).

**Theorem.** For each degree \(1\le n\le5\), exactly the balanced allocations minimize \(A_{n,k}\) among all \(0\le k\le n\). For degree six the unique minimizing allocations are \(k=2\) and \(k=4\); their common area is strictly less than the balanced area \(A_{6,3}=2\). In every degree divisible by six, a balanced allocation fails to minimize, witnessed by the competing multiplicity ratio \(1:2\).

More quantitatively, the following entirely rational strict enclosure holds:
\[
\frac{126966}{65536}\le A_{6,2}=A_{3,1}\le\frac{129888}{65536}
<2=A_{6,3}<\frac{158192}{65536}\le A_{6,1}.
\]
No claim is made that the displayed allocations minimize among polynomials whose zeros can lie at arbitrary points of the unit circle or disk.

## Assumptions and scope
Area means two-dimensional Lebesgue measure of the **strict** sublevel set. The polynomial is monic and all its zeros, counted with multiplicity, belong to the **fixed** set \(\{-1,1\}\), not to the full unit circle. The primary classification is for the six degrees \(1\) through \(6\); the obstruction in multiples of six is a direct consequence, not an assertion about every larger degree. Both endpoints must be permitted, but an allocation may use only one of them. Boundary equality has no effect on area because the polynomial level set has planar measure zero.

## Proof
**1. Symmetry and powers.** The substitution \(z\mapsto-z\) gives \(A_{n,k}=A_{n,n-k}\). If \(q\) is any nonconstant polynomial and \(m\ge1\) is an integer, then \(\{|q(z)^m|<1\}=\{|q(z)|<1\}\). In particular \(A_{n,0}=A_{n,n}=\pi\), since these are unit disks, and \(A_{6m,2m}=A_{6,2}\) and \(A_{6m,3m}=A_{6,3}\).

**2. Exact balanced even-degree area.** For \(n=2m\), the balanced polynomial is \((z^2-1)^m\); its strict unit lemniscate equals \(\{|z^2-1|<1\}\). In polar coordinates \(z=r e^{i\theta}\), the inequality simplifies to \(0\le r^2<2\cos(2\theta)\) wherever the cosine is positive. Thus its area is
\[
\frac12\int_0^{2\pi}\max\{2\cos(2\theta),0\}\,d\theta=2.
\]
Consequently \(A_{2,1}=A_{4,2}=A_{6,3}=2\), exactly.

**3. A finite *exhaustive* rational enclosure lemma.** For any \(n,k\), set \(D=256\). Cover \([-2,2]^2\) by its natural closed dyadic squares, whose sides on the final level have length \(D^{-1}\). A square \(S=[a,b]\times[c,d]\) in integer-scaled coordinates corresponds to \([a/D,b/D]\times[c/D,d/D]\). Let \(\ell_+(S),u_+(S)\) be the exact minimum and maximum of \((X-D)^2+Y^2\) on this integer-coordinate rectangle, and define \(\ell_-(S),u_-(S)\) with \(D\) replaced by \(-D\). Elementary convexity of squared distance gives
\[
\ell_\pm(S)=\operatorname{dist}(\pm D,[a,b])^2+\operatorname{dist}(0,[c,d])^2,
\quad u_\pm(S)=\max\{(a\mp D)^2,(b\mp D)^2\}+\max\{c^2,d^2\}.
\]
For all points in \(S\), the exact integer products bound \(D^{2n}|p_{n,k}(z)|^2\) below by \(\ell_+(S)^k\ell_-(S)^{n-k}\) and above by \(u_+(S)^ku_-(S)^{n-k}\). If the lower product is at least \(D^{2n}\), the whole square is exterior (up to the zero-measure boundary). If the upper product is strictly below \(D^{2n}\), the whole square is interior. Otherwise bisect the square in both directions and repeat, until reaching side length \(1/D\). At that terminal scale an undecided square contributes zero to the lower area and its full area to the upper area. The recursion visits **all** remaining squares, so it is not point sampling or partial enumeration. Furthermore, the entire strict lemniscate lies inside \(\{|z|<2\}\): if \(|z|\ge2\), then \(|z\pm1|\ge|z|-1\ge1\), hence \(|p_{n,k}(z)|\ge1\). Thus the initial square contains all area to be counted. The union of rectangular boundaries has measure zero.

The standalone `verify_area.py`, using only Python integer arithmetic, implements these bounds and obtains the following rigorous lower and upper numerators, all over the common area denominator \(65536\):

| Degree \(n\) | Multiplicity \(k\) | Lower numerator | Upper numerator |
|---:|---:|---:|---:|
| 3 | 1 | 126966 | 129888 |
| 4 | 1 | 138338 | 140672 |
| 5 | 1 | 149516 | 151682 |
| 5 | 2 | 125242 | 128836 |
| 6 | 1 | 158192 | 160260 |
| 6 | 2 | 126966 | 129888 |

The repeat at degrees three and six is independently forced by the power identity, providing an internal consistency check. Crucial comparisons are **strict integer inequalities**:
\[
129888<131072=2\cdot65536<138338,
\qquad128836<149516,
\qquad129888<131072<158192.
\]

**4. Exhausting the multiplicity allocations.** By symmetry, only \(0\le k\le\lfloor n/2\rfloor\) need comparison. In degree one both allocations are balanced. In degree two, the balanced area is \(2<\pi\). In degree three, the balanced allocation \(k=1\) has area at most \(129888/65536<2<\pi\), so it beats \(k=0\). In degree four, \(k=2\) has area two and beats \(k=1\), whose area is greater than two, and \(k=0\), whose area is \(\pi>2\). In degree five, the balanced \(k=2\) has area at most \(128836/65536\), strictly smaller than the lower bound \(149516/65536\) for \(k=1\) and smaller than \(\pi\) for \(k=0\). In degree six, \(k=2\) has area at most \(129888/65536<2\), defeating the balanced \(k=3\); \(k=1\) has area exceeding two and \(k=0\) has area \(\pi>2\). All minimizers follow by reflection symmetry. Finally, taking powers of the winning and losing sextics proves \(A_{6m,2m}<A_{6m,3m}\) for every \(m\ge1\). This completes the proof.

## Verification
Run `python verify_area.py` with Python 3 and no dependencies. It verifies six exact rational enclosures, checks the strict cross-degree comparisons as integer assertions, and prints `ALL EXACT AREA ENCLOSURES AND OPTIMIZER COMPARISONS PASS`. Unlike floating-point quadrature, the algorithm bounds the squared absolute value over each entire dyadic box and accounts for every box. The source is included as a standalone reproducibility artifact; no external tables or downloads are required.

## Relationship to prior work
Krishnapur, Lundberg and Ramachandran (2025) study area-minimizing polynomial lemniscates under unit-disk and unit-circle root constraints, prove asymptotic bounds, and numerically explore low-degree minimizing configurations in their Section 10. Their Figure 1 specifically notes a locally minimal cubic configuration with a doubled antipodal root, but it is not a global minimizer when all unit-circle root positions are permitted. That observation concerns a **different** optimization domain: the present classification fixes both sites at the antipodes and proves strict comparisons for all multiplicities up to degree six, using rigorous area certificates rather than the cited lattice sampling. Ghosh and Ramachandran (2026), and Pendyala (2026), study different large-degree/compact-set regimes; their accessible statements do not imply this exact finite two-site classification. Classical Cassini-oval identities explain the balanced even-degree benchmark, not the cubic comparison or the first failure in degree six.

## Limitations
The exact inequalities determine the minimizing **allocation** only when zeros must be \(-1\) or \(+1\); they do not determine unrestricted degree-six Erdős lemniscate minimizers. The interval certificate does not give a closed form for the cubic area or optimal quantitative gap, although its strict separation suffices. Its exhaustiveness is finite and exact, and is not being extrapolated to arbitrary unrelated degrees. The 2026 Pendyala manuscript was not available for complete primary-text inspection; unindexed equivalent prior work cannot be excluded by literature searches alone. Independent audit has not been performed.

## References
1. M. Krishnapur, E. Lundberg, K. Ramachandran, *On the area of polynomial lemniscates*, first public 2025-03-24, arXiv:2503.18270. https://arxiv.org/abs/2503.18270
2. S. Ghosh, K. Ramachandran, *A note on the Erdös minimal area problem*, first public 2026-04-03, arXiv:2604.03036. https://arxiv.org/abs/2604.03036
3. V. S. Pendyala, *Sharp order in Erdős's minimum-area problem for polynomial lemniscates*, first public 2026-06-13, arXiv:2606.17097. https://arxiv.org/abs/2606.17097
4. Classical Cassini-oval and Bernoulli-lemniscate polar parametrization; see e.g. https://mathworld.wolfram.com/CassiniOvals.html
