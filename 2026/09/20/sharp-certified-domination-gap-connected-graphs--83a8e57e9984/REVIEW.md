# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main bound follows from the established inequalities
\(\gamma_{\rm cer}(G)\le 2\gamma(G)\) and
\(\gamma(G)\le n/2\) for connected isolate-free graphs, together with
the fact that \(\gamma_{\rm cer}(G)\ne n-1\).

The new equality lemma was checked independently from the endpoint
statement. Refining the proof of the known
\(\gamma_{\rm cer}\le\gamma+|S_1|\) bound, equality
\(\gamma_{\rm cer}=2\gamma\) forces every vertex of a selected
minimum dominating set to be a half-shadowed weak support. Its unique
outside neighbor is therefore its private leaf, and domination forces
there to be no other outside vertices. This gives a corona. The converse
is immediate from the established certified domination number of a
corona.

For even order, equality in the gap bound forces
\(\gamma=n/2\) and \(\gamma_{\rm cer}=n\), hence the known corona
characterization applies. For odd order, a hypothetical larger gap would
force \(\gamma_{\rm cer}=n-1\), which is impossible. At equality, the
factor-two lemma eliminates the \(\gamma=(n-3)/2\) case; the remaining
case has \(\gamma_{\rm cer}=n-2\), and the established connected
characterization gives precisely the diadems for \(n\ge5\).

Direct enumeration of every connected graph in the NetworkX Graph Atlas
through order seven agrees with both the numerical formula and the
extremal classifications.

## Originality

**PASS, to the best of our knowledge.** The inspected full text of the
foundational certified-domination paper contains the factor-two upper
bound and says coronas establish its sharpness; it does not state an
if-and-only-if equality characterization for
\(\gamma_{\rm cer}=2\gamma\), nor an order-sharp maximum for
\(\gamma_{\rm cer}-\gamma\). The same paper separately characterizes
\(\gamma_{\rm cer}=n\) and \(\gamma_{\rm cer}=n-2\), which are used as
inputs here.

The inspected full text of the 2019 paper on equality of domination and
certified domination numbers focuses on \(\gamma_{\rm cer}=\gamma\),
upper certified domination, and related structural results. No statement
equivalent to the factor-two equality theorem or fixed-order gap theorem
was located.

Later searches found work on algorithms, criticality, certified variants,
and a 2025 constructive characterization of trees with
\(\gamma_{\rm cer}=\gamma\). No exact maximum of
\(\gamma_{\rm cer}-\gamma\) or converse factor-two equality theorem was
located. The full text of the 2025 tree-equality paper was not available
in the inspected sources; because it studies the same two parameters on
trees, a differently phrased overlap cannot be ruled out completely.
Unindexed literature remains another residual risk.

## Value

**PASS.** The result turns a known factor-two upper bound into an exact
equality characterization and then gives an exact parity-sensitive
fixed-order extremal theorem for all connected graphs, not just trees.
It also identifies every extremal graph: coronas in even order and
diadems in odd order at least five.

## Scientific limitations

- Originality is to the best of our knowledge.
- The theorem assumes finite simple connected graphs.
- The full theorem text of the 2025 tree-equality paper was not inspected.
- Unindexed or differently phrased corona/diadem results may exist.
