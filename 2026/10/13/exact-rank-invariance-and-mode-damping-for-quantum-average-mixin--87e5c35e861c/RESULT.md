# Exact rank invariance and mode damping for quantum average mixing under pendant extension

## Finding
For a real symmetric \(n\)-by-\(n\) matrix \(A\), adjoin one pendant coordinate to each original coordinate, all coupled by the same \(g>0\). In original/pendant layer ordering the enlarged Hamiltonian is
\[
H_g=\begin{pmatrix}A&gI_n\\gI_n&0\end{pmatrix}.
\]
For a matrix \(B\), define its continuous-time Cesàro quantum average mixing as
\[
\widehat M(B)=\lim_{T\to\infty}\frac1T\int_0^T e^{itB}\circ e^{-itB}\,dt.
\]
The Schur product \(\circ\) is entrywise multiplication. If \(A=\sum_{\theta\in\Theta}\theta E_\theta\) is its decomposition over *distinct* eigenvalues, set
\[
Q_\theta=E_\theta\circ E_\theta,\quad
S=\sum_{\theta\in\Theta}Q_\theta,\quad
T_g=\sum_{\theta\in\Theta}\frac{\theta^2}{\theta^2+4g^2}Q_\theta.
\]
Then the following exact block identity holds for every allowed \(A,g\):
\[
\boxed{\widehat M(H_g)=\frac12\begin{pmatrix}S+T_g&S-T_g\\S-T_g&S+T_g\end{pmatrix}.}
\]
Consequently the constant orthogonal layer transform \(2^{-1/2}\begin{psmallmatrix}I&I\\I&-I\end{psmallmatrix}\) conjugates \(\widehat M(H_g)\) to \(S\oplus T_g\). In particular,
\[
\boxed{\operatorname{rank}\widehat M(H_g)=\operatorname{rank}S+\operatorname{rank}\!\left(\sum_{\theta\ne0}Q_\theta\right),}
\]
which is independent of the numerical value of \(g>0\). Moreover \(\widehat M(H_{g_1})-\widehat M(H_{g_2})\) is positive semidefinite whenever \(0<g_1<g_2\); equivalently, only the antisymmetric layer mode block is damped, monotonically. The kernel consists exactly of symmetric layer vectors determined by \(\ker S\) and antisymmetric layer vectors determined by \(\bigcap_{\theta\ne0}\ker Q_\theta\).

For nonsingular \(A\), the rank doubles: \(\operatorname{rank}\widehat M(H_g)=2\operatorname{rank}\widehat M(A)\). Every matrix \(H_g\) is nonsingular irrespective of \(A\); therefore *each additional* uniform pendant extension after the first doubles the rank again (using any positive coupling at each stage).

For the standard path \(P_m\), \(m\ge1\), its pendant extension (a path comb) has average-mixing rank exactly \(m\) on \(2m\) vertices. For \(K_n\), \(n\ge3\), the extended matrix is positive definite, with sharp smallest eigenvalue
\[
\boxed{\lambda_{\min}(\widehat M(K_n\circ_gK_1))=\frac{n-2}{n(1+4g^2)}.}
\]

## Assumptions and scope
The matrix \(A\) is any finite real symmetric matrix (graph adjacency is the intended case); its eigenvalues are real and its eigenspace projectors are orthogonal. Pendant coupling \(g\) is homogeneous and strictly positive. The graph corona \(G\circ K_1\) attaches exactly one leaf to every base vertex, not a single leaf to one designated vertex. The evolution is the unweighted adjacency walk on the base and a uniform weighted adjacency walk on the enlarged graph. All limits are infinite-time Cesàro averages; they are not instantaneous or finite-horizon mixing claims. If \(0\) occurs in the base spectrum, its projector contributes to \(S\) but not \(T_g\).

## Proof
**Spectral splitting.** For each distinct base eigenvalue \(\theta\), the enlarged invariant eigenspaces reduce to the symmetric \(2\)-by-\(2\) matrix \(B_\theta=\begin{psmallmatrix}\theta&g\\g&0\end{psmallmatrix}\). Put \(d_\theta=\sqrt{\theta^2+4g^2}\), \(a_\theta=\theta/d_\theta\) and \(b_\theta=2g/d_\theta\). Its two eigenvalues are
\[
\lambda_{\theta,\pm}=\frac{\theta\pm d_\theta}{2},
\]
with orthogonal spectral projectors
\[
P_{\theta,\pm}=\frac12\begin{pmatrix}1\pm a_\theta&\pm b_\theta\\\pm b_\theta&1\mp a_\theta\end{pmatrix}.
\]
Because \(g>0\), the positive branch is strictly positive and the negative branch strictly negative. Differentiating either branch with respect to \(\theta\) gives \((1\pm\theta/d_\theta)/2>0\). Consequently all \(2|\Theta|\) branch eigenvalues are distinct; degeneracies *within* a fixed base eigenspace are already incorporated in its single projector \(E_\theta\). The full spectral projectors are \(E_\theta\otimes P_{\theta,\pm}\), with the tensor factors reordered into the two coordinate layers.

**Time averaging.** For any real symmetric \(B=\sum_\lambda\lambda F_\lambda\) with distinct spectral levels, integrating the phase differences shows, entrywise,
\[
\widehat M(B)=\sum_\lambda F_\lambda\circ F_\lambda,
\]
with no unwanted cross terms because the Cesàro mean of \(e^{it(\lambda-\mu)}\) vanishes for \(\lambda\ne\mu\). For fixed \(\theta\), the sum of the two layer Schur squares is
\[
P_{\theta,+}\circ P_{\theta,+}+P_{\theta,-}\circ P_{\theta,-}
=\frac12\begin{pmatrix}1+a_\theta^2&1-a_\theta^2\\1-a_\theta^2&1+a_\theta^2\end{pmatrix}.
\]
Here \(a_\theta^2=\theta^2/(\theta^2+4g^2)\). Multiplying entrywise by \(E_\theta\circ E_\theta\), then summing \(\theta\), gives the displayed block formula.

**Rank, kernel, and monotonicity.** The fixed orthogonal layer transform yields \(S\oplus T_g\). By the Schur product theorem each \(Q_\theta\) is positive semidefinite. For any finite family of positive-semidefinite matrices with *strictly positive* coefficients, the kernel of their sum equals the intersection of their kernels, since \(x^TQx=0\) is equivalent to \(Qx=0\). Thus
\[
\ker T_g=\bigcap_{\theta\ne0}\ker Q_\theta,
\qquad \ker S=\bigcap_{\theta}\ker Q_\theta,
\]
independent of \(g>0\). The full kernel is \(\{(z,z):z\in\ker S\}+\{(w,-w):w\in\ker T_g\}\); the sum is orthogonal. If \(A\) has no zero eigenvalue, the intersections coincide and the rank doubles. For \(0<g_1<g_2\), each coefficient \(\theta^2/(\theta^2+4g^2)\) decreases (strictly for \(\theta\ne0\)), so \(T_{g_1}-T_{g_2}\succeq0\), proving the Loewner monotonicity. Lastly, \(H_g(u,v)=0\) implies \(gu=0\) from the second block row and then \(gv=0\) from the first, proving every enlarged matrix nonsingular and justifying iteration.

**Path combs.** The normalized path eigenvectors are
\[
(v_k)_x=\sqrt{\frac2{m+1}}\sin\left(\frac{\pi kx}{m+1}\right),\quad 1\le k,x\le m.
\]
Every projector is rank one, so \(Q_{\theta_k}=(v_k\circ v_k)(v_k\circ v_k)^T\). Reflection in the spectral index gives \(v_k\circ v_k=v_{m+1-k}\circ v_{m+1-k}\). The distinct squared profiles indexed by \(1\le k\le\lceil m/2\rceil\) are linearly independent: put \(r=\lceil m/2\rceil\) and \(t_x=\cos(2\pi x/(m+1))\) for \(1\le x\le r\). These \(r\) nodes are distinct and are all strictly less than \(1\). The squared profile \(v_k(x)^2\) is a nonzero common scalar multiple of \(1-T_k(t_x)=(1-t_x)R_{k-1}(t_x)\), where \(T_k\) is the ordinary Chebyshev polynomial of degree \(k\) and \(R_{k-1}\) has exact degree \(k-1\). The \(r\times r\) evaluation matrix is a nonsingular Vandermonde-type matrix because the polynomials \(R_0,\ldots,R_{r-1}\) have strictly increasing degrees and nonzero leading coefficients; the common factors \(1-t_x\) are nonzero. Thus the profiles are independent. Thus \(\operatorname{rank}S=\lceil m/2\rceil\). For odd \(m\), precisely the middle index \(k=(m+1)/2\) gives the zero eigenvalue; deleting its squared profile lowers the rank by exactly one, while for even \(m\) none is removed. Therefore \(\operatorname{rank}T_g=\lfloor m/2\rfloor\), and the enlarged rank is \(m\).

**Clique gap.** For \(A(K_n)=J_n-I_n\), the spectral projectors are \(E_+=J_n/n\) at eigenvalue \(n-1\) and \(E_-=I_n-J_n/n\) at eigenvalue \(-1\). Define \(c_-=1/(1+4g^2)\), \(c_+=(n-1)^2/((n-1)^2+4g^2)\). Then
\[
S=\left(1-\frac2n\right)I_n+\frac2{n^2}J_n,\qquad
T_g=c_-\left[\left(1-\frac2n\right)I_n+\frac1{n^2}J_n\right]+\frac{c_+}{n^2}J_n.
\]
On the \(n-1\) dimensional subspace orthogonal to the all-ones vector, the eigenvalues of \(S,T_g\) are \(1-2/n\) and \(c_-(1-2/n)\), respectively. On the all-ones vector the eigenvalues are \(1\) and \(c_-(1-1/n)+c_+/n\); the latter exceeds \(c_-(1-2/n)\). For \(n\ge3\) all are positive, and the claimed smallest eigenvalue follows exactly.

## Verification
The accompanying standalone `verify.py` implements a second construction using independent eigendecomposition of each enlarged Hamiltonian; it checks graph families, randomly generated simple graphs, multiple strictly positive couplings, path-comb ranks, and the sharp clique gap. Run `python3 verify.py` with Python 3 and NumPy. Its successful local execution reported `VERIFY_OK numerical_graph_cases=288 path_cases=48 clique_gap_cases=27 max_abs_error=2.010e-14`. Finite floating-point tests corroborate the analytic identities; they do not establish them for infinitely many graphs or exact parameter values.

## Relationship to prior work
Ackelsberg, Brehm, Chan, Mundinger and Tamon, *Quantum State Transfer in Coronas* (arXiv:1605.05260), Proposition 3.2, already give the corona spectral eigenvalues and projectors used as input to the present derivation. Their conclusions concern state transfer, not the displayed average-mixing block decomposition, the coupling-invariant kernel/rank, Loewner order, or the quantitative clique and path-comb results. Godsil's 2013 average-mixing theorem and Coutinho et al., *Irrational quantum walks* (arXiv:2208.08971, Section 2), provide the Cesàro spectral-projector identity; the novelty considered here is the resulting exact pendant-extension structure, not either ingredient in isolation. An equivalent consequence hidden in general corona or mixing formulas cannot be entirely ruled out.

## Limitations
The result requires a real symmetric base Hamiltonian and uniform, nonzero pendant coupling. It does not classify arbitrary heterogeneous leaf couplings or finite-time mixing. The rank statement is for strictly positive couplings: the zero-coupling matrix has a separate degenerate structure and cannot be obtained merely by substituting \(g=0\) into the rank statement. The proof is mathematical; the accompanying floating-point calculations are only corroborative. The novelty comparison is not a claim of exhaustive coverage of all unpublished or unindexed work; independent review has not been performed.

## References
1. Ethan Ackelsberg, Zachary Brehm, Ada Chan, Joshua Mundinger, Christino Tamon, *Quantum State Transfer in Coronas*, Electronic Journal of Combinatorics 24 (2017), P2.24; first arXiv version May 17, 2016, arXiv:1605.05260, https://arxiv.org/abs/1605.05260 (especially Proposition 3.2).
2. Chris Godsil, *Average mixing of continuous quantum walks*, Journal of Combinatorial Theory, Series A 120 (2013), 1649–1662.
3. Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, Reinhard Werner, *Irrational quantum walks*, arXiv:2208.08971, first public August 18, 2022, https://arxiv.org/abs/2208.08971 (Section 2).
