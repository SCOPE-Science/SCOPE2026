# Complete Ramanujan classification of symmetric normal Cayley graphs of A5

## Context
The Hirano–Katata–Yamasaki program determines valency bounds guaranteeing
that normal Cayley graphs are Ramanujan for abelian, Frobenius, and dihedral
$2p$ groups, and studies coincidence of the true bound with the trivial
character-sum estimate. The smallest nonabelian simple group
$A_5 \cong \mathrm{PSL}(2,4)$ of order $60$ is the natural next closed case.
No sharp Ramanujan valency threshold or complete normal-Cayley verdict table
for $A_5$ appears in the surveyed prior work (Frobenius/dihedral bounds,
generalized-quaternion bounds, expander surveys).

## Definitions
- $A_5$: alternating group on 5 letters, $|A_5|=60$.
- Conjugacy classes: $\{1\}$ (size 1), $2A$ (double transpositions, size 15),
  $3A$ (3-cycles, size 20), $5A, 5B$ (the two 5-cycle classes, size 12 each).
- A connection set $S$ is *normal* if it is a union of conjugacy classes, and
  *symmetric* if $S=S^{-1}$ with $1 \notin S$.
- Each of the four nontrivial classes is inverse-closed (checked elementwise
  in the permutation model), so the symmetric normal sets are exactly the
  $2^4-1=15$ nonempty unions of $\{2A,3A,5A,5B\}$.
- $\mathrm{Cay}(A_5,S)$: Cayley graph under left multiplication, regular of
  degree $d=|S|$.
- Ramanujan: connected $d$-regular graph with
  $\lambda^* := \max_{\lambda \ne d}|\lambda| \le 2\sqrt{d-1}$.
- $\varphi=(1+\sqrt5)/2$, $\psi=(1-\sqrt5)/2$.

## Result
Every nonempty symmetric normal $S \subset A_5$ generates $A_5$ (hence
$\mathrm{Cay}(A_5,S)$ is connected), and every such graph is Ramanujan.
There are exactly 15 such graphs. The minimum valency is

$$D^* = 12,$$

attained at $S=5A$ and $S=5B$, so $D^*=12$ is the sharp valency threshold
guaranteeing Ramanujan over this family (sharp as the attained minimum;
no smaller symmetric normal degree exists and no sub-threshold
non-Ramanujan witness exists).

Exact spectra are given by the normal-Cayley character formula: for each
irreducible character $\chi$ of degree $\chi(1)$,

$$\lambda_\chi(S) = \frac{1}{\chi(1)}\sum_{s \in S}\chi(s)$$

with multiplicity $\chi(1)^2$. Committed character table (columns
$1,2A,3A,5A,5B$): trivial $1,1,1,1,1$; $3a$: $3,-1,0,\varphi,\psi$;
$3b$: $3,-1,0,\psi,\varphi$; $4$: $4,0,1,-1,-1$; $5$: $5,1,-1,0,0$.

Complete verdict table ($RB=2\sqrt{d-1}$; trivial-bound column is the
per-character trivial-estimate maximum):

| S | d | lambda* | RB | Ramanujan | trivial certifies |
|---|---|---|---|---|---|
| 2A | 15 | 5.0 | 7.483315 | yes | yes (5.0) |
| 3A | 20 | 5.0 | 8.717798 | yes | yes (5.0) |
| 2A+3A | 35 | 5.0 | 11.661904 | yes | yes (7.0) |
| 5A | 12 | 6.472136 ($2+2\sqrt5$) | 6.633250 | yes | yes (6.472136) |
| 5B | 12 | 6.472136 | 6.633250 | yes | yes (6.472136) |
| 2A+5A | 27 | 7.472136 ($3+2\sqrt5$) | 10.198039 | yes | NO (11.472136) |
| 2A+5B | 27 | 7.472136 | 10.198039 | yes | NO (11.472136) |
| 3A+5A | 32 | 6.472136 | 11.135529 | yes | yes (8.0) |
| 3A+5B | 32 | 6.472136 | 11.135529 | yes | yes (8.0) |
| 2A+3A+5A | 47 | 7.472136 | 13.564660 | yes | yes (11.472136) |
| 2A+3A+5B | 47 | 7.472136 | 13.564660 | yes | yes (11.472136) |
| 5A+5B | 24 | 6.0 | 9.591663 | yes | yes (8.944272) |
| 3A+5A+5B | 44 | 4.0 | 13.114877 | yes | yes (11.0) |
| 2A+5A+5B | 39 | 6.0 | 12.328828 | yes | NO (13.944272) |
| all-but-identity | 59 | 1.0 | 15.231546 | yes | yes (13.944272) |

The trivial per-character estimate
$|\lambda_\chi| \le \chi(1)^{-1}\sum_{s\in S}|\chi(s)|$ certifies Ramanujan
for 12 of the 15 graphs. The three exceptions $2A{+}5A$, $2A{+}5B$ ($d=27$)
and $2A{+}5A{+}5B$ ($d=39$) are genuinely Ramanujan by exact spectrum but not
certified by the trivial estimate. Tightest case: $d=12$,
$\lambda^*=2+2\sqrt5\approx6.472136$ vs $2\sqrt{11}\approx6.633250$
(margin $\approx 0.161$).

## Proof / evidence
1. Conjugacy classes and inverse-closedness verified by brute-force
   conjugation in the 60 even permutations of $\{0,\dots,4\}$: sizes
   $[1,12,12,15,20]$, each class inverse-closed.
2. Committed character table verified by exact row orthogonality
   $\sum_C |C|\chi_i(C)\chi_j(C)=60\delta_{ij}$ (all 25 inner products).
3. Character-route spectra computed from the formula above for all 15 sets;
   closed forms involve only integers and $\sqrt5$ (e.g. $2\pm2\sqrt5$,
   $-3\pm2\sqrt5$), and every Ramanujan inequality holds strictly as an exact
   $a+b\sqrt5$ comparison.
4. Matrix route: $60\times60$ Cayley adjacency matrices diagonalized by a
   symmetric eigensolver; the multiset
   $\{\lambda_\chi \text{ with multiplicity } \chi(1)^2\}$ agrees with the
   matrix eigenvalues to $<5\times10^{-13}$ (replay $<10^{-9}$) in every case.
5. Generation/connectedness: every nonempty normal $S$ spans a nontrivial
   normal subgroup, hence all of $A_5$ by simplicity; additionally confirmed
   by 60-vertex BFS on all 15 sets.
6. Replay: `python3 output/artifacts/verify.py` (numpy only) prints
   `VERIFY_OK: 15/15 Ramanujan, matrix agreement <1e-9, 12/15
   trivial-certified, exceptions [...]`.

## Limitations
- Finite classification over one group ($A_5$) and normal symmetric
  connection sets only; no claim about non-normal Cayley graphs of $A_5$ or
  any other group, and no general theorem beyond $A_5$.
- Matrix cross-check agreement is floating-point numerical evidence, not
  interval arithmetic; the spectra themselves are exact closed forms from the
  verified character table.
- $D^*=12$ is sharp as the attained minimum valency; because all 15 graphs
  are Ramanujan there is no sub-threshold non-Ramanujan witness, and the
  trivial estimate alone does not force all $d\ge D^*$ (exact split 12 vs 3
  recorded instead).

## Reproducibility
`output/artifacts/verify.py` (numpy only) rebuilds the permutation model,
class sizes, inverse-closedness, character-table orthogonality, all 15
character spectra, $60\times60$ adjacency eigenspectra with agreement check,
Ramanujan verdicts, trivial-bound certification split, and BFS connectedness
from the committed table and class lists. `output/artifacts/census.json`
records per-graph eigenvalues, $\lambda^*$, Ramanujan bound, agreement, and
trivial-bound values.

## References
- M. Hirano, K. Katata, Y. Yamasaki, Ramanujan Cayley graphs of Frobenius
  groups, Bull. Aust. Math. Soc. 94 (2016), 373–383. arXiv:1503.04075.
  https://arxiv.org/abs/1503.04075
- Y. Yamasaki, Ramanujan Cayley graphs of the generalized quaternion groups
  and the Hardy–Littlewood conjecture (2016). arXiv:1611.09977.
  https://arxiv.org/abs/1611.09977
- A. Lubotzky, Expander Graphs in Pure and Applied Mathematics (2011).
  arXiv:1105.2389. https://arxiv.org/abs/1105.2389
