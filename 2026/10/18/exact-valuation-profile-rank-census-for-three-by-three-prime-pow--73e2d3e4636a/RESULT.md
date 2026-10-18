# Exact valuation-profile rank census for three-by-three prime-power Fourier minors

## Finding
Let \(p\) be any prime, \(a\ge2\), and \(N=p^a\). For three-element subsets \(R,C\subset\mathbb Z/N\mathbb Z\), consider the complex Fourier submatrix
\[
F_N[R,C]=(\exp(2\pi i rc/N))_{r\in R,c\in C}.
\]
For a triple \(T=\{t_1,t_2,t_3\}\) of distinct residues, sort the three valuations \(v_p(t_i-t_j)\) as \((r,r,t)\), where \(0\le r\le t<a\). The two least valuations coincide by the ultrametric property. Write \((r,t)\) for the valuation profile of \(T\); let \((r,t)\) and \((s,u)\) be the profiles of \(R\) and \(C\), respectively.

Then the **exact rank** of every selected three-by-three submatrix is
\[
\operatorname{rank}F_N[R,C]=
\begin{cases}
1,&r+s\ge a,\\
2,&r+s<a\ \text{and}\ (t+s\ge a\ \text{or}\ r+u\ge a),\\
3,&t+s<a\ \text{and}\ r+u<a.
\end{cases}
\]
The cases partition all possibilities because \(t\ge r\) and \(u\ge s\). The classification includes dyadic and arbitrary odd prime powers, without any assumption that row and column sets coincide.

The number of unordered triples with profile \((r,t)\) is exactly
\[
W_{r,t}=\begin{cases}
p^r\binom p3 p^{3(a-r-1)},&t=r,\\
\dfrac{p^a(p-1)^2}{2}p^{2a-r-t-2},&r<t.
\end{cases}
\]
In particular \(W_{r,r}=0\) for \(p=2\). The exact number \(M_j\) of pairs of unordered three-element index sets \((R,C)\) for which the minor has rank \(j\) is the explicit finite arithmetic sum
\[
M_j=\sum_{0\le r\le t<a}\sum_{0\le s\le u<a}
W_{r,t}W_{s,u}\,\mathbf1\{\mathcal R_a(r,t;s,u)=j\},\qquad j\in\{1,2,3\},
\]
where \(\mathcal R_a\) is the rank function displayed above. All terms are integer arithmetic, and \(M_1+M_2+M_3=\binom N3^2\). This is an exact rank census computable from \(p,a\) using only \(O(a^4)\) summands, regardless of matrix size.

At the binary prime-power orders \(4,8,16\), respectively, the rank counts \((M_1,M_2,M_3)\) are \((0,0,16)\), \((0,320,2816)\), and \((256,26624,286720)\). At order \(27\) they are \((4455,323676,8227494)\). Thus rank-one defects first occur at binary order \(16\), whereas rank-two defects already occur at binary order \(8\).

## Assumptions and scope
All ranks and determinants are over \(\mathbb C\). Every row and column index set consists of **three distinct** residues, and the counting treats each unordered set once on each axis; the ordered pair of sets \((R,C)\) is retained. No cyclic ordering of the three selected indices enters the statement. The valuation of a residue difference is its largest exponent below \(a\) dividing any integer representative. Distinct residues ensure that valuation is below \(a\). The assertions apply to every prime, including \(p=2\), and every integer exponent \(a\ge2\).

## Proof
**Lemma (unit-circle rank rigidity).** Every singular three-by-three complex matrix whose nine entries have modulus one contains two proportional rows or two proportional columns. Multiplying the original matrix on both sides by invertible diagonal matrices reduces it to
\[
U=\begin{pmatrix}1&1&1\\1&A&B\\1&C&D\end{pmatrix},\qquad |A|=|B|=|C|=|D|=1.
\]
Its determinant vanishes exactly when \((A-1)(D-1)=(B-1)(C-1)\). If the common product is zero, at least one of the differences on each side is zero: each of the four possibilities gives an equal pair of normalized rows or columns. If the product is nonzero, complex conjugation of the determinant identity and \(\overline Z=Z^{-1}\) for unit-modulus \(Z\) yield \(AD=BC\). Substitution into the original identity gives \(A+D=B+C\). Two unordered complex pairs with the same sum and product coincide, so either \(A=C,B=D\) (equal rows) or \(A=B,C=D\) (equal columns). The converse is immediate.

**Rank-one criterion.** Every two-by-two minor of \(F_N[R,C]\) associated with row difference \(\Delta r\) and column difference \(\Delta c\) vanishes precisely when \(N\mid\Delta r\Delta c\). All two-by-two minors vanish if and only if the minimum row-difference valuation plus the minimum column-difference valuation is at least \(a\), i.e. \(r+s\ge a\). Since every Fourier entry is nonzero, this is equivalent to rank one.

**Singularity criterion.** Two selected Fourier rows indexed by \(r_1,r_2\) are proportional on all three selected columns if and only if
\[
N\mid(r_1-r_2)(c-c')\quad\text{for every }c,c'\in C.
\]
This occurs if and only if \(v_p(r_1-r_2)+s\ge a\). Some row pair attains valuation \(t\), so a proportional row pair exists exactly when \(t+s\ge a\). Transposing gives the criterion \(r+u\ge a\) for a proportional column pair. By the unit-circle lemma, **these are the only ways a three-by-three Fourier minor can be singular**. Combining with the rank-one criterion gives exactly the three rank cases stated.

**Profile enumeration.** If all three differences have valuation \(r\), the triple occupies one residue modulo \(p^r\) and three distinct children modulo \(p^{r+1}\). There are \(p^r\) choices of parent residue, \(\binom p3\) choices of children, and \(p^{a-r-1}\) choices of lift for each point. This gives the displayed \(W_{r,r}\).

If \(r<t\), exactly one unordered pair of points has difference valuation \(t\), while each of its differences from the third point has valuation \(r\). Choose the first point in \(p^a\) ways, the second in \((p-1)p^{a-t-1}\) ways, and the third in \((p-1)p^{a-r-1}\) ways. Divide by two for the order of the unique close pair. This gives \(W_{r,t}\). There are no other types. Inserting these profile multiplicities into the rank classification counts every ordered pair \((R,C)\) exactly once, proving all three exact census formulas.

## Verification
The standalone file `verify_primepower.py` independently computes Fourier-minor determinants exactly, by reducing the signed six-term determinant polynomial modulo
\[
\Phi_{p^a}(X)=1+X^{p^{a-1}}+\cdots+X^{(p-1)p^{a-1}}.
\]
This requires integer arithmetic only, not floating point. It then decides rank one by direct two-by-two minors, and compares every observed rank against the theorem. The exhaustive cases are \(N=4,8,9,16\), totaling \(323{,}808\) tested pairs. Another \(200{,}000\) deterministic seeded exact checks cover \(N=25,27,32,49,125\). Separately, the verifier checks all valuation-profile multiplicities at orders up to \(27\), the global count identities, and the output above. Run `python verify_primepower.py` alongside its standard-library-only dependencies; `verify_output.txt` records the observed success marker `EXACT_VERIFY_OK`. These finite tests corroborate, but do not replace, the general symbolic proof.

## Relationship to prior work
The prime-power full-spark theorem of Alexeev, Cahill and Mixon (Theorem 9 of [1]) tests whether **every** maximal minor of a fixed row-selected harmonic frame is nonsingular. It does not classify each minor's rank, because a non-full-spark row family can contain both singular and nonsingular column selections. Caragea and Lee [2] treat **principal** Fourier minors and are not a classification of independently selected index triples.

An existing complete rank census [3] treats the **prime-square case** \(a=2\) for odd primes, in agreement with the specialization here, but explicitly leaves higher prime powers outside scope. The present formula supplies a uniform classification and a full rank census for all exponents, including \(a\ge3\) and the dyadic transition \(4\to8\to16\). The finite-field affine-plane and even-semiprime minor results [4,5] concern different additive groups or moduli; their conditions cannot imply the prime-power valuation spectrum by substitution. Herr and Wiegand [6] classify Fourier **Hadamard** submatrices, a stronger orthogonality condition distinct from the present rank question.

## Limitations
This work classifies only three-by-three minors, not higher-order minors or arbitrary mixed-prime composite moduli. The polynomial-time rank count is an exact finite sum, not an asymptotic or a factorized closed polynomial for unrestricted exponent. The proof is self-contained once the elementary unit-circle argument is supplied; the computation is supplementary. Even though the searched literature did not identify an equivalent all-prime-power rank-census theorem, previously unindexed generalized-Vandermonde or harmonic-frame work could already imply it. Independent validation is not claimed.

## References
1. B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (first public 2011-10-17), especially Theorem 9.
2. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793 (first public 2024-09-15).
3. *All singular three-by-three minors of prime-square Fourier matrices*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b (specifically `RESULT.md`).
4. *Complete three-by-three Fourier-minor rank geometry on prime affine planes*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-three-by-three-fourier-minor-rank-geometry-on-prime-aff--ba0b52ec4cec.
5. *Singular three-by-three Fourier minors on even semiprime cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-three-by-three-fourier-minors-on-even-semiprime-cycles--8f025c6183d3.
6. J. E. Herr and T. M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets*, arXiv:1909.13145 (first public 2019-09-28).
