# Arithmetic rank resonance in cyclic finite-field line sampling

## Finding
Let \(q\) be a prime power, \(d\ge3\), and \(w_i\in\mathbb F_q^\times\) for every cyclic edge \(i\leftrightarrow i+1\). Let \(B\) have zero diagonal and entries \(B_{i,i+1}=B_{i+1,i}=w_i\) with cyclic indices, and every other entry zero. The ambient bilinear form is permitted to be degenerate. Let \(E=\{0\}\cup\{se_i:1\le i\le d,\ s\in\mathbb F_q^\times\}\), and for any nontrivial additive character \(\psi\) put
\[
M=(\psi(x^\top By))_{x,y\in E}.
\]
The matrix has order \(1+d(q-1)\). If \(d\) is odd it is invertible. If \(d=2m\) is even, write
\[
r=\frac{w_1w_3\cdots w_{d-1}}{w_2w_4\cdots w_d},\qquad h=\operatorname{ord}_{\mathbb F_q^\times}(r).
\]
Its complex nullity is
\[
\nu(M)=\begin{cases}
2(q-1)/h,&m\text{ even};\\
2(q-1)/h,&m\text{ odd and }h\text{ even};\\
0,&m\text{ odd and }h\text{ odd}.
\end{cases}
\]
In particular, odd cycles give exact reconstruction; cycles with four-divisible length always lose information, while cycles with length two modulo four lose information precisely when the alternating edge-product ratio has even multiplicative order. This exhibits a field-arithmetic obstruction not determined solely by the ordinary rank of the bilinear-form matrix.

## Assumptions and scope
The field may have characteristic two. All edge weights are nonzero, and the edge set is a simple undirected cycle with \(d\ge3\). The same nontrivial additive character is used for all matrix entries; its choice does not affect rank. The theorem concerns the finite self-sampling matrix indexed by the full union of coordinate axes. If \(B\) is invertible, this is a principal restricted Fourier matrix for the nondegenerate pairing \((x,y)\mapsto x^\top By\); the stated formula remains valid when \(B\) is singular, without calling the ambient transform nondegenerate.

## Proof
Put \(N=q-1\). An input vector on \(E\) consists of a coefficient at the origin and functions \(f_j:\mathbb F_q^\times\to\mathbb C\), one for each axis. Subtract the output row indexed by the origin from every row indexed by a nonzero axis point. The origin row determines the origin coefficient after all axis coefficients have been fixed. Thus the total rank is one plus the rank of the axis-to-axis difference operator
\[
(Tf)_i(s)=\sum_{j=1}^d\sum_{t\ne0}(\psi(B_{ij}st)-1)f_j(t).
\]
Decompose each axis function by the multiplicative characters \(\chi\) of \(\mathbb F_q^\times\). For nontrivial \(\chi\), the constant term in \(T\) disappears. If \(B_{ij}\ne0\), substitution \(u=B_{ij}st\) gives
\[
\sum_{t\ne0}\psi(B_{ij}st)\chi(t)=G(\chi,\psi)\chi(B_{ij})^{-1}\chi(s)^{-1},
\]
where the Gauss sum \(G(\chi,\psi)\ne0\). For \(B_{ij}=0\), the sum vanishes. The \(\chi\)-input block is therefore a nonzero scalar multiple of the matrix \(C_\chi\) whose nonzero entries on the cycle are \(\chi(w_i)^{-1}\), mapping to the \(\chi^{-1}\)-output block. For the trivial character, \(\sum_{t\ne0}(\psi(B_{ij}st)-1)=-q\) when \(B_{ij}\ne0\), and zero otherwise; hence its block is \(-qC_1\). All blocks use distinct input and output character spaces. Consequently
\[
\operatorname{rank}M=1+\sum_{\chi\in\widehat{\mathbb F_q^\times}}\operatorname{rank}C_\chi.
\tag{1}
\]
For odd \(d\), an admissible determinant permutation on a zero-diagonal weighted cycle must traverse the entire odd cycle; the two orientations contribute equally. Therefore \(\det C_\chi=2\prod_i\chi(w_i)^{-1}\ne0\) over \(\mathbb C\), and (1) gives full rank.

For \(d=2m\), order vertices by parity. Then \(C_\chi=\left(\begin{smallmatrix}0&R_\chi\\R_\chi^\top&0\end{smallmatrix}\right)\), where \(R_\chi\) is a cyclic bidiagonal \(m\times m\) matrix. Its determinant has precisely two matching terms,
\[
\det R_\chi=\chi(w_1w_3\cdots w_{d-1})^{-1}+(-1)^{m-1}\chi(w_2w_4\cdots w_d)^{-1}.
\]
Thus \(R_\chi\) is singular precisely if \(\chi(r)=(-1)^m\). In that case its rank is exactly \(m-1\): deleting a suitable row and adjacent column leaves a triangular \((m-1)\)-minor with nonzero edge-weight product. Otherwise it has rank \(m\). So each singular character contributes exactly two null directions to \(C_\chi\).

The finite multiplicative group is cyclic of order \(N\). Evaluation at an element \(r\) of order \(h\) maps its \(N\) multiplicative characters onto all \(h\)-th roots of unity, with each value occurring \(N/h\) times. For even \(m\), the required value is \(+1\), so there are \(N/h\) singular blocks. For odd \(m\), the required value is \(-1\), which appears precisely when \(h\) is even, again \(N/h\) times. Substituting into (1) proves the nullity and rank assertions.

## Verification
A standalone reproducibility program `verify.py` directly forms the complex matrices and compares numerical rank with the exact formula for 184 prime-field cases, and uses exact characteristic-two trace values for 18 tests over \(\mathbb F_4\). The program is corroborative; the complete proof holds for all prime powers, cycle lengths, and nonzero weights. The analytic proof does not require a floating-point rank tolerance.

## Relationship to prior work
Finite-field restriction theory and nonzero Gauss-sum evaluation are classical. Mockenhaupt–Tao (2002/2010) study finite-field Fourier restriction and Kakeya phenomena, while Iosevich–Koh (2008) develop extension estimates for quadratic surfaces and record finite-field Gauss-sum tools. Neither paper's inspected restriction theorems provides this finite-union-of-axes, weighted-cycle principal sampling-rank classification. The result uses that harmonic toolkit but answers an exact interpolation/rank question rather than a norm-estimate question. Earlier cyclic-matrix and finite Fourier sampling literature could contain an equivalent block decomposition; that possibility is not excluded.

## Limitations
The theorem is confined to a full coordinate-axis union with a cycle-sparse symmetric pairing and nonzero weights. It does not classify arbitrary sparse graphs, partial axis sampling, conditioning, or higher-dimensional subspace unions. For singular ambient bilinear forms, the statement is about the displayed character matrix, not invertibility of the ambient Fourier transform. Numerical checks cover finitely many examples only. No independent mathematical audit has been performed.

## References
- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (first posted 2008-04-28).
- G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, version dated 2010-03-21.
