# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/maximum-frobenius-dimension-quasi-hereditary-nakayama-algebras--c3d406cc8108`  
Assigned and audited source tree: `55c3fd3072fa0727106c0267ca876bddbeab141b`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `718f4f5ee4fac6a811deec1c56b2d6f9e70a24e6`  
Disposition: **passed**

## Correctness

**independently_supported**. The uniserial-Hom proof is sound. For a cyclic quasi-hereditary Nakayama algebra without a simple projective, Uematsu--Yamagata Proposition 3.1 guarantees a simple of projective dimension 2. Writing rho_i=i+c_i, the second-syzygy projectivity identity forces rho_a=rho_1 for a=c_0, hence a plateau rho_1=...=rho_a. Periodicity rho_{i+n}=rho_i+n gives a<=n, while comparison with rho_n gives the second plateau parameter b<=n. Consequently all projective and injective lengths are at most 2n-1, and the long injectives have the common top S_1. The standard uniserial Hom formula then allows dimension 2 only for a long source and target; only P_1 can contain S_1 twice, and only I_{q-1} admits both occurrences. Thus at most one of the n^2 Hom(I_s,P_j) summands has dimension 2 and all others have dimension at most 1, proving F(A)<=n^2+1. For the family (2,n+1,n,...,3), direct recomputation for n=2,...,7 gives totals 5,10,17,26,37,50 with exactly one two-dimensional Hom summand, matching n^2+1.

## Originality

**qualified_supported**. The 2020 MathOverflow question explicitly asks for this maximum, lists 5,10,17,26,37,50,65, and conjectures n^2+1. The classical Uematsu--Yamagata paper supplies the projective-dimension-2 quasi-heredity criterion, and Marczinzik--Sen treats homological characterizations and global-dimension bounds rather than Frobenius dimension. The July 2026 preprint Bounds on Frobenius dimension gives general vector-space-dimension bounds and path-algebra formulas; its advertised scope does not contain the Nakayama extremal theorem. Targeted current searches did not locate the n^2+1 theorem or the unique-double-Hom mechanism. Originality is therefore supported to the best of current evidence, with residual risk from older serial-ring literature under different terminology.

## Scientific value

**meaningful_exact_extremal_resolution**. The theorem resolves an explicit six-year-old extremal question for every n>=2, gives a uniform sharp family, and supplies a structural reason for the simple formula rather than only extending the finite sequence.

## Independent checks

- Inspected Uematsu--Yamagata Proposition 3.1 in lawful open full text; it states that a connected serial Artinian ring is quasi-hereditary iff it has a simple projective or a simple module of projective dimension 2.
- Re-derived the lifted-Kupisch plateau and length bounds.
- Reimplemented the uniserial Hom count for the sharp family and obtained n^2+1 for n=2 through 7 with one and only one dimension-2 summand.
- Checked the current MathOverflow statement and the scope of the 2026 Frobenius-dimension preprint.

## Literature and evidence checked

- https://mathoverflow.net/questions/351323/frobenius-dimensions-of-nakayama-algebras
- https://www.math.sci.hokudai.ac.jp/hmj/page/19-1/pdf/HMJ_19_1_1990_165-174.pdf
- https://arxiv.org/abs/2109.03441
- https://arxiv.org/abs/2607.15999
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/maximum-frobenius-dimension-quasi-hereditary-nakayama-algebras--c3d406cc8108
## Limitations

- Split basic finite-dimensional Nakayama algebras only.
- The theorem resolves the maximum problem, not the separate lower-bound question F(A)>=gldim(A).
- The originality assessment remains subject to older or unindexed serial-ring literature that may use different terminology.
