# Review of the sharp non-completeness mixing obstruction

## Correctness — PASS
The sharp lower bound is an operator-norm consequence of any unsupported offdiagonal entry: with centered coordinate vectors of norm squared \((n-1)/n\), a required zero transition has centered entry \(-1/n\). Equality forces an exact centered column identity, and two missing edges sharing a vertex would impose two incompatible columns. The explicit matching-deletion kernel is checked algebraically for feasibility; its invariant-space decomposition proves the full real spectrum is contained in \(\{1,1/(n-1),-1/(n-1),0\}\). The exact rational checker evaluates 224 independent parameter pairs but does not replace the general proof. The feasible matrix polytope is compact, so strictness beyond the matching class follows.

## Originality — PASS, subject to literature risks
The defining FMMC semidefinite problem is due to Boyd–Diaconis–Xiao (2004). The 2009 edge-transitive formula of Boyd–Diaconis–Parrilo–Xiao already implies the complete graph minus a **perfect matching** special case; this is acknowledged as prior coverage. Their edge-transitive theorem does not establish the **iff** classification among all incomplete graphs or cover general partial matching deletions directly. A 2025 broad clique-lift/subgraph FMRMC treatment was compared at its full-text relevant sections without finding an equivalent universal characterization. Published-record semantic searches and accessible previous claim comparisons found no implication-equivalent statement. A hidden corollary of an earlier SDP duality or spectral completion theorem remains the main originality risk; failed searches alone cannot settle that issue.

## Mathematical value — PASS
The complete extremal classification answers a natural network design question: which noncomplete communication graphs can mix as quickly as the fastest possible graph with one lost link? It shows that deletion of any matching is no worse, in optimized SLEM, than one missing link, but any two lost links sharing a node force a strict slowdown. This is a topology-wide structural law, not a numerical table, arbitrary slice, or renaming of the standard SDP.

## Scope and limitations
Holding loops are permitted; all transition matrices are symmetric, stochastic, and real. No results are claimed for nonreversible transition kernels or other notions of finite-time mixing. The classification does not parametrize all optimal matrices. The equal-value perfect-matching-deleted special case is not newly established relative to published edge-transitive graph theory.

Self-review: passed. Independent audit: not yet performed.
