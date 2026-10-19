# Exact exponential-spectrum multiplicities at the least-prime cardinality of squarefree cyclic groups

## Finding
Let \(N=p r_1\cdots r_t\), where \(t\geq1\) and \(p<r_1<\cdots<r_t\) are distinct primes, and put \(Q=N/p\). A **spectral pair** is an ordered pair of subsets \(A,B\subset\mathbb Z_N\), both of cardinality \(p\), for which the matrix \(\big(e^{2\pi iab/N}\big)_{a\in A,b\in B}\) has pairwise orthogonal columns. Write \(A_r\) for the image of \(A\) modulo a prime \(r\mid N\).

**Classification.** The pair \((A,B)\) is spectral if and only if both \(A_p\) and \(B_p\) contain all \(p\) residues, and for each \(r\mid Q\), at least one of \(A_r\), \(B_r\) is a singleton. In particular, an individual \(p\)-set \(A\) is spectral if and only if \(A_p=\mathbb Z_p\).

**All spectrum multiplicities.** For a spectral set \(A\), define \(S(A)=\{r\mid Q:\,|A_r|=1\}\). The number of literal frequency subsets \(B\) that are spectra for this fixed \(A\) is exactly
\[
\mathcal M(A)=Q\prod_{r\in S(A)}r^{p-1}.
\]
Every one of the \(2^t\) values obtained by varying \(S(A)\) occurs, and they are all distinct. The number of spatial sets \(A\) giving a specified \(S\subseteq\{r_1,\ldots,r_t\}\) is
\[
\mathcal N(S)=\prod_{r\in S}r\prod_{r\mid Q,\,r\notin S}(r^p-r).
\]
Consequently the exact number of **ordered spectral pairs of literal subsets** is
\[
\boxed{\displaystyle \#\{(A,B)\text{ spectral},\ |A|=|B|=p\}
=Q\prod_{r\mid Q}(2r^p-r).}
\]
For example, at \(N=30\) the four positive spectrum multiplicities are \(15,45,75,225\), occurring on respectively \(120,60,30,15\) spatial two-sets. The remaining \(210\) two-sets have no spectrum. There are exactly \(10125\) ordered spectral pairs.

## Assumptions and scope
The primes are distinct and \(p\) is the **least** prime divisor of the squarefree integer \(N\). The theorem counts each spatial/frequency subset literally; it does not quotient by translation, group automorphisms, or interchange of \(A\) and \(B\). The Fourier pairing is normalized only when calling the \(p\times p\) character matrix unitary: orthogonal columns have squared norm \(p\), so division by \(\sqrt p\) yields a unitary matrix. The Chinese remainder theorem identifies \(\mathbb Z_N\) and its character group with the products of the corresponding prime-coordinate groups; the standard pairing differs from the componentwise pairing only by invertible coordinate rescalings in the frequency variable. In particular, whether a frequency coordinate is zero is invariant under the choice.

## Proof
**1. A short vanishing-sum lemma.** Suppose that \(d\) is squarefree, all of its prime divisors are at least \(p\), and \(1\leq L\leq p\). If \(d\)-th roots of unity \(\xi_1,\ldots,\xi_L\), counted with multiplicity, satisfy \(\sum_{j=1}^{L}\xi_j=0\), then \(L=p\), the prime \(p\) divides \(d\), and the multiset of the \(\xi_j\) is a scalar multiple of the complete set of \(p\)-th roots of unity.

Here is a proof by induction on the number of prime factors of \(d\). For prime \(d=s\), a polynomial with nonnegative integral coefficients and degree less than \(s\) vanishes at a primitive \(s\)-th root only when all its \(s\) coefficients are equal, by the minimal polynomial \(1+X+\cdots+X^{s-1}\). Thus a nonempty vanishing sum of at most \(p\leq s\) terms exists only for \(s=p=L\), with each root once. The case \(d=1\) is impossible. For composite \(d\), choose a prime \(s\mid d\) with \(s>p\), and decompose each \(d\)-th root into an \(s\)-th root times a \((d/s)\)-th root. There are at most \(p<s\) occupied \(s\)-fibers. Since \(\Phi_s\) has degree \(s-1\) over \(\mathbb Q(\zeta_{d/s})\) (coprime cyclotomic conductors), the vanishing sum forces every fiber sum to vanish separately: its coefficient polynomial must be a scalar multiple of \(1+\cdots+X^{s-1}\), and an unoccupied fiber makes the scalar zero. By induction, every nonempty fiber then needs at least \(p\) terms. As there are at most \(p\) altogether, exactly one fiber is occupied, containing \(p\) roots constituting a rotated \(p\)-cycle. This proves the lemma. (If \(d\) is composite with all primes \(\geq p\), such an \(s>p\) exists because \(d\) is squarefree.)

**2. Fourier zero criterion.** Let \(|A|=p\) and \(\chi\) be a character of \(\mathbb Z_N\). By the lemma applied to the order of \(\chi\),
\[
\sum_{a\in A}\chi(a)=0
\quad\Longleftrightarrow\quad
\begin{cases}
\chi_p\ne1,\quad A_p=\mathbb Z_p,\\
\chi_r=1\ \text{or}\ |A_r|=1,\quad\text{for every prime }r\mid Q.
\end{cases}
\]
Indeed, a vanishing sum of \(p\) character values must be a complete rotated \(p\)-cycle. Thus the character has nontrivial \(p\)-component, the \(p\)-coordinates of \(A\) are distinct, and every coordinate where the character is nontrivial at \(r>p\) is constant on \(A\). Conversely, these conditions make all the \(r>p\) character factors constant on \(A\) and leave the full vanishing sum of \(p\)-th roots in the \(p\)-coordinate.

**3. Orthogonality and classification.** Column orthogonality is equivalent to \(\sum_{a\in A}\chi_{b-b'}(a)=0\) for every two distinct \(b,b'\in B\). The criterion forces \(A_p=\mathbb Z_p\) and forces every difference \(b-b'\) to have nonzero \(p\)-coordinate; hence \(B_p=\mathbb Z_p\). For any \(r\mid Q\) with nonconstant \(A_r\), the criterion forces \(b_r=b'_r\) for every pair \(b,b'\), i.e. \(B_r\) is constant. These are exactly the stated conditions, and the converse follows directly by applying the same zero criterion to every column pair. Since a \(p\times p\) character matrix with mutually orthogonal nonzero columns is an orthogonal basis, this is precisely the spectral-pair property.

**4. Counting without overcounting.** Fix \(A\) with \(A_p=\mathbb Z_p\). Every spectrum \(B\) has exactly one point with each prescribed \(p\)-coordinate. At a prime \(r\notin S(A)\), all of these points must have the same \(r\)-coordinate, giving \(r\) choices. At \(r\in S(A)\), the \(p\) coordinates of \(B\) can be chosen independently, giving \(r^p\) choices. Each such coordinate specification determines exactly one literal subset by the Chinese remainder theorem. Thus \(\mathcal M(A)=\prod_{r\notin S(A)}r\prod_{r\in S(A)}r^p=Q\prod_{r\in S(A)}r^{p-1}\).

For fixed \(S\), at each prime in \(S\), the coordinate function \(A_p\to\mathbb Z_r\) has \(r\) constant choices; outside \(S\) it has \(r^p-r\) nonconstant choices. This gives \(\mathcal N(S)\). Every \(\mathcal N(S)\) is positive. Distinct sets \(S\) have distinct products of their primes, so their multiplicities are distinct. Finally,
\[
\sum_{S}\mathcal N(S)\mathcal M(S)
=\prod_{r\mid Q}\big((r^p-r)r+r\,r^p\big)
=Q\prod_{r\mid Q}(2r^p-r).
\]
This exhausts all ordered pairs and completes the proof.

## Verification
The accompanying `verify_squarefree_spectra.py` computes exact reductions modulo the cyclotomic polynomial \(\Phi_N\), with no floating-point tolerance. It exhaustively compares the direct Fourier-column orthogonality test against the theorem for \(N=6,15,30\); obtains ordered-pair totals \(45,1225,10125\), respectively; and checks the predicted full multiplicity histograms. For \(N=105\), it additionally checks \(1700\) exact randomly selected Fourier-zero instances and \(250\) exact randomly selected pairs. The seeded tests are corroboration; the universal result rests on the preceding proof, not extrapolation.

Run `python verify_squarefree_spectra.py` with Python 3 and SymPy. The script prints `VERIFY_OK` after all assertions succeed.

## Relationship to prior work
Zhou's study of principal nonsingularity of finite Fourier matrices (first public version 2025-05-02, arXiv:2505.01189) addresses *invertibility of principal minors* and conditions for Riesz bases, not the unitary condition for arbitrary paired minor indices, nor counts of all spectra of a fixed support. The present exact classification concerns orthogonal \(p\times p\) submatrices, including independent row and column sets.

Tan and Zhang's 2026 treatment of Fuglede's conjecture for squarefree cyclic groups (arXiv:2610.02218) establishes the criterion for an individual set to have some spectrum. For prime cardinality, this provides the existence-level context, but existence alone does not determine **which** spectra occur, their \(2^t\) possible multiplicities, or the ordered-pair product count. The full text of that recent paper was not accessible for a complete priority comparison, so overlap in uninspected details remains possible.

The public result *Exact spectrum multiplicities for four-point spectral sets in \(\mathbb Z_{4p}\)* concerns a **non-squarefree** modulus and four-point supports, giving three multiplicity strata. Its explicit result is not an implication covering all least-prime-cardinality spectra on arbitrary squarefree cyclic groups. General cyclic spectral-set and tiling work, including Malikiosis's 2022 paper, provides background on character orthogonality and spectral pairs, but a stronger previous theorem under alternative terminology may exist.

## Limitations
The theorem assumes squarefree order and support cardinality exactly equal to its smallest prime factor. It does not treat composite cardinalities, nonsquarefree cyclic groups, or approximate/Riesz spectral bases. Spectra are counted as literal subsets rather than equivalence classes, and the reported priority assessment is bounded by the inspected literature; no independent audit is claimed.

## References
1. W. Zhou, *Principal Non-singularity of Fourier Matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189, first submitted 2025-05-02; Demonstratio Mathematica 59 (2026), DOI:10.1515/dema-2025-0242.
2. H. Tan and Y. Zhang, *Fuglede's Conjecture for Cyclic Groups of Square-free Order*, arXiv:2610.02218, first-public bibliographic date 2026-09-09.
3. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma (2022), DOI:10.1017/fms.2022.14; arXiv:2005.05800.
4. *Exact spectrum multiplicities for four-point spectral sets in \(\mathbb Z_{4p}\)*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-spectrum-multiplicities-for-four-point-spectral-sets-in-ma--41b784251307.
