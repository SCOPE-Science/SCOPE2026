# Exact fourteen-component range and component densities for the inverse-cubic divisor sum

## Finding

For each positive integer \(n\), put
\[
F(n)=\sigma_{-3}(n)=\sum_{d\mid n}\frac{1}{d^3}.
\]
Let \(\mathcal R=\overline{\{F(n):n\ge1\}}\) be the closure in \(\mathbb R\), and let
\[
T=\zeta(3)\prod_{p\in\{2,3,5,7\}}(1-p^{-3})
=\prod_{p\ge11}(1-p^{-3})^{-1}.
\]
Then \(\mathcal R\) has **exactly fourteen connected components**, the pairwise disjoint closed intervals in the table. Every integer has its value in exactly one of them, and the natural density of integers in each interval exists and equals the displayed rational number.

| Component | Left endpoint | Right endpoint | Natural density |
|---:|---|---|---|
| 1 | \( 1 \) | \( 1T \) | \( 8/35 \) |
| 2 | \( 344/343 \) | \( 343/342T \) | \( 4/105 \) |
| 3 | \( 126/125 \) | \( 125/124T \) | \( 2/35 \) |
| 4 | \( 6192/6125 \) | \( 42875/42408T \) | \( 1/105 \) |
| 5 | \( 28/27 \) | \( 1029/988T \) | \( 2/15 \) |
| 6 | \( 392/375 \) | \( 128625/122512T \) | \( 1/30 \) |
| 7 | \( 9/8 \) | \( 9/8T \) | \( 4/35 \) |
| 8 | \( 387/343 \) | \( 343/304T \) | \( 2/105 \) |
| 9 | \( 567/500 \) | \( 1125/992T \) | \( 1/35 \) |
| 10 | \( 6966/6125 \) | \( 42875/37696T \) | \( 1/210 \) |
| 11 | \( 73/64 \) | \( 196/171T \) | \( 2/15 \) |
| 12 | \( 4599/4000 \) | \( 6125/5301T \) | \( 1/30 \) |
| 13 | \( 7/6 \) | \( 9261/7904T \) | \( 1/15 \) |
| 14 | \( 147/125 \) | \( 18375/15314T \) | \( 1/10 \) |

The fourteen densities sum exactly to \(1\). In particular, the complete range closure and its full component-frequency distribution are both determined without a cutoff in \(n\).

## Assumptions and scope

The primes \(2,3,5,7\) are the only exceptional small primes. For a prime \(p\) and exponent \(a\ge0\), define \(f_p(a)=\sum_{j=0}^a p^{-3j}\) and \(f_p(\infty)=(1-p^{-3})^{-1}\). The table's right endpoints mean the displayed rational multiplier times the exact infinite Euler product \(T\), not a rounded approximation. The count is for the **ordinary** generalized divisor function, whose prime-power factor is \(f_p(a)\), not the unitary function whose factor is \(1+p^{-3a}\).

A natural density is \(\lim_{X\to\infty}X^{-1}\#\{1\le n\le X:F(n)\text{ lies in the specified interval}\}\). There are no assertions about how quickly this limit is attained.

## Proof

**1. All primes from \(11\) onward form a full interval in closure.** For every prime \(p\ge11\), write \(T_{>p}=\prod_{q>p}(1-q^{-3})^{-1}\). We establish the strict inequality
\[
T_{>p}>1+p^{-3}.\tag{1}
\]
For \(p\ge29\), Nagura's prime-interval theorem gives three distinct primes \(q_i\) satisfying \((6/5)^{i-1}p<q_i<(6/5)^ip\), for \(i=1,2,3\); all three left endpoints are at least \(25\). Hence
\[
\sum_{q>p}q^{-3}\ge\sum_{i=1}^3q_i^{-3}
>p^{-3}\sum_{i=1}^3(5/6)^{3i}>p^{-3}.
\]
For \(p\in\{11,13,17,19,23\}\), the same strict final inequality follows by checking respectively the explicit larger-prime sets
\[
\begin{array}{c|c}
p&\text{selected primes}\hline
11&13,17,19\\
13&17,19,23,29\\
17&19,23,29\\
19&23,29,31\\
23&29,31,37
\end{array}
\]
using exact rational arithmetic. Since \(T_{>p}>1+\sum_{q>p}q^{-3}\) (strictness comes from the positive further Euler-product terms), inequality (1) follows.

For any prime \(p\ge11\), adjacent local factors obey
\[
\frac{f_p(a+1)}{f_p(a)}
=1+\frac{p^{-3(a+1)}}{f_p(a)}\le1+p^{-3}<T_{>p}.
\]
Thus the intervals \([f_p(a),f_p(a)T_{>p}]\), for \(a=0,1,\ldots\), overlap and collectively cover \([1,f_p(\infty)T_{>p}]\) (with the limiting endpoint). To justify the infinite-prime passage directly, take any target \(y\in[1,T]\); at the smallest remaining prime choose a finite exponent \(a\) with \(f_p(a)\le y\le f_p(a)T_{>p}\), or a limit \(a\to\infty\), and divide \(y\) by this local factor. Repeat for successive primes. The residual after prime \(p\) belongs to \([1,T_{>p}]\), tending to \(1\) as \(p\to\infty\), so finite truncations approximate the target. Every finite truncation is a value of \(F\) on an integer coprime to \(210\). Conversely such a value is between \(1\) and \(T\). Therefore
\[
\overline{\{F(n):\gcd(n,210)=1\}}=[1,T].\tag{2}
\]

**2. The first four primes give twenty-four exact intervals.** For \(p\in\{2,3,5,7\}\), the ratios \(f_p(a+1)/f_p(a)\) strictly decrease with \(a\), and exact rational comparison with the bounds on \(T\) in the verifier gives the transition thresholds \(A_2=2\) and \(A_3=A_5=A_7=1\):
\[
\frac{f_p(A_p)}{f_p(A_p-1)}>T,
\qquad
\frac{f_p(A_p+1)}{f_p(A_p)}<T.
\]
Consequently, the intervals \([f_p(a),Tf_p(a)]\) for all \(a\ge A_p\) overlap successively and their union in closure is \([f_p(A_p),Tf_p(\infty)]\). Earlier exponents are separate choices. Define, for each prime, options \(a=0,\ldots,A_p-1\) with factor range \([f_p(a),f_p(a)]\), and option \(a\ge A_p\) with factor range \([f_p(A_p),f_p(\infty)]\). Multiplication by the prime tail in (2) gives, exactly, the union of \(3\cdot2\cdot2\cdot2=24\) closed intervals \([L,TU]\), where each \(L\) and \(U\) is a product of the chosen rational lower and upper factors. No exponent choices are omitted; endpoints with \(a\to\infty\) are interpreted in closure.

**3. Exact merging of these twenty-four intervals.** Sort the candidate intervals by increasing rational lower endpoint. Compute rigorous rational bounds \(T_-<T<T_+\) using
\[
\sum_{j=1}^{N}j^{-3}+\frac{1}{2(N+1)^2}
<\zeta(3)<
\sum_{j=1}^{N}j^{-3}+\frac{1}{2N^2},\qquad N=200.
\]
After multiplying by \(\prod_{p\in\{2,3,5,7\}}(1-p^{-3})\), these bound \(T\) exactly. For each new interval \([L,TU]\), a strict gap is established if \(L>T_+U_{\mathrm{previous}}\); a strict overlap is established if \(L<T_-U_{\mathrm{previous}}\). The bundled standalone `verify.py` computes and checks every one of the twenty-three comparisons as exact rational inequalities: there are thirteen gaps and ten overlaps, producing the fourteen disjoint intervals in the table. The same certificate checks all table endpoints, thresholds, and that the final upper endpoint equals \(\zeta(3)\). These are finite rational certificates, not floating-point estimates.

**4. Exact densities.** For a fixed prime \(p\), the integers with \(\nu_p(n)=a\) have natural density \((p-1)/p^{a+1}\); those with \(\nu_p(n)\ge A_p\) have density \(p^{-A_p}\). The four conditions are jointly independent by the Chinese remainder theorem and elementary divisibility counting. Therefore the density associated with each of the twenty-four head options is the product of its four rational weights. The disjoint components correspond to disjoint unions of these options, since every possible tail value in (2) remains inside the same component. Summing the weights within each merged component gives precisely the fourteen rational densities in the table, and the certificate verifies that their sum is \(1\). This completes the proof.

## Verification

`verify.py` is a standard-library-only Python 3 script computing every relevant comparison with `fractions.Fraction`. Run `python3 verify.py`. Its expected principal output is `CERTIFICATE_OK prime_head_options 24 connected_components 14 gaps 13 overlaps 10 total_density 1`, followed by all fourteen endpoint/density rows. Besides the interval merges, it checks the five finite-prime tail inequalities, the three-term rational Nagura consequence, and each small-prime exponent threshold. The analytic inputs are the classical Nagura theorem and the proved tail-filling argument; no finite computation is used to infer a general claim from examples.

## Relationship to prior work

Defant [1] investigates density and topology of ranges of generalized divisor functions. Sanna [2, Lemmas 2.3–2.5 and the recursive algorithm in Sections 3–4] supplies a general method for component intervals and frequencies and works out an explicit example for exponent \(2\). The theorem above specializes that general framework at the natural next cubic exponent and supplies a complete, explicitly certified new-looking exact component and density table; **the generic algorithm and tail-overlap method are not claimed as new**. Zubrilina [3] studies general connected-component bounds, not the displayed cubic table. Nagura's theorem [4] is used only as a published prime-gap input. An equally strong, unindexed exact table may exist, so independent priority review remains appropriate.

## Limitations

The theorem concerns exponent exactly \(3\), ordinary divisor sums, their topological range closure, and the natural densities of their fourteen components. It does not classify other exponents, claim an effective convergence rate for the densities, or establish a new prime-gap result. The machine certificate validates the finite rational part; it relies on the separate mathematical argument and the established prime-interval theorem for the infinite part. This is a self-reviewed mathematical claim, not an independently audited or published result.

## References

[1] Colin Defant, On the Density of Ranges of Generalized Divisor Functions, arXiv:1506.05432 (first posted 2015-06-17).

[2] Carlo Sanna, On the closure of the image of the generalized divisor function, arXiv:1507.08091 (first posted 2015-07-29).

[3] Nina Zubrilina, On the Number of Connected Components of Ranges of Divisor Functions, arXiv:1711.02871 (first posted 2017-11-08).

[4] Jitsuro Nagura, On The Interval Containing At Least One Prime Number, Proceedings of the Japan Academy 28 (1952), DOI:10.3792/pja/1195570997.
