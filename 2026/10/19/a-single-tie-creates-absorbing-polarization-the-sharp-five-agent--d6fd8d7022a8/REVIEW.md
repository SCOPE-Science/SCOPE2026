# Review of edge-created absorbing polarization

## Correctness — PASS

The strict-update dynamics has the integer number of disagreeing edges as a strict Lyapunov function, ensuring almost-sure finite absorption. The four-vertex obstruction follows from a two-plus-two stable partition and the path/cycle dichotomy. The exhaustive program enumerates all 728 connected labeled five-vertex graphs, all admissible nonedges, all binary states, and all five-vertex relabelings. It finds exactly 90 creation transitions partitioned into 30 and 60 labeled representatives, with no earlier example. Two exact rational methods reproduce each graph's absorption probability and mean attempted-update count. The star-family formula is derived from competing vertex clocks; a center-flip probability tending to zero supplies a separate infinite-family proof of the one-quarter limit. Limits: the census is exhaustive only up to five vertices, whereas the analytic family claim holds for every integer at least four.

## Originality — PASS, with residual risk

Baek, Ha and Jeong's zero-temperature random-network Glauber dynamics allows random tie flips, unlike strict tie-retaining majority; its ensemble discordance distribution does not determine the first single-edge polarization threshold. Benjamini and collaborators study synchronous majority; Mohan and Prałat use an asynchronous process with initially unannounced public opinions and private-signal tie-breaking. Directly inspected definitions and result sections do not cover the marked graph classification or rational absorption probabilities, and the potential-decrease lemma is explicitly treated as prior background. Equivalent graph-cut terminology and relevant indexed research records were searched. Risks: obscure preexisting small-graph local-minimum tables or equivalent coordination-game results could narrow the originality assessment; comprehensive exclusion of all literature is impossible.

## Mathematical value — PASS

A single positive social contact changes the qualitative set of reachable stable outcomes, contradicting naive network-connectivity heuristics in a precise, motivated binary opinion model. Both sharp minimum order and the only two first-layer transitions are resolved exactly, with probabilities and absorption-time comparisons rather than an unsupported illustrative graph. The persistence of a one-quarter effect under a one-edge change to growing stars shows this is not merely a tiny-network artifact. Model-specificity (iid fair initial opinions, tie retention, uniform asynchronous choices) is a substantive limitation, not concealed.

## Closest literature and limitations

Baek–Ha–Jeong, arXiv:1112.5927; Benjamini–Chan–O'Donnell–Tamuz–Tan, arXiv:1405.2486; Mohan–Prałat, arXiv:2309.04691. The novelty claim is restricted to edge-created polarized absorption and its sharp finite/asymptotic specifications, not to the classical existence of nonconsensus metastability. No independent validation or audit has been undertaken.

Self-review: passed. Independent audit: not yet performed.
