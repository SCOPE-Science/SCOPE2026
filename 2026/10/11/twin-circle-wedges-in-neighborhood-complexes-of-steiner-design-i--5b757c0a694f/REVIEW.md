# Same-model review

Claim reviewed: For every nontrivial Steiner \(2\)-design \(D=S(2,k,v)\) with \(2\le k<v\), let \(b\) be the number of blocks, let \(r\) be the number of blocks through each point, and let \(G_D\) be the point-block incidence graph. Then the Lovász neighborhood complex \(\mathcal N(G_D)\) has exactly two connected components. Each component simplicially collapses to a connected graph of cycle rank \(\mu=vr-v-b+1=b(k-1)-v+1=v(r-1)-b+1\), so each component has simple-homotopy type \(\bigvee^{\mu}S^1\). Hence \(\mathcal N(G_D)\simeq(\bigvee^{\mu}S^1)\sqcup(\bigvee^{\mu}S^1)\). For a projective plane of order \(q\), this specializes to \(\mu=q^3\).

## Correctness
PASS. The proof decomposes the neighborhood complex along the bipartition, proves a relative simplex-to-tree collapse lemma, applies it independently because distinct design blocks share at most one point, and computes both resulting graph ranks. The equality of the two ranks is exactly the incidence identity \(bk=vr\). Connectivity is proved on each side from the Steiner axiom. The finite verifier replays explicit elementary collapses on four designs and agrees with the symbolic formula.

## Originality
PASS. Kozlov's full paper supplies the common-neighbor definition and general simple-homotopy relation with \(\operatorname{Hom}(K_2,G)\), not the design-specific calculation. Shukla's full paper gives a qualitative wedge-of-circles result for maximum degree at most \(3\), which covers only a low-degree special case and does not imply the unbounded design family or exact rank. The closest indexed projective-plane result concerns a scale-two Vietoris–Rips complex, whose simplex condition is different. Residual risk remains from older linear-hypergraph terminology.

## Value
PASS. The result gives an exact simple-homotopy classification for a broad and natural incidence-geometry family and identifies the same invariant on both dual sides: the cycle rank \(vr-v-b+1\) of the incidence graph. The projective-plane value \(q^3\) is a concise structural specialization rather than an arbitrary finite parameter slice.

## Closest literature and limitations
Closest literature: arXiv:math/0503613v1 and arXiv:1802.04526v1. A separate indexed result computes a different Vietoris–Rips complex on finite-projective-plane incidence graphs. The theorem is nonequivariant, and the literature check cannot rule out unindexed or differently phrased general linear-hypergraph results.

Same-model review: passed. Independent audit: not yet performed.
