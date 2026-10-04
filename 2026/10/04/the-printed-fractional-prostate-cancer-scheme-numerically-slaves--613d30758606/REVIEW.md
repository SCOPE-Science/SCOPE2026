# Same-model review

## Correctness

PASS. The source defines different right-hand sides \(H_5\) for androgen and \(H_6\) for PSA. The final printed recurrences use \(H_5\) for both variables, so direct subtraction proves
\[
P_n-A_n=P_0-A_0.
\]
At the admissible source-parameter state
\[
X_1=X_2=0,\quad A=a_0=10,\quad P=1,\quad u=0,
\]
the intended integer-order model instead has
\[
H_5=0,\qquad H_6=-0.08.
\]
The printed recurrence therefore cannot consistently discretize the stated PSA equation. The bundled exact-arithmetic checker replays this witness.

## Originality

PASS. Componentwise use of a vector field is standard numerical analysis and is not claimed as new. The accepted contribution is source-specific: identifying the duplicated androgen field in the PSA recurrence, deriving the forced \(P-A\) invariant, and testing it against the source's own parameterized model. Exact source, correction, PSA, androgen, and \(H_5/H_6\) searches found no published repair. The known 2022 author correction to the cited numerical-method paper concerns a separate summation identity and explicitly leaves that method's formulation unchanged.

## Value

PASS. PSA is a principal modeled biomarker and is displayed throughout the numerical results. As written, the scheme cannot evolve PSA according to its biological equation at all; it makes PSA an affine copy of androgen. The correction is small in notation but substantial in model meaning and supplies an exact diagnostic for reproductions of the published algorithm.

## Closest literature and limitations

The closest numerical-method source is Toufik and Atangana, DOI 10.1140/epjp/i2017-11717-0, together with its 2022 author correction DOI 10.1140/epjp/s13360-022-02380-9. That correction does not address the later prostate-cancer component substitution. Portz, Kuang, and Nagy, DOI 10.1063/1.3697848, provide the earlier clinical model in which androgen and PSA are distinct variables.

No simulation source code accompanies the motivating article. The finding therefore applies to the published recurrence and its stated validation role; the actual code used to produce figures may have contained the \(H_6\) correction.

Same-model review: passed. Independent audit: not yet performed.
