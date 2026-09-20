# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The standard classification was checked directly. With a root in one part pinned at zero, the opposite part has values in \(\{-1,1\}\). If both signs occur, the rooted part is forced to zero; if only one sign occurs, every other vertex in the rooted part has exactly two choices. This gives \(2^a+2^b-2\) functions, exactly two of range one, and all others of range two.

For the lazy model, the opposite part has values in \(\{-1,0,1\}\). Splitting by its exact image gives four disjoint types: singleton image; one of the two adjacent two-point images; the nonadjacent image \(\{-1,1\}\); or all three values. Intersecting the allowed unit intervals for the rooted part gives respectively three, two, one, and one choices per free coordinate where applicable, yielding the stated closed count. Diameter at most two bounds the range by two. Range at most one is equivalent to the image lying in \(\{0,1\}\) or \(\{-1,0\}\), giving the stated coefficients by inclusion-exclusion.

The fixed-order extremizers follow from strict discrete convexity. For the lazy count, \(F(k)=3^k-2^{k+1}\) has second difference \(4\cdot3^{k-1}-2^k>0\). Thus the symmetric fixed-sum count is smallest at the balanced split and largest at a star. Monotonicity of the expectation in the relevant total count transfers the extremizers.

A standalone verifier exhaustively checks every rooted assignment for all \(1\le a,b\le4\), comparing the total count and each range coefficient to the theorem. All checks pass. The computation is supporting evidence and is not required by the proof.

## Originality

Originality is assessed **to the best of our knowledge**.

The directly relevant recent source is Yinfeng Zhu, arXiv:2609.19728v1 (17 September 2026). Its full accessible HTML was inspected. It defines both models, proves the standard and lazy path extremality results, and uses \(K_{2,3}\) as a running example. In that example it explicitly finds 10 standard functions with expected range \(9/5\), and 45 lazy functions with expected range \(58/45\). Searches within the full text found no general “complete bipartite” treatment. The formulas here recover both numerical examples.

The older standard source, Benjamini--Häggström--Mossel (2000), was checked through its bibliographic record and abstract, which describe general inequalities and selected special families but do not expose a complete-bipartite formula. The version-of-record full text was not completely inspected and is the most plausible older source capable of containing an unindexed elementary special-case enumeration.

The Loebl--Nešetřil--Reed (2003) lazy-model paper was checked through indexed bibliographic/abstract material. Its accessible abstract states the general 1-Lipschitz mapping problem, but the full article was not completely inspected. It is therefore another explicit residual originality risk.

Broader searches covered “complete bipartite”, \(K_{m,n}\), graph homomorphisms into the integers, graph-indexed random walks, integer 1-Lipschitz functions, exact expected range, and synonymous homomorphism-to-path formulations. Exact searches using the characteristic expressions \(2^a+2^b-2\) and the lazy exponential combination did not reveal equivalent formulas. No stronger or equivalent fixed-order extremal classification was found.

The remaining risks are an older result under different terminology, an unindexed observation in the two incompletely inspected classical articles, or very recent parallel work.

## Value

The theorem upgrades the isolated \(K_{2,3}\) calculations in the newest source to complete range distributions for every complete bipartite graph, in both the standard and lazy models. It also gives a fixed-order shape theorem: stars and balanced bicliques are the unique extrema, up to exchanging the parts.

The lazy asymptotics show a qualitative phenomenon not visible from the general path bound: within the dense canonical family \(K_{a,n-a}\), the expected range can converge either to 1 or to 2 solely by changing the balance of the bipartition. The formulas also provide exact finite test cases for future distributional or formal-verification work on graph-indexed random walks.

## Limitations

The formulas are specific to complete bipartite graphs and the uniform standard/lazy models. They do not resolve the stronger stochastic-domination form of the BHM conjecture. The 2000 and 2003 classical articles were not both completely inspected in full text, so older unindexed coverage remains a concrete originality risk. Finite computation does not replace the proof. Independent audit has not been performed.
