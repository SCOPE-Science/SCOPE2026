# A proper-class obstruction to the Zorn proof of pseudo-to-approximate amenability

## Main finding

Ghahramani, Soroushmehr and Zhang, arXiv:2609.17428v1, claim that every pseudo-amenable Banach algebra with a bounded approximate identity is approximately amenable. Their proof fixes a bound \(d\geq 1\), forms the collection \(\Sigma_d\) of isometric-isomorphism types of pseudo-amenable Banach algebras with a bounded approximate identity of bound at most \(d\) that are not approximately amenable, orders it by adjoining \(c_0\)-summands, proves that chains have upper bounds, applies Zorn's lemma, and then contradicts maximality by adjoining a sufficiently large \(c_0(I)\).

There is a foundational obstruction to this argument. In ordinary ZFC, under the contradiction hypothesis \(\Sigma_d\neq\varnothing\), the paper's own closure properties imply that the counterexample types occur in arbitrarily large cardinalities. Hence they cannot form a set-sized collection of representatives, and in fact every counterexample type has a strict successor for the paper's order. Ordinary Zorn's lemma therefore cannot be applied to the announced global collection.

More precisely:

**Theorem.** Fix \(d\geq 1\). Assume there exists a pseudo-amenable Banach algebra \(A\) with a bounded approximate identity of bound at most \(d\) that is not approximately amenable. Then:

1. for every cardinal \(\theta\), there exists such an algebra \(B\) with \(|B|>\theta\);
2. for the order \(\preceq\) used in arXiv:2609.17428v1, every \([A]\in\Sigma_d\) has a strict successor \([B]\in\Sigma_d\);
3. consequently there is no set of Banach algebras containing one representative of every isometric-isomorphism type in \(\Sigma_d\), and \(\Sigma_d\) cannot be the set-valued poset required by the ordinary form of Zorn's lemma.

Thus the Zorn step in Proposition 1 of arXiv:2609.17428v1 does not establish the claimed implication in standard ZFC. This does **not** show that the implication is false; it shows that a different proof, or a fully specified foundational reformulation with the necessary closure properties, is still required.

## Proof

The proof uses only closure and cardinality facts already used in arXiv:2609.17428v1.

Let \([A]\in\Sigma_d\), and write \(\kappa=|A|\). Choose a set \(I\) with
\[
|I|>\kappa .
\]
For example one may take \(|I|=2^\kappa\). Put
\[
J=c_0(I)
\]
with pointwise multiplication. The source paper itself uses this construction: \(J\) is pseudo-amenable and has a bounded approximate identity of bound \(1\leq d\). Its closure assertion also gives
\[
B=A\oplus^0 J\in\Sigma_d .
\]

The underlying set of \(J\) contains the coordinate vectors \((e_i)_{i\in I}\), hence
\[
|J|\geq |I|>\kappa.
\]
Therefore
\[
|B|\geq |J|>|A|.
\]
In particular \(A\) and \(B\) cannot be isometrically isomorphic.

Now compare this with the order in the source. Its first condition for \([A]\preceq[B]\) is satisfied because \(B\cong A\oplus^0 J\) with \([J]\) in the pseudo-amenable bounded-approximate-identity class. Its second condition excludes a reverse decomposition
\[
A\cong B\oplus^0 J'
\]
unless the two types are already equal. Such a reverse decomposition is impossible here for every \(J'\), since it would imply
\[
|A|=|B\oplus^0J'|\geq |B|>|A|.
\]
Hence
\[
[A]\prec[B].
\]
Thus every element of the purported counterexample poset has a strict successor.

The same construction proves unbounded cardinality. Given an arbitrary cardinal \(\theta\), choose
\[
|I|>\max\{\theta,|A|\}.
\]
Then the corresponding \(B=A\oplus^0 c_0(I)\) lies in \(\Sigma_d\) and has \(|B|>\theta\).

If there were a set \(\mathcal S\) of Banach algebras containing one representative of every isometric-isomorphism type in \(\Sigma_d\), then the set of cardinals
\[
\{|C|:C\in\mathcal S\}
\]
would have a cardinal upper bound. The preceding paragraph produces a counterexample type above that bound, a contradiction. Therefore no set-sized skeleton of all types in \(\Sigma_d\) exists under the hypothesis \(\Sigma_d\neq\varnothing\).

This is exactly where the use of Zorn's lemma breaks. The source's upper-bound construction forms a \(c_0\)-direct sum over a chain indexed by a set. Such an argument shows at most that every **set-sized** chain has an upper bound. For a proper-class collection this is not enough to force a maximal element. The class of all ordinals, for instance, has an upper bound for every set-sized chain but has no maximal ordinal.

The paper's final cardinal enlargement is therefore not a contradiction to the existence of a counterexample. Under the contradiction hypothesis it instead proves directly that there is always a larger counterexample type.

## A reusable closure principle

The same obstruction is not specific to amenability.

Suppose a class of Banach algebras \(\mathcal P\) is stable under \(c_0\)-direct sums, every \(c_0(I)\) belongs to \(\mathcal P\), and a subclass \(\mathcal C\subseteq\mathcal P\) has the property that
\[
A\in\mathcal C,\quad J\in\mathcal P
\quad\Longrightarrow\quad
A\oplus^0J\in\mathcal C.
\]
If \(\mathcal C\neq\varnothing\), then \(\mathcal C\) contains algebras of arbitrarily large cardinality. Any maximality proof that first treats all isomorphism types in \(\mathcal C\) as a set must therefore impose and justify an additional size restriction; a global Zorn argument cannot use the unrestricted class together with closure under arbitrary \(c_0(I)\).

## Relation to the source claim

The source explicitly starts from the class of all Banach algebras and then refers to its quotient by isometric isomorphism as though the resulting counterexample collection were a set. Merely passing to isomorphism types does not resolve the size issue. Even if the quotient notation is repaired by choosing representatives or codes, the theorem above shows that no set-sized skeleton can contain all counterexample types if one counterexample exists.

A Grothendieck-universe convention also does not automatically validate the printed proof. Once one restricts the objects to a fixed universe, one must recheck the upper-bound assertion for every chain in the resulting set-valued poset; a chain as large as the universe-boundary collection need not have a direct sum that remains in the restricted universe. No such restriction or closure verification appears in v1.

## Literature context and originality boundary

The 2026 preprint presents its proposition as closing the gap in the 2007 pseudo-amenability paper. A recent 2026 thesis likewise records, before this preprint, that whether pseudo-amenability plus a bounded approximate identity implies approximate amenability was still open and that the earlier proof had a gap.

The set/class distinction, Cantor's theorem, and the limitation of ordinary Zorn's lemma are standard foundational facts and are not claimed as new. The contribution here is the observation that the **same \(c_0(I)\) cardinal-enlargement mechanism used in the new preprint forces its counterexample collection to be proper-class-sized under the contradiction hypothesis**, so the Zorn step cannot be used to obtain the maximal element that the remainder of the proof contradicts.

Searches by the exact preprint identifier and title, together with terms including `Zorn`, `proper class`, `cardinality`, `correction`, `gap`, `pseudo-amenability`, and `approximate amenability`, did not locate a public correction or an earlier statement of this obstruction. Originality is therefore asserted only to the best of our knowledge.

## Limitations

- This result does not construct a pseudo-amenable Banach algebra with a bounded approximate identity that fails approximate amenability.
- It does not prove or disprove the implication claimed in arXiv:2609.17428v1.
- It audits the Zorn/cardinality argument in v1; an unrelated proof of the implication could still exist.
- No claim is made that a particular alternative foundational framework cannot support a reformulated argument. Such a reformulation would have to specify its universe or class theory and verify the required chain-closure and absoluteness properties.
- Very recent comments, revisions, or differently worded discussions may not yet be indexed.

## References

1. F. Ghahramani, M. Soroushmehr and Y. Zhang, *Equivalence of Pseudo- and Approximate Amenability in Banach Algebras*, arXiv:2609.17428v1 (2026). https://arxiv.org/abs/2609.17428
2. Y. Zhang, *Approximate amenability and pseudo-amenability in Banach algebras*, Annals of Mathematical Sciences and Applications 8 (2023), no. 2, 309–320. DOI: 10.4310/AMSA.2023.v8.n2.a6.
3. *Boundedly Pseudo-Amenable and Boundedly Approximately Amenable Banach Algebras*, University of Manitoba thesis (2026), discussion of the bounded-approximate-identity gap. https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/7a8fcada-f419-4c35-8674-53d85d9c112d/content
