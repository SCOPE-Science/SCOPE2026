# Independent audit — 2026-09-30

**Record:** `2026/09/20/tricolored-sum-free-developed-perfect-hash-families--337bc2288032`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `ce6c888e802e4e4ee25e559f18337b293026c9b1`  
**Disposition:** **PASSED**

## Correctness — PASS

The forward and converse correspondences were checked algebraically. Tri-colored sum-freeness forces injectivity of each coordinate list, so two distinct developed columns collide in at most one row. If three columns were unseparated, the three row collisions use the three different column pairs and eliminating translations gives an off-diagonal relation x_i+y_j+z_k=0, impossible. Conversely, normalized orbit representatives (0,r_i,s_i) produce (-s_i,r_i,s_i-r_i); repeated derived coordinates contradict the PHF property after an appropriate translate, and any all-distinct off-diagonal zero-sum relation explicitly constructs three unseparated columns. Hence k=|G|M_3(G) exactly. The fixed-characteristic exponent follows by direct substitution of the known tri-colored sum-free upper/lower rates. Kable–Mills–Wright's 2026 open preprint confirms that the 20 nonzero fourth powers in F_81 form a cap, yielding 81*20=1620 columns in the stated specialization; the repository verifier checks the finite field, cap and PHF conditions exhaustively.

## Originality — PASS (literature-bounded)

Walker–Colbourn (2007) is established prior art for perfect hash constructions from three-term-progression-free sets; its bibliographic record explicitly lists three-term arithmetic progression as a keyword. The assigned theorem recovers that one-colored construction as a special case but identifies the full diagonal-translation-developed class with arbitrary tri-colored sum-free sets. Searches combining perfect hash families with tri-colored/tricolored sum-free, group-developed, induced-matching and translation-orbit terminology did not locate the exact bijection or capacity identity |G|M_3(G). The finite F_81 example is not used as a global-current-record claim, avoiding dependence on inaccessible historical parameter tables.

## Scientific value — PASS

The structural equivalence transfers both upper and lower bounds from additive combinatorics into an exact capacity theorem for a natural symmetry class of PHFs, and it shows that diagonal development causes a genuine exponent loss relative to unrestricted near-quadratic three-row PHFs. The F_81 construction is a concrete reusable illustration.

## Evidence and literature

- Walker and Colbourn, Perfect Hash Families: Constructions and Existence (2007): https://doi.org/10.1515/JMC.2007.008
- Kleinberg, Sawin and Speyer, The Growth Rate of Tri-Colored Sum-Free Sets (2018): https://doi.org/10.19086/da.3734
- Kable, Mills and Wright, Subgroups of Finite Fields As Cap Sets (2026): https://arxiv.org/abs/2604.26989

## Limitations

- The exact correspondence is specific to three rows/strength three and diagonal translation symmetry.
- The asymptotic exponent is a statement about this developed subclass, not unrestricted perfect hash families.
- The historical PHF parameter tables were not fully inspected, so the 1620-column example is not asserted to be the current global v=81 record.

The independent audit finds the record scientifically complete on correctness, originality, and value at the audited tree. The originality verdict is bounded by the literature access and searches described above and does not treat inaccessible material as read.
