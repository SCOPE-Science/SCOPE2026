# Independent Audit — Binary classification of even exactly k-deficient-perfect numbers with two prime factors

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `d7f70175190d437f7a170b9dd9512c9ef6ba695d`  
**Audited current source tree:** `d7f70175190d437f7a170b9dd9512c9ef6ba695d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

GitHub was used only as read-only evidence. A repository comparison from the assignment inventory snapshot to the audited current `main` commit found no file changes under this record, so the audited tree equals the assigned source tree. The `INDEPENDENT_AUDIT_2026-09-30.md` and `.json` marker files were absent before this guarded plan was prepared.

## Correctness — PASSED

PASS. For n=2^a p^b and M=2^{a+1}-1, direct cancellation gives Delta=2n-sigma(n)=t+(t-1)(p+...+p^{b-1}) with t=p-M. Positivity forces p>M. Since Delta<p^b, every selected deficient divisor has p-adic exponent at most b-1. Grouping selected divisors by p-adic layer gives coefficients A_j that are subset sums of 1,2,...,2^a, hence 0<=A_j<=M<p. Base-p uniqueness therefore forces A_0=t and A_j=t-1 for j>=1, which in turn forces p<2M. Conversely, M<p<2M makes these digits valid unique binary subset sums, proving existence and uniqueness and the Hamming-weight formula k=s_2(t)+(b-1)s_2(t-1). Independent exact subset-sum enumeration for small a,b and odd primes reproduced the criterion and unique cardinality with zero mismatches.

## Originality — PASSED

PASS, narrowly scoped. Tang–Ren–Li (2013) determine deficient-perfect numbers with at most two distinct prime factors, which is the k=1 case. Chen (2019) treats exactly k-deficient-perfect numbers and classifies the odd exactly-2 two-prime case, while Aursukaree–Pongsriiam classify the odd exactly-3 case with at most two prime factors. Targeted searches did not locate the submitted arbitrary-k classification for the even 2^a p^b slice, its unique deficient-divisor representation, or the binary Hamming-weight formula. Prior k=1 and odd k=2,3 classifications receive no novelty credit.

## Scientific value — PASSED

PASS. The theorem completely solves a natural infinite two-prime-support family for every k, proves uniqueness rather than mere existence of the deficient-divisor set, recovers the known k=1 family, and turns fixed-k questions into explicit binary-weight conditions. Bertrand's postulate also supplies existence for every exponent pair (a,b), giving a clean global picture within the stated slice.

## Independent checks

- Re-derived the deficiency identity and the necessity of p>M.
- Checked the base-p digit uniqueness argument and binary subset uniqueness in every p-adic layer.
- Re-derived the endpoint k bounds and the fixed k=2 and k=3 slices.
- Independently performed exact subset-sum checks on a small parameter grid; every qualifying case had exactly the submitted k and a unique representation.
- Compared with the open Tang–Ren–Li 2013 article, Chen 2019, Aursukaree–Pongsriiam 2021, and current OEIS descriptions; no arbitrary-k even two-prime classification was located.
- GitHub compare found no changes under the assigned record path; the dated audit pair is absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The classification is only for even integers with exactly two distinct prime factors.
- It does not settle which fixed values of k occur infinitely often.
- An equivalent theorem under older divisor-partition terminology remains a residual priority risk despite targeted searches.

## Evidence and references

- https://doi.org/10.4064/cm133-2-8
- https://eudml.org/doc/284301
- https://math.colgate.edu/~integers/t37/t37.pdf
- https://doi.org/10.1080/00150517.2021.12427539
- https://oeis.org/A331627
- https://oeis.org/A331628
- https://oeis.org/A331629
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/even-k-deficient-perfect-binary-classification--8124957e2aa5

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
