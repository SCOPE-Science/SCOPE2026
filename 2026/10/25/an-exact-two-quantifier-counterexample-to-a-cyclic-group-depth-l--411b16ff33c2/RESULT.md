# An exact two-quantifier counterexample to a cyclic-group depth lower bound

## Finding

Write \(C_t=(\mathbb Z/t\mathbb Z,+)\). In the first-order language \(L=\{R,e,=\}\), with \(R(a,b,c)\) interpreted as \(a+b=c\) and \(e\) as zero, the following holds **for every integer \(k\ge2\)**:

\[
\min\{\operatorname{qr}(\varphi): C_5\models\varphi\ \Longleftrightarrow\ C_{5^k}\not\models\varphi\}=2.
\]

More precisely, the single sentence

\[
\theta:=\exists x\,\exists y\,\bigl(x\ne e\wedge y\ne e\wedge x\ne y\wedge\neg R(x,x,y)\wedge\neg R(y,y,x)\wedge\neg R(x,y,e)\bigr)
\]

is false in \(C_5\) and true in each \(C_{5^k}\) for \(k\ge2\). It has quantifier rank two and uses exactly two bound variables.

Gomaa's quantitative lower bound for finite cyclic groups states that if \(f\) is the least divisor belonging to exactly one of the two group orders, and \(2^n\le f<2^{n+1}\), every distinguishing sentence has rank at least \(n\). Here \(f=25\) and \(n=4\); therefore the displayed rank-two sentence is an explicit counterexample to that **numerical** bound in the stated relational group language.

## Assumptions and scope

The structures are the finite additive cyclic groups \(C_5\) and \(C_{5^k}\) for arbitrary integers \(k\ge2\). The only nonlogical group symbol is the ternary addition *relation*, not a binary function. The group identity is a named constant. No auxiliary predicates, order, parameters, or exponentiation terms are used in the sentence. Quantifier rank counts nesting of first-order quantifiers in the ordinary way; the quantifier-free matrix has rank zero.

## Proof

**Failure in the five-element group.** Fix any candidate \(x\ne0\) in \(C_5\). The six conjuncts in the matrix require \(y\) to avoid the five values

\[
0,\quad x,\quad 2x,\quad 2^{-1}x,\quad -x.
\]

Indeed these values violate, respectively, \(y\ne0\), \(x\ne y\), \(\neg R(x,x,y)\), \(\neg R(y,y,x)\), and \(\neg R(x,y,0)\). Since \(2^{-1}=3\pmod5\), these are \(0,x,2x,3x,4x\), the entire group. There is no suitable \(y\) for any nonzero \(x\); hence \(C_5\not\models\theta\).

**Uniform witnesses in every larger five-power group.** For \(k\ge2\), set \(x=5^{k-2}\) and \(y=3\cdot5^{k-2}\) in \(\mathbb Z/5^k\mathbb Z\). Both are nonzero and distinct. Moreover

\[
y-2x=x,\qquad 2y-x=5x=5^{k-1},\qquad x+y=4x.\]

Each displayed difference is nonzero modulo \(5^k\), so all negated addition predicates hold. Thus \(C_{5^k}\models\theta\) for all \(k\ge2\).

**Optimality of rank two.** In either group, the complete atomic diagram of any single variable \(z\), including terms involving the constant \(e\), is determined solely by whether \(z=e\). Indeed neither group has nonzero elements of order two; in the relational language, all atomic formulas in one free variable are equalities among \(z,e\) or instances \(R(a,b,c)\) with \(a,b,c\in\{z,e\}\). Their truth values are identical for \(z=e\) in both groups, and identical for \(z\ne e\) in both groups. Both alternatives occur. Every rank-one sentence is a Boolean combination of quantifier-free sentences and one-quantifier sentences, and therefore has the same truth value in these groups. Their least distinguishing rank is thus exactly two.

**Contradiction with the published threshold.** The divisors of \(5\) are \(\{1,5\}\). For any \(k\ge2\), the divisors of \(5^k\) are \(\{1,5,25,\ldots,5^k\}\). The smallest divisor present in exactly one divisor set is \(f=25\). The unique integer \(n\) with \(2^n\le25<2^{n+1}\) is \(n=4\). The rank-two sentence violates the asserted rank-at-least-four conclusion in the named theorem and corollary. No claim is made that the positive upper-bound construction, the distinct-prime setting, or the general asymptotic order-of-growth assertion fails.

## Verification

The included standalone file `verify_counterexample.py` evaluates the exact quantified matrix over \(C_5,C_{25},C_{125},C_{625}\). It independently enumerates all one-variable atomic types in \(L\) to check the rank-one lower bound on these examples, and verifies the explicit witnesses. Run `python3 verify_counterexample.py`; the recorded output is in `verify_output.txt`. The arbitrarily large \(k\) assertion is proved algebraically above, not inferred from finite tests.

## Relationship to prior work

The two primary sources explicitly define the same relational group language. The earliest publicly dated source located is Gomaa's 2007 thesis, which states the threshold as Theorem 3.12(1) and Corollary 3.7(1). The 2010 journal treatment states it as Theorem 6.13(1) and Corollary 6.14(1), following Theorem 6.9. The proof of the latter assumes that a shortest winning Ehrenfeucht–Fraïssé play must exhibit a distinguishing closed binder. The present two-variable counterexample is a pattern of **absent** addition relations, which need not constitute the postulated distinguishing closed binder. This pinpoints why the stated closed-binder argument does not establish a universal lower bound.

Related results on addition-chain upper bounds for **pairs of distinct prime-order groups** apply to a different class of comparisons and do not imply the present prime-versus-prime-power counterexample.

## Limitations

The result refutes the published **numerical quantifier-rank lower bound** for this infinite family only. It is not a replacement lower-bound theorem for arbitrary finite cyclic or abelian groups, and it neither refutes nor proves the separate asymptotic \(\Omega(\log f)\) statement. No independent external scientific audit has been performed. An earlier unindexed correction or equivalent observation may exist.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, doctoral dissertation, University of Maryland, publicly dated 2007-07-06, Chapter 3, Definition 3.5, Theorem 3.12 and Corollary 3.7. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; full text https://drum.lib.umd.edu/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/download
2. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI:10.1142/S0218196710006047, Theorems 6.9 and 6.13 and Corollary 6.14. https://www.researchgate.net/publication/220169697_DESCRIPTIVE_COMPLEXITY_OF_FINITE_ABELIAN_GROUPS
