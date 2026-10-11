# Exact positional Fourier-support incidence on the cyclic nine-point group

## Finding
Let \(G=\mathbb Z/9\mathbb Z\), let \(\zeta=e^{2\pi i/9}\), and use the unnormalized Fourier transform \(\widehat f(y)=\sum_{x\in G}f(x)\zeta^{xy}\) for functions \(f:G\to\mathbb C\). For \(1\le a,b\le9\), define
\[
I_9(a,b)=\#\{(A,B): A,B\subseteq G,\ |A|=a,\ |B|=b,\ \exists f:\operatorname{supp}f=A,\ \operatorname{supp}\widehat f=B\}.
\]
The exact positional-support incidence matrix, with row index \(a\) and column index \(b\), is
\[
\left(\begin{array}{rrrrrrrrr}
0&0&0&0&0&0&0&0&9\\
0&0&0&0&0&27&0&243&36\\
0&0&9&0&0&9&2430&729&84\\
0&0&0&0&486&7857&4131&1134&126\\
0&0&0&486&11259&9288&4374&1134&126\\
0&27&9&7857&9288&6732&2997&756&84\\
0&0&2430&4131&4374&2997&1296&324&36\\
0&243&729&1134&1134&756&324&81&9\\
9&36&84&126&126&84&36&9&1
\end{array}\right).
\]
Consequently, **exactly \(92{,}236\)** of the \((2^9-1)^2=261{,}121\) ordered nonempty time/frequency support-set pairs occur.

Under the affine action
\[
(A,B)\longmapsto(uA+a,\,u^{-1}B+b),\qquad
u\in(\mathbb Z/9\mathbb Z)^\times,\quad a,b\in G,
\]
these realizable pairs form **exactly \(302\) orbits**. Their orbit-size distribution (size:number) is
\[
1:1,\ 3:4,\ 9:12,\ 18:4,\ 27:20,\ 54:10,\ 81:10,\ 162:6,\ 243:103,\ 486:132.
\]
Adjoining Fourier duality \((A,B)\mapsto(B,-A)\) yields **exactly \(158\) orbits**, with size distribution
\[
1:1,\ 6:2,\ 9:2,\ 18:5,\ 36:2,\ 54:10,\ 81:2,\ 108:5,\ 162:4,\ 243:9,\ 324:3,\ 486:47,\ 972:66.
\]
In particular, the \(486\) realizable support pairs of sizes \((4,5)\) form a *single* affine orbit: the size-level boundary has a rigid positional realization.

## Assumptions and scope
The coefficient field is \(\mathbb C\); arbitrary complex nonzero amplitudes are allowed, without phase or sign restrictions. Support means the locations of *all and only* nonzero coefficients. Every \((A,B)\) is counted once as an ordered pair of actual index subsets. The transform uses plus sign and no normalization, which do not affect the existence of support pairs or the reported counts. The assertion is specific to the cyclic group of order nine, not the nonisomorphic group \((\mathbb Z/3\mathbb Z)^2\).

## Proof
**Exact-support criterion.** Fix nonempty \(A,B\subseteq G\), put \(R=G\setminus B\), and let \(M_{R,A}=(\zeta^{xy})_{y\in R,x\in A}\) over \(K=\mathbb Q(\zeta)\). Write \(r=\operatorname{rank}_K M_{R,A}\). There exists a function with exact supports \(A,B\) if and only if all three conditions hold:
\[
\begin{split}
r&<|A|,\\
\operatorname{rank}_K M_{R,A\setminus\{x\}}&=r\quad\text{for every }x\in A,\\
\operatorname{rank}_K M_{R\cup\{y\},A}&=r+1\quad\text{for every }y\in B.
\end{split}
\]
Indeed, the first condition makes \(L=\ker M_{R,A}\) a nonzero vector space. The second says that the coordinate functional at each \(x\in A\) is nonzero on \(L\), since the corresponding column lies in the span of the others. The third says that each wanted Fourier-coordinate functional is nonzero on \(L\). Because \(K\) is infinite, finitely many proper hyperplanes cannot cover \(L\), so one vector in \(L\) has every required time and Fourier coordinate nonzero. Conversely, failure of any condition forces a forbidden zero. This proves necessity and sufficiency for exact support, without a numerical tolerance.

**Exact cyclotomic ranks from two finite fields.** Here \(K\) has degree \(\varphi(9)=6\). Every square minor \(D\) of the Fourier matrix has order \(k\le9\) and is a cyclotomic integer. Each complex Galois conjugate of \(D\) is a determinant of a matrix with unit-modulus entries, so Hadamard's determinant inequality gives \(|\sigma(D)|\le k^{k/2}\). Therefore
\[
|N_{K/\mathbb Q}(D)|\le k^{3k}\le9^{27}=58149737003040059690390169.
\]
Use the distinct primes
\[
p_1=100000000000099,\qquad p_2=100000001000377,
\]
whose product is strictly greater than \(9^{27}\). For each prime choose a verified element \(r_i\in\mathbb F_{p_i}\) of multiplicative order nine, giving an evaluation homomorphism \(\mathbb Z[\zeta]\to\mathbb F_{p_i}\), \(\zeta\mapsto r_i\). For any minor, vanishing after this evaluation implies \(p_i\) divides its integer field norm. Thus, if a nonzero minor vanished in both finite fields, its nonzero norm would have absolute magnitude at least \(p_1p_2>9^{27}\), a contradiction. All reduction ranks cannot exceed characteristic-zero ranks, and some nonzero maximal minor survives at least one reduction. Hence **every submatrix rank over \(K\) equals the maximum of its two finite-field ranks**.

The accompanying arithmetic implementation verifies primality by complete trial division, confirms that its selected roots have order exactly nine, tabulates both ranks for all \(512^2\) pairs of row and column masks, and takes their maximum. It then applies the proved exact-support criterion to all \(511^2=261121\) ordered nonempty support pairs and sums by sizes. This gives the displayed \(9\times9\) integer matrix and total \(92236\), with no randomized sampling and no floating-point arithmetic.

**Orbit counts.** Time translation, modulation, and dilation of the input signal generate the displayed affine action. Since \(2\) generates the unit group modulo nine, two independent unit translations and the action \((A,B)\mapsto(2A,5B)\) generate it. Fourier inversion gives \(\widehat{\widehat f}(x)=9f(-x)\), so the additional transformation \((A,B)\mapsto(B,-A)\) also preserves realizability. The attached verifier forms the entire orbit of every unvisited realizable pair under the stated generators, explicitly checks that each generated pair is realizable, and counts disjoint orbit sizes. This produces the two orbit distributions and the single affine \((4,5)\) orbit; their weighted size sums independently equal \(92236\).

## Verification
Compile and execute the supplied standalone `checker.cpp` with a C++17 compiler, for example `g++ -std=c++17 -O3 checker.cpp -o checker && ./checker`. No external libraries, downloaded databases, tolerance thresholds, or third-party code are required. The program prints `PRIMES_VERIFIED`, its two primitive ninth roots, the complete incidence matrix, both orbit-size distributions, and `CHECK_PASS`. It verifies symmetry of the count matrix under Fourier duality and the weighted orbit checksums. All enumeration ranges are explicit, finite, and exhaustive.

## Relationship to prior work
Yang, Zhang, Wang, Geng and Chen (arXiv:2303.17203v1, 2023) study the *cardinality-level* uncertainty diagram of discrete Fourier matrices, with a rank criterion for existence. Their framework identifies **whether some** support pair of a specified cardinality occurs, but does not give the present *number of positional support pairs* for every cardinality pair or orbit counts. Bonami and Ghobber (arXiv:1003.5060v1, 2010) characterize minimizing-support extremals on cyclic prime-square groups; this controls the lower boundary but not the entire positional incidence matrix. Delvaux and Van Barel (KU Leuven report TW470, 2006) determine prime-power minimum Hamming weights using maximal rank-deficient blocks, not these incidence or orbit counts. The published three-by-three prime-square minor classification gives local small-minor ranks, but does not determine ranks of all rectangular Fourier submatrices needed for positional support incidence. The published order-eight incidence census addresses a different group and cannot imply these order-nine counts or orbits.

## Limitations
This is an exact finite classification for one group, not a formula for all odd prime powers. The proof of numerical counts is finite exhaustive computation, but is genuinely exhaustive over all support masks and is made exact by a rigorous cyclotomic-norm reduction certificate. The mathematical rank criterion and certification are proved; numerical totals rely on a replayable finite algorithm, not a compact hand derivation. As with any literature-based originality judgment, obscure earlier tables or differently indexed positional support computations could exist. Independent external review has not been performed.

## References
1. Y.-H. Yang, B.-B. Zhang, X.-L. Wang, S.-J. Geng, P.-Y. Chen, *Characterizing Kirkwood-Dirac nonclassicality and uncertainty diagram based on discrete Fourier transform*, arXiv:2303.17203v1, first public 2023-03-30. https://arxiv.org/abs/2303.17203
2. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first public 2010-03-26. https://arxiv.org/abs/1003.5060
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, KU Leuven Report TW470, September 2006. https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.pdf
4. *All singular three-by-three minors of prime-square Fourier matrices*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b
5. *Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-support-pattern-incidence-refinement-of-the-order-eight-fourier--78caf4d7929b
