# Independent audit — 2026/09/09/054

## Correctness — PASS

The seven listed triples cover the 21 core pairs once; adjoining distinct private vertices produces seven 4-edges on 14 vertices, each two meeting in one core vertex. Independently, a linear 4-graph has at most $binom(n,2)/6=n(n-1)/12$ edges by pair packing. For random 4-sets with probability α/n², the union bound over shared pairs gives at most $binom(n,2)binom(n-2,2)^2/2≤n^6/16$ conflicting pairs. Each labelled embedding of F+ has probability p^7, and there are at most n^14, so expected copies ≤α^7. Greedily removing an edge from every surviving conflict or copy costs at most the initial Y+Z. At α=1/3, independent rational arithmetic yields α/24−α²/16=1/144 and α^7=1/2187; $binom(n,4)≥(n^4−6n^3)/24$ establishes the stated finite inequality. This proof does not depend on the illustrative detector or a claimed limit.

## Originality — PASS, narrowly

The explicit constants for this particular 4-uniform Fano expansion are a direct, elementary instance of standard random alteration and pair packing. I found no matching numerical window in the checked open prior works. The Fano-plane Turán theorem concerns unrestricted 3-graphs, and Pikhurko's expanded complete-graph results concern a different forbidden family. The record's broad “first” claim is not established by a comprehensive literature search, and its method is not novel.

## Scientific value — PASS, limited

This gives a valid positive quadratic lower bound and universal upper bound for a precisely defined forbidden configuration. The factor-12 gap, absence of limit existence, and lack of stability sharply limit its reach. The exact density conjecture remains unsupported by the argument.

## Sources and scope

- Record RESULT.md, METADATA.json, and reproducibility descriptions; independent combinatorial and rational checks above.
- Bellmann–Reiher, *Turán's Theorem for the Fano plane*, https://arxiv.org/abs/1804.07673 .
- Pikhurko, *Exact Computation of the Hypergraph Turan Function for Expanded Complete 2-Graphs*, https://arxiv.org/abs/math/0510227 .
- Linear Turán numbers context, https://arxiv.org/abs/2607.16854 .
