# Scientific review: local Nash certificates and fragmentation

## Correctness

PASS. All hypotheses are explicit: simple undirected unit-weight graph, minimum degree at least one, maximum degree at most two, and coalition-size normalization inclusive of the agent. An agent with no friend inside its coalition can strictly improve by joining a neighbor's coalition. For every boundary edge, each endpoint then has exactly one friend inside and one outside. The two reciprocal-size deviation inequalities are necessary and sufficient. The cycle component upper bound follows because each coalition run and each separating gap has length at least two. Alternating balanced runs attain the bound for every cycle size. The eight-vertex count follows from forced run lengths and coalition-size balance. Exhaustive direct-payoff integer checking verified 172,620 set partitions; the proof covers arbitrarily many vertices.

## Originality

PASS under the inspected-source and indexed-record comparison, with residual priority risk. The 2015 Brandl–Brandt–Strobel paper treats general stability questions; the 2018 Bilò–Fanelli–Flammini–Monaco–Moscardelli study analyzes Nash existence, efficiency and paths/trees; and the 2023 Hanaka–Ikeyama–Ono paper concerns welfare optimization rather than an all-partition Nash certificate. None of the inspected statements implies the exact two-condition characterization together with the sharp disconnected-component spectrum. Related earlier work on welfare-optimal partitions and core-blocking coalitions on cycles addresses distinct predicates. An equivalent unindexed specialization may still exist.

## Value

PASS. The result converts unilateral stability on an entire bounded-degree social-network class into a linear-time size-and-adjacency certificate, despite the possibility of spatially disconnected coalitions. The sharp \(\max\{1,\lfloor n/4\rfloor\}\) fragmentation law and first eight-vertex example answer a natural structural question: how geographically fragmented a self-enforcing community can be. The statement is not merely a small enumeration; it applies to arbitrary finite path/cycle unions and makes a sharp all-size prediction.

## Limitations and closest literature

Most relevant: Bilò et al. (2018), https://doi.org/10.1613/jair.1.11211 ; Hanaka et al. (2023), https://arxiv.org/abs/2310.05139 ; Brandl et al. (2015), https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2015/aamas/p1219.pdf . This result does not classify stronger blocking notions or weighted, modified, higher-degree, or isolated-vertex models. Specialist preprints outside indexed coverage may overlap. No independent verification or external priority determination is claimed.

Self-review: passed. Independent audit: not yet performed.
