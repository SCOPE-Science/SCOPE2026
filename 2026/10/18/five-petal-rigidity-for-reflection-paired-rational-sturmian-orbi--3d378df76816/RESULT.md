# Five-petal rigidity for reflection-paired rational Sturmian orbits

## Finding
Let \(E_2:\mathbb T\to\mathbb T\) denote doubling modulo one, \(R(x)=-x\pmod1\), and let \(O_{k/n}\) be the periodic orbit with binary itinerary the cyclic lower mechanical word
\[
w_i=\left\lfloor\frac{(i+1)k}{n}\right\rfloor-\left\lfloor\frac{ik}{n}\right\rfloor,\quad 0\le i<n.
\]
For every pair of coprime integers \(n\ge3\), \(1\le k<n\), \(2k\ne n\), the smallest number of petals of a doubling flower containing the **two-orbit union** \(K_{k/n}=O_{k/n}\cup R(O_{k/n})\) is exactly **five**. Each individual orbit lies in a one-petal flower. In contrast, the reflection-paired support needs five: neither one nor three petals suffice. The exceptional orbits of slopes zero and one-half are each reflection invariant and need only one petal.

For \(k<n/2\), order the \(2n\) points of \(K_{k/n}\) numerically as \(y_1<\cdots<y_{2n}\), choose for each \(y_i\) its unique predecessor \(x_i\) *within the same finite invariant set*, and put \(b_i=0\) when \(x_i<1/2\) and \(b_i=1\) otherwise. The complete binary predecessor label string is
\[
 b_1\cdots b_{2n}=1^k0^{n-2k}1^k\,0^k1^{n-2k}0^k.
\]
Here superscripts denote ordinary finite word repetition. The five changes between neighboring blocks give the exact minimal petal count.

## Assumptions and scope
A doubling **preimage selector** chooses at every point one of its two inverse images, has only finitely many jump discontinuities, and is right-continuous at the chosen jump conventions; the closure of its image is a flower, whose number of petals equals the number of selector jumps. This standard definition follows Brown, Definition 2.1–2.2. A finite union of periodic doubling orbits is acted on bijectively by doubling; thus its predecessor \(x_i\) is unambiguous. Distinct periodic points cannot be antipodal, since antipodal points have the same image and doubling is injective on this periodic set.

The theorem concerns the canonical rational mechanical orbit and its reflection, not an arbitrary pair of one-flower supports. Integers \(k,n\) are coprime and \(0<k/n<1\), except for the separately stated boundary cases. Every binary expansion used is periodic and non-dyadic; the exceptional constant zero orbit is handled separately. The role of the continuous parameters of a flower is only to choose selector jumps in gaps avoiding the finite orbit.

## Proof
**1. A finite-set jump lemma.** Let \(K\subset\mathbb T\) be a finite, doubling-invariant union of periodic orbits. List its points \(y_1<\cdots<y_N\) in \([0,1)\), and let \(b_i\in\{0,1\}\) identify whether its predecessor in \(K\) is \(y_i/2\) or \((y_i+1)/2\). The minimum possible number of selector jumps required by a flower containing \(K\) is
\[
J(b)=\sum_{i=1}^{N-1}\mathbf1\{b_i\ne b_{i+1}\}+\mathbf1\{b_N=b_1\}.
\]
To see this, both inverse branches vary continuously between successive \(y_i\). Whenever consecutive labels differ, at least one selector switch is necessary. At the circular seam the two local inverse-branch coordinate charts exchange labels, so a further jump is needed precisely when the first and last numerical labels agree. Conversely, choose one jump strictly inside each forced gap, with the given branch on every interval that meets \(K\). The resulting selector has exactly \(J(b)\) jumps; endpoints can be placed off the finite set. For an arbitrary flower containing \(K\), if a selected orbit point lies on a jump boundary, adjust that boundary infinitesimally to retain its orbit point and exclude its antipode (which is absent from \(K\)); this cannot increase the jump count. Hence the count is a lower as well as an upper bound. Equivalently, this is half the circular orbit/antiorbit switch count used for a single orbit in Brown, Section 5; the same elementary selector argument works for a finite invariant union.

**2. The exact predecessor word for one rational mechanical orbit.** First assume \(0<k<n/2\), and write \(\alpha=k/n\). For each phase \(t=j/n\), \(0\le j<n\), define its periodic mechanical digit sequence
\[
w_i(t)=\lfloor t+(i+1)\alpha\rfloor-\lfloor t+i\alpha\rfloor.
\]
Since \(\gcd(k,n)=1\), these are exactly the distinct rotations of the original word: the shift by \(r\) has phase \(j\equiv rk\pmod n\). They occur in increasing lexicographic order as \(t=j/n\) increases. Indeed, for \(0\le t<t'<1\), the partial digit sums through index \(i-1\) equal \(\lfloor t+i\alpha\rfloor\) and \(\lfloor t'+i\alpha\rfloor\). Their difference belongs to \(\{0,1\}\), starts at zero and, at its first change to one, the digit of the larger phase is one while the smaller phase digit is zero. This proves lexicographic monotonicity (strictly for the distinct rational phases). The digit preceding the row of phase \(j/n\) is
\[
\lfloor j/n\rfloor-\lfloor(j-k)/n\rfloor=\begin{cases}1&0\le j<k,\\0&k\le j<n.\end{cases}
\]
Thus the orbit's sorted predecessor labels form \(1^k0^{n-k}\), and its single jump makes its one-petal containment explicit.

**3. Reflect and merge.** Because \(\alpha<1/2\), the mechanical word has no neighboring pair \(11\), including cyclically: after a digit one, the circle rotation phase lies below \(\alpha<1-\alpha\), so the next digit is zero. Every member of \(O_{k/n}\) whose first digit is zero lies strictly below \(1/3\), since the largest infinite binary word beginning with zero and containing no \(11\) is the alternating word \(0.010101\ldots=1/3\). Similarly every point of \(O_{k/n}\) beginning with one is strictly below \(2/3\). Equality in either bound would force the exceptional alternating period-two orbit, excluded by \(2k\ne n\).

It follows that the first-half-circle points of \(O_{k/n}\) all lie below \(1/3\), whereas the first-half-circle points of \(R(O_{k/n})\), being reflections of the upper-half points of \(O_{k/n}\), all lie above \(1/3\). Therefore the first half of the sorted union contains first the \(n-k\) points of the original orbit with initial zero, and next the \(k\) first-half points of its reflection. From Step 2, the original block has predecessor labels \(1^k0^{n-2k}\). Each reflected point in this half has predecessor label one: its unreflected counterpart lies in the *upper* half of the original orbit, where the last \(k\) labels in \(1^k0^{n-k}\) are zero; reflection exchanges inverse branches. Hence the first-half labels are exactly \(1^k0^{n-2k}1^k\).

Reflection maps \(y\mapsto1-y\), reverses order, and complements the predecessor label. Thus the second-half labels are the reversed bit-complement of the first-half labels, namely \(0^k1^{n-2k}0^k\). The concatenation is the claimed full label word. Since \(k\ge1\) and \(n-2k\ge1\), all six alternating blocks are nonempty. There are exactly five internal binary label switches, while the final label zero differs from the initial label one, adding no seam jump. The jump lemma therefore gives exactly five petals.

**4. Other slopes and boundaries.** The binary complement of a period-\(n\) mechanical word of slope \(\alpha\) is a cyclic mechanical word of slope \(1-\alpha\); complementing all digits implements the reflection \(R\) of its non-dyadic circle point. Therefore \(K_{\alpha}=K_{1-\alpha}\), so the preceding proof covers all rational \(\alpha\in(1/2,1)\). When \(\alpha=1/2\) the primitive word is \(01\) and the orbit \(\{1/3,2/3\}\) is its own reflection and lies in a semicircle. At slope zero the fixed orbit \(\{0\}\) is likewise symmetric and one-petal. These exhaust the rational mechanical cases.

## Verification
Exact rational replay is possible without numerical floating-point calculations. Enumerate reduced fractions \(k/n\) with \(3\le n\le23\), omit \(2k=n\), construct the periodic binary words, convert each cyclic rotation to its exact fraction with denominator \(2^n-1\), add reflected points, and determine the unique predecessor digits of their sorted union. The accompanying `verify.py` asserts the six-block formula and the exact cardinality \(2n\) in 170 cases. A finite enumeration checks those instances only; the preceding symbolic argument proves the theorem for every admissible denominator.

## Relationship to prior work
Brown (2026) introduces flowers and identifies the interlacing number of **one periodic orbit** with its petal count, and provides numerical tallies through period 14 (Section 5). This interlacing criterion is acknowledged prior work, not the new theorem. Brown also gives a three-petal example supporting two different periodic measures (Section 4), but does not evaluate the exact flower cost of the **reflection-paired rational mechanical orbit union**. The present contribution is the complete parameter-independent five-petal rigidity of that canonical two-orbit construction, including an exact six-block predecessor word and the exceptional reflection-fixed phases.

Classical theory of Christoffel/mechanical words supplies their individual balanced periodic codings. The independent Burrows–Wheeler literature, including Giuliani and collaborators (2024), examines sorting cyclic word rotations and run counts; its studied examples do not state the flower complexity of the above reflection-paired invariant sets. The sorted predecessor block calculation is supplied here directly rather than asserted as a novelty claim for individual words. An equivalent formulation buried in earlier orbit-ordering or word combinatorics work remains a bibliographic priority risk.

## Limitations
No upper bound of five is claimed for arbitrary unions of two Sturmian orbits or arbitrary two-orbit sets; the reflection pairing and rational mechanical hypotheses are essential. The theorem is a classification of finite orbit supports, not a characterization of maximizing potentials, and it does not address irrational Sturmian Cantor supports. Independent audit or exhaustive historical priority certification has not occurred.

## References
1. M. Brown, *Expanding Maps on Flowers, Interval Exchange Transformations, and Ergodic Optimization*, arXiv:2605.06962v1, first posted 2026-05-07, especially Definition 2.1–2.2, Section 4 examples, and Section 5.
2. S. Giuliani, S. Inenaga, Z. Lipták, G. Romana, M. Sciortino and C. Urbina, *Bit catastrophes for the Burrows-Wheeler Transform*, arXiv:2404.10426, 2024, Sections 2 and 4, for context on cyclic rotation sorting and BWT run counts.
3. S. Bullett and P. Sentenac, *Ordered orbits of the shift, square roots, and the devil's staircase*, Mathematical Proceedings of the Cambridge Philosophical Society 115 (1994), 451–481, as cited and discussed by Brown.
