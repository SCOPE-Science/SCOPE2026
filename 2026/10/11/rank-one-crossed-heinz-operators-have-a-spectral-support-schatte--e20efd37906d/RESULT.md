# Rank-one crossed-Heinz operators have a spectral-support Schatten crossover

## Finding

Let \(A\geq0\) be a bounded operator on a complex Hilbert space, let \(B=\beta uu^*\) with \(\beta>0\) and \(\|u\|=1\), and fix \(0<t<1\). Compare the crossed and ordinary Heinz operators
\[
C_t=A^tB^{1-t}+B^tA^{1-t},\qquad
H_t=A^tB^{1-t}+A^{1-t}B^t.
\]
Both have rank at most two. Let \(\mu\) be the probability spectral measure of \(A\) at \(u\), and put \(F(\lambda)=\lambda^t\), \(G(\lambda)=\lambda^{1-t}\),
\[
V_F=\int F^2\,d\mu-\left(\int F\,d\mu\right)^2,\quad
V_G=\int G^2\,d\mu-\left(\int G\,d\mu\right)^2,
\quad K=\int FG\,d\mu-\int F\,d\mu\int G\,d\mu.
\]
Then the exact norm-defect identities are
\[
\boxed{\|C_t\|_1^2-\|H_t\|_1^2
=2\beta\left(\sqrt{V_FV_G}-K\right)\geq0},
\qquad
\boxed{\|H_t\|_2^2-\|C_t\|_2^2=2\beta K\geq0}.
\]
Here \(\|\cdot\|_p\) is the Schatten \(p\)-norm, including \(p=\infty\). Equality in the first inequality holds exactly if \(t=1/2\) or the support of \(\mu\) has at most two points. Equality in the second holds exactly if the support has one point.

If the support of \(\mu\) has at least three points and \(t\ne1/2\), there is a **unique** exponent \(p_*\in(1,2)\) with
\[
\|C_t\|_p
\begin{cases}
>\|H_t\|_p,&1\leq p<p_*,\\
=\|H_t\|_p,&p=p_*,\\
<\|H_t\|_p,&p_*<p\leq\infty.
\end{cases}
\]
If the support has at least two points but either exactly two points or \(t=1/2\), the two trace norms are equal and \(\|C_t\|_p<\|H_t\|_p\) for every \(1<p\leq\infty\). When the support is a singleton, \(C_t=H_t\) for every \(p\).

An exact three-dimensional witness occurs at \(A=\operatorname{diag}(1,16,81)\), \(u=(1,1,1)/\sqrt3\), \(B=uu^*\), and \(t=1/4\):
\[
\|H_t\|_1^2=\frac{1004}{3},\quad
\|C_t\|_2^2=\frac{952}{3},\quad
\|C_t\|_1^2=\frac{952+4\sqrt{181}}3,
\]
so
\[
\|C_t\|_1^2-\|H_t\|_1^2
=\frac43(\sqrt{181}-13)>0.
\]
The same strict trace-norm reversal persists for sufficiently small positive-definite perturbations \(B+\varepsilon I\) in dimension three.

## Assumptions and scope

The Hilbert space may be finite- or infinite-dimensional; the bounded positive operator \(A\) need not be compact or invertible. Powers use continuous positive functional calculus, with \(0^r=0\) for \(r>0\). For a Borel set \(E\subset[0,\|A\|]\), \(\mu(E)=\langle E_A(E)u,u\rangle\), where \(E_A\) is the spectral projection measure. Thus \(\mu\) is a compactly supported probability measure. Its support means the closed measure-theoretic support, not the full spectrum of \(A\). The Schatten norms are finite because the displayed operators have finite rank. The theorem asserts no ordering for arbitrary higher-rank \(B\).

## Proof

Write \(P=uu^*\), \(a=\beta^{1-t}A^tu\), \(b=\beta^tA^{1-t}u\), and \(x=(I-P)a\), \(y=(I-P)b\). Because \(B^r=\beta^rP\) for all \(r>0\),
\[
C_t=au^*+ub^*,\qquad H_t=(a+b)u^*.
\]
Consequently \(H_t\) has rank at most one, \(C_t\) has rank at most two, and a direct Hilbert–Schmidt inner-product expansion gives
\[
\|H_t\|_1^2=\|H_t\|_2^2=\|a+b\|^2,
\qquad
\|H_t\|_2^2-\|C_t\|_2^2=2\operatorname{Re}\langle x,y\rangle.
\]
The quantity \(\langle x,y\rangle\) is real and equals \(\beta K\), by the spectral theorem.

Let \(s_1,s_2\geq0\) be the potentially nonzero singular values of \(C_t\). The factorization \(C_t=[a,u][u,b]^*\) gives, by taking the second exterior power (or the product of the two Gram determinants),
\[
s_1s_2=\|a\wedge u\|\,\|u\wedge b\|=\|x\|\,\|y\|
=\beta\sqrt{V_FV_G}.
\]
This identity remains valid when the rank drops, with both sides zero. Since \(\|C_t\|_1^2=(s_1+s_2)^2=\|C_t\|_2^2+2s_1s_2\), subtracting the rank-one formula for \(H_t\) gives the asserted trace-norm identity. Cauchy–Schwarz yields \(\sqrt{V_FV_G}\geq K\).

Strictness of the covariance has a separate proof:
\[
2K=\iint
\bigl(\lambda^t-\eta^t\bigr)
\bigl(\lambda^{1-t}-\eta^{1-t}\bigr)
\,d\mu(\lambda)\,d\mu(\eta).
\]
Both powers are strictly increasing on \([0,\infty)\), so \(K>0\) precisely when \(\mu\) is not a point mass. In that case \(V_F,V_G>0\), and equality in the Cauchy–Schwarz bound occurs exactly when \(G(\lambda)=cF(\lambda)+d\) on the support, with \(c>0\). For \(t=1/2\), the powers coincide. Otherwise, writing \(z=\lambda^t\) gives \(G(\lambda)=z^{(1-t)/t}\), a strictly convex or strictly concave graph. A line intersects this graph in at most two support points. Conversely, any one- or two-point support admits an affine relation. This proves both equality classifications.

If the support is nontrivial, \(V_F,V_G>0\) and hence \(s_2>0\). The map \(p\mapsto(s_1^p+s_2^p)^{1/p}=\|C_t\|_p\) is continuous and strictly decreasing on \([1,\infty]\). By contrast, the rank-one Schatten norm \(\|H_t\|_p=\|a+b\|\) is independent of \(p\). For three-or-more-point support and \(t\ne1/2\), the strict trace inequality at \(p=1\) and the strict reversed Hilbert–Schmidt inequality at \(p=2\) give the existence and uniqueness of \(p_*\in(1,2)\). The two-point and half-parameter cases have equality only at \(p=1\); a singleton gives \(x=y=0\) and \(C_t=H_t\).

For the explicit witness, the vectors of diagonal entries of \(A^t\) and \(A^{1-t}\) are respectively \((1,2,3)\) and \((1,8,27)\). Their uniform three-point variances and covariance are \(2/3\), \(362/3\), and \(26/3\). Thus \(s_1s_2=2\sqrt{181}/3\), while the squared Hilbert–Schmidt norms of \(H_t\) and \(C_t\) are respectively \(1004/3\) and \(952/3\). Their substitution into the identities proves the exact displayed strict defect. Continuity of positive fractional powers and singular values under finite-dimensional perturbation shows that replacing \(B\) by \(B+\varepsilon I\) preserves strictness for all sufficiently small \(\varepsilon>0\).

## Verification

The standalone standard-library verifier `verify_rank_one_heinz.py` independently reconstructs both witness matrices using rational entries, checks the two Hilbert–Schmidt norms, the squared product of singular values via all two-by-two minors, and the strict witness inequality using \(181>13^2\). It also checks two-support and equal-power equality cases. Run `python3 verify_rank_one_heinz.py`. These finite checks are supplemental; the claims for arbitrary spectral measures rest on the preceding analytic arguments.

## Relationship to prior work

Sababheh and Bourin (arXiv:2610.04567v1, first posted 2026-10-03) prove universal crossed/ordinary Heinz weak majorization for two-by-two positive matrices and identify an earlier positive-definite three-dimensional operator-norm obstruction. The present statement instead provides a complete rank-one-input trace/Schatten characterization over arbitrary Hilbert spaces, including an exact three-dimensional trace-norm obstruction already at \(t=1/4\). Bottazzi, Elencwajg, Larotonda, and Varela (arXiv:1403.7472) establish a Hilbert–Schmidt comparison in the central parameter range and exhibit an operator-norm counterexample outside it; neither implication determines the trace-norm reversal here. Standard bounds of the crossed expression against \(A+B\) do not imply or contradict a comparison with the usually smaller ordinary Heinz expression. Manjegani's tracial Heinz mean inequalities address the ordinary Heinz expression and a different majorization relation.

## Limitations

The spectral-support classification requires the second input to have exactly rank one; it does not characterize arbitrary positive matrix pairs. The exponent \(p_*\) is defined implicitly as the unique root of a two-singular-value equation, not by a universal closed formula; it may approach \(1\). The exact witness establishes a failure of comparison with the ordinary Heinz expression, not of Bourin's distinct conjectured bound against \(A+B\). No assertion about independent external validation is made.

## References

1. Mohammad Sababheh and Jean-Christophe Bourin, *Crossed-Heinz Inequalities: The Two-Dimensional Threshold and Higher-Dimensional Stability*, arXiv:2610.04567v1 (2026-10-03), https://arxiv.org/html/2610.04567v1.
2. Tamara Bottazzi, Rene Elencwajg, Gabriel Larotonda, and Alejandro Varela, *Inequalities related to Bourin and Heinz means with a complex parameter*, arXiv:1403.7472v1 (2014-03-28), https://arxiv.org/abs/1403.7472; J. Math. Anal. Appl. 426 (2015), 765–773.
3. Rajendra Bhatia, *Trace inequalities for products of positive definite matrices*, J. Math. Phys. 55 (2014), 013509, doi:10.1063/1.4863899.
4. Seyed Mahmoud Manjegani, *Tracial and majorisation Heinz mean-type inequalities for matrices*, J. Inequal. Appl. 2016, article 23, doi:10.1186/s13660-016-0965-8.
