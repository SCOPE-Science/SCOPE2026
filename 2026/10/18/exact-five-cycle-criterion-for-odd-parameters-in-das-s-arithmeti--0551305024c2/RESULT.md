# Exact five-cycle criterion for odd parameters in Das's arithmetic map

## Finding
Let \(k\) be a **positive odd integer**, and let \(\varphi_k\) act on integers \(n\ge2\) by
\[
\varphi_k(n)=\begin{cases}n+k,&n\text{ is prime},\\P^+(n),&n\text{ is composite},\end{cases}
\]
where \(P^+(n)\) denotes the largest prime divisor of \(n\). Put \(q=P^+(k+1)\).

**Theorem.** The map \(\varphi_k\) possesses an orbit of exact least period five if and only if all three conditions hold:
1. \(k+2\) is prime;
2. \(q\) is odd;
3. \(k+q\) is a power of two.

Whenever these conditions hold, there is **exactly one** period-five cycle, up to cyclic rotation, namely
\[
2\longmapsto k+2\longmapsto2(k+1)\longmapsto q\longmapsto k+q\longmapsto2.
\]
Equivalently, all odd parameters giving an exact five-cycle arise from an integer \(m\ge1\) and an odd prime divisor \(q\mid 2^m+1\) with odd cofactor \(h=(2^m+1)/q\ge3\) satisfying
\[
P^+(h-1)\le q\qquad\text{and}\qquad q(h-1)+1\text{ is prime},
\]
by taking \(k=q(h-1)-1\). Every parameter obtained in this way has exactly one period-five cycle.

## Assumptions and scope
The map is the deterministic prime-increment/largest-prime-divisor map introduced by Das. The parameter is any **odd** positive integer; even parameters are not covered. An *exact period-five cycle* consists of five pairwise distinct integers \(n_0,\ldots,n_4\ge2\) with \(\varphi_k(n_j)=n_{j+1}\) for \(0\le j<4\) and \(\varphi_k(n_4)=n_0\). A cycle is identified up to rotation. The function \(P^+(a)\) is defined only for integers \(a\ge2\), which suffices for every occurrence above.

## Proof
**Step 1: Every odd-length cycle contains \(2\).** Since \(k\) is odd, every odd prime \(p\ge3\) maps to \(p+k\), which is even and at least \(4\), hence composite. Conversely, every composite maps to a prime. A cycle that avoids \(2\) must therefore alternate odd primes and composite integers, so its length is even. Every period-five cycle must contain \(2\).

**Step 2: The five-state pattern is forced.** Rotate a hypothetical period-five orbit to start at \(2\). If \(k+2=\varphi_k(2)\) were composite, its image would be an odd prime (because \(k+2\) is odd), whose next image would be an even composite. The image of that even composite is a prime; if it is \(2\), the orbit has returned after only four steps, and if it is odd, its next image is an even composite different from \(2\). Neither case is compatible with an exact five-cycle. Therefore \(k+2\) must be prime. The first three transitions are consequently
\[
2\longmapsto k+2\longmapsto2(k+1)\longmapsto P^+(2(k+1))=q,
\]
where \(q=P^+(k+1)\). If \(q=2\), the orbit has already returned to \(2\) in three steps, contradicting exact period five. Hence \(q\) is an odd prime. Its image is the even composite integer \(q+k\), whose next image is \(2\) precisely when \(q+k\) has no odd prime divisor, i.e. when it is a power of two. Thus all three conditions are necessary.

Conversely, if the conditions hold, each displayed arrow follows from the definition, and the five states are distinct: \(q\le k+1<k+2\); the states \(2\), \(q\), and \(k+2\) are distinct primes; and the two even composite states \(2(k+1)\), \(k+q\) are distinct because equality would imply \(q=k+2>k+1\). Therefore the period is exactly five. Since every such cycle contains \(2\) and \(\varphi_k\) is deterministic, the cycle is unique.

**Step 3: Arithmetic parametrization.** In the cycle, write \(k+q=2^m\). Because \(q\mid k+1\), the identity \(2^m+1=(k+1)+q\) shows \(q\mid2^m+1\). Let \(h=(2^m+1)/q\). Then \(k+1=q(h-1)\), and \(h\) is odd. Positivity and \(q\le k+1\) give \(h\ge3\). The equality \(P^+(k+1)=q\) is exactly the condition \(P^+(h-1)\le q\); primality of \(k+2\) is exactly primality of \(q(h-1)+1\). Conversely, for any listed \((m,q,h)\), setting \(k=q(h-1)-1\) gives an odd positive parameter, \(k+2=q(h-1)+1\) prime, \(P^+(k+1)=q\), and \(k+q=2^m\). The first characterization applies. \(\square\)

## Verification
The standalone `verify.py` implements the map using an exact largest-prime-factor sieve. For all odd \(1\le k\le5000\), it starts at every prime \(p\le k+2\), evaluates five successive steps, retains cycles only when the five visited states are distinct, and compares with the theorem's explicit predicted cycle. It finds exactly five qualifying parameters in this range:
\[
(k,q,m)=(5,3,3),(21,11,5),(51,13,6),(59,5,6),(1365,683,11).
\]
For instance, at \(k=5\) the cycle is \(2\to7\to12\to3\to8\to2\), and at \(k=21\) it is \(2\to23\to44\to11\to32\to2\).

Run `python3 verify.py` from the extracted package directory. Its finite census is a regression test, **not** an infinite proof; the unconditional classification for all odd parameters is established by the symbolic argument above.

## Relationship to prior work
Das introduced \(\varphi_k\), proved ultimate periodicity, and raised questions about possible loops and their counts. Previous classifications of exact period-two, period-three, and period-four cycles do not cover period five. In particular, the exact Fermat-prime characterization of period three is already established in earlier work and is **not** claimed as new here. The present result addresses the next odd period and connects it instead to prime divisors of integers \(2^m+1\), with an additional cofactor-smoothness and shifted-primality test.

Dubickas considers a broader family of bounded iterative integer sequences, with examples of short admissible cycles. Those results do not give the exact largest-prime-divisor rule's odd-parameter five-cycle criterion. A published finite odd-parameter loop census and an even-parameter cycle-locator theorem likewise do not imply this all-odd-parameter characterization. Targeted literature and research-database comparisons did not locate an equivalent complete statement.

## Limitations
This theorem classifies period-five cycles **only for odd parameters**, not even ones. It does not prove infinitude of qualifying \(k\) or characterize other periods. The displayed prime-divisor parameterization is exact but includes primality and smoothness tests, rather than a closed list of qualifying integers. The finite computation establishes no unbounded-domain claim. An unindexed equivalent result may exist, and no independent mathematical audit is claimed.

## References
1. Angsuman Das, "A Family of Iterated Maps on Natural Numbers," arXiv:2312.06629v1, first made public 11 December 2023; *Experimental Mathematics* 33 (2024), 776–780, DOI 10.1080/10586458.2023.2294184. Original map and questions about loops.
2. Artūras Dubickas, "A Class of Bounded Iterative Sequences of Integers," *Axioms* 13 (2024), 107, DOI 10.3390/axioms13020107. Broader periodic-sequence framework.
3. "Exact cycles of lengths three and four in Das's arithmetic map," mathematical result in the earlier research record identified by `9113f264-80c9-4b61-9cc6-3b7754ef99d2`; preceding known coverage, not a new assertion here.
4. "Period-two and period-three classification for Das's map," mathematical result identified by `a6fb565f-372c-4ebb-9055-037c1563acd6`; preceding known coverage.
5. published-finding corpus, "Thirty-six distinct loops for Das's map at \(k=20735\)," mathematical note, 4 October 2026; record `2026/10/4/SCOPE-thirty-six-distinct-loops-for-das-s-map-at-k-20735--c588f79a1e3b`.
6. published-finding corpus, "Even-parameter cycle bound from the least missing prime \(\rho(k)\)," mathematical note, 4 October 2026; record `2026/10/4/SCOPE-even-parameter-cycle-bound-from-the-least-missing-prime-rho-k--644ecc618762`.
