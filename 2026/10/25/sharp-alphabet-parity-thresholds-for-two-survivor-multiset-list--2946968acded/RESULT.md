# Sharp alphabet-parity thresholds for two-survivor multiset list decoding

## Finding

For an unordered multiset deletion channel with a fixed alphabet of \(q\ge4\) symbols, exactly two surviving symbols, and decoder list allowance \(L\), let \(M_q(n,L;2)\) be the largest codebook of distinct source multisets of size \(n\) for which every possible received two-symbol multiset is produced by at most \(L\) codewords.

Put \(k=2^{q-3}\), \(K=4k=2^{q-1}\), \(E=(q+2)k\), \(L_0=(q+3)k\), and
\[
B_q(L)=\left\lfloor\frac{qL}{2}\right\rfloor+q2^{q-2}.
\]
For every \(n\ge q+1\), \(M_q(n,L;2)\le B_q(L)\). This bound cannot be attained at any source length \(n\ge q+1\) if \(L<L_0\) when \(q\) is even or if \(L<L_0-1\) when \(q\) is odd. At the first admissible list allowance, equality is attained as follows:

* For even \(q\), at \(L=L_0\), equality holds for every \(n\ge\max\{q+1,3+k\}\).
* For odd \(q\), at \(L=L_0-1\), equality holds for every \(n\ge\max\{q+1,3+k\}\).

More generally, for every \(L\ge L_0\), equality holds whenever
\[
n\ge\max\left\{q+1,3+\left\lceil\frac{L-K}{q-1}\right\rceil\right\}.
\]
At \(L=L_0\), for all \(n\ge\max\{q+1,3+k\}\), every optimal code is obtained by including **all** singly-heavy multisets (exactly one symbol of multiplicity at least two) and, independently for every unordered distinct-symbol pair, choosing exactly \(k\) of the \(n-3\) two-symbol multisets in which both multiplicities are at least two. Therefore the exact number of labeled optimum codebooks is
\[
\binom{n-3}{k}^{\binom q2}.
\]
For instance, \(M_4(5,14;2)=44\) with a unique labeled optimum, whereas \(M_4(n,13;2)<42\) for all \(n\ge5\). For odd-alphabet illustration, \(M_5(n,31;2)=117\) for every \(n\ge7\).

## Assumptions and scope

Messages are integer vectors \(x=(x_0,\ldots,x_{q-1})\) with \(x_i\ge0\), \(\sum_i x_i=n\). A received message is an integer vector \(y\) of sum two with \(0\le y_i\le x_i\) coordinatewise. Each distinct input multiset is either included once or excluded; the decoder must return no more than \(L\) inputs for each such \(y\). Symbols are labeled. Assumptions throughout: \(q\ge4\), \(n\ge q+1\), \(L\) a positive integer. The early-onset statement identifies when the specific incidence bound becomes sharp; it is not an exact capacity formula for every smaller \(L\) or \(n\).

## Proof

**1. Incidence upper bound.** Because \(n\ge q+1\), each word has a *heavy* coordinate of multiplicity at least two. Partition any code \(\mathcal C\) into \(S\) words with precisely one heavy coordinate and \(T\) words with at least two. For every symbol \(i\), the monochromatic received word \(2e_i\) has at most \(L\) parents. Summing over the \(q\) such received words gives \(S+2T\le qL\). For each choice of heavy symbol, all other \(q-1\) coordinates of a singly-heavy word are zero or one; its heavy multiplicity is uniquely determined, hence there are exactly \(K=2^{q-1}\) singly-heavy words for each heavy symbol and \(S\le qK\). Consequently
\[
2|\mathcal C|=2S+2T\le qL+S\le qL+qK,
\]
which proves the stated bound.

**2. Baseline mixed-pair incidence and strict onset.** The complete family of \(qK\) singly-heavy words contains exactly \(E=(q+2)k\) parents for each mixed received pair \(e_i+e_j\), with \(i\ne j\). Indeed, heavy coordinate \(i\) and heavy coordinate \(j\) contribute \(2^{q-2}\) each, and each of the remaining \(q-2\) choices for the heavy coordinate contributes \(2^{q-3}\).

Suppose equality in the incidence bound holds. Set \(\delta=qK-S\ge0\). Let \(p\in\{0,1\}\) be the parity of \(q(L+K)\). Since \(2|\mathcal C|=qL+qK-p\) and \(S+2T\le qL\), necessarily \(\delta\le p\). For \(p=0\), this forces \(\delta=0\), so all singly-heavy words are present. Each remaining word has exactly two heavy coordinates, and the \(q\) monochromatic output lists are saturated. Thus there are \(q(L-K)/2\) remaining words, each contributing at least one mixed-pair parent incidence, while the total mixed-pair headroom is \(\binom q2(L-E)\). Hence
\[
\frac{q(L-K)}2\le\binom q2(L-E),
\quad\text{equivalently}\quad L\ge L_0.
\]
If \(q\) is even, \(p=0\) for every \(L\), proving the even-alphabet threshold. If \(q\) is odd, \(p=0\) when \(L\) is even, ruling out all even \(L<L_0\).

For odd \(q\) and odd \(L\), \(p=1\), so \(\delta\) is zero or one. A single omitted singly-heavy word contributes to at most \(\binom q2\) mixed receive types. Equality would require
\[
\left\lfloor\frac{q(L-K)}2\right\rfloor+\delta
\le \binom q2(L-E+\delta).
\]
For \(L=L_0-1\), the inequality is impossible if \(\delta=0\), because left minus right is \(\binom q2-(q+1)/2>0\). For \(L=L_0-3\), it is impossible for \(\delta=1\), because left minus right is \(2\binom q2-(3q-1)/2>0\). Decreasing the odd \(L\) further strengthens both obstructions since \(q/2<\binom q2\). This proves nonattainment below \(L_0-1\). Cases with a negative displayed lower bound for the extra-word count are already excluded by \(\delta\le1\): each list would have fewer than \(K-1\) parents despite at least \(K-1\) mandatory singly-heavy parents.

**3. Construction above the onset.** Include every singly-heavy word. Write \(r=L-K\), which satisfies \(r\ge(q-1)k\). Choose a loopless multigraph on the \(q\) symbols having \(\lfloor qr/2\rfloor\) edges counted with multiplicity, all degrees at most \(r\), and edge multiplicity at most \(\lceil r/(q-1)\rceil\). Its existence follows constructively from standard round-robin factorizations: for even \(q\), cycle through the \(q-1\) one-factors of the complete graph; for odd \(q\), cycle through its \((q-1)/2\) Hamilton cycles, each contributing two degrees, and for odd \(r\) add an alternating matching on \(q-1\) vertices from the next cycle. The complete edge partition and degree statements are explicitly checked in the accompanying reproducibility program.

For each graph edge \(\{i,j\}\) of multiplicity \(m\), add \(m\) distinct multisets supported on exactly those two symbols, each with both multiplicities at least two. Such words exist whenever \(n-3\ge m\); the stated source-length condition ensures this. The monochromatic list at each symbol has size at most \(K+r=L\). Each mixed-pair list has baseline \(E\) and receives at most \(\lceil r/(q-1)\rceil\) additional parents. Since \(r\ge(q-1)k\),
\[
\left\lceil\frac r{q-1}\right\rceil\le r-(q-2)k=L-E.
\]
Thus every list is admissible and the number of codewords is
\(qK+\lfloor qr/2\rfloor=B_q(L)\).

**4. Odd-alphabet one-step-earlier construction.** For odd \(q\), put \(L=L_0-1\). Start with all singly-heavy words except the unique word whose heavy coordinate is symbol \(0\) and whose other \(q-1\) coordinates equal one. On the complete graph \(K_q\), place \(k\) copies of every edge and then remove one copy of each edge in a matching covering the \(q-1\) vertices other than symbol \(0\). For each remaining edge occurrence use a different supported-on-two-symbols word with both multiplicities at least two; the hypothesis \(n\ge 3+k\) permits this. The monochromatic list of symbol \(0\) has size \((K-1)+(q-1)k=L\), and each other monochromatic list has size \(K+(q-1)k-1=L\). The deleted singly-heavy word covered *all* mixed receive pairs, so every mixed list has size at most \((E-1)+k=L\). The codebook contains
\[
qK-1+\binom q2k-\frac{q-1}{2}=B_q(L_0-1)
\]
words, as required.

**5. Complete classification at \(L=L_0\).** Since \(qL_0+qK\) is even, equality in the first counting inequality forces \(S=qK\) and every remaining word to have exactly two heavy coordinates. The number of remaining words is \(\binom q2k\). There is precisely \(\binom q2k\) total mixed-pair list headroom over the full singly-heavy baseline; consequently every remaining word contributes to exactly one mixed receive pair. Its support therefore consists of precisely its two heavy coordinates. Each of the \(\binom q2\) distinct pairs must receive exactly \(k\) such words. For any fixed pair, exactly \(n-3\) available multisets have both multiplicities at least two, and choices across pairs are independent. This proves the classification and labeled count.

## Verification

The accompanying standard-library `checks/verification.py` constructs the codebooks, evaluates every one of the \(\binom{q+1}{2}\) received-two-symbol lists directly, verifies that every list has at most \(L\) parents, and compares the total code size to the proven upper bound. It checks both parity constructions and nearby list allowances for alphabet sizes \(4\) through \(8\). Its factorization routines were separately tested for alphabet sizes \(4\) through \(23\) and residual degrees through four full factorization layers. The optional SciPy-based `checks/finite_opt.py` independently solves the complete \(q=4,n=5\) finite integer program, obtaining optima \(39,41,44,45\) at allowances \(L=12,13,14,15\) respectively. These finite checks corroborate, but do not establish, the infinite proof.

## Relationship to prior work

Kreindel, Essayag, and Zabokritskiy study unordered multiset deletion codes and, in Section 4.3 of *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, prove a unique-decoding size formula for exactly two surviving symbols. For \(n\ge q+1\), that maximum unique-decoding codebook has size \(q\). That statement is the special case of list size one; it does not give the exact high-list capacities, parity thresholds, or optimizer enumeration here. Their subsequent paper on polynomial constructions and deletion-ball geometry likewise addresses correction and geometry rather than the present sharp list-decoding equality question. Earlier work by Kovačević and Tan introduces the multiset coding framework without determining these list-capacity thresholds.

## Limitations

The result does not give exact values for arbitrary \(L\) below the equality threshold, nor for source lengths smaller than \(q+1\). The lower bound on source length for attainment above the threshold is sufficient and is not asserted to be optimal at every large allowance. The optimizer enumeration concerns labeled alphabets and only the boundary \(L=L_0\). The result is a mathematical deduction and finite numerical verification; it is not an independent external validation or a formal-machine-checked proof. Unindexed equivalent list-decoding results may exist.

## References

1. Avraham Kreindel, Isaac Barouch Essayag, and Aryeh Lev Zabokritskiy (Yohananov), *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first public 2026-01-09; especially Section 4.3. https://arxiv.org/abs/2601.05636
2. Avraham Kreindel, Isaac Barouch Essayag, and Aryeh Lev Zabokritskiy (Yohananov), *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322. https://arxiv.org/abs/2603.18322
3. Vladimir Kovačević and Vincent Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837. https://arxiv.org/abs/1612.08837
