# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The theorem is an exact structural calculation in the two-register passive-output model. Because the output register never appears on a right-hand side, a basic instruction acting on the sole work register can add only a constant. Therefore the input coefficient in the work register can change only at input accesses.

With at most two accesses, any nonlinear computation must direct both nonzero accesses to the work register, with opposite coefficients in order to restore it. Output updates then split into an input-free contribution \(B(\tau)\) and an active-interval contribution \(H(\tau+ax)\). Cleanliness gives
\[
B(\tau)+H(\tau+ax)=f(x),
\]
and subtraction at \(x=0\) forces
\[
H(\tau+y)-H(\tau)=H(y)-H(0).
\]
Thus \(H-H(0)\) is additive and so is \(f-f(0)\). Conversely, an additive polynomial \(A\) is computed by the two-access transcript
\[
U\leftarrow U+x,\quad
O\leftarrow O+A(U),\quad
U\leftarrow U-x,\quad
O\leftarrow O-A(U),
\]
with an optional constant output update. This restores the arbitrary initial work-register value exactly.

The standard classification of additive polynomials gives \(A(X)=aX\) in characteristic zero and \(A(X)=\sum_j a_jX^{p^j}\) in characteristic \(p>0\). Hence \(X^{p^e}\) has arbitrarily large formal degree while still using two registers and two accesses. This is a polynomial identity, not a finite-field interpolation artifact.

The public verification script checks the formal binomial criterion in characteristics \(2,3,5,7\) and reproduces the vanishing of all mixed terms for tested linearized polynomials. It is supporting evidence only; the proof is general.

Potential edge cases were checked explicitly. Direct accesses to the passive output contribute only affine-linear terms. If fewer than two nonzero accesses hit the work register, restoration prevents any input dependence from remaining there. Constant shifts of the work register during the active interval are harmless because they can be absorbed into the polynomials used by output updates.

## Originality

The motivating source, arXiv:2609.18692, was inspected at theorem and proof level. Its Section 3 states that the lower-bound section assumes characteristic zero. It proves that at most two input accesses give degree at most one for any number of registers, and proves the exact two-register frontier \(D^{\mathrm{pass}}_{2,K}(t)=t-1\) in characteristic zero. Its positive-characteristic discussion concerns extending the four-access construction when the characteristic is sufficiently large. The paper contains no occurrence of “Frobenius” or “additive” and does not state the positive-characteristic two-call collapse.

The 2025 MFCS paper defining the same modern register-program framework was inspected in its register-program and polynomial-construction sections. It gives four-access programs for univariate polynomials over prime fields and exploits finite-field/Boolean polynomial structure elsewhere, but no two-access Frobenius construction or exact two-register two-access classification was found.

Targeted searches combined `register program`, `passive-output`, `two input accesses`, `Frobenius`, `additive polynomial`, `linearized polynomial`, `positive characteristic`, and the motivating arXiv identifier. Searches for the motivating paper together with `Frobenius`, `positive characteristic`, and `additive polynomial` returned only the motivating paper or unrelated material. The current SCOPE repository was searched by the source arXiv identifier and by register/Frobenius/additive-polynomial terminology; no overlapping record was found before publication.

The algebraic fact that additive polynomials in characteristic \(p\) are exactly \(\sum a_jX^{p^j}\) is classical and is not claimed as new. The originality claim is restricted to the exact register-program characterization and the resulting sharp characteristic dichotomy. Because the proof becomes short once one tests Frobenius against the two-call transcript, folklore and near-simultaneous priority risk are substantial.

No inaccessible source was identified as particularly likely to contain the exact claim. The two closest register-program sources were accessible, and the classical additive-polynomial fact is well documented.

## Value

The result makes the characteristic-zero assumption in the recent input-access lower bounds mathematically sharp. Rather than a weakened lower bound in characteristic \(p\), two accesses already suffice for arbitrarily high formal degree with only one work register. This rules out any characteristic-independent lower bound based solely on polynomial degree once two calls are permitted.

The exact characterization also explains the mechanism. Two-call cleanliness reduces to a finite-difference identity, and the polynomials whose finite difference is independent of the catalytic value are precisely additive polynomials. This turns an apparent technical failure of a Vandermonde/exponential argument into a structural boundary of the model.

For infinite positive-characteristic fields, polynomial degree is unambiguous and the degree frontier is genuinely infinite. For finite fields, the record explicitly separates the formal polynomial statement from the representation-dependent degree of polynomial functions.

## Limitations

The exact iff theorem is limited to one work register plus one passive output and at most two input accesses. It does not classify all positive-characteristic programs with more work registers, nor does it address non-passive outputs. The construction is commutative and does not transfer directly to matrix rings. No algorithmic consequence for a complete catalytic machine is claimed beyond the register-program statement itself.
