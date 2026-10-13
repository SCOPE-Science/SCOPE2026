# Self-review

## Correctness — PASS
The displayed state is normalized by \(9+4+36+9=58\). The global bipartition is already in Schmidt form, so the order-\(2\) purity is exactly \(737/1682\). Both direct-pair X-state reductions have concurrence \(24/29\), and the defining source’s exact two-qubit formula reduces at order \(2\) to \(-\log_2(1-C^2/2)\). The resulting residual ratio is \(611618/619817<1\). The packaged exact-arithmetic checker reproduces every rational identity. The claim is not based on sampling or on the checker alone.

## Originality — PASS
The closest source, Cornelio–de Oliveira (arXiv:0906.0332), establishes four-qubit violations numerically and reports approximate spectra and entanglement values; it does not provide this amplitude vector or exact residual. Focused searches covered the source title, exact coefficient pattern, exact residual integers, strong-superadditivity wording, second-order-monogamy aliases, and later Rényi-entanglement literature. Kim–Sanders and Wang–Mu–Vedral–Fan address broader formulas/monogamy but no retrieved statement implies this witness. Gour–Wallach concerns a different four-qubit extremal problem. Residual risk is an obscure or poorly indexed exact witness.

## Value — PASS
An exact four-term state is materially more informative than an opaque numerical optimizer output: every reduction and the violation can be checked by hand, and the witness sits in the natural maximally correlated subspace \(\operatorname{{span}}\{{|xyxy\rangle:x,y\in\{{0,1\}}\}}\). The result supplies a clean analytic certificate for a phenomenon whose defining paper emphasized the difficulty of finding numerically. It does not claim global optimality or a full classification.

Self-review: passed. Independent audit: not yet performed.
