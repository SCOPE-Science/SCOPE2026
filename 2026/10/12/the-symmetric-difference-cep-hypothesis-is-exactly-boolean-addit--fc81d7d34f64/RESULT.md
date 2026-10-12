# The symmetric-difference CEP hypothesis is exactly Boolean additivity

## Finding

**Theorem.** Let \(B\) be any Boolean algebra, including the one-element algebra, and let \(f:B\to B\) be arbitrary. Write \(x\triangle y=(x\wedge\neg y)\vee(y\wedge\neg x)\). The following are equivalent:

1. For all \(x,y,z\in B\), \(x\triangle y\le z\) implies \(f(x)\triangle f(y)\le f(z)\).
2. For all \(x,y\in B\), \(f(x\vee y)=f(x)\vee f(y)\).

The second property is **additivity** as defined by Gyenis, Molnár and Öztürk [1]. These equivalent conditions need not entail normality \(f(0)=0\). For \(B=\mathcal P(\{1,\ldots,n\})\), with any integer \(n\ge1\), precisely \((2^n+1)^n\) maps satisfy either property.

**Concrete correction.** The operator in [1, Example 2.2], \(f(\{1,3\})=\{1,2,3\}\) and \(f(X)=X\) for all other subsets, violates property 1. Take \(x=\{1,3\}\), \(y=\{1\}\), \(z=\{3\}\). Then \(x\triangle y=z\), but \(f(x)\triangle f(y)=\{2,3\}\not\subseteq f(z)=\{3\}\). Thus the proposed strict weakening in [1, Section 2] is not established by this condition, regardless of whether the particular algebra has the congruence extension property (CEP) for another reason.

## Assumptions and scope

No finiteness, atomicity, normality, or preservation of \(0\) is assumed for the structural equivalence. The count concerns all set-theoretic unary maps of the Boolean algebra with \(n\ge1\) labelled atoms, not maps modulo isomorphism or term-equivalence. The displayed witness concerns exactly the operator written in [1, Example 2.2], not other constructions or the paper's later non-additivity results. The constant map \(f(x)=1\) demonstrates the lack of a normality implication when \(B\) is nontrivial.

## Proof

Suppose property 1. If \(a\le b\), then \(a\triangle b=b\wedge\neg a\le b\). Hence \(f(a)\triangle f(b)\le f(b)\). For arbitrary Boolean elements \(u,v\), \(u\triangle v\le v\) forces \(u\le v\). Therefore \(f(a)\le f(b)\): the map \(f\) is order-preserving.

Let \(u=x\vee y\). Since \(u\triangle x=y\wedge\neg x\le y\), property 1 gives \(f(u)\triangle f(x)\le f(y)\). Monotonicity gives \(f(x)\le f(u)\), so \(f(u)\triangle f(x)=f(u)\wedge\neg f(x)\). Thus \(f(u)\wedge\neg f(x)\le f(y)\), equivalently \(f(u)\le f(x)\vee f(y)\). The reverse inequality follows from monotonicity. Hence \(f\) preserves binary joins.

Conversely, suppose that \(f\) preserves binary joins; then \(f\) is monotone. For \(x,y\in B\), put \(p=x\wedge\neg y\), \(q=y\wedge\neg x\), and \(r=x\wedge y\). We have \(x=p\vee r\), \(y=q\vee r\), and \(x\triangle y=p\vee q\). The Boolean identity \((a\vee c)\triangle(b\vee c)\le a\vee b\), applied with \(a=f(p)\), \(b=f(q)\), \(c=f(r)\), yields

\[
f(x)\triangle f(y)\le f(p)\vee f(q)=f(x\triangle y).
\]

Whenever \(x\triangle y\le z\), monotonicity yields \(f(x\triangle y)\le f(z)\). This proves property 1.

For the finite count, fix an output atom \(j\) of \(\mathcal P(\{1,\ldots,n\})\). Its membership in \(f(X)\) is a join-preserving Boolean-valued function \(h_j(X)\). If \(h_j(\varnothing)=1\), it is identically one. Otherwise it is uniquely determined by its \(n\) binary values on the singleton inputs, with no restrictions, giving \(2^n\) possibilities. The \(n\) output atoms can be chosen independently, hence \((2^n+1)^n\). The witness failure follows from the explicit set calculation above. \(\square\)

## Verification

Run the included standalone Python 3 program `verify.py` with `python3 verify.py`. It enumerates every unary operator on Boolean algebras with one and two atoms, then every monotone unary operator on the three-atom Boolean algebra, independently compares both conditions, checks the exact counts, and evaluates the published witness. Its output ends with `VERIFY_OK`; checks give counts \(3\), \(25\), and \(729\) for one, two, and three atoms respectively. The finite experiments do not establish the arbitrary-Boolean-algebra theorem; its universal proof is the preceding Boolean-algebra argument. The three-atom enumeration is exhaustive within monotone maps, a complete test domain for property 1 by the first proof step.

## Relationship to prior work

Gyenis, Molnár and Öztürk [1, Section 1] explicitly distinguish additivity (preservation of binary joins) from normality (preservation of zero). Their Fact 2.1 gives the displayed symmetric-difference quasi-identity as a sufficient condition for CEP. Their Section 2 describes it as strictly weaker than additivity and asserts that the non-additive operator in Example 2.2 satisfies it. The theorem here establishes an equivalence with their additivity condition, and the displayed triple directly contradicts the Example 2.2 membership assertion. These observations do not contest that additive maps have CEP and do not decide CEP for the Example 2.2 algebra by any other method.

Related discussions of CEP for arbitrary unary expansions [2] provide context; no claim of a new criterion for CEP is made. The structural equivalence could also be expressible as a general Boolean-algebra identity in older universal-algebra literature; identifying every such equivalent historical formulation requires further scrutiny.

## Limitations

This result corrects only the claimed gap between a specific quasi-identity and additivity, and the asserted example satisfying it. It does **not** disprove the CEP of that example, the existence of strongly non-additive CEP varieties, or the remaining constructions in [1]. The finite enumeration formula counts functions on labelled powerset Boolean algebras, not all term-equivalence classes. Independent scholarly review has not been performed.

## References

[1] Z. Gyenis, Z. Molnár, Ö. Öztürk, *More on modal logics and deduction*, arXiv:2603.17724v1 (18 March 2026), Sections 1–2, especially Fact 2.1 and Example 2.2. https://arxiv.org/html/2603.17724v1

[2] Z. Gyenis and Z. Molnár, *Varieties of modal algebras without congruence extension property*, arXiv:2402.07293 (2024), background on the relationship between CEP and Boolean expansions. https://arxiv.org/abs/2402.07293
