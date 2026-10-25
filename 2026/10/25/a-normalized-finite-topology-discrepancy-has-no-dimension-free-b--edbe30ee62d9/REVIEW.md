# Review

## Correctness — PASS

The poset \(P\) has order complex the four-cycle, so \(H_1(P;\mathbb Z)\cong\mathbb Z\). Adding \(a<b\) yields two 2-simplices sharing an edge, a disk with zero first homology. The three-stage filtrations give the exact degree-one barcodes \(\{(0,2)\}\) and \(\varnothing\), so the bottleneck distance is \(1\). Exactly one point is added to one minimal open, giving discrepancy \(1/N^2\).

## Originality — PASS

The closest source, Kayacan’s finite-topology persistence framework, proves stability for bounded perturbations of the input metric. Its later version treats local-refinement and fixed-dictionary hypotheses and reports empirical discrepancy comparisons; those results do not imply a dimension-independent bound from the normalized minimal-open discrepancy for arbitrary finite-topology filtrations. Targeted searches found no exact covering statement. This is not a claim of exhaustive novelty proof.

## Value — PASS

The counterexample gives a sharp asymptotic separation between a normalized local topology-change score and persistence stability. It shows why an empirical relation between the two cannot, without additional hypotheses, be promoted to a dimension-free theorem.

## Closest literature and limitations

The result is limited to abstract finite-topology filtrations on a shared labelled set. It does not refute stability under metric perturbations or establish instability within any particular density-based or anchor-based construction. The included standard-library script verifies the finite face counts and boundary ranks; the integral homology follows from the explicit cycle and disk descriptions.

Self-review: passed. Independent audit: not yet performed.
