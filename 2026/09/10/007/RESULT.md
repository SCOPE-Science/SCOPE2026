# No 4-fold Massey product at the Limonchenko–Panov reference complex: sharp order-3 boundary

## Context

The Golod vs higher-Massey hierarchy for moment-angle complexes asks, after the
Berglund–Jöllenbeck correction, how far non-formality extends beyond cup
products. Limonchenko–Panov (arXiv:2201.12779) constructed a reference
minimally-non-Golod complex with trivial cup product and one nontrivial triple
Massey product. The admitted target asked for a strictly defined nontrivial
4-fold Massey product with trivial indeterminacy and detector value 1 at that
same complex, on four pairwise-disjoint degree-3 classes. This record decides
that question negatively and sharply.

## Definitions

Fix $K_0$ as the simplicial complex of Limonchenko–Panov, arXiv:2201.12779,
Theorem 2, on vertex set $[9]=\{1,\dots,9\}$, defined by the 15 published
minimal non-faces (1-indexed, paper order):

$(1,2,3)$, $(4,5,6)$, $(7,8,9)$, $(1,4,7)$, $(1,2,4,5)$, $(5,6,7,8)$,
$(2,3,7,8)$, $(2,3,5,6,7)$, $(1,2,4,6,8,9)$, $(1,3,4,5,8,9)$,
$(1,3,5,6,7,9)$, $(2,3,4,5,7,9)$, $(2,3,4,5,8,9)$, $(2,3,4,6,7,9)$,
$(2,3,5,6,8,9)$.

$K_0 = \{\sigma \subseteq [9] : \sigma \text{ contains none of the above}\}$.
Let $Z = Z_{K_0}$ be the moment-angle complex. Work over $\mathbf{Q}$
throughout.

Support convention: a cohomology class is "supported on $J$" if it lies in
the image of $H^*(Z_{K_J}) \to H^*(Z_K)$, i.e. in the Hochster split summands
$I \subseteq J$. "Pairwise-disjoint supports" means the representing $J$'s
are pairwise disjoint.

Standard lemmas used: Hochster formula
$H^p(Z) \cong \bigoplus_I \tilde{H}^{p-|I|-1}(K_I)$ over $\mathbf{Q}$;
Massey degree $\deg\langle x_1,\dots,x_n\rangle = \sum |x_i| - n + 2$;
Baskakov disjointness rule (product of classes on $I,J$ with
$I \cap J \neq \emptyset$ is zero).

## Result

For $K_0$ as pinned above, with $Z = Z_{K_0}$ over $\mathbf{Q}$:

(A) $H^3(Z;\mathbf{Q}) = 0$. Hence no nonzero degree-3 quadruple
$(a,b,c,d)$ exists; the admitted degree-3 4-fold conjunction with detector
$\varphi(m)=1$ has no witness.

(B) Every nonempty homology support $I$ (i.e. $\tilde{H}_*(K_I) \neq 0$)
satisfies $|I| \geq 3$. Hence no four nonzero positive-degree classes with
pairwise-disjoint supports exist ($4 \times 3 = 12 > 9$). Exhaustively, among
the 61 nonempty homology supports there are exactly 0 disjoint quadruples
and exactly 1 disjoint triple: $\{123\},\{456\},\{789\}$ (the published
triple supports).

(C) Support-free degree gap: lowest positive cohomology degree is 5 and top
degree is 14, with
$\dim H^p = \{0{:}1, 5{:}4, 7{:}3, 8{:}10, 9{:}3, 10{:}4, 11{:}13, 12{:}21,
13{:}21, 14{:}8\}$.
Every 4-fold Massey product of positive-degree classes has degree
$\sum|x_i|-2 \geq 4\cdot 5-2 = 18 > 14$, always the zero group. Hence every
defined value is $m=0$ and $\varphi(m)=0 \neq 1$ for every linear detector.
The Massey hierarchy at $K_0$ stops sharply at order 3: triple output degree
$5+5+5-1=14$ with $H^{14}=\mathbf{Q}^8 \neq 0$.

## Proof / Evidence

Exact rational (`Fraction`) boundary-rank homology of all $2^9=512$ induced
subcomplexes $K_I$, aggregated by the Hochster formula. Full 1-skeleton
(all 9 vertices, all 36 edges are faces) follows from every minimal non-face
having size $\geq 3$, so each $K_I$ with $|I|\leq 2$ is a simplex: this gives
the hand-proof of $H^1=H^2=H^3=H^4=0$ plus per-case computational
certification, and $H^6=0$ by $(s,q)$ case analysis. The sweep yields the
table above (total $\dim 88$), 61 nonempty homology supports all of size
$\geq 3$, and the exhaustive $C(61,4)$/$C(61,3)$ disjointness census.
Theorem A uses a dichotomy: the all-zero cochains satisfy every 4-fold
defining equation, so $0$ is in the zero-quadruple Massey set; the set is
then either non-singleton (failing trivial indeterminacy) or $\{0\}$ on that
system (then $\varphi(m)=0$). No claim is made that the zero-quadruple set
equals $\{0\}$. Theorem C uses the certified lowest/top degrees plus the
standard Massey degree formula.

Cross-checks: regex transcription audit of the archived e-print source
matches the hardcoded 15-item list in order (15/15); independently written
facet-down homology engine agrees on 7 unit cases, the full complex
($\tilde{H}_4=\mathbf{Q}^8$), and sampled subcomplexes; all 6 pairwise cups
among $H^5$ generators vanish (disjoint pairs by acyclic union, overlapping
pairs by Baskakov rule); triple pair-unions $K_{123456},K_{456789}$ are
acyclic.

## Limitations

Rational coefficients only; integral torsion not addressed. Support means
Hochster-split support as defined above. No global cup-length claim is made
beyond the certified $H^5$-generator level (4 disjoint support pairs have
nonzero cup-target groups; target-group-nonzero $\neq$ product-nonzero).
The e-print sentence "$4$-dimensional / nonzero $H^4(\mathcal{K})$"
contradicts the audited printed list (39 facets: 34 5-sets and 5 6-sets,
$f=(9,36,80,99,60,5)$, full $\tilde{H}_4=\mathbf{Q}^8$, i.e. dim 5); this is
flagged as a datum only and no theorem uses the dim-4 sentence. The
zero-quadruple Massey set is not claimed to equal $\{0\}$.

## Reproducibility

Stdlib-only Python (`fractions`, `itertools`, `re`). Each script prints a
PASS line and exits 0:

- `python3 output/artifacts/verify_target_obstruction.py` → ALL_TARGET_OBSTRUCTION_CHECKS_PASS
- `python3 output/artifacts/verify_general_disjoint_obstruction.py` → ALL_GENERAL_DISJOINT_CHECKS_PASS
- `python3 output/artifacts/verify_cups_triple.py` → ALL_CUP_CHECKS_PASS
- `python3 output/artifacts/verify_max_disjoint.py` → MAX_DISJOINT_CERT_PASS
- `python3 output/artifacts/verify_transcription.py` → TRANSCRIPTION_AUDIT_PASS
- `python3 output/artifacts/verify_low_degree.py` → LOW_DEGREE_PASS
- `python3 output/artifacts/verify_homology_engine.py` → ENGINE_CROSSCHECK_PASS
- `python3 output/artifacts/verify_degree_gap.py` → DEGREE_GAP_PASS
- `python3 output/artifacts/verify_support_lemma.py` → SUPPORT_LEMMA_PASS
- `output/artifacts/k0_paper.tex` — archived arXiv e-print source (transcription reference)

## References

- I. Limonchenko, T. Panov, Minimally non-Golod face rings and Massey products, arXiv:2201.12779 (2022).
- J. Grbić, A. Linton, Non-trivial higher Massey products in moment-angle complexes, arXiv:1911.07083 (2019, v3 2021).
- S. Amelotte, B. Briggs, Homotopy types of moment-angle complexes associated to almost linear resolutions, arXiv:2506.15457 (2025).
