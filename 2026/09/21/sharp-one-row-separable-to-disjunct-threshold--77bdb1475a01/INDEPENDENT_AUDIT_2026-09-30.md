# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/sharp-one-row-separable-to-disjunct-threshold--77bdb1475a01`  
Assigned and audited source tree: `ea895f4b3038f238f23a58bd570ee701d4c2710a`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `fe0a06537885d433463348373d9d8539bf1d79f8`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The construction and frontier are correct. With 2d+1 columns, exact (2d-1)-separability reduces to distinguishing the omitted pair; private ordinary rows recover omitted ordinary columns and the q_i/r_j rows resolve the remaining C versus C' ambiguity. The two displayed d-covers impose contradictory requirements x_C=1 and x_C=0 on any single appended row, so one row cannot give d-disjunctness, while two private rows for C and C' make every column private. An independent exhaustive implementation for d=2,3,4 reproduced exact (2d-1)-separability and non-d-disjunctness. The monotonicity lemma then combines with the Chen--Hwang 2d-separable-to-d-disjunct one-row theorem to give G(s)=floor(s/2) for both parities.

## Originality

**qualified_supported**. Chen--Hwang 2007 was located in full text and states exactly the positive theorem that a 2d-separable matrix can be made d-disjunct by adding at most one row; the 2009 error-tolerant extension restates that result. Current searches did not locate the audited obstruction family, a proof that the factor two is worst-case sharp for one-row augmentation, or the exact general frontier floor(s/2). Originality is therefore supported for the sharpness construction/frontier, not for the conversion theorem or standard separability implications. A differently indexed cover-free-family formulation remains a residual risk.

## Scientific value

**meaningful_exact_sharpness_result**. The theorem determines the exact worst-case one-row frontier between two central nonadaptive group-testing design notions and proves that the classical factor-two parameter loss cannot be improved without extra hypotheses. The obstruction is an explicit infinite family rather than a small exceptional example.

## Independent checks

- Reconstructed the omitted-pair proof of exact (2d-1)-separability.
- Checked the logically incompatible single-row requirements for the two d-covers.
- Exhaustively generated the witness matrices for d=2,3,4 and verified the claimed separability and failure of d-disjunctness.
- Inspected the accessible Chen--Hwang 2007 theorem text and the 2009 restatement.

## Literature and evidence checked

- https://doi.org/10.1016/j.dam.2006.10.009
- https://doi.org/10.1016/j.dam.2008.06.004
- https://doi.org/10.1007/s10878-015-9951-1
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/sharp-one-row-separable-to-disjunct-threshold--77bdb1475a01

## Limitations

- Binary noiseless matrices and one-row augmentation only.
- The witness row count is not optimized and extremal matrices are not classified.
- Error-tolerant variants are not resolved.
- Equivalent cover-free/superimposed-code formulations remain a residual terminology risk.
