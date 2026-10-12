# The first composite multiplicity layer of \(s\)-practical numbers
## Finding
Let \(s(n)=\sigma(n)-n\) be the sum of the proper divisors of \(n\). Following Schwab and Thompson, call \(n\) \(s\)-practical when every integer in
\[
1\le m\le S_s(n):=\sum_{d\mid n}s(d)
\]
is a sum of distinct entries of the multiset \(\{s(d):d\mid n\}\).

If \(n\) is composite and \(s\)-practical, then
\[
\Omega(n)\ge 4.
\]
The boundary is rigid:
\[
\Omega(n)=4\quad\Longleftrightarrow\quad n=60
\]
among composite \(s\)-practical integers. Thus the complete \(\Omega(n)\le4\) list consists of \(1\), all primes, and \(60\).

## Assumptions and scope
Here \(\Omega(n)\) counts prime factors with multiplicity. The value \(s(1)=0\) does not affect subset sums, so it is omitted when the positive weights are sorted. We use the standard complete-sequence criterion: positive integers \(w_1\le\cdots\le w_k\) have every subset sum from \(0\) through \(\sum_i w_i\) exactly when
\[
w_{i+1}\le 1+\sum_{j\le i}w_j
\]
for every \(i<k\). This is Proposition 1.1 in Schwab--Thompson.

For a prime \(p\), \(s(p)=1\). Conversely, if \(d\) is composite, then \(s(d)\ge3\): if \(p\mid d\) is prime, the distinct proper divisors \(1\) and \(p\) already contribute at least \(3\). Hence the positive weight multiset for \(n\) contains exactly \(\omega(n)\) copies of \(1\), one for each distinct prime divisor.

## Proof
We exhaust the multiplicative partitions of \(\Omega(n)\).

For \(\Omega(n)=2\), either \(n=p^2\) or \(n=pq\) with distinct primes. In the first case the weights begin with \(1,p+1\), so \(p+1\ge3>2\). In the second they begin with \(1,1,p+q+1\), so \(p+q+1\ge6>3\). Neither case is \(s\)-practical.

For \(\Omega(n)=3\), a prime cube fails for the same reason. For \(n=p^2q\), the two prime weights are \(1,1\), and the next possible weight \(s(p^2)=p+1\) must be at most \(3\); hence \(p=2\). Writing \(n=4q\), after weights \(1,1,3\) the next weight is \(q+3\), unless \(q=3\); the complete-sequence inequality forces \(q=3\). The sole candidate \(12\) has positive weights
\[
1,1,3,6,16,
\]
and fails because \(16>12\). If \(n=pqr\) is squarefree, the three initial ones are followed by a pair-product weight at least \(s(6)=6>4\). Thus no composite with \(\Omega(n)\le3\) is \(s\)-practical.

Now suppose \(\Omega(n)=4\). A fourth power fails immediately as above.

If \(n=p^3q\), the first two positive weights are \(1,1\), so \(s(p^2)=p+1\le3\) forces \(p=2\). The next inequality then leaves only \(q=3\), giving \(n=24\). Its positive weights are
\[
1,1,3,6,7,16,36,
\]
and \(36>35\), so \(24\) fails.

If \(n=p^2q^2\) with \(p<q\), the same first-gap argument forces \(p=2\). After \(1,1,3\), the next smallest weight is \(q+1\), so \(q+1\le6\). Hence \(q\in\{3,5\}\), producing \(36\) and \(100\). Their first fatal inequalities are respectively \(55>53\) and \(22>20\).

It remains to treat \(n=p^2qr\), where \(p,q,r\) are distinct primes. There are three initial ones, so the next positive composite weight must be at most \(4\). A product of two distinct primes has proper-divisor sum at least \(6\), while \(s(p^2)=p+1\); therefore the repeated prime is \(p=2\) or \(p=3\).

If \(p=2\), write the other primes as \(q<r\). After \(1,1,1,3\) the running sum is \(6\), and the next smallest unused weight is \(s(2q)=q+3\). Thus \(q+3\le7\), so \(q=3\). After adding \(s(6)=6\), the running sum is \(12\); the next smallest unused weight is \(\min\{r+3,16\}\). It must be at most \(13\), so \(r\in\{5,7\}\). This leaves \(60\) and \(84\).

If \(p=3\), the next weight after \(1,1,1,4\) must be at most \(8\). If neither other prime is \(2\), the smallest pair weight is at least \(s(15)=9\), so one of them is \(2\). Write the third prime as \(r\ge5\). After adding \(s(6)=6\), the running sum is \(13\), and the next smallest unused weight is \(\min\{r+3,21\}\). Hence \(r+3\le14\), so \(r\in\{5,7,11\}\), producing \(90,126,198\).

Finally, if \(n\) is squarefree with four prime factors, the four initial ones are followed by a pair-product weight at least \(6>5\), so the complete-sequence criterion fails.

The remaining five candidates are decided exactly. The positive weights for \(60\) are
\[
1,1,1,3,6,8,9,16,22,42,108.
\]
Each weight is at most one plus the sum of its predecessors, so \(60\) is \(s\)-practical. For \(84,90,126,198\), the first fatal inequalities are respectively
\[
140>132,\qquad 144>127,\qquad 186>151,\qquad 270>262.
\]
Together with the earlier failures, this proves both the lower bound and uniqueness at \(\Omega(n)=4\).

## Verification
A standalone checker independently enumerates every composite \(n\le10^6\) with \(\Omega(n)\le4\), builds all divisor values \(s(d)\) from the prime factorization, and applies the complete-sequence criterion. It finds only \(60\). It also checks the exact sorted weights of \(60\) and the explicit rejected candidates \(12,24,36,84,90,100,126,198\). This finite computation is regression evidence only; the proof above is symbolic and has no numerical cutoff.

## Relationship to prior work
Schwab and Thompson introduced \(f\)-practical numbers and, in their section on functions that are neither additive nor multiplicative, defined \(s(n)=\sigma(n)-n\), proved that every prime is \(s\)-practical, and proved that the \(s\)-practical set has asymptotic density zero. Their paper also supplies the complete-sequence criterion used here. It does not state a classification by \(\Omega(n)\) or a first composite multiplicity layer.

OEIS A393492 records \(s\)-practical numbers and its table contains both \(48\) and \(60\). Its comments state that all primes occur and that no composite prime power occurs, attributing the latter observation to a 2026 master's thesis by Anniek Reuijl. The database does not state the global bound \(\Omega(n)\ge4\) for composites or the uniqueness of \(60\) at equality. A finite table cannot imply the unbounded classification proved here.

## Limitations
The theorem concerns only the first multiplicity layer. It does not classify \(s\)-practical integers with \(\Omega(n)\ge5\), nor does it address their counting function beyond the published density result. The 2026 Reuijl thesis is a closely relevant source; its repository record was identifiable, but its full text was not available for inspection during this review. Indexed metadata and OEIS attribute to it the prime-power exclusion, not the present complete low-\(\Omega\) classification, so an unindexed equivalent statement there remains a residual originality risk.

## References
1. Nicholas Schwab and Lola Thompson, *A generalization of the practical numbers*, arXiv:1701.08504, first submitted 30 January 2017; later published in *International Journal of Number Theory* 14 (2018), 1487--1503, DOI 10.1142/S1793042118500902.
2. OEIS A393492, *S-practical numbers*, including the table through \(10000\) and references to Schwab--Thompson and Reuijl.
3. Anniek Reuijl, *Representing integers with sums of proper divisors*, master's thesis, Utrecht University, 2026.
