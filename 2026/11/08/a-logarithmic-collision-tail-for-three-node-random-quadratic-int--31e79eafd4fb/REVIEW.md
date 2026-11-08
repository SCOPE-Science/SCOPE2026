# Scientific review

**Correctness — PASS.** PASS: Ordered-node density 6; three exact rational Lagrange formulas; global bound W<=sqrt(3)/(st); hierarchy decomposition makes large-gap and comparable-gap regions O(1/T); each unbalanced small-gap region contributes half-log area times 6sqrt(2) integral, giving total 6sqrt(2)(z^2-z+1/3). Remainder near endpoints or z has arbitrarily small leading coefficient. Layer cake gives p<1; Gaussian conditioning gives corresponding error moment law. checker.py passed 12 symbolic identities and diagnostics for z=0 and 1/2. Proof of infinite T-tail does not rely on simulation.

**Originality — PASS, qualified.** PASS with residual precedence risk: Compared actual published-finding corpus searches, own random quadratic interpolation/affine-exact claims, and inspected primary literature. Their settings or implications do not establish the iid three-node logarithmic tail coefficient. General interpolation identities and collision estimates are acknowledged; no claim of absolute literature uniqueness.

**Value — PASS.** PASS: Basic iid node sampling for quadratic interpolation has a different and much worse tail (log T)/T than stratified one-per-cell interpolation; even the mean absolute Gaussian-noise error is infinite. Exact coefficient reveals how evaluation location controls the risk and diagnoses a concrete reason to enforce spacing or conditioned designs. Natural complete minimal three-node classification, not a numerically arbitrary slice.

The nearest primary work is Kunis and Nagel, arXiv:1812.08645, deterministic Fourier Vandermonde near-collision conditioning; and Dolbeault and Chkifa, arXiv:2306.07435, designed stable sampling. The directly checked prior interpolation results differ in their random node constraints or polynomial exactness. The strongest residual risk is an unlocated equivalent tail calculation in probability or random Vandermonde literature. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
