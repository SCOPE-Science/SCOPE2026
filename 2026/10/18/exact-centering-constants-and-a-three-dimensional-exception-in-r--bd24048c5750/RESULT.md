# Exact centering constants and a three-dimensional exception in real Lorentz sequence spaces

## Finding

Let \(n\geq 2\) be an integer, \(w_1\geq\cdots\geq w_n>0\), and let \(X_w=(\mathbb R^n,\|\cdot\|_w)\) with \(\|x\|_w=\sum_{j=1}^{n}w_j|x|_{(j)}\), where \(|x|_{(1)}\geq\cdots\geq|x|_{(n)}\) are the rearranged coordinate magnitudes. Set \(W_j=\sum_{i=1}^{j}w_i\), \(W_0=0\), and \(H_n=\{x:\sum_i x_i=0\}\). The least norm of a real linear projection from \(X_w\) onto \(H_n\) is attained by coordinate centering \(P_nx=x-(n^{-1}\sum_i x_i)\mathbf1\).

Its exact value is the finite maximum \(\lambda_n(w)=\max_{1\leq k\leq n,\,0\leq s\leq\lfloor k/2\rfloor} F_{n,k,s}(w)\). Define \(d=(k-2s)/n\) and \(r=k-s\). The explicitly evaluable terms are
\[
F_{n,k,s}(w)=\frac{1}{W_k}\begin{cases}
(1+d)W_s+(1-d)(W_k-W_s)+d(W_n-W_k),&d\leq 1/2,\\
(1+d)W_s+d(W_{s+n-k}-W_s)+(1-d)(W_n-W_{s+n-k}),&d\geq 1/2.
\end{cases}
\]
The two expressions agree at the shared boundary. Thus at most \(\sum_{k=1}^n(1+\lfloor k/2\rfloor)\) explicit rational expressions determine the unrestricted projection constant.

There is a sharp dimension threshold for norm-one complementability of this particular symmetric hyperplane:
\[
\lambda_2(w)=1,\qquad
\lambda_3(w)=\max\left\{\frac{W_3+w_1}{3w_1},\frac{2(W_3+w_1)}{3W_3}\right\},
\]
and for dimension three \(\lambda_3(w)=1\) precisely when \(w_2+w_3=w_1\). In every dimension \(n\geq4\), \(\lambda_n(w)>1\) for **every strictly positive decreasing weight vector**. No lower bound uniform over weights is claimed.

## Assumptions and scope

The spaces, projections, and operator norms are real. Weights are finite and strictly positive, with nonincreasing order; overall scaling does not change the projection constant. The theorem concerns only the specified coordinate-sum-zero hyperplane, not all hyperplanes or infinite-dimensional Lorentz spaces. We use the standard \(p=1\) weighted-rearrangement Lorentz norm, not the quadratic \(\ell_{w,2}\) norm. The minimum ranges over every bounded real linear projection onto \(H_n\), without symmetry restrictions.

## Proof

**1. A minimal projection by symmetry.** Put \(\varphi(x)=\sum_i x_i\). Every projection \(Q\) onto \(\ker\varphi\) has the form \(Q=I-v\varphi\), with \(\varphi(v)=1\). Every permutation of coordinates acts isometrically on \(X_w\) and preserves \(H_n\). Average the conjugates of \(Q\) over all permutations. The average remains a projection onto \(H_n\), has norm at most \(\|Q\|\), and equals \(I-n^{-1}\mathbf1\varphi=P_n\), since the averaged \(v\) has all coordinates \(1/n\). Therefore \(\lambda_n(w)=\|P_n\|\).

**2. Exact vertex reduction.** For a nonzero real vector \(x\), order its magnitudes as \(a_1\geq\cdots\geq a_n\geq0\), set \(a_{n+1}=0\), and keep its coordinate signs. Writing \(u_k\) for the signed indicator of its \(k\) largest-magnitude coordinates gives \(x=\sum_{k=1}^n(a_k-a_{k+1})u_k\) and \(\|x\|_w=\sum_{k=1}^n(a_k-a_{k+1})W_k\). Hence every point of the unit ball is a convex combination of vectors \(u_k/W_k\), where each \(u_k\) has exactly \(k\) nonzero entries, each equal to \(1\) or \(-1\). Convexity of \(x\mapsto\|P_nx\|_w\) proves that the norm is the maximum on this finite set. Permutations and global sign reversal allow \(r=k-s\) positive and \(s\) negative entries with \(0\leq s\leq\lfloor k/2\rfloor\).

**3. Sorted output.** For this signed vector the input mean is \(d=(r-s)/n=(k-2s)/n\), so the magnitudes of the centered output are \(1+d\) repeated \(s\) times, \(1-d\) repeated \(r\) times, and \(d\) repeated \(n-k\) times. Since \(0\leq d\leq1\), their descending order is respectively \((1+d,1-d,d)\) when \(d\leq1/2\) and \((1+d,d,1-d)\) when \(d\geq1/2\). Computing the weighted rearrangement norm and dividing by \(W_k\) proves the displayed formula. This reduction is an equality, not a finite-sampling bound.

**4. Dimensions two and three.** In dimension two, centering equals one-half of identity minus coordinate swap, so \(\|P_2\|\leq1\); it fixes the nonzero hyperplane, giving equality. In dimension three the finite formula has only two possible maxima greater than or equal to one: the indicator supported on a single coordinate gives \((W_3+w_1)/(3w_1)\), and the fully supported sign vector with two plus signs and one minus sign gives \(2(W_3+w_1)/(3W_3)\). The zero-mean two-support vectors give one; the other types have no larger ratio (the two-support equal-sign value is the first expression divided by \(W_2/w_1\), and a constant-sign full-support vector centers to zero). This proves the exact dimension-three expression. Its first term is at most one iff \(W_3\leq2w_1\), and the second at most one iff \(W_3\geq2w_1\). Thus \(\lambda_3(w)=1\) exactly at \(W_3=2w_1\).

**5. The obstruction in every higher dimension.** For \(n\geq3\), testing \(e_1\) gives
\[
\frac{\|P_ne_1\|_w}{\|e_1\|_w}=1+\frac{W_n-2w_1}{nw_1}.
\]
Testing the full sign vector with \(n-1\) plus signs and one minus sign gives
\[
\frac{\|P_nu\|_w}{\|u\|_w}=1+\frac{(n-2)(2w_1-W_n)}{nW_n}.
\]
Consequently a contractive projection in dimension at least three would require \(W_n=2w_1\). In dimension four, then test the vector with two plus signs, one minus sign and one zero. Its centered output has magnitudes \((5/4,3/4,3/4,1/4)\), while its input has three unit magnitudes. The output norm exceeds the input norm by exactly \(w_4/2>0\). In dimensions \(n\geq5\), test the full sign vector with \(n-2\) plus signs and two minus signs. Its output norm exceeds its input norm by \(2(n-4)w_2/n>0\), since \(W_n=2w_1\). Either way \(\|P_n\|>1\), proving the strict higher-dimensional obstruction. The preceding symmetry argument makes this a statement about every projection onto \(H_n\), not merely centering.

## Verification

A standalone pure-Python exact-rational checker, `lorentz_checker.py`, computes the finite maximum and independently enumerates all ternary signed-support probes for 72 rational-weight samples in dimensions two through seven. It additionally checks the explicit two- and three-dimensional formulas and positive higher-dimensional examples. Run it with `python3 lorentz_checker.py` in a standard Python installation. Finite checks are corroboration only; the vertex decomposition and witness inequalities above prove the theorem for all admissible weights and dimensions.

## Relationship to prior work

Randrianantoanina's real Lorentz one-complementation theorem treats \(\ell_{w,p}\) for \(1<p<\infty\) (arXiv:math/9702214, Section 3), rather than this endpoint \(p=1\). The earlier complex-space theorem (arXiv:math/9605214) concerns different scalar-field and subspace hypotheses. Jameson's study of operators on \(d(w,1)\) emphasizes positive decreasing-sequence tests, whereas centering is a signed operator. Kamińska, Lee and Lewicki study extreme points and the relationship between existence sets and one-complemented subspaces in \(d(w,1)\); that abstract relationship alone does not decide the present weight-dependent norm. The result here identifies a specific endpoint phenomenon: a continuous family of three-dimensional norm-one projections, but none with strictly positive weights in dimensions four and higher, and gives a full finite norm formula rather than just an existence criterion.

## Limitations

This theorem makes no claim concerning complex scalars, other hyperplanes, infinite-dimensional Lorentz spaces, or best constants over all weights in a fixed dimension. The norm formula is finite but not simplified to a single expression for arbitrary \(n\). The published literature comparison is incomplete: the full texts of Jameson (1999) and Kamińska–Lee–Lewicki (2009) were not available for exhaustive theorem-by-theorem inspection, so an equivalent published treatment cannot be excluded. No independent mathematical or bibliographic audit has been performed.

## References

1. B. Randrianantoanina, *1-Complemented Subspaces of Spaces With 1-Unconditional Bases*, arXiv:math/9605214 (first submitted 9 May 1996).
2. B. Randrianantoanina, *One-complemented subspaces of real sequence spaces*, arXiv:math/9702214 (first submitted 24 February 1997), especially Section 3.
3. G. J. O. Jameson, *Norms and lower bounds of operators on the Lorentz sequence space \(d(w,1)\)*, Illinois J. Math. 43 (1999), 79–99, doi:10.1215/ijm/1255985338.
4. A. Kamińska, H. J. Lee and G. Lewicki, *Extreme and smooth points in Lorentz and Marcinkiewicz spaces with applications to contractive projections*, Rocky Mountain J. Math. 39 (2009), 1533–1572, doi:10.1216/RMJ-2009-39-5-1533.
