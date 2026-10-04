# Endpoint obstruction to the proposed Lagrange-constant phase transition
## Finding
For the substitutions \\(\\phi_{a,b}:0\\mapsto aa,\\ 1\\mapsto bb\\) and the rational mechanical words used in Yasutomi's arXiv:2609.32450v1, the endpoint pair \\((0,1)\\) is explicitly classified as type (1). Nevertheless, for every pair of positive integers \\(a<b\\),
\[
\\mathcal L([\\phi_{a,b}(G(0))])=\\sqrt{a^2+4}
<\\sqrt{b^2+4}
=\\mathcal L([\\phi_{a,b}(G(1))]).
\]
Therefore, whenever \\(a\\ge2\\) and \\(b\\ge a^2+2\\), this endpoint pair contradicts Conjecture 5.1(II)(1), which predicts the reverse inequality for every type-(1) pair. In particular, the proposed global type-(1) phase reversal at \\(b=a^2+2\\) is false on the conjecture's stated closed rational domain.

## Assumptions and scope
Let \\(a,b\\) be positive integers with \\(a<b\\). For rational \\(x\\in[0,1]\\), define the mechanical word by
\[
G(x,n)=\\lfloor nx\\rfloor-\\lfloor(n-1)x\\rfloor,
\]
and let \\(\\phi_{a,b}\\) replace every \\(0\\) by the two-letter block \\(aa\\) and every \\(1\\) by \\(bb\\). The Lagrange constant \\(\\mathcal L\\) is the standard continued-fraction Lagrange constant used in the source.

The claim concerns only the endpoint pair \\((x,y)=(0,1)\\). It does not decide the proposed phase-transition behavior for interior type-(1) pairs, nor does it challenge the proved \\(b=a+1\\) ordering theorem in the preprint.

## Proof
For every integer \\(n\\),
\[
G(0,n)=0,\\qquad G(1,n)=1.
\]
Hence \\(\\phi_{a,b}(G(0))\\) is the constant continued-fraction word with partial quotient \\(a\\), while \\(\\phi_{a,b}(G(1))\\) is the constant word with partial quotient \\(b\\).

For a positive integer \\(c\\), put \\(r_c=[0;\\overline c]\\). Then \\(r_c=1/(c+r_c)\\), so
\[
r_c=\\frac{\\sqrt{c^2+4}-c}{2}.
\]
For a constant continued fraction, the two tails entering the Perron expression for the Lagrange constant are both \\(r_c\\); equivalently, this is the endpoint specialization of the source's Theorem 3.5 and its definition of \\(L(x,1)\\). Thus
\[
\\mathcal L([0;\\overline c])=c+2r_c=\\sqrt{c^2+4}.
\]
Applying this with \\(c=a\\) and \\(c=b\\) gives the two exact endpoint values. Since \\(a<b\\), we have \\(a^2+4<b^2+4\\), and therefore
\[
\\sqrt{a^2+4}<\\sqrt{b^2+4}.
\]

The source's Lemma 1.4 declares \\((0,1)\\) to be type (1). Its Conjecture 5.1(II)(1) asserts that, for \\(a\\ge2\\) and \\(b\\ge a^2+2\\), every type-(1) pair \\(x<y\\) should instead satisfy \\(\\mathcal L([\\phi_{a,b}(G(x))])>\\mathcal L([\\phi_{a,b}(G(y))])\\). The endpoint inequality proved above has the opposite sign for every such \\(a,b\\), which completes the counterexample family.

## Verification
The proof is symbolic and does not depend on finite computation. The included `verify.py` independently checks the constant mechanical words and the exact squared inequality over \\(11{,}960\\) parameter pairs with \\(2\\le a\\le300\\) and forty consecutive values of \\(b\\) beginning at \\(a^2+2\\). It also records the smallest boundary witness \\((a,b)=(2,6)\\), for which the two values are \\(\\sqrt8\\) and \\(\\sqrt40\\). Its recorded output is:

`VERIFY_OK constant_words=401 parameter_cases=11960 witness_a=2 witness_b=6 L0=2.8284271247461900976033774484193961571393437507538961463533594759814649569242141 L1=6.3245553203367586639977870888654370674391102786504336537150097055851888772784764`

The finite replay is corroborative only; the infinite family follows from the exact formula above.

## Relationship to prior work
Yasutomi's preprint defines the three pair types, with \\((0,1)\\) singled out inside type (1), proves the \\(b=a+1\\) ordering theorem, and then proposes Conjecture 5.1 for arbitrary \\(b>a\\). In the conjectural regime \\(b\\ge a^2+2\\), part (II)(1) reverses the type-(1) inequality and states it for all rational \\(x<y\\) in the closed interval. The endpoint formulas above show that this universal quantifier cannot include \\((0,1)\\).

Targeted searches of published-finding corpus for the title, Conjecture 5.1, the endpoint pair, the constant continued-fraction formula, and the proposed threshold found no published finding giving this correction. Web searches for the title together with “counterexample,” “Conjecture 5.1,” and the threshold likewise returned the source itself but no correction. The closest published-finding corpus hits concerned unrelated conjecture counterexamples or unrelated phase-boundary problems.

## Limitations
This result is an endpoint obstruction. It does not determine whether an appropriately restricted conjecture for \\(0<x<y<1\\) is true, does not identify the correct interior transition threshold, and does not address type (2) or type (3) beyond noting that they are separate clauses. A later revision of the source could remove or amend the endpoint from Conjecture 5.1; the comparison here is specifically with arXiv:2609.32450v1, first public on 2026-09-26.

## References
1. Shin-ichi Yasutomi, “On the Ordering and Injectivity of Lagrange Constants Associated with Certain Substitutions,” arXiv:2609.32450v1, 2026. In particular: Lemma 1.4, Theorem 3.5, and Conjecture 5.1.
