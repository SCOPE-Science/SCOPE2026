# Exact pointwise James profile of finite-dimensional \(\ell_\infty^n\)
## Finding
Let \(n\ge 2\) and let \(X=\ell_\infty^n\) over the reals. For \(x=(x_1,\ldots,x_n)\in S_X\), define \(s_2(x)\) to be the second-largest member of the multiset \(\{|x_1|,\ldots,|x_n|\}\). For every finite real parameter \(t\ge1\),
\[
J(x,\ell_\infty^n,t)=\left(\frac{2^t+(1+s_2(x))^t}{2}\right)^{1/t}.
\]
Hence the pointwise profile is nonconstant for every finite \(t\ge1\). Its minimum is \(\left((2^t+1)/2\right)^{1/t}\), attained at coordinate unit vectors, and its maximum is \(2\), attained exactly at those sphere points having at least two coordinates of modulus \(1\).

## Assumptions and scope
The pointwise James type constant is
\[
J(x,X,t)=\sup_{y\in S_X} M_t(\lVert x-y\rVert,\lVert x+y\rVert),
\qquad
M_t(a,b)=\left(\frac{a^t+b^t}{2}\right)^{1/t},
\]
with \(1\le t<\infty\). The statement concerns finite-dimensional real \(\ell_\infty^n\) with \(n\ge2\). It does not claim a formula for \(t<1\), nor for infinite-dimensional \(\ell_\infty\).

## Proof
Rincón-Villamizar's Proposition 4.4 states that for finite-dimensional \(X\) and \(t\ge1\), the supremum may be restricted to the extreme points of \(B_X\). For \(X=\ell_\infty^n\), these are precisely the sign vectors \(\varepsilon\in\{-1,1\}^n\).

Signed coordinate permutations are isometries of \(\ell_\infty^n\). Thus, after applying such an isometry, write
\[
x=(1,a_2,\ldots,a_n),\qquad 1\ge a_2\ge\cdots\ge a_n\ge0,
\]
so that \(a_2=s_2(x)\).

Fix a sign vector \(\varepsilon\). If \(\varepsilon_1=1\), then \(\lVert x+\varepsilon\rVert_\infty=2\). In the other shifted vector, the first coordinate is zero; for \(i\ge2\), a coordinate with \(\varepsilon_i=1\) contributes \(|a_i-1|\le1\), while a coordinate with \(\varepsilon_i=-1\) contributes \(a_i+1\le a_2+1\). Therefore
\[
\lVert x-\varepsilon\rVert_\infty\le1+a_2.
\]
If \(\varepsilon_1=-1\), the same argument with the two shifted vectors exchanged gives the corresponding bound with the two shifted norms interchanged. Thus their unordered pair is coordinatewise bounded by \(\{2,1+a_2\}\). Because \(M_t\) is increasing in each variable, every vertex contributes at most \(M_t(2,1+a_2)\).

Equality is attained by taking \(\varepsilon_1=1\), \(\varepsilon_2=-1\), and \(\varepsilon_i=1\) for \(i\ge3\). Then
\[
\lVert x+\varepsilon\rVert_\infty=2,
\qquad
\lVert x-\varepsilon\rVert_\infty=1+a_2.
\]
Proposition 4.4 therefore yields the displayed formula. Since the formula is strictly increasing in \(s_2(x)\), and \(0\le s_2(x)\le1\), the stated minimum, maximum, and equality cases follow.

## Verification
The proof is finite and exact once Proposition 4.4 is invoked: all possible extreme-point directions are covered by the two cases \(\varepsilon_1=1\) and \(\varepsilon_1=-1\), and the equality sign vector is explicit. The accompanying `verify.py` independently enumerates cube vertices for representative rational sphere points and several values of \(t\); those computations are sanity checks only and are not used as a substitute for the proof.

## Relationship to prior work
Rincón-Villamizar introduced the pointwise James type constant and proved the extreme-point reduction used above. The same paper computes global James-type constants for \(\ell_p\) when \(1\le p<\infty\), but it does not state the pointwise \(\ell_\infty^n\) formula above. A 2004 paper of Tang, Ji, and Wang studies an older pointwise nonsquare constant and reports exact \(\ell_p\) and \(L_p\) values; that older invariant is isosceles-constrained and is not the finite-\(t\) power-mean profile considered here.

A closely related published database result establishes a finite-\(p\) threshold: for real \(\ell_p\) with \(2<p<\infty\), the pointwise James-type profile becomes independent of the base point exactly when \(t\ge p\). The present formula shows that the endpoint \(p=\infty\) behaves differently: no finite \(t\) makes the profile constant.

## Limitations
The result is restricted to finite-dimensional real \(\ell_\infty^n\) and finite \(t\ge1\). No assertion is made here for \(t<1\), for the geometric-mean or minimum endpoints, or for infinite-dimensional \(\ell_\infty\). The full text of the 2004 Tang--Ji--Wang paper was not available during comparison, so its abstract and its description in the 2023 paper were used only to delimit that older invariant; this leaves a small bibliographic residual risk, not a gap in the proof.

## References
1. M. A. Rincón-Villamizar, “The pointwise James type constant,” *Analysis Mathematica* 49 (2023), 651–659, DOI 10.1007/s10476-023-0221-7.
2. X.-W. Tang, D.-H. Ji, and S.-X. Wang, “Pointwise nonsquare constant in normed space,” *Acta Analysis Functionalis Applicata* 6 (2004), 10–15.
