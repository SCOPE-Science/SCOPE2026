# Exact one-point type spectrum over rectangular chain-product parameters

## Finding
Let \(\mathbb R\) be the countable universal homogeneous partial order. Fix integers \(a,b\geq1\), and individually name the \(ab\) parameters inducing the product-ordered grid \(P_{a,b}=C_a\times C_b\), with \((i,j)\leq(i',j')\) exactly when \(i\leq i'\) and \(j\leq j'\). Write \(F(a,b)\) for the number of complete first-order one-types over these named parameters, including equality types, and \(N(a,b)\) for the nonalgebraic types. Then
\[
\boxed{F(a,b)=(a+b+3)\binom{a+b}{a}-\binom{a+b+1}{a}-\binom{a+b+1}{b},\qquad N(a,b)=F(a,b)-ab.}
\]
In particular, for square grids,
\[
\boxed{F(n,n)=\left(2n-1+\frac{2}{n+1}\right)\binom{2n}{n}\sim \frac{2}{\sqrt\pi}\sqrt n\,4^n.}
\]
At fixed \(a\geq1\), \(F(a,b)\) and \(N(a,b)\), viewed as polynomials in \(b\), have exact degree \(a+1\) and leading coefficient \(a/(a+1)!\). Thus the same family has polynomial type growth at fixed grid width and exponential growth along square grids. The square totals for \(n=1,\ldots,8\) are \(4,22,110,518,2352,10428,45474,195910\).

## Assumptions and scope
The product order is non-strict; its associated strict relation is denoted \(<\). Complete one-types are the orbits on points under the pointwise stabilizer of the named finite grid in \(\operatorname{Aut}(\mathbb R)\), by ultrahomogeneity and one-point extension realization. Exactly \(ab\) types are algebraic (one equality type per parameter). Every other type specifies a finite one-point extension. All order ideals/filters below are *downward/upward closed subsets*, including the empty subset (not necessarily directed lattice ideals). The displayed all-size theorem assumes \(a,b\geq1\). The binomial expression also evaluates to \(1\) at a zero dimension, as expected for empty parameters, but that trivial boundary is not required for the theorem.

## Proof
**Step 1: admissible one-point relations.** For a point \(x\) not among the named parameters, let \(L=\{p:p<x\}\) and \(U=\{p:x<p\}\). Transitivity requires that \(L\) is a down-set, \(U\) an up-set and \(\ell<u\) for every \(\ell\in L\), \(u\in U\). Conversely, these three properties make the relation obtained by inserting \(x\) into the parameter poset a partial order with the specified incomparabilities. Its finite extension is realized in \(\mathbb R\). Two realizations induce the same complete type exactly when their finite extensions are isomorphic over the individually named parameters. This established description is used here as background, not claimed as new.

**Step 2: count nonempty lower sets by coordinate maxima.** Let \(J(r,s)=\binom{r+s}{r}\) be the number of down-sets (equally, up-sets) in an \(r\times s\) product of chains; monotone lattice paths give this count, including \(r=0\) or \(s=0\). There are \(J(a,b)\) valid extensions with \(L=\varnothing\), since \(U\) is an arbitrary up-set.

Now suppose \(L\ne\varnothing\). Put \(i=\max\{u:(u,v)\in L\}\) and \(j=\max\{v:(u,v)\in L\}\). Then \(1\le i\le a\), \(1\le j\le b\), and the lower-set property forces all \((u,1)\) for \(u\le i\) and all \((1,v)\) for \(v\le j\) into \(L\). The remaining part is an arbitrary ideal of the interior \((i-1)\times(j-1)\) rectangle, so exactly \(J(i-1,j-1)\) lower sets have these maxima. Precisely one of these has \((i,j)\in L\): the full \(i\times j\) rectangle.

**Step 3: admissible upper sets and a single correction.** A point strictly above every member of \(L\) must belong to \([i,a]\times[j,b]\); every point there works except \((i,j)\) when that corner lies in \(L\). Thus if \((i,j)\notin L\) there are \(J(a-i+1,b-j+1)\) admissible choices of \(U\). If \((i,j)\in L\), the unique invalid up-set is the entire upper-right rectangle, because it contains the forbidden lower-left corner. Hence the number of extensions for each maxima pair \((i,j)\) is exactly \(J(i-1,j-1)J(a-i+1,b-j+1)-1\). Summation yields
\[
N(a,b)=J(a,b)+\sum_{i=1}^{a}\sum_{j=1}^{b}\left[\binom{i+j-2}{i-1}\binom{a+b-i-j+2}{a-i+1}-1\right].\tag{1}
\]

**Step 4: evaluate the convolution by marked paths.** The double sum of the products of binomial coefficients in (1) counts monotone paths from \((0,0)\) to \((a,b)\), each with a marked vertex \((u,v)\) satisfying \(0\le u<a\) and \(0\le v<b\). All marked path vertices, without restrictions, number \((a+b+1)J(a,b)\). Marks on the boundary \(u=a\) number \(\binom{a+b+1}{b}\) by the hockey-stick identity; marks on \(v=b\) number \(\binom{a+b+1}{a}\). Their overlap is the terminal vertex, occurring once per path and therefore counted \(J(a,b)\) times. Inclusion-exclusion gives
\[
\sum_{i=1}^{a}\sum_{j=1}^{b}J(i-1,j-1)J(a-i+1,b-j+1)
=(a+b+2)J(a,b)-\binom{a+b+1}{a}-\binom{a+b+1}{b}.\tag{2}
\]
Combining (1) and (2), \(N(a,b)=(a+b+3)J(a,b)-\binom{a+b+1}{a}-\binom{a+b+1}{b}-ab\). Restoring the \(ab\) equality types proves the boxed formula for \(F(a,b)\).

**Step 5: growth.** At \(a=b=n\), use \(\binom{2n+1}{n}=(2n+1)\binom{2n}{n}/(n+1)\); the exact square formula follows. Stirling's approximation \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) gives the asymptotic. With fixed positive \(a\), the leading terms of \((a+b+3)\binom{a+b}{a}\) and \(\binom{a+b+1}{b}=\binom{a+b+1}{a+1}\) are \(b^{a+1}/a!\) and \(b^{a+1}/(a+1)!\), respectively; \(\binom{a+b+1}{a}\) has only degree \(a\). The asserted positive leading coefficient is therefore \(a/(a+1)!\). Subtracting \(ab\) does not change that leading coefficient.

## Verification
A standalone Python 3 standard-library checker (`verify_grid.py`) directly tests the closed expression against the lattice-path convolution on every \(0\le a,b\le16\), giving 289 identities. A logically separate enumeration loops over all down-sets and up-sets of 29 small grids, checking the strict cross-order condition. A third enumeration assigns all three relative states to each grid point and directly checks transitivity of the resulting \((ab+1)\)-point strict relation for 24 grids. All pass. The recorded output (`verification_output.txt`) ends with `ALL_TESTS_PASS`. The independent finite tests are corroboration; the proof above supplies the infinite-family conclusion. The embedded code and output are part of this package.

## Relationship to prior work
The random poset's Fraïssé one-point extension property is classical; see Droste and Kuske [1]. Dolinka and Mašulović [2], Lemma 3.3 in the arXiv version (Lemma 4.3 in the published pagination), explicitly use sets \(L\) and \(U\) for finite-poset one-point extensions. An existing exact-counting result [3] makes this a general ideal/filter correspondence and establishes #P-completeness over arbitrary finite parameter posets. Accordingly neither the generic correspondence nor the ability to enumerate valid pairs by brute force is claimed here as new. That prior result gives chain and antichain examples, but no closed expression for the parameter family \(C_a\times C_b\), and its general complexity theorem does not supply the evaluated bivariate convolution, exact square asymptotics or fixed-width polynomial law. Known exact methods for series–parallel and tree-cover parameter posets do not cover the entire grid family: for example, the \(2\times3\) grid contains an induced four-point N-order, and its cover graph has diamonds. Standard lattice-path ideal counts are likewise background. Pretzel's classical insertion construction [4] is relevant; its full text was not accessible in the completed comparison and could contain related identities. The present claim is restricted to the explicit grid formula and its demonstrated growth consequences, with that originality qualification.

## Limitations
Only a two-chain Cartesian product is treated; no closed form or efficient algorithm for arbitrary parameter posets is claimed. No statement is made about types of tuples of arity greater than one, about probabilistic distributions of realizations, or about a new general #P classification. The source comparison cannot exclude an equivalent formula in inaccessible or unindexed insertion-position literature. Scientific review is self-review; independent audit and independent validation have not been performed.

## References
1. M. Droste and D. Kuske, *On random relational structures*, Journal of Combinatorial Theory, Series A **102** (2003), 241–254, DOI 10.1016/S0097-3165(03)00004-9. An author-hosted preliminary full text (15 pp.) was inspected.
2. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, first publicly posted 15 September 2010; Proceedings of the Edinburgh Mathematical Society **55** (2012), 635–656, DOI 10.1017/S0013091510001161. The entire arXiv full text (20 pp.), especially §3.1, Lemma 3.3, was inspected.
3. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly available research record and full result at `https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`, published 4 October 2026. Its complete result statement, proof, scope and limitations were compared.
4. O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics **32** (1980), 59–68, DOI 10.1016/0012-365X(80)90100-4. Abstract and bibliographic information were available; the full paper was not read.
