# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The construction separates the two symmetric parameters in the Fang--Xu template. For parameter p, the B1--C2 gadget has parts p+t and t, minimum degrees at least 2t-p and t, and exactly max{t^2,(p+t)(2t-p)} edges; an independent q-gadget is placed between C1 and B2. Direct degree calculations give minimum degree at least n+t under the sole size condition n>=p+q+3t.

The triangle support was checked adversarially: because every triangle in a tripartite graph uses one vertex from each main part, the specified adjacency pattern leaves only A1-B1-C2 and A3-B2-C1. Their counts are p|E(H_p)| and q|E(H_q)|, yielding exactly F_t(p)+F_t(q).

The threshold argument is exact. On t<=u<=sqrt(2)t,
F_t(u)/t^3-2=(u/t-1)(2-(u/t)^2)>=0. The first integer p_t above sqrt(2)t has F_t(p_t)<2t^3; if it lies beyond the branch switch at phi t, this follows instead from F_t(p_t)=p_t t^2<2t^3. Thus (p,q)=(p_t,t) is a strict counterexample for n>=4t+p_t. Conversely, p+q<t+p_t forces both parameters below p_t, so each term is at least 2t^3; this proves the claimed optimality inside the family.

Boundary cases t=1 and t=2 were checked separately in the symbolic argument and verifier. The strict 4t^3 corollary is asserted only for t>=2.

The standalone verifier constructs the graphs and counts triangles directly. It checked 1,636 graph instances covering every p,q in [t,2t] for 1<=t<=12 at two admissible orders, plus 4,999 threshold-arithmetic instances for 2<=t<=5000. All checks passed.

## Originality

**PASS, to the best of our knowledge.**

The bipartite gadget and the symmetric p=q construction are prior work and are not claimed as new. Fang--Xu, arXiv:2609.20590v1, was inspected directly. Their Theorem 1.3 and Section 2 use |A1|=|A3|=p, |B1|=|C1|=p+t and two copies of the same H_p, producing 2F_t(p), and optimize near p=phi t. No unequal p,q formulation or sqrt(2)-threshold optimization appears in the accessible v1 text.

The original Bollobás--Erdős--Szemerédi 1975 paper was also inspected directly, including the construction on pp. 100--101. It gives the classical 4t^3 example and the proposed n>=5t lower bound, not the asymmetric two-parameter extension.

Searches used the exact source title and arXiv identifier, balanced-tripartite minimum-degree triangle formulations, '4t^3', 'sqrt(2)', asymmetric and unequal-parameter construction language, and broader multipartite triangle-count terminology. No prior statement of the two-parameter formula or the n >= 4t+floor(sqrt(2)t)+1 counterexample range was located.

No specific inaccessible paper was identified as especially likely to overturn originality. The principal residual risk is recency: the Fang--Xu preprint is only days old, so an unindexed parallel observation or a later revision could contain the same asymmetrization.

## Value

**PASS.**

The result materially narrows the order range in which the 50-year-old 4t^3 proposal is now known to fail. The leading threshold coefficient drops from 3+2phi about 6.236 to 4+sqrt(2) about 5.414, much closer to the original boundary 5. The mechanism also distinguishes two optimization goals that the symmetric construction conflates: minimizing triangle count for abundant order versus minimizing the order at which any strict violation first occurs.

The general bound F_t(p)+F_t(q) is reusable: for a prescribed available order budget p+q<=n-3t, the two sides can be optimized independently or asymmetrically.

## Limitations

- This is an upper-bound construction and does not determine f(n,t).
- The optimality statement concerns only this two-parameter family; other constructions may violate 4t^3 below the stated threshold.
- The bipartite gadget and all symmetric special cases are prior work.
- The very recent source paper creates a non-negligible parallel-work/revision risk despite the present searches.
- Finite verification supports but does not replace the symbolic proof.
- Independent audit has not been performed.
