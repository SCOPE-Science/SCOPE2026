# Review

## Correctness

PASS. The four displayed marker sets satisfy the source's \(L=3\) separation and coverage conditions. Each of the four overlap equations holds with canonical witness \(-1\), and witness uniqueness follows because two possible witnesses would place two points at distance at most \(2\) inside a \(3\)-separated set. Hence the closed four-walk has total canonical direction \(-4\), directly falsifying the zero-sum property at \(L=3\). The finite verifier exhausts all \(2^{13}\) candidate subsets and confirms the exact census \(59\) vertices, \(75\) edges, \(4\) simple four-cycles, with exactly one bad cycle.

## Originality

PASS. Wang states and proves the canonical construction only for \(L\ge4\); full-text searches found no treatment of \(L=3\) and no sharpness statement. Focused published-result searches for \(M_{1,3}\), the marker-window parameter, four-walk direction sums, and the \(L=3\) boundary found no equivalent result. Wang's Proposition 7.7 concerns the stated regime \(L\ge4\) and does not imply the excluded boundary or its unique bad cycle.

## Value

PASS. The parameter \(L\ge4\) is load-bearing in the marker-window construction that produces the finite targets separating successive continuous-homomorphism dimensions. The result identifies the exact first boundary failure rather than merely observing that the published proof uses \(4\): it exhibits the obstruction and shows by complete census that a single simple four-cycle is responsible. This is a motivated boundary counterexample useful for any attempt to shrink the marker window or modify the direction certificate.

## Closest literature and limitations

The closest source is Wang's 2026 preprint itself: Lemma 7.3 proves the canonical zero-sum property for every \(L\ge4\), while its proof uses the inequalities \(L+4\le2L\) and \(4\le L\). The source contains no \(L=3\) analysis. Gao--Jackson--Krohne--Seward provide the earlier continuous-combinatorial setting but not this marker-window graph.

The claim is deliberately limited to Wang's canonical translation-witness labels on \(M_{1,3}\). It does not assert impossibility of some different abstract edge-direction assignment.

Self-review: passed. Independent audit: not yet performed.
