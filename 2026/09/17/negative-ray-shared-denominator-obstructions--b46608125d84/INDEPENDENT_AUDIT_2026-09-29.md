# Independent audit — 2026-09-29

**Record:** `2026/09/17/negative-ray-shared-denominator-obstructions--b46608125d84`  
**Audited source tree:** `3cab70dbbe79e2b30374e9e70ad9337169044701`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** PASSED

## Correctness

PASS. The uniform-closure argument is exact: a rational function that is bounded on (-infinity,0] has a finite limit at -infinity, uniform limits preserve that limit, and the compactification y=-x/(1-x) converts every f with a finite endpoint limit into a continuous function on [0,1], so polynomial approximation yields the common denominator (1-x)^n. For f(x)=e^{ix}, any finite-error rational approximant is bounded and hence approaches a single limit L at -infinity, while the target alternates between 1 and -1 along two sequences; this gives E_n>=1 and r=0 gives equality. For g(z)=e^z sin(e^{-z}), the points x_k=-log((k+1/2)pi) give alternating values (-1)^k/a_k. An error below 1/a_{2n+1} forces 2n+1 sign changes of Re r, but Re(p/q) has real numerator p q# + p# q of degree at most 2n and pole-free denominator, proving the algebraic lower bound. I also checked the topological objection to the cited proof: the slit plane is simply connected and infinity is a boundary point there, so it cannot have the asserted exterior-disk normalization with infinity as an interior point.

## Originality

PASS, qualified. The cited 2025 Mathematics article was inspected in open full text and does state the broad shared-denominator geometric theorem for functions analytic in the slit domain, with the exterior-domain conformal step challenged here. Searches through September 29 found no published correction or equivalent pair of counterexamples. The qualitative compactification closure itself is elementary and is not treated as the novelty; the contribution is the explicit obstruction to the published no-assumptions theorem, including a finite-limit entire example with a quantitative nongeometric lower bound.

## Scientific value

PASS. The record identifies a false general theorem in current numerical-analysis literature, gives two transparent counterexamples that separate qualitative convergence from geometric rate, and pinpoints the geometric failure in the proof without overclaiming against the paper's phi-function computations. That is clear corrective scientific value.

## Evidence and literature

- https://doi.org/10.3390/math13243985 — A. H. Al-Mohy, Shared-Pole Caratheodory--Fejer Approximations for Linear Combinations of phi-Functions, Mathematics 13 (2025), 3985; open full text inspected for Theorem 1 and its conformal setup.
- https://arxiv.org/abs/2609.14489 — T. Schmelzer, The 1/9-problem for the phi-functions; scalar best-approximation asymptotics for fixed phi-functions, distinct from simultaneous shared-denominator optimality.

## Limitations

- The record refutes the theorem at its stated generality but does not determine the optimal simultaneous common-denominator rate for the specific phi-function family.
- No correction or follow-up covering these examples was located through 2026-09-29; absence from search is not itself a proof of priority.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit changes only the independent-audit verification channel and does not alter Lean or expert-attestation channels.
