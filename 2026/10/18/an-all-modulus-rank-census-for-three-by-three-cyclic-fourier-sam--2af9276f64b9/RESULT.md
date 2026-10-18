# An all-modulus rank census for three-by-three cyclic Fourier sampling

## Finding
For every integer \(N\ge3\), the ranks of **all** three-row, three-column submatrices of the cyclic Fourier matrix admit a complete divisor-only census. Write \(F_N=(\zeta^{rc})_{r,c\in\mathbb Z/N\mathbb Z}\), where \(\zeta=\exp(2\pi i/N)\). Independently choose unordered three-element sets \(R,C\). Define
\[
g_R=\gcd(N,r-r':r,r'\in R),\qquad g_C=\gcd(N,c-c':c,c'\in C).
\]
Then
\[
\operatorname{rank}F_N[R,C]=
\begin{cases}
1,&N\mid g_R g_C,\\
3,&R\text{ is injective mod }N/g_C\text{ and }C\text{ is injective mod }N/g_R,\\
2,&\text{otherwise}.
\end{cases}
\]
The cases are disjoint: rank one cannot satisfy both injectivity conditions.

Here and throughout, all divisors are **positive**, \(\mu\) is the number-theoretic Möbius function, and \(\binom{s}{3}=0\) for integers \(s<3\). Define
\[
A_N(e,d)=e\binom{d/\gcd(e,d)}{3}
\left(\frac{N}{\operatorname{lcm}(e,d)}\right)^3,
\quad
T_N(g,d)=\sum_{\substack{e\mid N\\g\mid e}}\mu(e/g)A_N(e,d),
\quad Q_N(g)=T_N(g,N).
\]
For \(j=1,2,3\), let \(R_j(N)\) denote the number of **ordered pairs \((R,C)\) of unordered three-element index sets** for which the submatrix has rank \(j\). Then the exact complete census is
\[
\begin{aligned}
R_1(N)&=\sum_{\substack{g,h\mid N\\N\mid gh}}Q_N(g)Q_N(h),\\
R_3(N)&=\sum_{g,h\mid N}T_N(g,N/h)T_N(h,N/g),\\
R_2(N)&=\binom N3^2-R_1(N)-R_3(N).
\end{aligned}
\]
No cyclotomic matrices or minor enumeration is needed to evaluate these formulas. Rank-one submatrices exist exactly when there are integers \(a,b\ge3\) with \(ab\mid N\). For instance, at order \(N=18\), \((R_1,R_2,R_3)=(684,71604,593568)\), and at order \(N=15\), the triple \(R=\{0,5,10\}\), \(C=\{0,3,6\}\) gives a rank-one **nonprincipal** minor even though squarefree Fourier matrices have no singular principal three-by-three minors.

## Assumptions and scope
The matrix is complex-valued, and every entry lies on the unit circle. No primality, parity, prime-power, or squarefreeness assumption on \(N\) is imposed. The rank is over \(\mathbb C\). All three row indices and all three column indices are distinct modulo \(N\); rows and columns need not be disjoint from each other. Counts are **not** divided by permutation or translation stabilizers: each unordered row set and each unordered column set contributes one pair.

## Proof
**Step 1: unit-circle determinant rigidity.** Let \(M\) be any three-by-three matrix with all nine entries of modulus one. Multiplying rows and columns by unimodular constants does not change rank or proportionality. After such dephasing,
\[
M=\begin{pmatrix}1&1&1\\1&a&b\\1&c&d\end{pmatrix},
\qquad |a|=|b|=|c|=|d|=1.
\]
Its determinant vanishes exactly when \((a-1)(d-1)=(b-1)(c-1)\). If the common product vanishes, one of \(a,d\) and one of \(b,c\) equal one; the four possibilities produce two equal rows or columns. If the product is nonzero, use \(\overline{z-1}=-(z-1)/z\) for \(|z|=1\) and conjugate the equality to obtain \(ad=bc\). Expanding the original equality then yields \(a+d=b+c\). Consequently \(a,d\) and \(b,c\) are the roots, with multiplicity, of the same quadratic polynomial, so \(\{a,d\}=\{b,c\}\). If \(a=b\) and \(d=c\), columns two and three coincide; if \(a=c\) and \(d=b\), rows two and three coincide. Thus a singular unit-circle three-by-three matrix always has two proportional rows or two proportional columns. The converse is immediate. Furthermore, rank one is exactly the case when **every** row is proportional to the others.

**Step 2: modular geometry.** For two rows \(r,r'\in R\), the corresponding restricted Fourier row vectors are proportional precisely when the ratio \(\zeta^{(r-r')c}\) is constant over \(c\in C\). This is equivalent to \(N\mid(r-r')(c-c')\) for all column differences. Since \(g_C\) is the greatest common divisor of \(N\) and those column differences, Bézout's identity makes this condition equivalent to \(N\mid(r-r')g_C\), or \(r\equiv r'\pmod{N/g_C}\). The symmetric argument applies to columns. The rigidity lemma shows that rank three holds precisely when neither kind of proportional pair occurs. All rows are proportional precisely when \(N\) divides every product of one row difference with one column difference, which by Bézout is equivalent to \(N\mid g_Rg_C\). This proves the three-way rank classification.

**Step 3: exact divisor stratification.** Fix divisors \(e,d\mid N\). We count three-element subsets whose elements are **all congruent modulo \(e\)** and are **pairwise incongruent modulo \(d\)**. First choose one of \(e\) residue classes modulo \(e\). Inside it there are \(d/\gcd(e,d)\) compatible residues modulo \(d\), each containing \(N/\operatorname{lcm}(e,d)\) elements of \(\mathbb Z/N\mathbb Z\). Choose three distinct such residues and one element from each. This yields exactly \(A_N(e,d)\).

For a triple \(R\), the condition of being congruent modulo \(e\) is equivalent to \(e\mid g_R\). Thus \(A_N(e,d)\) counts all triples with \(e\mid g_R\) and injectivity modulo \(d\). Möbius inversion on the divisor lattice yields \(T_N(g,d)\): it counts exactly those triples with \(g_R=g\) and distinct residues modulo \(d\). In particular \(Q_N(g)=T_N(g,N)\) counts **all** triples with \(g_R=g\), since any three distinct group elements are already distinct modulo \(N\).

**Step 4: assemble ranks.** The choices \(R,C\) are independent. By Step 2, rank one is equivalent to \(N\mid g_Rg_C\), so summing \(Q_N(g)Q_N(h)\) over the admissible divisor pairs yields \(R_1(N)\). Rank three requires, when \(g_R=g\) and \(g_C=h\), precisely that \(R\) be injective modulo \(N/h\) and \(C\) be injective modulo \(N/g\). Their numbers are \(T_N(g,N/h)\) and \(T_N(h,N/g)\), respectively; independence gives \(R_3(N)\). There are \(\binom N3^2\) ordered pairs \((R,C)\) altogether, hence the subtraction formula for \(R_2(N)\).

**Step 5: sharp existence criterion for rank one.** Any three-element set with difference gcd \(g_R\) lies in one congruence class modulo \(g_R\), containing only \(N/g_R\) elements, so \(N/g_R\ge3\); likewise \(N/g_C\ge3\). Setting \(a=N/g_R\), \(b=N/g_C\), the rank-one condition \(N\mid g_Rg_C\) is exactly \(ab\mid N\). Conversely, if \(a,b\ge3\) and \(ab\mid N\), the three-element sets \(R=\{0,N/a,2N/a\}\) and \(C=\{0,N/b,2N/b\}\) satisfy \(g_R=N/a\), \(g_C=N/b\) and hence rank one. This completes the proof.

## Verification
A standalone standard-library program, `verify_census.py`, computes all cyclic Fourier three-by-three determinant polynomials as exact elements of \(\mathbb Z[X]/(\Phi_N(X))\), using the defining primitive-root minimal polynomial \(\Phi_N\). It assigns rank one by vanishing two-by-two minors when the determinant vanishes, and directly compares the result with the independent divisor sums. **Every** pair of three-row and three-column subsets was checked for the moduli \(N=3,4,5,6,7,8,9,10,12,15,16,18\). Further exact divisor evaluations were carried out for \(N=20,21,24,25,27,30,36,40,45,60\). Full output appears in `verification_output.txt`. The arithmetic code and exhaustive finite cases corroborate the symbolic proof; they do not replace the proof for unbounded \(N\).

## Relationship to prior work
Caragea and Lee, *On the principal minors of Fourier matrices* (2024), establish principal-minor results for squarefree and other orders; those results concern the diagonal condition \(R=C\), rather than independent arbitrary three-element row and column sets. Herr and Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets* (2019), classify orthogonal/Hadamard Fourier submatrix patterns, not all three possible ranks. More recent work on principal minors of squarefree order also has a strictly different sampling condition.

Existing special-case calculations already classify singular three-by-three cyclic Fourier minors for odd prime squares, prime powers and twice an odd prime, and separately handle three-by-three Fourier minors for elementary prime affine planes. Such special cases are **not claimed as new** here. Their restricted modulus hypotheses, however, do not imply the displayed joint divisor census at arbitrary mixed-prime orders. The new object is the uniform all-\(N\) rank count together with its simple exact rank-one arithmetic criterion. A differently indexed equivalent theorem outside the inspected literature remains possible.

## Limitations
The theorem addresses only size-three minors of the cyclic complex Fourier matrices and says nothing about singularity of larger minors, matrices over finite characteristic, or rectangular row/column sizes other than three. The theorem is exact; its originality is a best-knowledge literature assessment rather than a proof of historical uniqueness. In particular, previously published prime-power and squarefree special cases remain prior work.

## References
1. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, first public September 15, 2024. https://arxiv.org/abs/2409.09793.
2. J. E. Herr and T. M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets*, first public September 28, 2019. https://arxiv.org/abs/1909.13145.
3. A. Caragea, D. G. Lee, A. Malikiosis and G. E. Pfander, *Principal minors of Fourier matrices of square-free order*, 2025. https://arxiv.org/abs/2505.24326 (supporting comparison only).
