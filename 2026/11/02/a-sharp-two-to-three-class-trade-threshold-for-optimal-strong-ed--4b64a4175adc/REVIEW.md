# Scientific review: optimal Heawood strong-edge-colouring trades

## Correctness

PASS. The edge set is the \(21\) Fano incidence flags, whose induced-match compatibility is explicitly defined. A four-flag induced matching is excluded by the tangent-line argument for four-point subsets of the Fano plane, and an explicit partition into seven compatible triples establishes optimality. A least-uncovered-edge exact-cover recurrence exhausts the \(416\) unordered optimum partitions without duplicates. Complete pair comparison proves there is no legal two-class trade and that the three-class graph has exactly \(1568\) edges; all-source BFS establishes connectedness, radius \(6\), and diameter \(6\). Automorphism actions exhaust the six claimed orbits. The separately implemented vector-space C++ program checks the critical enumeration and distance claims independently of the cyclic-incidence implementation. The theorem concerns only this finite graph and the expressly defined trades.

## Originality

PASS under the available record, with explicit historical residual risk. Kloks–Ung–Wang (arXiv:1110.3583, 2011) define and treat strong edge-colouring in distinct algorithmic graph classes but do not classify Heawood colourings. The Skupień 2023 full-text discussion directly treats both the Petersen and Heawood graphs: the Heawood chromatic index \(7\) and existence of a seven-triple decomposition are known, while the paper's uniqueness result is for Petersen, not Heawood. Lužar et al. (arXiv:2101.04768) likewise acknowledge the pre-existing index \(7\), without giving the optimum-colouring census or this trade graph. Ordinary proper three-edge-colouring, Fano harmonious vertex-colouring, and matching-complex calculations are not equivalent to the claimed strong seven-edge-colouring trade classification. Targeted research-record searches returned no covering item. This negative search does not establish publication priority and does not exclude unindexed or inaccessible work.

## Value

PASS. This is a natural structural question following the known extremal strong chromatic index: how many optimisers are there, and how much simultaneous recolouring is necessary to travel between them without increasing the palette? The answer exhibits a sharp local-mobility threshold (two classes frozen, three classes connected), a tight six-step diameter, nonuniform degrees, and six symmetry types. The contrast with the known unique Petersen optimum is especially motivating. The result is an exact reconfiguration benchmark for optimal strong edge assignments, not a routine recalculation of the known scalar index. It makes no claim of a general theorem for other cubic graphs.

## Prior literature and limitations

Closest relevant primary material: Kloks–Ung–Wang (2011), arXiv:1110.3583; Skupień (2023), DOI:10.7151/dmgt.2394 (full public text inspected); and Lužar et al. (2021), arXiv:2101.04768. The Faudree et al. 1990 index result is explicitly excluded from novelty. Other nearby work on graph reconfiguration or Fano structures may exist. A same-object unindexed classification remains a residual risk. Reconfiguration under individual Kempe chains was not analysed; the permitted move is simultaneous repartition of at most three whole colour classes.

Self-review: passed. Independent audit: not yet performed.
