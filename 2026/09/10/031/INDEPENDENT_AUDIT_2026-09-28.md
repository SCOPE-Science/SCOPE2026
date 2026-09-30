# Independent Audit — 2026/09/10/031

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `47b1f61d6df69077e787bb98983d2a73323e2dec`  
**Audited current source tree:** `47b1f61d6df69077e787bb98983d2a73323e2dec`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. I independently reconstructed the signed 28×28 base adjacency matrix from the logged 42-edge order and 42 signs. The signing has exactly 21 positive and 21 negative base edges. Numerical diagonalization gives ρ(A_t)=2.61049984694..., consistent with the claimed [2.6104,2.6105) interval. I separately verified the exact Rayleigh certificate from the archived integer vector: w^T A_s w=2610502980388, w^T w=1000001200328, and 10000·num−26104·den=998470517888>0. For the upper endpoint I performed exact rational LDL^T on (26105/10000)^2 I−A_t^2; every pivot is positive, proving ρ(A_t)<2.6105. Since A_s=[[0,A_t],[A_t,0]], ρ(A_s)=ρ(A_t). Exact integer traces independently reproduce Tr A_t^4=420, Tr A_t^6=2436, Tr A_t^7=−168, Tr A_t^8=14964, while the unsigned graph gives 420,2436,336,15540. The logged unsigned graph has the published Coxeter spectrum/intersection data and its 28 vertices/42 edges/girth-7 identity is consistent with standard references.

## Originality

SUPPORTED AS AN EXPLICIT COUNTEREXAMPLE/CERTIFICATE. General signing and 2-lift theory is classical and remains active; the record's contribution is this particular balanced fibre-symmetric Coxeter-cover witness and exact spectral enclosure, together with the short-walk trace-rigidity observation. A targeted search for the exact spectral value/witness did not reveal a prior publication; that negative search is treated only as supporting context, not a proof of novelty.

## Scientific value

STRONG BENCHMARK VALUE. The witness decisively refutes the proposed universal lower exclusion with a large margin and the trace argument explains why the proposed Tr4/Tr6 obstruction could never work on a girth-7 cubic base. The record appropriately does not claim optimality of the signing.

## Limitations

- The true optimum over the constrained signing class is not determined.
- The base-graph identity is supported by its explicit construction/invariants rather than an external canonical-label certificate, though the spectrum and intersection data match the Coxeter graph reference exactly.
- Floating-point diagonalization was used only as an independent sanity check; the decisive upper/lower spectral bounds were reverified with exact rational/integer arithmetic.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/031
- https://doi.org/10.1017/S0963548304006509
- https://www.math.mun.ca/distanceregular/graphs/coxeter.html
- https://doi.org/10.1007/s00493-006-0029-7
- https://annals.math.princeton.edu/2015/182-1/p07
