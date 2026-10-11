# A zero-frequency criterion for quasi norm attainment of convolution graphs on \(c_0\)

## Finding

Let \(\mathbb K\) be either \(\mathbb R\) or \(\mathbb C\). Suppose \(a=(a_n)_{n\ge1}\in\ell_1(\mathbb N;\mathbb R)\) has \(a_n>0\) for every \(n\), and write \(A=\sum_{n\ge1}a_n>0\). Let \(S:c_0(\mathbb K)\to c_0(\mathbb K)\) be the forward shift, given by \((Sx)_1=0\) and \((Sx)_n=x_{n-1}\) for \(n\ge2\). For any \(c=(c_j)_{j\ge0}\in\ell_1(\mathbb N_0;\mathbb K)\) with \(C=\sum_{j\ge0}|c_j|<A\), define

\[
W_c=\sum_{j=0}^{\infty}c_jS^j,\qquad f_a(x)=\sum_{n=1}^{\infty}a_nx_n,\qquad T_cx=(f_a(x),W_cx).
\]

The target of \(T_c\) is \(\mathbb K\oplus_\infty c_0(\mathbb K)\). Put \(s(c)=\sum_{j\ge0}c_j\) and \(b_n=\sum_{j=0}^{n-1}c_j\). The following single classification, including its quantitative norm-distance assertion, holds:

\[
\boxed{\|W_c\|=C,\quad \|T_c\|=A,\quad T_c\notin\operatorname{NA},\quad T_c\in\operatorname{QNA}\iff s(c)=0.}
\]

When \(s(c)=0\), \(b=(b_n)\in c_0\), and the norm-\(A\) limit points of \(T_c(B_{c_0})\) are exactly \(\{\lambda(A,b):|\lambda|=1\}\). When \(s(c)\ne0\), this intersection with the sphere of radius \(A\) is empty. The auxiliary component has the independent, sharper property

\[
\boxed{W_c\in\operatorname{QNA}\iff W_c\in\operatorname{NA}\iff c\text{ has finite support}.}
\]

Holding \(a\) fixed, consider the open affine family \(\mathcal T_A=\{T_d:\|d\|_1<A\}\), with its inherited operator norm. Its relative quasi-norm-attaining subset is a closed, nowhere-dense codimension-one hyperplane section, and the distance to this subset is attained with the exact formula

\[
\boxed{\operatorname{dist}\bigl(T_c,\mathcal T_A\cap\operatorname{QNA}\bigr)=|s(c)|.}
\]

All assertions are valid with real or complex scalars.

## Assumptions and scope

Here \(\operatorname{NA}\) means ordinary norm attainment and \(\operatorname{QNA}\) means that the norm closure of the image of the closed unit ball intersects the sphere of radius equal to the operator norm. Equivalently, \(T\in\operatorname{QNA}(X,Y)\) if some \((x^{(k)})\subset B_X\) has \(Tx^{(k)}\to y\in Y\) in norm with \(\|y\|=\|T\|\). The strict gap \(\|c\|_1<A\), positivity at every coordinate of \(a\), absolute summability of \(c\), and the \(c_0\) target for the convolution component are essential stated hypotheses. No positivity assumption on the scalar coefficients \(c_j\) is made. Distances and topology for the final assertion are **relative to the fixed-weight affine family**, not to all bounded operators between the two Banach spaces.

## Proof

**Operator norms and failure of ordinary norm attainment.** By the forward-shift coordinate formula,

\[
(W_cx)_n=\sum_{j=0}^{n-1}c_jx_{n-j},\qquad n\ge1.
\]

The absolutely convergent operator series has norm at most \(C\). Conversely, the coordinate \(n\) functional has norm exactly \(\sum_{j=0}^{n-1}|c_j|\): choose finitely many unit-modulus coordinates of \(x\) to align the coefficients. Taking the supremum over \(n\) gives \(\|W_c\|=C\). Since \(a_n>0\), the functional \(f_a\) has norm \(A\), approached by initial-block indicator vectors. Hence \(\|T_c\|=\max\{A,C\}=A\).

If \(x\in B_{c_0}\), then \(x_n\to0\) and some \(|x_n|<1\). With all \(a_n>0\), this yields \(|f_a(x)|<A\). Also \(\|W_cx\|\le C<A\), so \(\|T_cx\|<A\) for every \(x\in B_{c_0}\). Therefore \(T_c\notin\operatorname{NA}\).

**Necessity of cancellation.** Suppose \(T_cx^{(k)}\to(u,y)\) in the direct-sum norm for some \(x^{(k)}\in B_{c_0}\), with \(\|(u,y)\|=A\). Because \(\|y\|\le C<A\), necessarily \(|u|=A\). Write \(u=\lambda A\), where \(|\lambda|=1\). Then

\[
\sum_{n\ge1}a_n\bigl(1-\operatorname{Re}(\overline\lambda x_n^{(k)})\bigr)
=A-\operatorname{Re}(\overline\lambda f_a(x^{(k)}))\longrightarrow0.
\]

Every summand is nonnegative, and every \(a_n\) is strictly positive. Thus for each fixed \(n\), \(\operatorname{Re}(\overline\lambda x_n^{(k)})\to1\), and \(|x_n^{(k)}|\le1\) implies \(x_n^{(k)}\to\lambda\). Passing to the limit in each *finite* coordinate sum gives

\[
y_n=\lim_{k\to\infty}(W_cx^{(k)})_n=\lambda\sum_{j=0}^{n-1}c_j=\lambda b_n.
\]

The limit \(y\) lies in \(c_0\), while absolute summability implies \(b_n\to s(c)\). Hence \(s(c)=0\). The same argument shows that any sphere-radius norm limit must be precisely \(\lambda(A,b)\) with \(|\lambda|=1\).

**Sufficiency of cancellation.** Suppose \(s(c)=0\). Then \(b\in c_0\). For positive integers \(k\), let \(u^{(k)}\in B_{c_0}\) be the finitely supported ramp

\[
u_n^{(k)}=\begin{cases}1,&1\le n\le k,\\2-n/k,&k<n<2k,\\0,&n\ge2k.\end{cases}
\]

It has \(\|u^{(k)}\|_\infty=1\), tends coordinatewise to the constant sequence \(1\), and satisfies \(|u_{n-j}^{(k)}-u_n^{(k)}|\le\min\{1,j/k\}\) whenever \(1\le j<n\). Dominated convergence yields \(f_a(u^{(k)})\to A\). For \(n\le k\), \((W_cu^{(k)})_n=b_n\). For \(n>k\), the exact decomposition

\[
(W_cu^{(k)})_n-b_n
=(u_n^{(k)}-1)b_n+\sum_{j=0}^{n-1}c_j(u_{n-j}^{(k)}-u_n^{(k)})
\]

implies

\[
\|W_cu^{(k)}-b\|_\infty\le\sup_{n>k}|b_n|+\sum_{j=0}^{\infty}|c_j|\min\{1,j/k\}\longrightarrow0.
\]

The first term vanishes because \(b\in c_0\); the second does so by dominated convergence on the absolutely summable coefficients. Thus \(T_cu^{(k)}\to(A,b)\), a vector of norm \(A\). Multiplying all ramp vectors by \(\lambda\) realizes every \(\lambda(A,b)\) of unit-modulus phase, proving the full sphere-limit statement.

**The convolution component separately.** If \(c\) has finite support, one sufficiently late row of \(W_c\) contains every nonzero coefficient. A finitely supported unit vector aligning that row shows \(\|W_cx\|=C\), so \(W_c\in\operatorname{NA}\subseteq\operatorname{QNA}\). The conclusion includes \(c=0\). Conversely, suppose \(c\) has infinitely many nonzero entries. Each fixed row satisfies

\[
|(W_cx)_n|\le\sum_{j=0}^{n-1}|c_j|<C\qquad(x\in B_{c_0}).
\]

This strict inequality persists for each fixed coordinate of any norm limit \(y\in\overline{W_c(B_{c_0})}\). A nonzero sequence in \(c_0\) attains its supremum norm at some coordinate; therefore no such \(y\) can have norm \(C\). Hence \(W_c\notin\operatorname{QNA}\).

**Exact relative operator-norm distance.** First, \(\|T_c-T_d\|=\|W_{c-d}\|=\|c-d\|_1\), so the coefficient-to-operator parametrization is isometric. For every \(d\) with \(s(d)=0\), the triangle inequality gives \(\|c-d\|_1\ge|s(c)|\).

When \(s(c)\ne0\), write \(\lambda=s(c)/|s(c)|\) and \(R=\sum_{j\ge0}\bigl(\operatorname{Re}(\overline\lambda c_j)\bigr)_+\), where \(r_+=\max\{r,0\}\). Since \(\sum_j\operatorname{Re}(\overline\lambda c_j)=|s(c)|\), one has \(R\ge|s(c)|>0\). Define

\[
h_j=\lambda\frac{|s(c)|}{R}\bigl(\operatorname{Re}(\overline\lambda c_j)\bigr)_+,\qquad d_j=c_j-h_j.
\]

Then \(\sum_jh_j=s(c)\) and \(\sum_j|h_j|=|s(c)|\), so \(s(d)=0\) and \(\|c-d\|_1=|s(c)|\). Moreover \(0\le |s(c)|/R\le1\), and subtracting from \(c_j\) a scalar between zero and its projection onto the \(\lambda\)-ray cannot increase its modulus: \(|d_j|\le|c_j|\). Consequently \(\|d\|_1\le\|c\|_1<A\), making \(T_d\) admissible. The zero-sum case takes \(d=c\). This proves the exact, attained distance formula. The sum functional on \(\ell_1\) is continuous, nonzero, and surjective onto \(\mathbb K\), so its kernel is a closed codimension-one subspace; its intersection with the open ball of radius \(A\) has empty relative interior. The complement is relatively open dense.

## Verification

Every limit passage above is justified by either a fixed finite coordinate sum or an explicitly bounded absolutely summable series. The core cancellation estimate is uniform in the coordinate index; it is not a pointwise-to-norm convergence shortcut. Complex phases are handled by \(\operatorname{Re}(\overline\lambda\cdot)\), and the distance-minimizing correction is valid over both fields.

For concrete contrasts, take \(a_n=3\cdot2^{-n}\), so \(A=3\). With \(c=(1,0,0,\dots)\), the component \(W_c=I\) norm-attains, and \(f_a\) quasi norm-attains, but their combined operator \(T_c\) does **not** quasi norm-attain. With \(c=(1,-1,0,\dots)\), the operator \(T_c\) quasi norm-attains without norm attainment. With \(c=(-1,2^{-1},2^{-2},\dots)\), the coefficients are infinitely supported and have zero sum and \(\|c\|_1=2<3\); thus \(W_c\) itself fails quasi norm attainment while \(T_c\) has it. Direct numerical checks on truncated ramps recover the predicted convergence; the infinite assertions rely on the displayed analytic proof.

## Relationship to prior work

Choi, Choi, Jung and Martín introduced quasi norm attainment and proved general existence, density, and adjoint characterizations. Their Proposition 4.3 produces non-quasi-norm-attaining maps into \(c_0\); Sections 5 and 6 treat different structural conditions and stability of **density**. Their Problem 7.3 asks a separate question about density under \(\ell_\infty\)-sums of range spaces, which is **not answered** here. The present result instead supplies an exact symbol-cancellation criterion and an attained metric formula inside a natural analytic-convolution graph family, with contrasting behavior of individual coordinates. Earlier general statements do not yield these parameter-specific formulas by direct implication. The earliest public preprint date of that motivating paper is 2020-04-23 (its later journal date is not used for dating this direction).

## Limitations

The strict domination \(\|c\|_1<A\) is required: equality or reversal changes which target coordinate can supply a maximal-norm limit. This theorem neither classifies arbitrary Toeplitz operators nor proves that quasi-norm-attaining operators are non-dense in the full operator space. The metric distance concerns only \(\mathcal T_A\) with fixed \(a\); it does not measure distance to all quasi-norm-attaining operators. Originality comparison cannot exclude equivalent statements in literature not indexed or not accessible in the checked searches. No independent audit is claimed.

## References

1. G. Choi, Y. S. Choi, M. Jung, M. Martín, *On quasi norm attaining operators between Banach spaces*, arXiv:2004.11025v1, first submitted 2020-04-23; https://arxiv.org/abs/2004.11025.
2. The same paper, open-access journal edition, *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 116 (2022), article 133; https://doi.org/10.1007/s13398-022-01281-x.
