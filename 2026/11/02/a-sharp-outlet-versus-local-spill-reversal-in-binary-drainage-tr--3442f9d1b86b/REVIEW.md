# Evidence assessment: binary drainage-tree spill reversal

## Correctness (C): PASS

The domain is fully specified: independent Bernoulli\((q)\) headwater inputs at four leaves, independent Bernoulli\((p)\) local inputs at exactly three internal vertices, and a three-input majority threshold at each confluence. The recursion \(F_p(x,y)=p(x+y)+(1-2p)xy\) follows by enumerating the three independent input bits. The two nonisomorphic four-leaf full binary trees give \(u=F_p(q,q)\), \(v=F_p(u,q)\), then root probabilities \(F_p(u,u)\), \(F_p(v,q)\), and expected internal spill counts \(2u+F_p(u,u)\), \(u+v+F_p(v,q)\). Expansion yields the two factorized identities in RESULT.md for all \(p,q\in[0,1]\). The sign of the remaining bracket is strictly positive on the open square, establishing the unique threshold, strict opposite rankings and boundary equalities. The independent `CHECK.py` enumerated 128 primitive configurations, matched both whole bivariate polynomials coefficient by coefficient, and passed 68 rational assertions. This checks a finite seven-input model exhaustively and does not assert properties of arbitrary large networks.

## Originality (O): PASS within specified evidence; historical-priority uncertainty remains

The full 24-page Peter–de Araújo–Araújo–Herrmann article, arXiv:1404.4232 (journal version available online 2014-03-13; arXiv version public 2014-04-16), was inspected for its water balance, routing, network reallocation, spill connectivity and avalanche comparisons (Sections 2.1, 2.6 and 3.2). Its physical-state reservoir simulation is distinct from these exact independent Boolean-threshold four-headwater probabilities. The full Amarù–Gaillardon–De Micheli 2014 majority-inverter graph manuscript was inspected around the majority algebra and transformation theorems; their identities reuse Boolean variables and do not state or dominate the exact shape-dependent probability and expected-count inequalities. Hui and Lund's 2014 parallel-reservoir allocation work concerns a distinct continuous optimization setting, but its full article could not be inspected, so comparison is limited to the abstract and bibliographic information. Additional searches for tree majority-gate probabilities, cascade topology, Bernoulli thresholds, hydrological flood networks and mathematical-result aliases revealed no direct covering theorem. An unknown earlier graph-reliability, stochastic-gate or reservoir reduction could still contain an equivalent statement. Search absence alone is not claimed to prove uniqueness.

## Mathematical value (V): PASS

Four headwaters form the smallest full binary confluence network with two distinct topologies, hence a natural complete finite classification, not an arbitrary parameter slice. The theorem separates two relevant risk objectives: outlet-spill probability and expected upstream spill burden. Their orderings are provably opposite with a sharp, input-independent threshold, showing why minimizing a single downstream outcome can increase the expected count of affected internal confluences even in a highly symmetric, exactly analyzable cascade. The result is useful as a reproducible benchmark for discrete flood-connectivity approximations; it does not imply a practical reservoir design rule without physical calibration.

## Closest sources and limits

- Peter et al., *Flood avalanches in a semiarid basin with a dense reservoir network* (2014), arXiv:1404.4232, full text inspected.
- Hui and Lund, *Flood Storage Allocation Rules for Parallel Reservoirs* (2014), https://doi.org/10.1061/(ASCE)WR.1943-5452.0000469, abstract only; incomplete priority comparison.
- Amarù et al., *Majority-Inverter Graph: A Novel Data-Structure and Algorithms for Efficient Logic Optimization* (2014), https://si2.epfl.ch/demichel/publications/archive/2014/PID3143501.pdf, full text inspected in the relevant logic sections.

Self-review: passed. Independent audit: not yet performed.
