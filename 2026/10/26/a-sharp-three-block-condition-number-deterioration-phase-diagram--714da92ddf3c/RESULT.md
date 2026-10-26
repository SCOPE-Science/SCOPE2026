# A sharp three-block condition-number deterioration phase diagram for rank-one block Jacobi

## Finding
For a real symmetric positive-definite rank-one spike \(A=I+vv^\top\), exact block-Jacobi symmetric preconditioning can increase rather than decrease its Euclidean spectral condition number. This cannot happen with at most two blocks. For three active blocks with squared spike energies \((s,s,t)\), \(s,t>0\), it happens **exactly** in the two regions
\[
0<t<s\quad\text{or}\quad s<t<\frac{s(4s+3)}{s+1}.
\]
Equality with the original condition number holds precisely on \(t=s\) and \(t=s(4s+3)/(s+1)\); improvement holds above the second boundary. Throughout this entire two-parameter family the condition-number ratio is strictly below \(3/2\), and its supremum \(3/2\) is sharp as \(s\to\infty\) with \(t=\sqrt{s}\). For example, the exact block-Jacobi preconditioner of
\[
A=\begin{pmatrix}5&4&2\\4&5&2\\2&2&2\end{pmatrix}
\]
produces condition number \(7+2\sqrt6>10=\kappa_2(A)\), despite using exact diagonal blocks.

## Assumptions and scope
Let \(d\ge2\), \(v\in\mathbb R^d\), and \(A=I_d+vv^\top\). Fix a partition of coordinates into \(b\) nonempty blocks, write \(v=(v_1,\ldots,v_b)\), and set \(q_j=\|v_j\|_2^2\). Define the exact block-Jacobi matrix \(P=\operatorname{blockdiag}(I+v_1v_1^\top,\ldots,I+v_bv_b^\top)\), and the symmetrically scaled SPD matrix \(S=P^{-1/2}AP^{-1/2}\). The condition number means \(\kappa_2(S)=\lambda_{\max}(S)/\lambda_{\min}(S)\), not the condition number of a nonsymmetric left-preconditioned representation. The motivating classification takes \(b=3\) and positive energies \((s,s,t)\); blocks may each have arbitrary positive dimension. All assertions are exact-arithmetic statements.

## Proof
**Block reduction.** On the one-dimensional direction \(e_j=v_j/\sqrt{q_j}\) in each positive-energy block, \(P_j\) acts by \(1+q_j\). It acts as the identity on the perpendicular subspace. Consequently, \(S\) is the identity on all these perpendicular subspaces, and its remaining eigenvalues are those of the explicit \(b\)-by-\(b\) matrix
\[
H_{ii}=1,\qquad H_{ij}=\sqrt{\frac{q_iq_j}{(1+q_i)(1+q_j)}}\quad(i\ne j).
\]
If \(v\ne0\) and \(d\ge2\), the unpreconditioned condition number is \(1+\sum_jq_j\).

**Two-block safety.** For \(b=2\) and energies \(x,y>0\), \(H\) has eigenvalues \(1\pm\theta\), where \(\theta=\sqrt{xy/((1+x)(1+y))}\). Hence
\[
\kappa_2(S)=\frac{1+\theta}{1-\theta}\le1+x+y=\kappa_2(A).
\]
The inequality follows by squaring the positive factors in \(\theta\le(x+y)/(x+y+2)\):
\[
(x+y)^2(1+x)(1+y)-xy(x+y+2)^2=(x-y)^2(x+y+1)\ge0.
\]
Equality holds exactly when \(x=y\). Zero-energy blocks follow directly by continuity.

**Three-block spectrum.** Put \(q_1=q_2=s\), \(q_3=t\), and \(K=1+2s+t\). The reduced matrix is
\[
H=\begin{pmatrix}1&a&c\\a&1&c\\c&c&1\end{pmatrix},\quad
 a=\frac{s}{1+s},\quad c=\sqrt{\frac{st}{(1+s)(1+t)}}.
\]
The antisymmetric eigenvector \((1,-1,0)\) gives \(\lambda_0=1/(1+s)\). The orthogonal symmetric two-dimensional subspace gives
\[
\lambda_\pm=\frac{2+3s\pm\sqrt{\Delta}}{2(1+s)},\quad
\Delta=s^2+\frac{8st(1+s)}{1+t}.
\]
Writing \(B=2+3s\), direct factorization shows
\[
\Delta-9s^2=\frac{8s(t-s)}{1+t}.
\]
Thus the smallest eigenvalue is \(\lambda_0\) when \(t\le s\), and \(\lambda_-\) when \(t\ge s\); the largest is always \(\lambda_+\). Extra unit eigenvalues from larger blocks never change these extrema. Therefore
\[
\kappa_2(S)=\begin{cases}
(B+\sqrt\Delta)/2,&t\le s,\\[2pt]
(B+\sqrt\Delta)/(B-\sqrt\Delta),&t\ge s.
\end{cases}
\]
For \(t<s\), comparison with \(K\) reduces to the positive difference
\[
\Delta-(s+2t)^2=\frac{4t(s-t)(2s+t+1)}{1+t}>0.
\]
For \(t>s\), comparison with \(K\) is equivalent, after positive-factor cross multiplication, to the sign of
\[
\Delta(K+1)^2-B^2(K-1)^2
=\frac{4(t-s)(2s+t+1)[s(4s+3)-(s+1)t]}{1+t}.
\]
These formulas establish the claimed exact strict/equality/improvement regions.

**Sharp \(3/2\) ceiling within the family.** If \(t\le s\), then \(\Delta\le9s^2\) and \(\kappa_2(S)\le1+3s<3K/2\). If \(t>s\), the desired bound is equivalent to \(B(3K-2)>(3K+2)\sqrt\Delta\). Both sides are positive; their squared difference admits the strictly positive certificate
\[
\begin{aligned}
&B^2(3K-2)^2-\Delta(3K+2)^2\\
&=\frac{4(2s+t+1)}{1+t}
\bigl[9s(t-s)^2+27s^3+41s^2+(s-3t)^2+13s+6t+1\bigr]>0.
\end{aligned}
\]
For \(s=L^2\), \(t=L\), with \(L\to\infty\), the first-case formula gives \(\kappa_2(S)/(1+2s+t)\to3/2\), proving sharpness.

**Exact witness.** For \(v=(2,2,1)\) and singleton blocks, \(P=\operatorname{diag}(5,5,2)\), while \(A=I+vv^\top\) has eigenvalues \(1,1,10\). The eigenvalues of \(S\) are \(1/5,(7-2\sqrt6)/5,(7+2\sqrt6)/5\); hence \(\kappa_2(S)=7+2\sqrt6\), which is strictly greater than \(10\).

## Verification
Run `python VERIFY.py` with Python 3.10+, SymPy, and NumPy. It uses exact symbolic identities for all critical factorizations and the explicit witness, plus 1,800 reproducible seeded finite floating-point eigensystem comparisons and a sharpness sequence. The mathematical proof above is independent of numerical sampling; the tests do not certify uncountably many parameters.

## Relationship to prior work
Vitale, Meanti, Rando, Ayuso de Dios, and Rosasco (2026) motivate the use of block Jacobi by defining it explicitly as an exact baseline for the sketched BLOKS preconditioner in their Appendix B, equation (28). The theorem here addresses this **exact baseline only**, not BLOKS's sketched approximation or its convergence runtime. Demmel (2023) studies general near-optimal block-Jacobi scaling; these general bounds do not themselves provide the specialized rank-one three-block deterioration regions or the sharp \(3/2\) ceiling proved here. Kolotilina (2004) gives the known two-block eigenvalue pairing \(1\pm\sigma\), so the two-block formula is background rather than a separately claimed discovery. Kolotilina (2002) addresses general optimal block scaling but its full text was not available for detailed implication comparison. No mathematical uniqueness is claimed from absence of a search hit.

## Limitations
The sharp \(3/2\) ceiling is established **only** for the three-block family with energies \((s,s,t)\); it is not a universal bound for all block partitions or all SPD matrices. The precise phase diagram assumes two equal positive block energies and one independently varying positive energy. Nothing is proved about approximate, randomized, low-precision, or nonsymmetric preconditioners, nor about wall-clock performance of iterative solvers. Earlier specialized results may exist in less accessible matrix-scaling literature.

## References
1. G. Vitale, G. Meanti, M. Rando, B. Ayuso de Dios, and L. Rosasco, *BLOKS: Scaling Kernel Solvers with Sketched Block Preconditioning*, arXiv:2610.13382v1 (first posted 2026-10-09), https://arxiv.org/abs/2610.13382 .
2. J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications 44 (2023), 408–413, https://doi.org/10.1137/22M1504901 .
3. L. Yu. Kolotilina, *A Class of Optimally Conditioned Block 2 × 2 Matrices*, Journal of Mathematical Sciences 121 (2004), 2474–2480, https://doi.org/10.1023/B:JOTH.0000026285.08558.74 .
4. L. Yu. Kolotilina, *Optimally Conditioned Block Matrices*, Linear Algebra and its Applications 340 (2002), 55–67, https://doi.org/10.1016/S0024-3795(01)00412-8 .
