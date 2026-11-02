# Parity rigidity and unique coprime matchings of divisor sets

## Finding
For a positive integer \(n\), let \(D(n)\) be the set of its positive divisors and let \(N=\tau(n)=|D(n)|\). Given a set \(S\) of \(N\) **distinct positive integers**, define
\[
C_n(S)=\#\{f:D(n)\xrightarrow{\sim}S:\gcd(d,f(d))=1\ \text{for every }d\mid n\}.
\]
Let \(P(n)=\{p:p\text{ is prime and }p\mid n\}\), and for \(s>0\) put \(\operatorname{supp}_n(s)=\{p\in P(n):p\mid s\}\).

**General parity and uniqueness theorem.** For every \(n\ge1\) and every such \(S\), exactly one of the following holds:

* \(n\) is squarefree and the \(N\) supports \(\operatorname{supp}_n(s)\) are pairwise distinct. In this case \(C_n(S)=1\).
* Otherwise \(C_n(S)\) is an even nonnegative integer.

Thus \(C_n(S)\) cannot be an odd integer greater than one.

**Arithmetic-progression classification.** For arbitrary positive integers \(a,b\), set
\[
\mathcal P_{n;a,b}=\{a+bt:0\le t<\tau(n)\}.
\]
The count \(C_n(\mathcal P_{n;a,b})\) is one if and only if one of these disjoint conditions holds:

1. \(n=1\);
2. \(n=p\) is prime and exactly one of \(a\) and \(a+b\) is divisible by \(p\);
3. \(n=6\), \(a\equiv0\pmod3\), and \(\gcd(b,6)=1\).

In every other case the count is even (possibly zero). No coprimality assumption on \(a,b\) is imposed. For the original initial interval \(\{1,2,\ldots,\tau(n)\}\), unique matchability occurs **only at \(n=1,2\)**.

## Assumptions and scope
All sets are finite, and \(S\) is a set rather than a multiset. Numbers \(n,a,b\) are strictly positive, with \(b\ge1\) ensuring distinct progression terms. A coprime matching is a bijection, counted once for each assignment of partners; no identifications by symmetry are made. The value \(n=1\) is included, with an empty prime-support set. Neither the existence of a matching in all cases nor the exact positive even count is asserted.

## Proof
**1. Identical support profiles force even parity.** The bipartite coprimality graph has left vertices \(d\mid n\), right vertices \(s\in S\), with an edge if and only if their prime supports within \(P(n)\) are disjoint. If \(n\) is not squarefree, for some prime \(p\), the two different divisors \(p,p^2\) have identical neighborhoods. Swapping their images in any matching is a fixed-point-free involution on the finite set of matchings: the images are necessarily distinct and the transposition preserves allowed edges. Therefore \(C_n(S)\) is even. If \(n\) is squarefree but two different elements \(s_1,s_2\in S\) have the same support, they have identical neighborhoods; swapping their preimages likewise gives a fixed-point-free involution and an even count.

**2. All support patterns force a single matching.** Suppose \(n\) is squarefree and the right supports are distinct. Write \(r=|P(n)|\), so \(N=2^r\); the right supports must therefore be precisely all subsets \(T\subseteq P(n)\). Likewise the left divisors are in bijection with the subsets \(U\subseteq P(n)\). Match the right vertex of support \(T\) to the left divisor with support \(P(n)\setminus T\); these supports are disjoint, giving a perfect matching. To prove uniqueness, order right supports by decreasing size. Support \(P(n)\) can only be matched with the empty left support. Inductively, when the right support is \(T\), every allowed left support is contained in \(P(n)\setminus T\); all its proper subsets have already been assigned to right supports of larger cardinality. Thus the only unused permissible left support is exactly \(P(n)\setminus T\). This forces every edge of the matching. For \(r=0\), the one edge from divisor one is also forced. The two steps prove the general theorem, including the parity statement.

**3. Progressions with at least three prime factors cannot be unique.** Assume unique matching for a progression, so \(n\) is squarefree with \(r\) prime factors and \(N=2^r\). Every prime \(p\mid n\) must divide **exactly \(N/2\)** progression terms, because exactly half of all subsets of \(P(n)\) contain \(p\). If \(p\mid b\), the progression has either zero or \(N\) multiples of \(p\), neither allowed. If \(p\nmid b\), multiples occur at one residue class of the index modulo \(p\), so their number is at most \(\lceil N/p\rceil\). For \(r\ge3\), \(N\ge8\), and some \(p\mid n\) is at least three; then
\[
\left\lceil\frac{N}{p}\right\rceil\le\left\lceil\frac N3\right\rceil<\frac N2,
\]
a contradiction. Hence \(r\le2\).

**4. Classification for zero, one, or two prime factors.** When \(r=0\), \(n=1\) and the single match is forced. When \(r=1\), squarefreeness gives \(n=p\), and the two right support patterns are distinct exactly when one of \(a,a+b\) is divisible by \(p\). When \(r=2\), put \(n=pq\) with primes \(p<q\) and \(N=4\). Both primes must divide exactly two of the four terms. Since a prime \(q\ge5\) divides at most one term if \(q\nmid b\), the larger prime must be \(3\), and therefore \(n=6\). Exactly two of the four terms are multiples of three if and only if \(3\mid a\) and \(3\nmid b\): among indices \(0,1,2,3\), the repeated residue class modulo three occurs at indices \(0,3\). Exactly two terms are even if and only if \(b\) is odd. Under these conditions, indices \(0,3\) contain the two multiples of three with opposite parity, while indices \(1,2\) contain the two nonmultiples of three, again with opposite parity. All four right support patterns occur, proving both necessity and sufficiency. Finally setting \(a=b=1\) eliminates \(n=6\) and leaves only the prime \(p=2\), plus \(n=1\).

## Verification
Run `python3 verify.py` from the extracted package directory. It counts matchings independently by bit-mask dynamic programming over the original gcd graph, comparing the exact integer count with (i) the support-pattern criterion and (ii) the arithmetic-progression classification. It tests \(1\le n\le180\) when \(\tau(n)\le12\), \(1\le a\le14\), and \(1\le b\le5\), totaling 12,320 parameter triples; small instances are independently checked by enumerating all permutations. Additional arbitrary-target-set tests include squarefree divisors of \(6,30,210\) and examples with repeated profiles or repeated divisor powers. The recorded output is

```text
VERIFY_OK cases=12320 odd=220 unique=220 zero=3309 six_examples=8 arbitrary_sets=6 independent_brute=yes
```

The proof above covers **all** integers and progressions. These finite checks are corroborative, not a substitute for the unrestricted proof.

## Relationship to prior work
McNew and Pomerance, *Matchable numbers* (first public 2026-04-07, arXiv:2604.05304; subsequently Mathematika, DOI 10.1112/mtk.70116), systematically studied Recamán's divisor-set matching problem and established arithmetic-density and squarefree existence results; their Sections 1–6 address existence, not the number of matchings. The later Alekseyev paper *Coprime matchings of divisor sets* (arXiv:2610.37512v1, 2026-10-27) gives a necessary-and-sufficient **existence** criterion for arbitrary progressions, not a uniqueness or parity theorem. The OEIS entry A394994 records which positive integers admit matchings to the initial interval, not multiplicities. The present result classifies forced/odd multiplicity and identifies the exceptional progression \(n=6\), which is not a consequence of the existence statements without additional analysis.

## Limitations
The theorem does not determine the precise number of matchings when that number is a positive even integer, and it does not generalize the progression-specific exception beyond length \(\tau(n)\). A general Boolean-disjointness matrix argument underlies the uniqueness step; the specialized arithmetic classification is the nontrivial parameter consequence. Although relevant available primary texts and mathematical-record searches were compared, independent priority assessment has not been performed; earlier unindexed formulations of the Boolean matching observation may exist.

## References
1. N. McNew and C. Pomerance, *Matchable numbers*, arXiv:2604.05304, first public 2026-04-07; published in *Mathematika* 72(3), 2026, DOI:10.1112/mtk.70116. https://arxiv.org/html/2604.05304
2. M. A. Alekseyev, *Coprime matchings of divisor sets*, arXiv:2610.37512v1, first public 2026-10-27. https://arxiv.org/html/2610.37512v1
3. OEIS Foundation, A394994, *Matchable numbers*. https://oeis.org/A394994
4. C. Pomerance and J. L. Selfridge, *Proof of D. J. Newman's coprime mapping conjecture*, *Mathematika* 27 (1980), 69–83, DOI:10.1112/S0025579300009955.
