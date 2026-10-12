# A one-parameter exponential obstruction for local automorphisms of \(\pi_3\)
## Finding
Let \(\pi_3\) be the complex associative algebra with basis \(e_1,\ldots,e_5\) and nonzero products
\[
e_1^2=e_2,\qquad e_1e_2=e_2e_1=e_3,\qquad e_1e_4=e_5,\qquad e_4^2=e_5.
\]
For every \(\tau\in\mathbb C\), define
\[
\Phi_\tau(e_1)=-e_1,\quad
\Phi_\tau(e_2)=e_2,\quad
\Phi_\tau(e_3)=-e_3,\quad
\Phi_\tau(e_4)=\tau e_3-e_4,\quad
\Phi_\tau(e_5)=e_5.
\]
Then every \(\Phi_\tau\) is an algebra automorphism. In particular it is a local automorphism and its matrix lies in the plus component \(LocAut_+(\pi_3)\) used in Theorem 13 of the recent preprint arXiv:2511.17316v3.

For every \(\tau\ne0\), however,
\[
\Phi_\tau\notin\{\exp(\nabla):\nabla\in LocDer(\pi_3)\}.
\]
Consequently the equality asserted in Theorem 13,
\[
LocAut_+(\pi_3)=\{\exp(\nabla):\nabla\in LocDer(\pi_3)\},
\]
is false. The obstruction is sharp on this family: \(\Phi_0\) is the exponential of a genuine derivation.

## Assumptions and scope
The ground field is \(\mathbb C\). Matrices act on column coordinate vectors in the ordered basis \((e_1,e_2,e_3,e_4,e_5)\). The finding concerns only the algebra \(\pi_3\) and the surjectivity assertion in Theorem 13 of arXiv:2511.17316v3. It makes no claim about the analogous statement for \(\pi_2\).

The preprint was first public on 2025-11-21. Its current version v3 defines \(\pi_3\), gives the displayed matrix family for \(LocAut_+(\pi_3)\), gives a matrix description of local derivations, and states the exponential equality as Theorem 13. The proof below does not assume the sufficiency direction of that local-derivation classification: the matrix constraints needed for the obstruction are independently recovered as necessary conditions directly from the definition of a local derivation.

## Proof
First, \(\Phi_\tau\) is invertible because its matrix is triangular with diagonal entries \((-1,1,-1,-1,1)\). It preserves every nonzero defining product:
\[
\Phi_\tau(e_1)^2=e_2=\Phi_\tau(e_2),
\]
\[
\Phi_\tau(e_1)\Phi_\tau(e_2)=\Phi_\tau(e_2)\Phi_\tau(e_1)=-e_3=\Phi_\tau(e_3),
\]
\[
\Phi_\tau(e_1)\Phi_\tau(e_4)=(-e_1)(\tau e_3-e_4)=e_5=\Phi_\tau(e_5),
\]
and
\[
\Phi_\tau(e_4)^2=(\tau e_3-e_4)^2=e_5=\Phi_\tau(e_5),
\]
because all products involving \(e_3\) on either side vanish. The remaining basis products are zero and remain zero. Hence \(\Phi_\tau\in Aut(\pi_3)\subseteq LocAut(\pi_3)\). Its matrix has the plus sign in the \((3,3)\) entry, so it lies in the source's \(LocAut_+(\pi_3)\).

Now let \(L\) be an arbitrary local derivation. Directly solving the Leibniz equations for ordinary derivations gives a six-dimensional derivation space. If \(v\in\pi_3\), locality forces
\[
L(v)\in\{D(v):D\in Der(\pi_3)\}.
\]
Applying this necessary condition to the ten vectors
\[
(0,0,0,0,1),\ (0,0,0,1,-1),\ (0,0,1,-1,-1),\ (0,0,1,0,-1),\ (0,0,1,0,0),
\]
\[
(0,1,-1,-1,-1),\ (0,1,-1,0,-1),\ (0,1,-1,0,0),\ (1,-1,-1,-1,-1),\ (1,-1,-1,0,-1)
\]
and eliminating the six derivation parameters yields the seven-dimensional necessary matrix space
\[
A=
\begin{pmatrix}
x&0&0&0&0\\
p&2x&0&0&0\\
r&q&3x&s&0\\
0&0&0&x&0\\
t&0&0&u&2x
\end{pmatrix}.
\]
This exact elimination is reconstructed in `artifacts/verify.py`; it agrees with the matrix form stated in Theorem 9 of the source, but only the independently verified necessity is used here.

On the invariant subspace spanned by \(e_3,e_4,e_5\), the \(e_3,e_4\) block relevant to the coefficient of \(e_3\) in \(\exp(A)e_4\) is
\[
\begin{pmatrix}3x&s\\0&x\end{pmatrix}.
\]
For \(x\ne0\), its exponential has off-diagonal entry
\[
s\,\frac{e^{3x}-e^x}{2x}.
\]
Suppose that \(\exp(A)=\Phi_\tau\). Comparing the first diagonal entry gives \(e^x=-1\), so \(x\ne0\) and \(e^{3x}=(e^x)^3=-1\). Therefore the displayed off-diagonal entry is zero. But the \((3,4)\) entry of \(\Phi_\tau\) is \(\tau\). Thus \(\tau\ne0\) is impossible.

Finally, the boundary case is attained. The diagonal operator
\[
D_0=\operatorname{diag}(i\pi,2i\pi,3i\pi,i\pi,2i\pi)
\]
is a derivation, as follows immediately from the degrees of the four nonzero products, and
\[
\exp(D_0)=\Phi_0.
\]
This proves both the counterfamily and the sharpness statement.

## Verification
`artifacts/verify.py` uses exact SymPy arithmetic to reconstruct \(Der(\pi_3)\) from all basis Leibniz identities, obtaining dimension \(6\). It then imposes the pointwise local-derivation condition on the ten displayed vectors and computes the intersection exactly; the resulting necessary space has dimension \(7\) and equals the displayed matrix family.

The same script symbolically verifies that \(\Phi_\tau\) preserves all \(25\) ordered basis products for an indeterminate \(\tau\). It verifies the differential equation for the displayed triangular exponential block, checks the vanishing at \(e^x=-1\), and verifies directly that \(D_0\) is a derivation with \(\exp(D_0)=\Phi_0\). The replay output in `artifacts/verification_output.txt` ends with `CHECK_OK`.

The computation is finite exact linear algebra and symbolic differentiation; no finite sampling is used to infer an infinite statement. The ten-vector calculation supplies only a necessary condition for local derivations, which is all the non-exponential argument requires.

## Relationship to prior work
Arzikulov, Khakimov and Qurbonov, arXiv:2511.17316v3, is the direct source. Its Theorem 13 states the opposite surjectivity claim. In its proof the \((3,4)\) entry is written as a scalar function \(\lambda_{3,4}(x_1)\) times a free parameter, and the converse argument proceeds by choosing parameters after noting that the relevant infinite sums are bounded. Boundedness does not imply that these coefficients are nonzero. The exact closed form is
\[
\lambda_{3,4}(x)=\frac{e^{3x}-e^x}{2x},
\]
which vanishes whenever \(e^x=-1\). The family \(\Phi_\tau\) isolates precisely this missed resonance.

The earlier Cayley-algebra literature motivates comparing local automorphism groups and local derivation Lie algebras, but it concerns a different algebra and does not imply exponential surjectivity for \(\pi_3\). Exact-title, theorem-number, matrix-entry, exponential-surjectivity and correction/erratum searches located the current v3 preprint but no published correction or equivalent counterexample. Semantic literature searches likewise returned no statement covering this \(\pi_3\) resonance.

## Limitations
The finding refutes the surjectivity equality for \(\pi_3\); it does not classify the full exponential image of \(LocDer(\pi_3)\). It also does not assess the analogous theorem for \(\pi_2\). The motivating preprint is recent, so an unindexed contemporaneous correction could exist. The independent calculation proves exactly the local-derivation constraints needed for the obstruction, not a new full classification of all local derivations.

## References
1. F. Arzikulov, U. Khakimov, A. Qurbonov, “The relationship between local derivations and local automorphisms of some associative algebras,” arXiv:2511.17316v3, first public 2025-11-21; current revision 2026-08-07. https://arxiv.org/abs/2511.17316
2. Sh. Ayupov, A. Elduque, K. Kudaybergenov, “Local and 2-local automorphisms of Cayley algebras,” arXiv:2107.01147v1, 2021. https://arxiv.org/abs/2107.01147
