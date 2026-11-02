# Scientific review: boundary-derivative singular-value law

## Correctness — PASS

The exact action of each analytic monomial on the orthonormal weighted harmonic basis was recomputed in all three index regions. Gamma-ratio asymptotics yield the positive/negative tail coefficients \(\mp(\alpha+1)mn/k^2\) with a uniform \(O(k^{-3})\) finite-band error. For general polynomials, these coefficients assemble into the boundary Laurent symbol \(f'\overline{g'}\). The explicit counting lemma for finite Laurent symbols was proved using geometric index blocks, finite Toeplitz singular distributions, and rank-defect estimates. The residual \(k^{-3}\) band contributes only \(O(t^{-1/3})\) singular values above a fixed multiple of \(t\), so it cannot alter the \(t^{-1/2}\) coefficient. Exact counting inversion and a harmonic-sum comparison produce the theorem. The companion `check.py` passes 411 checks, but the infinite statements rely on proof.

## Originality — PASS (best-knowledge assessment)

The motivating 2026 Tian–Wang–Zhao theorem proves vanishing rigidity rather than singular-value asymptotics. The full 2013 Dong–Zhou paper gives angular symmetry and commutativity conditions for quasihomogeneous symbols, while a previously available monomial calculation provides the individual \(m,n\) instances of the present formula. Those are not claimed as new. The new point is the arbitrary polynomial-pair boundary integral \(L(f,g)\), where different Fourier bands interact and scalar monomial singular values cannot simply be summed. The 2026 Huang–Wang–Zhao theorem studies spectra of individual polynomial Toeplitz operators. The 2026 Chbichib–Ghiloufi abstract studies the different ambient operator \([M_u,P_\alpha]\), with order-\(j^{-1}\) decay. Comparisons located no equivalent or dominating statement. A general microlocal Weyl theorem or an unseen argument in an inaccessible full source remains a genuine residual risk; this is not a certification of publication priority.

## Mathematical value — PASS

A sharp quantitative spectral law for every nonconstant polynomial pair is a natural strengthening of qualitative noncommutation. The exact constant, the universal \(1/2\) Schatten threshold, and the boundary interference functional are meaningful invariants that cannot be read from the monomial formulas. This is an all-degree natural classification at leading order, not a parameter-specific example.

## Sources and limits

The primary full texts inspected are Tian–Wang–Zhao, arXiv:2609.14635; Dong–Zhou, doi:10.1007/s11785-012-0223-0; and Huang–Wang–Zhao, arXiv:2610.09638. The abstract/record of Chbichib–Ghiloufi, arXiv:2605.24698, was inspected, but its full text was unavailable. The theorem covers analytic polynomial symbols and \(\alpha>-1\); it does not classify finite-index singular values, nonsmooth symbols, or lower-order spectral terms. Independent mathematical verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
