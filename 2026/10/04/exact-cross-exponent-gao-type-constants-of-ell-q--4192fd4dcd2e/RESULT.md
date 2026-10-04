# Exact cross-exponent Gao-type constants of \(\ell_q\)
## Finding
For every real \(\ell_q(I)\) with at least two coordinates, \(1\le q\le\infty\), and every Gao exponent \(r\ge1\), let \(q'\) be the Hölder conjugate and \(s=\min\{q,q'\}\), with endpoint conventions \(1'=\infty\) and \(\infty'=1\). Then
\[
c_{\mathrm{NJ}}^{(r)}(\ell_q(I))=
\begin{cases}
1,&1\le r\le s,\\
2^{1-r/s},&r\ge s.
\end{cases}
\]
Here \(c_{\mathrm{NJ}}^{(r)}(X)=\inf_{x,y\in S_X}(\|x+y\|^r+\|x-y\|^r)/2^r\). Thus the exact phase transition occurs at \(r=\min\{q,q'\}\).

This completely separates the ambient exponent \(q\) from the Gao exponent \(r\). At the transition \(r=s\), both branches equal \(1\).

## Assumptions and scope
The scalar field is real. The coordinate index set \(I\) may be finite or infinite but has at least two elements. For \(1<q<\infty\), \(q'=q/(q-1)\); the endpoint conventions are \(1'=\infty\) and \(\infty'=1\). The Gao-type constant is
\[
c_{\mathrm{NJ}}^{(r)}(X)=\inf_{x,y\in S_X}\frac{\|x+y\|^r+\|x-y\|^r}{2^r}.
\]

## Proof
Put \(a=\|x+y\|_q\) and \(b=\|x-y\|_q\) for \(x,y\in S_{\ell_q(I)}\), and set \(s=\min\{q,q'\}\). The key estimate is
\[
a^s+b^s\ge 2^s.
\]
For \(q=1\) or \(q=\infty\), this is the triangle inequality \(a+b\ge\|2x\|=2\). For \(1<q\le2\), Clarkson's inequality gives
\[
a^q+b^q\ge 2^{q-1}(\|x\|_q^q+\|y\|_q^q)=2^q.
\]
For \(2<q<\infty\), choose norming functionals \(x^*,y^*\in S_{\ell_{q'}(I)}\) with \(x^*(x)=y^*(y)=1\). Writing \(A=\|x^*+y^*\|_{q'}\) and \(B=\|x^*-y^*\|_{q'}\),
\[
4=(x^*+y^*)(x+y)+(x^*-y^*)(x-y)\le Aa+Bb.
\]
Hölder's inequality on \(\mathbb R^2\) and the second Clarkson inequality for exponent \(q'\le2\) give
\[
4\le(A^q+B^q)^{1/q}(a^{q'}+b^{q'})^{1/q'}\le2(a^{q'}+b^{q'})^{1/q'},
\]
so \(a^{q'}+b^{q'}\ge2^{q'}\). This proves the key estimate in all cases.

If \(1\le r\le s\), monotonicity of the two-dimensional power means yields
\[
(a^r+b^r)^{1/r}\ge(a^s+b^s)^{1/s}\ge2,
\]
so the Gao quotient is at least \(1\). Equality is attained by \(y=x\).

If \(r\ge s\), the sharp comparison between the \(\ell_r^2\) and \(\ell_s^2\) norms gives
\[
(a^r+b^r)^{1/r}\ge2^{1/r-1/s}(a^s+b^s)^{1/s}\ge2^{1+1/r-1/s},
\]
hence the quotient is at least \(2^{1-r/s}\). For \(1\le q\le2\), equality is attained by
\[
x=2^{-1/q}(e_1+e_2),\qquad y=2^{-1/q}(e_1-e_2),
\]
for which \(a=b=2^{1-1/q}\). For \(2\le q\le\infty\), equality is attained by \(x=e_1\), \(y=e_2\), for which \(a=b=2^{1/q}\), with \(2^{1/\infty}=1\). Therefore the lower bounds are sharp.

## Verification
The proof is analytic and does not depend on finite enumeration. A standalone deterministic checker samples dimensions \(2,3,5\), multiple values of \(q\) and \(r\), checks sampled quotients against the claimed formula, and evaluates the explicit extremizers. It returns `VERIFY_OK`. These computations are corroborative only; the global infimum is established by the inequalities above.

## Relationship to prior work
Zuo, Huang, Huang, and Wang (2022) define the same Gao-type constant and compute the diagonal case in which the exponent of the constant equals the ambient \(\ell_p\) exponent. Their Example 1 gives \(1\) for \(1<p\le2\), \(2^{2-p}\) for \(p>2\), and \(2^{1-p}\) at the \(\ell_1\) and \(\ell_\infty\) endpoints. The present formula recovers those values by taking \(r=q\), but additionally determines every cross-exponent pair \((q,r)\) and identifies the transition at \(\min\{q,q'\}\). Their introduction reports that the earlier Asif et al. work supplied only universal bounds and the exact \(\ell_1^2\) case. A 2023 paper on the generalized Gao constant studies a distinct supremum-type invariant and does not imply this infimum formula.

## Limitations
No claim is made for complex scalars or for Banach lattices beyond classical \(\ell_q\) spaces. The originality comparison is strongest against the inspected 2022 full text and targeted exact-invariant searches; an obscure source using materially different terminology could remain undiscovered.

## References
1. Z. Zuo, Y. Huang, H. Huang, J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” *Mathematics* 10 (2022), 4591. DOI: 10.3390/math10234591. First published 4 December 2022.
2. Z.-F. Zuo, Y.-M. Huang, J. Wang, “The generalized Gao’s constant of absolute normalized norms in \(\mathbb R^2\),” *Mathematical Inequalities & Applications* 26 (2023), 109–129. DOI: 10.7153/mia-2023-26-09.
3. J. A. Clarkson, “Uniformly convex spaces,” *Transactions of the American Mathematical Society* 40 (1936), 396–414.
