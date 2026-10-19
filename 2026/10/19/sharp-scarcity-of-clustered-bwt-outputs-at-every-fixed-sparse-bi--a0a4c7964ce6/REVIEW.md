# Scientific review

## Correctness — PASS
The claim is a two-sided asymptotic count for each **fixed** weight \(k\ge4\), not a claim of exact enumeration. The proof separates BWT ones using the lexicographic order of initial zero-run lengths, then bounds all failures by the union of explicit integer-hyperplane neighborhoods among the cyclic gap compositions. A positive-volume family with two tied maximal gaps gives the matching lower bound. The marked-one-to-word factor \(n/k\), distinct interpretations of linear and cyclic runs, nonconstant-word endpoint lemma, and strict inequalities in the separator construction were checked. Direct exhaustive rotation-sort verification on 190,890 words agreed with the deterministic lemmas. The finite checks are corroboration, not substitutes for the analytic proof.

## Originality — PASS, subject to external priority review
The 1994 definition paper and the 2017 clustering-ratio paper were materially inspected, including their core theorems and examples. The 2017 theorem \(\rho(\operatorname{BWT}(w))\le2\rho(w)\) uses **input run count** as its parameter, and its explicit extremal constructions are not a sharp counting theorem for uniformly selected fixed-weight inputs. The 2017 fixed-point paper asks for \(\operatorname{BWT}(w)=w\), a different condition; its full text could not be retrieved and remains a stated bibliographic risk. No examined primary result proves the stated uniform family of sharp \(\Theta_k(n^{k-1})\) exceptional counts for all \(k\ge4\). Searches cannot rule out an unindexed equivalent derivation, and this assessment is not independent validation.

## Value — PASS
The theorem answers a naturally motivated data-compression combinatorics question: does the BWT cluster repeated bits when the number of rare symbols is fixed and the block becomes long? It gives a sharp negative answer **in the run-count statistic**, identifies a testable deterministic gap certificate, and quantifies the nonmaximal cases to optimal order. Unlike individual fixed-weight computations, it is valid for every fixed number of rare symbols at least four. It does not imply comparable bit-rate performance, a uniform regime of growing Hamming weight, or exact leading constants.

Self-review: passed. Independent audit: not yet performed.
