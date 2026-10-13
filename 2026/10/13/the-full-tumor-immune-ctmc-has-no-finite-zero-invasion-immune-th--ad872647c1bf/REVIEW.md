# Self-review

## Correctness
PASS. The source's transition graph gives a finite positive-rate route from every finite state with nonzero tumor burden to the invasion boundary. Repeated immune-death jumps can first reach \(y=0\). On that face tumor death, immune birth, immune death, and cytokine production vanish, while tumor birth remains strictly positive for every \(1\le x<K\). A finite sequence of tumor births therefore reaches \(x=K\) with positive probability. Requiring every holding time in this finite path to be sufficiently short gives strict positivity on every finite horizon \(T>0\).

## Originality
PASS. The source itself emphasizes limitations of the frozen branching approximation but interprets its numerical zero count and deterministic immune-threshold crossing as making extinction certain in the fully coupled stochastic model. Exact-DOI, alias, published-finding corpus, and own-ledger searches found no equivalent source-specific correction. Older tumor stochastic literature establishes branching, CTMC, and extinction-threshold context but does not imply this exact transition-graph statement in the inspected material.

## Value
PASS. The result corrects the difference between suppression and impossibility in the exact model used for the paper's principal stochastic-invasion comparison. It also gives a mathematically precise reason that a zero count among \(10^4\) simulated paths cannot certify a zero invasion probability. This is a meaningful rare-event interpretation issue, not a change of notation or a routine recomputation.

## Closest literature and limitations
Merrill (1984), DOI 10.1007/BF00275990, is a classical branching/jump-process tumor-extinction reference. Liu, Li, and Pan (2018), DOI 10.1016/j.physa.2018.02.118, use a different tumor-immune CTMC for extinction probabilities. Yang, Tan, and Cheke (2019), DOI 10.1016/j.cnsns.2019.02.025, derive stochastic extinction and persistence thresholds in a different pulsed-treatment model. The accepted theorem does not estimate the source parameter set's exact rare-event probability, and it does not equate the exact CTMC with the article's tau-leaping approximation.

Self-review: passed. Independent audit: not yet performed.
