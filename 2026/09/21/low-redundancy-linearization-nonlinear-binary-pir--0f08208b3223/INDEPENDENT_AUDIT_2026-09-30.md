# Independent audit — 2026-09-30

**Record:** `2026/09/21/low-redundancy-linearization-nonlinear-binary-pir--0f08208b3223`  
**Audited source tree:** `e26344a7a8991622da91c492ee0851c81f875a50`  
**Disposition:** passed

## Correctness — PASS

PASS. After identifying the linear associated code with V=F_2^k, each inverse-labeling coordinate f_j is constant on cosets of W_s^perp for every recovery span W_s, so it factors through V/(W_1^perp+...+W_t^perp), whose dimension is dim(W_1 cap ... cap W_t). Modding the t recovery spans by their common intersection and adding the unrecovered columns gives k<=n-(t-1)d_j and hence d_j<=floor(r/(t-1)). Under r<=3t-4, d_j<=2. Because the inverse labeling is a permutation, each coordinate is balanced; the induced quotient function is balanced, and every balanced Boolean function on at most two variables is affine. Thus the whole labeling is affine with invertible linear part, and translating it yields a linear t-PIR encoder on the same code with the same recovery sets up to fixed output complements. The length-11, size-2^7 consequence follows from r=4 and the standard linear 3-PIR bound binom(r,2)>=k.

## Originality — PASS

PASS. Hollmann--Luhaäär's accessible arXiv paper explicitly distinguishes a nonlinear associated code from a nonlinear encoder labeling a linear code and poses the length-11, size-2^7 binary 3-PIR case, but it does not provide this low-redundancy affine-forcing theorem. Targeted searches in PIR/batch-code literature did not locate the quotient-dimension bound or the threshold r<=3t-4. The theorem addresses exactly the second nonlinearity mechanism identified in that prior work and sharpens the interpretation of the open 11/2^7 case without claiming to solve its existence.

## Scientific value — PASS

PASS. The result removes an entire class of nonlinear encoders from consideration in a concrete low-redundancy regime using a short structural argument. It converts linear-code lower bounds into lower bounds for nonlinear labelings of linear associated codes and materially narrows the unresolved 3-PIR parameter case. The binary dimension-two balanced-function phenomenon also clearly identifies why the method stops at the stated threshold.

## Independent checks

- Reconstructed the kernel/coset invariance argument for arbitrary recovery functions.
- Verified the dimension inequality using disjoint recovery sets and the remaining generator columns.
- Enumerated the balanced truth-table possibilities in dimensions 0, 1, and 2 and checked affine forcing.
- Inspected Hollmann--Luhaäär's open-access manuscript for the nonlinear-labeling distinction and the length-11, size-2^7 open problem.

## Literature evidence

- https://arxiv.org/abs/2208.14552 — Hollmann and Luhaäär, open-access manuscript on optimal possibly nonlinear 3-PIR codes; explicitly distinguishes nonlinear labeling of a linear associated code and states the 11/2^7 open case.
- https://arxiv.org/abs/1605.01869 — Rao and Vardy, redundancy lower bounds for linear PIR codes.
- https://arxiv.org/abs/2407.18124 — Hollmann, Puškin and Riet, later PIR-code work providing current adjacent context.

## Limitations

- The affine-forcing step is binary and uses the exceptional fact that every balanced Boolean function on at most two variables is affine.
- The threshold r<=3t-4 is sufficient, not claimed necessary.
- The length-11, size-2^7 binary 3-PIR existence question remains open; the theorem only forces any solution to have a genuinely nonlinear associated code.

No GitHub write was performed by the audit chat. The guarded publication plan stages only this audit evidence and the independent-audit verification channel.
