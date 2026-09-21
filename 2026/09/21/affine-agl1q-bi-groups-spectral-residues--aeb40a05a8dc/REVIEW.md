# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For a connected Cayley graph on a group having exactly \(d\) linear
characters and one nonlinear character of degree \(d\), every nonlinear-block
eigenvalue contributes to the regular adjacency spectrum with multiplicity divisible
by \(d\). If \(m(\alpha)\) is a spectral multiplicity and \(\ell(\alpha)\) counts
linear characters having sum \(\alpha\), then
\(m(\alpha)\equiv\ell(\alpha)\pmod d\). The only possible ambiguity is
\(\ell(\alpha)=d\); this would force all linear character sums, including the
principal one, to equal \(|S|\), contradicting simplicity of the top eigenvalue in a
connected regular graph. Hence the spectrum recovers the complete multiset of linear
character sums. The zero-trace identity for a loopless Cayley adjacency matrix then
forces
\[
\chi(S)=-d^{-1}\sum_{\lambda(1)=1}\lambda(S),
\]
so the singleton nonlinear character-sum set is recovered too. The published
connected-complement reduction then extends this to the BI-group property.

The Frobenius corollary was checked against Seitz's classification. In that branch,
the cyclic complement has order \(|G'|-1\), the number of linear characters is the
complement order, and the character-degree sum-of-squares identity makes the unique
nonlinear degree equal to the same number. The non-CI corollary uses the standard
Sylow restriction for CI-groups: a cyclic Sylow \(5\)-subgroup of order at least 25
is forbidden.

Stress tests against the known small cases agree with the literature:
\(\operatorname{AGL}(1,3)\cong S_3\), \(\operatorname{AGL}(1,4)\cong A_4\),
and the order-20 and order-42 groups handled explicitly in the 2019 paper all fall
under the theorem.

## Originality

**PASS, to the best of our knowledge.** The 2015 paper leaves classification of
BI-groups as an open direction. The full 2019 Abdollahi--Zallaghi paper was inspected:
it proves the BI property for the order-20 and order-42 Frobenius groups by separate,
explicit character-table and spectral multiplicity case analyses, and gives a
classification only through order 30. Searches in that paper for Frobenius-group and
\(\operatorname{AGL}(1,q)\) generalizations found none.

Targeted literature searches were made for BI/Babai-invariant groups together with
Frobenius groups, sharply 2-transitive groups, \(\operatorname{AGL}(1,q)\), unique
nonlinear irreducible characters, and infinite BI-but-not-CI families. No prior theorem
matching the spectral-residue criterion or its all-\(q\) affine corollary was located.
Current references still present the general classification of finite BI-groups as an
open problem. A 2026 preprint on Ramanujan normal Cayley graphs of ratio-one Frobenius
groups studies a different question and does not state the BI property.

The classification of groups with one nonlinear character is classical and is not
claimed as new; neither are the regular-representation spectral decomposition nor the
CI Sylow restriction. The claimed contribution is the residue-modulo-degree recovery
argument and its consequences for the Frobenius branch of Seitz's classification and for an infinite
BI-but-not-CI subfamily.

Residual risk remains because bibliographic indexing is not exhaustive, and an
unindexed or differently phrased observation could exist. No inaccessible source was
identified whose title or available description specifically suggests this theorem.

## Value

**PASS.** The result turns two previously isolated nonabelian BI examples into a full
infinite structural family and gives a short reusable criterion based only on character
degrees and spectral multiplicities. It also produces infinitely many nonabelian
BI-groups that fail the stronger CI property, sharpening the separation between the two
notions.

## Limitations

The theorem does not settle the extraspecial \(2\)-group branch of Seitz's
classification, because there are \(d^2\) linear characters there and the modular
multiplicity reconstruction breaks down. The result is stated for simple undirected
Cayley graphs, as in the 2019 BI-group definition, and does not claim the corresponding
digraph statement.
