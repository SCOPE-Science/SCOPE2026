# Independent audit — 2026-09-29
- Source: `2026/09/13/071`
- Assigned/current tree SHA: `18216d6eb6a8c528789bc71df57de739e4ef911a`
- Disposition: **repaired**

## Three-axis assessment

### Correctness

**PASSED** — The six-component computation checks exactly. The quadratic locus decomposes into C_i=L_i x {q_i} x L_i and D_i={q_i} x L_i x {q_i}; restriction of the two cubics to C_i gives one nondegenerate (1,1) equation, while every D_i is contained because each cubic monomial has a zero endpoint factor. The incidence is E_i-D_j iff i!=j. At P=(q_1,q_0,q_1), the affine Jacobian has rank exactly 4, hence tangent dimension 2 versus local dimension 1. The committed verification script and log agree.

### Originality

**PASSED** — De Laet treats the Heisenberg quotients and their infinite point modules, while Walton and the corrigendum treat truncated schemes for the unquotiented degenerate Sklyanin algebra. The submitted finite V_3(T_1) six-curve cut, its exact incidence and the rank-4 singularity certificate require imposing the two quotient cubics and are not formal consequences of those cited results.

### Scientific value

**PASSED** — The result gives an exact finite-level geometric invariant of a natural quotient: component equations, connectivity, incidence and a singularity certificate. It is narrow but structurally interpretable and reproducible. The repair corrects only the committed artifact paths and narrows priority wording.

## Independent checks

- reconstructed the pair and triple quadratic loci from disjoint-support conditions
- recomputed every cubic restriction to C_0,C_1,C_2 over w^2+w+1=0
- checked D_i containment monomial by monomial and all E_i-D_j intersections
- rederived the rank-4 Jacobian minor at P
- verified committed artifacts live under artifacts/ rather than output/artifacts/
- confirmed main has no changes under this record since the inventory commit

## Limitations

- Only t=1 and truncation level d=3 are audited.
- No claim is made for higher d or other quotient parameters.
- Open-access sources were sufficient; Oxford Download was not needed.

## Citations

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/071
- https://arxiv.org/abs/1510.04024
- https://arxiv.org/abs/0812.0609
- https://arxiv.org/abs/1112.5211
