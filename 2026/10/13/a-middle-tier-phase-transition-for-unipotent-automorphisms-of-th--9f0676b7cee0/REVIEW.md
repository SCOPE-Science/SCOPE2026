# Self-review

## Correctness — PASS

For every \(a,b\ge2,c\ge1\), the proof begins with all primitive normal rays of the chain-polytope fan. The character inequalities for coordinate rays force the indicated complete root lists, and the inequalities for triple rays exclude all other roots. The bracket computation uses the actual Demazure derivation formula, not a guess from root counts; its squarefree-deletion structure proves both the abelian/vector-group split and the exact lower-central-series length \(\max(a,b)+1\). The only finite computations used are the separately replayed bounded exact enumerations in the included checker, which do not replace the infinite proof.

## Originality — PASS, with stated residual risk

The comparison was made at implication level against the full-text general results of Nill (arXiv:math/0407491v1, Section 2), the chain-polytope and order/chain equivalence paper of Hibi and Li (arXiv:1208.4029v1, Sections 1–2), and the automorphism/column-vector survey of Bruns and Gubeladze (arXiv:math/0002024, Section 3). Those works provide the method and relevant polytope background but not the explicitly calculated three-tier root sets or group nilpotency class. Related searchable results on poset algebras, general toric automorphisms and other Demazure models do not imply this formula from their published assertions. The original Stanley paper was only partly accessible in the consulted transcription and its full text was not used to declare absence of specialized theorems. Equivalent unindexed studies of this exact family remain a residual possibility; failed searches alone do not prove novelty.

## Value — PASS

For a natural infinite family already motivated by the classical chain/order-polytope correspondence, the theorem describes the entire connected automorphism group, not merely a dimension bound. The single-element middle tier creates exponentially many root groups and arbitrarily large unipotent nilpotency class, while adding one middle element collapses the radical to an abelian vector group. The sharp structural boundary is a substantive automorphism invariant and provides a concrete comparison point for toric degenerations and symmetry of poset polytopes.

## Scope and verification limits

The result assumes complex base field and outer tiers at least two, concerns the chain-polytope toric variety (not the order-polytope model), and does not identify the disconnected automorphism group. Programmatic checks cover \(30{,}861\) vectors in bounded boxes over eleven parameter triples; all claims for arbitrary parameters follow by the symbolic fan and Lie calculations. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
