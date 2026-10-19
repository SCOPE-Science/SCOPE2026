# Native commutation spreads fail to recover isotopy in generalized twisted fields

## Finding

Fix a prime power \(q>2\), an integer \(n\ge3\), distinct integers \(1\le r,s<n\), and a coefficient \(c\in K^\times\), where \(K=\mathbb F_{q^n}\), such that \(N_{K/\mathbb F_q}(c)\ne1\). Give the additive group of \(K\) the bilinear multiplication
\[
x\star y=xy-cx^{q^r}y^{q^s}.
\]
Put \(g=\gcd(n,r-s)\), \(H=\mathbb F_{q^g}\), \(Q=q^n\), and \(h=q^g\). For any \(x,y\in K\),
\[
x\star y=y\star x\quad\Longleftrightarrow\quad x=0\ \text{or}\ y/x\in H.
\]
Thus for each nonzero \(x\), the native commuting centralizer is exactly the additive \(\mathbb F_q\)-subspace \(xH\) of cardinality \(h\). The maximal additive subspaces of pairwise commuting elements are precisely the lines \(xH\). The graph on nonzero elements, with distinct commuting pairs adjacent, is the disjoint union of \(\frac{Q-1}{h-1}\) cliques of size \(h-1\).

For every integer \(t\ge1\), the number of ordered pairwise-commuting \(t\)-tuples (including zero entries and repetitions) is
\[
C_t=1+\frac{Q-1}{h-1}(h^t-1).
\]
In particular the entire native commutation hierarchy, together with the literal commutation relation on the common underlying set \(K\), depends on \(r,s\) only through \(\gcd(n,r-s)\) and is independent of admissible \(c\).

This hierarchy fails to determine isotopy classes. Fix any \(q>2\), any \(c\in\mathbb F_{q^6}^\times\) with nonunit norm to \(\mathbb F_q\), and compare the products having \((r,s)=(1,5)\) and \((r,s)=(2,4)\). They both have \(g=2\), hence the same actual commuting pairs, the same spreads, and the same \(C_t\) for every \(t\). But their unital Albert normalization yields division algebras whose left and right nuclei have orders \(q\) and \(q^2\), respectively. Nucleus orders are preserved by isotopy of division algebras. Hence the two presemifields are nonisotopic despite their identical native commutation relations.

## Assumptions and scope

The product is Albert's **nonunital** binomial presemifield multiplication, not the normalized unital division-algebra product. All counts are labeled on the original additive underlying set, and tuples are required to commute pairwise under that exact multiplication. The field \(H\) is the fixed field of the automorphism \(z\mapsto z^{q^{r-s}}\) (exponents interpreted modulo \(n\)). The coefficient condition is sufficient for no nonzero zero divisors; the result is not asserted for \(N(c)=1\).

## Proof

**No zero divisors.** If nonzero \(x,y\) gave \(x\star y=0\), then
\[
c=x^{1-q^r}y^{1-q^s}.
\]
Every factor on the right has norm one from \(K\) to \(\mathbb F_q\). This contradicts \(N(c)\ne1\). Bilinearity over \(\mathbb F_q\) follows from the Frobenius maps. Thus the product defines a finite presemifield.

**Commuting equivalence.** If \(x\ne0\), write \(y=xt\). The ordinary field-multiplication terms cancel in \(x\star y-y\star x\); division by the nonzero factor \(c x^{q^r+q^s}\) leaves
\[
t^{q^r}=t^{q^s}.
\]
The solutions are exactly the fixed field of \(\mathrm{Frob}_q^{r-s}\), namely \(H=\mathbb F_{q^{\gcd(n,r-s)}}\), including \(t=0\). For \(x=0\) the two products are zero. This proves the full equivalence, all boundary cases, and the centralizer formula.

**Spread and enumeration.** Every nonzero commuting pair belongs to the same multiplicative \(H\)-line. The \(H\)-lines partition \(K^\times\) into \(L=(Q-1)/(h-1)\) disjoint sets, each having \(h-1\) nonzero elements. Each \(H\)-line is an additive pairwise-commuting subspace because the displayed criterion applies to all its points. Conversely, any additive commuting subspace containing nonzero \(x\) lies in \(xH\), proving maximality and uniqueness. A tuple other than the all-zero tuple occupies a unique \(H\)-line (identified by any nonzero entry). Each line supports \(h^t-1\) such tuples, proving \(C_t=1+L(h^t-1)\) for every \(t\ge1\).

**Nonisotopic identical-commutation pair.** In degree \(n=6\), the exponent differences for \((1,5)\) and \((2,4)\) have the same gcd \(2\) with \(6\), so their commuting relation is identical on \(K\) for any choices of admissible coefficients, in particular the same \(c\). Albert [1, Theorem 1] proves that the normalized unital generalized twisted field has right nucleus isomorphic to the fixed field of the automorphism used on the second factor, and left nucleus isomorphic to the fixed field of the automorphism used on the first factor (the notation of [1] reverses the exponent labels). Hence both nucleus orders are \(q\) for the pair \((1,5)\) and \(q^2\) for \((2,4)\). Albert also states and invokes isotopy invariance of these nucleus isomorphism types. The two normalized division algebras are not isotopic. Since normalization is an isotopy from each displayed presemifield, the original two presemifields are not isotopic either.

## Verification

The accompanying standalone `verify_semifield.py` uses finite polynomial arithmetic and direct native products (no algebra or finite-field packages). The complete nonzero-product and commuting-pair relations are checked for field orders \(27,125,81\); the three-entry tuple formula is checked exhaustively for field order \(27\). Larger order \(729\) tests check the relevant commutation conditions for forty explicitly chosen first coordinates against every possible second coordinate and independently compare both example exponent pairs. Computation checks finitely many cases; the arbitrary-parameter theorem follows from the algebraic argument above and Albert's nucleus theorem, not from extrapolation.

To replay: `python3 verify_semifield.py`. A successful run ends in `VERIFY_OK_TWISTED_FIELDS`.

## Relationship to prior work

Albert [1] defines these binomial products, proves the nucleus theorem used to distinguish isotopy classes, and studies commutativity of the **normalized unital division algebras**. That is a distinct operation from native pairwise commutation in the displayed nonunital product. The definition, no-zero-divisor criterion, and nucleus calculations belong to [1], not to the present finding. Sheekey [2, §§1.2–1.3, 1.6] documents the correspondence between isotopy classes of presemifields and rank-metric spread sets and surveys generalized twisted fields, without in the inspected text supplying the native all-arity commuting-tuple spectrum or the same-relation/nonisotopic pair.

The contribution assessed here is the explicit native commuting-line geometry, its exact all-arity count, and the consequent failure of native commutation (even as a literal relation on one underlying set) to reconstruct isotopy classes. The elementary cancellation lemma is proved above rather than claimed as a new general algebraic technique.

## Limitations

The theorem is restricted to these nonunital binomial products, to \(q>2\), and to the norm-exclusion regime. Their normalized unital isotopes need not have the same pairwise commutation relations, and no claim is made that native commutation is isotopy invariant. This does not classify all semifields, general presemifields, or the automorphism groups of the commuting graphs. A mathematically equivalent native commutation calculation under other terminology may have appeared previously; published priority beyond the inspected sources remains subject to independent literature review.

## References

[1] A. A. Albert, *Generalized twisted fields*, Pacific Journal of Mathematics **11** (1961), 1–8, especially Theorem 1 and §§1, 3, 4. https://msp.org/pjm/1961/11-1/pjm-v11-n1-p01-p.pdf (journal dated November 1961; an exact earliest public day was not established).

[2] J. Sheekey, *A new family of linear maximum rank distance codes*, arXiv:1504.01581, first preprint publicly posted 7 April 2015; see §§1.2–1.3 and 1.6. https://arxiv.org/abs/1504.01581
