# Exact support-budget profile for the weighted maximum coefficient inequality
## Finding
Fix integers \(m\ge 1\) and \(s\ge 1\), and exponents \(1\le p,t\le\infty\). For a complex \(m\)-homogeneous polynomial
\[
P(z)=\sum_{|\alpha|=m}a_{\alpha}z^{\alpha}
\]
on \(\ell_p^n\), let \(C_{m,p,t}^{(s)}\) be the least dimension-free constant for which
\[
\max_{|\alpha|=m}|a_{\alpha}u^{\alpha}|
\le C_{m,p,t}^{(s)}\,\|u\|_t^m\,\|P\|_p
\]
holds whenever \(\#\operatorname{supp}u\le s\). Put \(k=\min\{s,m\}\).

If \(t\le p\), then
\[
C_{m,p,t}^{(s)}=1.
\]
If \(p<t\), write
\[
m=kq+r,\qquad q=\lfloor m/k\rfloor,\qquad 0\le r<k.
\]
Then
\[
C_{m,p,t}^{(s)}=
\left(
\frac{m^m}{q^{q(k-r)}(q+1)^{(q+1)r}}
\right)^{1/p-1/t}.
\]
For \(p<t\), the constants increase strictly with the support budget through \(s=1,\ldots,m\) and stabilize for \(s\ge m\). Thus the one-coordinate constant is \(1\), while the unrestricted value at \(s\ge m\) is exactly \(m^{m(1/p-1/t)}\), recovering the sharp unrestricted constant in Barbosa--Núñez-Alarcón--Raposo--Santos.

## Assumptions and scope
The scalar field is \(\mathbb C\). The polynomial norm \(\|P\|_p\) is the supremum of \(|P(z)|\) over the unit ball of \(\ell_p^n\). The convention \(1/\infty=0\) is used. The support restriction is on the diagonal weight vector \(u\), not on the set of nonzero monomials of \(P\).

The statement is uniform in the ambient dimension. No restriction is imposed on the number of nonzero coefficients of \(P\).

## Proof
Normalize \(\|u\|_t=1\). If \(u^\alpha=0\), the corresponding term is irrelevant. Otherwise \(\operatorname{supp}\alpha\subseteq\operatorname{supp}u\), so
\[
\#\operatorname{supp}\alpha\le k.
\]

The exact coefficient functional from Barbosa--Núñez-Alarcón--Raposo--Santos gives
\[
|a_\alpha|\le
\left(\frac{m^m}{\alpha^\alpha}\right)^{1/p}\|P\|_p,
\]
where
\[
\alpha^\alpha=\prod_{j:\alpha_j>0}\alpha_j^{\alpha_j}.
\]
Their exact monomial optimization with exponent \(t\) gives
\[
|u^\alpha|\le
\left(\frac{\alpha^\alpha}{m^m}\right)^{1/t}.
\]
Hence
\[
|a_\alpha u^\alpha|
\le
\left(\frac{m^m}{\alpha^\alpha}\right)^{1/p-1/t}\|P\|_p.
\]

When \(t\le p\), the exponent \(1/p-1/t\) is nonpositive and \(m^m/\alpha^\alpha\ge1\), so the right side is at most \(\|P\|_p\). The choice \(P(z)=z_1^m\), \(u=e_1\), gives equality. Thus \(C_{m,p,t}^{(s)}=1\).

Now assume \(p<t\), so \(1/p-1/t>0\). It remains to maximize \(m^m/\alpha^\alpha\) over positive integer exponent patterns with total mass \(m\) and at most \(k\) nonzero parts. Splitting a part \(a\ge2\) into \(a-1\) and \(1\) strictly decreases the product of powered parts, because
\[
(a-1)^{a-1}<a^a.
\]
Therefore a minimizer of \(\alpha^\alpha\) uses exactly \(k\) positive parts. For two parts satisfying \(a\ge b+2\), strict convexity of \(x\mapsto x\log x\) gives
\[
(a-1)\log(a-1)+(b+1)\log(b+1)
< a\log a+b\log b,
\]
so smoothing \((a,b)\) to \((a-1,b+1)\) strictly lowers \(\alpha^\alpha\). Consequently every minimizing exponent pattern is balanced: it has \(k-r\) entries equal to \(q\) and \(r\) entries equal to \(q+1\). Hence
\[
\min \alpha^\alpha=q^{q(k-r)}(q+1)^{(q+1)r},
\]
which proves the upper bound.

For sharpness, take precisely this balanced multi-index \(\alpha^*\) and the monomial \(P(z)=z^{\alpha^*}\). The exact monomial formula gives
\[
\|P\|_p=
\left(\frac{(\alpha^*)^{\alpha^*}}{m^m}\right)^{1/p}.
\]
For finite \(t\), choose \(u_j=(\alpha_j^*/m)^{1/t}\) on the support of \(\alpha^*\) and zero elsewhere. Then \(\|u\|_t=1\) and
\[
|u^{\alpha^*}|=
\left(\frac{(\alpha^*)^{\alpha^*}}{m^m}\right)^{1/t}.
\]
For \(t=\infty\), choose \(u_j=1\) on that support. In both cases the ratio of the left side to \(\|u\|_t^m\|P\|_p\) is exactly the asserted constant.

Finally, when \(p<t\), allowing one additional support coordinate before \(k=m\) permits a strict split of a positive exponent, which strictly lowers the minimal value of \(\alpha^\alpha\). Thus the profile is strictly increasing through support budgets \(1,\ldots,m\), after which no degree \(m\) monomial can use more than \(m\) coordinates and the profile stabilizes.

## Verification
The proof reduces the problem to two exact identities from the focal source and one finite integer optimization that is proved by strict splitting and smoothing. No finite enumeration is used to infer the general statement.

Boundary cases are included. For \(s=1\), one has \(k=1\) and the formula gives \(C_{m,p,t}^{(1)}=1\). For \(s\ge m\), one has \(k=m\), \(q=1\), and \(r=0\), so the formula gives the published unrestricted value \(m^{m(1/p-1/t)}\) when \(p<t\). At \(p=t\), both branches give \(1\). The convention \(1/\infty=0\) makes the sharpness argument valid at \(t=\infty\).

## Relationship to prior work
Barbosa, Núñez-Alarcón, Raposo, and Santos prove the exact coefficient functional and exact monomial optimization used above, and from them derive the unrestricted weighted maximum constant
\[
C_{m,p,t}=
\begin{cases}
m^{m(1/p-1/t)},&p\le t,\\
1,&t\le p.
\end{cases}
\]
Their Proposition 4.4 allows arbitrary \(u\) and does not state the sharp profile when the support of \(u\) is capped.

Caro-Montoya, Núñez-Alarcón, and Serrano-Rodríguez study a different support restriction: the active monomials of the polynomial are required to involve at most a fixed number of variables, and the target is a Bohnenblust--Hille coefficient-sum norm. That result does not determine the present diagonal-weight support profile or the weighted maximum functional.

Targeted searches also compared the claim with support-sensitive Bohnenblust--Hille and monomial-convergence terminology. No inspected source implied the exact support-budget formula above.

## Limitations
The result concerns the maximum-coefficient endpoint only; it does not classify finite-support weight constants for the finite coefficient exponents in the broader weighted Hardy--Littlewood scale. It also does not impose or analyze sparsity of the coefficient support of \(P\).

The originality search found no equivalent statement, but because the proof is a short exact refinement of the focal coefficient estimate, an older observation under monomial-convergence or coordinate-support terminology remains a residual literature risk.

## References
1. A. Barbosa, D. Núñez-Alarcón, A. Raposo, and J. Santos, *Sparse Kahane--Salem--Zygmund Forms and Weighted Hardy--Littlewood Inequalities Across the Critical Endpoint*, arXiv:2610.01500v1, first public 2026-10-01.
2. N. Caro-Montoya, D. Núñez-Alarcón, and D. Serrano-Rodríguez, *Asymptotic Contractivity of Bohnenblust--Hille Constants with Bounded Monomial Support*, Bulletin of the Brazilian Mathematical Society, 57 (2026), Article 40, DOI:10.1007/s00574-026-00527-1.
