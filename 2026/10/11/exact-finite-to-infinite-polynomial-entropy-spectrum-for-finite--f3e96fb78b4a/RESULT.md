# Exact finite-to-infinite polynomial entropy spectrum for finite-chain-recurrent regular curves
## Finding
Let \(X\) be a nondegenerate regular curve and let \(f:X\to X\) be a homeomorphism whose chain recurrent set is finite. Then \(h_{\mathrm{pol}}(f)=1\). For every integer \(n\ge 2\) and every \(1\le m<n\),
\[
h_{\mathrm{pol}}(F_n(f))=h_{\mathrm{pol}}(\mathcal{S}F_n(f))=h_{\mathrm{pol}}(\mathcal{S}F_n^{m}(f))=n.
\]
For the full hyperspace of nonempty closed subsets,
\[
h_{\mathrm{pol}}(2^f)=+\infty.
\]
Consequently, finite-chain-recurrent dynamics on a nondegenerate regular curve has a complete induced polynomial-entropy spectrum: every finite-particle and generalized quotient layer has exactly linear level \(n\), while passing to the unrestricted hyperspace produces an infinite jump.

## Assumptions and scope
A regular curve is a continuum in which every point has arbitrarily small neighborhoods with finite boundary. The nondegeneracy assumption means that \(X\) contains more than one point. The space \(F_n(X)\) is the hyperspace of nonempty subsets of cardinality at most \(n\). The symmetric-product suspension is \(\mathcal{S}F_n(X)=F_n(X)/F_1(X)\), and the generalized suspension is \(\mathcal{S}F_n^{m}(X)=F_n(X)/F_m(X)\) for \(1\le m<n\). The full hyperspace \(2^X\) consists of all nonempty closed subsets of \(X\). All induced maps are those obtained by applying \(f\) pointwise and then passing to the indicated quotient.

## Proof
For a homeomorphism of a regular curve, the cited regular-curve dynamics result gives \(\mathcal{CR}(f)=\mathrm{NW}(f)\). Since \(\mathcal{CR}(f)\) is finite, \(\mathrm{NW}(f)\) is finite. A nondegenerate continuum has infinitely many points, so \(X\setminus\mathrm{NW}(f)
eq\varnothing\); hence \(f\) has a wandering point.

Đorić and Katić prove that every homeomorphism of a regular curve has polynomial entropy at most \(1\), and that the existence of a wandering point forces equality. Therefore
\[
h_{\mathrm{pol}}(f)=1.
\]
Đorić's finite-chain-recurrence theorem for symmetric products and generalized symmetric-product suspensions states that, for every \(n>m\ge1\),
\[
h_{\mathrm{pol}}(\mathcal{S}F_n^{m}(f))=h_{\mathrm{pol}}(F_n(f))=n\,h_{\mathrm{pol}}(f).
\]
Taking \(m=1\) also gives the ordinary suspension \(\mathcal{S}F_n(f)\). Substituting \(h_{\mathrm{pol}}(f)=1\) proves all finite-level equalities.

Finally, Đorić and Katić prove that a regular-curve homeomorphism with a wandering point satisfies \(h_{\mathrm{pol}}(2^f)=+\infty\). Their proof uses the invariant inclusions \(F_n(X)\subset 2^X\) together with \(h_{\mathrm{pol}}(F_n(f))=n\) for every \(n\). This gives the claimed finite-to-infinite jump.

## Verification
The proof is deductive and uses no finite computation as evidence for an infinite statement. The hypotheses match the cited theorems: a regular curve is compact, the map is a homeomorphism, and its chain recurrent set is finite. Nondegeneracy is used only to ensure that a finite non-wandering set cannot equal all of \(X\). The integer quantifiers are \(n\ge2\) and \(1\le m<n\). The full-hyperspace conclusion uses the same wandering point already forced by finite chain recurrence.

## Relationship to prior work
The 2025 symmetric-product-suspension paper proves the factor \(n\) formula for compact spaces with finite chain recurrence and extends it to \(\mathcal{S}F_n^{m}\), but its concrete exact-entropy applications are stated for the interval and circle. The 2026 regular-curve paper proves \(h_{\mathrm{pol}}(f)=1\), \(h_{\mathrm{pol}}(F_n(f))=n\), and \(h_{\mathrm{pol}}(2^f)=+\infty\) when a regular-curve homeomorphism has a wandering point, but does not state the suspension or generalized-suspension spectrum. Combining the two results with finite chain recurrence yields the all-\(n\), all-\(m\) classification above. Earlier work of Barragán, Santiago-Santos, and Tenorio defines and studies \(\mathcal{S}F_n^{m}\) through qualitative dynamical properties, not polynomial entropy.

## Limitations
The claim is restricted to nondegenerate regular curves and homeomorphisms with finite chain recurrent set. It does not assert an analogous exact spectrum for arbitrary continuous maps, for regular-curve homeomorphisms with infinite chain recurrent set, or for continua outside the regular-curve class. It also does not classify finer growth constants beneath polynomial entropy.

## References
1. Maša Đorić, *Polynomial entropy on the \(n\)-fold symmetric product and its suspension*, arXiv:2507.10126v1, first public 2025-07-14.
2. Maša Đorić and Jelena Katić, *Polynomial entropy on regular curves*, arXiv:2602.19256v1, first public 2026-02-22.
3. Franco Barragán, Alicia Santiago-Santos, Jesús F. Tenorio, *Dynamic properties of the dynamical system \((\mathcal{S}F_n^{m}(X),\mathcal{S}F_n^{m}(f))\)*, Applied General Topology 21 (2020), 17–34, DOI 10.4995/agt.2020.11807.
