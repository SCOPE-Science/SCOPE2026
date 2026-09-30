# Independent audit — 2026-09-30

Record: `2026/09/19/szeged-wiener-equality-near-complete-graphs--9ebf1703573f`  
Assigned and audited source tree: `5e3cdfcd5790e5810562561a1a85f2efcedacc9e`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `67aa55709321c40c6fca0370286366df950236d2`  
Disposition: **repaired**

## Correctness

**independently_reproduced**. The three four-parameter formulas and the equality classification are correct. Direct reconstruction from the Venn-cell parameters, all-pairs distances, and the defining Szeged edge counts produced no formula failures in an independent finite exhaustive check. The exact Diophantine case split under the two-connectivity constraints leaves the Zhang–Li family for every n>=10 and only one additional n=10 isomorphism type. These formulas agree exactly with the earlier 18 September SCOPE theorem after exchanging the labels for the 'both' and 'neither' neighborhood classes.

## Originality

**requires_provenance_repair**. The original separate-originality claim is not sustainable against repository chronology. `2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8` was committed at 2026-09-18 03:47:31 UTC and already contains the same high-clique theorem, formulas and n=10 exception. This record first appeared at 2026-09-19 09:46:00 UTC. It is therefore retained as a later alternate derivation and reproducibility package, with no separate discovery-priority claim. The external Zhang–Li paper still poses the general equality classification problem.

## Scientific value

**useful_corroborating_rederivation**. After provenance correction, the record remains valuable as an independently written proof and verifier for a nontrivial structural slice of the Zhang–Li problem, but it is corroborative rather than a separate SCOPE advance beyond the earlier 18 September theorem.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/c0fc87c28df975025d87707c9327bc68127a1d1c
- https://arxiv.org/abs/2609.20025
- https://arxiv.org/abs/1602.05184
## Limitations

- No separate originality claim remains relative to the earlier SCOPE record.
- The theorem covers only graphs containing an (n-2)-clique.
- The global Zhang–Li equality problem remains open.
- Finite computation supports but does not replace the symbolic proof.
