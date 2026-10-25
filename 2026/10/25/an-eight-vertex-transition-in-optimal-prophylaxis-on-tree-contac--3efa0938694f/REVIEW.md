# Scientific review of the eight-vertex vaccination transition

## Correctness
**PASS.** For a removed vertex, the expected outbreak size from a source sampled uniformly among unvaccinated vertices equals the ordered-pair connection probability sum divided by the remaining population size. Every connected pair in a residual tree has a unique path, so the expression is an exact polynomial in the independent edge-transmission probability. The exhaustive lower bound uses a complete leaf-extension construction of all unlabelled trees through seven vertices, with duplicate removal by graph isomorphism and exact real-root sign certification of all needed polynomial comparisons. The eight-vertex witness's two objective polynomials differ by \(2p(p^3+p^2-1)\); strict monotonicity of the cubic, comparison with all other targets, and an independent edge-subset enumeration support the sharp transition.

## Originality
**PASS, with qualifications.** Newman's 2002 epidemic-percolation analysis establishes the transmission model, not a sharp minimum tree order at which the best vaccination vertex depends on transmissibility. Holme (2017) studies closely related exact node vaccination rankings on small graphs, including graphs up to seven vertices, but uses the Markovian continuous-time SIR dynamics with shared recovery-time dependence, rather than independent edge openings; its stated census does not establish the present eight-vertex tree threshold. Earlier network-vaccination and target-selection results motivate the question but were not found to supply its exact sharp answer. Search and source comparisons were restricted to accessible material; an equivalent independent-bond optimal-node theorem in older graph-reliability literature remains a residual bibliographic risk.

## Value
**PASS.** The target-selection question is a natural public-health optimization problem: whether intervention priority can be chosen from topology alone or changes when transmissibility changes. The result gives a rigorous, minimal eight-individual boundary, a complete order-at-most-seven guarantee, and a nontrivial exact algebraic threshold between vaccinating a branching hub and a different, more balanced location. It separates local-degree intervention intuition from large-transmission component-size effects. No claim is made for non-tree networks, heterogeneous transmission, multiple vaccinees, or correlated SIR transmissions.

## Scope and outstanding checks
The exhaustive classification is finite and requires exact symbolic and graph-isomorphism computation to reproduce, rather than a uniform closed-form structural argument. Independent expert audit and a fully exhaustive historical literature review have not been performed. Closest inspected primary texts: Newman (arXiv:cond-mat/0205009, pp. 1–3, 8), Holme (arXiv:1708.06456, pp. 1–3); Takeuchi–Yamamoto (2006) was assessed from the accessible abstract.

Self-review: passed. Independent audit: not yet performed.
