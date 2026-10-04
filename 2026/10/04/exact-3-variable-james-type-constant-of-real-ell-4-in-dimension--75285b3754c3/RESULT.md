# Exact 3-variable James type constant of real \(\ell_4\) in dimension at least three
## Finding
For every real sequence space \(X=\ell_4(I)\) with \(|I|\ge 3\), define
\[
J_T(X)=\sup_{x,y,z\in S_X}\min\{\|x-y\|,\|y-z\|,\|z-x\|\}.
\]
Then
\[
J_T(X)=(1+\sqrt[3]{2})^{3/4}=1.843189342150636\ldots.
\]
The value is attained already in a three-coordinate subspace.

## Assumptions and scope
The scalar field is real, and \(I\) is any index set with at least three elements. The norm is \(\|x\|_4=(\sum_{i\in I}|x_i|^4)^{1/4}\). No claim is made here for two-dimensional \(\ell_4^2\), where the three-point packing problem has a different dimensional constraint.

## Proof
Set \(r=\sqrt[3]{2}\) and \(K=(1+r)^3\). We first prove the sharp scalar inequality
\[
(a-b)^4+(b-c)^4+(c-a)^4\le K(a^4+b^4+c^4) 
\tag{1}
\]
for all real \(a,b,c\).

By homogeneity, maximize the quotient of the two sides of (1) over \(a^4+b^4+c^4=1\). At a maximizer with three distinct coordinates, the Lagrange equations are
\[
(a-b)^3+(a-c)^3=\lambda a^3,
\]
with the two cyclic analogues. Subtracting the first two equations and dividing by \(a-b\), and doing the same cyclically, gives bracket equations whose differences are
\[
-\lambda(a-c)(a+b+c)=0,\qquad
\lambda(a-b)(a+b+c)=0.
\]
Multiplying the three Lagrange equations by \(a,b,c\) and summing gives \(\lambda=N/D\), where \(N\) and \(D\) are the numerator and denominator of the quotient. At a maximizing nonconstant triple this is positive, so \(\lambda>0\); distinctness therefore forces \(a+b+c=0\). Direct expansion then gives
\[
(a-b)^4+(b-c)^4+(c-a)^4=9(a^4+b^4+c^4).
\]

A larger value is obtained when two coordinates coincide. If their common value is nonzero, scaling gives a triple of the form \((1,1,t)\), and its quotient is
\[
f(t)=\frac{2(1-t)^4}{2+t^4}.
\]
If the common value is zero, the quotient is \(2\), so it cannot be maximal once a value above \(9\) is exhibited. For the nonzero-common-value family, the derivative factors as
\[
f'(t)=\frac{8(t-1)^3(t^3+2)}{(t^4+2)^2}.
\]
Hence the global maximum on the extended real line occurs at \(t=-r\). Using \(r^3=2\),
\[
f(-r)=\frac{2(1+r)^4}{2+r^4}=(1+r)^3=K>9.
\]
Thus (1) is sharp, with equality at permutations and nonzero scalar multiples of \((1,1,-r)\).

Now let \(x,y,z\in S_X\). Applying (1) coordinatewise and summing yields
\[
\|x-y\|_4^4+\|y-z\|_4^4+\|z-x\|_4^4
\le K(\|x\|_4^4+\|y\|_4^4+\|z\|_4^4)=3K.
\]
Therefore at least one of the three fourth powers is at most \(K\), so
\[
J_T(X)\le K^{1/4}=(1+\sqrt[3]{2})^{3/4}.
\]

For equality, choose three distinct coordinates and put \(s=[2(1+r)]^{-1/4}\). On those coordinates define
\[
x=s(1,1,-r),\qquad y=s(1,-r,1),\qquad z=s(-r,1,1),
\]
with all remaining coordinates zero. Since \(r^4=2r\), each vector has fourth-power norm \(s^4(2+r^4)=1\). Every pairwise difference has fourth-power norm
\[
2s^4(1+r)^4=(1+r)^3=K.
\]
Thus all three distances equal \(K^{1/4}\), proving the lower bound and hence the formula.

## Verification
The proof reduces the infinite-dimensional statement to the sharp scalar inequality (1). The Lagrange-multiplier calculation exhausts the compact normalized scalar problem: an all-distinct stationary point has quotient \(9\), while every repeated-coordinate case reduces to the one-variable function \(f\), whose derivative has exactly the displayed real critical factors. The equality triple satisfies the normalization and all three distance identities algebraically from \(r^3=2\). No finite experiment is used as a substitute for an infinite-dimensional argument.

## Relationship to prior work
Ni, Liu, Zhou and Xia introduced \(J_T\) as a three-variable James type constant and established general bounds, the inner-product value, and values for selected spaces. Their author-uploaded March 2024 preprint was inspected for the defining statement and its concrete examples; no exact value for real \(\ell_4\), nor a general exact \(\ell_p\) formula implying the result above, was found there. Searches under the names “3-variable James type constant”, “three-point packing on the unit sphere”, and classical James-constant variants likewise did not identify a statement implying this \(\ell_4\) formula.

## Limitations
The theorem requires at least three coordinates because the sharp equality configuration uses three cyclic coordinate patterns. It does not determine \(J_T(\ell_4^2)\), nor does it assert an exact formula for \(\ell_p\) when \(p\ne4\). The bibliographic search found no equivalent published formula, but terminology from spherical-code or metric-packing literature can differ; that remains a residual literature risk rather than a mathematical gap in the proof.

## References
Q. Ni, Q. Liu, Y. Zhou, and J. Xia, “3-variable James type constants in Banach spaces,” author-uploaded preprint, public full text uploaded 2024-03-24, Mathematics Subject Classification 46B20, 46C15, ResearchGate publication 379237890, https://www.researchgate.net/publication/379237890_3-variable_James_type_constants_in_Banach_spaces.
