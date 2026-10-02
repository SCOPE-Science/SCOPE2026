# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. With one work register and a passive output, call-free work updates are constants. In any nonlinear two-call clean program the two nonzero work-register accesses must cancel. Collecting output updates before and after the active interval gives \(H(\tau+ax)-H(\tau)=f(x)-f(0)\), so after rescaling \(f-f(0)\) is additive. Conversely, any constant plus additive polynomial is computed by the displayed two-access finite-difference transcript. Over characteristic \(p>0\), polynomial additivity is exactly the standard \(p\)-linearized form \(\sum_j a_jX^{p^j}\), so arbitrarily high formal degree is attained already by Frobenius powers.

Originality: PASS. The complete inspected portion of Vinciguerra's primary preprint explicitly assumes characteristic zero throughout the call-lower-bound section and states \(D^{\mathrm{pass}}_{r,K}(2)=1\) only there. Its positive-characteristic statements concern four-call constructions under a large-characteristic restriction, not a two-call classification. Published-record and targeted searches found no earlier theorem identifying the two-call class with additive polynomials. Standard linearized-polynomial theory supplies the algebraic classification after additivity is proved, but not the register-program necessity argument.

Scientific value: PASS. The theorem identifies a sharp structural boundary in a newly active register-program model: the characteristic-zero two-call degree frontier collapses completely in positive characteristic, and the exact mechanism is additive finite difference. This is a natural diagnostic for how characteristic assumptions enter catalytic algebraic lower bounds.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
