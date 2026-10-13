# The eight-site uniform \(XY\) chain admits exact uniform average mixing under random readout
## Finding
Let \(P_8\) be the path on eight vertices, equivalently the single-excitation sector of the uniformly coupled eight-site \(XY\) chain. There exists a probability distribution supported on at most \(17\) readout times \(t_j\in\mathbb R\) such that the averaged mixing matrix is exactly \(J/8\).

This resolves the first modulus left open by the arithmetic classification in arXiv:2609.14463v1. In that notation \(N=8\) and \(q=N+1=9\): \(q\) is neither a power of two, a prime, nor twice a prime, and it is not covered by the paper's parity-collision obstruction families.

## Assumptions and scope
The Hamiltonian is the adjacency matrix of \(P_8\), with eigenvalues
\[
\theta_r=2\cos\!\left(\frac{r\pi}{9}\right),\qquad 1\le r\le 8.
\]
For a readout-time law \(\mu\), define
\[
y_{rs}=\int_{\mathbb R}\cos\!\bigl((\theta_r-\theta_s)t\bigr)\,d\mu(t).
\]
As in the cited source, the averaged mixing matrix is
\[
\widehat M[\mu]=D_0+2\sum_{r<s}y_{rs}\,E_r\circ E_s,
\qquad
D_0=\sum_r E_r\circ E_r.
\]
The claim concerns existence of an exact time distribution. It does not give explicit numerical readout times; their existence follows from a finite phase certificate plus the dense one-parameter phase flow.

## Proof
For \(q=9\),
\[
\theta_1=\theta_2+\theta_4.
\]
Moreover \(\theta_2=\theta_1^2-2\), while \(\theta_1\) satisfies the irreducible cubic
\[
\theta_1^3-3\theta_1-1=0.
\]
Hence \(1,\theta_1,\theta_2\) are linearly independent over \(\mathbb Q\), so the single relation among the four positive eigenvalues is \(\theta_1-\theta_2-\theta_4=0\).

The closure of the positive-mode phase flow is therefore the three-torus
\[
\mathcal T=
\left\{
(\phi_1,\phi_2,\phi_3,\phi_4):
\phi_1=\phi_2+\phi_4\pmod{2\pi}
\right\},
\]
with negative modes extended by \(\phi_{9-r}=-\phi_r\). Write
\[
\phi_2=\frac{\pi a}{2},\qquad
\phi_3=\frac{\pi b}{2},\qquad
\phi_4=\frac{\pi c}{2},
\]
for \(a,b,c\in\{0,1,2,3\}\), and \(\phi_1=\phi_2+\phi_4\). On these \(64\) phase points assign probability \(W_{abc}/256\), where the four \(4\times4\) slices \(W_a=(W_{abc})_{b,c}\) are
\[
W_0=
\begin{pmatrix}
1&1&14&1\\
1&11&1&1\\
1&1&4&1\\
1&23&1&1
\end{pmatrix},
\quad
W_1=
\begin{pmatrix}
1&1&1&3\\
1&1&13&1\\
13&1&1&1\\
1&1&5&13
\end{pmatrix},
\]
\[
W_2=
\begin{pmatrix}
17&1&14&1\\
1&17&1&1\\
1&1&4&1\\
1&1&1&1
\end{pmatrix},
\quad
W_3=
\begin{pmatrix}
1&1&1&1\\
1&1&1&1\\
1&19&1&17\\
21&1&1&1
\end{pmatrix}.
\]
All \(64\) weights are strictly positive and their numerators sum to \(256\). Exact quarter-turn arithmetic gives, for every \(1\le r<s\le8\),
\[
\sum_{a,b,c}\frac{W_{abc}}{256}
\cos(\phi_r-\phi_s)
=
\begin{cases}
-\frac18,&s-r\ \text{even},\\
0,&s-r\ \text{odd}.
\end{cases}
\]

These are sufficient for exact uniform average mixing. Indeed, if
\[
\mathcal E=\sum_{\substack{r<s\\s-r\ {\rm even}}}E_r\circ E_s,
\]
then the path identities
\[
D_0+2\mathcal E=\frac12(I+\widetilde I),
\qquad
D_0=\frac{2J+I+\widetilde I}{18}
\]
give
\[
D_0-\frac14\mathcal E=\frac18J.
\]

It remains to pass from a phase law on \(\mathcal T\) to an actual readout-time law. The \(28\) pair differences restrict to \(16\) distinct nonzero cosine characters on \(\mathcal T\). These characters are linearly independent as real trigonometric functions, so \(\operatorname{aff}Y(\mathcal T)\) has dimension \(16\), where
\[
Y(\phi)=\bigl(\cos(\phi_r-\phi_s)\bigr)_{r<s}.
\]
The \(64\) quarter-turn points above also have exact affine rank \(16\). Because every listed weight is positive, their barycenter \(Y^\star\) lies in the relative interior of their convex hull, and hence in \(\operatorname{relint}\operatorname{conv}Y(\mathcal T)\).

Kronecker density makes the actual time-phase curve dense in \(\mathcal T\). In finite dimensions, a convex set and its closure have the same relative interior. Therefore \(Y^\star\) belongs to the convex hull of the actual time coherence curve, not merely to its closure. Carathéodory's theorem in the \(16\)-dimensional affine hull then gives an exact representation by at most \(17\) readout times.

## Verification
`artifacts/verify.py` performs exact rational/integer checks of the finite certificate. It verifies that all \(64\) weights are positive, that they sum to \(1\), that all \(28\) required pair moments equal \(0\) or \(-1/8\) according to parity, that the quarter-turn coherence vectors have affine rank \(16\), and that the restricted pair characters form exactly \(16\) nonzero cosine classes. Running the packaged script prints `VERIFY_OK`.

The cubic relation and Kronecker-torus description are analytic. The finite certificate is used only for the finite phase barycenter and rank statement; it is not being extrapolated as an infinite computation.

## Relationship to prior work
Baptista, Coutinho, and Marques introduced generalized average mixing under arbitrary sampling distributions and exhibited uniform average mixing for small paths, including \(P_3\) and \(P_4\). Kang later proved a specific obstruction for \(P_{11}\).

The 2026 arithmetic paper arXiv:2609.14463v1 proves uniform average mixing when \(q=N+1\) is a power of two, a prime, or twice a prime, and proves nonexistence for three parity-collision families. It explicitly states that the remaining moduli are undecided. The present result settles \(q=9\), the smallest such modulus, positively. Its certificate also shows that rational dependence of the positive Bohr frequencies does not by itself obstruct exact randomized uniform mixing.

## Limitations
The proof is specific to \(q=9\). It does not classify other unresolved composite moduli, and it does not supply closed-form readout times. The \(17\)-point support bound is existential; it follows from relative-interior membership and Carathéodory rather than from an explicit time list.

The phase certificate does not imply instantaneous uniform mixing, nor does it assert pretty good state transfer. It only proves exact uniformity after averaging over a suitable finite random readout law.

## References
1. M. Kang, *Arithmetic of Bohr Frequencies Governs Uniform Mixing in Randomly Timed Quantum Spin Chains*, arXiv:2609.14463v1 (2026).
2. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1; Quantum Information Processing 23, 272 (2024), DOI:10.1007/s11128-024-04480-0.
3. M. Kang, *An Exact Obstruction to Uniform Average Mixing on \(P_{11}\)*, arXiv:2607.25490v1 (2026).
