# Review

## Correctness
PASS. The automorphism dimension follows from the projective-bundle automorphism sequence, the fact that \(\operatorname{Aut}(E)\) is open in \(H^0(\operatorname{End}E)\), and Riemann--Roch on \(\mathbb P^1\). The identity
\[
h^1(\operatorname{End}E)=\sum_{i>j}\max\{a_i-a_j-1,0\}
\]
is a direct summand-by-summand calculation. Harris's degeneration order makes the balanced orbit dense in the fixed-\((d,k)\) scroll locus, so orbit codimension is exactly the stabilizer-dimension excess. The extremal upper bound is proved by an elementary inequality after writing \(a_i=1+b_i\), and its equality conditions force the unique least-balanced type. The standalone exact checker replayed 2212 splitting types and the published surface specialization without discrepancy.

## Originality
PASS with a stated residual literature risk. Ma supplies the rank-three automorphism sequence, Harris supplies the degeneration order, Ramkumar restates the least-balanced terminal degeneration, and Ferapontov--Kruglikov supply the complete surface automorphism dimensions. None of the inspected sources states the all-dimensional identity between symmetry excess and projective-orbit codimension or the resulting fixed-\((d,k)\) sharp extremal theorem. Targeted database searches for the cohomological defect, balanced-scroll automorphism dimensions, and orbit codimensions returned no semantically covering result.

## Value
PASS. The result turns the discrete splitting-type stratification of rational normal scrolls into an exact geometric statistic: the same computable cohomology group measures excess symmetry and codimension from the generic balanced orbit. It also gives sharp closed-form endpoints of the symmetry/codimension spectrum at fixed dimension and degree, with unique extremizers. This is more than a recomputation of individual automorphism groups because it identifies the invariant controlling the entire degeneration stratification.

## Closest literature and limitations
The closest direct comparison is the surface formula of Ferapontov--Kruglikov, which agrees exactly with the \(k=2\) specialization. Ma's exact sequence provides the projective-bundle mechanism in rank three. Harris and Ramkumar determine degeneration order but not the automorphism/codimension formula. The theorem excludes singular scrolls and does not make scheme-theoretic claims about orbit closures or the full Hilbert component.

Same-model review: passed. Independent audit: not yet performed.
