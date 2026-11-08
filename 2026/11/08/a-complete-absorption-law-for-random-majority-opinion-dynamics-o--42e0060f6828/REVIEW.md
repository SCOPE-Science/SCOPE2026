# Scientific review

**Claim assessed:** The complete class-selection and first-entrance-time law for synchronous random-majority dynamics on triangular books \(B_m=K_2\vee\overline K_m\), for all even \(m\ge2\), together with the uniform-start oscillation limit. The domain and notation are as in RESULT.md.

## Correctness: PASS

The two hubs have odd degree \(m+1\) and hence no tie. When equal their next opinions coincide; every leaf becomes the common hub opinion, and the following configuration is either unanimous or in the designated two-cycle. When opposed the leaves use independent fair tie coins, generating a fresh binomial count. The hub outputs are both zero below the half threshold, both one above it, and opposed at equality. At a balanced opposed state the number of rounds before leaving the balanced state is geometric with success probability \(1-c_m\); binomial upper/lower-tail symmetry fixes both the exit color and the final class probabilities. Fresh leaves at the subsequent agreeing-hub state yield one- or two-step terminal entrance, with probability \(d_m\) for one step. These steps prove the complete generating functions, expectations, variances, and uniform-start selection probabilities, and exclude other recurrent classes. The geometric factor has success probability strictly positive for all even \(m\ge2\). The analytic proof handles all such \(m\), unlike finite checking.

The independent exact-rational absorbing-chain checker reconstructs all \(4(m+1)\) aggregate states at \(m=2,4,6,8\) and tests all three terminal-class probabilities and the first two entrance-time moments, passing 480 state identities. Potential boundary errors were reviewed at \(k=0,r,m\), and initial terminal times were correctly assigned zero.

## Originality: PASS, subject to unindexed-priority uncertainty

The primary research article is A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1 (2023-02-14). Its model definition, cycle-graph section, general stabilization and absorbing-state sections, and relevant appendix material were examined from the available full HTML. Those results include cycle-graph outcomes and general constructions, but do not give the full triangular-book class-selection and hitting-time distribution. The complete graph \(B_m\) has triangles and two adjacent universal hubs, so the previously known complete-bipartite or cycle cases cannot imply this statement directly. Out–Zehmakan (arXiv:2109.14265) treats a different, tie-retaining majority rule; its relevant accessible sections were read. The abstract of Benjamini et al. (arXiv:1405.2486) was also checked, without inferring full-text noncoverage from the abstract. Published mathematical research record searches on book graphs, adjacent hubs, fair tie-breaking and stochastic absorption exposed no statement that covers all parts of this theorem; failure to find such a statement is not a proof of absolute priority. A closely related complete-bipartite calculation likewise does not cover the nonbipartite graph or its absorption times.

## Value: PASS

Two mutually influential vertices with common neighbors are a natural minimal clustered social network, and the triangular-book family gives a connected nonbipartite graph with unboundedly many triangles. It is mathematically substantive that for every even size all initial profiles have exactly three terminal classes, with an exactly solvable outcome law and full time generating function. The asymptotic oscillation probability \(1/2\) under fair random initialization shows that clustering and triangles do not force consensus under this update; the unbalanced-versus-balanced initial hub cases also reveal a geometrically distributed delay not detectable from consensus probabilities alone. These are useful graph-specific structural quantities rather than an arbitrary finite census or a restatement of a known general identity.

## Closest literature and limitations

Source-specific comparisons and residual priority risks are recorded in AUDIT.json. Generalizations to odd \(m\), perturbations of the graph, and asynchronous or correlated updates are unproved. Finite tests are not substitutes for a universal mathematical proof. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
