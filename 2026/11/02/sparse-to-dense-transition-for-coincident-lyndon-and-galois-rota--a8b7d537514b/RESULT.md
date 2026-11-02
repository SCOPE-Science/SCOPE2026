# Sparse-to-dense transition for coincident Lyndon and Galois rotations

## Finding

For integers \(n\ge2\) and \(1\le k<n\), let \(\mathcal P_{n,k}\) be the **primitive binary necklaces** of length \(n\) containing exactly \(k\) zeroes; rotations, but not reversal or complementation, are identified. Let \(C_{n,k}\) count necklaces for which the usual lexicographically least rotation (the Lyndon rotation) is also least under the alternating order (the Galois rotation). At the first differing position, the alternating order compares \(0<1\) at odd **one-based** positions and \(1<0\) at even positions.

For the generating functions below set \(C_{n,k}=0\) outside the range \(n>k\). The same-rotation coincidence statistic has the following exact and asymptotic profile:

1. For every \(n\ge2\), \(C_{n,1}=1\). For two and three zeroes, respectively,
   \[
   \sum_{n\ge0}C_{n,2}z^n=\frac{z^5}{(1-z)(1-z^4)},\qquad
   \sum_{n\ge0}C_{n,3}z^n=\frac{z^7}{(1-z)^2(1-z^6)}.
   \]
   In particular, \(C_{n,2}=\lfloor(n-1)/4\rfloor\) for \(n\ge3\), and
   \[
   C_{n,3}=\sum_{j\ge0}\max\{n-6-6j,0\}\quad(n\ge4).
   \]
2. For every **fixed integer** \(k\ge2\), if \(U_{n,k}\) counts primitive necklaces whose circular gaps between successive zeroes are strictly positive and whose *unique smallest gap* is odd, then
   \[
   \sum_{n\ge0}U_{n,k}z^n
     =\frac{z^{3k-1}}{(1-z)^{k-1}(1-z^{2k})},\qquad
   U_{n,k}\le C_{n,k}=U_{n,k}+O_k(n^{k-2}).
   \]
   Consequently, with \(P_{n,k}=|\mathcal P_{n,k}|\),
   \[
   C_{n,k}=\frac{n^{k-1}}{2k!}+O_k(n^{k-2}),\qquad
   P_{n,k}=\frac{n^{k-1}}{k!}+O_k(n^{k-2}),\qquad
   \lim_{n\to\infty}\frac{C_{n,k}}{P_{n,k}}=\frac12.
   \]
3. At positive zero density the conclusion reverses: for any integer sequence \(k_n\) with \(k_n/n\to\alpha\in(0,1)\),
   \[
   \frac{C_{n,k_n}}{P_{n,k_n}}\longrightarrow0
   \]
   **exponentially fast**. For \(k>n/2\), in fact \(C_{n,k}=0\).

This gives a sparse-to-dense distinction for the coincidence of two natural canonical rotations, rather than an estimate of either canonicalization in isolation.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\) with \(0<1\). A length-\(n\) word is primitive if its \(n\) rotations are all distinct. The usual minimum of a primitive rotation class is its unique Lyndon representative; the alternating minimum is its unique Galois representative. The comparison is performed on equal-length rotations; hence no prefix convention is needed. The number \(k\) is the number of zeroes, not of ones. The parameter \(k\) is fixed in the half-limit, whereas \(k/n\) tends to a strictly positive constant in the density-zero limit.

For a necklace with no cyclic occurrence of \(00\), put \(m=n-k\), and encode it by a circular ordered \(k\)-tuple \((g_1,\ldots,g_k)\) of **positive** integers summing to \(m\): the gap \(g_i\) is the number of consecutive ones after the \(i\)-th zero and before the next zero. Cyclically shifting the tuple corresponds exactly to shifting the starting zero. A necklace with a unique smallest gap is automatically primitive.

## Proof

**1. Exclusion of adjacent zeroes.** Every nonconstant circular binary word contains both a cyclic \(00\), if one exists, and a cyclic \(01\). The Lyndon rotation begins with \(00\) when a cyclic \(00\) exists. In the alternating order, among zero-start rotations, a rotation beginning \(01\) is smaller than one beginning \(00\), because position two is compared in reverse. Thus no necklace with a cyclic \(00\) is counted by \(C_{n,k}\).

**2. Gap-parity lemma.** Suppose all circular gaps are positive and \(k\ge2\). Compare two zero-start rotations whose initial gaps are \(a<b\). Both begin with \(0\) followed by \(a\) copies of \(1\). The first differing position is \(a+2\) (one-based): the shorter-gap rotation has \(0\) and the longer-gap rotation has \(1\). The shorter-gap rotation is always lexicographically smaller. It is alternating-order smaller precisely when \(a\) is odd. If the smallest gap is even, the primitive necklace has some larger gap (otherwise all gaps are equal and the word repeats a shorter block); therefore its Lyndon and Galois rotations differ. If the smallest gap is odd and occurs exactly once, its zero-start rotation defeats all others in both orders. The first letter eliminates all one-start rotations. Therefore unique positive odd minimum gaps are sufficient for coincidence; even minimum gaps, and zero gaps, are impossible.

**3. Exact two- and three-zero cases.** For \(k=1\), the sole zero fixes the same unique starting position for both orders, independently of the gap's parity. For \(k=2\), a primitive gap pair is unequal, and by step 2 agreement occurs precisely when the smaller gap \(a\) is odd. Writing \(a=1+2j\), the larger gap can be any \(b\ge a+1\), so the length is \(n=2+a+b\ge5+4j\). Summing over \(j\ge0\) and the extra length gives \(z^5/((1-z)(1-z^4))\).

For \(k=3\), with a positive odd minimum \(a\), either it is unique, or precisely two of the three gaps are \(a\) and the third is larger. In the tied case the Lyndon gap order is \((a,a,b)\), rather than \((a,b,a)\). Those two corresponding word rotations first differ at one-based position \(2a+3\), which is always odd; the Lyndon choice is consequently also the alternating choice. The all-equal case is nonprimitive. Hence for exactly three zeroes coincidence is **equivalent** to having a positive odd smallest gap. Put \(M=m-3a\). For \(M\ge1\), the three-gap necklaces with minimum exactly \(a\) consist of one repeated-minimum configuration \((a,a,a+M)\) and \(M-1\) unique-minimum configurations \((a,a+u,a+v)\), where \(u,v\ge1\) and \(u+v=M\). Thus there are \(M\) such necklaces. As \(n=3+3a+M\), summing \(\sum_{M\ge1}Mz^{3+3a+M}\) for \(a=1,3,5,\ldots\) yields \(z^7/((1-z)^2(1-z^6))\), and its stated coefficient formula.

**4. Unique-minimum enumeration for arbitrary fixed \(k\).** Anchor each eligible circular \(k\)-tuple at its unique smallest gap \(a=1+2j\). Its remaining \(k-1\) gaps are independently at least \(a+1\). Every anchored tuple specifies exactly one primitive necklace. Since the entire binary word length is \(n=k+\sum_i g_i\), its length-generating function is
\[
\sum_{j\ge0}\frac{z^{k+ka+(k-1)}}{(1-z)^{k-1}}
=\frac{z^{3k-1}}{(1-z)^{k-1}(1-z^{2k})}.
\]
The only possible remaining coincident necklaces have a tied positive odd minimum. Such circular gap vectors satisfy one equality between two of the \(k\) gaps, in addition to their fixed-sum constraint, and hence number \(O_k(n^{k-2})\). This counts rotations at most a fixed \(k\)-fold factor and is an upper bound even when some tuples are nonprimitive. Thus \(0\le C_{n,k}-U_{n,k}=O_k(n^{k-2})\).

For fixed \(k\), the generating function above has coefficient
\[
U_{n,k}=\frac{n^{k-1}}{2k!}+O_k(n^{k-2}).
\]
Indeed, its pole at \(z=1\) is of order \(k\) with leading coefficient \(1/(2k)\); the other \((2k)\)-th roots of unity contribute only \(O_k(n^{k-2})\), and the remaining binomial-coefficient expansion has the same error. The standard primitive fixed-content necklace count follows directly by Möbius inversion:
\[
P_{n,k}=\frac1n\sum_{d\mid\gcd(n,k)}\mu(d)\binom{n/d}{k/d}.
\]
Its \(d=1\) term is \(n^{k-1}/k!+O_k(n^{k-2})\); every \(d\ge2\) term is lower order. This proves the fixed-\(k\) half-limit.

**5. Positive-density exclusion.** For \(1\le k\le n/2\), the number of *indexed* circular binary words avoiding cyclic \(00\) is
\[
A_{n,k}=\frac{n}{n-k}\binom{n-k}{k}.
\]
To see this, an indexed word together with a distinguished zero is counted by choosing its distinguished zero position in \(n\) ways and choosing one of \(\binom{n-k-1}{k-1}\) positive gap compositions. Each indexed word has exactly \(k\) choices of distinguished zero, giving \(A_{n,k}=\frac{n}{k}\binom{n-k-1}{k-1}\), equal to the displayed formula. More directly, the ratio to all \(\binom nk\) indexed words satisfies
\[
\frac{A_{n,k}}{\binom nk}
=\frac{n}{n-k}\prod_{j=0}^{k-1}\frac{n-k-j}{n-j}
\le\frac{n}{n-k}\exp(-k^2/n).
\]
Since every coincident primitive necklace avoids cyclic \(00\), \(nC_{n,k}\le A_{n,k}\). At \(k/n\to\alpha\in(0,1)\), the nonprimitive indexed words form an exponentially negligible proportion of all \(\binom nk\) words: proper repetitions have multiplicity \(d\ge2\) and contribute at most \(\sum_{d\mid\gcd(n,k),\ d\ge2}\binom{n/d}{k/d}\), exponentially smaller than \(\binom nk\) by the binomial entropy estimate for fixed \(\alpha\). Hence the number of primitive indexed words is asymptotic to \(\binom nk\), and \(C_{n,k}/P_{n,k}\) is exponentially small for \(0<\alpha\le1/2\). If \(k>n/2\), at least two cyclic zeroes must be adjacent, making coincidence impossible. This proves the dense regime.

## Verification

The accompanying standalone Python program `verify.py` constructs full cyclic rotation classes directly, compares the two minima under the specified one-based alternating convention, and checks the Möbius primitive-count formula, the exact \(k=2,3\) formulas, the unique-odd-gap generating-function coefficients, and the circular-adjacency count. It performs deterministic finite checks for \(2\le n\le24\) and \(1\le k\le5\), independently deriving both minima from the actual rotations. See `VERIFICATION.md` for the result. The all-length conclusions rely on steps 1–5 of this proof, not on finite enumeration.

## Relationship to prior work

Hendrian, Köppl, Yoshinaka and Shinohara, *Algorithms for Galois Words: Detection, Factorization, and Rotation*, arXiv:2403.02636 (first public March 5, 2024), define the relevant alternating minimum and prove algorithms for obtaining it. Their Sections 2 and 7 treat efficient computation and their Section 8 reports factorization experiments, not a distribution of coincidences with ordinary Lyndon rotations. Dolce, Restivo and Reutenauer, *On generalized Lyndon words*, arXiv:1812.04515 (first public December 11, 2018), establish general factorization and Galois-characterization results, but do not give this fixed-content coincidence profile. Reutenauer's *Mots de Lyndon généralisés* is foundational for alternating Lyndon orders and their cyclic representatives; its Galois-number interpretation does not provide the counts proved here.

The primitive necklace Möbius formula is classical background and not claimed new. The claim here is specifically the intersection of the two canonical representatives, its exact low-zero-weight enumeration, and its sparse-versus-dense behavior. Searches and comparisons did not reveal the same result, but absence from indexed sources is not proof of priority.

## Limitations

The complete finite-length coincidence count is proved here only for \(k=1,2,3\); for fixed \(k\ge4\) the theorem gives an exact unique-minimum subfamily and a sharp leading asymptotic, **not** an exact all-necklace count. No uniform transition is asserted for intermediate regimes \(k\to\infty\) with \(k=o(n)\). The density theorem concerns primitive binary necklaces and exact agreement of the two selected rotations; it does not measure edit or cyclic distance between the selected rotations. An independently adjudicated literature-priority determination remains outstanding.

## References

- D. Hendrian, D. Köppl, R. Yoshinaka, A. Shinohara, *Algorithms for Galois Words: Detection, Factorization, and Rotation*, arXiv:2403.02636 (first public 2024-03-05); CPM 2024, LIPIcs 296, Article 18. https://arxiv.org/abs/2403.02636 ; https://doi.org/10.4230/LIPIcs.CPM.2024.18
- F. Dolce, A. Restivo, C. Reutenauer, *On generalized Lyndon words*, arXiv:1812.04515 (first public 2018-12-11); Theoretical Computer Science 777 (2019), 232–242. https://arxiv.org/abs/1812.04515
- C. Reutenauer, *Mots de Lyndon généralisés*, Séminaire Lotharingien de Combinatoire 54, Article B54h (2006). https://www.mat.univie.ac.at/~slc/s/s54reut.pdf
