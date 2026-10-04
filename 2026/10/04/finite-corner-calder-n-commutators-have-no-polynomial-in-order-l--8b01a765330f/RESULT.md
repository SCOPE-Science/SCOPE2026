# Finite-corner Calderón commutators have no polynomial-in-order loss

## Finding

Let \(A:\mathbb R\to\mathbb R\) be Lipschitz and piecewise affine with finitely many breakpoints. Let
\[
I_1,\ldots,I_N
\]
be its maximal affine intervals and put
\[
L=\|A'\|_\infty.
\]
For every integer \(n\ge1\), define
\[
T_{A,n}f(x)
=
\operatorname{p.v.}\int_{\mathbb R}
\frac{f(y)}{x-y}
\left(
\frac{A(x)-A(y)}{x-y}
\right)^n\,dy.
\]
Then
\[
\|T_{A,n}\|_{L^2(\mathbb R)\to L^2(\mathbb R)}
\le
\pi N L^n.
\]

Hence a fixed piecewise-affine profile with finitely many corners has no polynomial growth in the commutator order after the natural normalization by \(L^n\). The same conclusion holds uniformly for any family in which the number of affine pieces is bounded.

For compactly supported polygonal profiles this strictly improves the general bounded-variation consequence of the recent higher-order commutator estimates, which has a \(\sqrt n\)-type factor. Therefore neither the linear factor from the general Lipschitz theorem nor the \(\sqrt n\) factor from the refined regularity theorem can be sharp on the finite-corner subclass.

## Assumptions and scope

The function \(A\) is continuous automatically because it is Lipschitz. Its finitely many breakpoints divide \(\mathbb R\), up to endpoints of measure zero, into \(N\) intervals on each of which
\[
A(x)=s_jx+b_j
\]
for some slope \(s_j\) satisfying
\[
|s_j|\le L.
\]

The estimate is for the unnormalized kernel convention used above. With a Hilbert-transform normalization containing a factor \(1/\pi\), the numerical constant changes accordingly.

The theorem does not claim a sharp dependence on the number \(N\) of affine pieces. Its point is the complete absence of any additional dependence on the commutator order \(n\) when \(N\) is fixed.

## Proof

Decompose
\[
L^2(\mathbb R)=\bigoplus_{j=1}^N L^2(I_j)
\]
and write
\[
T_{A,n}=(T_{ij})_{1\le i,j\le N},
\qquad
T_{ij}=\mathbf 1_{I_i}T_{A,n}\mathbf 1_{I_j}.
\]
We show that every block satisfies
\[
\|T_{ij}\|_{2\to2}\le \pi L^n.
\]

First suppose \(i=j\). On \(I_i\), the function \(A\) is affine with slope \(s_i\), so for almost every distinct \(x,y\in I_i\),
\[
\frac{A(x)-A(y)}{x-y}=s_i.
\]
Therefore
\[
T_{ii}f(x)
=
s_i^n\,\mathbf 1_{I_i}(x)
\operatorname{p.v.}\int_{I_i}\frac{f(y)}{x-y}\,dy.
\]
The unnormalized Hilbert transform
\[
H_0f(x)=\operatorname{p.v.}\int_{\mathbb R}\frac{f(y)}{x-y}\,dy
\]
has \(L^2\) norm \(\pi\). Restriction on both sides cannot increase the norm, so
\[
\|T_{ii}\|_{2\to2}\le \pi |s_i|^n\le \pi L^n.
\]

Now suppose \(i\ne j\). Since \(A\) is \(L\)-Lipschitz,
\[
\left|
\frac{A(x)-A(y)}{x-y}
\right|
\le L.
\]
Assume for definiteness that \(I_j\) lies to the left of \(I_i\), and choose any point \(c\) between the two intervals. For \(x\in I_i\) and \(y\in I_j\), put
\[
u=x-c\ge0,
\qquad
v=c-y\ge0.
\]
Then
\[
|x-y|=u+v
\]
and consequently
\[
|T_{ij}f(x)|
\le
L^n\int_{I_j}\frac{|f(y)|}{|x-y|}\,dy.
\]
After the translation-reflection above, the positive operator on the right is a restriction of the Carleman operator
\[
(Cg)(u)=\int_0^\infty\frac{g(v)}{u+v}\,dv.
\]
Its \(L^2(0,\infty)\) norm is at most \(\pi\). A self-contained weighted Schur estimate uses
\[
\phi(u)=u^{-1/2}
\]
and the identity
\[
\int_0^\infty\frac{v^{-1/2}}{u+v}\,dv
=
\pi u^{-1/2},
\]
with the symmetric identity in the other variable. Hence
\[
\|T_{ij}\|_{2\to2}\le \pi L^n.
\]
The case in which \(I_i\) lies to the left of \(I_j\) is identical.

Finally, let
\[
f=\sum_{j=1}^N f_j,
\qquad
f_j=\mathbf1_{I_j}f.
\]
For each \(i\),
\[
\left\|
\sum_{j=1}^N T_{ij}f_j
\right\|_2
\le
\pi L^n\sum_{j=1}^N\|f_j\|_2.
\]
Squaring and summing over \(i\), then applying Cauchy--Schwarz to the finite sum over \(j\), gives
\[
\|T_{A,n}f\|_2^2
\le
\pi^2N^2L^{2n}\|f\|_2^2.
\]
Taking square roots proves
\[
\|T_{A,n}\|_{2\to2}\le \pi N L^n.
\]

## Verification

The proof reduces every operator block to one of two classical kernels and verifies both directly.

On a single affine interval the divided difference is exactly the constant slope, so the block is a restricted Hilbert transform multiplied by \(s_i^n\). Its norm is at most \(\pi|s_i|^n\).

Between two distinct affine intervals the Lipschitz estimate alone gives the pointwise domination
\[
|K_n(x,y)|\le \frac{L^n}{|x-y|}.
\]
Choosing a point between the intervals converts \(|x-y|^{-1}\) to \((u+v)^{-1}\), the Carleman kernel. The weighted Schur calculation
\[
\int_0^\infty\frac{v^{-1/2}}{u+v}\,dv=\pi u^{-1/2}
\]
certifies the required \(L^2\) bound without an external numerical constant or computation.

The finite block-matrix estimate then contributes only the factor \(N\), independent of \(n\). No finite experiment, asymptotic extrapolation, or unproved cancellation is used.

## Relationship to prior work

Hernández, Mateu, and Prat prove the current general estimate
\[
\|T_{A,n}\|_{2\to2}\le Cn\|A'\|_\infty^n
\]
for arbitrary Lipschitz \(A\), and explicitly ask whether the linear factor in \(n\) is sharp. They note that the examples they examined exhibit only the exponential factor and no polynomial growth. For compactly supported profiles with additional regularity, including bounded-variation derivatives, their refined theory yields a \(\sqrt n\)-type upper factor.

The finite-corner theorem above isolates a concrete structural reason why polygonal examples cannot settle that sharpness question: after decomposing at the corners, every off-diagonal interaction is controlled by one Carleman block, uniformly in the order. Thus a fixed finite set of corners cannot create any polynomial-in-\(n\) amplification.

Muhly and Xia prove a reduction theorem for Calderón commutators under the assumption that the relevant derivatives belong to \(\mathrm{VMO}\). A genuinely piecewise-affine function with a slope jump generally has a derivative outside \(\mathrm{VMO}\), so that result does not supply the present finite-corner estimate. It also does not quantify a uniform-in-order bound for the jump case.

Targeted searches for piecewise-affine, piecewise-linear, finite-corner, Carleman-block, and higher-order Calderón commutator formulations did not locate a published statement equivalent to the theorem above.

## Limitations

The dependence \(\pi N\) on the number of affine pieces is only a transparent universal bound; it is not claimed optimal.

The result does not exclude polynomial growth for Lipschitz functions with infinitely many slope changes, nor for families in which the number of affine pieces itself grows with \(n\). It therefore narrows the source sharpness problem rather than resolving it globally.

The proof is one-dimensional and uses the ordered geometry of intervals. No analogue for higher-dimensional Calderón-type commutators is asserted.

## References

1. J. Hernández, J. Mateu, and L. Prat, *\(L^2\)-boundedness of the \(n\)-th Calderón commutator on Lipschitz graphs*, arXiv:2606.04682, 2026.
2. P. S. Muhly and J. Xia, *Reduction of Calderón Commutators*, Bulletin of the London Mathematical Society 30 (1998), 67--72.
