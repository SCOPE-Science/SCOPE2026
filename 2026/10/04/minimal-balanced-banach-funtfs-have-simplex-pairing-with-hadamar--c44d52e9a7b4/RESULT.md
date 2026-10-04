# Minimal balanced Banach FUNTFs have simplex pairing, with Hadamard realizations in \(\ell_1^n\)

## Finding
Let \(X\) be an \(n\)-dimensional real Banach space with \(n\ge 2\), and let \(\{(x_j,f_j)\}_{j=1}^N\subset X\times X^*\) be a balanced finite unit-norm tight frame (FUNTF):
\[
\lVert x_j\rVert=\lVert f_j\rVert=f_j(x_j)=1,
\qquad
\sum_{j=1}^N x_j=0,
\qquad
\sum_{j=1}^N f_j=0,
\]
and
\[
\sum_{j=1}^N x_j\otimes f_j=\lambda I_X.
\]
Then necessarily \(N\ge n+1\). If \(N=n+1\), then \(\lambda=(n+1)/n\) and the complete pairing matrix is forced:
\[
f_i(x_j)=
\begin{cases}
1,&i=j,\\
-1/n,&i\ne j.
\end{cases}
\]
Conversely, if a real Hadamard matrix of order \(n+1\) exists, then real \(\ell_1^n\) has a balanced FUNTF of the sharp minimum length \(n+1\). In particular, for every integer \(r\ge2\), real \(\ell_1^{2^r-1}\) has a minimum-length balanced FUNTF of length \(2^r\).

## Assumptions and scope
A Banach FUNTF here means a family satisfying the unit norm and norming conditions \(\lVert x_j\rVert=\lVert f_j\rVert=f_j(x_j)=1\) together with a scalar frame operator. Balanced means both vector and functional sums vanish. The lower bound and the rigidity statement apply to every finite-dimensional real Banach space. The existence statement is proved only in dimensions \(n\) for which a real Hadamard matrix of order \(n+1\) is available; it does not settle existence for every dimension or every length.

## Proof
Let \(T:\mathbb R^N\to X\) be the synthesis map \(Te_j=x_j\), and let \(\Phi:X\to\mathbb R^N\) be the analysis map \((\Phi x)_j=f_j(x)\). Tightness gives
\[
T\Phi=\lambda I_X.
\]
Hence \(T\) is onto and the vectors \(x_j\) span \(X\), so \(N\ge n\). If \(N=n\), the balance relation \(T\mathbf 1=0\) is a nontrivial linear dependence among exactly \(n\) spanning vectors, which is impossible. Therefore \(N\ge n+1\).

Now assume \(N=n+1\). Taking traces gives
\[
\lambda n=\operatorname{tr}(T\Phi)=\operatorname{tr}(\Phi T)=\sum_{j=1}^N f_j(x_j)=N,
\]
so \(\lambda=N/n=(n+1)/n\). Set \(A=\Phi T\), so \(A_{ij}=f_i(x_j)\). Since \(T\Phi=\lambda I_X\),
\[
A^2=\Phi(T\Phi)T=\lambda A.
\]
Moreover \(\operatorname{rank}A=n\). Balance gives \(A\mathbf 1=0\) and \(\mathbf 1^{\mathsf T}A=0\). Since \(A\) is an \((n+1)\)-by-\((n+1)\) matrix of rank \(n\), its right kernel and left kernel are both exactly the span of \(\mathbf 1\). Thus \(P=A/\lambda\) is the projection with kernel \(\operatorname{span}\{\mathbf 1\}\) and range \(\mathbf 1^\perp\), hence
\[
P=I-\frac1N\mathbf 1\mathbf 1^{\mathsf T}.
\]
Therefore
\[
A=\frac Nn\left(I-\frac1N\mathbf 1\mathbf 1^{\mathsf T}\right),
\]
which has diagonal entries \(1\) and off-diagonal entries \(-1/n\).

For the converse, let \(H\) be a real Hadamard matrix of order \(N=n+1\), normalized so that its first row is all \(1\)'s. Delete that row and call the resulting \(n\)-by-\(N\) sign matrix \(S=[s_1\ \cdots\ s_N]\). Hadamard orthogonality gives
\[
S\mathbf 1=0,
\qquad
SS^{\mathsf T}=NI_n.
\]
Define
\[
x_j=\frac1n s_j\in\ell_1^n,
\qquad
f_j(y)=s_j^{\mathsf T}y.
\]
Then \(\lVert x_j\rVert_1=1\), \(\lVert f_j\rVert_\infty=1\), and \(f_j(x_j)=1\). The row-sum identity gives both balance conditions, while
\[
\sum_{j=1}^N x_j\otimes f_j
=\frac1n SS^{\mathsf T}
=\frac Nn I_n.
\]
Thus the family is a balanced FUNTF of length \(n+1\), which is minimum by the first part. Sylvester Hadamard matrices of every order \(2^r\) give the asserted infinite family.

## Verification
The accompanying `verify.py` constructs Sylvester Hadamard matrices of orders \(2^r\) for \(2\le r\le8\) and checks with exact integer and rational arithmetic that the rows balance, the Banach norming conditions hold, the complete pairing matrix has diagonal \(1\) and off-diagonal \(-1/n\), and the frame operator is \((n+1)/n\) times the identity. It returns `VERIFY_OK sylvester_cases=7 r_range=2..8`. These finite checks are consistency tests only; the theorem for arbitrary \(n\) is proved analytically above.

## Relationship to prior work
Cheng and Heil define Banach FUNTFs and explicitly ask whether balanced FUNTFs of every admissible length exist in real \(\ell_1^n\). The result above does not solve that full existence problem: it identifies the universal sharp lower bound, proves a rigid simplex pairing law at the minimum length, and gives minimum-length realizations whenever a Hadamard matrix of order \(n+1\) exists. Earlier Banach-frame-potential work develops FUNTFs without this balanced minimum-length classification, while the balanced-frame literature found in the comparison search is Hilbert-space based. Hadamard constructions of tight Hilbert frames are also classical, but the Banach norming-functional realization and the forced pairing law above are the relevant additional ingredients here.

## Limitations
No claim is made that a Hadamard matrix exists for every order \(n+1\), nor that balanced FUNTFs exist for every \(N\ge n+1\). The theorem is real-valued. The exact pairing law is proved only at the minimum possible length \(N=n+1\); longer balanced FUNTFs can have different pairing matrices. The finite verifier does not establish any infinite family beyond the analytic Sylvester construction.

## References
Y.-S. Cheng and C. Heil, “Existence of Finite Unit-norm Tight Frames in Banach Spaces,” Graduate Journal of Mathematics 7 (2022), 17–38. Question 2.21 asks for balanced FUNTF existence in real \(\ell_1^n\).

J. A. Chávez-Domínguez, D. Freeman, and K. Kornelson, “Frame potential for finite-dimensional Banach spaces,” Linear Algebra and its Applications 578 (2019), 1–26; arXiv:1804.03677.

M. Heineken, P. Morillas, and A. Tarazaga, “Balanced frames: a useful tool in signal processing with good properties,” arXiv:1904.00920.
