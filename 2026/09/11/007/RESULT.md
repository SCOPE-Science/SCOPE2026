# No member of the socle-PSL(3,8) almost-simple window is Hurwitz (2,3,7)-generated: complete Frobenius tables plus maximal-subgroup / quotient obstructions

## Context

Hurwitz (2,3,7)-generation is the classical Hurwitz/Macbeath benchmark refined by
Liebeck–Shalev: which finite simple and almost-simple groups are quotients of the
(2,3,7) triangle group controls automorphism bounds of Riemann surfaces and feeds
Beauville structures and expander Cayley constructions. Simple-group
PSL(3,q) criteria (Conder update; Cohen/Lucchini: PSL(3,q) Hurwitz only for small
or restricted q; q=8=1 mod 7 is non-Hurwitz) decide the simple control but do not
decide almost-simple extensions. The natural next layer over the fixed socle
PSL(3,8) ≅ L3(8) (|L3(8)|=16482816, Out=6) is the window
W = {L3(8), L3(8):3, Aut(L3(8))=L3(8):6}, with |L3(8):3|=49448448 and |Aut|=98896896.

## Definitions

- Hurwitz (2,3,7)-generated: G = ⟨x,y⟩ with |x|=2, |y|=3, |xy|=7
  (equivalently x²=y³=z⁷=xyz=1 with z=(xy)⁻¹, ⟨x,y⟩=G).
- Normalized Frobenius constant n(C₂,C₃,C₇): character-sum count of triples per
  fixed z; CMC = class-multiplication coefficient (number of (x,y) pairs with xy=z).
- ATLAS standard generators: L3(8): a²=b³=1, |ab|=21; L3(8):3: e²=1, |f|=12,
  |ef|=21; L3(8):6: g∈2A, h∈18D, |gh|=24. Maximal subgroups and SLP word programs
  (max1W1, max2W1, max5W1) per the official ATLAS L3(8) page.
- GAP CTblLib labels: "L3(8)", "L3(8).3", "L3(8).6".

## Result

Let W = {L3(8), L3(8):3, L3(8):6 = Aut(L3(8))}. Then:

1. **Normalized Frobenius (2,3,7) constants** (GAP 4.12.1 + CTblLib 1.3.7,
   Irr-sum with CMC cross-check):
   - L3(8): only (2a,3a,7g),(2a,3a,7h) have n=1 (CMC 49 per fixed z);
     (2a,3a,7i/7j/7k) have n=15/7 (CMC 105); all (2a,3a,7a–7f) are 0.
   - L3(8):3: (2a,3a,7c/7d) have n=1/3 (CMC 49); (2a,3a,7e) has n=15/7
     (CMC 105); everything involving outer classes 3b/3c is 0.
   - Aut = L3(8):6: (2a,3a,7b) has n=1/3 (CMC 49); (2a,3a,7c) has n=15/14
     (CMC 105); everything involving 2b/3b/3c is 0.
2. **Verdicts: no member of W is Hurwitz (2,3,7)-generated.**
   - L3(8): exhaustive per-class check — for one z in each of the 5
     small-centralizer 7-classes, ALL (x,y)∈2a×3a with xy=z generate proper
     subgroups only: the two 49-pair classes give |H|=168 throughout and 49/49
     per z are G-conjugate to the stored ATLAS L2(7) maximal M5 (exact
     IsConjugate test); the three 105-pair classes give |H|=504 throughout
     with H ≅ PSL(2,8), and 105/105 pairs per z lie in a conjugate of the named
     parabolics max1 `2^6:(7×L2(8))` or max2 `2^6:(7×L2(8))` (56/105 in each;
     73-transversal exact membership). Since all other (2,3,7) class triples are
     empty, no generating triple exists.
   - L3(8):3: quotient obstruction. The ATLAS word program L38d3G1-max1W1 builds
     the socle N=L3(8) (order 16482816, verified normal of index 3, quotient C3).
     Any homomorphism to C3 kills elements of orders 2 and 7 (coprime to 3), so
     every involution and every element of order 7 lies in N. Hence for any triple
     xyz=1 with |x|=2, |z|=7, both x,z∈N, so y=x⁻¹z⁻¹∈N; every (2,3,7) triple lies
     in N and ⟨x,y⟩≤N<G.
   - Aut = L3(8):6: reduction to the previous case. In the verified 657-point
     representation, the ATLAS program L38d6G1-max1W1 builds M1=L3(8):3 (order
     49448448, normal, quotient C2). ALL order-3 and ALL order-7 elements lie
     inside M1; only the outer involution class 2b lies outside. The positive
     triples use x=2a (inside), so every positive (2,3,7) triple lies in M1,
     which is itself non-Hurwitz.

The simple-group leg is a replay control; novelty rests on the :3 and :6
extension tables (outer-class vanishing) plus the machine-checked
quotient/reduction chain.

## Proof / evidence

- `frobenius_all.log` + `frobenius_L38d3.log`: Irr-sum normalized constants +
  CMC cross-check for all three tables (centralizer data included for :3).
- 73-point L3(8) p73bB0 rep-check (a order 2, b order 3, ab order 21, |G| exact),
  class-2a size 4599; exhaustive 49/105-pair generation test per 7-class
  (submitted 1.06 MB scan logs inspected via tails/summaries; hashes recorded).
- Exact named-maximal attribution: 49/49 L2(7)-conjugate; 105/105 in a
  max1/max2 parabolic conjugate (union 105/105; 56/105 each).
- `:3` 73-point rep-check, socle construction via max1W1, normality/index/
  quotient verification, coset census (orders 2: 3/0, 7: 1039/0 in-N).
- Aut 657-point rep-check (g order 2, h order 18, gh order 24, |G| exact), max1
  construction, per-order centralizer coset census (3: 267/0, 7: 1061/0 in-M1).
- ATLAS SLP convention; maximal-subgroup orders rebuilt from words.
- Caveat: the L38G1-p73aB0 copy on the ATLAS site is corrupt and was NOT used;
  the p73bB0 copy verifies cleanly and is the basis.

## Limitations

- Correctness inherits trust in GAP 4.12.1 / CTblLib 1.3.7 and ATLAS
  word/representation correctness; library versions and SHA-256 hashes recorded.
- Coset censuses are pseudo-random samples keyed by centralizer sizes, but the
  decisive trapping is a coprimality theorem (orders 2,7 into the index-3 socle;
  orders 3,7 into the index-2 :3 subgroup), so sampling is confirmatory.
- The corrupt ATLAS L38G1-p73aB0 copy was identified and excluded.

## Reproducibility

Load G from GAP Character Table Library; recompute normalized Frobenius (2,3,7)
structure constants with full character-sum log. In the ATLAS permutation
representations with standard generators (73-pt for L3(8) and :3, 657-pt for :6),
check the rep orders and group order, build N (resp. M1) via the archived SLP
word programs, verify normality/index/quotient, run the class-2a scan
(L3(8)) and per-order coset censuses (:3, :6), and the named-maximal membership /
conjugacy tests. Archived generators, SLP programs, cyc programs, and logs with
SHA-256 hashes are in output/artifacts/.

## References

- ATLAS of Finite Group Representations: Linear group L3(8).
  https://brauer.maths.qmul.ac.uk/Atlas/lin/L38/
- An update on Hurwitz groups (Conder). https://heldermann-verlag.de/gcc/gcc02/gcc028.pdf
- Hurwitz Groups of Large Rank (Lucchini). https://doi.org/10.1112/S0024610799008467
- Hurwitz components of groups with socle PSL(3,q) (Salih, Extracta Math. 36, 2021).
- Hurwitz Groups and G2(q) (Malle) — character-plus-maximal method precedent.
