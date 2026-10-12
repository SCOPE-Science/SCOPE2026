# Exact completion-time transform for coupon multiplicity counts
## Finding
Consider the classical uniform coupon collector with \(m\ge2\) coupon types. Let \(T_m\) be the first draw at which every type has appeared. At that stopping time, let
\[
K_{m,r}=\#\{i:\text{coupon type }i\text{ has appeared exactly }r\text{ times by }T_m\}.
\]
For \(r\ge2\), define
\[
H_{m-2}(y)
=
\sum_{u\ge m-2}S(u,m-2)y^u
=
\frac{y^{m-2}}{\prod_{j=1}^{m-2}(1-jy)},
\]
where \(S(u,k)\) is a Stirling number of the second kind and \(H_0(y)=1\).

Then, for every integer \(r\ge2\), with \(y=x/m\),
\[
\boxed{
\mathbb E\!\left[K_{m,r}x^{T_m}\right]
=
\frac{m!}{r!}y^{r+1}
\frac{d^r}{dy^r}\left[y^rH_{m-2}(y)\right].
}
\]
This is an exact finite joint transform of completion time and the entire post-completion multiplicity spectrum above the singleton coordinate. In particular, differentiation in \(x\) gives every mixed factorial moment of \(T_m\) with \(K_{m,r}\).

For doubletons, write
\[
H_m^{(q)}=\sum_{k=1}^m\frac1{k^q},
\qquad
H_m=H_m^{(1)}.
\]
The transform gives
\[
\boxed{
\mathbb E K_{m,2}
=
\frac12\left(H_m^2-2H_m+H_m^{(2)}\right)
}
\]
and the exact covariance
\[
\boxed{
\operatorname{Cov}(T_m,K_{m,2})
=-\frac m2
\left[
H_m^2-2H_mH_m^{(2)}+3H_m^{(2)}-2H_m^{(3)}
\right].
}
\]
It is zero for \(m=2\) and strictly negative for every \(m\ge3\). Hence unusually long completion histories are accompanied, in the second-moment sense, by fewer coupon types left at multiplicity exactly two.

Moreover,
\[
\operatorname{Cov}(T_m,K_{m,2})
=
-\frac12m(\log m)^2+O(m\log m).
\]

## Assumptions and scope
Coupon draws are independent and each of the \(m\) types has probability \(1/m\). The stopping rule is the first complete collection. The statistic \(K_{m,r}\) is evaluated at that random stopping time, not after a deterministic number of draws.

The transform is asserted for \(r\ge2\). The singleton coordinate is deliberately excluded from the originality claim because the exact joint distribution of completion time and the number of singletons was treated previously.

## Proof
Fix integers \(m\ge2\), \(r\ge2\), and \(t\ge m\). Consider all length-\(t\) coupon sequences whose first complete collection occurs on draw \(t\), and sum \(K_{m,r}\) over those sequences.

The final draw must be the first appearance of one distinguished coupon type \(\ell\). A type counted by \(K_{m,r}\), with \(r\ge2\), is necessarily different from \(\ell\). Choose the ordered pair consisting of the last new type \(\ell\) and a marked multiplicity-\(r\) type \(i\); there are \(m(m-1)\) choices.

Among the first \(t-1\) positions, choose the \(r\) locations occupied by \(i\). The type \(\ell\) occurs nowhere before the final draw. Every one of the remaining \(m-2\) types must occur at least once in the remaining \(t-1-r\) positions. The number of onto assignments to those types is
\[
(m-2)!S(t-1-r,m-2).
\]
Therefore the total \(K_{m,r}\)-weight of successful sequences of length \(t\) is
\[
m!\binom{t-1}{r}S(t-1-r,m-2).
\]
Since every length-\(t\) sequence has probability \(m^{-t}\),
\[
\mathbb E\!\left[K_{m,r}\mathbf 1\{T_m=t\}\right]
=
\frac{m!}{m^t}
\binom{t-1}{r}S(t-1-r,m-2).
\]
Put \(u=t-1-r\) and \(y=x/m\). The ordinary generating function of the Stirling numbers is
\[
H_{m-2}(y)
=
\sum_{u\ge m-2}S(u,m-2)y^u.
\]
The derivative identity
\[
\frac1{r!}\frac{d^r}{dy^r}\left[y^rH_{m-2}(y)\right]
=
\sum_{u\ge m-2}\binom{u+r}{r}S(u,m-2)y^u
\]
then gives the displayed joint transform after multiplication by \(m!y^{r+1}\).

For \(r=2\), differentiate the rational function at \(y=1/m\). The logarithmic derivatives of
\[
H_{m-2}(y)=\frac{y^{m-2}}{\prod_{j=1}^{m-2}(1-jy)}
\]
reduce to finite harmonic sums. Simplification gives
\[
\mathbb E K_{m,2}
=
\frac12\left(H_m^2-2H_m+H_m^{(2)}\right).
\]
Also,
\[
\mathbb E[T_mK_{m,2}]
=
\left.x\frac{d}{dx}\mathbb E[K_{m,2}x^{T_m}]\right|_{x=1}.
\]
Subtracting \(\mathbb ET_m\,\mathbb EK_{m,2}\), with the classical identity
\[
\mathbb ET_m=mH_m,
\]
yields
\[
\operatorname{Cov}(T_m,K_{m,2})
=-\frac m2 B_m,
\]
where
\[
B_m
=
H_m^2-2H_mH_m^{(2)}+3H_m^{(2)}-2H_m^{(3)}.
\]
Now \(B_2=0\), and direct subtraction gives
\[
B_{n+1}-B_n
=
\frac{2}{(n+1)^3}
\left[
n(n+1)H_n-(n+1)^2H_n^{(2)}+2n
\right].
\]
The bracket equals
\[
(n-1)+(n+1)\sum_{k=2}^n\frac{n(k-1)-1}{k^2},
\]
which is strictly positive for \(n\ge2\). Thus \(B_m>0\) for every \(m\ge3\), proving the sign claim.

Finally, \(H_m=\log m+O(1)\), while \(H_m^{(2)}\) and \(H_m^{(3)}\) remain bounded. Substitution gives
\[
\operatorname{Cov}(T_m,K_{m,2})
=
-\frac12m(\log m)^2+O(m\log m).
\]

## Verification
The accompanying `checker.py` has two independent finite replay layers. First, it exhaustively enumerates coupon sequences for small \(m\) and \(t\), retains exactly those for which the first complete collection occurs on the final draw, computes the multiplicity spectrum directly, and verifies the Stirling-number coefficient formula.

Second, it checks the doubleton mean and covariance identities exactly with rational arithmetic for a large range of \(m\). It also verifies the positive increment formula for \(B_m\), which certifies the finite sign argument independently of floating-point numerics.

Finite enumeration is supplementary; the all-\(m\), all-\(r\ge2\) theorem is proved by the counting and generating-function argument above.

## Relationship to prior work
Myers and Wilf derived the exact joint distribution of completion time and the number of singleton coupon types at successful termination. That result covers the coordinate \(r=1\), which is why the transform here is stated only for \(r\ge2\).

Mahmoud and Smythe study the joint behavior of coupon types collected exactly \(r\) times, but their phases are prescribed by deterministic or externally randomized sample sizes rather than by the first-completion stopping rule. Their framework establishes the importance of the full multiplicity spectrum but does not supply the stopping-time transform above.

Recent work on the siblings version of coupon collection gives exact harmonic-polynomial expectations for residual album deficits at the main completion time and joint asymptotic behavior among those deficits. Those marginal completion-time spectrum identities imply many expectations of the \(K_{m,r}\), so the marginal doubleton mean is not itself the originality claim. The contribution here is the additional completion-time variable: the exact transform \(\mathbb E[K_{m,r}x^{T_m}]\) and its mixed-moment consequences, including the finite negative doubleton covariance.

## Limitations
The formula uses equal coupon probabilities. For nonuniform coupon probabilities, the marked type and the final new type carry unequal weights and the Stirling-number reduction no longer applies in this form.

The result gives a one-coordinate transform for each \(K_{m,r}\); it does not give the full multivariate generating function of all multiplicity counts jointly with \(T_m\).

Older occupancy or coupon-collector literature may encode an equivalent derivative identity under a different generating-function notation. Targeted full-text and semantic comparisons did not locate such a statement, but this remains the principal originality risk.

## References
1. A. N. Myers and H. S. Wilf, “Some new aspects of the coupon-collector's problem,” arXiv:math/0304229, first submitted 16 April 2003.
2. H. M. Mahmoud and R. T. Smythe, “On the Joint Behavior of Types of Coupons in Generalized Coupon Collection,” *Advances in Applied Probability* 44 (2012). DOI: 10.1239/aap/1339878719.
3. C. D. Long, “Extremality and Limit Laws for the Siblings of the Coupon Collector,” arXiv:2606.29635, 2026.
