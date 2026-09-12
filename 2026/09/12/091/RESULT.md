# Universal Local-Clifford Equivalence of Three-Ququart Stabilizer AME States to Weighted Graph States

## Context

Three-qudit stabilizer states over prime-power local dimension exhibit torsion
phenomena absent for prime dimensions: stabilizer modules over Z_4 need not be
free, and not every ququart stabilizer state is local-Clifford (LC) equivalent
to a graph state. Absolutely maximally entangled (AME) states of three
ququarts — pure states in (C^4)^{⊗3} with all three single-party reductions
maximally mixed I/4 — form a natural test class: either every stabilizer AME
state is LC-equivalent to a weighted graph state, or some stabilizer AME
module furnishes an explicit counterexample. Prior work (prime-dimension
stabilizer-to-graph theorems; Helwig AME qudit graph-state constructions;
Looi–Griffiths squarefree tripartite structure) does not decide the Z_4 case.

## Definitions

- Phase space V = Z_4^6 with vectors (x|z) = (x_1,x_2,x_3|z_1,z_2,z_3) and
  symplectic form ⟨(x|z),(x′,z′)⟩ = z·x′ − x·z′ ∈ Z_4.
- A pure three-ququart stabilizer state has stabilizer group S of order 64
  with trivial phase intersection; its module M = S/{phases} ⊂ V has |M| = 64
  and is maximal isotropic, hence M = M^⊥.
- Weighted graph module: row-span of [I|Γ] with Γ = Γᵀ ∈ M_3(Z_4) and
  Γ_ii = 0. Every graph module is free (≅ Z_4^3) with torsion number
  t(M) = #{v ∈ M : 2v = 0} = 8.
- Local Cliffords act as Sp(2,Z_4) = SL(2,Z_4) per site; they preserve t(M),
  so no LC image of a graph state has t(M) > 8.
- AME at module level: M contains no nonzero vector of support-weight ≤ 1,
  equivalent to all single-party reductions equal to I/4.

## Result

Every pure three-ququart stabilizer AME state is local-Clifford equivalent to
a weighted graph state. Equivalently: every maximal-isotropic AME module
M ⊂ Z_4^6 is free (M ≅ Z_4^3, t(M) = 8), and every free maximal-isotropic
module is LC-equivalent to a weighted graph module [I|Γ]. Residual generator
phases are absorbed by a local Pauli. Consequently no stabilizer-AME
counterexample exists. Explicit criterion: compute t(M); AME forces the free
value 8, and the mod-2 symplectic pattern plus diagonal shears below gives the
graph form and the local Clifford explicitly.

## Proof / Evidence

Lemma 1 (freeness): Let K = M ∩ 2V, U = halve(K) ⊂ F_2^6 (dim k,
t(M) = 2^k), W = π(M) ⊂ F_2^6 (dim m, k+m = 6). Then W is isotropic and
W = U^⊥, so U is coisotropic, m ≤ 3, k ≥ 3. AME implies U is clean
(no weight-≤1 vector). Cases k ≥ 4 (m = 0,1,2) are impossible: m=0 gives
U = F_2^6; m=1 gives U = w^⊥ containing a weight-1 vector at every site;
m=2 uses per-site determinants δ_i = z_{1i}x_{2i}+x_{1i}z_{2i} with
Σδ_i = ⟨w_1,w_2⟩ = 0, while cleanliness would force all δ_i = 1, i.e. sum 3 = 1
(mod 2), a contradiction. Hence k = 3, |K| = 8, and with |M| = 64 this forces
M ≅ Z_4^3. Exhaustive F_2 checks confirm: all 315 planes and 63 lines have
weight-1 vectors in their annihilators.

Lemma 2 (graph reduction): For a free basis [X|Z], the mod-2 image is a
Lagrangian plane (kernel M ∩ 2V = 2M has 8 elements). By induction on sites
using the transitive S_3 ≅ Sp(2,F_2) action, some local pattern makes the
X-block invertible (unitriangular up to row order). The pattern lifts to
SL(2,Z_4) (maps (x,z)↦(z,−x) and (x,z)↦(x+z,z)), giving odd, hence unit,
determinant over Z_4. Row-reduce to [I|Γ′]; isotropy gives Γ′ symmetric; local
shears (x_i,z_i)↦(x_i,z_i−Γ′_{ii}x_i) kill the diagonal. All 135 F_2
Lagrangians admit such a pattern (exhaustion); 300/300 random free Z_4
Lagrangians (150 AME) reduce with module equality verified.

Lemma 3 (phases): For graph Paulis P_j with phases ω^{c_j}, conjugation by a
local Pauli shifts c_j by s_j − (Γt)_j with s ranging over all of Z_4^3, so
t=0, s=−c kills all phases; the zero-phase graph group is valid by freeness.

Witness: Γ = K_3 with all weights 1 gives generators g_i = X_i∏_j Z_j^{Γ_ij}
with module size 64, torsion 8, min support-weight 2, and Hilbert-space
verification (64-dim matrices): commuting generators, 64 distinct Paulis,
rank-1 projector, all three reductions I/4.

## Limitations

Specific to three ququarts over Z_4 with maximal-isotropic modules of order
64; the determinant argument uses three sites. Uses standard finite-symplectic
facts (|M|·|M^⊥| = |V|; pure stabilizer groups of order 64). Random-sampling
checks support but do not replace the analytic proof; mod-2 enumerations are
exhaustive at the F_2 level.

## Reproducibility

Run output/artifacts/verify_freeness.py (F_2 freeness), verify_reduction.py
(K3 AME check plus 300 graph reductions), verify_enumeration.py (135
Lagrangians plus 40k Z_4 samples), verify_hilbert.py (numpy Hilbert-space AME
verification). All scripts are deterministic up to stated random seeds.

## References

- W. Helwig, Absolutely Maximally Entangled Qudit Graph States,
  arXiv:1306.2879 (2013).
- S. Y. Looi and R. B. Griffiths, Tripartite entanglement in qudit stabilizer
  states, Phys. Rev. A 84, 052306 (2011).
- Y. Wong and L. Jiang, Local unitary decomposition of tripartite arbitrary
  leveled qudit stabilizer states, arXiv:2507.09416 (2025).
- M. Van den Nest, J. Dehaene, B. De Moor, local-Clifford equivalence and
  invariants of stabilizer states, Phys. Rev. A 71–75 (2005–2007).
