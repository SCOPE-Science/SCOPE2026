# Same-model review

## Correctness
PASS. The matrix family is positive definite exactly for \(a>2/3\) by Sylvester's criterion, and its displayed inverse is entrywise positive. Direct substitution into the exact conjugate-gradient recurrence yields \((x_2)_1=N_a(B)/Q_a(B)\). The identity
\[
p_1^\mathsf T A_ap_1
=
\frac{(B^2+1)^2Q_a(B)}{(2B^2+a)^3}
\]
proves \(Q_a(B)>0\). For \(a\le4\), every coefficient of \(N_a\) is nonnegative and its constant term is positive; for \(a>4\), its leading term is negative and forces eventual sign reversal. The one- and two-dimensional minimality argument uses only the positive first stepsize, exact finite termination, and inverse positivity. The packaged exact-rational checker independently replays the witness and formula on rational test parameters.

## Originality
PASS with material residual risk. Hestenes--Stiefel's finite-step/variational CG theory, Meijerink--van der Vorst's use of CG on symmetric \(M\)-matrices, and Schmelzer--Stoll's broad observation that unconstrained CG does not preserve \(x\ge0\) are all treated as prior work. Semantic and literature searches under symmetric \(M\)-matrix, Stieltjes, inverse-positive, positivity-preserving, negative iterate, and minimal-dimension aliases found no implication-equivalent statement of the three-dimensional minimum or the sharp \(a=4\) family boundary. Two highly relevant full texts were not recovered, so equivalent specialized examples inside them remain an explicit risk rather than being dismissed.

## Value
PASS. Inverse positivity is the canonical matrix property ensuring that nonnegative forcing produces a nonnegative exact solution, so failure of the iterative path inside that class is structurally meaningful. The result identifies the minimum dimension, gives a small exact witness, and supplies a sharp parameter boundary rather than only an isolated counterexample. It clarifies that energy-norm progress and eventual positivity of the exact solution do not imply coordinatewise positivity of intermediate Krylov iterates, which is directly relevant when CG is used inside algorithms with physical or optimization nonnegativity constraints.

Same-model review: passed. Independent audit: not yet performed.
