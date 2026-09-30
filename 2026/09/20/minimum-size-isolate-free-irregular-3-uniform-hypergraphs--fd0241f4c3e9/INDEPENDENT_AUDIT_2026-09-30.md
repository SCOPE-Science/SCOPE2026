# Independent audit — Minimum size of isolate-free irregular 3-uniform hypergraphs

## Scope
Independent review of `2026/09/20/minimum-size-isolate-free-irregular-3-uniform-hypergraphs--fd0241f4c3e9` for task `d78192f91c71d25955327c261d13fec3`. The assigned source tree `8e09ee7165b35df92da154560abfce8ba41e2f3d` matches the tree on repository `main` at commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`. Audit date: 2026-09-30 UTC.

## Correctness
**PASS.**

- The lower bound is exact: n distinct positive degrees have sum at least n(n+1)/2, while a 3-uniform hypergraph has total degree 3m.
- The modulo-6 induction was checked case by case. Adding a new vertex with link graph F creates distinct new triples; the specified matchings, or the three-edge path plus matching in residue classes 1 and 4, transform D_{n-1} to the claimed D_n and add exactly M_n-M_{n-1} edges.
- The n=7 boundary case has enough vertices for the path construction, and independent arithmetic verified sum(D_n)=3 ceil(n(n+1)/6) for every 6<=n<=200. The committed verifier independently encodes the same construction and reports successful checks through n=200.

## Originality
**PASS_NARROW.**

- Gyárfás–Jacobson–Kinch–Lehel–Schelp (1992) gives existence of irregular uniform hypergraphs and the six-vertex seven-edge 3-uniform example, and discusses eliminating an isolate, but the checked open full text does not state the fixed-order minimum-edge formula here.
- Broader degree-sequence literature, including Behrens et al. and Li–Miklós, addresses graphicness/realizability in different regimes. Exact and synonymous searches for the sparse degree sets and ceil(n(n+1)/6) did not locate an equivalent theorem.
- The originality conclusion remains bounded because older sparse set-system/degree-sequence literature is fragmented and may use different terminology.

## Scientific value
**PASS.**

- The result makes the elementary degree-sum obstruction sharp at every order n>=6, identifies the exact two residue classes requiring the minimal divisibility correction, and supplies an explicit recursive realization rather than only an existence argument.

## Literature checked
- [Irregularity Strength of Uniform Hypergraphs](https://users.renyi.hu/~gyarfas/Cikkek/61_GyarfasJacobsonKinchLehelSchelp_IrregularityStrengthOfUniformHypergraphs.pdf)
- [New Results on Degree Sequences of Uniform Hypergraphs](https://doi.org/10.37236/3414)
- [Dense, irregular, yet always graphic 3-uniform hypergraph degree sequences](https://arxiv.org/abs/2312.00555)

## Limitations
- The theorem is for simple isolate-free 3-uniform hypergraphs and does not classify all extremal realizations.
- Originality is to the best of the targeted literature check; differently indexed sparse hypergraph degree-sequence work remains a residual risk.

## Conclusion
The record **passes** the independent three-axis audit on the stated, literature-bounded claim. No substantive research-file correction is required. This audit does not convert a targeted literature search into an exhaustive priority guarantee.
