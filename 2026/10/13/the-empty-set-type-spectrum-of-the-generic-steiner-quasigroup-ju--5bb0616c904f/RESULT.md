# The empty-set type spectrum of the generic Steiner quasigroup jumps to continuum at arity \(3\)

## Finding

Let \(T^*_{\mathrm{Sq}}\) be the complete model-completion theory of Steiner quasigroups in the language with one binary operation. Its complete empty-set type spectrum begins

\[
|S_0(T^*_{\mathrm{Sq}})|=1,\qquad
|S_1(T^*_{\mathrm{Sq}})|=1,\qquad
|S_2(T^*_{\mathrm{Sq}})|=2,
\]

and then jumps sharply:

\[
|S_n(T^*_{\mathrm{Sq}})|=2^{\aleph_0}\qquad(n\ge 3).
\]

In particular, arity \(3\) is the exact first arity at which \(T^*_{\mathrm{Sq}}\) witnesses failure of smallness.

## Assumptions and scope

Types are complete \(n\)-types over the empty set in the pure Steiner-quasigroup language \(\{\cdot\}\). The axioms used are

\[
x\cdot x=x,\qquad x\cdot y=y\cdot x,\qquad x\cdot(x\cdot y)=y.
\]

The result concerns \(T^*_{\mathrm{Sq}}\), the complete theory studied by Silvia Barbina and Enrique Casanovas. It does not claim an analogous spectrum for arbitrary Steiner-system theories or for expansions by extra predicates.

## Proof

Barbina and Casanovas prove that \(T^*_{\mathrm{Sq}}\) is complete and eliminates quantifiers. They also prove in Theorem 3.3 that there are \(2^{\aleph_0}\) complete types over \(\varnothing\) in three variables. Since the language is countable, this is the maximum possible cardinality, so

\[
|S_3(T^*_{\mathrm{Sq}})|=2^{\aleph_0}.
\]

For one variable, every term is provably equal to \(x\): this follows inductively from idempotence, because once two subterms reduce to \(x\), their product reduces to \(x\cdot x=x\). Quantifier elimination therefore leaves exactly one complete \(1\)-type.

For two variables, put \(z=x\cdot y\). If \(x=y\), every term reduces to that one element. If \(x\ne y\), then \(z\ne x,y\), because \(x\cdot y=x\) would imply
\[
y=x\cdot(x\cdot y)=x\cdot x=x,
\]
and similarly for \(z=y\). Moreover
\[
x\cdot z=y,\qquad y\cdot z=x,\qquad z\cdot z=z.
\]
Thus every term in \(x,y\) reduces to one of \(x,y,z\), and the entire equality diagram is forced once one knows whether \(x=y\). There are therefore exactly two quantifier-free \(2\)-types, equality and inequality. Quantifier elimination gives
\[
|S_2(T^*_{\mathrm{Sq}})|=2.
\]

Finally, for each \(n>3\), every complete \(3\)-type \(p(x_1,x_2,x_3)\) gives a complete \(n\)-type by adjoining
\[
x_4=x_1,\ldots,x_n=x_1.
\]
Distinct \(3\)-types remain distinct, so \(|S_n|\ge 2^{\aleph_0}\); countability of the language gives the reverse inequality.

## Verification

The bundled verifier exhaustively enumerates all \(3^9=19{,}683\) binary operation tables on a fixed three-element set. It confirms that exactly one table satisfies the three Steiner-quasigroup identities, and checks that one generator is closed while every two distinct generators close to all three elements with the forced multiplication rules above.

The verifier returns:

`VERIFY_OK 38 exact assertions`

The infinite \(3\)-type lower bound and quantifier elimination are source theorems rather than computational claims.

## Relationship to prior work

Barbina and Casanovas explicitly prove the continuum-sized family of complete \(3\)-types and quantifier elimination. The exact low-arity counts and the resulting all-arity spectrum above are short consequences of those results plus the elementary two-generator normal form; they were not stated in the inspected source.

Candidate-specific searches in published-finding corpus, exact web searches for Steiner-quasigroup \(1\)- and \(2\)-type counts, and searches of the cumulative research ledger found no equivalent spectrum statement. The closest same-source ledger findings concern \(k\)-closure of the automorphism group and finite partial-Steiner one-point extensions, not complete-type cardinalities. A current-week finding computes a similar type spectrum for existentially closed projective planes, but for a different theory with a different threshold.

The originality claim is therefore deliberately narrow: the contribution is the explicit sharp spectrum
\[
1,1,2,2^{\aleph_0},2^{\aleph_0},\ldots
\]
and the identification of \(3\) as the least non-small arity, not the published continuum-\(3\)-type theorem itself.

## Limitations

The derivation is short and may be known informally to specialists; unindexed folklore remains the main originality risk. The result is only an empty-set type count and does not describe the internal geometry or Borel complexity of the continuum many \(3\)-types. No independent audit has yet been performed.

## References

1. Silvia Barbina and Enrique Casanovas, “Model theory of Steiner triple systems,” arXiv:1805.06767; *Journal of Mathematical Logic* 20 (2020), 2050010, DOI 10.1142/S0219061320500105.
2. MaRDI publication record for the same article, recording MSC 03C10, 03C45, and 05B07.
