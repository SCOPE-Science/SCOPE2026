# A ternary-to-binary flatness reversal for quadratic Fourier shells on five and six variables

## Finding
For an integer \(n\ge4\) and unimodular coefficients \(a_{ij}\), consider the squarefree homogeneous Fourier polynomial
\[
P_{n,a}(z)=\sum_{1\le i<j\le n}a_{ij}z_i z_j,\qquad z\in\mathbb T^n,
\]
with normalized fourth moment \(\mathcal M_n(a)=\int_{\mathbb T^n}|P_{n,a}(z)|^4\,dm(z)\), where \(m\) is probability Haar measure. For \(q\ge2\), write \(\mu_q=\{e^{2\pi i j/q}:0\le j<q\}\) and \(\mathcal M_n(q)=\min_{a_{ij}\in\mu_q}\mathcal M_n(a)\). The exact first two nontrivial alphabet comparisons are
\[
\boxed{\mathcal M_5(2)=150,\quad\mathcal M_5(3)=130,\quad
\mathcal M_6(2)=315,\quad\mathcal M_6(3)=363.}
\]
The unrestricted unimodular minima are \(130\) in five variables and \(315\) in six variables. More precisely, \(\mathcal M_5(q)=130\) if and only if \(3\mid q\), and \(\mathcal M_6(q)=315\) if and only if \(2\mid q\). Thus ternary phases cancel every four-vertex matching defect in five variables but cannot attain the six-variable conference bound, whereas binary phases are quantitatively preferable in six variables. Among ternary six-variable coefficient arrays satisfying the normalization \(a_{1j}=1\) for \(j=2,\ldots,6\), exactly \(360\) attain the optimum \(363\). This count is of normalized arrays, not a count of orbits under all residual phase symmetries.

Two exact identities expose the structure. Let \(A\) be the symmetric matrix with zero diagonal and off-diagonal entries \(a_{ij}=a_{ji}\). Then, writing \(B_n=n(n-1)(4n-7)/2\) and \(L_n=n(n-1)(n^2-3n+3)/2\),
\[
\begin{split}
\mathcal M_n(a)&=B_n+4\sum_{i<j<k<l}
\left|a_{ij}a_{kl}+a_{ik}a_{jl}+a_{il}a_{jk}\right|^2\\
&=L_n+\sum_{i\ne j}\left|(AA^*)_{ij}\right|^2.
\end{split}
\]
These identities hold for every integer \(n\ge4\) and all unimodular coefficients. The second identity identifies equality in \(\mathcal M_n(a)\ge L_n\) exactly with symmetric complex conference matrices. Its conference-matrix constructions are established background; the new finite-alphabet feature here is the sharp six-variable ternary value and its reversal of the five-variable order.

## Assumptions and scope
All exponents are distinct vectors \(e_i+e_j\) in \(\mathbb Z^n\), and integration is over the continuous torus \(\mathbb T^n\) with normalized Haar measure. Coefficients are arbitrary unit complex numbers unless restricted to \(\mu_q\). No coefficients are permitted to vanish. The finite enumeration is an exhaustive exact-arithmetic proof only for the stated fixed six-variable ternary problem; it does not classify all larger values of \(n\) or all alphabets \(q\). The same fourth-moment identities hold on a product of finite cyclic groups of common order at least five, because no nonzero difference of the relevant exponent sums can vanish modulo that order.

## Proof
**Coefficient identity.** Orthogonality of torus characters gives \(\mathcal M_n(a)=\|P_{n,a}^2\|_2^2\). In \(P_{n,a}^2\), repeated edges produce \(\binom n2\) monomials with coefficient modulus one. Pairs of distinct edges meeting at one vertex produce \(n\binom{n-1}{2}\) monomials with coefficient modulus two. Four distinct vertices admit three perfect matchings, whose common monomial has coefficient twice the displayed matching sum. This proves the first identity. Expanding the row correlations \(\sum_{i\ne j}|(AA^*)_{ij}|^2\), each diagonal term contributes \(n(n-1)(n-2)\) in total, while the mixed terms contribute \(8\) times the real part of the three matching-product cross terms per four-vertex set. Comparing this expansion with the first identity yields \(\mathcal M_n(a)=L_n+\sum_{i\ne j}|(AA^*)_{ij}|^2\), after simplifying constants.

**Five variables.** Here \(B_5=L_5=130\) and there are five four-vertex matching sums. Put \(\omega=e^{2\pi i/3}\). Normalize \(a_{1j}=1\) and on vertices \(2,3,4,5\) assign the three phases \(1,\omega,\omega^2\) to the three opposite-edge pairs of the complete graph on those four vertices. Each matching sum on every four-vertex set is \(1+\omega+\omega^2=0\), proving the unrestricted and ternary minimum \(130\). Conversely, a zero matching sum of three unit complex numbers forces their ratios to be the primitive cube roots: indeed, dividing by one summand and imposing modulus one on the other two yields the equilateral triangle. For coefficients in \(\mu_q\), this forces \(3\mid q\). For binary coefficients, every matching sum is an odd integer and has squared modulus at least one, giving \(130+4(5)=150\); equality is realized by deleting the first row and column of the displayed six-variable sign matrix below, where all five matching sums have modulus one.

**Six variables and the binary optimum.** The second identity yields \(\mathcal M_6(a)\ge L_6=315\). Equality occurs for the following real symmetric conference matrix, which has zero diagonal, entries \(\pm1\) off the diagonal, and satisfies \(CC^\mathsf{T}=5I_6\):
\[
C=\begin{pmatrix}
0&1&1&1&1&1\\
1&0&-1&-1&1&1\\
1&-1&0&1&1&-1\\
1&-1&1&0&-1&1\\
1&1&1&-1&0&-1\\
1&1&-1&1&-1&0
\end{pmatrix}.
\]
Thus \(315\) is the unrestricted and binary minimum. Suppose a \(\mu_q\)-valued matrix attained \(315\). For any two rows, orthogonality would express zero as the sum of four members of \(\mu_q\). Four unit complex numbers with sum zero necessarily split into two antipodal pairs. To see this, rearrange two of them against the other two; equal-length pairs with a common nonzero sum are symmetric about that sum, so the opposite pair is their negative, while a zero pair-sum already consists of antipodes. Hence \(-1\in\mu_q\), requiring \(q\) even. Conversely any even \(q\) contains the displayed binary construction.

**Six-variable ternary optimum.** The remaining sharp \(\mu_3\) calculation is finite and exact. Because multiplying each variable by a cube root preserves the fourth moment, every ternary coefficient configuration is equivalent to one with all five entries on edges incident to vertex \(1\) equal to \(1\). Exactly ten edges remain free, giving \(3^{10}=59049\) complete configurations. Encode each free coefficient by an exponent in \(\{0,1,2\}\). For each four-vertex set, the three matching products have exponents \(x,y,z\) modulo three, and the squared modulus of their sum equals \(0\) if these exponents are pairwise distinct, \(9\) if all are equal, and \(3\) otherwise. Exhaustive iteration of all \(59049\) exponent vectors with this integer-only rule yields a minimum aggregate defect of \(27\), attained in exactly \(360\) arrays satisfying the fixed-edge normalization. The full defect histogram (defect, number of configurations) is

`(27,360), (30,2646), (33,3240), (36,4680), (39,8640), (42,9180), (45,10170), (48,4320), (51,5130), (54,2700), (57,4050), (60,1080), (63,900), (69,810), (72,360), (75,270), (81,420), (99,90), (135,3)`.

Its counts sum to \(59049\). Since \(B_6=255\), the minimum moment is \(255+4(27)=363\). An independent termwise noncancellation argument would give only \(\mathcal M_6\ge315+30=345\): each of the \(30\) ordered off-diagonal row correlations is a sum of four cubic roots, whose squared modulus is at least one. The sharp value \(363\) therefore detects genuinely coupled constraints among the correlations, not merely the absence of a conference matrix. The attached checker implements the complete enumeration and independently recomputes an attaining moment using exact arithmetic in the Eisenstein integers and the matrix-correlation identity. This is an exhaustive finite proof, not a random sample or a numerical extrapolation.

## Verification
Run `python3 checker.py` with Python 3.9 or later; no dependencies are needed. The program uses exact integer arithmetic for the full \(3^{10}\) enumeration; its root-of-unity checks use the representation \(a+b\omega\) with \(\omega^2+\omega+1=0\). It independently evaluates the two fourth-moment formulas for every normalized binary configuration in dimensions four, five, and six; verifies the conference matrix and its five-variable principal submatrix; and checks both the ternary optimum and the number of normalized minimizers. It prints a `PASS` report on success. The six-variable ternary enumeration tests the entire gauge-reduced search space; gauge invariance is proved above.

## Relationship to prior work
Balister, Bollobás, Morris, Sahasrabudhe and Tiba establish existence of globally flat one-variable Littlewood polynomials, motivating phase constraints as a fundamental harmonic-analysis question; their theorem does not give exact fourth moments of complete-graph quadratic Fourier shells. Haemers and Parsaei Majd analyze conference matrices and principal submatrices. Et-Taoui's 2021 survey explicitly displays the real symmetric six-variable conference matrix and a five-variable complex conference matrix with cube-root entries: their existence is prior work, not claimed as new. Et-Taoui and Makhlouf classify small complex conference matrices, including symmetric matrices of order six; that classification addresses the **zero-defect** case but not the nonzero optimum \(363\) for the excluded ternary alphabet. The distinct new statement is the exact, exhaustive, positive-gap ternary minimization on six variables together with the first-five/six phase-alphabet reversal. Closest related Fourier records concern six points in a two-dimensional triangular aperture, four consecutive one-variable frequencies, and quadratic Walsh chaos; those have different character relations and do not imply the ten-free-edge ternary census here.

## Limitations
The six-variable ternary exact minimum is supported by a finite exhaustive certificate; it is not a claimed formula in arbitrary dimension. Conference-matrix existence, including the displayed small matrices, is longstanding, and is used rather than rediscovered. The survey and open-access conference paper were available, but full text of the more directly relevant complex skew-symmetric classification paper could not be obtained; its abstract discloses a classification through order six, leaving a residual historical-priority risk for reformulations of the zero-defect statements. No literature source inspected states the specific ternary residual optimum \(363\) or the \(150/130\) versus \(315/363\) reversal. These negative comparisons are best-knowledge observations, not proofs of absolute historical uniqueness. No higher-degree or non-squarefree Fourier claims are asserted.

## References
1. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe and M. Tiba, *Flat Littlewood Polynomials Exist*, arXiv:1907.09464, first submitted 2019-07-22, https://arxiv.org/abs/1907.09464.
2. W. H. Haemers and L. Parsaei Majd, *Spectral symmetry in conference matrices*, arXiv:2004.05829, first submitted 2020-04-13, https://arxiv.org/abs/2004.05829; *Designs, Codes and Cryptography* 90 (2022), 1983–1990.
3. B. Et-Taoui, *A survey on complex conference matrices*, lecture slides, 2021-09-28, https://www.math.colostate.edu/~king/codex/slides/EtTaoui_2021_09_28.pdf.
4. B. Et-Taoui and A. Makhlouf, *Complex skew-symmetric conference matrices*, *Linear and Multilinear Algebra* 70 (2022), 6648–6663, doi:10.1080/03081087.2021.1967848; first published online 2021-08-23.
