# Scientific review

## Correctness — PASS

The orthogonal reducing decomposition is valid because the operator is symmetric and the selected subspace invariant. The two preconditioned spectra, endpoint formulas, and the reciprocal-parameter minimization can be reconstructed directly. The borderline cases \(c=a\), \(b=d\) and repeated eigenvalues are covered. The analytical proof is universal; 153,030 deterministic verification comparisons corroborate but do not replace it.

## Originality — PASS with residual bibliographic uncertainty

Fan, Hu, and Zhang introduce the two inverse preconditioner families and prove nonsingularity and Richardson estimates; they do not give the all-scalar exact invariant-subspace spectral minimax formulas or improvement iff criterion in the sections inspected. Pasetto et al. study a differently constructed ROM preconditioner and numerical spectral profiles. González analyzes a general Frobenius-optimal approximate-inverse framework, not the specific scalar pair in the accessible abstract. Related spectral boost work addresses angle misalignment and not the all-endpoint Type-I ridge classification. The scalar endpoint calculus is elementary after the model-specific reduction; a preexisting equivalent classification elsewhere remains a real risk.

## Mathematical value — PASS

Scalar tuning of a singular reduced inverse is intrinsic to the new proposed preconditioner, not an arbitrary slicing parameter. The theorem separates invertibility from useful spectral conditioning, gives the exact minimizer and a necessary/sufficient improvement boundary, and proves that adding the ridge across retained modes can be arbitrarily worse than adding it only on the complement. It is intended as an ideal invariant-subspace diagnostic, not a claim about noninvariant production solvers.

## Closest literature and limitations

Fan, Hu, Zhang (2026), arXiv:2609.11097v1, equations (4),(7), Section 3; Pasetto et al. (2017), DOI 10.1002/nme.5320, Sections 4–5; González (2006), DOI 10.1137/S0036144504431905, abstract only. Standard invariant-subspace spectral calculus is background. No independent audit or general noninvariant result is claimed.

Self-review: passed. Independent audit: not yet performed.
