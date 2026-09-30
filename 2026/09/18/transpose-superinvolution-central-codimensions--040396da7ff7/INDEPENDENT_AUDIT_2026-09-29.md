# Independent audit — Exact central codimensions for the transpose superinvolution on M2

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/transpose-superinvolution-central-codimensions--040396da7ff7`  
**Audited tree:** `1a96e3161af816fed06c3415b1214625c747248e`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The exact formulas are internally consistent and independently reproduced. Applying the binomial transform to the Bezerra dos Santos–Reis codimension sum gives c_n^*=C(2n+2,n+1)-2^n. Summing the compositionwise central layer described by the source normal forms gives an even-n2 contribution 2^{n-1} and a balanced odd-variable contribution C(2n,n)-2^n, hence z_n^*=C(2n,n)-2^{n-1}. Subtraction gives the stated central codimension, and central-binomial asymptotics give the 1:3 split and exponent 4. Exact integer recomputation for n=1,...,10 matched both closed formulas.

## Originality

**PASS.** The 2016 Giambruno–Ioppolo–Martino work is prior art for identities/cocharacters/codimensions, and the 2026 Bezerra dos Santos–Reis preprint gives generators for central *-polynomials and an exact summation formula for the ordinary *-codimensions; these are not claimed new. The audit also obtained the full Giordani–Ioppolo–dos Santos–Vieira central-exponent article through authorized Oxford access after open-access attempts failed. That paper treats existence and possible values of the central superinvolution exponent; for the four-dimensional M_{1,1}(F) transpose-superinvolution case it concludes exponent 4 but does not give the exact central-codimension sequence or the compositionwise 1:3 asymptotic split. Targeted searches found no earlier statement of the three exact sequences claimed here.

## Scientific Value

**PASS.** The record extracts a closed central-binomial formula from a nested codimension sum and computes the previously unstated central layer and its cocharacter multiplicities. The exact one-quarter/three-quarter asymptotic decomposition is a concrete refinement of general exponent theory for this canonical four-dimensional example.

## Independent checks

- Algebraically verified the binomial-transform generating function and checked c_n^*=C(2n+2,n+1)-2^n for n=1,...,10 against the source summation formula.
- Independently enumerated the composition sum for the central layer for n=1,...,10 and recovered z_n^*=C(2n,n)-2^{n-1} exactly.
- Checked the identity C(2n+2,n+1)-C(2n,n)=((3n+1)/(n+1))C(2n,n) and the limiting ratios z_n^*/c_n^*→1/4 and c_n^{z,*}/c_n^*→3/4.
- Read the 2026 Bezerra dos Santos–Reis abstract: it claims generators of identities and central polynomials, the *-codimension sequence and cocharacters, but only states the 4^n n^{-1/2} growth rate in the abstract.
- After arXiv/open-access full text for the Giordani et al. central-exponent paper was unavailable, used authorized Oxford Download and read all 18 pages. Its exp=4 section includes M_{1,1}(F) with transpose superinvolution and proves only central-exponent value 4, not the exact sequences claimed here.

## Literature and prior-art boundary

- https://arxiv.org/abs/2609.20458 — Bezerra dos Santos and Reis (2026), source for *-identities, central *-polynomial generators, cocharacters and the full *-codimension summation.
- https://doi.org/10.1016/j.laa.2016.04.016 — Giambruno, Ioppolo and Martino (2016), prior identity/cocharacter/codimension computation for this transpose-superinvolution algebra.
- https://doi.org/10.4153/S0008439525101276 — Giordani, Ioppolo, dos Santos and Vieira, full text checked via authorized Oxford access; general central-exponent theory and exponent-4 treatment, no matching exact central-codimension formulas found.
- https://doi.org/10.1007/s00209-025-03689-8 — La Mattina, dos Santos and Vieira (2025), prior proper-central-exponent theory; treated as general prior art, not claimed new.

## Limitations

- The exact calculation is for M_{1,1}(F)=M_2(F) with the canonical grading and transpose superinvolution in characteristic zero.
- The normal-form classification used to count central constituents comes from the very recent 2026 preprint and could be revised.
- The novelty claim is limited to the closed exact sequences, compositionwise central multiplicities, and their asymptotic split; general central-exponent theory is prior art.

## Repository identity

The assigned source-tree SHA `1a96e3161af816fed06c3415b1214625c747248e` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
