# Same-model review

## Correctness
PASS. The source formula gives \(R_e\le\tau\), so every season with \(\tau<1\) has zero infections. In a zero-infection block the population vector shifts deterministically and forgets its initial value after \(r-1\) seasons; the immunity recursion over the same block depends only on new drift marks. This proves a common \(r-1\)-step component of mass \(\beta^{r-1}\) for every initial state. The total-variation contraction and stationary-law conclusions then follow. The included exact-rational checker is a consistency test only; the arbitrary-\(r\) proof is symbolic.

## Originality
PASS. The full motivating article was inspected. Proposition 2.1 proves qualitative stationary convergence under a continuous-density hypothesis and a positive atom at complete drift, and the following remark explicitly says that removing the atom may be possible while treating only \(r=2\) separately. Exact-title, identifier, regeneration, Doeblin, uniform-ergodicity, geometric-mixing, and atom-removal searches found no arbitrary-\(r\) theorem for this model. Published comparison-database searches likewise found no covering result. Generic Doeblin theory supplies the standard implication from a global minorization to uniform ergodicity but not the model-specific \(r-1\)-season coalescence or the constant \(\beta^{r-1}\).

## Value
PASS. This closes a stated structural gap in the source for all finite immunity-memory lengths and strengthens qualitative convergence to an explicit initialization-uniform total-variation rate. The rate directly quantifies loss of dependence on the unknown incoming immunity state, which is relevant to stationary simulation burn-in and long-run epidemic prediction.

## Closest literature and limitations
The closest primary source is Britton–Pugliese, DOI 10.1007/s00285-025-02308-8 / arXiv:2505.17933. Standard global-minorization theory is background rather than covering prior work; DOI 10.1002/wics.70002 was inspected for that implication. The bound here is sufficient, not claimed optimal, and the theorem retains the source's iid assumption across seasons. It does not address models with serially dependent seasonal marks or statistical estimation of \(\beta\).

Same-model review: passed. Independent audit: not yet performed.
