# Independent audit — 2026-10-01

## Final claim assessed

The explicit rotation system in `RESULT.md` gives a minimum-genus orientable quadrangulation of \(K_{4,10}\) with an orientation-preserving automorphism of order \(10\) acting cyclically on the ten-vertex part.

## Correctness — PASS

A fresh face trace of the stated rotations gives exactly 20 faces, all of length 4. With 14 vertices and 40 edges, Euler's formula gives genus 4, which equals Ringel's minimum-genus value. A separate cyclic-order check verifies that \(a_0\leftrightarrow a_1\) together with \(b_i\mapsto b_{i+1}\) preserves every vertex rotation and has order 10.

## Originality — PASS

Searches compared the statement with Ringel-type complete-bipartite genus results, Jones's classification of regular embeddings of \(K_{n,n}\), Fan–Li edge-transitive embedding work, and the published internal corpus. Those sources either give the genus, concern equal bipartition sizes, or impose stronger/different transitivity. No source inspected states or implies this exact \(K_{4,10}\) minimum-genus order-10 cyclic witness.

Residual risk: an older current-graph construction could encode an equivalent witness without emphasizing this automorphism.

## Scientific value — PASS

The claim is an explicit symmetric extremal embedding for a natural complete bipartite graph, with a short independently checkable certificate. It is more than a bare genus recomputation because the order-10 symmetry is additional structure at minimum genus.

## Outcome

Correctness, originality, and scientific value all pass for the final claim as stated.
