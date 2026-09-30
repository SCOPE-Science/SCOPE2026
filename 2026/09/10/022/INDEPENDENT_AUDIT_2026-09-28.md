# Independent audit — 2026-09-28

Record: `2026/09/10/022`  
Audited tree: `2bb816a4a3f46711fa4eb5d5e196fa7184bf0f59`  
Disposition: **passed**

## Correctness
The core finite claims survive an independent reconstruction. I rebuilt the five named Steiner triple systems, checked the Steiner pair axiom, and independently enumerated sails. The counts are 28, 72, 260, 420, and 912. A fresh NAE-constraint DPLL search found sail-free 2-colourings for orders 7, 9, 13, and 15 and an UNSAT result for the named cyclic STS(19). These checks do not rely on the repository's archived DPLL trace.

## Originality
Granath et al. identify the sail as the remaining small configuration in the relevant program, and Sárközy's later paper still poses the sail Ramsey question. I did not locate a prior source giving this exact named-family 7/9/13/15 witness plus cyclic-19 forcing certificate. That supports originality of the finite certificate only; it is not a proof that no earlier unpublished or differently phrased computation exists.

## Scientific value
The record supplies a reproducible finite benchmark, explicit lower-order witnesses, and a certified named STS(19) obstruction. This is scientifically useful evidence, but it is much weaker than the general sail 2-Ramsey question and the record states that limitation correctly.

## Limitations
The audit does not promote the named cyclic STS(19) statement to all STS(19) or to an asymptotic theorem. The literature search was targeted rather than exhaustive.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/022
- https://doi.org/10.1002/jcd.21585
- https://real.mtak.hu/162638/
- https://arxiv.org/abs/2305.01193
