# Census construction notes

The order-eight census was generated from the complete NetworkX graph atlas at order seven. For each of the 1,044 unlabeled seven-vertex graphs, one new vertex was added with each of its 128 possible neighborhoods. Exact graph isomorphism testing then removed duplicates. Every eight-vertex graph occurs in this augmentation: delete any one vertex, identify the resulting seven-vertex graph with its atlas representative, and recover the deleted vertex by its neighborhood. The exact quotient contains 12,346 graphs, agreeing with the standard Brendan McKay unlabeled-graph census count for order eight.

The generated order-eight file has SHA-256 `d6bba0a339f03ea5ae2a9035c09e73e9852e4d8e4614578f8ca82d113d9c96cc`. The combined order-one-through-eight census consumed by `verify.py` is `graphs_upto8.g6`.
