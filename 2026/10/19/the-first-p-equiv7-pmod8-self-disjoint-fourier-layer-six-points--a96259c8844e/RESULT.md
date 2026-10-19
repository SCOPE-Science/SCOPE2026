# The first \(p\equiv7\pmod8\) self-disjoint Fourier layer: six points and three symmetry orbits

## Finding
Let \(G=\mathbb F_7^2\), equipped with the standard dot-product Fourier transform, and let \(\sigma_7\) denote the minimum number of nonzero coefficients of a nonzero function whose time support is disjoint from its Fourier support. Then
\[
\boxed{\sigma_7=6.}
\]
Exactly \(5488\) six-element subsets \(S\subset G\) support such a function; for each such \(S\), its coefficient vector is unique up to nonzero complex scaling, and all six coefficients are nonzero. Under affine transformations preserving the dot product up to a nonzero scalar, these \(5488\) supports constitute exactly three orbits of respective sizes \(2352\), \(784\), and \(2352\).

A representative of the first orbit is
\[
S_1=\{(0,0),(0,1),(0,2),(2,0),(2,1),(2,6)\}.
\]
Representatives of the second and third orbits are
\[
S_2=\{(0,0),(0,1),(0,3),(1,0),(2,1),(4,3)\},
\]
\[
S_3=\{(0,0),(0,1),(0,3),(1,1),(1,2),(1,6)\}.
\]

## Assumptions and scope
Write \(\zeta=\exp(2\pi i/7)\), and identify \(G\) with its dual using the standard coordinate dot product. The unitary Fourier transform is
\[
\widehat f(\xi)=\frac17\sum_{x\in G}f(x)\zeta^{x\cdot\xi}.
\]
The support of \(f\) is the set of its nonzero complex coefficients. The invariant is
\[
\sigma_7=\min\{|\operatorname{supp}f|:0\ne f:G\to\mathbb C,\quad
\operatorname{supp}f\cap\operatorname{supp}\widehat f=\varnothing\}.
\]
The theorem concerns exactly the first prime \(7\equiv7\pmod8\); no all-prime extension is claimed. An affine dot-product similitude is \(x\mapsto Ax+t\), with \(A\in\mathrm{GL}_2(\mathbb F_7)\) and \(A^\top A=\lambda I\), for some \(\lambda\in\mathbb F_7^\times\).

## Proof
**Reduction to principal Fourier minors and normalization.** For each \(S\subseteq G\), set \(M_S=(\zeta^{x\cdot y})_{x,y\in S}\). A nonzero function with \(\operatorname{supp}f\subseteq S\) and \(\widehat f|_S=0\) exists precisely when \(M_S\) is singular. Translation \(S\mapsto S+t\) changes \(\zeta^{(x+t)\cdot(y+t)}\) by a nonzero row factor \(\zeta^{x\cdot t}\), a nonzero column factor \(\zeta^{y\cdot t}\), and a common factor \(\zeta^{t\cdot t}\). Thus singularity is translation-invariant; for each cardinality \(k\), it suffices to check the \(\binom{48}{k-1}\) subsets containing \((0,0)\).

**Certified exhaustive arithmetic, not floating-point sampling.** The standalone source `artifacts/verify.py` implements a complete finite exhaustion. For \(k\le6\), it builds \(M_S\) using only exponents in \(\mathbb Z/7\mathbb Z\). A complex zero determinant must also vanish after specializing \(\zeta\) to any primitive seventh root in a finite field of characteristic other than seven. Four explicit specializations are
\[
(q,r)\in\{(29,7),(43,4),(71,20),(113,16)\},\quad r^7\equiv1\pmod q,\ r\ne1.
\]
The program verifies primitiveness and applies exact modular Gaussian elimination. Every normalized set whose determinant is nonzero in at least one such field is therefore certainly nonsingular over \(\mathbb C\). For sizes \(k=1,2,3,4,5\), the numbers of normalized sets are respectively \(1,48,1128,17296,194580\); all are rejected by the first two fields. Hence all principal minors of orders at most five are nonsingular in characteristic zero.

For \(k=6\), there are \(\binom{48}{5}=1{,}712{,}304\) normalized sets. The successive counts of modular-zero survivors are \(57{,}360\), \(960\), \(672\), and \(672\). The code examines all \(672\) survivors via exact signed permutation expansion
\[
P_S(T)=\sum_{\pi\in\mathfrak S_6}\operatorname{sgn}(\pi)
 T^{\sum_{j=1}^{6}x_j\cdot x_{\pi(j)}\bmod7}\in\mathbb Z[T]/(T^7-1).
\]
Writing \(P_S(T)=\sum_{j=0}^{6}c_j T^j\), evaluation at \(T=\zeta\) is zero if and only if all seven integer coefficients are equal, since the minimal polynomial is \(1+T+\cdots+T^6\). Also \(\sum c_j=0\) for a determinant of order at least two (sum of permutation signs), so this is equivalent to \(c_0=\cdots=c_6=0\). All \(672\) surviving sets satisfy this exact identity. These and only these \(672\) normalized sets are singular. For the displayed representative \(S_1\), its exponent matrix (rows and columns in the displayed order) is
\[
\begin{pmatrix}
0&0&0&0&0&0\\0&1&2&0&1&6\\0&2&4&0&2&5\\0&0&0&4&4&4\\0&1&2&4&5&3\\0&6&5&4&3&5
\end{pmatrix},
\]
and its exact signed determinant coefficient vector is \((0,0,0,0,0,0,0)\). This also supplies a reproducible explicit existence certificate.

**Counting all supports and coefficient fibers.** Each six-set has exactly six choices of a marked element that can be translated to the origin. Double-counting marked sets gives exactly \(672\cdot49/6=5488\) singular six-sets. Every five-element principal minor is invertible; hence every singular six-by-six matrix has rank exactly five. Its kernel is one-dimensional. If a nonzero kernel vector vanished at any one coordinate, restricting to the other five row equations would contradict invertibility of the corresponding five-by-five principal minor. Therefore its six coefficients are all nonzero. Conversely a function supported on fewer than six sites would induce a singular principal minor of smaller order, which has been excluded. This proves the minimal cardinality and exact one-projective-class-per-support statement.

**Complete geometric orbit classification.** The invertible linear similitudes for the anisotropic dot product are exactly the \(96\) maps with matrices
\[
\begin{pmatrix}a&-b\\b&a\end{pmatrix}
\quad\text{or}\quad
\begin{pmatrix}a&b\\b&-a\end{pmatrix},\qquad(a,b)\ne(0,0),
\]
because \(a^2+b^2\ne0\) for nonzero \((a,b)\in\mathbb F_7^2\), and their matrices have \(A^\top A=(a^2+b^2)I\). Such a change of indices transforms dot products by multiplication by \(\lambda\), hence transforms principal minors through the cyclotomic Galois automorphism \(\zeta\mapsto\zeta^\lambda\), preserving singularity. The exact verifier reduces all \(672\) normalized singular sets modulo translations to \(112\) distinct translation classes and applies all \(96\) similitudes. Exhaustive orbit partition returns exactly three translation-class orbits of sizes \(48,16,48\), represented by \(S_1,S_2,S_3\). Each six-point set has a translation orbit of exactly \(49\): a nontrivial translation has order seven, so an invariant nonempty set would have cardinality divisible by seven, contradicting six. Consequently the full orbits have \(49\cdot48=2352\), \(49\cdot16=784\), and \(49\cdot48=2352\) supports, as claimed.

## Verification
Run `python3 artifacts/verify.py` with a standard Python 3 interpreter. The program exhaustively enumerates all normalized supports of cardinality one through six; uses exact modular elimination and cyclotomic group-ring identities; counts support and symmetry orbits; and raises an error if a stated number or structural invariant differs. A complete successful execution returns `VERIFY_OK` with \(672\) normalized singular six-sets and \(5488\) six-sets globally. The computation is a finite, exhaustive certificate for the finite theorem, rather than an extrapolation from a sample. The script has no external dependencies and uses no floating point.

## Relationship to prior work
Zhou's 2026 paper [1, Proposition 3] establishes self-disjoint-support constructions on \(\mathbb F_p^2\), including the \(p\equiv3\pmod4\) case, but does not determine its optimal support cardinalities; its exhibited upper bound at \(p=7\) is \(12\). The published result [2] resolves the infinite subclass \(p\equiv3\pmod8\) with minimum four, explicitly leaving \(p\equiv7\pmod8\) unresolved. The present result gives the first exact value in that complementary subclass and additionally classifies all smallest supports and unique coefficient fibers. The Kronecker-Fourier work [3] constructs general rank-deficient rectangular submatrices and gives uncertainty estimates, without a verified statement of this exact \(6\times6\) principal-minor classification at \(\mathbb F_7^2\). The cyclic-group principal-minor work [4] uses a different Fourier matrix. The cited results are not claimed to be exhaustive historical coverage.

## Limitations
The result applies to the standard dot-product pairing on \(\mathbb F_7^2\), not arbitrary perfect pairings or all \(p\equiv7\pmod8\). The exact enumeration is auditable computational mathematics rather than a short closed-form symbolic classification; its completeness relies on the supplied program and the argument connecting modular nonvanishing to characteristic-zero nonvanishing. No independent external audit has been performed. Earlier, incompletely inspected structural literature on Kronecker Fourier matrices could contain a mathematically equivalent special case, and the historical-priority assessment is qualified accordingly.

## References
1. W. Zhou, *On number of cyclic \(n\)-roots and disjointness of Fourier supports*, arXiv:2608.06335, first public 2026-08-06, https://arxiv.org/abs/2608.06335 .
2. *Sharp four-point self-disjoint Fourier supports on \(\mathbb F_p^2\) for \(p\equiv3\pmod8\)*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-four-point-self-disjoint-fourier-supports-on-mathbb-f-p-2--7b34d464851b .
3. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra and its Applications 426 (2007), 349–367, https://doi.org/10.1016/j.laa.2007.05.009 .
4. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, https://arxiv.org/abs/2409.09793 .
