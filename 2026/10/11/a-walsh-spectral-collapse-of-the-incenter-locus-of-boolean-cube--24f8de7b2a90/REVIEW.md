# Independent mathematical audit

## correctness

PASS

For d>=1, the centered zonotope in H={sum x_v=0} has support h(u)=1/2 Σ_edges |u_v−u_w|. The discrete layer-cake/coarea identity for nested upper-level sets gives radius min_S |∂S|/(2||1_S−(|S|/N)1||), and, by both support inequalities, all ball centers satisfy |Σ_{v∈S}c_v|+r sqrt(s(N−s)/N)<=|∂S|/2. Induction with binary entropy H_2(t)>=2t for t in [0,1/2] yields e(S)<=s log_2(s)/2, with equality at power-of-two sizes only for subcubes. For s<=N/2, t=ln(N/s) yields lower bound (sqrt N/(2 ln2))*t/sqrt(e^t−1). Its derivative has sign 2(1−e^(−t))−t, with one positive zero, so interior sizes are strictly worse than the minimum of halfcube s=N/2 and singleton s=1. The two squared radius candidates are N/4 and d² N/[4(N−1)], respectively; compare d² with 2^d−1. For 2<=d<=4 all minimizing cuts are exactly the 2d coordinate halfcubes (d=1 gives the same two singletons); for d>=5 all minimizing cuts are exactly 2N singletons/complements. These are genuine facets by connectedness of S and its complement. In d<=4, d independent degree-one Walsh normals plus the H sum constraint force exactly the span of degree>=2 Walsh characters; every other inequality strict at zero gives a relative neighborhood, so dim N−d−1. For d>=5, singleton opposites force every center coordinate zero. Independent new Python bitset cut enumeration (not the bundled verifier) checked every nontrivial cut for d=1..4, yielding 2,4,6,8 minimizing cuts and squared radii 1/2,1,2,4; checked 2375,2761,3194 deterministic cuts for d=5,6,7 with no violations and only singleton equalities. Finite checks corroborate, while analytic inequalities prove all d. The theorem does not determine vertices/volumes of the small-d center polytope and excludes weighted variants.

## originality

PASS

Qualified best-of-knowledge PASS applies ONLY to the all-dimensional exact optimal-cut equality/contact structure and classification of the entire incenter locus (Walsh affine span for d<=4; uniqueness for d>=5). The radius-as-normalized-cut formula is already explicitly present in a published Resultary general weighted-graph theorem; Harper/Bernstein/Lindsey/Hart edge isoperimetry and Padrol–Pilaud–Poullot facet combinatorics are prior premises. Their available statements and full-text relevant theorems do not provide all centers or the dimension-five transition. The other relevant vertex-transitive-zonotope radius theorem has a narrower hypothesis and expressly does not classify all centers. The identical Resultary record for the assigned finding is not independent evidence. Extensive qualified scope and residual risks are recorded; no search-failure-based novelty proof is claimed.

## value

PASS

Maximum inscribed Euclidean balls and their complete center sets are intrinsic, natural invariants of the unweighted Boolean-cube graphical zonotope family, not an arbitrary slice. The result exhibits a sharp geometric uniqueness transition: 11-dimensional optimal-center freedom at d=4 (ambient dimension 15) collapses to a unique center at d=5 (ambient dimension 31), with tangible changes from 2d coordinate-halfcube contacts to 2^(d+1) singleton contacts. Walsh degree decomposition fully describes the affine freedom in low dimensions, which is distinct from merely obtaining an already-known radius formula. It is a motivated self-contained all-d geometric classification, without claiming a general theory for other zonotopes or a paper-sized follow-on.

The dated certificate retains the supplied scientific assessment, sources and limitations.
