# Exact anticommuting-pair enumerator for signed partial involutions

## Finding
Let \(W_n\) denote the finite monoid of \(n\)-by-\(n\) monomial partial matrices whose nonzero entries belong to \(\{+1,-1\}\). Products are ordinary integer-matrix products, and \(0\) denotes the zero matrix. For \(n\ge0\), count ordered pairs \((A,B)\in W_n^2\) satisfying \(A^2=P_A\), \(B^2=P_B\), and \(AB=-BA\), where \(P_A,P_B\) are the diagonal partial identities on the supports of \(A,B\). Equivalently, \(A\) and \(B\) are self-inverse signed partial permutations that anticommute.

Writing \(D_A,D_B\) for their coordinate supports, the complete joint support-rank exponential generating function is
\[
\boxed{\sum_{n\ge0}\frac{z^n}{n!}\sum_{(A,B)}u^{|D_A|}v^{|D_B|}=\exp\!\left(z+2zu+z^2u^2+2zv+z^2v^2+4z^2u^2v^2+2z^4u^4v^4\right).}
\]
In particular, the exact unrefined count \(a_n\) has generating function
\[
\boxed{\sum_{n\ge0}a_n\frac{z^n}{n!}=\exp(5z+6z^2+2z^4).}
\]
The first six values, for \(n=0,\ldots,5\), are \(1,5,37,305,2905,30125\). All pairs admit a unique decomposition into five kinds of singleton components, four kinds of signed two-point components, and one four-point component (counting component types up to signed conjugacy). On every common-support component, the support has size two or four. Consequently an anticommuting pair of **full** signed involution matrices exists only in even dimensions, with support components of size two and four.

## Assumptions and scope
The signs are the integers \(\pm1\), and equality \(AB=-BA\) is equality of ordinary integer matrices (or over any coefficient field with characteristic different from two). No arbitrary field scalars are permitted as entries. The zero map is included. A signed partial involution has identical domain and image support, and its square is the partial identity; it need not be fixed-point-free. The pairs are ordered and need not have the same domain. The variables \(u,v\) mark the individual domain cardinalities, not the rank of the matrix products. The case \(n=0\) contains the unique pair of empty matrices.

## Proof
**Support decomposition.** From \(AB=-BA\) and \(A^2=P_A\), \(B^2=P_B\), we deduce \(AP_B=P_BA\) and \(BP_A=P_AB\) by multiplying the anticommutation identity once more. Thus each signed permutation preserves the support of the other and its complement. Every pair decomposes uniquely into the four invariant coordinate types: neither defined, only \(A\) defined, only \(B\) defined, or both defined. The first yields isolated zero coordinates and contributes \(\exp(z)\).

**One active signed involution.** On an \(A\)-only block, \(A\) is an ordinary signed permutation with \(A^2=I\). Its permutation cycles are either fixed points or transpositions. A fixed point has two sign choices. On a transposition, the two signs must agree, giving two signed permutations on any prescribed pair. Hence its labeled component exponential is \(\exp(2zu+z^2u^2)\). The \(B\)-only factor is \(\exp(2zv+z^2v^2)\).

**Both active, unsigned permutations.** On the common-support block the underlying unsigned permutations \(\sigma_A,\sigma_B\) commute, since changing the sign of a monomial matrix does not change its nonzero entry positions. Both are involutions, so their action on a transitive orbit factors through \((C_2)^2\). A transitive orbit has size one, two or four. Size one is impossible because two nonzero signed scalars commute. On a two-point orbit, both underlying permutations cannot be the nontrivial swap: otherwise \(AB\) is diagonal with entries \(\pm1\), forcing \((AB)^2=I\), while anticommutation and the involution conditions force \((AB)^2=-I\). Hence exactly one of \(\sigma_A,\sigma_B\) swaps the two coordinates and the other fixes them. There are two such types. In each type, the diagonal involution has opposite signs at the two points, and the swapping involution has equal signs on its two arrows. For any specified labeled pair this gives \(2\cdot2=4\) matrix pairs per type; the combined labeled exponential contribution is \(2(4/2!)z^2u^2v^2=4z^2u^2v^2\).

A four-point orbit is regular under the two underlying involutions. On a specified labeled four-set, there are \(4!/4=6\) regular actions of \((C_2)^2\) with the generators distinguished. Each generator has two transposition orbits, hence initially four sign choices; together there are \(2^4=16\) sign choices. The relation \(AB=-BA\) imposes one independent sign equation around the unique square orbit, leaving exactly \(8\) choices. Thus there are \(6\cdot8=48\) valid signed actions on a given four-set, contributing \(48/4!=2\) times \(z^4u^4v^4\) to the connected labeled series.

**Assembly and boundary conditions.** There are no larger transitive underlying orbits and all components are independent; the labeled exponential formula multiplies their factors. Summing the displayed exponent contributions gives the multivariate theorem. The specialization \(u=v=1\) gives \(\exp(5z+6z^2+2z^4)\). The same bijection handles every \(n\ge0\), including the empty case and overlap ranks zero. If both matrices have full support, the singleton and one-active blocks vanish and all remaining blocks have even size, proving the parity consequence.

## Verification
`verify.py` constructs every signed partial monomial matrix with square equal to its support projection, calculates signed matrix products directly, tests \(AB=-BA\), and compares the exhaustive counts against independently evaluated exponential-series coefficients for every \(n\in\{0,1,2,3,4,5\}\). The output is `VERIFY_OK` after the six successful cases. Counts are corroborative only: the proof for unbounded \(n\) is the transitive block classification and labeled-set assembly above.

## Relationship to prior work
Elliott, Levine, and Mitchell (2023) investigate enumerations in ordinary finite symmetric inverse monoids, including monogenic inverse submonoids. Araújo, Bentz, and Konieczny (2012) study the ordinary commutation relation in symmetric inverse semigroups. The signed rook monoid is a standard \(C_2\)-wreath-product variant of the rook monoid. The present problem uses *anticommutation* rather than commutation and has a nontrivial signed Clifford-type obstruction; the ordinary commuting-action formulas do not imply the size-two/four signed block classification. General representation theory of Clifford algebras motivates the even-dimensional obstruction, but does not by itself supply the exact labeled signed-partial-matrix enumerator.

## Limitations
This result concerns signs \(\pm1\) and literal anticommutation over a coefficient ring where \(1\ne-1\). Over characteristic two the relation becomes ordinary commutation and the formulas need not apply. It does not classify general monomial matrices with arbitrary nonzero field entries or more than two anticommuting generators. The exponential formula is standard, while the signed block classification and resulting exact polynomial are the assessed contribution. Publication-priority risks include broader signed-rook or monomial Clifford module classifications whose exact enumerative consequences may not be explicit in search results.

## References
1. L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387v1, first posted 2023-03-22, https://arxiv.org/abs/2303.12387 .
2. J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664 (2012), https://arxiv.org/abs/1205.1664 .
3. T. Halverson, M. Reeks, *Gelfand Models for Diagram Algebras*, arXiv:1302.6150 (2013), https://arxiv.org/abs/1302.6150 .
