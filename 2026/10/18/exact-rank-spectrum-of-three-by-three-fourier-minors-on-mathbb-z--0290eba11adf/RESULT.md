# Exact rank spectrum of three-by-three Fourier minors on \(\mathbb Z_{3p}\)

## Finding
For each prime \(p\ge5\), identify the odd semiprime cyclic group with \(G=\mathbb Z_3\times\mathbb Z_p\). Its unnormalized complex Fourier character matrix is
\[
F_{(a,b),(u,v)}=\exp(2\pi i au/3)\exp(2\pi i bv/p).
\]
Let \(R,C\subset G\) be any sets of three distinct indices. A three-element set is **3-pure** if all its first coordinates are equal and **\(p\)-pure** if all its second coordinates are equal. It is **3-colliding**, respectively **\(p\)-colliding**, if at least two of its first, respectively second, coordinates agree.

**Exact classification.** The minor \(F[R,C]\) is singular if and only if at least one of the following four conditions holds:

1. \(R\) is 3-pure and \(C\) is \(p\)-colliding;
2. \(C\) is 3-pure and \(R\) is \(p\)-colliding;
3. \(R\) is \(p\)-pure and \(C\) is 3-colliding;
4. \(C\) is \(p\)-pure and \(R\) is 3-colliding.

The rank is **one** if and only if \(R\) is 3-pure and \(C\) is \(p\)-pure, or vice versa. Every other singular minor has rank **two**.

Set \(T=\binom{3p}{3}\). Among all \(T^2\) ordered pairs of *unordered* three-element row and column sets, the exact counts \(N_j\) of rank \(j\) are
\[
\boxed{N_1=p^2(p-1)(p-2),\qquad N_2=3p^2(p-1)(3p^2-7p+6),}
\]
\[
\boxed{N_3=T^2-p^2(p-1)(9p^2-20p+16).}
\]
Thus the number of singular minors is exactly \(p^2(p-1)(9p^2-20p+16)\).

## Assumptions and scope
The prime \(p\) is at least five. Every rank, proportionality, and determinant is over \(\mathbb C\), not a finite field. No equal-amplitude, real-coefficient, or positivity restriction is assumed. Each row set and each column set has three *distinct* elements; the ordered pair \((R,C)\) distinguishes the roles of rows and columns. Fourier normalization and the choice of sign in the exponential do not alter ranks. The Chinese-remainder isomorphism \(\mathbb Z_{3p}\cong G\) identifies character tables up to index permutation.

## Proof
**1. Rigidity of unimodular three-by-three matrices (known elementary fact).** Every entry of \(F\) has modulus one. Multiplying three rows and three columns by nonzero unimodular constants reduces any selected minor to
\[
M=\begin{pmatrix}1&1&1\\1&u&v\\1&w&t\end{pmatrix},\qquad |u|=|v|=|w|=|t|=1.
\]
Singularity is equivalent to \((u-1)(t-1)=(v-1)(w-1)\). If both products are nonzero, conjugate this identity and use \(\overline{z-1}=-(z-1)/z\) for unimodular nonzero \(z\); division yields \(ut=vw\). Expanding the original identity then gives \(u+t=v+w\). Equal sums and products force the multisets \(\{u,t\}\) and \(\{v,w\}\) to coincide, hence either the second and third rows or the second and third columns coincide. If the products vanish, checking the four possibilities directly yields two proportional rows or two proportional columns. Conversely, such a proportional pair always makes the determinant vanish. Therefore, **a three-by-three matrix with unimodular entries is singular exactly when it has a proportional row pair or a proportional column pair.** This rigidity lemma is not asserted as a novel contribution.

**2. Classification by annihilators.** For two distinct row indices \(x,x'\in G\), the corresponding restricted rows are proportional precisely when \(\chi_c(x-x')\) is constant as \(c\) ranges over the three selected columns. Equivalently, all column differences belong to the annihilator \((x-x')^\perp\) in \(G\). If \(x-x'\) has order \(3p\), its annihilator is trivial and cannot contain differences between three distinct columns. If it has order \(3\), its annihilator is \(\{0\}\times\mathbb Z_p\); the two rows agree in their \(p\)-coordinate, and all columns must be 3-pure. If it has order \(p\), its annihilator is \(\mathbb Z_3\times\{0\}\); the two rows agree in their 3-coordinate, and all columns must be \(p\)-pure. Transposing yields the same alternatives with rows and columns interchanged. This proves the four singularity conditions.

Rank one requires all three selected rows to be proportional. Since a 3-pure triple has three distinct \(p\)-coordinates, and a \(p\)-pure triple consists of the three different 3-coordinates, the annihilator characterization gives rank one precisely when a 3-pure row triple meets a \(p\)-pure column triple, or conversely. To see there are no other rank-one cases, if two row differences had nontrivial annihilators of distinct prime orders, the selected column differences would have to lie in their trivial intersection, contradicting the three distinct columns. All remaining singular matrices therefore have rank two.

**3. Incidence count.** Let \(H=\binom p3\). There are \(3H\) 3-pure triples, and \(p\) \(p\)-pure triples; these classes are disjoint because each triple has three distinct group elements. The number of \(p\)-colliding triples is \(p+9p(p-1)\): either all three have the same \(p\)-coordinate (\(p\) choices), or exactly two have that coordinate (choose that coordinate, the other coordinate, the two points from its three-point fiber, and the remaining point, giving \(p(p-1)\binom32\cdot3=9p(p-1)\)). The number of 3-colliding triples is \(T-p^3\), since choosing one point in each of the three 3-coordinate fibers yields \(p^3\) triples with no collision.

Count the four singularity events by inclusion-exclusion. The sum of their sizes is
\[
2(3H)\bigl(p+9p(p-1)\bigr)+2p(T-p^3).
\]
Only two pairwise intersections are possible: 3-pure rows with \(p\)-pure columns simultaneously satisfy the first and fourth conditions, and the transposed configuration satisfies the second and third. Both intersections have size \(3Hp\); all other intersections, and all triple intersections, are empty. Consequently
\[
N_1+N_2=2(3H)\bigl(p+9p(p-1)\bigr)+2p(T-p^3)-6Hp
=p^2(p-1)(9p^2-20p+16).
\]
There are exactly \(N_1=2(3H)p=p^2(p-1)(p-2)\) rank-one pairs. Subtraction gives \(N_2=3p^2(p-1)(3p^2-7p+6)\). The remaining \(T^2-N_1-N_2\) pairs have rank three. This proves the formulas for **every** prime \(p\ge5\).

## Verification
The companion standalone standard-library Python program `checker.py` exhausts all \(T^2\) row-set/column-set pairs for \(p=5\) and \(p=7\). It independently computes rank over a finite field containing an element of exact order \(3p\), by testing the normalized determinant and all four multiplicative entries; separately it checks the four congruence conditions and closed-form counts. It passed both checks:

- \(p=5\): \(N_1=300\), \(N_2=13{,}800\), \(N_3=192{,}925\).
- \(p=7\): \(N_1=1{,}470\), \(N_2=91{,}728\), \(N_3=1{,}675{,}702\).

Reproduce with `python3 checker.py`. Calculations in a finite field do **not** establish complex nonvanishing for arbitrary primes; the all-prime theorem follows from the analytic rigidity lemma, group annihilators, and exact combinatorial counting above.

## Relationship to prior work
Chebotarev's prime-order minor nonvanishing theorem and Tao's prime-order Fourier uncertainty theorem motivate examining composite lengths; they do not classify arbitrary three-by-three minors of order \(3p\). Delvaux and Van Barel analyze maximal rank-deficient submatrices of Kronecker Fourier matrices and their subgroup/tiling construction, covering important constituent rank-defect structures, but the inspected results do not give the present complete **rank-one/rank-two/full-rank incidence count**. Loukaki proves useful nonvanishing criteria for the square-free cyclic order \(pq\), while Caragea and Lee treat principal minors; neither directly provides arbitrary nonprincipal three-by-three rank multiplicities.

Published classifications of all three-by-three minors of the **different groups** \(\mathbb F_p^2\), \(\mathbb Z_{p^2}\), and \(\mathbb Z_{2p}\) are close analogues. The first two have repeated-prime structure; the third has only rank-two singular minors, whereas the odd-squarefree family here has a nonzero rank-one stratum. The elementary unit-modulus lemma used in the proof already appears in the \(\mathbb F_p^2\) classification and is reused, not presented as original. The asserted contribution is the entire order-\(3p\) classification and its distinct closed count.

## Limitations
The theorem concerns only three-by-three submatrices, only complex Fourier matrices, and only the family \(3p\) with prime \(p\ge5\). Finite modular tests are evidence for two sample orders, not proof of the infinite statement. The structure follows by applying an established elementary lemma to this group and performing a dedicated exhaustive symbolic incidence count. An earlier equivalent enumeration, or a hidden corollary of more general maximal-rank-defect literature, may exist despite the specific comparisons. No independent scientific audit has been performed.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first submitted 2003-08-29, https://arxiv.org/abs/math/0308286.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, technical report TW477 (November 2006), https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.pdf; journal version, Linear Algebra Appl. 426 (2007), 349–367.
3. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first submitted 2010-03-26, https://arxiv.org/abs/1003.5060.
4. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, https://arxiv.org/html/2409.09793v4.
5. M. Loukaki, *Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle*, arXiv:2412.08600v1, https://arxiv.org/abs/2412.08600.
6. *Complete three-by-three Fourier-minor rank geometry on prime affine planes*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-three-by-three-fourier-minor-rank-geometry-on-prime-aff--ba0b52ec4cec.
7. *Singular three-by-three Fourier minors on even semiprime cycles*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-three-by-three-fourier-minors-on-even-semiprime-cycles--8f025c6183d3.
