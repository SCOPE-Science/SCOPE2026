# Exact rank spectrum of derivations of a truncated polynomial algebra

## Finding

Let \(p\) be a prime, \(q=p^e\) with \(e\geq 1\), \(k=\mathbb F_q\), and \(A=k[x]/(x^m)\) for an integer \(m\geq 2\). Regard each \(k\)-linear derivation \(D\in\operatorname{Der}_k(A)\) as a \(k\)-linear endomorphism of \(A\). Put \(\epsilon=1\) when \(p\nmid m\), and \(\epsilon=0\) when \(p\mid m\). The complete rank-generating polynomial is

\[
\mathcal R_{m,q}(z)=\sum_{D\in\operatorname{Der}_k(A)}z^{\operatorname{rank}_k D}
=1+\sum_{t=1}^{m-\epsilon}(q-1)q^{t-1}z^{\,t-\lfloor t/p\rfloor}.
\]

For each integer \(t\) in the displayed range, exactly \((q-1)q^{t-1}\) derivations have rank \(t-\lfloor t/p\rfloor\); when multiple values of \(t\) give the same exponent, their multiplicities add. The constant term accounts for the zero derivation. This formula holds for every finite field and every truncation length \(m\geq2\).

## Assumptions and scope

All derivations are \(k\)-linear and satisfy the Leibniz rule. Rank is vector-space rank over \(k\), not rank over the quotient ring. The result concerns the one-variable truncated algebra \(k[x]/(x^m)\); it does not classify derivations up to conjugacy, their Jordan forms, or derivations of multivariable quotients.

## Proof

Every derivation is determined by \(f=D(x)\) and acts on representatives by \(D(g)=f g'\). The relation \(x^m=0\) imposes \(m x^{m-1}f=0\) in \(A\). Thus, if \(p\nmid m\), the constant coefficient of \(f\) must vanish; if \(p\mid m\), every \(f\in A\) is admissible.

For nonzero \(f\), let \(s\) be its order of vanishing, so \(f=x^s u\) with \(u\) a unit and \(0\leq s<m\). Let

\[
W=\operatorname{span}_k\{x^{i-1}:1\leq i\leq m-1,\ p\nmid i\}.
\]

The monomial derivative formula gives \(D(A)=fW\). Multiplication by \(f\) has kernel \((x^{m-s})\), so

\[
\operatorname{rank}_k D=\dim_k W-\dim_k\bigl(W\cap(x^{m-s})\bigr).
\]

In the monomial basis, this is the number of integers \(i\) with \(1\leq i\leq m-s\) that are not divisible by \(p\), namely \(t-\lfloor t/p\rfloor\) for \(t=m-s\). In the case \(s=0\), admissibility forces \(p\mid m\), so the endpoint \(i=m\) is divisible by \(p\) and the same formula still holds. There are \((q-1)q^{m-s-1}=(q-1)q^{t-1}\) elements of valuation \(s\). The allowed values are \(t=1,\ldots,m-1\) if \(p\nmid m\), and \(t=1,\ldots,m\) if \(p\mid m\). Adding the zero derivation proves the formula.

## Verification

The proof is symbolic and covers every prime power \(q\). The accompanying standard-library script independently constructs the matrices of all admissible derivations and checks their ranks for \(p=2\), \(m=2,\ldots,7\); \(p=3\), \(m=2,\ldots,5\); and \(p=5\), \(m=2,\ldots,4\). All 13 tested cases agree with the formula. These finite checks are sanity checks, not the proof of the universal statement.

## Relationship to prior work

Jelisiejew studies local Artinian Gorenstein algebras through automorphism-group orbits and tangent spaces, and gives explicit formulas involving derivations of power-series rings. The rank enumerator above is a different invariant: it counts all derivations of the finite quotient \(k[x]/(x^m)\) by their vector-space ranks, with the characteristic-divisibility boundary \(p\mid m\) made explicit. The inspected source does not state this rank distribution. The literature comparison is not an exhaustive proof of historical priority.

## Limitations

No classification of conjugacy orbits, Jordan partitions, or multivariable derivation ranks is claimed. The finite computations cover only the listed prime fields and lengths; all other cases rely on the proof. Independent mathematical audit has not been performed, and an unindexed source may contain an equivalent rank formula.

## References

1. J. Jelisiejew, *Classifying local Artinian Gorenstein algebras*, arXiv:1511.08007v1, first submitted 2015-11-25, especially §§2.2–2.3. https://arxiv.org/abs/1511.08007 .
