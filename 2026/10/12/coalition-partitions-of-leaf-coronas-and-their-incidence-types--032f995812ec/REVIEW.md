# Review of Coalition partitions of leaf coronas and their incidence types

## Correctness
PASS. The unique private-neighbor property proves domination if and only if a set meets each core-leaf pair, for **every** base graph. Encoding pairs as edges of the incidence multigraph makes a coalition partition equivalent to no singleton vertex cover and every block-vertex lying in a two-vertex cover. If five or more blocks exist, three outsiders of a chosen two-cover force one of its vertices to be a singleton cover, a contradiction. At four blocks, the cover constraints remove all loops and restrict the simple support to exactly \(2K_2\), \(P_4\), or \(C_4\). Surjective edge assignments, independent pair orientations, and the groups of respective orders \(8,2,8\) count every unordered optimum exactly once. Independent full enumeration of all 120333 vertex partitions for core orders 2 through 5 confirms both value and counting formula. The finite check is corroborative, not the infinite proof.

## Originality
PASS. Haynes et al. (2020) define ordinary coalitions and study paths, cycles, and general bounds, with no leaf-corona count. Bakhshesh–Henning–Pradhan (2021) examine extremal coalition numbers on trees, not the universal leaf-corona partition support. Alikhani et al. (2023) and Guan–Wang (2024) concern the stronger **connected** coalition number and obtain value \(2\) for connected leaf coronas, which does not imply ordinary coalition number or classify optimum partitions. The direct incidence-cover reduction and exact enumeration are not supplied by those results or the searched indexed findings. Residual risk is incomplete coverage of otherwise indexed literature or differently phrased treatments.

## Value
PASS. The theorem settles both a universal exact ordinary coalition value and the complete structure and count of its optimal partitions on a natural graph operation, regardless of the arbitrary base-graph edges. The three-support classification gives a structural explanation and turns the count into a surjection/automorphism formula. For connected bases, it also pinpoints a uniform strict gap from the already studied connected-coalition value \(2\), making the distinction between two related domination-partition parameters mathematically concrete.

Self-review: passed. Independent audit: not yet performed.
