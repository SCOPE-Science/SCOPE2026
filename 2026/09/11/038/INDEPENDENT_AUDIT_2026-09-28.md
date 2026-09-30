# Independent audit — 2026-09-28

Record: `2026/09/11/038`  
Audited tree: `51a0e57596afe1c0cbf21b178455ef0d7cd953f1`  
Disposition: **passed**

## Correctness

A fresh Laplacian calculation on the stated 8-vertex multigraph reproduces genus 5 and degrees `[4,4,4,4,2,2,2,2]`. Exhaustive exact lattice-equivalence checks show every singleton subtraction `D*-q` is equivalent to an effective degree-2 divisor, while exactly 18 vertex-pair subtractions are non-effective; in particular `(0,4)` is a valid rank-<2 witness. Thus the finite-graph Baker–Norine rank is exactly 1.

The record is overly cautious when it says the metric rank is not formally closed by its artifact. Hladky–Kral'–Norine prove Baker's conjecture that a divisor on a graph has the same rank on the corresponding unit-length metric graph. Therefore the stated finite rank also supplies the metric rank needed for the tropical interpretation. I did not rely on the artifact's edge-split sweep.

## Originality and value

Melo–Zheng and Aidun et al. address trigonal curves/graphs under stronger connectivity hypotheses; the present graph has edge-connectivity 2. Targeted searches did not locate this exact square-backbone divisor computation. The exact rank on a natural small genus-5 closed loop assembly is a defensible finite invariant, with no lifting/non-liftability theorem claimed.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/038 ; https://arxiv.org/abs/0709.4485 ; https://arxiv.org/abs/2501.03903 ; https://alco.centre-mersenne.org/articles/10.5802/alco.80/
