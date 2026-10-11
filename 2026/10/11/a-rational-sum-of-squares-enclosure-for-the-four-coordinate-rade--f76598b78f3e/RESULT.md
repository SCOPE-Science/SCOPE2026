# A rational sum-of-squares enclosure for the four-coordinate Rademacher projection on real \(L^4\)

## Finding
On the uniform probability space \(\Omega=\{-1,1\}^4\), let \(r_i(\varepsilon)=\varepsilon_i\) and let \(R_4f=\sum_{i=1}^4 (\mathbb E[f r_i])r_i\) be the real first-chaos (Rademacher) projection. Let \(t\) be the unique real root of \(t^3+9t+6=0\). Then
\[
\left(\frac{21}{21+18t^2+t^4+24t}\right)^{1/4}\leq\|R_4\|_{L^4\to L^4}\leq\left(\frac{200}{123}\right)^{1/4}.
\]
The lower and upper bounds are respectively approximately \(1.1234973384\) and \(1.1292269153\). The upper bound is a strict improvement over the elementary fourth-moment/Khintchine upper bound \(3^{1/4}\). No exact norm equality is asserted.

## Assumptions and scope
The scalar field is real, the measure is uniform on all sixteen sign vectors, and \(R_4\) is the unweighted orthogonal Walsh projection, considered as an operator in real \(L^4\). All inequalities are exact, and the upper bound applies to every real input function on the cube.

## Proof
**Reduction to eight coefficients.** The map \(f\mapsto [f(\varepsilon)-f(-\varepsilon)]/2\) is an \(L^4\) contraction and preserves \(R_4f\); thus it suffices to consider odd functions. Set \(\chi=r_1r_2r_3r_4\). Since the four degree-one Walsh characters and four degree-three characters \(\chi r_i\) form a basis of the real odd functions, every such function is uniquely \(f=S+\chi T\), with \(S=\sum_i a_i r_i\), \(T=\sum_i b_i r_i\) and \(R_4f=S\).

Write \(A=\sum_i a_i^2\), \(B=\sum_i b_i^2\), \(C=\sum_i a_i b_i\), and \(F(a)=3A^2-2\sum_i a_i^4\), with \(F(b)=3B^2-2\sum_i b_i^4\). A Walsh expectation expansion gives
\[
\mathbb E(f^4)-\frac{123}{200}\mathbb E(S^4)
=(1-c)F(a)+F(b)+6AB+12C^2-12\sum_i a_i^2b_i^2+24\sum_i\left(b_i\prod_{j\ne i}a_j+a_i\prod_{j\ne i}b_j\right),\quad c=123/200.
\]
The term with coefficient \(24\) follows from \(\mathbb E[\chi S^3T]=6\sum_i b_i\prod_{j\ne i}a_j\) and its counterpart exchanging \(a,b\).

**Exact positive-definite Gram certificate.** Put \(p=255/100\), \(s=665/100\), \(h=483/100\), \(q=252/100\), \(v=636/100\), \(u=639/100\); set \(\alpha=1-c\), \(\beta=3-3c-p/2\), \(\delta=3-s/2\), \(\epsilon=3-h/2\), \(\zeta=3-u/2\), and \(\theta=12-q-v\). Define an \(8\times8\) symmetric rational matrix \(M_0\) with \(4\times4\) diagonal blocks having diagonal/off-diagonal entries \((\alpha,\beta)\) and \((1,\delta)\), and both cross blocks having diagonal/off-diagonal entries \((\epsilon,\zeta)\). Define \(M_1\) as the \(4\times4\) matrix with diagonal \(h\) and off-diagonal \(\theta\), and
\[
M_2=\begin{pmatrix}p&q&4&4\\q&s&4&4\\4&4&u&v\\4&4&v&u\end{pmatrix}.
\]
Let \(z_0=(a_1^2,\ldots,a_4^2,b_1^2,\ldots,b_4^2)\) and \(z_1=(a_1b_1,\ldots,a_4b_4)\). For each pair \(i<j\) of indices from \(1,2,3,4\), let \(k<\ell\) denote the complementary pair and let \(z_{ij}=(a_i a_j,b_i b_j,a_kb_\ell,a_\ell b_k)\). An exact coefficient comparison yields
\[
\mathbb E(f^4)-\frac{123}{200}\mathbb E(S^4)=z_0^\top M_0z_0+z_1^\top M_1z_1+\sum_{i<j}z_{ij}^\top M_2z_{ij}.
\]
Every leading principal minor of each of the three matrices is strictly positive. The exact rational minors, in increasing order, are as follows:

\(M_0\): \(77/200,5353/40000,295829/8000000,1030301/320000000,4967887/16000000000,359897643/12800000000000,2908720213/1280000000000000,14331199589/102400000000000000\).

\(M_1\): \(483/100,27189/2000,32369787/1000000,7095299409/100000000\).

\(M_2\): \(51/20,106071/10000,1219369/1000000,254463/4000000\).

Hence Sylvester's criterion makes all three matrices positive definite; their quadratic-form sum is nonnegative. Therefore \(\mathbb E(S^4)\leq(200/123)\mathbb E(f^4)\) for every \(f\), giving the upper bound.

**Constructive lower bound.** On the first three signs take \(f_3=r_1+r_2+r_3+t r_1r_2r_3\), independent of the fourth sign. The projection sends it to \(S_3=r_1+r_2+r_3\), with \(\mathbb E(S_3^4)=21\) and \(\mathbb E(f_3^4)=21+18t^2+t^4+24t\). The latter strictly convex polynomial is minimized where \(t^3+9t+6=0\), which has a unique real root. This witnesses the stated lower bound.

## Verification
The accompanying `verify.py` recomputes every rational leading principal minor and checks the entire quartic polynomial identity coefficient-by-coefficient in eight independent indeterminates. It uses exact arithmetic and asserts that all three Gram matrices are positive definite. The lower witness is checked by a direct analytic Walsh-moment expansion. This is a fully symbolic finite computation, not extrapolation from floating-point sampling.

## Relationship to prior work
Skrzypek, *On the \(L_p\) norm of the Rademacher projection and related inequalities* (first available February 25, 2009; DOI below), establishes exact three-coordinate formulas and analyzes related complementary projections. This enclosure is for the four-coordinate first-chaos projection on the real fourth-power space, not the three-coordinate projection or the complementary projection \(I-E\). The lower witness embeds the established three-coordinate mechanism; the rational Gram upper bound is a different four-coordinate statement. Generic Khintchine fourth-moment bounds provide much weaker upper control.

## Limitations
The upper bound may not be sharp and the exact norm is not determined. The statement concerns real scalars and precisely four independent symmetric signs; neither extension to complex data nor to arbitrary numbers of coordinates is claimed. Some specialized historical finite Rademacher-projection estimates may be absent from searchable sources; originality has not received independent audit.

## References
Lesław Skrzypek, *On the \(L_p\) norm of the Rademacher projection and related inequalities*, Proceedings of the American Mathematical Society **137** (2009), 2661–2669, https://doi.org/10.1090/S0002-9939-09-09875-X (first available 2009-02-25). Standard finite Walsh orthogonality and Sylvester's criterion are used directly as described in the proof.
