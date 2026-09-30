# Independent audit — Exact moduli and area spectrum of a translation-self-polar planar family

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/translation-self-polar-moduli-area-spectrum--0367c8ee18b6`  
**Audited tree:** `c856e89e059e40b8c58ca69c45660c8ead720952`

## Disposition

**PASSED.**

## Correctness

**PASS.** The classification and area law survive independent reconstruction. Every selected vertex lies on one fixed strictly convex circle, so equality of bodies recovers the logarithmic orbit and any affine equivalence must carry that circle to itself; hence it is Euclidean and acts on the parameter by x↦±x modulo 2η. Independently computing polygon areas from the defining vertices for m=0.7, 2, and 5 at x=0, 0.3η, and η agrees to floating-point precision with sinh(2η)∑sech(x+2nη). Poisson summation gives the stated Fourier coefficients, and the standard Fourier series of Jacobi dn with q=exp(-π²/(2η)) gives the displayed dn representation; dn is strictly decreasing on [0,K], yielding the strict moduli coordinate and endpoint extrema.

## Originality

**PASS.** PASS with an explicit recency limitation. Segal's September 2026 preprint supplies the translated-self-polar construction and the negative answer motivating this family, but targeted searches for its identifier together with the periodized-sech area law, Jacobi-dn spectrum, and affine-moduli classification did not locate those refinements. The earlier SCOPE record `2026/09/17/analytic-rigidity-of-milman-polar-sum-equation--8d105c333ef0` concerns rigidity of a different functional on analytic positive-curvature bodies and does not contain this explicit-family moduli or area spectrum. The full arXiv text of Segal's very recent v1 was not independently retrievable in this run, so contemporaneous or source-text overlap remains a stated residual priority risk rather than being silently excluded.

## Scientific value

**PASS.** The result turns an existence construction into an exact one-dimensional affine-congruence moduli space with a strictly monotone intrinsic coordinate. The closed periodized-sech/Fourier/Jacobi formula and the proof of uncountably many pairwise non-affinely-equivalent translated-self-polar bodies add concrete geometric structure beyond the motivating counterexample.

## Independent checks

- Reconstructed the equality and affine-equivalence argument from the common construction circle and its two accumulation points.
- Numerically formed finite vertex sets for m=0.7, 2, and 5 and compared their shoelace areas with the periodized-sech formula at three phases; discrepancies were at machine precision.
- For m=2 obtained A(0)=5.11577564606935 and A(η)=4.96650163011354, matching the record.
- Matched the Poisson-series coefficients to the standard Jacobi-dn Fourier expansion and checked strict decrease on the fundamental interval.

## Evidence and literature

- https://arxiv.org/abs/2609.12685 — Alex Segal, Self-dual sets up to a translation: a negative answer to Milman's question (2026); underlying construction and translated-polar context.
- https://dlmf.nist.gov/22.11 — DLMF Jacobi elliptic-function Fourier expansions used to identify the periodized-sech series with dn.
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/analytic-rigidity-of-milman-polar-sum-equation--8d105c333ef0 — Earlier SCOPE result on analytic rigidity; inspected and found mathematically distinct from the assigned explicit-family moduli theorem.

## Limitations

- The classification is only for Segal's explicit planar alpha-family, not all K with K^circ=K-s.
- The origin-based polar area product is not a Santaló-minimized Mahler product.
- Segal's source is extremely recent; its full v1 text was not independently retrievable during this run, leaving residual priority risk.

## Repository identity

The assigned source-tree SHA `c856e89e059e40b8c58ca69c45660c8ead720952` exactly matched the current tree at the audited path on `main`; GitHub was read only during this audit.
