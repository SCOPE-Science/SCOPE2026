# Independent Audit — 2026/09/10/027

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `135d553c02a151f4f72f0c88dd73a84061233ac6`  
**Audited current source tree:** `135d553c02a151f4f72f0c88dd73a84061233ac6`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. I independently recomputed the advertised envelope closure. For t>R0^{-2}, splitting at r=t^{-1/2} gives M(t)=R0^6 t^{-1/2}/6 - t^{-7/2}/42; for t<=R0^{-2}, M(t)=R0^7/7. Hence M(t)t^alpha is uniformly bounded exactly for alpha<=1/2 in the stated feasible range, so alpha=4-s' gives s'>=7/2. At s'=3 (alpha=1) the comparison ratio grows as t^{1/2}. The conclusion is correctly limited to this squared spectral-envelope bookkeeping and does not assert a Falconer theorem. The cited Raani--Singh preprint is openly available and does establish high-frequency decay for the Koranyi-sphere spectral coefficients; its n=1 proof exhibits the relevant quarter-power high-frequency scale. I did not re-prove that paper's uniform spectral estimate.

## Originality

SUPPORTED, NARROW. Raani--Singh's stated result concerns positive Koranyi upper density and high-frequency R_k decay, not this compact-set Mattila-envelope threshold calculation. A targeted search did not identify an earlier statement of this exact 7/2 closure calculation, but absence from search is not used as proof of novelty. The defensible originality is the explicit bookkeeping obstruction/criterion conditional on the cited decay, not a new distance-set theorem.

## Scientific value

MEANINGFUL ROUTE-DIAGNOSTIC VALUE. The calculation rules out the advertised s>3 closure for this particular spectral-transfer envelope and isolates the decay strength that a future proof would need. It is elementary once the decay and r^6 bookkeeping are fixed, so its value is primarily as a sharp obstruction/check rather than as a standalone major theorem.

## Limitations

- The Raani--Singh spectral decay is used as an external input and was not independently reproved here.
- No full Frostman/Mattila argument at s>7/2 is established; the record correctly says that remains open.
- The r^6/squared-envelope reduction is audited as the stated route bookkeeping, not as a proof that every possible Heisenberg Falconer method must obey it.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/027
- https://arxiv.org/abs/2507.14917
