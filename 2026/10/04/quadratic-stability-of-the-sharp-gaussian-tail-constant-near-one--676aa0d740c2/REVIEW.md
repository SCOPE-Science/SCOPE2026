# Same-model review

## Correctness
PASS. The proof separates the only nonstandard local step from the prior global theorem. If the residual support radius is smaller than the gap between the dominant coefficient and the threshold, conditioning on the residual sum makes the two-sided central interval have constant length, so the exact tail is \(1-t/a_1\). Uniform coupling to a single uniform variable and the prior uniqueness of \(t_0\) localize the global optimizer into that plateau. The derivative equation is then one-dimensional; the Mills-ratio identity gives strict monotonicity, uniqueness, and the implicit-function expansion. The optimized-value derivative correctly uses the envelope condition. `verify.py` reproduces the constants and independently stress-checks finite weighted-uniform convolutions.

## Originality
PASS, with residual historical risk. The lead sharp-tail paper states the global bound and the unique one-uniform threshold but gives no coefficient-space deficit or local Hessian for the optimized comparison constant. The inspected central-section stability papers concern different functionals; the closest distributional-stability theorem also imposes \(\|a\|_\infty\le1/\sqrt2\), excluding the one-sparse regime. Targeted indexed-record and web searches for the exact constants, aliases, one-sparse stability, weighted-uniform Gaussian comparison, and deficit formulations returned no equivalent statement. The calculation is elementary once the relevant localization is recognized, so an older differently phrased cube-slab or convolution result remains a genuine residual risk.

## Value
PASS. The sharp constant in the lead theorem is attained only in the sparse one-uniform geometry. Quantifying how that extremum deteriorates under desparsification is therefore a natural stability question, not an arbitrary slice. The result identifies the exact second-order loss \(\kappa\varepsilon^2\), shows that the tangent-space quadratic term is isotropic, and proves an exact local collapse from all residual coordinates to the single parameter \(a_1\). This supplies a quantitative near-equality law for a sharp probability inequality whose extremizer is otherwise only identified qualitatively.

## Closest literature and limitations
The closest inspected sources are arXiv:2305.06235v1, DOI:10.1214/22-AOP1584, DOI:10.1007/s00208-023-02669-9, DOI:10.1112/mtk.12225, and the Barthe--Koldobsky slab theorem DOI:10.1016/S0001-8708(02)00055-5. The result is local and does not give a global stability inequality or address the lead paper's higher-threshold extremizer conjectures.

Same-model review: passed. Independent audit: not yet performed.
