# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-shifted-vietoris-sine-threshold--df20aa3dc998`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `080b1f90ad6251535fef1e050ff27eca7672e4eb`  
**Disposition:** **PASSED**

## Correctness — PASS

The alternating half-mesh lemma is valid for absolutely continuous f with f(0)=0 and f' in L1. Applying it to u^(1-s) gives the even-n endpoint slope -1/2 n^(1-s)+o(n^(1-s)); the shifted-power error has summable first differences and is lower order. Applying the same lemma to u^(-s)sin(yu) gives the claimed 1/n boundary-layer profile, and adjacent pairing makes the shift correction O(n^-1) before multiplication by n^s. The s=0 case is exact. For sufficiency at s>=1, the source theorem covers the positive-exponent range; the boundary cases where one exponent is zero are independently closed by the Belov alternating-sum criterion using monotonic q_k, b_k=kq_k<=1 and the one-turn/unimodal logarithmic-derivative analysis in the record.

## Originality — PASS (literature-bounded)

Sangal–Swaminathan prove the sufficient Vietoris-type positivity range and state the Belov criterion, but the checked arXiv text does not state this shifted-family converse, the endpoint-slope asymptotic, or the universal fixed-y boundary layer. Searches combining the exact coefficient family, λ+μ threshold, necessity/sharpness, endpoint derivative and regularly-varying terminology did not locate the same classification. A prior regularly-varying-coefficient application under different notation remains the main residual risk.

## Scientific value — PASS

The result turns a one-sided exponent condition used in a known Vietoris extension into an exact threshold and gives a quantitative mechanism for failure below it. The universal -1/2 sin(y) boundary profile explains why nonnegative shifts cannot repair the endpoint instability.

## Evidence and literature

- Sangal and Swaminathan, Vietoris type theorem related to positivity of trigonometric polynomials: https://arxiv.org/abs/1705.03759
- Sangal and Swaminathan, Geometric Properties of Cesàro Averaging Operators: https://doi.org/10.1155/2017/6584584
- Kwong, A New Family of Nonnegative Sine Polynomials: https://ncts.ntu.edu.tw/upload/blistfs29160804294214120.pdf

## Limitations

- Cosine positivity by itself is not classified below λ+μ=1.
- Sangal–Swaminathan Theorem 3.2 is printed with λ,μ>0; the λ=0 or μ=0 sine boundary cases are supported here by the direct Belov-criterion check rather than by attributing those endpoints literally to that theorem.
- A differently phrased theorem for regularly varying coefficients could overlap the converse or boundary asymptotics.

The independent audit finds the record scientifically complete on all three axes at the audited tree. The literature verdict is bounded by the sources and searches explicitly described above; it is not inferred merely from failure to find a match.
