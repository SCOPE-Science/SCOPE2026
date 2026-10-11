# Same-model review

## Correctness
PASS. The complete source H-description is used with the correct affine metric. Singleton facets \(x_i=3\) give the candidate radius and a universal upper bound. For all other facets, the proof controls the projected normal by \(H\le\sqrt Q\), converts positivity of the coefficient vector into \(W-H\ge t-\sqrt t\), and combines this with the exact source bound on \(\kappa(k,l)\). This resolves all large supports uniformly. The only five small ambient/support pairs left by the coarse bound are checked by exact rational squared-distance certificates, all strictly positive. Summing singleton constraints proves global optimality and uniqueness.

## Originality
PASS. The 2017 primary paper was inspected at the exact halfspace construction, singleton-facet observation, and realization theorem, including direct PDF-page inspection. The later Minkowski-sum paper was inspected as the strongest same-object follow-up. Neither source contains inradius, Euclidean, Chebyshev, or radius terminology. Published-result and literature searches under inradius, inball, uniform-center, and facet-distance formulations found no covering statement.

## Value
PASS. The simple permutoassociahedron is a canonical hybrid of permutohedral and associahedral geometry with an explicit but highly nonuniform truncation system. The theorem proves that all those additional cuts leave one exact simplex-scale inball untouched:
\[
r_{\mathrm{in}}(PA_n)
=
\frac{3^{n+1}-3(n+1)}{\sqrt{n(n+1)}}.
\]
It also proves uniqueness of the uniform center and gives the complete contact set: exactly the \(n+1\) singleton facets.

## Closest literature and limitations
The source already implies an upper bound by embedding the polytope in the simplex \(x_i\ge3\), but it does not prove that the simplex inball survives every further permutoassociahedral truncation. That all-facet comparison is the new content. The theorem is specific to this realization; normally equivalent realizations can have different support offsets and different Euclidean inradii.

Same-model review: passed. Independent audit: not yet performed.
