# Fibonacci staircase and sharp entropy-defect oscillation for golden-rotation ordinal patterns

## Finding
Let \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\), and let \(R(x)=x+\alpha\pmod1\) preserve Lebesgue probability measure on \([0,1)\). For \(n\ge1\), let \(\Pi_n(x)\) record the relative ordering, from smallest to largest, of the \(n\) real representatives
\[
\{x\},\ \{x+\alpha\},\ \ldots,\ \{x+(n-1)\alpha\}.
\]
Write \(H_n=-\sum_\pi\Pr(\Pi_n=\pi)\log\Pr(\Pi_n=\pi)\), with natural logarithms and \(H_1=0\). Set \(F_1=F_2=1\), \(F_{j+1}=F_j+F_{j-1}\), and
\[
C=-\alpha\log\alpha-\alpha^2\log(\alpha^2)=(2-\alpha)\log\varphi.
\]
**For every integer \(m\ge2\), and every integer \(F_m\le n<F_{m+1}\),** the finite-order ordinal information gain has the exact Fibonacci staircase
\[
\boxed{H_{n+1}-H_n=C\alpha^{m-2}.}\tag{1}
\]
Moreover its entire finite-order entropy is explicitly
\[
\boxed{H_n=(m-2)\log\varphi+\frac C5\bigl(1-(-\alpha^2)^{m-2}\bigr)
+(n-F_m)C\alpha^{m-2}.}\tag{2}
\]
In particular \(H_n/\log n\to1\). Defining \(L=C\varphi^2/\sqrt5\), the full subsequential accumulation set of the scaled information gain is
\[
\boxed{\operatorname{Acc}\bigl(n(H_{n+1}-H_n)\bigr)=[L,\varphi L].}\tag{3}
\]
For any sequence \(m\to\infty\) and \(F_m\le n_m<F_{m+1}\) satisfying \(n_m/F_m\to t\in[1,\varphi]\), the logarithmic entropy defect has the **sharp phase profile**
\[
H_{n_m}-\log n_m\longrightarrow
G(t)=\tfrac12\log5-2\log\varphi+\frac C5+L(t-1)-\log t.\tag{4}
\]
Its full accumulation interval is
\[
\boxed{\operatorname{Acc}(H_n-\log n)=
\left[G(1)+1-L+\log L,\ G(1)\right].}\tag{5}
\]
Here \(L=0.778617088734806\ldots\), \(\varphi L=1.259828913794409\ldots\), and the endpoints of (5) are approximately \(-0.0535540013665\) and \(-0.0247010166134\). Although the underlying rotation has zero measure-theoretic entropy, its finite-order ordinal uncertainties have a nonconstant log-periodic defect and an exact Fibonacci increment staircase.

## Assumptions and scope
The ordering uses real representatives in \([0,1)\), not cyclic order on the circle. All indices are positive integers, the rotation slope is the *specified golden irrational*, the initial phase is uniformly distributed, and entropies use natural logarithms. Ties between distinct orbit coordinates do not occur because \(\alpha\) is irrational. This is the difference of the entropies of successive **single ordinal partitions**, also called sorting entropy; it is *not* the conditional entropy between two time-shifted ordinal patterns. In the usual Sturmian coding of this rotation, the same phase partition occurs for length-\((n-1)\) symbolic blocks; accordingly the result also describes finite-block Shannon entropy of that specific invariant Sturmian measure under the corresponding indexing. It does not describe entropy of canonical finite-type covers of the Sturmian language.

## Proof
**1. The ordinal probability atoms are rotation gaps.** For \(n\ge2\), the ordering of the \(n\) real orbit representatives can change only when a coordinate wraps through zero, namely at the \(n\) distinct phase points \(-j\alpha\pmod1\), \(0\le j<n\). As one crosses each such point, exactly the associated coordinate moves from largest to smallest; the circular ordering of the coordinate labels is otherwise fixed. Thus all \(n\) intervening arcs yield *distinct* linear permutations. Their probabilities are precisely their lengths. For \(n=1\) there is one atom of length one and the same statement holds. Reflection of all phase points does not change the multiset of gaps. Consequently \(H_n\) is the Shannon entropy of the circular gaps between \(\{j\alpha\}\), \(0\le j<n\).

**2. Exact one-sided Fibonacci neighbor lemma.** Set \(P_1=0\), \(P_2=1\), and \(P_{j+1}=P_j+P_{j-1}\). The identities
\[
F_j\alpha-P_j=(-1)^{j+1}\alpha^j,
\qquad |F_jP_{j-1}-F_{j-1}P_j|=1
\]
hold for all \(j\ge2\) (the first also for \(j=1\)). Fix \(m\ge2\). For any \(1\le h<F_{m+1}\), no integer \(p\) can satisfy
\[
\min\{-\alpha^{m-1},\alpha^m\}<
(-1)^{m+1}(h\alpha-p)<
\max\{-\alpha^{m-1},\alpha^m\}.
\]
Indeed the two consecutive integer vectors \((F_m,P_m)\) and \((F_{m-1},P_{m-1})\) are a unimodular basis. Write \((h,p)=a(F_m,P_m)+b(F_{m-1},P_{m-1})\) with integers \(a,b\). If both coefficients are nonnegative and positive, then \(h\ge F_m+F_{m-1}=F_{m+1}\), impossible; if both are nonpositive then \(h\le0\). Otherwise one coefficient vanishes or the coefficients have opposite signs. In either case the signed error is outside the strict interval between the two opposite-signed errors \(\alpha^m\) and \(-\alpha^{m-1}\). This establishes the no-closer-neighbor statement with strict inequalities, including both endpoints. (The sign interchange when \(m\) changes parity is explicitly handled by the prefactor.)

Fix \(F_m\le n<F_{m+1}\). Before \(\{n\alpha\}\) is inserted among \(\{j\alpha\}\), \(0\le j<n\), its two adjacent neighbors are precisely the points indexed by \(n-F_m\) and \(n-F_{m-1}\). Their two circular distances to the new point are \(\alpha^m\) and \(\alpha^{m-1}\), in some order. To see that none of the other earlier points is between them, subtract its index from \(n\) to obtain \(1\le h\le n<F_{m+1}\), then apply the preceding no-closer-neighbor lemma. For \(m=2,n=1\), the two predecessor indices coincide at zero but describe opposite sides of that same circle point, and the conclusion is unchanged. The pre-insertion gap therefore has length
\[
\alpha^m+\alpha^{m-1}=\alpha^{m-2},
\]
using \(\alpha+\alpha^2=1\).

**3. Exact entropy increment.** Inserting the next phase point affects exactly this one gap; it replaces a length \(\alpha^{m-2}\) by lengths \(\alpha^{m-1}\) and \(\alpha^m\). Since entropy is \(-\sum p\log p\), the change equals
\[
-\alpha^{m-1}\log\alpha^{m-1}-\alpha^m\log\alpha^m
+\alpha^{m-2}\log\alpha^{m-2}
=C\alpha^{m-2}.
\]
This proves (1) simultaneously for all positive integer lengths, without finite-size extrapolation.

**4. Closed entropy and scaled limit.** The interval \(F_j\le n<F_{j+1}\) contains \(F_{j-1}\) integer indices. Summation of (1), beginning with \(H_1=0\), gives
\[
H_n=C\sum_{j=2}^{m-1}F_{j-1}\alpha^{j-2}+(n-F_m)C\alpha^{m-2}.
\]
Binet's identity gives
\[
F_{j-1}\alpha^{j-2}=\frac\varphi{\sqrt5}-\frac{(-1)^{j-1}\alpha^{2j-3}}{\sqrt5}.
\]
Summing the geometric term, using \(\alpha/(\sqrt5(1+\alpha^2))=1/5\) and \(C\varphi/\sqrt5=\log\varphi\), yields exactly (2). These identities also imply \(H_n=\log n+O(1)\) for \(n\to\infty\).

For the same Fibonacci window, Binet's formula gives \(F_m\alpha^{m-2}\to\varphi^2/\sqrt5\), \(F_m\sim\varphi^m/\sqrt5\), and \(F_{m+1}/F_m\to\varphi\). Combining these asymptotics with (1) shows every subsequential limit of \(n(H_{n+1}-H_n)\) lies in \([L,\varphi L]\). For every \(t\in[1,\varphi]\), selecting an integer in the window nearest to \(tF_m\), clamped to its endpoints, realizes that limit: (3) is therefore the *entire* accumulation set. Substituting \(n/F_m\to t\) into (2), and subtracting \(\log n\), yields (4). The continuous function \(G\) is strictly convex because \(G''(t)=1/t^2>0\), satisfies \(G(1)=G(\varphi)\), and has its unique minimum at \(t=1/L\). The inequalities \(1<1/L<\varphi\) follow from the displayed exact value of \(L\) (or elementary bounds on \(\log\varphi\)); hence its range is the interval (5). The same clamped-index argument realizes every value in that range.

## Verification
`verify.py` performs a separate finite exact-field computation in \(\mathbb Q(\sqrt5)\): it inserts 2000 successive orbit points using algebraic-number sign comparisons, verifies their neighboring Fibonacci indices and both gap lengths at every insertion, and checks entropy increments with floating-point logarithms. The check covers sixteen Fibonacci windows and reports the stated constants. An independent enumeration of sorted rotation gaps for lengths 1 through 119 also reproduced the closed expression (2), within floating-point rounding. Neither finite experiment proves the all-length assertions; the unimodular-lattice argument in Step 2 does.

## Relationship to prior work
Bandt and Pompe [1] introduced the ordinal-pattern/permutation-entropy framework. Unakafov and Keller [2, Sections 2.2 and 4] analyze sorting entropy and conditional entropy of ordinal patterns in general and discuss periodic maps and a *different expanding golden-mean map*. Their inspected treatment does not state (1)--(5) for irrational golden rotation. Classical Sturmian coding and the three-gap theorem supply the foundational correspondence between Sturmian block frequencies and rotation gaps, and are acknowledged as prior mathematical machinery. In particular, (1)--(5) can equally be interpreted as an exact finite-block Shannon-entropy statement for the corresponding Sturmian process; this is not a second independent result.

A published 2026 result [3] proves a *different* Fibonacci staircase for the **topological entropies of canonical shifts-of-finite-type approximations** of the Fibonacci Sturmian subshift, whose values solve an exponential return-loop equation. Neither that invariant nor its scaled interval is (1)--(5), and its statement does not imply these probability-weighted ordinal-entropy formulas. General three-gap frequencies determine the relevant gap lengths, but the inspected literature did not provide the explicit entropy-increment plateaux and complete defect accumulation interval stated here. A prior equivalent computation of Shannon block entropy under different terminology remains a substantive historical-priority risk.

## Limitations
The proof is for the precise golden irrational slope and Lebesgue initial law, not arbitrary irrational rotations, other invariant input measures, irregular observation times, or genuinely successive-pattern conditional entropy. The full finite-word frequency and entropy information is obtainable in principle from classical Sturmian gap structure; novelty is claimed only for the specified exact finite-scale entropy profile and sharp fluctuations, not the underlying three-gap theorem or sorting-entropy definitions. Historical coverage outside inspected full texts is unresolved. There has been no independent scientific audit.

## References
[1] Christoph Bandt and Bernd Pompe, *Permutation Entropy: A Natural Complexity Measure for Time Series*, Physical Review Letters 88, 174102 (first public 2002-04-11), https://doi.org/10.1103/PhysRevLett.88.174102.

[2] Anton M. Unakafov and Karsten Keller, *Conditional entropy of ordinal patterns*, arXiv:1407.5390v1 (first public 2014-07-21), https://arxiv.org/abs/1407.5390; especially Sections 2.2, 3 and 4.

[3] *A Fibonacci entropy staircase and its full scaled accumulation interval*, research record published 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-fibonacci-entropy-staircase-and-its-full-scaled-accumulation-i--be7c0c99809f (distinguishable finite-type-cover invariant; comparison only).
