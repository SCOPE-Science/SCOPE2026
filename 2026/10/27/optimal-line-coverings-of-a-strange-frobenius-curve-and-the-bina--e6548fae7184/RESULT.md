# Optimal line coverings of a strange Frobenius curve and the binary boundary

## Finding
Let \(p\) be prime, let \(m\ge1\) be odd, put \(q=p^m\), and let
\[
C:\quad YZ^{p^2-1}=X^{p^2}\subset\mathbb P^2_{\mathbb F_q}.
\]
Write \(P_s=[s:s^{p^2}:1]\), \(s\in\mathbb F_q\), and \(P_\infty=[0:1:0]\). Every line through two distinct affine rational points contains exactly \(p\) such points; its affine parameter set is precisely an affine \(\mathbb F_p\)-line in the \(m\)-dimensional vector space \(\mathbb F_q\). Every affine \(\mathbb F_p\)-line occurs once, producing the \(2\text{-}(q,p,1)\) design with \(q(q-1)/(p(p-1))\) blocks.

For **odd** \(p\), all optimal \(q/p+1\)-element line coverings of \(C(\mathbb F_q)\) are obtained, uniquely, by choosing an arbitrary affine line spread (a partition into affine \(\mathbb F_p\)-lines) of \(\mathrm{AG}(m,p)\), taking the corresponding \(q/p\) secants, and adjoining one arbitrary \(\mathbb F_q\)-line through \(P_\infty\). For odd \(m\ge3\), this produces at least
\[
(q+1)(p+1)^{p^{m-2}}
\]
distinct optimal covering sets. The odd-characteristic conclusion fails sharply: for \(p=2\), every odd \(m\ge3\) admits an optimal cover with a repeated affine point among its two-secants and one affine point covered only by the line through infinity.

## Assumptions and scope
All rational points and covering lines are defined over \(\mathbb F_q\), not over its algebraic closure. A covering is a **set of distinct projective lines**, and optimal means minimum cardinality. The algebraic curve is the specific nonreflexive plane curve above; it is not a claim about every strange plane curve. The finite vector space \(\mathbb F_q\) is identified with \(\mathrm{AG}(m,p)\) only at the level of its affine \(\mathbb F_p\)-structure. An affine line spread is a partition into (possibly differently directed) affine one-dimensional \(\mathbb F_p\)-subspaces. The lower bound and an explicit optimal pencil covering were proved by Asgarli--Dassarma--Ghioca--MacLean--Stokdyk, Proposition 4.1 (2026).

## Proof
**1. Rational points and secants.** The projective equation yields exactly the \(q\) affine points \(P_s\) and the point \(P_\infty\). Since \(m\) is odd,
\[
\gcd(p^2-1,p^m-1)=p-1.
\]
For distinct \(s,t\), set \(u=t-s\ne0\) and \(A=u^{p^2-1}\). The unique projective line through \(P_s,P_t\) has affine equation
\[
y=Ax+B,\qquad B=s^{p^2}-As.
\]
Its affine graph points correspond to solutions of \(x^{p^2}-Ax=B\). The additive map \(x\mapsto x^{p^2}-Ax\) has kernel \(u\mathbb F_p\): nonzero kernel elements are precisely \(u v\) with \(v^{p^2-1}=1\), and the displayed gcd forces \(v\in\mathbb F_p^\times\). Hence the full line section is \(\{P_{s+uv}:v\in\mathbb F_p\}\), of cardinality \(p\). Conversely every \(s+u\mathbb F_p\) arises from its distinct point pair, and two affine subsets give the same geometric line only when they coincide. Every pair of affine graph points belongs to a unique maximal section, establishing the asserted Steiner design. Lines through \(P_\infty\) are exactly \(Z=0\) and \(X=aZ\), \(a\in\mathbb F_q\); they contain zero or one affine graph point, respectively. All other lines meet the affine graph in either zero, one, or \(p\) rational points (an empty or nonempty fiber of an additive polynomial).

**2. Shape of an optimal cover when \(p\ge3\).** Proposition 4.1 gives the minimum \(k=q/p+1\). Let an optimal covering contain \(r\) lines through \(P_\infty\); necessarily \(r\ge1\). The other \(k-r\) lines cover at most \(p\) affine graph points each; lines through \(P_\infty\) each cover at most one. If \(r\ge2\), the maximum number of affine points covered is
\[
p(k-r)+r=q+p-(p-1)r\le q-p+2<q,
\]
a contradiction. Thus \(r=1\), and the other \(q/p\) lines must all be maximal \(p\)-secants: if one had at most one affine rational point, all those secants plus the single infinity line would cover at most \(q-p+2<q\) affine points. There are exactly \(q\) incidences, counting repetitions, among the maximal secants. Since the line through infinity contributes at most one affine point, these secants either partition all \(q\) points, or cover exactly \(q-1\) points. In the latter case their incidence multiset has one double-covered parameter \(a\) and one omitted parameter \(b\ne a\).

Each affine \(\mathbb F_p\)-line \(s+u\mathbb F_p\) has coordinate sum
\[
\sum_{v\in\mathbb F_p}(s+uv)=ps+u\sum_{v\in\mathbb F_p}v=0
\]
inside \(\mathbb F_q\), because \(p\) is odd; also \(\sum_{x\in\mathbb F_q}x=0\). Summing all secant parameter multisets therefore gives \(0=a-b\), contradicting \(a\ne b\). Thus the secants partition all affine graph points. The single remaining line can be any of the \(q+1\) lines through \(P_\infty\); conversely every spread and every such final line is an optimal cover, and the choices are recoverable from the line set.

**3. Many nonpencil optimal covers.** Suppose \(m\ge3\). Choose an \(\mathbb F_p\)-linear subspace of dimension two in \(\mathbb F_q\); its \(p^{m-2}\) affine cosets partition \(\mathbb F_q\). Within each two-dimensional affine plane, independently choose any of its \(p+1\) line directions, partitioning that plane into \(p\) parallel affine lines. Different choices yield different spreads, giving \((p+1)^{p^{m-2}}\) distinct spreads. Each of the \(q+1\) possible lines through \(P_\infty\) yields a distinct covering. This proves the displayed lower bound; it is not asserted to enumerate all spreads.

**4. Sharp characteristic-two boundary.** Let \(p=2\) and \(m\ge3\) odd. Any two distinct affine graph points lie on exactly one two-secant, by Step 1. Choose eight distinct field elements labeled \(a_0,\ldots,a_7\) and choose secants with parameter pairs \(\{a_0,a_1\}\), \(\{a_1,a_2\}\), \(\{a_3,a_4\}\), \(\{a_5,a_6\}\). These cover seven elements, repeating \(a_1\) and omitting \(a_7\). Partition the other \(q-8\) field elements arbitrarily into \((q-8)/2\) unordered pairs, each determining a two-secant. We now have exactly \(q/2\) two-secants covering all affine graph points except \(P_{a_7}\), with a single repeated affine point. Add the vertical projective line \(X=a_7Z\), which contains \(P_{a_7}\) and \(P_\infty\). This covers all \(q+1\) rational curve points with \(q/2+1\) lines, hence is optimal by Proposition 4.1, but its two-secants are not a spread. Distinct pair lines cannot coincide, because every two-secant has exactly two affine graph points.

## Verification
The standalone `verify_frobenius_spread.py` is a deterministic, dependency-free finite-field checker. It constructs \(\mathbb F_{27}\) and \(\mathbb F_{125}\) as irreducible cubic quotient rings, enumerates all maximal secant blocks, checks exact intersection sets, the unique-block-per-pair condition, point degrees, zero first moments, and both parallel and nonparallel spreads. In \(\mathbb F_8\) it enumerates every two-secant and constructs the non-spread five-line optimal cover. The universal statements above follow from the field identities and counting arguments, not the finite tests.

## Relationship to prior work
Asgarli, Dassarma, Ghioca, MacLean and Stokdyk (2026), Proposition 4.1, establish geometric irreducibility, nonreflexivity, rational point count, the bound of \(p\) points on each rational line, and the numerical optimal covering number \(q/p+1\), exhibiting one fixed-direction pencil. All of those facts are acknowledged. The present statement instead classifies the complete set of optimal covering configurations for odd \(p\), identifies the maximal-section incidence structure, exhibits exponentially many nonpencil covers, and determines the sharp failure in characteristic two.

The affine-spread notion and its general finite-geometric context are established earlier, for example in Gupta--Pavese (2024). The general near-cover phenomenon in affine geometry is classical: Blokhuis--Brouwer--Szőnyi (2009/2010), citing Jamison, gives stronger lower bounds for covering all but one affine point. In particular the odd-characteristic near-spread obstruction is related to this earlier work; the explicit first-moment argument above avoids claiming it as independently new. The novelty assessed here is the *specific full optimal-cover classification on this algebraic curve* together with its combinatorial multiplicity and sharp binary exception, not the underlying affine-spread or near-cover theorem.

## Limitations
The theorem counts a large subfamily of optimal covers but not the exact total number of affine line spreads or optimal covers; classifying spreads up to affine-group equivalence is not attempted. The odd-characteristic classification need not hold for other plane curves. The characteristic-two construction proves existence of non-spread minimizers, not their exhaustive classification. The proof is mathematical and the finite checker only supplies bounded corroboration. Historical priority of an equivalent curve-specific formulation is not independently established.

## References
1. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (9 October 2026), Section 4, Proposition 4.1, https://arxiv.org/html/2610.13042v1 .
2. S. Gupta, F. Pavese, *Affine vector space partitions and spreads of quadrics*, arXiv:2402.07882v1 (12 February 2024), Designs, Codes and Cryptography 92 (2024), https://doi.org/10.1007/s10623-024-01447-1 .
3. A. Blokhuis, A. E. Brouwer, T. Szőnyi, *Covering all points except one*, Journal of Algebraic Combinatorics 32 (2010), 59–66, https://doi.org/10.1007/s10801-009-0204-1 .
