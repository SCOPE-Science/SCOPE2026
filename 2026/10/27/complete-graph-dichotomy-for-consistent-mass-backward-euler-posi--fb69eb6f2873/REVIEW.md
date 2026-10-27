# Scientific review

## Correctness — PASS

Exact edgewise assembly yields \(M=\ell(2D+A)/6\) and \(K=(D-A)/\ell\). Above \(t=\ell^2/6\), the backward Euler system is a Stieltjes matrix, so its inverse times the nonnegative consistent mass is nonnegative. Below that threshold, hypothetical nonnegativity forces the inverse system matrix to be a Stieltjes matrix; its irreducibility forces its own inverse to be strictly positive, contradicting an off-diagonal zero from any missing graph edge. The complete-graph spectral formula proves the exception independently. The proof covers every graph size and real step size. Reproduced code checked all 995 connected graph-atlas cases on two to seven vertices across 11 steps, 330 exact rational tests, and four symbolic complete-graph examples. No finite sweep is treated as an infinite proof.

## Originality — PASS, with residual risk

Compared the exact *implication* of the claimed two-branch theorem against the accessible research history, public mathematical-result indexing, and two inspected primary preprints. Li–Huang (2012) supply sufficient mesh/step conditions for planar and higher-dimensional FE settings; Jin–Lazarov–Thomée–Zhou (2015), especially Theorems 4.1–4.3, establish small-step failures under their mesh assumptions and a Stieltjes-based sufficient threshold. Their results explain the sufficient half but do not imply the exact necessity for every noncomplete connected metric network at *all* steps below the boundary, nor the complete-graph exception. Special-family results on chains, trees and complete bipartite graphs concern narrower graph classes, and cannot imply the universal dichotomy. The classical inverse-Stieltjes lemma is acknowledged as known, not claimed new. Residual risk: potential specialized or unindexed full classifications, especially older work by Thomée–Wahlbin (full text unavailable here); independent review could alter originality judgment.

## Value — PASS

The central question is physically natural: when can a consistent-mass FE update of network heat diffusion create negative nodal temperatures despite nonnegative initial data? The theorem replaces topology-by-topology eigenvalue computations with a universal sharp threshold and an unexpected exact exception determined only by graph completeness. It immediately gives a scheme-selection rule for equilateral branched, cyclic and densely connected metric networks, and exhibits a nontrivial structural obstruction via inverse-positive matrix theory. This is more than a numerical table, a renamed inequality, or a routine isolated specialization; it is a complete classification for a broad natural graph family.

## Limitations and closest literature

The proof is specific to equal edge lengths, unit edge diffusivity, nodal continuous piecewise-linear FE, consistent mass and all-Neumann metric coupling. Other graph discretizations and heterogeneous lengths are outside scope. Li–Huang 2012 and Jin et al. 2015 are closest inspected mathematical texts; the 2008 Thomée–Wahlbin work was identified but only its abstract was available. The embedded checker supports, but does not substitute for, the infinite proof. No claim of external certification is made.

Self-review: passed. Independent audit: not yet performed.
