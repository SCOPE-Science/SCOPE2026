# Review of Sharp endpoint for a controlled g-frame perturbation theorem

## Correctness
PASS. In the specialization \(T=U=I\), the family \(\Lambda_n f=\langle f,e_n\rangle\) is Parseval and \(\Gamma_n f=n^{-1}\langle f,e_n\rangle\) is Bessel and complete but has no positive lower g-frame bound. The mixed operator is exactly \(\operatorname{diag}(1,1/2,1/3,\ldots)\), so its distance from the identity is exactly \(1=A\) and it is not invertible. For \(\lambda<A\), lower bounds for both the mixed operator and its adjoint give invertibility, and the source's Cauchy--Schwarz step yields \((A-\lambda)^2/B\).

## Originality
PASS. The primary full text was checked at Definition 3.1, Theorem 3.4, its proof, and Proposition 3.5. The theorem explicitly includes equality at \(\lambda=A\), while the proof's purported lower bound becomes zero there. Targeted searches using the source identifier, theorem number, endpoint equality, mixed-operator terminology, diagonal counterexample, and strict-threshold formulations did not locate a covering correction. Earlier controlled-g-frame literature supplies the framework but not this endpoint result.

## Value
PASS. The issue changes an asserted invertibility-and-reconstruction criterion at its exact stability boundary. The counterexample is not a zero-family degeneracy: every coefficient map is nonzero and the Bessel family is complete. The correction is minimal, quantitative, and threshold-sharp, retaining the theorem with the single change \(\lambda<A\).

## Closest literature and limitations
The closest scientific source is the theorem itself, where the proof derives \((A-\lambda)\|f\|\) before claiming bounded-below invertibility. Proposition 3.5 in the same paper uses the strict condition \(\varepsilon<1\). Rahimi--Fereydooni's earlier controlled-g-frame paper establishes the background framework and multiplier operators but does not imply the endpoint correction. The remaining originality risk is an unindexed erratum, thesis remark, or informal note.

Same-model review: passed. Independent audit: not yet performed.
