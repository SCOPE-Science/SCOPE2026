# Independent Audit — complex-plucker-sharp-constants--7196b90b39f6

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `650dfdddd558254abd6c0c5c9c29b7e318d48688`  
**Audited current source tree:** `650dfdddd558254abd6c0c5c9c29b7e318d48688`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. At p=2, Cauchy--Binet plus the Gram-Hadamard inequality gives norm 1. At p=infinity, row-wise Hadamard gives at most n^(n/2), and the unnormalised complex Fourier matrix attains that value in every order. Multilinear complex interpolation between these endpoints yields n^{n(1/2-1/p)} for 2<p<infinity, and the same Fourier frame attains it because each row has l^p norm n^{1/p}. As an independent numerical sanity check, for n=3,p=4 the Fourier-frame ratio is 2.279507056954778, equal to 3^(3/4). The real-scalar continuity corollary follows by 1<=C_R<=C_C and squeezing as p decreases to 2.

## Originality — PASSED

PASS, WITH A SCALAR-FIELD QUALIFICATION. Feldman's source explicitly leaves p>2 exact constants, 2+ continuity, and fixed-n p-growth open, and bases its lower bound on real {+/-1} Hadamard matrices. Its own proof uses multilinear complex interpolation and complex-matrix language. The record's new point is the complex-scalar completion using Fourier complex Hadamards in every order. Searches did not locate the exact Plucker-coordinate formula elsewhere, but older tensor/compound-matrix literature remains a residual priority risk; the classical ingredients are not claimed as new.

## Scientific value — PASSED

PASS. The formula resolves the source's entire supercritical complex regime, identifies exact extremizers, settles its complex continuity/asymptotic questions, and clarifies the real-versus-complex boundary. The argument is short but materially changes the status of the recent open sharp-constant problem.

## Independent checks

- rederived both endpoint norms and the complex interpolation exponent
- independently evaluated the n=3,p=4 Fourier extremizer
- checked Feldman Remark 2.2/Problem P1 in open arXiv HTML
- verified current tree SHA and absence of 2026-09-29 audit markers

## Limitations

- The source preprint does not put a scalar-field convention next to every statement; the audit supports the record's interpretation that the complex case is naturally included, but a strictly real authorial intent would make this a complementary theorem rather than a correction.
- Older tensor-norm and compound-matrix literature was searched but not exhaustively book-by-book; priority is therefore qualified.
- No claim is made that the real constant is determined in non-Hadamard orders.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/complex-plucker-sharp-constants--7196b90b39f6
- https://arxiv.org/abs/2608.00983
- https://arxiv.org/abs/quant-ph/0512154
