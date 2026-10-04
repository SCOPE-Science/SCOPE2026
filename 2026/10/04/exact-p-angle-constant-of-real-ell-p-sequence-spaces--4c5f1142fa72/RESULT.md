# Exact P-angle constant of real \(\ell_p\) sequence spaces
## Finding
For every index set \(I\) with at least two elements and every \(1\le p\le\infty\), the Yang--Li P-angle constant of the real sequence space \(\ell_p(I)\) satisfies \(S_P(\ell_p(I))=1-2^{-\left|1-2/p\right|}\), with the convention \(2/\infty=0\). Equivalently, \(S_P(\ell_p(I))=1-2^{1-2/p}\) for \(1\le p\le2\) and \(S_P(\ell_p(I))=1-2^{2/p-1}\) for \(2\le p\le\infty\). The lower-exponent branch is attained by two disjoint coordinate unit vectors, while the upper-exponent branch is attained by the two-coordinate Hanner pair.

In particular, \(S_P(\ell_2(I))=0\), \(S_P(\ell_1(I))=S_P(\ell_\infty(I))=1/2\), and Hölder conjugates have the same value: \(S_P(\ell_p(I))=S_P(\ell_{p'}(I))\) whenever \(1<p<\infty\).

## Assumptions and scope
All spaces are real. The index set \(I\) may be finite or infinite but must contain at least two indices. For unit vectors \(x,y\in\ell_p(I)\) with \(x\ne\pm y\), Yang and Li define the P-angle constant by taking the supremum of
\[
\cos\operatorname{ang}_P(x+y,x-y)
=\frac{\|x+y\|_p^2+\|x-y\|_p^2-4}{2\|x+y\|_p\|x-y\|_p}.
\]
The endpoint convention is \(2/\infty=0\). No finite-dimensional reduction is assumed in the upper bound.

## Proof
Put \(a=\|x+y\|_p\) and \(b=\|x-y\|_p\). Since \(x\ne\pm y\), both are positive, and the displayed P-angle equals
\[
F(a,b)=\frac{a^2+b^2-4}{2ab}.
\]
For \(1<p<\infty\), set \(m=p\) when \(p\ge2\), and set \(m=p/(p-1)\) when \(1<p\le2\). Clarkson's inequalities give
\[
a^m+b^m\le 2^m.
\]
Fix \(t=a/b>0\) and write \((a,b)=s(t,1)\). Then
\[
F(s t,s)=\frac{1+t^2}{2t}-\frac{2}{s^2t},
\]
so for fixed \(t\) it increases with \(s\). Hence its maximum under \(a^m+b^m\le2^m\) occurs on the boundary and is at most
\[
R_m(t)=\frac{1+t^2-(1+t^m)^{2/m}}{2t}.
\]
The function satisfies \(R_m(t)=R_m(1/t)\). To show that it is nonincreasing for \(t\ge1\), put \(\alpha=2/m\in(0,1]\), \(u=t^m\), and \(v=(u-1)/(u+1)\in[0,1)\). Direct differentiation shows that \(R_m'(t)\le0\) is equivalent to
\[
(1+v)^\alpha-(1-v)^\alpha\le 2^\alpha v.
\]
Let \(G(v)=(1+v)^\alpha-(1-v)^\alpha\). On \([0,1]\),
\[
G''(v)=\alpha(\alpha-1)\big((1+v)^{\alpha-2}-(1-v)^{\alpha-2}\big)\ge0.
\]
Thus \(G\) is convex, with \(G(0)=0\) and \(G(1)=2^\alpha\), so convexity below the endpoint chord gives \(G(v)\le2^\alpha v\). Therefore \(R_m\) is maximized at \(t=1\), and
\[
F(a,b)\le R_m(1)=1-2^{2/m-1}.
\]
For \(2\le p<\infty\), this is \(1-2^{2/p-1}\). For \(1<p\le2\), the conjugate exponent \(m=p/(p-1)\) gives \(2/m-1=1-2/p\), hence the bound \(1-2^{1-2/p}\).

The endpoint upper bound \(F(a,b)\le1/2\) follows directly from \(0<a,b\le2\): the convex quadratic \(a^2-ab+b^2\) is at most \(4\) on \([0,2]^2\), which is equivalent to \(a^2+b^2-4\le ab\).

Sharpness is attained on two coordinates. For \(1\le p\le2\), choose distinct indices \(i,j\) and \(x=e_i\), \(y=e_j\). Then \(a=b=2^{1/p}\), giving \(F=1-2^{1-2/p}\). For \(2\le p<\infty\), choose
\[
x=2^{-1/p}(e_i+e_j),\qquad y=2^{-1/p}(e_i-e_j).
\]
Then \(a=b=2^{1-1/p}\), giving \(F=1-2^{2/p-1}\). For \(p=\infty\), take \(x=e_i+e_j\) and \(y=e_i-e_j\), so \(a=b=2\) and \(F=1/2\). These witnesses also cover \(p=2\), where the value is \(0\).

## Verification
The proof uses only the definition of the P-angle, the two classical Clarkson inequalities, one one-variable monotonicity reduction, and explicit two-coordinate extremizers. The derivative reduction was re-expanded symbolically: up to a positive factor its sign is the sign of
\[
u^\alpha-1-(u-1)(1+u)^{\alpha-1},
\]
which is exactly the endpoint-chord inequality for \(G\) after substituting \(v=(u-1)/(u+1)\). No numerical experiment, finite enumeration, or external certificate is used to prove the infinite-dimensional statement.

Boundary checks are exact: the two branches agree at \(p=2\); the endpoint values are \(1/2\); and replacing \(p\) by its Hölder conjugate leaves \(\left|1-2/p\right|\) unchanged.

## Relationship to prior work
Yang and Li introduced \(S_P(X)\), proved the universal bound \(0\le S_P(X)\le1/2\), and in their \(\ell_p\) example exhibited the same natural two-coordinate configurations that furnish lower bounds. Their paper does not provide the matching all-\(p\) upper bound above; the present argument supplies it through Clarkson's inequalities and proves exactness for every real \(\ell_p(I)\) with at least two coordinates.

The Clarkson inequalities are classical and provide the sharp power-sum constraints on \(\|x+y\|_p\) and \(\|x-y\|_p\). A separate 2022 paper on angle moduli in Banach spaces studies different angular invariants and does not imply this exact P-angle constant.

## Limitations
The result is restricted to real \(\ell_p\) sequence spaces. It does not classify equality cases beyond the explicit extremizers, and it makes no claim for general Banach spaces, noncommutative \(L_p\) spaces, or complex P-angle variants. Literature searches cannot exclude an obscure or poorly indexed independent derivation; no such exact all-\(p\) formula was found in the inspected primary source, related angle-moduli paper, or semantic database searches.

## References
1. Zhijian Yang and Yongjin Li, “New Geometric Constant Related to the P-angle Function in Banach Spaces,” arXiv:2208.11239, first public version 2022-08-23.
2. James A. Clarkson, “Uniformly Convex Spaces,” Transactions of the American Mathematical Society 40 (1936), 396–414, DOI 10.1090/S0002-9947-1936-1501880-4.
3. “Some Moduli of Angles in Banach Spaces,” Mathematics 10 (2022), 2965, DOI 10.3390/math10162965.
