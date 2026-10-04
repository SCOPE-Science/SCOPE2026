# Review of Exact two-read single-deletion reconstruction optimum at binary length \(7\)

## Correctness
PASS. The claim is finite and fully quantified. `certificate.json` supplies a size-\(70\) compatible set and a proper \(70\)-coloring of the complete compatibility graph on all \(128\) binary length-\(7\) words. `verify.py` reconstructs deletion balls from first principles and checks both certificates pairwise. `search.py` separately rebuilds the graph and performs an exact branch-and-bound maximum-clique search, returning \(70\). The proof uses no extrapolation from smaller cases.

## Originality
PASS, with residual risk. The closest primary sources define the same two-read single-deletion problem, Type-A confusability, and the graph-theoretic clique-cover method, but the inspected statements give constructions and asymptotic bounds rather than the exact length-\(7\) value. Exact-value, graph-alias, redundancy, table, and implication searches did not locate a source stating \(70\). A poorly indexed or unpublished finite computation could still overlap.

## Value
PASS. The exact value concerns the central finite invariant \(\rho(n,2;D_1)\) explicitly posed by the foundational work, not a renamed metric. The matching independent-set/clique-cover certificates sharpen the same graph framework used for the asymptotic lower bound and provide a reproducible finite benchmark for constructions and bounds.

## Closest literature and limitations
Cai–Kiah–Nguyen–Yaakobi (arXiv:2001.01376v1) introduce the fixed-read reconstruction-code problem and the two-read single-deletion case. Chrisnata–Kiah–Yaakobi (arXiv:2004.06032v1) characterize Type-A-confusable pairs, define the confusability graph, and prove \(\rho(n,2;D_1)=\log_2\log_2 n+\Theta(1)\). The present claim is exact only for \(n=7\), does not imply a general finite formula, and leaves classification of all optima open.

Same-model review: passed. Independent audit: not yet performed.
