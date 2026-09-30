# Independent audit — SCOPE-20260913-012

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
With L0 fully infected, a healthy v in L1 always has an infected neighbour on the e5 axis. Its upper neighbour is on the same axis and therefore cannot supply a second distinct axis. Thus the distinct-axes rule infects v exactly when an in-layer neighbour on one of e1,…,e4 is infected. L1 is therefore exactly r=1 bootstrap on the connected 4D torus, so it fills iff its initial set is nonempty and the exact failure probability is (1-p)^A.

For the standard two-neighbour rule with the upper layer frozen at its initial Bernoulli state, a single seed in L1 or a single occupied helper directly above a site starts the same connected-layer cascade, so frozen failure is exactly (1-p)^(2A); allowing full upper-layer dynamics can only reduce failure. The surface calculation is also exact: for a box (L,L,L,L,γL) at fixed V=γL^5, area coefficient is (8γ+2)γ^(-4/5), giving 18·2^(-4/5)≈10.3383 at γ=2, versus 10 for the cube.

### Originality
Limited. The claims are elementary finite-volume consequences of the update rule and rectangular surface arithmetic. The record wisely does not claim the unresolved sharp-window theorem.

### Scientific value
Moderate as a clean exact local-growth lemma and as a correction to the proposed γ=2 isoperimetric heuristic; limited as a global threshold result.
