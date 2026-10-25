# Scientific review

## Correctness — PASS
For every original leaf edge, deleting first the outgoing midpoint-to-neighbor arc and then the incoming neighbor-to-midpoint arc is justified by maximal-face domination; each elementary-collapse step preserves homotopy. The remaining two opposite arcs on the leaf half-edge form an independent zero-sphere factor. Induction over all edges yields the cross-polytope boundary, including isolated components and the \(m=1\) boundary. The arrow-reversal involution has no invariant nonempty simplex, so its Lefschetz number fixes the integral orientation character \((-1)^m\). The accompanying finite exhaustive checker reproduced every local domination for 339 forest inputs. It is a regression check, not a substitute for the infinite proof.

## Originality — PASS, with risk
The defining 2026 source treats bidirected paths and polygons. The general homotopy source studies specific orientations and regional decompositions; neither directly implies an elementary collapse of arbitrary *once-subdivided*, all-bidirected forests, much less the reversal character. A directly inspected public result treats **unsubdivided** bidirected double stars and even allows mixed-dimensional homology, making its hypotheses genuinely different; the claim is not an application of its formula. An inspected public result on bidirected polygons has cyclic, not acyclic, underlying graphs. Broader equivalences under alternative names remain possible, and neither database searches nor access to primary texts certify global uniqueness.

## Value — PASS
This is a uniform simple-homotopy classification of an infinite class with arbitrary branching and disconnected components, not a new computation for an arbitrarily selected small graph. Its elementary-collapsing mechanism explains the topological change caused by edge subdivision, whereas generic unsubdivided bidirected trees can have mixed-dimensional homology. The global arrow-reversal sign is integral symmetry information not determined by a bare Betti number.

## Closest literature and boundaries
Caputi–Collari–Smith (arXiv:2601.05670), Proposition 2.2, covers the path-only special case. Caputi–Collari–Di Trani–Smith (arXiv:2208.04656) covers alternative oriented-tree constructions. The public bidirected-double-star classification covers the original unsubdivided graph, not this transformed graph. Forest, subdivision, and full bidirection assumptions are essential. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
