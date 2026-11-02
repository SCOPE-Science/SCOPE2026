# Self-review

## Correctness — PASS

The claim is reconstructed with explicitly quantified \(n\), a consistent worst-case landmark threshold, and a proof by exhaustive pair-intersection types. The two possible bisectors follow directly from \(d_{J(n,2)}(X,Y)=2-|X\cap Y|\). Their cardinality difference \(2(n-5)\) gives the threshold. Inclusion maximality is characterized by connected-component unions across a two-vertex cut; this supplies the special \(n=4,5,6\) cases and proves the stable range. Kneser transfer accounts for landmarks equal to the compared pair, where the positive-distance complement identity does not apply. A fresh independent all-pairs-distance program enumerates all bisectors for \(4\le n\le10\) and directly checks every subset at \(n=4,5\). The code reports `VERIFY_OK`. No finite enumeration is used as a proof for unbounded \(n\).

## Originality — PASS with priority risk

The earliest directly motivating source (Korivand–Khashyarmanesh–Tavakoli, 2022) computes the Petersen universal threshold only. Bailey et al. (2013) give resolving constructions and the ordinary minimum metric dimension, not maximal nonresolving sets. Kratica et al. (2024) work with equal-distance **existence** for each pair, a different quantifier; their full paper has no claimed universal threshold or inclusion-maximal nonresolving classification. Existing research records on metric thresholds of Hamming graphs and minimum equalizer sets of triangular/Kneser graphs concern different graph families or logically different objects. The candidate is not a mere restatement of the Petersen case or of equidistant dimension. The residual risk is an unlocated published bisector-classification theorem.

## Mathematical value — PASS

This is the complete worst-case failure geometry of a natural infinite family already used in metric-dimension and equidistant-dimension research. The large threshold (quadratic in root order) contrasts with the known linearly growing optimally placed metric dimension. Inclusion-maximal failures retain a second smaller structural orbit for all \(n\ge7\), invisible to the scalar threshold; the small cases exhibit genuine shifts. These precise obstruction profiles support exact worst-case landmark redundancy questions and provide useful, non-arbitrary graph-family information.

## Scope and residual limits

The theorem addresses two-subset Johnson/connected Kneser graphs, not higher Johnson levels. The verification range is finite; priority searches cannot exclude all unindexed sources. Independent mathematical audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
