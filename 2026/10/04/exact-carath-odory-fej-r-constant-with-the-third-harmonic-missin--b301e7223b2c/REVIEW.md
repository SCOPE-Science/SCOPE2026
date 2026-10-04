# Review

## Correctness
**PASS.** The upper bound is the positive combination \(T(1/2)+2T(1/3)=3-2\lambda\), so every feasible polynomial has \(\lambda\le3/2\). The proposed coefficients factor exactly as \((2-x)(x+1)(2x+1)^2/6\), which is nonnegative on \([-1,1]\). Equality forces zeros at both certificate points; the interior zero at \(x=-1/2\) must be stationary, and the resulting two linear equations uniquely determine the remaining coefficients. Herglotz's finite-support equivalence gives the positive-definite-sequence formulation. The checker confirms the algebra with exact rational arithmetic but is not used as an infinite proof.

## Originality
**PASS.** The closest primary source defines exactly the general quantity \(M(H)\), lists several solved structured sets, and gives the duality \(M(H)M(\mathbb N_{\ge2}\setminus H)=2\). The inspected solved list does not include \(H=\{2,4\}\), and the duality only converts it into the unsolved-looking two-hole complement rather than yielding a value. Révész's earlier minimax theorem is a general duality framework, and the later locally compact Abelian-group paper is a general reduction framework; neither inspected text states this numerical special case. Targeted semantic and web searches under equivalent sparse-support formulations found no covering statement.

Residual risk: because the proof is elementary, an older or poorly indexed extremal-polynomial source may contain the same support value in different notation. That risk is recorded rather than treated as eliminated by search failure.

## Value
**PASS.** The support \(\{1,2,4\}\) is the first natural degree-four Carathéodory–Fejér support obtained by deleting an interior harmonic from an initial interval. The exact value \(3/2\) quantifies the effect of forbidding the third harmonic and lies strictly between the classical degree-two and degree-four full-support constants \(\sqrt2\) and \(\sqrt3\). The unique extremizer and the two-point dual certificate make the result structural rather than a numerical table entry.

## Closest literature and limitations
Kolountzakis–Révész provide the precise \(M(H)\) framework, known structured examples, and complement duality; Révész provides the earlier general minimax duality; Krenedits–Révész provide the general positive-definite/LCA formulation. The claim is restricted to the real even support \(\{1,2,4\}\); arbitrary sparse supports and the unrestricted complex variant remain outside its scope.

Same-model review: passed. Independent audit: not yet performed.
