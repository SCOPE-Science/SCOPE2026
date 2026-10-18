# Extremal modular digit-sum gaps in every integer base: exact lengths, starting points, and densities

## Finding

Fix an integer base \(b\ge2\), put \(m=b+1\), and let \(s_b(n)\) be the sum of the ordinary base-\(b\) digits of the nonnegative integer \(n\), including \(s_b(0)=0\). A positive interval \([a,a+L-1]\cap\mathbb Z\) is **admissible** if \(m\nmid s_b(n)\) for every integer in it. Let \(L_b\) be the greatest possible admissible length. Then

\[
L_b=\begin{cases}
3b-2,&b\text{ odd},\\
4b-2,&b\text{ even}.
\end{cases}
\]

All intervals attaining this maximum start at \(a=b(q-1)+1\) for a unique integer \(q\ge1\). Their complete classification is as follows.

* **Odd \(b\).** Set \(k=(b+1)/2\). The integer \(q\) is admissible exactly when one of the following disjoint cases holds:
  1. \(q\bmod b\in\{1,\ldots,b-2\}\) and \(s_b(q)\equiv1\pmod{b+1}\);
  2. \(q=b^t h\), where \(t\) is a positive multiple of \(k\), \(h\ge1\), \(b\nmid h\), and \(s_b(h)\equiv1\pmod{b+1}\);
  3. \(q=b^t h-1\), where \(t\) is a positive multiple of \(k\), \(h\ge1\), \(b\nmid h\), and \(s_b(h-1)\equiv1\pmod{b+1}\).
* **Even \(b\).** The integer \(q\) is admissible exactly when \(q=b^t h-1\) with \(h\ge1\), \(b\nmid h\), \(t\ge1\), \(t\equiv b/2\pmod{b+1}\), and \(s_b(h-1)\equiv0\pmod{b+1}\).

Writing \(E_b(X)\) for the number of starting points \(a\le X\) of maximal admissible intervals, the natural density exists and equals

\[
\lim_{X\to\infty}\frac{E_b(X)}X
=\begin{cases}
\displaystyle\frac{b-2+2(b-1)/(b^{(b+1)/2}-1)}{(b+1)b^2},&b\text{ odd},\\[8pt]
\displaystyle\frac{(b-1)b^{-b/2}}{(b+1)b^2(1-b^{-(b+1)})},&b\text{ even}.
\end{cases}
\]

Both densities are strictly positive. In particular, the previously known decimal modulus-\(11\) maximum \(38\) is recovered, and its maximal-run starting points have density exactly \(10000/122222222221\).

## Assumptions and scope

The theorem concerns the ordinary nonnegative positional digit sum in integer bases \(b\ge2\), and the **specific natural modulus** one greater than the base, \(m=b+1\). The interval endpoints are positive integers and have no upper bound. Densities count *starting integers*, not runs weighted by length. No statement for a free, unrelated modulus is made.

## Proof

**1. A block omits precisely one digit-sum residue.** For every \(q\ge0\) and \(0\le r<b\),
\[
s_b(bq+r)=s_b(q)+r.
\]
The \(b=m-1\) digit sums in the block \(I_q=[bq,bq+b-1]\) are consecutive. Modulo \(m\), the block omits exactly one residue. It contains no zero residue if and only if \(s_b(q)\equiv1\pmod m\); call such a block *good*. Every other block contains exactly one multiple of \(m\) among its digit sums.

**2. Carry differences and sharp universal upper bounds.** Let \(t\ge0\) be the number of trailing base-\(b\) digits equal to \(b-1\) in \(q\). Then
\[
s_b(q+1)-s_b(q)=1-(b-1)t\equiv1+2t\pmod m.
\]
For odd \(b\), the modulus \(m\) is even, so \(1+2t\not\equiv0\pmod m\). Hence there are no two consecutive good blocks. For even \(b\), there are no three consecutive good blocks: of the two transitions between three consecutive indices, at least one has \(t=0\), causing a digit-sum increase by exactly \(1\). An interval of length \(3b-1\) contains at least two complete consecutive blocks \(I_q\); one of length \(4b-1\) contains at least three. Therefore \(L_b\le3b-2\) for odd \(b\) and \(L_b\le4b-2\) for even \(b\).

For odd \(b\), the interval \([1,3b-2]\) is admissible: its digit sums, in its three successive partial/full blocks, lie respectively in \(\{1,\dots,b-1\}\), \(\{1,\dots,b\}\), and \(\{2,\dots,b\}\). For even \(b\), take \(q=b^{b/2}-1\). Since
\[
s_b(q)=(b-1)b/2\equiv1\pmod m,
\qquad s_b(q+1)=1,
\]
both \(I_q\) and \(I_{q+1}\) are good. Moreover \(s_b(q-1)\equiv0\) and \(s_b(q+2)\equiv2\pmod m\). Thus
\[
[b(q-1)+1,\ b(q+2)+b-2]
\]
is an admissible interval of length \(4b-2\). Both upper bounds are attained.

**3. Every extremal starting point.** A maximal interval of length \(3b-2\) (odd \(b\)) or \(4b-2\) (even \(b\)) must begin at residue \(1\pmod b\). Indeed, beginning at residue \(0\) or at any residue \(2,\dots,b-1\) would force respectively two or three consecutive full good blocks, contradicting Step 2. Write its beginning as \(a=b(q-1)+1\). The outer partial blocks then each contribute \(b-1\) points. Since neither can contain a forbidden digit sum, their initial digit-sum residues must be \(0\) (left block \(I_{q-1}\)) and \(2\) (right block), respectively.

For odd \(b\), the complete middle block is \(I_q\); the exact necessary and sufficient conditions are
\[
s_b(q-1)\equiv0,\quad s_b(q)\equiv1,\quad
s_b(q+1)\equiv2\pmod m.
\]
If \(q\bmod b\in\{1,\dots,b-2\}\), both relevant increments are ordinary, giving case 1. If \(q=b^t h\) with \(t\ge1\), \(b\nmid h\), then the incoming carry satisfies \(s_b(q)-s_b(q-1)\equiv1+2t\). It is congruent to \(1\) precisely when \(2t\equiv0\pmod m\), equivalent to \(k\mid t\); the outgoing increment is ordinary, giving case 2. If \(q=b^t h-1\) with \(t\ge1\), \(b\nmid h\), the incoming increment is ordinary and the outgoing carry must again satisfy \(2t\equiv0\pmod m\); then \(s_b(q)=(b-1)t+s_b(h-1)\equiv s_b(h-1)\pmod m\), giving case 3.

For even \(b\), the two complete middle blocks are \(I_q,I_{q+1}\). Consecutive goodness forces a carry from \(q\) to \(q+1\): \(q=b^t h-1\) with \(b\nmid h\), \(t\ge1\), and
\[
1+2t\equiv0\pmod m
\iff t\equiv b/2\pmod m.
\]
Then \(s_b(q)=(b-1)t+s_b(h-1)\equiv1+s_b(h-1)\pmod m\), so goodness is equivalent to \(s_b(h-1)\equiv0\pmod m\). The outside partial blocks are automatically admissible since the adjacent digit-sum residues are \(0\) and \(2\). This proves all the classifications.

**4. Density of all extremizers.** We use a standard elementary digit-convolution fact: for fixed \(b\ge2\), \(m\ge2\), and any specified set of units digits, the residues of \(s_b(n)\pmod m\) are asymptotically uniform when the unrestricted higher digits increase. To prove it, write \(\zeta=e^{2\pi i/m}\). For every nontrivial character \(\zeta^j\), the normalized sum \(b^{-1}\sum_{r=0}^{b-1}\zeta^{jr}\) has absolute value strictly less than \(1\), since digits \(0\) and \(1\) are distinct phases. On digit boxes with \(j\) unrestricted positions, the corresponding Fourier coefficient decays geometrically. Partition arbitrary long integer intervals into complete digit boxes plus a bounded remainder, then let the box length grow. This gives the asserted limiting uniformity even after fixing the last digit within a proper nonempty set.

For odd \(b\), set \(k=m/2\). Case 1 has proportion \((b-2)/(bm)\) of all possible \(q\). In each of cases 2 and 3, requiring exactly \(t\) trailing zeros or maximal digits has base-density \((b-1)/b^{t+1}\), and the independent higher-digit-sum condition contributes a factor \(1/m\). Summing over positive multiples \(t\) of \(k\), the combined proportion is
\[
\frac{b-2}{bm}+\frac{2(b-1)}{mb(b^k-1)}.
\]
For even \(b\), summing \(t=b/2+j(b+1)\) over \(j\ge0\) gives proportion
\[
\frac{b-1}{mb}\frac{b^{-b/2}}{1-b^{-m}}
\]
of qualifying \(q\). Truncating the geometric sums incurs a tail of density at most \(b^{-T}\) for valuations at least \(T\), so limits and infinite sums may be interchanged. Since each \(q\) gives one starting point \(a=b(q-1)+1\), each preceding density is divided by \(b\) for starting points among all positive integers. The displayed formulas follow.

## Verification

A self-contained Python verifier in `verify.py` computes digit sums independently, enumerates every possible maximal-length starting point in a finite interval for bases \(2\) through \(12\), compares it with the full stated classification, and checks that no interval of one larger length occurs there. It checks \(2,492,834\) starting points in all. It also constructs and directly checks a provably maximal interval in each base \(2\) through \(30\), including endpoint behavior, without treating these finite tests as a proof of the infinite result. Execute `python3 verify.py` using Python 3 standard library only.

Numerical illustrations: in base \(3\), the maximum is \(7\), and extremal starts have density \(1/24\). In base \(4\), the maximum is \(14\), and the density is \(4/1705\). In base \(10\), the maximum is \(38\), the earliest extremal start is \(999981\), and the density is \(10000/122222222221\); the length and earliest start are already known in the cited decimal source.

## Relationship to prior work

The 2023 University of Waterloo Problem of the Month explicitly considers consecutive decimal integers whose digit sums avoid a prescribed modulus. Its published solution proves the decimal cases \(m=2,7,9,11\), including the sharp \(m=11\) bound \(38\) and earliest starting point \(999981\). The July 2022 Mathematics Stack Exchange discussion proves the separate decimal \(m=8\) maximum \(14\). Those decimal classifications are not claimed as new. Neither inspected source gives a parity-dichotomous formula for *all bases* at modulus \(b+1\), a complete classification of all extremal starts, or their exact asymptotic densities. The present proof makes the carry-congruence obstruction and sparse extremal-frequency calculation explicit. Ordinary digit-sum equidistribution is used as an elementary input and is not claimed as novel.

## Limitations

The theorem is restricted to modulus \(b+1\); it does not solve arbitrary-modulus digit-sum avoidance. For each base, the formula for the density is a limiting frequency, not an exact finite-count expression for every cutoff. The cited sources and searched records may not exhaust independently circulating or unindexed treatments of arbitrary bases.

## References

1. University of Waterloo Centre for Education in Mathematics and Computing, *Problem of the Month, October 2023, Problem 1*, including published solution, https://cemc.uwaterloo.ca/sites/default/files/documents/2024/Combined-POTM-2023-24.html .
2. Mathematics Stack Exchange, *What is the length of the longest sequence of consecutive natural numbers, none of which has a digit sum divisible by 8? What about other divisors?*, question posted July 16, 2022, answer posted July 17, 2022, https://math.stackexchange.com/questions/4494103/what-is-the-length-of-the-longest-sequence-of-consecutive-natural-numbers-none .
