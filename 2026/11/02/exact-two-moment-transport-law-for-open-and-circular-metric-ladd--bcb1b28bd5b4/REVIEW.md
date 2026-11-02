# Scientific review

## Correctness — PASS

The theorem concerns two exact, fully specified length-metric graphs, normalized arclength and two independent points. The shortest-path endpoint-route analysis separates rail–rail, rail–rung and rung–rung pairs; the only nontrivial local correction arises when points lie on opposite rail copies within the same cell. Each conditional first and second moment is explicitly integrated in `RESULT.md`; the ordered arclength weights then yield all stated rational expressions. The strict open-versus-circular inequality has a positive-coefficient polynomial certificate for all integer orders at least three. An explicit coupling gives the claimed \(4/n\) almost-sure bounds and the triangular/uniform limiting laws. An independent exact rational checker recomputed the first two moments over 2,401 unordered pairs of metric edges from 14 finite graphs. Finite tests verify the formulas at those orders but do not substitute for the proof for every order.

## Originality — PASS, with residual risk

The closest work is Doyle and Graver (1982) on mean distances of graph-shaped domains, the 2023 continuously sampled network-mean algorithm of Garijo–Márquez–Silveira, and the 2024 general geometric bounds of Baptista–Kennedy–Mugnolo. The accessible 2023 full text explicitly characterizes the earlier special-family catalogue and contains no ladder/prism family formula; its arbitrary-graph computation algorithm does not state a symbolic all-orders second moment or the vanishing-length-fraction topology-change limit. The 2024 general bounds likewise do not imply the sharp formulas. The classical discrete Wiener polynomial of the prism concerns uniformly sampled vertices, not uniform arclength from all edges. Searches for equivalent names, graph products and network moment aliases uncovered no matching result. The full 1982 source remained inaccessible, and unindexed prior results remain possible; a secondary description is not a replacement for the original text.

## Mathematical value — PASS

The result fully determines two transport moments for each of two growing, non-cactus metric-network families and identifies a parity effect for the periodic network. More importantly, two added unit edges are an asymptotically negligible fraction of total length but change the entire scaled pair-distance law and reduce the leading mean and variance by sharp, nonzero proportions. The comparison is a natural geometric-network efficiency and boundary-condition phenomenon rather than an arbitrary isolated calculation. No claim is made for arbitrary edge weights or general network optimization.

## Sources and limitations

The earliest day-resolved primary geometric-network source used for archival placement is Bose et al., arXiv:1304.1909, first posted 2013-04-06. Earlier 1982 contributions are acknowledged with their year/month publication precision, without assigning an invented exact day. Material read in the later open-access full texts included the metric-graph definitions, previously solved special families, general algorithms and inequalities. The 1982 full text and one relevant original discrete-polymer paper were not materially inspected; their scope and the remaining priority risk are explicitly distinguished. The exact verifier uses only Python 3 standard-library arithmetic.

Self-review: passed. Independent audit: not yet performed.
