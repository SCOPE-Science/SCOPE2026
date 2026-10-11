# Same-model review

## Correctness

PASS. The regular-simplex face-direction spaces have an explicit Gram structure. Two positive-dimensional face-direction spaces intersect trivially exactly when the faces share at most one vertex. Disjoint pairs are orthogonal. For a shared-vertex pair of dimensions \(r\) and \(s\), the normalized cross-Gram optimization is
\[
\sqrt{\frac r{r+1}}\sqrt{\frac s{s+1}}.
\]
The source's admissibility condition gives \(r+s\le n\); strict monotonicity forces \(r+s=n\), and balancing gives
\[
r=\left\lfloor\frac n2\right\rfloor,
\qquad
s=\left\lceil\frac n2\right\rceil.
\]
Substitution into the source's exact formula for \(M\) gives the claimed \(M_n\). The bundled exact checker verifies every face pair through dimension \(12\).

## Originality

PASS. The primary source leaves \(c\) as an abstract finite maximum and does not specialize Proposition 4.3 to regular simplices. Searches for arbitrary regular-simplex face angles, principal and Friedrichs angles, shared-vertex face subspaces, and source-specific specializations found no covering formula or equality classification. Nearby published results concern other simplex functionals.

## Value

PASS. The result turns an implicit constant in a recent general theorem into an explicit all-dimensional regular-simplex benchmark and identifies the unique worst combinatorial face type. The resulting far-observer radius is a natural quantitative cutoff attached directly to the source theorem.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest result is Proposition 4.3 of Kenderov--Mushkarov--Nikolov, which defines
\[
c
\]
and
\[
M=\frac12\left(1+\frac1{\sqrt{1-c^2}}\right)
\]
for an arbitrary polytope but does not evaluate \(c\) for regular simplices.

Standard regular-simplex formulas for facet dihedral angles do not imply the required maximum over all pairs of face-direction spaces. The main residual bibliographic risk is an older equivalent formula under principal-angle or Friedrichs-angle terminology.

The theorem does not claim that the sufficient radius \(M_n\) is the smallest possible radius for the local-maximizer conclusion.
