# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/q11-cubic-acute-seven-exchange-isolation--a555a8810a2a`  
Assigned source tree: `c64bf6f9ddcd1b4c2b29f7065a4d97cb96d42122`  
Audited current source tree: `c64bf6f9ddcd1b4c2b29f7065a4d97cb96d42122`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `644c3c79fa24897ac8edf7a95aac5267d7255fc8`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The local-isolation theorem is correct. For binary cube vertices, (x-y)·(z-y) counts coordinates with x_i=z_i!=y_i, so a right angle at y is exactly the Hamming-geodesic condition y in I(x,z); this establishes the acute/general-position equivalence. The supplied C++ verifier was inspected line by line: for every deletion mask of size r<=7 it forms exactly the vertices compatible with every retained pair, computes exact pair compatibility against retained vertices, and then backtracks through all r+1-subsets while checking all-new triples. These conditions exhaust every triple of a proposed 25-point extension, and deleted base vertices are allowed to reappear. An independent compile-and-run reproduced the complete output, including 280824 relevant deletion masks at r=7, maximum 101 candidates and no completion. Hence any 25-point set intersects the displayed 24-point witness in at most 16 vertices and has symmetric difference at least 17.

## Originality

**qualified_supported_computational_local_rigidity**. OEIS A089676 currently records 24 as the best known lower-bound witness in dimension 11 and supplies the Kamenetsky construction; Korze-Vesel treat the equivalent hypercube general-position problem and separating-system literature supplies the coding translation. Searches using cubic acute, hypercube general position, (2,1)-separating and frameproof-code vocabularies together with exchange/local/overlap terminology did not locate this seven-exchange statement for the explicit witness. The result is therefore supported as a local computational rigidity theorem, not as a new global bound, with normal residual risk from differently indexed coding literature.

## Scientific value

**meaningful_local_search_obstruction**. The theorem does not improve the known 24-point lower bound, but it completely excludes a large natural repair neighborhood around the strongest recorded witness: any 25-point improvement must replace at least one third of the old points. This gives concrete guidance for exact and heuristic searches at the unresolved dimension.

## Independent checks

- Inspected the exact verifier source (Git blob 9c768bc6bc395aef89dc92caebcbe0992b5c5499) and verified that its candidate, pair and all-new-triple checks are jointly necessary and sufficient.
- Independently compiled and reran the verifier; the output exactly matched the committed result through deletion radius seven.
- Checked the binary dot-product/geodesic equivalence and the conversion from intersection <=16 to symmetric difference >=17.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/q11-cubic-acute-seven-exchange-isolation--a555a8810a2a
- https://oeis.org/A089676
- https://oeis.org/A089676/a089676_1.txt
- https://doi.org/10.1007/s00009-023-02416-z
- https://doi.org/10.1007/s11856-012-0126-9
- https://doi.org/10.1016/S0304-0208(08)73398-X
## Limitations

- This is a local theorem for one explicit configuration and its cube-automorphic images, not a global upper bound for gp(Q_11).
- A 25-point set sharing at most 16 vertices with the witness remains possible.
- The exhaustive certificate stops at seven deletions and is computational rather than proof-assistant formalized.
- Differently indexed frameproof/separating-code literature remains a residual originality risk.
