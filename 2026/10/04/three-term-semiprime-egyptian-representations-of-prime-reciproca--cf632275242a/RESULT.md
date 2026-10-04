# Three-term semiprime Egyptian representations of prime reciprocals
## Finding
For a prime \(p\), let \(\lambda(p)\) denote the minimum length of a representation
\[
\frac1p=\sum_{i=1}^k\frac1{n_i},
\]
where the \(n_i\) are distinct and each \(n_i\) is the product of two distinct primes. Li's theorem that every positive rational with squarefree reduced denominator has such a representation implies that \(\lambda(p)\) is finite.

The exact first nontrivial length is characterized as follows:
\[
\lambda(p)=3
\quad\Longleftrightarrow\quad
\exists\text{ distinct primes }q,r\ne p\text{ with }(q-1)(r-1)=p+1.
\]
In that case every three-term representation has denominator set \(\{pq,pr,qr}\), and hence is
\[
\frac1p=\frac1{pq}+\frac1{pr}+\frac1{qr}.
\]
No representation of \(1/p\) with one or two distinct squarefree-semiprime denominators exists.

A useful consequence is the sharp congruence-class simplification
\[
p\equiv1\pmod4
\quad\Longrightarrow\quad
\lambda(p)=3\iff p+2\text{ is prime}.
\]
Thus, in the residue class \(1\pmod4\), the shortest possible semiprime Egyptian representation of a prime reciprocal occurs exactly at the lower member of a twin-prime pair.

## Assumptions and scope
A "semiprime" here means a product of two **distinct** primes, matching the motivating source. All unit-fraction denominators in a representation are distinct. The theorem concerns prime reciprocals \(1/p\) and classifies exactly when the minimum length equals three; when the displayed factorization does not exist, it proves only \(\lambda(p)\ge4\), not an exact larger value.

The source theorem guarantees finiteness because the reduced denominator \(p\) is squarefree. The proof of the three-term criterion itself is elementary and does not depend on the source's analytic or formal-verification machinery.

## Proof
Represent a finite set of distinct squarefree semiprimes by a finite simple graph \(G\) whose vertices are the primes occurring in the denominators and whose edge \(\{u,v}\) represents the denominator \(uv\). Suppose
\[
\frac1p=\sum_{\{u,v\}\in E(G)}\frac1{uv}.
\]
The prime \(p\) must occur as a vertex: otherwise the reduced denominator of the right-hand side would divide the product of the vertices of \(G\), which is coprime to \(p\), impossible.

Let
\[
L=\prod_{v\in V(G)}v.
\]
Fix a vertex \(q\ne p\). Multiplying the identity by \(L\) and reducing modulo \(q\), the left side \(L/p\) is \(0\pmod q\). Every right-side term from an edge not incident with \(q\) is also \(0\pmod q\). If \(q\) had degree one, with unique neighbour \(r\), the remaining term would be
\[
\frac{L}{qr}\not\equiv0\pmod q,
\]
a contradiction. Therefore every vertex other than \(p\) has degree at least two.

A one-edge graph containing \(p\) has a non-\(p\) leaf, so length one is impossible. A two-edge simple graph containing \(p\) also has a leaf different from \(p\): the two edges are either disjoint or form a path of length two. Hence length two is impossible.

Now suppose there are exactly three edges. The degree sum is six. Since every non-\(p\) vertex has degree at least two, a connected three-edge graph containing \(p\) cannot have four or more vertices: if \(p\) had degree one, the other three vertices would already contribute at least six to the degree sum, and if \(p\) had degree at least two the total is larger still. A disconnected component not containing \(p\) would likewise have minimum degree at least two and consume all three edges, leaving no edge incident with \(p\). Thus \(G\) has exactly three vertices, all of degree two, so it is a triangle on \(\{p,q,r}\).

Consequently every three-term representation has the form
\[
\frac1p=\frac1{pq}+\frac1{pr}+\frac1{qr}.
\]
Multiplication by \(pqr\) gives
\[
qr=q+r+p,
\]
which is equivalent to
\[
(q-1)(r-1)=p+1.
\]
This proves necessity. Conversely, if distinct primes \(q,r\ne p\) satisfy this factorization, reversing the algebra proves the displayed three-term identity, and the three denominators are distinct squarefree semiprimes. Since lengths one and two are impossible, this is exactly the condition \(\lambda(p)=3\).

Finally suppose \(p\equiv1\pmod4\). Then \(p+1\equiv2\pmod4\). If both \(q\) and \(r\) were odd, \((q-1)(r-1)\) would be divisible by four. Hence one of \(q,r\) must equal \(2\), and the factorization forces the other to equal \(p+2\). The converse is immediate. This proves the twin-prime corollary.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It exhaustively checks all one-, two-, and three-edge subsets of the complete graph on the first ten primes, confirming that every equality to a prime reciprocal at length three is exactly a triangle satisfying \((q-1)(r-1)=p+1\), and that no length-one or length-two equality occurs in that finite universe. It also checks the divisor-factorization criterion and the \(p\equiv1\pmod4\) twin-prime corollary for every prime \(p\le5000\).

The finite computation is corroboration only. The theorem for all primes is established by the modular leaf argument and the three-edge graph classification above.

## Relationship to prior work
Li's 2026 paper proves that every positive rational \(a/b\) with squarefree \(b\) is a finite sum of distinct unit fractions with squarefree-semiprime denominators. Its introduction and theorem are existential, and its construction uses large complete bipartite graphs; the paper does not state a minimum-length classification. The earlier 2026 paper by Li proves all natural-number targets and rational targets above a threshold, likewise without a short-length classification. Butler--Erdős--Graham treat denominators with three distinct prime factors rather than semiprimes.

The present result asks the first finite-length question for the simplest squarefree denominators that are not themselves allowable denominators: prime denominators. It converts a three-term representation into a triangle in the prime-support graph and gives the exact shifted-prime factorization criterion. In the class \(p\equiv1\pmod4\), that criterion collapses to the twin-prime condition.

Targeted searches for the exact triangle identity, the factorization \((q-1)(r-1)=p+1\), minimum-length semiprime Egyptian representations of \(1/p\), and the prime-support leaf obstruction found no published statement of this classification. An informal Egyptian-fraction puzzle page contains a related local modular relation for semiprime representations of integers; it does not state the reciprocal-prime three-term theorem. An unrestricted OEIS table counts ordinary three-term Egyptian representations but imposes no semiprime condition.

## Limitations
The theorem does not determine \(\lambda(p)\) when no admissible factorization of \(p+1\) exists; it only gives the rigorous lower bound \(\lambda(p)\ge4\), with finiteness supplied by Li's existence theorem. No density assertion is made about primes satisfying the factorization criterion. The originality search cannot exclude unindexed folklore, especially because the graph argument is elementary; this residual risk is recorded in the review.

## References
1. Shisheng Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306*, arXiv:2609.32140v1 (2026). Primary MSC 11D68.
2. Shisheng Li, *Every natural number is a sum of distinct semiprime unit fractions*, arXiv:2606.15159v2 (2026).
3. Steve Butler, Paul Erdős, Ron Graham, *Egyptian Fractions with Each Denominator Having Three Distinct Prime Divisors*, Integers 15 (2015), A51.
