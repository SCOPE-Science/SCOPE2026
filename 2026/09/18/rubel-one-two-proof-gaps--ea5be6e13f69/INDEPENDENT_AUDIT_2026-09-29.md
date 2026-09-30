# Independent audit — 2026-09-29

**Record:** `2026/09/18/rubel-one-two-proof-gaps--ea5be6e13f69`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The record identifies two genuine, logically independent gaps in arXiv:2609.20607v1. The source's Theorem 1.1 and its reverse metric implication are explicitly restricted to simply connected domains, while the proof of Theorem 1.4 starts from an arbitrary Rubel(1) domain and asserts finite inner diameter from the wrong implication direction. Independently, for u=Re f along an arc-length curve gamma, u_ss=Re(f''(gamma) gamma_s^2+f'(gamma) gamma_ss); the curvature term prevents large second tangential derivative from forcing large |f''|. Recalculation of the record's example f(z)=z^2, gamma(t)=t+i sin t at t=2*pi*n+pi/4 gives u_s=sqrt(2/3)(2t-1) and u_ss=(4t+10)/9 while f''=2.

## Originality

**PASS** — The arXiv record still has only v1 as of 2026-09-29, and the current full HTML continues to state Theorem 1.4, Rubel(1)=Rubel(2), with the same two disputed steps. Searches for the arXiv identifier, theorem wording, correction, erratum, and curvature terms did not locate a public correction or earlier discussion of these specific gaps. Originality is therefore accepted for the source-specific diagnosis, not for the elementary path-integral lemma or chain rule.

## Scientific value

**PASS** — The defects occur in a newly stated equality between the first two Rubel classes and in the immediate geometric corollary. Pinpointing the invalid implication and the missing curvature term prevents those conclusions from being treated as proved and supplies an explicit obstruction that any repair must address.

## Independent checks

- Read the current arXiv v1 HTML at the theorem statements and Section 5 proof: lines around Theorem 1.4 explicitly infer finite inner diameter for an arbitrary Rubel(1) domain and then infer |f''| from the second derivative of a restriction.
- Re-derived the arbitrary-domain easy direction finite inner diameter => Rubel(1) by the last-level-crossing/path-integral argument and confirmed it does not yield the converse used in the source.
- Symbolically differentiated u(t)=t^2-sin^2 t using ds/dt=sqrt(1+cos^2 t), reproducing the record's u_s and u_ss values at t=2*pi*n+pi/4 while f'' remains constant.

## Findings

- The source proof currently contains both identified gaps; no later arXiv revision was present at audit time.
- The record correctly limits its conclusion to failure of the presented proof rather than falsity of Rubel(1)=Rubel(2).
- The explicit smooth bounded-curvature example is a valid counterexample to the second-order inference used in the proof.

## Literature evidence

- https://arxiv.org/abs/2609.20607 — MacMahon preprint; current arXiv entry shows only v1, submitted 17 September 2026.
- https://arxiv.org/html/2609.20607v1 — Current full HTML inspected, including Theorems 1.1/1.4 and the complete Section 5 proof.
- https://doi.org/10.1112/S002557930001490X — Hinchliffe (2003), background on unbounded analytic functions on plane domains; not needed for the source-local proof-gap finding.

## Limitations

- This audit does not prove the equality Rubel(1)=Rubel(2) false and supplies no counterexample to the equality.
- A future revision may repair the theorem by a different argument.
- No novelty is claimed for the chain rule or the elementary finite-inner-diameter implication themselves.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
