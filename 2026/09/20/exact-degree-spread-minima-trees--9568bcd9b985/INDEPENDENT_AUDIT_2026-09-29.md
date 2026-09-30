# Independent audit — Exact fixed-order degree-spread minima for trees

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/exact-degree-spread-minima-trees--9568bcd9b985`  
**Assigned and audited tree:** `01fd88746afd1ef9c264b557aca3fd78e351684e`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review.

## Correctness

PASS. For k>=1, every degree at least k+2 contributes at least k+1 to sum_v(d(v)-1)=n-2, so at most floor((n-2)/(k+1)) such vertices exist and all remaining degrees fit in one width-k interval. The proposed degree multiset realizes equality: q copies of k+2, one copy of r+1 when n-2=q(k+1)+r with r>0, and leaves otherwise; its degree sum is 2n-2, hence it is a tree degree sequence by Prüfer coding, and every competing window has at most q+1<=n-q entries. For k=0, the leaf identity gives n<=3R-2 and the three explicit degree-count families attain R=ceil((n+2)/3). Independent exhaustive enumeration of all tree degree multisets for 2<=n<=12 and 0<=k<=4 found no mismatch with either formula.

## Originality

PASS on the all-orders boundary. Caro–Lauri–Zarb (2019) prove sp(T,k)>=(nk+2)/(k+1) for k>=1 and call the bound sharp via trees using only degrees 1 and k+2; their displayed multiplicities require the congruence that makes those counts integral. For k=0 they give the older lower bound and a sharp congruence-class family. Caro–West (2009) describes the tree repetition bound as approximately sharp in general. The assigned record closes all residue classes with one intermediate degree (and explicit 1/2/3-degree constructions for k=0), yielding the exact fixed-n extremal function. No prior source located states these all-order ceiling formulas.

## Scientific value

PASS. The result upgrades known lower bounds and congruence-class sharpness into exact extremal functions for every tree order and every window width, with very simple witnesses. That is a clean completion of an existing extremal problem rather than a restatement of the prior bound.

## Independent checks

- Re-derived both lower bounds and checked the tree-degree-sequence realizability of the witnesses.
- Exhaustively enumerated tree degree multisets through n=12 for k=0,...,4; all minima agree with the claimed formulas.
- Inspected the accessible full text of Caro–Lauri–Zarb (2019): Theorem 3.1 gives the same lower bounds and a two-degree sharpness construction, but not an every-n residue-class formula.
- Checked the current source tree against the assignment snapshot.

## Literature and evidence

- https://arxiv.org/abs/1806.08303 — Caro, Lauri and Zarb, Notes on Spreads of Degrees in Graphs: prior tree lower bounds and congruence-compatible sharpness construction.
- https://bica.the-ica.org/Volumes/85/Reprints/BICA2018-10-Main-Reprint.pdf — Published full text of Caro–Lauri–Zarb (2019), especially Theorem 3.1 on tree spreads.
- https://doi.org/10.37236/96 — Caro and West (2009), repetition-number lower bound and approximate sharpness for trees.
- https://arxiv.org/abs/2609.19762 — Caro, Škrekovski and Zarb (2026), recent degree-spread work; accessible material does not state the audited fixed-order tree formulas.

## Limitations

- The theorem gives only the extremal value, not a classification of all extremal trees or degree sequences.
- The closest 2019 paper uses the word “sharp” for its lower bound; the audit interprets the displayed construction literally and distinguishes sharpness over admissible/congruence orders from an exact formula at every n.
- A screenshot request for the accessible BICA PDF was blocked by URL restrictions, but the full searchable text was available and inspected.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `01fd88746afd1ef9c264b557aca3fd78e351684e`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
