# Exact bipartite threshold for generalized strong-majority edge colouring

## Claim

For every integer `k >= 2`, let `delta_k^bip` be the least integer `d` such that every finite simple bipartite graph of minimum degree at least `d` admits a strong `1/k`-majority edge-colouring with `k+1` colours. Then

`delta_k^bip = k^2 + 1`.

The lower bound is witnessed by `K_{k^2,k^2+1}`.

## Definition

An edge-colouring is strong `1/k`-majority when, for every edge `e=uv` and every colour `alpha`, at most

`(d(u)+d(v)-2)/k`

edges adjacent to `e` have colour `alpha`.

## Upper bound

A theorem of de Werra gives, for every bipartite graph and every number `q` of colours, an edge-colouring in which colour-degrees at each vertex differ by at most one. With `q=k+1`, this gives

`d_alpha(v) <= ceil(d(v)/(k+1))`.

For every integer `d >= k^2+1`,

`ceil(d/(k+1)) <= (d-1)/k`.

Indeed, write `d=(k+1)t+r`, `0<=r<=k`. If `r=0`, the inequality reduces to `kt <= (k+1)t-1`. If `r>0`, it reduces to `t+r>=k+1`, which follows from `d >= (k+1)(k-1)+2`.

Hence for an edge `uv`, the number of adjacent edges of colour `alpha` is at most

`d_alpha(u)+d_alpha(v) <= (d(u)-1)/k + (d(v)-1)/k = (d(u)+d(v)-2)/k`.

Thus `delta_k^bip <= k^2+1`.

## Sharp lower bound

Let `G=K_{k^2,k^2+1}` with parts `X,Y`. Fix one colour and let `H` be its colour-class subgraph. Every ambient edge has `2k^2-1` adjacent edges, so for every `x in X`, `y in Y`,

`d_H(x)+d_H(y)-2*1_{xy in E(H)} <= 2k-1`.  (1)

Call a vertex high if its `H`-degree is at least `k`. If high vertices occur on opposite sides, (1) forces all such opposite pairs to be adjacent in `H`; moreover every high pair then has degree sum at most `2k+1`.

The source proof derives from this the single-colour bound

`|E(H)| <= M_k := k^3-k^2+k`.

The cases are:

1. If one side has no high vertex, summing degrees on that side gives at most `k^2(k-1)` or `(k^2+1)(k-1)=M_k-1`.
2. If both sides have high vertices but no high degree is `k+1`, every high degree is exactly `k`; if `p` high vertices lie in `X`, any high vertex in `Y` sees all of them and hence `p<=k`, so
   `|E(H)| <= pk+(k^2-p)(k-1) <= M_k`.
3. If some high vertex has degree `k+1`, the opposite-side degree constraints from (1) force all vertices of degree at least `k-1` into its at most `k+1` neighbours. Summing degrees gives at most `k^3-2k^2+3k` in one orientation and `k^3-2k^2+2k+2` in the other, both at most `M_k` for `k>=2`.

Therefore `k+1` colours cover at most

`(k+1)M_k = k^4+k`

edges, but

`|E(G)| = k^2(k^2+1) = k^4+k^2 > k^4+k`.

So `G` is not strongly `1/k`-majority `(k+1)`-edge-colourable, giving `delta_k^bip >= k^2+1` and hence equality.

## Reproducibility

`artifacts/verify.py` checks the upper arithmetic and lower-case algebra for `2<=k<=100`, and uses a binary MILP for the `k=2` one-colour extremal problem. The archived script executed successfully during packaging, returning the exact optimum `6=M_2` with zero reported MIP gap.

The complete source report, including the fuller case analysis, candidate history, literature searches, and limitations, is preserved verbatim in compressed form as `artifacts/research_note.md.gz`; `artifacts/research_note.md` gives the decompression command and uncompressed SHA-256.

## Prior work and scope

The closest source is P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v2. It introduces the generalized strong `1/k` notion, proves a general sufficient minimum degree `2k^2+1`, records the `K_{4,5}` obstruction for `k=2`, and asks for the general threshold. The upper-bound tool comes from de Werra's balanced bipartite edge-colouring theorem, quoted in Kalinowski--Kamyczura--Pilśniak--Woźniak, arXiv:2605.23828. Pękała--Przybyło's earlier arXiv:2309.16624 concerns a different vertexwise generalized-majority condition.

## Limitations

the same-model review classified originality as a qualified PASS only. The clearest inaccessible threat is D. S. McNeil's August 2026 personal communication, cited by Pękała--Przybyło for `K_{4,5}` and other computational examples. Very recent or unindexed follow-up work could also overlap. No independent review is claimed.
