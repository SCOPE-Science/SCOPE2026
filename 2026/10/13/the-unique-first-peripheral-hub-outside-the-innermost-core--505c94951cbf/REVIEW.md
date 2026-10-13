# Self-review

## Correctness
**PASS.** The proof does not rely on finite search for the sharp lower bound or the isomorphism classification. If a unique maximum-degree vertex \(h\) lies outside the maximum \(k\)-core, then \(h\) has at most \(k-1\) neighbors in that core, giving \(\deg(h)\le |V|-3\). For at most six vertices this forces \(k=2\), and connectedness then contradicts uniqueness of the degree leader. At seven vertices, the same argument forces a \(3\)-vertex \(2\)-core, hence a triangle, and then forces the unique degree-\(4\) hub with exactly three pendant leaves. The exhaustive replay independently confirms all connected labeled graphs through order seven and the complete \(420\)-graph orbit.

Risk: the result is only about the first graph order and does not assert a larger-order classification.

## Originality
**PASS.** Prior work already owns the \(k\)-core concept and the qualitative observation that highly connected hubs can occupy peripheral low-coreness positions. The accepted claim is narrower and structural: the exact smallest connected order for a **unique** degree leader to miss the innermost core, together with uniqueness of the first obstruction and its labeled count. Searches by standard aliases, exact graph order, peripheral-hub language, and the degree-versus-coreness implication did not locate an equivalent theorem or table.

Risk: search failure is not proof of bibliographic uniqueness. A small-graph atlas, lecture note, or code corpus could contain the same seven-vertex observation.

## Value
**PASS.** Degree is the most local notion of network prominence, while coreness records survival inside recursively cohesive structure. The literature explicitly uses this contrast to explain why hubs can be peripheral. The smallest network where a single unambiguous degree leader is already expelled from the innermost core is therefore a natural structural boundary, not an arbitrary parameter slice. The fact that the whole first layer is one graph type makes the obstruction interpretable and reusable.

Self-review: passed. Independent audit: not yet performed.
