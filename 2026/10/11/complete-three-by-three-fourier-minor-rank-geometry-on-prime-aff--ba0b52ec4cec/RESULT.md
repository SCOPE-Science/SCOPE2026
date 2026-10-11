# Complete three-by-three Fourier-minor rank geometry on prime affine planes

## Finding
Fix any prime \(p\ge3\), let \(V=\mathbb F_p^2\), and form the unnormalized character matrix
\[
F_p=(\exp(2\pi i\,a\cdot b/p))_{a,b\in V}.
\]
For distinct three-element subsets \(A,B\subset V\), put \(F_p[A,B]\) for the selected three-by-three matrix. A three-point set is **linear** if it lies on an affine line and **triangular** otherwise. The complete ranks are characterized by the following mutually exhaustive geometric rules:

1. If both \(A\) and \(B\) are triangular, the rank is \(3\).
2. If \(A\) is triangular and \(B\) is linear with direction \(w\ne0\), the rank is \(2\) exactly when \(w\cdot(a-a')=0\) for some two distinct \(a,a'\in A\), and otherwise is \(3\). The transposed rule applies when \(A\) is linear and \(B\) triangular.
3. If both are linear, with respective directions \(v,w\ne0\), the rank is \(1\) if \(v\cdot w=0\) and \(3\) otherwise. In general, for every linear \(A\) with direction \(v\), the rank is \(1\), \(2\), or \(3\) according as the three projected values \(v\cdot b\) have one, two, or three distinct values.

Let
\[
T=\binom{p^2}{3},\qquad C=\binom p3,\qquad L=p(p+1)C,\qquad U=T-L,\qquad K=pC.
\]
Among the \(T^2\) ordered pairs \((A,B)\) of unordered three-point sets, the exact numbers \(R_j\) of rank \(j\) are
\[
\boxed{R_1=LK,\quad R_2=3UK+L(T-p^3C-K),\quad
R_3=U(T-3K)+Lp^3C.}
\]
For a fixed triangular \(A\), exactly \(3K\) column triples are singular and each has rank \(2\). For a fixed linear \(A\), exactly \(p^3C\) are nonsingular, exactly \(K\) have rank \(1\), and the other \(T-p^3C-K\) have rank \(2\).
The rank-deficient counts also simplify to
\[
R_1=\frac{(p+1)p^4(p-1)^2(p-2)^2}{36},\qquad
R_2=\frac{(p+1)p^5(p-1)^3(p-2)}6.
\]
For \(p=3\), the rank multiplicities are \((36,1296,5724)\); for \(p=5\) they are \((15000,600000,4675000)\).

## Assumptions and scope
All ranks are ordinary complex matrix ranks; no normalization affects them. The row and column supports are unordered sets of exactly three distinct elements, but an *ordered pair* means that the row-set and column-set positions are distinguished. The dot product is the standard nondegenerate bilinear pairing over \(\mathbb F_p\). A direction is a one-dimensional linear subspace, unaffected by rescaling a nonzero direction vector. The theorem holds for every prime \(p\ge3\), not merely those computationally checked.

## Proof
**Step 1: elementary unit-modulus determinant rigidity.** Let \(M\) be any three-by-three complex matrix whose nine entries have absolute value one. Multiplying rows and columns by unit scalars makes its first row and first column identically \(1\), leaving
\[
M'=\begin{pmatrix}1&1&1\\1&u&v\\1&w&t\end{pmatrix},
\qquad |u|=|v|=|w|=|t|=1.
\]
Its determinant vanishes exactly if
\[
(u-1)(t-1)=(v-1)(w-1).
\]
If either side is zero, the equation immediately forces two equal rows or two equal columns (inspect the four choices \(u=1\) or \(t=1\), paired with \(v=1\) or \(w=1\)). If neither side vanishes, conjugate the equation, use \(\overline{z-1}=-(z-1)/z\) for \(|z|=1\), and divide by the original nonzero equation. This gives \(ut=vw\). Expanding the original equation then gives \(u+t=v+w\). The two unordered pairs \(\{u,t\}\) and \(\{v,w\}\) have equal sum and product, so coincide. Hence either \(u=v,t=w\) (equal second and third columns), or \(u=w,t=v\) (equal second and third rows). Conversely, proportional rows or columns always force determinant zero. Thus a unit-modulus three-by-three matrix is singular if and only if two rows or two columns are proportional.

**Step 2: translate rigidity into finite geometry.** Two rows of \(F_p[A,B]\) indexed by \(a,a'\) are proportional exactly when
\[
(a-a')\cdot(b-b')=0\quad\text{for all }b,b'\in B.
\]
Because \(a-a'\ne0\), this means \(B\) lies on an affine line parallel to the one-dimensional orthogonal complement of \(a-a'\). The transposed condition characterizes proportional columns: it requires \(A\) to be linear with direction annihilated by a difference of two points of \(B\). If neither \(A\) nor \(B\) is linear, neither phenomenon occurs, so rank is \(3\).

If \(A\) is triangular, its three edge-difference directions are distinct, hence their orthogonal line directions are distinct. For each of the three directions, the singular column sets consist of triples on one of \(p\) parallel affine lines. These classes are disjoint since a triple cannot lie on two different lines, proving the fixed-\(A\) count \(3p\binom p3=3K\). A noncollinear \(A\) rules out rank \(1\): every rank-one character minor would have three proportional rows, which would put \(B\) in the intersection of two distinct affine lines, impossible for three distinct points. Hence all these singular minors have rank \(2\).

If \(A\) is linear with direction \(v\), every selected Fourier row is, up to diagonal phase multipliers, a row with entries \(\zeta^{s_i v\cdot b_j}\) where the three \(s_i\in\mathbb F_p\) are distinct. Two Fourier columns are proportional exactly when their projected values \(v\cdot b_j\) coincide. Two rows are proportional only when all three projected values are identical, since their index differences are nonzero multiples of \(v\). Therefore the unit-modulus determinant lemma implies rank \(3\) precisely when all three projected values are distinct. If exactly two coincide, exactly two columns are proportional while the remaining column is not, giving rank \(2\). If all coincide, every column is proportional, giving rank \(1\). This establishes all cases and shows in particular that two linear triples with nonorthogonal directions have rank \(3\), whereas orthogonal directions give rank \(1\).

**Step 3: count every rank.** A finite affine plane has \(p+1\) directions and \(p\) lines per direction. Each line contains \(\binom p3=C\) three-point subsets, so the number of linear \(A\) is \(L=p(p+1)C\), and the number of triangular \(A\) is \(U=T-L\). For a fixed direction there are \(K=pC\) three-point subsets of its parallel lines. For fixed linear \(A\) of direction \(v\), choose three distinct values among the \(p\) values of the functional \(b\mapsto v\cdot b\); each chosen fiber contains \(p\) points, so \(p^3C\) triples \(B\) give rank \(3\). Exactly \(K\) have constant projection and rank \(1\); the remainder have rank \(2\). For triangular \(A\) the fixed-row classification in Step 2 gives \(3K\) rank-two partners and \(T-3K\) full-rank partners. Multiplication by \(L\) and \(U\) gives the displayed \(R_1,R_2,R_3\). Their sum is \(T^2\).

## Verification
The attached standard C++17 program `checker.cpp` runs exact cyclotomic determinant and all two-by-two-minor checks for **every** unordered three-row and three-column pair when \(p=3,5\). A determinant is stored as an integer coefficient vector of powers of a primitive \(p\)-th root. Since the minimal polynomial is \(\Phi_p(X)=1+\cdots+X^{p-1}\), its vanishing is tested with exact integer arithmetic (coefficients all equal), without floating-point thresholds. Independently the code constructs proportional-row/column tests and the finite-plane geometric prediction, compares each to exact rank, and separately checks the three closed-form global multiplicities.

Reproduce with `c++ -O3 -std=c++17 checker.cpp -o checker && ./checker`. Expected messages: `CHECK_PASS p=3 triples=84 collinear=12 rank1=36 rank2=1296 rank3=5724 exact_cyclotomic=true geometry=true` and `CHECK_PASS p=5 triples=2300 collinear=300 rank1=15000 rank2=600000 rank3=4675000 exact_cyclotomic=true geometry=true`.

## Relationship to prior work
Caragea and Lee (2024) consider **principal** minors of the Fourier matrix on the cyclic group \(\mathbb Z_N\), proving squarefreeness implications for small principal minors. This is not the character table of \(\mathbb F_p^2\) and does not enumerate arbitrary distinct row/column triples. A published classification of all three-by-three minors of the **cyclic** group \(\mathbb Z_{p^2}\) also gives ranks using residue occupancy mod \(p\), but the group character tables and exact rank counts differ: for example, at \(p=3\) the cyclic group has \(333\) singular pairs, while the present noncyclic affine plane has \(1332\). Indeed, for every prime the new rank-one and rank-two counts are each exactly \(p+1\) times the corresponding counts for the cyclic prime-square matrix; the geometric proofs and character groups remain distinct. Those cyclic results do not imply the displayed prime-affine-plane incidence formulas.

Delvaux and Van Barel (2006/2007) study rank-deficient blocks of Kronecker Fourier matrices and exact Hamming numbers, including \(F_p\otimes F_p\). Their results control *maximal* rank-deficient patterns and some constructive tilings, rather than classify every individual three-by-three minor. Biró and Lev (2018) develop structural finite-plane Fourier uncertainty inequalities rather than this exact minor-rank incidence distribution. These works motivate the question; they are not restated as novel.

## Limitations
The all-prime theorem concerns only three-by-three minors of the noncyclic rank-two elementary-abelian Fourier matrix, and not larger minors or cyclic prime-square matrices. The supporting computation verifies only \(p=3,5\); it is not used to infer the all-prime theorem. The unit-modulus determinant identity is elementary and is not independently claimed as new. A specialized earlier classification or a consequence of a broader rank-deficiency theory may exist despite the comparisons performed; the present originality assessment is not independent bibliographic certification.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793v1, submitted 2024-09-15; inspected version arXiv:2409.09793v4, https://arxiv.org/html/2409.09793v4.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW477 (2006), https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.pdf; later Linear Algebra Appl. 426 (2007), 349–367.
3. A. Biró and V. F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424v1, submitted 2018-08-22; inspected version https://arxiv.org/html/1808.07424v2.
4. *All singular three-by-three minors of prime-square Fourier matrices*, published mathematical result on the cyclic group \(\mathbb Z_{p^2}\), verified against its accessible complete statement and proof; the noncyclic character table differs.
