# A 16/27 lower bound for four-colour rainbow Schur triples

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult `REVIEW.md` for limitations. Publication is not peer review or a guarantee of priority.

## Claim

Let `Lambda_{n,4}` be the maximum, over all 4-colourings `c:[n]->[4]`, of the fraction of ordered pairs `(x,y)` with `x+y<=n` for which `c(x),c(y),c(x+y)` are pairwise distinct. Then

`liminf_{n->infinity} Lambda_{n,4} >= 16/27`.

This improves the lower bound `10/21` in Hegde--Kumar--Pratibha, arXiv:2609.18474v1.

## Construction

Use colours `A,B,C,D`. For `x in [n]`:

- if `x == 0 mod 3`, use `A`;
- if `x != 0 mod 3` and `x <= n/4`, use `B`;
- if `n/4 < x <= 2n/3`, colour residue `1 mod 3` by `C` and residue `2 mod 3` by `D`;
- if `x > 2n/3`, swap `C,D` on the two nonzero residues.

Boundary rounding changes only `O(n)` triples.

## Area calculation

Scale `(x,y)` to the triangle

`T={(u,v): u>0, v>0, u+v<=1}`,

of area `1/2`, and set

`L=(0,1/4]`, `M=(1/4,2/3]`, `H=(2/3,1]`.

For each fixed ordered residue pair modulo 3, lattice points in a polygonal subregion have asymptotic density `1/9`. The source proof computes the rainbow area for each residue type:

- `(0,0)`: `0`;
- exactly one summand has residue `0`: `47/144` for each of four ordered residue pairs;
- equal nonzero residues `(1,1)` and `(2,2)`: `1/4` each;
- distinct nonzero residues `(1,2)` and `(2,1)`: `31/72` each.

The total good area over all nine ordered residue pairs is

`4*(47/144) + 2*(1/4) + 2*(31/72) = 8/3`.

Multiplying by residue density `1/9`,

`|R_n(c)| = (8/27)n^2 + O(n)`.

Since the number of ordered Schur pairs is

`C(n,2) = n^2/2 + O(n)`,

the rainbow fraction tends to

`(8/27)/(1/2) = 16/27`.

## Reproducibility

`artifacts/verify.py` recomputes all nine polygonal areas with exact rational inclusion-exclusion, verifies the total coefficient `8/27`, and brute-force counts the construction for several `n` divisible by 36. The archived script executed successfully during packaging.

For the checked multiples of 36 it also observes the exact finite formula

`|R_n(c)| = 8n^2/27 + 5n/18`.

That finite identity is diagnostic only; the asymptotic theorem does not rely on it.

The complete source report is preserved verbatim in compressed form as `artifacts/research_note.md.gz`; `artifacts/research_note.md` gives the decompression command and uncompressed SHA-256.

## Prior work and scope

Hegde, Kumar and Pratibha, *A somewhat sure note on an un-Schur problem*, arXiv:2609.18474v1 (16 Sep 2026), extend the anti-Ramsey Schur multiplicity problem to general numbers of colours. Their general lower bound specializes to `10/21` at `k=4`, and their paper says the general bounds are likely non-optimal and highlights the `k=4` case for further investigation. The earlier Parczyk--Spiegel paper introduced the multiplicity problem in the three-colour setting.

## Limitations

This is only a lower bound; the exact four-colour asymptotic value and the published upper bound `3/4` are unchanged. No optimality is claimed for the modular/interval construction. Because the closest preprint was only about a day old during the source report, unpublished calculations, private communication, and unindexed revisions are material originality threats. No independent validation is claimed.
