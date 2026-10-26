# A four-asset correlation matrix reverses the condition-number comparison

## Finding

There is a valid four-asset correlation matrix for which the Euclidean condition-number comparison and the Schatten-1 comparison of the signed and unsigned exponential systems have opposite signs. With the signed matrix and correlation matrix defined below, the Euclidean ratio is exactly greater than one, while the Schatten-1 ratio is less than \(0.989\). Therefore the trace-norm ratio used in the global-balance analysis cannot be substituted for worst-case Euclidean relative-perturbation sensitivity, even on a positive-definite correlation matrix.

Let

\[
A=\begin{pmatrix}
0&-1&-1&-1\\
-1&0&-1&1\\
-1&-1&0&1\\
-1&1&1&0
\end{pmatrix},\qquad
C=I_4+\frac25 A,\qquad B=|A|.
\]

The matrix \(C\) has diagonal entries \(1\), off-diagonal entries in \(\{-2/5,2/5\}\), and is positive definite. Thus \(C\) is an admissible correlation matrix. Absolute values of matrices in this result are entrywise, so \(|C|=I_4+(2/5)B\).

For the induced Euclidean matrix norm, define \(\operatorname{cond}_2(M)=\|M\|_2\|M^{-1}\|_2\). Then

\[
\frac{\operatorname{cond}_2(e^{-C})}{\operatorname{cond}_2(e^{-|C|})}
=\exp\!\left(\frac{4\sqrt5-8}{5}\right)>1.
\]

In contrast, the ratio formed with the Schatten-1 (nuclear) norm, \(\operatorname{cond}_*(M)=\|M\|_*\|M^{-1}\|_*\), satisfies

\[
\frac{\operatorname{cond}_*(e^{-C})}{\operatorname{cond}_*(e^{-|C|})}<0.989<1.
\]

The two norm-based comparisons therefore disagree even on the direction of the comparison. This is a norm-specific counterexample, not a claim about empirical financial losses.

## Assumptions and scope

The matrices are real and symmetric. The correlation matrix \(C\) is positive definite, and the comparator \(|C|\) is also positive definite. The Euclidean condition number is the induced 2-norm condition number, which is the norm governing worst-case relative perturbations of a vector under the usual Euclidean error model. The Schatten-1 expression is treated separately as the nuclear-norm product used in the cited global-balance paper. No claim is made that the nuclear-norm ratio is algebraically undefined or useless as a distinct statistic.

## Proof

First, exact determinant expansion gives

\[
\det(\lambda I_4-A)=(\lambda^2-1)(\lambda^2-5),
\]

so the eigenvalues of \(A\) are \(\{-\sqrt5,-1,1,\sqrt5\}\). Since \(B\) is the adjacency matrix of the complete graph on four vertices,

\[
\operatorname{spec}(B)=\{3,-1,-1,-1\}.
\]

Consequently, the eigenvalues of \(C\) are \(1\pm(2\sqrt5/5)\) and \(1\pm2/5\). The least is positive because \(4/5<1\). The eigenvalues of \(|C|\) are \(11/5\) and \(3/5\) with multiplicity three, so both matrices are positive definite.

For a real symmetric matrix \(H\), the eigenvalues of \(e^{-H}\) are \(e^{-\lambda_i(H)}\), and hence

\[
\operatorname{cond}_2(e^{-H})=e^{\lambda_{\max}(H)-\lambda_{\min}(H)}.
\]

The spectral width of \(C\) is \(4\sqrt5/5\), while that of \(|C|\) is \(8/5\). Their difference is \((4\sqrt5-8)/5>0\), proving the first ratio is greater than one.

For the nuclear-norm ratio, scalar identity shifts cancel from the quotient. Put \(t=2/5\). The spectra above give

\[
R_*(t)=
\frac{\bigl(2\cosh(t\sqrt5)+2\cosh t\bigr)^2}
{(e^{3t}+3e^{-t})(e^{-3t}+3e^t)}
=
\frac{4\bigl(\cosh(t\sqrt5)+\cosh t\bigr)^2}
{10+6\cosh(4t)}.
\]

The last expression is bounded rigorously using rational Taylor bounds. For \(q=u^2<56\), positivity of the hyperbolic-cosine series and a geometric bound on the tail after \(u^4/24\) give

\[
\cosh u\le 1+\frac q2+\frac{q^2}{24}
+\frac{q^3}{720(1-q/56)}.
\]

Also, for \(z\ge0\),

\[
\cosh z\ge1+\frac{z^2}{2}+\frac{z^4}{24}
+\frac{z^6}{720}+\frac{z^8}{40320}.
\]

At \(t=2/5\), applying the upper bound with \(q=4/5\) and \(q=4/25\), and the lower bound with \(z^2=64/25\), yields the exact rational bounds

\[
U_1=\frac{110801}{77625},\qquad
U_2=\frac{10611401}{9815625},\qquad
L=\frac{105715049}{41015625},
\]

and exact rational arithmetic verifies

\[
4(U_1+U_2)^2<10+6L,
\qquad
\frac{4(U_1+U_2)^2}{10+6L}<\frac{989}{1000}.
\]

Thus \(R_*(2/5)<0.989<1\), completing the sign reversal. The complete calculation is reproducible with the standalone standard-library script `verify.py`.

## Verification

Running `python3 verify.py` checks both characteristic polynomials by exact rational determinant expansion, checks the positive-definiteness inequality, and verifies the rational Taylor-bound comparison without floating-point arithmetic. The printed decimal ratios are illustrative only; the proof of the strict nuclear-norm inequality uses rational bounds. The exact Euclidean inequality follows from \(\sqrt5>2\).

## Relationship to prior work

Bartesaghi, Diaz-Diaz, Grassi, and Uberti define the global-balance index using traces of matrix exponentials and, in their §4.2, connect it to a ratio of condition-number products. Their Eq. (14) describes relative perturbation sensitivity through a supremum over vector perturbations; their Eq. (15) then evaluates a product of trace/nuclear norms, and Proposition 4 classifies that trace-norm ratio by signed closed-walk counts. The present calculation does not introduce the global-balance index or the trace-norm formula. It isolates a distinction between that trace-norm quantity and the induced Euclidean condition number: for one admissible correlation matrix, the signs of the two comparisons differ.

## Limitations

This is one exact four-asset counterexample to treating the trace-norm ratio as interchangeable with Euclidean worst-case sensitivity. It does not refute the algebraic definition of the trace-norm ratio, nor does it determine whether global balance is empirically predictive of losses in any dataset. The conclusion is scoped to the public preprint's stated perturbation-sensitivity interpretation and the explicitly defined Euclidean norm.

## References

1. P. Bartesaghi, F. Diaz-Diaz, R. Grassi, and P. Uberti, “Global Balance and Systemic Risk in Financial Correlation Networks,” arXiv:2407.14272, first public on 2024-07-19; published as *Physica A* 674 (2025), 130698, DOI: 10.1016/j.physa.2025.130698. Sections 4.2–4.3, Eqs. (14)–(19), and Appendix A.
2. MSC2020 classification 91G45, “Financial networks (including contagion, systemic risk, regulation),” American Mathematical Society.
