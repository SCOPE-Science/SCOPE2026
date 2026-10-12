# Nineteen components of the alternating reciprocal-cube divisor-sum range

## Finding
Let \(s_{-3}\) be the multiplicative function on positive integers specified for each prime \(p\) and nonnegative integer \(a\) by
\[
s_{-3}(p^a)=\sum_{k=0}^{a}(-p^{-3})^k.
\]
Define the positive constant
\[
T=\prod_{p\ge11}(1-p^{-3})
 =\frac1{\zeta(3)\prod_{p\in\{2,3,5,7\}}(1-p^{-3})}.
\]
Then the closure in \(\mathbb R\) of the range of \(s_{-3}\) has **exactly nineteen connected components**, with **eighteen strict gaps**. Explicitly,
\[
\boxed{\overline{s_{-3}(\mathbb N)}=\bigcup_{j=1}^{19}[L_jT,U_j]}.
\]
The following is the complete exact endpoint table; each coefficient is a rational number.

| \(j\) | \(L_j\) | \(U_j\) |
|---:|---:|---:|
| 1 | \(\frac{15314}{18375}\) | \(\frac{25426807}{30375000}\) |
| 2 | \(\frac{247}{294}\) | \(\frac{4921}{5832}\) |
| 3 | \(\frac{99541}{117600}\) | \(\frac{13357}{15552}\) |
| 4 | \(\frac{5301}{6125}\) | \(\frac{1818375807}{2100875000}\) |
| 5 | \(\frac{217}{250}\) | \(\frac{108507}{125000}\) |
| 6 | \(\frac{171}{196}\) | \(\frac{117307}{134456}\) |
| 7 | \(\frac{7}{8}\) | \(\frac{7}{8}\) |
| 8 | \(\frac{68913}{78400}\) | \(\frac{6620706313287}{7529536000000}\) |
| 9 | \(\frac{302157}{343000}\) | \(\frac{56439141}{64000000}\) |
| 10 | \(\frac{1767}{2000}\) | \(\frac{883557}{1000000}\) |
| 11 | \(\frac{11115}{12544}\) | \(\frac{427114787}{481890304}\) |
| 12 | \(\frac{9747}{10976}\) | \(\frac{3641}{4096}\) |
| 13 | \(\frac{57}{64}\) | \(\frac{57}{64}\) |
| 14 | \(\frac{122512}{128625}\) | \(\frac{3632401}{3796875}\) |
| 15 | \(\frac{988}{1029}\) | \(\frac{703}{729}\) |
| 16 | \(\frac{42408}{42875}\) | \(\frac{1818375807}{1838265625}\) |
| 17 | \(\frac{124}{125}\) | \(\frac{15501}{15625}\) |
| 18 | \(\frac{342}{343}\) | \(\frac{117307}{117649}\) |
| 19 | \(1\) | \(1\) |

## Assumptions and scope
All integers are positive, all prime-power exponents are nonnegative, and the closure is topological closure in the real line. Products over prime numbers converge absolutely. The assertion is solely for the alternating divisor function at parameter \(r=3\), not the ordinary generalized divisor function \(\sigma_{-3}\). The expression \([L_jT,U_j]\) is a genuine interval, with endpoints as displayed; the nineteen intervals are pairwise disjoint.

## Proof
**1. The prime tail fills an interval.** For any prime \(p\), set \(y=p^{-3}\) and \(u_p(a)=\sum_{k=0}^a(-y)^k\). Its least possible value is \(u_p(1)=1-y\), while \(u_p(0)=1\) is largest. For \(p\ge11\), set
\[
T_p=\prod_{q\ge p}(1-q^{-3}),\qquad T_{>p}=\prod_{q>p}(1-q^{-3}).
\]
We first establish \(T_{>p}\le u_p(2)=1-p^{-3}+p^{-6}\) for **every** prime \(p\ge11\). In each of the five cases \(p=11,13,17,19,23\), the following larger primes have a reciprocal-cube sum exceeding \(p^{-3}\), by exact rational inequalities:
\[
\begin{array}{c|l}
11&13,17,19\\
13&17,19,23,29\\
17&19,23\\
19&23,29,31\\
23&29,31,37
\end{array}
\]
For every \(p\ge29\), Nagura's theorem (a prime exists strictly between \(x\) and \(6x/5\) for every \(x\ge25\)) gives three distinct subsequent primes \(q_1,q_2,q_3\) with \(p<q_j<(6/5)^jp\). Hence
\[
\sum_{q>p}q^{-3}>p^{-3}\sum_{j=1}^3(5/6)^{3j}>p^{-3}.
\]
In all cases, the Euler factors and the bound \(e^{-t}<1-t+t^2\) for \(t>0\) yield
\[
T_{>p}\le \exp\!\left(-\sum_{q>p}q^{-3}\right)
<e^{-p^{-3}}<1-p^{-3}+p^{-6}=u_p(2).
\]
Now order the local values \(u_p(a)\) from lowest to highest, including their accumulation point \((1+y)^{-1}\). Their largest consecutive *logarithmic* gap is the gap between \(u_p(2)\) and \(u_p(0)=1\). This follows directly by comparing successive even exponents and successive odd exponents (and also follows from Defant's Lemma 2.2). Accordingly the closed intervals
\[
[u_p(a)T_{>p},u_p(a)]\quad(a\ge0)
\]
form an overlapping chain whose closure covers \([T_p,1]\). Choose such an exponent successively at primes \(p\ge11\) for any target \(z\in[T,1]\); at each step the residual target remains between the remaining tail product and \(1\). Since these residual endpoints both converge to \(1\), the finite partial products of the selected prime-power factors converge to \(z\). Conversely, every tail-only value lies in \([T,1]\). Thus
\[
\overline{\{s_{-3}(m):\gcd(m,210)=1\}}=[T,1].
\]
**2. The four small primes give 32 exact interval blocks.** At \(p=2\), the exponent classes \(0,1,2,\ge3\) contribute the following local lower/upper factor pairs:
\[
(1,1),\ (7/8,7/8),\ (57/64,57/64),\ (455/512,3641/4096).
\]
At each of \(p=3,5,7\), the exponent classes \(0,\ge1\) contribute respectively \((1,1)\) and \((u_p(1),u_p(2))\). The two endpoint exponent choices within each nonsingleton class produce overlapping tail intervals. Their overlap follows from the strict rationally verified inequalities
\[
u_p(2)T\le u_p(1)\quad(p=3,5,7),\qquad
u_2(4)T\le u_2(3).
\]
For any fixed choices of classes at the four primes, changing just one endpoint exponent also preserves interval overlap (other local factors cancel). Thus all exponent choices in one class tuple form a connected chain, and every further exponent belongs between its extreme values. Each class tuple therefore supplies exactly one interval
\[
\left[\left(\prod_{p\in\{2,3,5,7\}}\ell_p\right)T,
\ \prod_{p\in\{2,3,5,7\}}u_p\right],
\]
where \(\ell_p,u_p\) are its listed lower and upper factors. There are \(4\cdot2^3=32\) class tuples; no integer falls outside them.

**3. Rational certificates for all mergers and strict gaps.** The accompanying standalone `verify.py` constructs all 32 intervals as exact rational coefficient pairs. It bounds \(\zeta(3)\) between
\[
Z_N+\frac1{2(N+1)^2}<\zeta(3)<Z_N+\frac1{2N^2},\qquad
Z_N=\sum_{k=1}^N\frac1{k^3},\quad N=180.
\]
These yield rational lower and upper bounds for \(T\). For every pair of consecutive intervals in increasing lower-endpoint order, the program certifies either an overlap for **every** permitted \(T\), or a strict gap for **every** permitted \(T\), using only integer arithmetic and the `Fraction` class. Thirteen overlaps merge the 32 intervals into 19 nonempty components, with eighteen strict gaps. It checks the exact rational endpoints of every component as in the table. Thus the displayed 19 intervals are precisely the closure of the entire range.

## Verification
Run `python3 verify.py` with an unmodified Python 3 standard library. The expected final line is `EXACT_CERTIFICATE_OK local_states=32 components=19 gaps=18 overlaps=13 zeta_terms=180 tail_witnesses=5`. All finite prime witnesses, the rational bound for \(T\), local exponent block overlaps, and 32-to-19 interval comparisons are checked from first principles by the included source. The infinite prime-tail coverage is established in the proof using the cited Nagura theorem; it is **not** inferred from finite enumeration. The implementation computes each coefficient from local alternating sums rather than accepting the table as input.

## Relationship to prior work
Defant introduced \(s_{-r}\), proved a general density criterion, and explicitly asked which parameters give a prescribed exact number of closure intervals. The 2015 work establishes that \(r=3\) is on the nondense side but does not compute its number of components. A separately published classification gives exactly two components at \(r=2\) and explicitly makes no assertion for other parameters. Its endpoints and proof do not imply a component count at \(r=3\). Ordinary and unitary generalized divisor sums use different prime-power factors and likewise do not imply the present alternating-function classification. This theorem answers the component-count question at \(r=3\) together with all endpoints.

## Limitations
The theorem determines the closure at the single parameter \(r=3\) only. It does not calculate the natural densities associated with the nineteen intervals, characterize nearby real parameters, or assert new facts about ordinary generalized divisor sums. The main proof uses Nagura's established prime-interval theorem. Literature searching cannot exclude all unindexed or unpublished prior discoveries.

## References
1. Colin Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128v1 (first submitted 2015-07-04), Definition 1.1, Lemma 2.2, Theorem 2.4 and Section 3 (open problem). https://arxiv.org/html/1507.01128v1
2. Jitsuro Nagura, *On the Interval Containing at Least One Prime Number*, Proceedings of the Japan Academy **28** (1952), 177–181, doi:10.3792/pja/1195570997.
3. *Exactly two closure components for the alternating divisor range at parameter two*, public result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exactly-two-closure-components-for-the-alternating-divisor-range--f19c7ab30430.
