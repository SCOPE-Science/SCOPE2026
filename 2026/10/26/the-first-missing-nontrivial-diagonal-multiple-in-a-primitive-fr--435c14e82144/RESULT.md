# The first missing nontrivial diagonal multiple in a primitive Frobenius problem

## Finding

**Theorem.** Let \(a,b\ge 2\) be coprime integers. Call an integer \(n\) *primitively representable* when \(n=ax+by\) for some \(x,y\in\mathbb Z_{\ge0}\) with \(\gcd(x,y)=1\). Then every diagonal multiple \(mab\) with \(2\le m\le15\) is primitively representable, regardless of \(a,b\). Moreover,

\[
16ab\text{ is not primitively representable}
\quad\Longleftrightarrow\quad
(55\mid a\text{ and }273\mid b)\text{ or }(273\mid a\text{ and }55\mid b).
\]

Thus \(16\) is the first nontrivial diagonal multiplier for which such failure can occur, and its failure locus is completely described by two oriented divisibility patterns. For instance, \(a=55\), \(b=273\) yields a gap at \(16ab=240240\), so the primitive restricted Frobenius number obeys \(g(55,273)\ge240240\). The multiplier \(m=1\) is excluded from the universal positive assertion: for \(a,b\ge2\), the sole two representations of \(ab\) are \((x,y)=(b,0)\) and \((0,a)\), neither primitive.

## Assumptions and scope

All integers \(a,b\ge2\) are allowed subject only to \(\gcd(a,b)=1\). The coefficient variables are nonnegative integers. The claimed first-failure result concerns **exact diagonal multiples** \(mab\), not all integers between them, and does not determine the full primitive Frobenius number \(g(a,b)\). The source first made public on October 12, 2026 has primary MSC 11N99.

## Proof

**Reduction.** If \(ax+by=mab\), reducing modulo \(b\) and \(a\), respectively, shows \(x=bj\) and \(y=a(m-j)\) for a unique integer \(0\le j\le m\). For \(m\ge2\), the endpoints \(j=0,m\) are nonprimitive since \(a,b\ge2\). Consequently, primitive representability is equivalent to the existence of an integer \(1\le j\le m-1\) with

\[
\gcd(bj,a(m-j))=1. \tag{1}
\]

For a prime \(p\), coprimality of \(a,b\) implies the following exact obstruction test at an interior index: if \(p\mid a\), then \(p\) divides both coordinates precisely when \(p\mid j\); if \(p\mid b\), it does so precisely when \(p\mid(m-j)\); if \(p\nmid ab\), it does so precisely when \(p\mid\gcd(j,m-j)\). These are all possibilities.

**Multipliers from prime powers.** If \(m-1\) is \(1\) or a power of one prime \(p\), the choices \(j=1\) and \(j=m-1\) give gcds \(\gcd(b,m-1)\) and \(\gcd(a,m-1)\). They cannot both exceed one because \(\gcd(a,b)=1\). This settles
\[
 m\in\{2,3,4,5,6,8,9,10,12,14\}. \tag{2}
\]

**Four remaining multipliers below sixteen.** For \(m=7\) or \(m=15\), write \(m-1=2p\), with \(p=3\) or \(7\), respectively. Unless \(j=1\) or \(j=m-1\) already works, the two prime divisors \(2,p\) must occur in opposite members of \(a,b\). If \(2\mid a\), \(p\mid b\), select \(j=p\); then the coordinates \((pb,(p+1)a)\) are coprime because \(p+1\) is a power of two, \(b\) is odd, \(p\nmid a\), and \(\gcd(a,b)=1\). If the divisibilities are reversed, take \(j=p+1\), the reflected solution.

For \(m=11\), the initial two choices, if both obstructed, force either \(2\mid a,5\mid b\) or the reversed pattern. In the first pattern \(b\) is odd and \(5\nmid a\). If \(3\nmid b\), choose \(j=5\): \(\gcd(5b,6a)=1\). If \(3\mid b\), choose \(j=3\): \(\gcd(3b,8a)=1\). For the reversed pattern, interchange \(a,b\) and replace \(j\) by \(11-j\). For \(m=13\), failure of the two initial choices forces either \(2\mid a,3\mid b\) or the reverse. In the first case \(j=9\) works because \(\gcd(9b,4a)=1\); in the reverse case reflect it to \(j=4\). This proves every case through \(m=15\).

**The sharp obstruction at sixteen.** Every even \(j\) is excluded from (1), since both \(j\) and \(16-j\) are even. To exclude both \(j=1\) and \(j=15\), the primes \(3\) and \(5\) must divide opposite members of \(a,b\) (the two initial gcds are \(\gcd(b,15)\) and \(\gcd(a,15)\)). By symmetry suppose \(5\mid a\) and \(3\mid b\). Then \(j=3\) can fail only if \(13\mid b\), since \(3\nmid a\); \(j=9\) can fail only if \(7\mid b\), since \(3\nmid a\); and \(j=11\) can fail only if \(11\mid a\), since \(5\nmid b\). Thus nonrepresentability forces \(55\mid a\) and \(273\mid b\).

Conversely suppose these divisibilities hold. The odd interior indices \(j=1,3,5,7,9,11,13,15\) are excluded by the prime obstructions \(3,13,5,3,7,11,3,5\), in that order. Together with the even-index obstruction, this excludes every interior index. Interchanging \(a,b\) yields the second pattern. The necessary and sufficient classification is proved. \(\square\)

## Verification

The accompanying standalone Python 3 checker, `verify.py`, implements the exact prime-local condition independently of the displayed gcd test. It exhaustively checks all \(3^6=729\) assignments of the six primes \(2,3,5,7,11,13\) to the mutually exclusive categories dividing \(a\), dividing \(b\), or dividing neither, and tests all multipliers \(2\le m\le16\). This finite check is exhaustive for the prime-state model because a common prime divisor of the two candidate coordinates must divide \(j\) or \(m-j\), each at most \(15\). It also checks 13,416 coprime pairs in the box \(2\le a,b\le150\) using integer gcds and specific larger witnesses including \((55,273)\). The executable's successful result is `VERIFY_OK state_assignments=729 coprime_pairs=13416 diagonal_range=2..16`. The universal result follows from the proof, not from a bounded enumeration.

To replay, run `python3 verify.py` in the same directory as this document; the checker uses Python's standard library only.

## Relationship to prior work

Jaffe (2026), Theorem 2.1, identifies primitive representations with denominator occurrences in a Stern/Farey array, and Sections 3–7 study existence, exact special cases, bounds, and open questions for the corresponding primitive Frobenius number. The present statement isolates a different invariant: the first nontrivial diagonal multiple of the product of the generators that can fail to have a primitive coefficient pair, together with the complete parameter locus at that threshold. The 2026 article's general existence theorem does not specify this finite threshold, and its tabulated examples only cover generators up to 200, below one member of the minimal exceptional pair.

A related CRT-offset lower-bound method yields nonprimitive numbers of the form \(kab-ac-bd\) under size hypotheses; those shifted gaps do not classify the unshifted values \(mab\) uniformly over all coprime generator pairs. A different fixed-generator asymptotic lower bound for the primitive Frobenius number likewise does not decide which exact diagonal multiples fail. Tripathi's classical Frobenius work concerns unrestricted nonnegative coefficients, so it does not cover the primitive gcd constraint. Searches may miss an equivalent older formulation; originality is subject to external review.

## Limitations

The classification only covers multipliers through \(16\) and assumes both generators at least \(2\) and coprime. It does not classify missing non-diagonal integers, all later diagonal multipliers, or the exact primitive Frobenius number. The prime-state computation is finite and independent of the proof but not a substitute for it. The possibility of unstated implicit coverage in broader number-theoretic literature cannot be completely excluded; no independent mathematical audit has been performed.

## References

1. Grace Natalie Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1, first posted 2026-10-12. https://arxiv.org/html/2610.17267v1
2. Amitabha Tripathi, *A note on the Frobenius and the Sylvester numbers*, Notes on Number Theory and Discrete Mathematics 24 (2018), 71–73. DOI: 10.7546/nntdm.2018.24.2.71-73.
