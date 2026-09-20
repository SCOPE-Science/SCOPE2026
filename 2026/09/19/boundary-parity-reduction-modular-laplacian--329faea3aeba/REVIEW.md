# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The key identities are exact consequences of modular arithmetic and integer-linearity of the mask Laplacian.

For even \(k\), standard reduction satisfies \([x]_k\equiv x\pmod2\) for every integer \(x\). Therefore \(K_kv\equiv L_Mv\pmod2\) for arbitrary integer-valued \(v\), and applying one binary Laplacian gives \(B(K_kv)=B^2v\).

For binary \(u\), \((L_Mu)(p)\in[-d,d]\). At an inactive site the Laplacian is nonnegative; at an active site it is negative exactly when at least one mask neighbor is inactive. Thus \(\mathbf1_{\{L_Mu<0\}}=\partial_Mu\). For \(k>d\), standard residues are \(x\) for \(x\ge0\) and \(k+x\) for \(x<0\), so parity differs from \(x\) exactly by \((k\bmod2)\partial_Mu\). Applying the binary Laplacian \(r\) times gives the stated boundary-forcing formula by linearity over \(\mathbb F_2\).

The support identity follows because every nonzero \(L_Mu(p)\) has magnitude strictly below \(k\), and therefore cannot reduce to zero modulo \(k\). The finite-speed inclusion follows from the locality of one mask-Laplacian update. The schedule corollaries are induction over successive binary checkpoints.

The compact verification artifact checks the scalar identities across many degrees and moduli, exact even erasure on binary and non-binary integer test states, the boundary formula for several masks, support invariance, finite-speed localization, and representative \([2,k,2^{\times s}]^\infty\) schedules. These computations support reproducibility but are not independent validation.

## Originality

**PASS, to the best of our knowledge, for the narrow source-specific refinement.** arXiv:2609.20416v1 was inspected at the model definition and Section 3.4.1 theorem/proof level. Its Lemma 3.1 already proves that odd \(k,\ell>d\) produce the same parity from binary input and hence the same state after the next binary update; it also explicitly predicts a common higher-odd class. Those facts are prior work and are excluded from the novelty claim.

The source describes even insertions as binary-like but does not state the exact identity \(B K_k=B^2\) for every even \(k\), including moduli at or below the mask degree and arbitrary integer-valued input. It also does not identify the odd correction with the inner active boundary, derive \(B^rK_ku=B^{r+1}u+B^r\partial_Mu\), prove boundary-layer localization, or formulate the resulting parity-word quotient of insertion schedules.

The earlier arXiv:2509.05815v1 was inspected in its alternating and mixed-schedule sections. It reports an empirical even/odd dichotomy and binary-like behavior for even insertions, but no exact erasure or boundary-forcing theorem was found.

External searches using the exact source identifier and combinations of `modular Laplacian`, `parity`, `even insertion`, `odd modulus`, `binary update`, `boundary`, and `mask degree` located the source paper and earlier papers in the same series but no earlier statement of the exact even-erasure or boundary-pulse identities. Repository searches by the source identifier and claim terminology found no prior SCOPE record covering this result.

Residual originality risk remains because the core algebra is elementary once one explicitly projects the inserted state modulo \(2\); an unindexed note or a result stated in different terminology could contain an equivalent observation. No inaccessible paper was identified as a particularly close candidate likely to overturn the source-specific claim.

## Value

**PASS.** The source's main empirical dichotomy is that even insertions remain binary-like while odd insertions can sustain qualitatively different high-density regimes. The exact erasure theorem upgrades the even side from a visual or statistical resemblance to an identity at every binary checkpoint. The boundary formula simultaneously gives a geometric mechanism for the odd side: above the mask-degree threshold, the entire deviation from the binary reference is an evolving pulse emitted by the active boundary. This yields exact all-time schedule equivalence classes and a finite-speed localization statement that can be reused in later analysis of seed-size and geometry effects.

## Limitations

The explicit boundary-pulse formula for odd moduli assumes binary input and \(k>d\). It does not classify small odd moduli such as \(k=3\) for degree-four masks, where multiple wrapping and configuration-specific coincidences can occur. The locality result does not by itself prove a decay estimate, carpet persistence, or long-time aperiodicity. The originality assessment is not independent validation.
