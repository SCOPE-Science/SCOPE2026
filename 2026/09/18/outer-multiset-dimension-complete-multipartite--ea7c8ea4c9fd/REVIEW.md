# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof reduces every representation in a complete multipartite graph to the multiplicity of distance 2. If a landmark set contains \(s_i\) vertices of part \(V_i\), then every outside vertex of that part has representation \(\{\!\{1^{|S|-s_i},2^{s_i}\}\!\}\). This immediately forces at most one omitted vertex per part; two omitted vertices from distinct parts are distinguished exactly when the two corresponding part sizes differ. The lower and upper bounds \(n-d\) therefore match, and the basis count follows bijectively. The argument covers singleton parts and the smallest connected case \(K_2\).

The statement was stress-tested against the known endpoints: balanced complete multipartite graphs have one distinct part size and hence dimension \(n-1\), while graphs with all part sizes distinct have dimension \(n-r\). Stars give \(n-2\) when the two part sizes differ. An exhaustive finite check from the definitions verified the characterization, dimension, and basis count for all 58 nondecreasing part-size types of total order at most 8.

## Originality

The foundational Gil-Pons--Ramírez-Cruz--Trujillo-Rasua--Yero (2019) paper was inspected at Proposition 3.4; that proposition treats complete multipartite graphs only when all part sizes are equal. The closest later primary source, Klavžar--Kuziak--Yero (2023), was inspected at the relevant theorem and complete-multipartite passage. It explicitly gives the balanced case and, separately, the case of pairwise distinct part sizes. It does not state the mixed regime with repeated and nonrepeated sizes. The full Pervaiz--Simanjuntak--Saputro (2025) joined-graphs paper was inspected; its complete list of treated families is stars, wheels, generalized wheels, windmills, fans, and generalized fans. Exact and synonymous literature searches for complete multipartite, complete \(k\)-partite, repeated part sizes, distinct part sizes, joins of independent sets, and basis enumeration did not locate the general formula or characterization. The 2026 survey table lists only the balanced complete multipartite value.

Originality is therefore assessed as PASS to the best of our knowledge, not as certainty. No material inaccessible source was identified among the closest references. The main residual risk is very recent or poorly indexed parallel work, or an equivalent statement under terminology not captured by the searches. No checked source contained the full resolving-set characterization or the basis enumeration.

## Value

The result closes the natural gap between the two complete-multipartite endpoint cases already placed side by side in the 2023 literature. The exact dependence on the number of distinct part sizes explains the additional obstruction created by repeated size classes, and the characterization of every resolving set is stronger than the numerical dimension formula. The basis count and the elementary-symmetric enumeration give reusable combinatorial information beyond a single parameter value.

## Limitations

The theorem concerns connected complete multipartite graphs and does not claim a formula for arbitrary graph joins or general diameter-two graphs. It does not address algorithmic complexity beyond this family. The computational check is only a sanity check and is not used in the proof. Originality is to the best of our knowledge; no material inaccessible source was identified among the closest references.
