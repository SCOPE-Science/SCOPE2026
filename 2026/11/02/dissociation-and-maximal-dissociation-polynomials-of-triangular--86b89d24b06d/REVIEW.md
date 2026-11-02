# Scientific review

## Correctness — PASS

For a selected base edge \(uv\), its degree in the induced triangular graph is \(\deg_H(u)+\deg_H(v)-2\). The bound one forces a disjoint union of base \(K_2\), \(P_3\), and singleton components. Maximality is equivalent to either using all root vertices or leaving one unused root vertex while using only \(P_3\) components. Adding an edge in the excluded cases gives a valid enlargement, and every omitted edge in the two admitted cases breaks the maximum-degree-one condition. The labeled exponential formula counts these configurations without duplication. The coefficient-ratio argument handles the corrected highest coefficient for orders congruent to one modulo three; the finite boundary cases are checked directly. The standalone graph-level verifier agrees for \(2\le n\le9\) and separately checks strict log-concavity for \(2\le n\le200\). Numerical checks are not used to prove the unrestricted statement.

## Originality — PASS, provisional

Orlovich et al., *The complexity of dissociation set problems in graphs* (2011), DOI:10.1016/j.dam.2011.04.023, treat line graphs and prove an extremal cardinality formula for line graphs of Hamiltonian-path graphs; this already implies the maximum size \(\lfloor 2n/3\rfloor\) here. That scalar statement is credited, not claimed new. Their accessible abstract and relevant line-graph theorem/sections do not supply coefficientwise all-set and inclusion-maximal counts or the corrected one-unused-vertex class. Their complete publisher PDF could not be inspected, leaving a specific priority risk. Tu, Li, and Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs* (arXiv:2103.01402; 2021), were inspected in accessible full text: their general graph bounds and extremal classifications do not cover this family-specific coefficient theorem. Tu, Xiao, and Lang, *Counting the number of dissociation sets in cubic graphs* (2023), DOI:10.3934/math.2023507, give cubic graph bounds; triangular graphs are not cubic. Relevant Johnson/line graph formulations, indexed counting tables, and existing related graph-family enumerators were compared without finding a complete equivalent. Lack of a match cannot establish publication priority.

## Mathematical value — PASS

For \(n\ge4\), the triangular graphs \(L(K_n)\) form a canonical strongly regular family. The result determines *both* complete labeled subset distributions and the finer inclusion-maximal distributions, not simply a known dissociation number. The maximal configurations have a structural one-unused-vertex exception responsible for top-coefficient corrections; this leads to a sharp gap-free cardinality spectrum, an isolated all-maximal-equal phenomenon at order seven, and strict log-concavity. These are informative invariants of a natural graph family, with plausibly useful partition and counting interpretations. No claim is made of a general line-graph polynomial theorem or a novel component-enumeration technique.

## Remaining limitations

The first related full preprint is dated 2021-03-02. An exact equivalent may have appeared under \(K_2/P_3\)-partition, dissociation, or line-graph language. The 2011 publisher full text was not available through the accessible route, and independent mathematical and priority reviews have not been conducted. The all-parameter theorem depends on the proof, not the finite verification.

Self-review: passed. Independent audit: not yet performed.
