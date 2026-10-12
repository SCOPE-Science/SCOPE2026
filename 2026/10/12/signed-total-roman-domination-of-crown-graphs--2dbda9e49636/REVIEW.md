# Review

## Correctness
PASS. For each deleted pair index \(i\), the exact open-neighborhood inequalities are \(Y-y_i\ge1\) and \(X-x_i\ge1\). Any shore containing a label \(2\) has sum at least \(3\); a shore without a label \(2\) has sum at least \(2\). A putative total weight at most \(5\) forces one shore sum to equal \(2\); for \(n\ge4\) this shore then contains a label \(-1\) but no label \(2\), forcing the opposite shore to contain a label \(2\) and no label \(-1\), hence to have sum at least \(n+1\ge5\). The \(n=3\) shore-sum-two case is excluded by parity. Explicit constructions give weight \(6\) for both parities. At equality, both shore sums are \(3\), which yields the stated label-count equations and the exact rescue compatibility rule. The bundled checker independently confirms the result and minimum counts for \(3\le n\le8\).

## Originality
PASS with stated residual access risks. Searches covered “crown graph,” \(K_{n,n}-M_n\), “complete bipartite minus perfect matching,” the bipartite-Kneser alias \(H(n,1)\), STRD/STRDF terminology, and minimum-function counting. The closest same-invariant literature gives the complete-bipartite baseline, general complexity, recent cubic/complete-multipartite results, and single-edge modification questions; none of the accessible statements implies the crown-family theorem or the minimum-function census. The full text of the 2026 same-invariant preprint and the 2025 edge-modification article was unavailable during this review, so an equivalent hidden statement in either source remains a residual risk.

## Value
PASS. Crown graphs are a canonical dense regular bipartite family obtained by one structured perfect-matching deletion from \(K_{n,n}\). The theorem shows a sharp perturbation effect: the known complete-bipartite value is \(2\) for \(n\ne3\) and \(4\) for \(n=3\), whereas every connected crown graph has value \(6\). The result also classifies and counts all optimizers rather than supplying only a scalar minimum.

## Closest literature and limitations
Zhao–Miao gives the exact complete-bipartite baseline. Koster–Volkmann–Wehrmann is the closest recent source by invariant and treats cubic and complete multipartite graphs. Guo–Volkmann–Wang explicitly considers edge deletion/subdivision effects. The accessible material from the latter two sources does not state this perfect-matching-deletion theorem, but lack of full-text access is preserved as an originality risk. The theorem does not address arbitrary partial matching deletions or general dense bipartite graphs.

Self-review: passed. Independent audit: not yet performed.
