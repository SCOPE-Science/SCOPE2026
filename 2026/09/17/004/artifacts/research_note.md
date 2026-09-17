# SCOPE research note: dimension-three magic positivity for generalized parking-function polytopes

## Claim

Let \(a,b,c\) be positive integers. Then the generalized parking-function
polytope \(\mathfrak X_3(a,b,c)\) is magic positive.

Consequently, Conjecture 8.1 of Hill--Luo--Trinh--Vindas-Meléndez
(arXiv:2607.15503) holds for every parameter vector of length three.

## Input from the literature

Write \(L(b_1,\ldots,b_n)=|\mathfrak X_n(\mathbf b)\cap\mathbb Z^n|\).
Hill et al., Theorem 4.1, give a lattice-slice recursion. In dimension two
their Example 4.2 gives

\[
L_2(x,y)=(x+y)^2-\binom{y+1}{2}.
\]

Their Lemma 5.1 / Corollary 5.6 gives

\[
\operatorname{ehr}_{\mathfrak X_n(\mathbf b)}(t)
=L_n(1+t(b_1-1),tb_2,\ldots,tb_n).
\]

For \(n=3\), the recursion specializes to

\[
L_3(x,y,z)
=xL_2(x+y,z)
+\sum_{r=1}^{y}L_2(x+y-r,z+r)
+\sum_{r=1}^{z}L_2(x,y+z-r).
\]

## Calculation

Expanding,

\[
\begin{aligned}
6L_3(x,y,z)={}&
6x^3+18x^2y+18x^2z+18xy^2+36xyz+9xz^2-9xz\\
&+5y^3+12y^2z-3y^2+6yz^2-12yz-2y\\
&+z^3-3z^2+2z.
\end{aligned}
\]

Put \(x=1+(a-1)t,\ y=bt,\ z=ct\). Write the resulting cubic Ehrhart
polynomial in the magic basis

\[
\operatorname{ehr}(t)
=\mu_0(t+1)^3+\mu_1t(t+1)^2+\mu_2t^2(t+1)+\mu_3t^3.
\]

Set \(A=a-1,\ B=b-1,\ C=c-1\), so \(A,B,C\ge0\). Direct expansion gives

\[
\mu_0=1,
\]

\[
6\mu_1=18A+16B+11C+9,
\]

\[
6\mu_2=
18A^2+36AB+27AC+27A
+15B^2+24BC+22B
+6C^2+14C+9,
\]

and

\[
\begin{aligned}
6\mu_3={}&
6A^3+18A^2B+18A^2C+18A^2
+18AB^2+36ABC+36AB\\
&+9AC^2+27AC+18A
+5B^3+12B^2C+12B^2\\
&+6BC^2+12BC+7B
+C^3+3C^2+2C.
\end{aligned}
\]

Every displayed coefficient is nonnegative for \(A,B,C\ge0\). Therefore
all four magic coefficients are nonnegative, proving magic positivity.

## Checks

The attached verification script derives the formulas symbolically and also
enumerates lattice points directly from the defining inequalities, independently
of the slice recursion, for every \(1\le a,b,c\le5\) and \(1\le t\le4\):
500 parameter/dilation cases, with no discrepancy.

It also recovers the published examples

\[
\operatorname{ehr}_{\mathfrak X_3(3,2,2)}(t)
=172t^3+84t^2+15t+1
\]

with magic coefficients \((1,12,57,102)\), and for
\((a,b,c)=(2,3,1)\) the magic coefficients
\((1,59/6,115/3,54)\).

## Originality status

Qualified same-model review PASS, to the best of current searches. Hill et al.
explicitly leave arbitrary parameter vectors open, report checking all
\(\mathbf b\in\{1,2,3,4\}^3\) computationally, and formulate Conjecture 8.1.
Searches through 17 September 2026 found no subsequent proof of the complete
length-three case. Related results cover the two-parameter family
\((a,b,\ldots,b)\), stable partial permutohedra, Pitman--Stanley polytopes,
or sufficiently-large type-Y generalized permutohedra, not arbitrary
\((a,b,c)\).
