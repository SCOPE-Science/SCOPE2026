# Scientific review: locally-optimal colourings of circular ladders

## Correctness — PASS

The graph has exactly three neighbours at each vertex for every \(n\ge3\), so unique-neighbour-plurality is exactly the two-of-three condition. An unequal rung forces both horizontal neighbours in each layer to agree with the vertex; propagation closes the entire cycle and makes both layers individually monochromatic. Otherwise every rung agrees and the local condition is exactly absence of singleton monochromatic runs. The two cases are disjoint, exhaustive and sufficient. Cyclic boundary sets with \(r\) runs have count \(\tfrac nr\binom{n-r-1}{r-1}\), including the two-run case; the cyclic proper-colouring count is \((k-1)^r+(-1)^r(k-1)\). Formal-series logarithms establish the Lucas and rational forms for all permitted parameters. A packaged independent script checks \(2{,}065{,}492\) assignments and symbolic-identity specializations. No finite experiment is used as an infinite proof.

## Originality — PASS with explicit residual risk

Jones–Winkeler (arXiv:2603.18289v1, 2026) already define the notion and give a general subcubic recurrence, which is fully credited; no separate prism coefficient distribution or six-periodic closed formula was identified in the inspected source. Shukla (2005) describes binary Ising-ladder frozen-domain structures, overlapping the two-colour intuition but not supplying the all-palette formula. Search comparisons for prism/circular-ladder majority fixed states and the characteristic Lucas root found no exact dominating result. The search is not an exhaustive guarantee of priority; unindexed equivalent work remains possible. The original paper's general recurrence ensures computability but does not state the explicit claimed family identity.

## Value — PASS

The source introduces the locally-optimal polynomial precisely to quantify obstacles to graph consensus. A full explicit evaluation on the canonical three-regular cylindrical family answers that counting question at every length and every palette size. The dichotomy describes *all* admissible configurations, distinguishes global layer polarization from local stable blocks, resolves the maximum number of usable colours, and exhibits an exact six-periodic correction to a Lucas recurrence together with a rational generating function and growth rate. These strengthen a basic binary-domain observation rather than repeating it.

## Source boundaries and limitations

Primary comparison: Jones and Winkeler, *Counting Strict Gridlock on Graphs*, arXiv:2603.18289v1; definition, relevant recurrence and appendix text inspected, plus targeted searches for prism and ladder terminology. Earlier comparison: Shukla, *Voter dynamics on an Ising ladder: coarsening and persistence*, Journal of Physics A 38 (2005), 5441–5451; text-layer pages 1–3 examined for frozen-domain discussion, without a successful visual screenshot. General majority dynamics (binary opinions) and unrelated prism graph invariants do not automatically imply the all-palette formula. No claim of stochastic convergence probability, publication priority proof, or independent scientific certification is made.

Self-review: passed. Independent audit: not yet performed.
