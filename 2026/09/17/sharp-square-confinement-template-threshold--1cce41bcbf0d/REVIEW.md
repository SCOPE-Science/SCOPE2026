# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces every instance in the stated template to two necessary geometric pressures.

First, the full witness gives \(H\ge b+c\), while rejection from the pivot's hole gives \(c>1-w\). Hence \(a=H+w>1+b\ge1+(b+c)/2\). The same witness gives the exact necessary root-pair bound
\[
s\ge \left(1+\frac1{\sqrt2}\right)(a+1),
\]
and best fit's strict preference for the large hole gives \(s>2(b+c)\).

Second, the two strict quadratic inequalities and the coupling \(p+q\ge s-b-c\) from the quadrant-confinement certificate imply
\[
8as+6(b+c)s-5s^2-(b+c)^2>0.
\]
The monotonicity argument in \(s\) and then in \(a\) was checked symbolically by direct expansion. At the boundary \(s=(1+1/\sqrt2)(a+1)\), \(a=1+(b+c)/2\), the expression becomes exactly one eighth of the quadratic defining \(Y\). All strictness directions are consistent, so equality cannot occur.

The upper/sharpness direction is supplied by the explicit family already proved in Theorem 38 of arXiv:2609.15554v2, which satisfies the template assumptions and has \(\rho\to Y^+\).

## Originality

**PASS, to the best of our knowledge.** The following coverage was checked:

- arXiv:2609.15554v2, especially Lemma 35, Theorem 38, and Open Problem 44;
- the current accompanying Calamares repository, including `docs/drafts/cuadrado_limite.md` and `docs/generalizaciones.md`;
- targeted searches for the exact constant \(Y\), its defining polynomial, “quadrant confinement,” “square threshold,” and synonymous nested-ring formulations;
- current SCOPE records under the source paper, nested rings, square pans, quadrant confinement, and the numerical constant.

The primary source explicitly says that no optimality of \(Y\) is asserted, even for all parameters of the confinement criterion. The accompanying square-limit note explicitly leaves open a lower bound forcing \(\rho\ge Y\) for the slipped family, and the generalizations note says both family-level and global optimality remain open. No matching proof of the template lower bound was found.

The claim here is deliberately narrower than global optimality: it concerns the canonical four-ring root-pair/hole-pair witness branch with a quadrant-confinement certificate. No specific inaccessible paper was identified as especially likely to contain this refinement. Residual originality risk is nevertheless elevated because the source is only days old and follow-up work may not yet be indexed.

## Value

**PASS.** The result turns the source's limiting constant into an exact sharp boundary for a natural and explicitly identified construction/certificate architecture. It shows that the balanced point defining \(Y\) is forced by the whole canonical parameter family rather than being an artifact of the particular perturbation chosen for the upper bound. This narrows the search for a better square counterexample: any improvement below \(Y\) must leave at least one of the stated structural ingredients.

## Limitations

The theorem does not determine the global square threshold. It does not cover alternative witness forests, different pivot structures, non-confinement certificates for the root triple, or larger inventories.

No independent validation or formal verification is asserted.
