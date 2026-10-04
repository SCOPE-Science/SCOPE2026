# Even-parameter cycle bound from the least missing prime \(\rho(k)\)

## Finding
For a positive integer \(k\), Das defines
\[
\varphi_k(x)=
\begin{cases}
x+k,&x\text{ prime},\\
P^+(x),&x\text{ composite},
\end{cases}
\]
where \(P^+(x)\) is the largest prime divisor of \(x\).

Assume throughout this finding that \(k\ge2\) is even. Let
\[
\rho(k)=\min\{q:q\text{ prime and }q\nmid k\}.
\]
Then every periodic cycle of \(\varphi_k\) contains a prime not exceeding
\[
B(k)=\max\left\{\rho(k),\frac{k(\rho(k)-1)}2\right\}.
\]
Consequently, if \(L(k)\) denotes the number of distinct cycles, then
\[
L(k)\le \pi(B(k)).
\]

Two common cases become especially simple. If \(k\ge4\) is even and \(3\nmid k\), then \(\rho(k)=3\) and
\[
B(k)=k,
\qquad
L(k)\le\pi(k).
\]
If \(6\mid k\) and \(5\nmid k\), then \(\rho(k)=5\) and
\[
B(k)=2k,
\qquad
L(k)\le\pi(2k).
\]
For \(k=2\), the formula gives \(B(2)=3\).

## Assumptions and scope
The map is exactly the deterministic largest-prime-divisor map introduced by Das. A cycle is a directed periodic orbit of this map.

The theorem concerns even parameters only. For odd \(k\), Das already proves a direct descent once a prime exceeds \(k\), so the difficult parity case in the original argument is the even one.

The least missing prime \(\rho(k)\) is the quantity denoted \(N(k)\) by Dubickas. The proof uses only its elementary prime-run consequence: except when a starting prime equals \(\rho(k)\), one of the first \(\rho(k)\) terms of its arithmetic progression with step \(k\) is composite.

## Proof
Every cycle contains a prime, because a composite state maps immediately to a prime.

Let \(C\) be a cycle. If \(C\) already contains a prime at most \(B(k)\), there is nothing to prove. Suppose instead that every prime in \(C\) is greater than \(B(k)\).

Choose a prime \(p\) in \(C\). Since
\[
p>B(k)\ge\rho(k),
\]
we have \(p\ne\rho(k)\). Because \(k\) is even and \(p\) is odd, every term
\[
p,
\quad p+k,
\quad p+2k,
\quad\ldots
\]
is odd.

Let \(\ell\ge1\) be the least index for which
\[
c=p+\ell k
\]
is composite. Such an index exists; for example, the term with index \(p\) is
\[
p+pk=p(1+k),
\]
which is composite.

Dubickas's arithmetic-progression lemma for the least prime not dividing \(k\) implies, because \(p\ne\rho(k)\), that among
\[
p,p+k,\ldots,p+(\rho(k)-1)k
\]
there is a composite. Hence
\[
\ell\le\rho(k)-1.
\]
The composite \(c\) is odd. Therefore its largest prime divisor satisfies
\[
P^+(c)\le\frac c3.
\]
The next prime state after the prime block is thus
\[
q=P^+(c)
\le\frac{p+\ell k}{3}
\le\frac{p+k(\rho(k)-1)}3.
\]
Since
\[
p>B(k)\ge\frac{k(\rho(k)-1)}2,
\]
we obtain
\[
q<p.
\]

Thus, whenever a prime state of the cycle is larger than \(B(k)\), passing through its maximal consecutive prime block and the following composite produces a strictly smaller prime state. Under the supposition that every prime of \(C\) exceeds \(B(k)\), repeated prime-to-prime transitions would strictly decrease forever. That is impossible on a finite directed cycle, where the same prime must eventually recur. Hence every cycle contains a prime at most \(B(k)\).

Distinct cycles of a deterministic map are disjoint. Assign to each cycle its least prime not exceeding \(B(k)\). This assignment is injective into the set of primes at most \(B(k)\), proving
\[
L(k)\le\pi(B(k)).
\]

The displayed special cases follow from \(\rho(k)=3\) when \(k\) is even and not divisible by \(3\), and from \(\rho(k)=5\) when \(6\mid k\) but \(5\nmid k\).

## Verification
The accompanying `verify.py` checks the critical local descent on every even
\[
2\le k\le400
\]
and every tested prime
\[
3\le p\le5000
\]
above the claimed threshold. It verifies that the first composite occurs by index \(\rho(k)-1\), that its largest prime factor is at most one third of it, and that the next prime state is smaller than \(p\).

As a separate regression, it follows trajectories for all starts through \(1000\) for every even \(k\le100\) and checks that every observed cycle contains a prime at most \(B(k)\).

These finite checks are not used for exhaustiveness. The theorem for all even \(k\) follows from the symbolic descent argument above.

## Relationship to prior work
Das proves eventual periodicity, finiteness of \(L(k)\), and a generic loop locator based on the fact that sufficiently long prime arithmetic progressions force many small primes to divide \(k\). His Remark 2.8 gives the published comparison scale \(k\sqrt{k}/2\) for a prime that must occur in each loop.

Dubickas later introduces exactly the least-missing-prime parameter \(N(k)=\rho(k)\), proves that a prime progression with step \(k\) encounters a composite within the first \(\rho(k)\) terms except for one explicit exceptional start, and derives global bounds for a broader class of iterative sequences. The inspected paper does not state an intrinsic cycle-count bound for Das's deterministic map.

The present result combines that exact prime-run ceiling with a feature specific to even \(k\): after a block of odd primes, the first composite is odd, so its largest prime divisor is at most one third of it. This improves the generic locator whenever the resulting \(B(k)\) is smaller. In particular, for every even \(k\ge8\) with \(3\nmid k\), it replaces the \(k\sqrt{k}/2\) scale by the linear bound \(k\).

Targeted searches for the exact bound \(k(\rho(k)-1)/2\), the special bound \(L(k)\le\pi(k)\) for even \(k\) not divisible by \(3\), and equivalent least-missing-prime formulations did not locate a prior statement.

## Limitations
The theorem is an upper bound on the location and number of cycles; it does not determine \(L(k)\) exactly and does not resolve whether \(L(k)\) is unbounded as \(k\) varies.

For parameters with many consecutive small prime divisors, \(\rho(k)\) can be larger, so the arithmetic-sensitive bound is not uniformly smaller than every previously published numerical bound at every small \(k\).

Literature non-detection cannot rule out an equivalent observation in an unindexed source.

## References
1. Angsuman Das, “A Family of Iterated Maps on Natural Numbers,” arXiv:2312.06629v1, first posted 11 December 2023; DOI 10.1080/10586458.2023.2294184; MSC \(11B83\), \(11B37\), \(11A25\).
2. Artūras Dubickas, “A Class of Bounded Iterative Sequences of Integers,” *Axioms* 13 (2024), 107; DOI 10.3390/axioms13020107.
