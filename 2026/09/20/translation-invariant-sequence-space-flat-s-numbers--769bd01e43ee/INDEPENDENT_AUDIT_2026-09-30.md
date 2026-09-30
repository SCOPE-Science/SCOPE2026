# Independent audit — 2026-09-30

**Record:** `2026/09/20/translation-invariant-sequence-space-flat-s-numbers--769bd01e43ee`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `1af825082af918531461bf5c23a5f431807cffec`  
**Disposition:** **PASSED**

## Correctness — PASS

The disjoint-translate argument was reconstructed. A finitely supported near-norming vector u is translated so that both the input supports and suitably truncated output supports are pairwise disjoint. Choosing the tail errors in l_infinity (p=1), l_q (1<p<infinity), or l_1 (c_0) gives a copy E of l_p or c_0 on which ||Tx||>=(||T||-epsilon)||x||. The translated finite-support norming functionals define an explicit norm-one projection onto E, including the c_0 coefficient-vanishing check. This immediately forces distance ||T|| from the strictly singular ideal and hence from FSS and compact operators. The approximation and Bernstein identities follow directly; finite-codimensional intersection gives the Gelfand identity, and uniform tail smallness on a finite-dimensional quotient subspace plus a far translate of Tu gives the Kolmogorov identity. The translate-selection step excludes only finitely many group elements at each stage, so it works for arbitrary infinite discrete groups, not only countable or abelian ones.

## Originality — PASS (literature-bounded)

The closest source, Karlovych–Shargorodsky (2024), was first sought through open routes and then obtained through authorized institutional access; all 17 pages were inspected. Its main theorem proves maximal noncompactness (Hausdorff measure of noncompactness = essential norm = operator norm) for a broad class of translation-invariant sequence-space operators on Z^d. It does not state Bernstein/Gelfand/Kolmogorov flatness, distance to the FSS/strictly-singular ideals, or the 1-complemented almost-norming witness. The assigned record explicitly treats maximal noncompactness/essential-norm equality as prior art, so the stronger same-space s-number profile remains distinct in the checked literature.

## Scientific value — PASS

The record upgrades qualitative/noncompactness information to exact values of four classical finite-index s-number scales and three nested operator-ideal distances. The complemented almost-norming subspace is a reusable structural obstruction stronger than the numerical equalities alone.

## Evidence and literature

- Karlovych and Shargorodsky, Discrete Riesz transforms on rearrangement-invariant Banach sequence spaces and maximally noncompact operators (2024): https://kclpure.kcl.ac.uk/portal/en/publications/discrete-riesz-transforms-on-rearrangement-invariant-banach-seque/
- Edmunds and Lang, Notes on Non-Compact Maps and the Importance of Bernstein Numbers (2025): https://arxiv.org/abs/2503.19600
- Crombez and Govaerts, Towards a Classification of Convolution-Type Operators From l1 to linfinity (1980): https://doi.org/10.4153/CMB-1980-060-4

## Limitations

- The theorem is restricted to same-space operators on l_p(G), 1<=p<infinity, and c_0(G), and does not cover l_infinity(G).
- Maximal noncompactness and essential-norm equality themselves are prior art and are not original contributions of this record.
- Older multiplier/Fredholm literature may contain related disjoint-translate arguments under different terminology, so priority is literature-bounded rather than absolute.

The independent audit finds the record scientifically complete on correctness, originality, and value at the audited tree. The originality verdict is bounded by the literature access and searches described above and does not treat inaccessible material as read.
