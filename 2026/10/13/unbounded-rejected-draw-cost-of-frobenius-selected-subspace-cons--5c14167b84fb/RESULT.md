# Unbounded rejected-draw cost of Frobenius-selected subspace-constrained Kaczmarz

## Finding
For every real \(0<t\le\frac12\), the **exact minimizer** of the one-row Frobenius projected-residual criterion for the nonsingular system below incurs expected \((1+t^2)/t^2\) raw proposals before its first effective Kaczmarz update, while another admissible constrained row incurs only \(2+t^2\). Both solve the same prescribed system after **one accepted update**. Consequently, the proposal-count ratio diverges, even though the number of accepted steps is identical.

## Assumptions and scope
Let
\[
A_t=\begin{pmatrix}t^{-1}&0&0\\1&t&0\\0&0&1\end{pmatrix},\quad
x_\star=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad
b=A_tx_\star=\begin{pmatrix}0\\t\\0\end{pmatrix},\qquad 0<t\le\tfrac12.
\]
Its determinant is one. For a candidate singleton constraint \(I_p=\{j\}\), define \(P_j=I-A_j^\dagger A_j\), and minimize the row-interpolative criterion \(F_j=\|A_tP_j\|_F^2\). Start the linear solver at \(x_0^{(j)}=A_j^\dagger b_j\). Among the remaining rows, propose independently with replacement and probabilities
\[
q_{i\mid j}=\frac{\|P_j a_i\|_2^2}{\sum_{k\ne j}\|P_j a_k\|_2^2},\qquad i\ne j,
\]
where \(a_i\) is the transpose of row \(i\). Reject proposals whose row residual is zero and repeat until a nonzero residual is chosen. On acceptance, take the exact unit-relaxed projected Kaczmarz step
\[
x_+=x-\frac{a_i^{\mathsf T}x-b_i}{\|P_j a_i\|_2^2}P_j a_i.
\]
The count includes rejected raw proposals and the eventual accepted proposal. This is the singleton-row specialization of the projected-row-norm sampling in Sun–Qi–Han–Xie, Algorithm 1 and Remark 3.1, with its relaxation parameter \(\zeta=1\). The result assumes independent draws, exact zero-residual detection, and exact arithmetic.

## Proof
The three projected Frobenius objectives are exactly
\[
F_1=1+t^2,\qquad F_2=1+\frac1{1+t^2},\qquad
F_3=t^{-2}+1+t^2.
\]
Since \(t^2(1+t^2)\le5/16<1\), we have \(F_1<F_2\). Clearly \(F_1<F_3\). Thus the globally Frobenius-optimal singleton constraint is uniquely \(j=1\). The first row also has the largest unprojected Euclidean norm, so ordinary first-step row-CPQR selects it.

For \(j=1\), \(x_0^{(1)}=0\), \(P_1=\operatorname{diag}(0,1,1)\), and the two remaining projected rows are \(t e_2\) and \(e_3\). Only row two has a nonzero residual, and a raw draw selects it with probability
\[
q_{2\mid1}=\frac{t^2}{1+t^2}.
\]
The number of trials up to and including acceptance is geometric with mean \(W_1=(1+t^2)/t^2\). Its accepted step moves exactly to \(x_\star=e_2\).

For \(j=2\), writing \(v=(1,t,0)^{\mathsf T}\), we have \(P_2=I-vv^{\mathsf T}/(1+t^2)\) and \(x_0^{(2)}=tv/(1+t^2)\). Of the two remaining projected rows, row one has squared norm \(1/(1+t^2)\) and row three has squared norm one. The initial row-one residual equals \(1/(1+t^2)\ne0\), while the row-three residual is zero. Therefore
\[
q_{1\mid2}=\frac1{2+t^2},\qquad W_2=2+t^2.
\]
The accepted row-one step changes the iterate by \(x_\star-x_0^{(2)}\), and therefore terminates exactly. It follows that
\[
\frac{W_1}{W_2}=\frac{1+t^2}{t^2(2+t^2)}\longrightarrow+\infty.
\]
Finally, for either \(j=1\) or \(j=2\) the two remaining projected rows are orthogonal, with squared norms respectively \((t^2,1)\) and \((1/(1+t^2),1)\). Their squared singular-value-to-Frobenius ratios, exactly the one-step decrement in the standard unconditioned Kaczmarz contraction certificate, are
\[
1-\rho_1=\frac{t^2}{1+t^2}=\frac1{W_1},\qquad
1-\rho_2=\frac1{2+t^2}=\frac1{W_2}.
\]
Thus the certificate gap and the rejected-draw overhead have the same geometric mechanism. The derivation does not claim that the certificate is the accepted-step convergence rate: in this particular instance, conditioning on a nonzero row makes the accepted-step solution exact.

## Verification
Run `python verify.py` with Python 3 and SymPy. The standalone script independently constructs every projected matrix with exact rational arithmetic at \(t=1/k\) for integers \(2\le k\le74\), checks global Frobenius selection, raw acceptance probabilities, the exact accepted iterates, and the corresponding projected-row spectral ratios. The script prints `VERIFY_OK exact_rational_parameter_cases=73 row_policies=3`. The universal assertions are proved above, not inferred from finite tests.

## Relationship to prior work
Sun, Qi, Han and Xie (2026, arXiv:2605.29304v1, Algorithm 1 Step 2, Remark 3.1, Section 3.2 and Appendix 7.2) prescribe nonzero-residual resampling, squared projected-row-norm probabilities, and a Frobenius minimization surrogate for selecting the constrained rows. They establish convergence in accepted iterations and explain its dependence on projected singular values. Those ingredients are established prior work. The contribution here is the explicit **same-system, competing-constraint family** showing unbounded raw-proposal regret of their Frobenius surrogate, with exact formulas and identical one-accepted-step termination. Lok and Rebrova (arXiv:2309.04889v2, Algorithm 1 and Theorem 1.1) analyze the foundational constraint-based row projection with ordinary IID selection, without the present Frobenius-optimal-versus-alternative raw-draw comparison. Their subsequent SC-RCD framework (arXiv:2506.09394) treats a different coordinate-descent and low-rank-matrix selection strategy. Their general analysis is not claimed as new.

## Limitations
The pathological quantity is the number of independent row **proposals**, not the accepted-iteration count. An implementation that samples only from nonzero residual rows without repeated rejection can avoid this overhead, at the possible cost of maintaining a changing distribution. The exhibit is a three-dimensional triangular, nonuniformly scaled system; it does not give an average-case claim for well-conditioned families or imply failure of the cited accepted-iteration convergence theorem. Selecting a single fixed constraint row and taking unit relaxation are essential to the exact formulas. Other sketch distributions, block selections, and floating-point zero tests are not covered.

## References
- Y. Sun, H.-D. Qi, D. Han, J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1 (first public 2026-05-28), https://arxiv.org/abs/2605.29304.
- J. Lok, E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889v2, https://arxiv.org/abs/2309.04889.
- J. Lok, E. Rebrova, *Subspace-constrained randomized coordinate descent for linear systems with good low-rank matrix approximations*, arXiv:2506.09394, https://arxiv.org/abs/2506.09394.
