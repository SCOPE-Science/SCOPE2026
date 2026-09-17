# A (14h-13)-Barrycade construction of height h-1

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. The parent preprint is extremely recent and an unpublished predecessor manuscript is a material originality threat.

## Claim

For every integer `h>=2`, the source report proposes a construction of a

`(14h-13)`-Barrycade

of height `h-1`.

If `H(n)` denotes the maximum height of an `n`-Barrycade, this gives

`H(14h-13) >= h-1`

and consequently

`limsup H(n)/n >= 1/14`.

The source report presents this as a sharpening of the explicit `24h` construction in Dębski--Grytczuk--Naroski--Pawlik--Przybyło--Śleszyńska-Nowak, arXiv:2609.18476v1, improving the displayed asymptotic construction density from `1/24` to `1/14`.

## Definition

For a permutation `pi=(a_1,...,a_n)`, let

`S_pi={a_1, a_1+a_2, ..., a_1+...+a_{n-1}}`.

An `n`-Barrycade of height `t` is a family of `t` permutations of `[n]` whose proper-prefix-sum sets are pairwise disjoint.

## Three-skip lemma

Set

`x_1=2h+1`.

For `i=2,...,h-1`, choose `x_i` greedily as the least integer `d>x_{i-1}` such that

`J_i(d)={d+i, d+2i, d+i+2h}`

is disjoint from every earlier

`J_k={x_k+k, x_k+2k, x_k+k+2h}`.

The key observation is that a fixed earlier `k` can reject at most three candidate values over the entire greedy process. Among the nine possible equalities between a new and old joint, only three are compatible with `d>x_k`:

1. `d+i=x_k+2k`,
2. `d+i=x_k+k+2h`,
3. `d+2i=x_k+k+2h`.

The other six imply a negative value for `d-x_k` when `k<i<=h-1`. Each surviving new coordinate increases throughout the greedy search, so it can meet its corresponding fixed old coordinate at most once.

Only `k<=h-2` can obstruct a later choice. Hence total skips are at most `3(h-2)`, while the `h-2` greedy stages contribute the ordinary unit increments. Therefore

`x_{h-1} <= (2h+1)+(h-2)+3(h-2)=6h-7`.            (1)

## Row construction

Let `X=x_{h-1}` and

`L=2X+2h+1`.

For `1<=i<h`, define the block sequence

`P_i=(x_i,i,2h-i,2X+1-x_i)`,

and take `P_h=(L)`.

The source report checks that all block lengths among the `P_i` are globally distinct, that `h` and `2h` do not occur, and that the greedy joint-disjointness permits copies of the `P_i` to start one unit apart without joint collision.

It then assembles `h` rows cyclically from the `P_i`, introduces one `h` block in each of the first `h-1` rows, deletes row `h`, appends the still-unused lengths in common order, appends `2h-i` to row `i`, and finally replaces the consecutive pair `(i,2h-i)` inside its distinguished `P_i` copy by the single block `2h`.

The replacement preserves total length and deletes a joint rather than creating one. Each surviving row becomes a permutation of `[n]`, with pairwise disjoint proper-prefix-sum sets.

By (1),

`L <= 2(6h-7)+2h+1=14h-13`,

and the construction takes

`n=14h-13`.

## Computational corroboration

The source report states a verifier implementing the greedy `x_i`, the `P_i`, cyclic row assembly and final replacement. It checked that the rows are permutations and that all proper-prefix-sum sets are disjoint for `h=2,...,15` and additional values through `h=300`.

The companion files supporting this finding are now archived as `artifacts/proof_note.md` and `artifacts/verify.py`. The verifier's built-in default test set covers `h=2,...,15` and selected values through `h=100`; the broader through-`h=300` check remains the same-model review's reported source-report computation. These computations are corroborating sanity checks, not independent proof verification.

## Closest prior work

- Dębski et al., arXiv:2609.18476v1, is the direct parent source. The source report states that its public v1 uses a nine-collision accounting and a `24h`-scale explicit construction.
- Richard Guy's 2020 *Building Barrycades and Constructing Corrals* is the original problem source identified by the run.
- An unpublished manuscript *Building barricades*, cited in adjacent 2026 work, is the strongest originality threat because its constants were inaccessible.
- A 2025 Barrycades chapter by Brian Hopkins was available only in limited preview.

The source report also notes an arithmetic inconsistency in one displayed constant line of the parent v1; this archive records that observation but does not make any stronger claim about the parent theorem.

## Limitations

The unpublished predecessor manuscript could already contain the same or a stronger constant. The parent preprint was one day old, so an unposted revision or contemporaneous observation is plausible. This is a same-model review, not independent verification.
