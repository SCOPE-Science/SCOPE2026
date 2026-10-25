# A five-family classification of uniform-digit fixed points of elated maps

## Finding

For an integer base \(b\ge2\), let \(E_b\) send a positive integer to its leading base-\(b\) digit times the sum of squares of all its base-\(b\) digits. Call a positive integer *uniform-digit* if every nonzero digit in its base-\(b\) expansion has the same value. The integer \(1\) is always fixed. Every *nontrivial* uniform-digit fixed point \(N>1\), over all bases, belongs to exactly one of the following five digit-pattern families, with digit \(2\le a<b\):

| Base-\(b\) pattern | Necessary and sufficient Diophantine identity |
|---|---|
| \((a0)_b\) | \(b=a^2\) |
| \((aa)_b\) | \(b+1=2a^2\) |
| \((a0a)_b\) | \(b^2+1=2a^2\) |
| \((aa0)_b\) | \(b^2+b=2a^2\) |
| \((aaa)_b\) | \(b^2+b+1=3a^2\) |

There are no other nontrivial uniform-digit fixed points of any length. The last three families are Pell-type: respectively \(b^2-2a^2=-1\), \((2b+1)^2-8a^2=1\), and \((2b+1)^2-12a^2=-3\). The first admissible bases and digits are \((7,5)\), \((8,6)\), and \((22,13)\), and each Pell-type family is infinite. In the last family, all solutions with \(b\ge2\) arise by starting from \((x,a)=(3,1)\), iterating \((x,a)\mapsto(7x+24a,2x+7a)\) at least once, and putting \(b=(x-1)/2\).

Writing \(B(X)\) for the number of integer bases \(2\le b\le X\) admitting at least one such nontrivial fixed point, one has the sharp-order counting law
\[
B(X)=\left(1+\frac1{\sqrt2}\right)\sqrt X+O(\log(X+2)).
\]
Among even bases, the corresponding count is \(\frac12\sqrt X+O(\log(X+2))\). In particular, infinitely many even nonsquare bases (including \(8\), \(22\), \(288\), and \(4366\)) have nontrivial fixed points, so not every positive integer is elated in those bases.

## Assumptions and scope

All bases are integers \(b\ge2\); all integers and digits are positive where explicitly stipulated, except that zero digits may occur. The digit pattern \((a0a)_b\), for example, means the integer \(ab^2+a\). A uniform-digit number may contain any number of zero digits, but its *positive* digits are all equal. The theorem classifies only fixed points with this property, not other fixed points or cycles. The asymptotics count **bases** once each, not fixed points with multiplicity. The motivating first public preprint appeared on 2024-09-15 (arXiv:2409.09863).

## Proof

**Digit-length restriction.** Let a uniform-digit integer have leading digit \(a\) in position \(k\), exactly \(r\ge1\) nonzero digits, and all these digits equal to \(a\). Then \(N\ge ab^k\), \(r\le k+1\), and \(E_b(N)=ra^3\le (k+1)a(b-1)^2\). For every \(b\ge2\), \(b^3>4(b-1)^2\); moreover \(b^k/(k+1)\) increases with \(k\ge3\). Thus if \(k\ge3\), then \(b^k>(k+1)(b-1)^2\) and \(E_b(N)<N\). The leading position of a fixed point is therefore at most two. A one-digit fixed point satisfies \(a=a^3\), giving only \(a=1\); also, a single nonzero digit in position two would force \(b^2=a^2\), forbidden by \(a<b\).

**Exhaustion and converse.** For a remaining nontrivial uniform-digit fixed point with \(r\) nonzero digits in positions \(I\subseteq\{0,1,2\}\), the exact equation is
\[
N=a\sum_{i\in I}b^i=E_b(N)=ra^3,
\qquad \sum_{i\in I}b^i=ra^2.
\]
Taking \(\max I=1\) or \(2\) gives exactly the five stated patterns and identities. Conversely, each identity with \(2\le a<b\) makes its displayed digit pattern an actual base-\(b\) expansion fixed by \(E_b\). Each listed positive Diophantine solution with \(b\ge2\) automatically satisfies \(a<b\): this is obvious for \(b=a^2\) and \(b=2a^2-1\); for each quadratic-in-\(b\) family, the defining identity yields \(a^2<b^2\) whenever \(b\) is at least its first admissible value.

**Pell families.** For \((a0a)_b\), the classical negative Pell solutions \(b+a\sqrt2=(1+\sqrt2)^{2m+1}\) give \((b,a)=(1,1),(7,5),(41,29),\dots\). For \((aa0)_b\), the standard positive Pell solutions \(x+y\sqrt2=(3+2\sqrt2)^m\), with \(x=2b+1\) and \(y=2a\), give \((b,a)=(1,1),(8,6),(49,35),(288,204),\dots\). For \((aaa)_b\), set \(x=2b+1\). The norm equation is \(x^2-12a^2=-3\). The positive unit \(7+2\sqrt{12}\) sends a solution to the next one by
\[
(x,a)\longmapsto(7x+24a,\;2x+7a).
\]
It starts with \((3,1)\) and then \((45,13),(627,181),(8733,2521),\dots\). For completeness, every positive solution with \(a\ge4\) descends under the inverse map \((x,a)\mapsto(7x-24a,7a-2x)\): the inequalities \(24/7<x/a<7/2\) make both coordinates positive, and \(x/a>3\) makes the second coordinate smaller than \(a\). The ratios follow from \(x^2=12a^2-3\) for \(a\ge4\). Neither \(a=2\) nor \(a=3\) gives an integral \(x\); \(a=1\) gives \(x=3\). Thus the stated recurrence exhausts this family. In each family the fundamental-unit recurrences grow exponentially, so the number of admissible bases at most \(X\) is \(O(\log(X+2))\).

**Counting distinct bases.** The first two families occur respectively at \(b=a^2\) and \(b=2a^2-1\), both for integers \(a\ge2\). They contribute \(\sqrt X+O(1)\) and \(\sqrt{X/2}+O(1)\) distinct bases. Their intersection obeys \(q^2-2a^2=-1\), a negative Pell equation with only \(O(\log(X+2))\) solutions through \(X\). The other three families together also contribute at most \(O(\log(X+2))\) bases. Inclusion-exclusion gives the displayed \(B(X)\). For even bases, the second family is odd, the negative-Pell family has odd \(b\), and the even squares in the first family contribute \(\frac12\sqrt X+O(1)\); the remaining families contribute only \(O(\log(X+2))\). The recurrences in the last two Pell families yield infinitely many even nonsquare bases, proving the final assertion.

## Verification

The standalone `check_uniform.py` independently builds all allowed equal-positive-digit patterns up to three digits, evaluates \(E_b\) directly, and compares them with the five Diophantine tests for every base \(2\le b\le1000\). It also checks exact recurrence witnesses for the generalized Pell family. Running `python3 check_uniform.py` prints `VERIFIED: classification all equal-positive-digit fixed points, bases 2..1000`. This is a finite sanity check; the proof above establishes the infinite claim.

## Relationship to prior work

Fox, Fox, Grundman, Lynn, Namoijam, and Vanderschoot introduced elated numbers (first public preprint 2024-09-15). Their full paper gives a descent bound and complete finite orbit tables for bases \(2\) through \(10\), not this unrestricted-base uniform-digit classification or its base-counting asymptotic. Their table includes the already-known examples \((22)_7\), \((505)_7\), and \((660)_8\); these **individual examples are not claimed as new**. OEIS A377086 and A377087 tabulate total fixed-point and cycle counts for finite ranges of bases and do not imply the present structural characterization. OEIS A001108 and classical Pell literature give the square-triangular index sequence used here; the Pell parametrizations themselves are classical, not new. The contribution being assessed is the joint exhaustive classification for the elated map together with its base-counting law.

## Limitations

This does not characterize arbitrary digits, all elated cycles, or answer whether the *total* number of cycles is unbounded. It does not settle whether some even base outside these families has every positive integer elated. A previously unindexed structural observation could overlap this relatively elementary argument.

## References

- N. B. Fox, N. H. Fox, H. G. Grundman, R. Lynn, C. Namoijam, and M. Vanderschoot, *Elated Numbers*, arXiv:2409.09863 (first public version 2024-09-15); later open-access journal version: *La Matematica* 5 (2026), article 38, DOI 10.1007/s44007-025-00185-7.
- OEIS A377086, *Number of fixed points under the elated map by base*, https://oeis.org/A377086.
- OEIS A377087, *Number of nontrivial cycles under the elated map by base*, https://oeis.org/A377087.
- OEIS A001108, *Indices of triangular numbers that are squares*, https://oeis.org/A001108; see also Wolfram MathWorld, *Triangular Number*, discussion of square triangular numbers.
