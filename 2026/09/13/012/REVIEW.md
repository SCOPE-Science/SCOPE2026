# Review

Independent mathematical audit completed on 2026-10-01 UTC.

- Correctness: **PASS**
- Originality: **PASS**
- Scientific value: **PASS**
- Disposition: **PASSED**

## Correctness

With \(L_0\) full, every \(v\in L_1\) already has the \(e_5\) axis represented by its below neighbor. Its above neighbor lies on the same axis and cannot provide a second axis, so under the two-distinct-axes rule \(v\) activates exactly when an in-layer neighbor on one of \(e_1,\dots,e_4\) is infected. Hence \(L_1\) is exactly 1-neighbor bootstrap on a connected 4-torus, fills iff its initial set is nonempty, and has exact failure probability \((1-p)^A\). For the standard 2-neighbor rule, one initial in-layer seed or one frozen above-layer helper seeds the same in-layer spread, giving \((1-p)^{2A}\) in the frozen-helper model and an upper bound in full dynamics. The box surface coefficient \(18\,2^{-4/5}\approx10.3383\) exceeds the cube coefficient 10, so the stated isoperimetric correction is also correct.

## Originality

The closest primary literature on modified bootstrap uses the much stronger condition 'at least one active neighbor in each of the \(d\) dimensions'. Holroyd's dimensional-reduction observation for that model is therefore not the same as the record's two-distinct-axes rule. Standard \(r\)-neighbor threshold papers likewise do not imply the exact \((1-p)^A\) single-face law for this rule. No earlier published SCOPE record or primary source located in the searches states this exact local cascade/exponent split.

## Scientific value

This is a motivated structural lemma for the exact nonstandard update rule under study: it identifies the true one-face dynamics, gives an exact finite-volume failure law and exposes a factor-two local exponent difference from standard 2-neighbor bootstrap. That local mechanism is a natural input to any future multi-slab or threshold analysis, even though the global sharp window remains open. The elementary cube-vs-\(\gamma=2\) surface correction is supporting context rather than the sole source of value.

## Limitations

- The audit validates only the single-face law, standard-rule comparison, and elementary surface correction; it does not validate the admitted two-sided sharp window or multi-slab growth.
- Originality is best-of-knowledge under terminology variation for anisotropic bootstrap rules.
