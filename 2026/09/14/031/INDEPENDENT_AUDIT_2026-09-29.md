# Independent audit — 2026-09-29

Record: `2026/09/14/031`  
Audited source tree: `6fa4a237686fe26eccad02756441022df2478c87`  
Disposition: **passed**

## Correctness

The finite-window claim is correct. The archived exact endpoint logs satisfy crossed+uncrossed=200^144 at both p=99/200 and p=101/200. Independently rechecking the logged integers gives 4*C(99,101)-200^144>0 and 3*200^144-4*C(101,99)>0, with both strict margins 332 digits long. Because left-right crossing is increasing in p, these endpoint certificates imply 1/4 < P_p(Cross) < 3/4 throughout [0.495,0.505]. The transfer-state design retains frontier connectivity and persistent left/right-touch flags, which is sufficient for exact two-terminal crossing enumeration.

## Originality

Transfer-matrix and connectivity-state methods for finite percolation/reliability are established, and exact finite-lattice percolation polynomials have been computed in prior work. This audit did not locate the same 8x8 bond-crossing endpoint certificate in the checked literature, but search non-detection is not a priority proof. The contribution is best viewed as an exact finite benchmark, not a new percolation method.

## Scientific value

The exact rational endpoint certificate gives a rigorous finite-scale instance of near-critical stability and is useful as a reproducible benchmark. Its scope is intentionally finite and it does not improve asymptotic RSW or scaling-window theory.

## Limitations

- The proof is computer-assisted and depends on the correctness of the short exact-integer transfer program plus its archived cross-checks.
- The RESULT and METADATA reproducibility paths use the stale prefix output/artifacts/, while the audited files are actually under artifacts/; this is a packaging defect, not a defect in the endpoint certificate.
- No claim is made that these are the first published exact 8x8 bond-crossing endpoint values.
- The result is for one finite 8x8 vertex box and does not constitute a new asymptotic near-critical theorem.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/031
- https://arxiv.org/abs/2204.01517
- https://doi.org/10.1103/PhysRevE.54.2547
- https://doi.org/10.1214/EJP.v13-565
