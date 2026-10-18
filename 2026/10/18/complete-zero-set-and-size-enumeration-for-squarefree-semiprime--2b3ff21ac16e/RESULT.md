# Complete zero-set and size enumeration for squarefree semiprime convolution idempotents

## Finding
Let \(p\ne q\) be primes, \(N=pq\), and \(G=\mathbb Z/N\mathbb Z\). For any frequency subset \(J\subseteq G\) define
\[
h_J(t)=\frac1N\sum_{k\in J}\exp(2\pi i kt/N).
\]
These are exactly the convolution idempotents on \(G\). Set
\[
U=\{t\in G:\gcd(t,N)=1\},\quad S_p=\{t\in G:\gcd(t,N)=p\},\quad S_q=\{t\in G:\gcd(t,N)=q\}.
\]
For a formal variable \(z\), define
\[
P_{p,q}(z)=\sum_{r=0}^{p}\bigl(\binom{p}{r}\bigr)^q z^{rq},\qquad
Q_{p,q}(z)=\sum_{s=0}^{q}\bigl(\binom{q}{s}\bigr)^p z^{sp}.
\]

**Theorem.** The only possible exact zero sets \(Z(h_J)=\{t:h_J(t)=0\}\), with their complete cardinality-weight enumerators \(\sum_{J:Z(h_J)=Z}z^{|J|}\), are:

| Exact zero set | Cardinality-weight enumerator |
| --- | --- |
| \(G\) | \(1\) |
| \(G\setminus\{0\}\) | \(z^{pq}\) |
| \(U\cup S_p\) | \((1+z^q)^p-1-z^{pq}\) |
| \(S_p\) | \(P_{p,q}(z)-(1+z^q)^p\) |
| \(U\cup S_q\) | \((1+z^p)^q-1-z^{pq}\) |
| \(S_q\) | \(Q_{p,q}(z)-(1+z^p)^q\) |
| \(\varnothing\) | \((1+z)^{pq}-P_{p,q}(z)-Q_{p,q}(z)+1+z^{pq}\) |

Every listed class occurs for every pair of distinct primes. In particular the last polynomial counts **zero-free nontrivial convolution idempotents by Fourier rank**: its coefficient of \(z^k\) is their number with \(|J|=k\). Therefore
\[
\#\{J:Z(h_J)=\varnothing\}=2^{pq}-\sum_{r=0}^{p}\bigl(\binom{p}{r}\bigr)^q-\sum_{s=0}^{q}\bigl(\binom{q}{s}\bigr)^p+2.
\]
A spectral set \(J\) with cardinality relatively prime to \(N\) always gives a zero-free idempotent; this follows directly from the displayed enumerator.

## Assumptions and scope
Circular convolution is unnormalized, \((f*g)(t)=\sum_{u\in G}f(u)g(t-u)\); Fourier inversion uses the factor \(N^{-1}\), so \(h_J*h_J=h_J\). Both primes may be odd, and one may equal \(2\). The empty mask gives the zero function, whose zero set is all of \(G\). The full mask gives the delta function at zero. The theorem addresses exact zero sets, not merely prescribed subsets of zeros, and counts actual subsets \(J\), without quotienting by translation or inversion.

Under the Chinese remainder isomorphism \(G\cong\mathbb Z_p\times\mathbb Z_q\), view \(1_J\) as a \(p\)-by-\(q\) zero-one matrix \(M=(M_{ab})\), with \(a\in\mathbb Z_p\), \(b\in\mathbb Z_q\). Say that its *column sums are uniform* if \(\sum_a M_{ab}\) is independent of \(b\), and its *row sums are uniform* if \(\sum_b M_{ab}\) is independent of \(a\).

## Proof
**1. Fourier-idempotent reduction.** Fourier transformation converts circular convolution into coordinatewise multiplication. Thus \(h*h=h\) if and only if each Fourier coefficient is \(0\) or \(1\); its support is a unique set \(J\), and Fourier inversion gives \(h=h_J\). Also \(h_J(0)=|J|/N\), so \(0\) can be a zero only when \(J\) is empty.

**2. The three nonzero time strata.** The Galois automorphisms of \(\mathbb Q(e^{2\pi i/N})\) show that the nonzero zero set is a union of the three sets \(U,S_p,S_q\). For \(t\in S_p\), the exponential depends only on \(b\in\mathbb Z_q\) through a nontrivial \(q\)-th root. The unique rational linear relation among the \(q\) distinct \(q\)-th roots is their complete sum. Therefore \(h_J\) vanishes on \(S_p\) precisely when the column sums of \(M\) are uniform. Similarly, it vanishes on \(S_q\) precisely when the row sums are uniform.

**3. Primitive-zero rigidity.** For \(t\in U\), after permuting CRT coordinates, the vanishing equation is
\[
\sum_{a=0}^{p-1}\sum_{b=0}^{q-1}M_{ab}\zeta_p^a\zeta_q^b=0,
\]
where the roots are primitive. Over \(\mathbb Q\), the map sending a matrix to the displayed cyclotomic sum is surjective onto \(\mathbb Q(\zeta_{pq})\), because its terms are all \(N\)-th roots. Hence its kernel has dimension \(pq-(p-1)(q-1)=p+q-1\). Every additive matrix \(M_{ab}=\alpha_a+\beta_b\) belongs to this kernel, because both complete root sums vanish; additive matrices form a \(p+q-1\)-dimensional space. Thus the primitive-zero equation is equivalent to this additive form.

For a zero-one additive matrix, differences between any two rows are constant across columns and belong to \(\{-1,0,1\}\). If all rows coincide, \(M\) depends only on \(b\). Otherwise two rows differ by \(1\) or \(-1\) everywhere, forcing one row to be all zero and the other all one; comparison with the zero row forces *every* row to be constant. Then \(M\) depends only on \(a\). Conversely both kinds of coordinate-cylinder matrix annihilate primitive characters. Consequently
\[
U\subseteq Z(h_J)\iff M\text{ depends only on }a\text{ or only on }b.
\]
In the first case column sums are uniform, and in the second case row sums are uniform. In particular, primitive zeros never occur without zeros in \(S_p\) or \(S_q\).

**4. Simultaneous row/column rigidity.** If all column sums equal \(r\in\{0,\ldots,p\}\) and all row sums equal \(s\in\{0,\ldots,q\}\), counting the ones both ways gives \(qr=ps\). Because \(p\) and \(q\) are distinct primes, \(p\mid r\); hence \(r=0\) or \(r=p\). The matrix is empty or full. Thus a proper nonempty mask cannot have zeros in both \(S_p\) and \(S_q\).

**5. Complete weighted count.** A matrix with uniform column sum \(r\) has \(\binom pr\) choices independently in each of the \(q\) columns; its total weight is \(rq\). Its generating polynomial is exactly \(P_{p,q}\). Among these, the matrices depending only on \(a\) have polynomial \((1+z^q)^p\). Similarly, matrices with uniform row sums have enumerator \(Q_{p,q}\), and those depending only on \(b\) have \((1+z^p)^q\). The two uniformity events intersect only at the empty and full matrices, with generating polynomial \(1+z^{pq}\). Splitting the two events into cylinders and noncylinders, then subtracting their union from all \((1+z)^{pq}\) masks, yields each row of the table. The four intermediate nonempty zero-set classes are realized by uniform noncylinder matrices or proper nonempty coordinate cylinders; singleton masks supply the zero-free class. Thus no rows of the table are merely formal.

## Verification
Run \(`python3 checker.py`\) from the directory containing the accompanying source file. It has no third-party dependencies. It constructs the exact integer cyclotomic polynomial \(\Phi_{pq}\) and, for every frequency mask, reduces the relevant Fourier sums modulo \(\Phi_{pq}\), at time representatives \(1,p,q\). It compares every resulting exact zero-set class and every zero-free cardinality coefficient against the theorem; it also checks the other four nontrivial class polynomials. Exhaustive checks passed for \((p,q)=(2,3),(2,5),(2,7),(3,5)\), comprising \(64,1024,16384,32768\) distinct masks respectively. Zero-free mask totals were \(36,740,12824,30030\). This finite verification does not replace the proof for arbitrary distinct primes.

## Relationship to prior work
Siripuram and Osgood (2020) formulate the convolution-idempotent zero-set problem and solve it for prime-power lengths; their concluding discussion identifies composite lengths as a further challenge. This theorem treats precisely squarefree lengths with two distinct prime factors and refines the solution by the spectral-mask cardinality. Lam and Leung (1995/2000), especially their Theorem 3.3, already describe vanishing sums of roots of unity with two prime factors; the primitive-character cancellation ingredient is classical and **is not claimed new here**. The contribution assessed here is the joint exact zero-set stratification and its full cardinality-weight enumerator for every semiprime length. Related existing work on four-point indicators on \(\mathbb Z_{2p}\) examines one special frequency-cardinality layer rather than all idempotents and their exact joint zero strata.

## Limitations
The proof uses two distinct primes and zero-one Fourier multipliers. It does not classify orders having repeated prime factors or three or more distinct prime factors, nor does it address general complex Fourier weights. The proof is self-contained, but the originality assessment is literature-limited: an equivalent enumerator or reformulation may exist in older cyclic-coding or cyclotomic-sum literature.

## References
1. A. Siripuram and B. Osgood, *Convolution Idempotents with a Given Zero-Set*, arXiv:2001.00739v1 (first public 2020-01-03); IEEE Transactions on Signal Processing **68** (2020), 4773–4781. https://arxiv.org/abs/2001.00739
2. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (1995), especially Theorem 3.3 and Corollary 3.4; Journal of Algebra **224** (2000), 91–109. https://arxiv.org/abs/math/9511209
3. A. Siripuram, W. Wu and B. Osgood, *Discrete Sampling: A Graph Theoretic Approach to Orthogonal Interpolation*, arXiv:1411.7086 (2014); IEEE Transactions on Information Theory **65** (2019), 8119–8130. https://arxiv.org/abs/1411.7086
