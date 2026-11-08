# Independent mathematical audit

## correctness

PASS

For K_{m,n} with m≥n≥1, every subset of size ≤2 is GP, and a set of size ≥3 is GP precisely if it lies entirely in one bipartition class, giving coefficients a0=1,a1=m+n,a2=C(m+n,2), a_k=C(m,k)+C(n,k) for k≥3. The tail t_k has generating function (1+z)^n[1+(1+z)^{m−n}]. The second factor has coefficients b0=2,b1=d,b_k=C(d,k), and its only modified log-concavity minor is d²−2C(d,2)=d≥0; binomial first factor is log-concave, and nonnegative convolution of no-gap log-concave sequences is log-concave by TP2 Toeplitz/Cauchy–Binet. Thus only possible full-polynomial valley is a2>a3<a4. For m≤7, C(r,4)≤C(r,3), so no valley. For m≥10, if n≥9 then C(r,3)≥r² for both r≥9, giving a3≥a2; if n≤8, F(m,n)=C(m,3)+C(n,3)−C(m+n,2) is strictly increasing in m≥10 and its m=10 eight values are all >0. Checking m=8,9 gives exactly five (8,4..8) and two (9,6..7) negative F entries, all with a4>a3. The exceptional set was independently checked by exact integer binomial calculations for 1≤n≤m≤100, including tail log-concavity, and the source verifier Git blob f5aeacd501c35e2c106d7f0defdc6e9f04b629f1 was inspected. These finite checks do not replace the all-size inequality proof.

## originality

PASS

The final claim is compared by statement and implication, not by title. The previously published formula for ψ(K_m,n) is identical and explicitly credited; the new claim is its all-parameter shape theorem. Individual known examples K8,4, K9,7, K8,8 are subsumed, not touted as original. Earlier complete multipartite polynomial formulas do not include the complete seven-exception boundary in inspected parts. Earlier results cover graphs beyond complete bipartite but are weaker on this specific shape classification. General log-concavity-preserving convolution is textbook; applying it to the special t0=2 coefficient via factorization and coupling to exceptional a2 supplies the nontrivial classification. The complete two-part seven-exception list is not a reference table extracted from Resultary; search returned related graph families (spider, corona, dual general-position, complete-multipartite variants), not a preexisting full K_m,n classification. Absence of matching database entry alone does not prove novelty. From known coefficient formula one must prove global tail log-concavity, show no future valleys, derive a finite bound on m, and check the two transition rows m8,m9. Published example calculations do not imply the iff theorem without these inequalities; a preexisting fully general unimodality theorem covering K_m,n would defeat the claim if identified. Accessible primary texts were materially compared; inaccessible plausible primary texts are named as residual risks rather than treated as disproving novelty.

## value

PASS

The general-position polynomial of complete bipartite graphs is a natural already-established graph counting invariant, and published papers explicitly raised nonunimodality through isolated examples. The complete all-parameter classification into precisely seven exceptions, with a structural log-concave tail forbidding all later valleys, resolves the natural bipartite shape question. This is not a repetition of the known polynomial formula or three previously listed examples: it supplies a sharp iff theorem and explains why all other part sizes are unimodal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
