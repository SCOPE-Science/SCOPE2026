# Same-model review

## Correctness
**PASS.** The upper bound follows from two necessary nonnegativity constraints at \(\theta=\pi\) and \(\theta=4\pi/5\). Their combination gives \(a\le\sqrt5/2\) with no numerical approximation. At equality, both constraints are tight; the zero at \(4\pi/5\) must be stationary, and the derivative equation uniquely determines the two remaining coefficients. For attainment, the candidate polynomial factors exactly as \((x+1)(x-r)^2R(x)\) on \(x=\cos\theta\). The derivative \(R'\) has negative leading coefficient and negative discriminant, and \(R(1)>0\), so \(R>0\) on \([-1,1]\). This proves universal nonnegativity and the full equality classification. Risk: arithmetic transcription is the main local failure mode; the standalone exact symbolic replay checks every displayed identity.

## Originality
**PASS.** The closest general source defines the same support-constrained Carathéodory–Fejér problem but does not evaluate this support. Nearby exact database results concern different supports such as \(\{1,2,4\}\) and \(\{1,3,4\}\). A prior qualitative theorem for \(\mathcal M_{m,n}\) implies only \(\mathcal M_{4,6}>\sec(\pi/8)\), not the exact value or extremizer. Searches across Carathéodory–Fejér, positive-definite, and support aliases did not uncover an implication-equivalent statement. Risk: older sparse trigonometric-polynomial literature may encode the same small support differently, so the package records this as residual risk rather than treating search failure as proof of novelty.

## Value
**PASS.** The support \(\{1,4,6\}\) defines a natural exact coefficient extremum in the classical sparse Carathéodory–Fejér framework. The result gives both a closed sharp constant and the unique extremizer, with a two-contact certificate and a global factorization. It is not a mere recomputation of a known table entry or a numerical special case; it resolves the complete continuous optimization for this support and sharpens the previously available qualitative strict inequality.

## Closest literature and limitations
Krenedits–Révész, arXiv:1304.0071v1, supplies the general support-constrained framework and primary MSC 43A35. Kolountzakis–Révész, arXiv:math/0312218v1, supplies broader positive-definite extremal context but optimizes a different functional. The theorem here is support-specific and leaves arbitrary support pairs and finite cyclic sampling open.

Same-model review: passed. Independent audit: not yet performed.
