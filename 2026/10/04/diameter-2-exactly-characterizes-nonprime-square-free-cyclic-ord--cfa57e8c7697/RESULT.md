# Diameter \(2\) exactly characterizes nonprime square-free cyclic orders in the \(\psi\)-divisibility graph
## Finding
Let \(G=C_n\) be a finite cyclic group, and let \(\Psi_G\) be its \(\psi\)-divisibility graph: the vertices are the nontrivial subgroups of \(G\), and distinct vertices \(H,K\) are adjacent when one contains the other and the sum of element orders of the smaller subgroup divides that of the larger subgroup.

Then
\[
\operatorname{diam}(\Psi_G)=2
\]
if and only if \(n\) is square-free and has at least two distinct prime divisors.

Equivalently, among finite cyclic groups, diameter \(2\) occurs exactly for the nonprime square-free orders. This resolves Problem 2.9 of Lazorec's paper on \(\psi\)-divisibility graphs.

## Assumptions and scope
For a finite group \(X\), write
\[
\psi(X)=\sum_{x\in X} o(x).
\]
For a prime \(p\) and integer \(a\ge 1\),
\[
\psi(C_{p^a})=\frac{p^{2a+1}+1}{p+1},
\]
and the standard divisibility criterion is
\[
\psi(C_{p^a})\mid\psi(C_{p^b})
\quad\Longleftrightarrow\quad
2a+1\mid 2b+1.
\]
Also, \(\psi\) is multiplicative on direct products of coprime order.

Diameter is used in the ordinary connected-graph sense. The one-vertex graph \(\Psi_{C_p}\) has diameter \(0\). The known connectivity classification for cyclic groups says that \(\Psi_{C_n}\) is connected when \(n\) has at least two distinct prime divisors, while the remaining prime-power cases do not create a diameter-\(2\) exception.

The primary classification is MSC 20D60, arithmetic and combinatorial problems involving abstract finite groups.

## Proof
First suppose that \(n\) is square-free and has at least two distinct prime divisors. Every subgroup \(C_d\le C_n\) is obtained by selecting a subset of the prime factors of \(n\). By coprime multiplicativity,
\[
\psi(C_d)\mid\psi(C_n).
\]
Hence \(C_n\) is adjacent to every other vertex. Two distinct prime-order subgroups are incomparable, so the graph is not complete. Therefore its diameter is exactly \(2\).

Conversely, suppose that \(\operatorname{diam}(\Psi_{C_n})=2\). Connectivity excludes all prime-power cases except \(C_p\), whose graph has diameter \(0\). Thus \(n\) has at least two distinct prime divisors.

Assume for contradiction that \(n\) is not square-free. Choose a prime \(p\) with
\[
n=p^\alpha m,\qquad \alpha\ge 2,\qquad m>1,\qquad (p,m)=1.
\]
We first choose an integer \(t\) satisfying
\[
2\le t\le\alpha,\qquad 2t+1\ \text{is prime},\qquad \alpha<3t-2.
\]
For \(\alpha=2,3,4\), one may take \(t=2,2,3\), respectively. If \(\alpha\ge5\), Bertrand's postulate applied to \(\alpha+1\) gives a prime \(r\) with
\[
\alpha+1<r<2\alpha+2.
\]
Since \(r\) is odd, write \(r=2t+1\). Then \(t\le\alpha\) and \(t>\alpha/2\), so
\[
3t-2>\frac{3\alpha}{2}-2>\alpha.
\]

Now consider the two vertices
\[
H=C_{p^t},\qquad K=C_{p^{t-1}m}.
\]
They are incomparable, hence not adjacent. We show that they have no common neighbor.

A common neighbor \(L\) must be either below both \(H\) and \(K\), or above both, because the mixed containment possibilities would force \(H\) and \(K\) themselves to be comparable.

If \(L\) is below both, then
\[
L=C_{p^j}
\]
for some \(1\le j\le t-1\). Adjacency of \(L\) to \(H\) would require
\[
2j+1\mid 2t+1.
\]
But \(2t+1\) is prime and
\[
1<2j+1<2t+1,
\]
which is impossible.

If \(L\) is above both, then, because \(K\) already contains the full \(m\)-part,
\[
L=C_{p^s m}
\]
for some \(t\le s\le\alpha\). Adjacency of \(K\) to \(L\), after cancelling the common factor \(\psi(C_m)\), requires
\[
\psi(C_{p^{t-1}})\mid\psi(C_{p^s}),
\]
equivalently
\[
2t-1\mid 2s+1.
\]
Since \(s\ge t\), the quotient is an odd integer greater than \(1\), hence at least \(3\). Therefore
\[
2s+1\ge 3(2t-1),
\]
so
\[
s\ge 3t-2.
\]
This contradicts \(s\le\alpha<3t-2\).

Thus \(H\) and \(K\) have no common neighbor. Since the cyclic graph is connected when at least two distinct primes divide \(n\), their distance is at least \(3\), contradicting diameter \(2\). Hence \(n\) must be square-free.

## Verification
The proof uses only four ingredients: the subgroup lattice of a cyclic group, multiplicativity of \(\psi\) on coprime direct products, the prime-power divisibility criterion
\[
\psi(C_{p^a})\mid\psi(C_{p^b})
\Longleftrightarrow
2a+1\mid2b+1,
\]
and Bertrand's postulate.

The accompanying `artifacts/verify.py` independently reconstructs cyclic \(\psi\)-divisibility graphs for a finite test range using exact integer arithmetic. It checks the square-free diameter-\(2\) direction, checks that nonsquare-free mixed-prime orders do not have diameter \(2\), and validates the proof's explicit pair \(C_{p^t},C_{p^{t-1}m}\) for sampled factorizations. These computations are sanity checks, not substitutes for the proof.

## Relationship to prior work
Lazorec introduced the \(\psi\)-divisibility graph and proved the prime-power divisibility criterion used above. In Problem 2.9, the paper explicitly asks for a proof that diameter \(2\) for a finite cyclic group forces at least two prime divisors and square-free order, while noting that the converse is clear. The argument above supplies the missing direction.

A 2026 paper by Kumar, Kumar, and Sehgal studies extreme vertices for \(\Psi_{C_{p^n}}\), i.e. prime-power cyclic groups, rather than the mixed-prime diameter-\(2\) classification. Targeted searches for the exact diameter statement, the square-free characterization, and the cited Problem 2.9 did not locate a published solution. Recent results on \(\psi\)-divisibility of cyclic-by-cyclic semidirect products and of \(Z\)-groups concern divisibility of subgroup sums and do not imply that a cyclic \(\psi\)-divisibility graph of diameter \(2\) has a universal vertex.

## Limitations
The theorem is only about finite cyclic groups. It does not classify diameter \(2\) for noncyclic groups, nor does it address other graph invariants.

The originality assessment is based on targeted searches of the source problem, recent \(\psi\)-divisibility-graph literature, and closely related published-result indexes. As with any literature search, an equivalent unpublished or differently phrased argument could have been missed.

## References
1. M.-S. Lazorec, *A graph related to the sum of element orders of a finite group*, Contributions to Discrete Mathematics 18 (2023), 113–128. Earliest public version: arXiv:2203.00071, 28 February 2022. DOI: 10.55016/ojs/cdm.v18i2.73182.
2. J. Harrington, L. Jones, A. Lamarche, *Characterizing Finite Groups Using the Sum of the Orders of the Elements*, International Journal of Combinatorics (2014), Article ID 835125. DOI: 10.1155/2014/835125.
3. A. Kumar, V. Kumar, A. Sehgal, *Extreme Vertices of the Psi-Divisible Graph of the Group \(Z_{p^n}\)*, Journal of the Indonesian Mathematical Society 32 (2026), article 2145. DOI: 10.22342/jims.v32i2.2145.
