# Review

## Correctness

PASS. The published polygonal characterization reduces every homothetic illumination body to an admissible \((k,l)\)-extension with \(k+l=2q\) and \(2q+1<m/2\). For an equiangular polygon, direct solution of the two sideline equations gives the exact support recurrence
\[
A h_{i-q-1}+B h_{i+q}=\mu D h_i,
\]
with \(A,B,D>0\). Summing fixes \(\mu D=A+B\). On a nonzero Fourier mode the recurrence would require
\[
A z^{-(q+1)}+Bz^q=A+B.
\]
Since both powers of \(z\) lie on the unit circle and both weights are positive, equality forces each power to equal \(1\); coprimality of \(q\) and \(q+1\) then gives \(z=1\). Thus only the constant support mode survives, which is exactly a regular polygon.

The packaged checker independently reconstructs sideline intersections for regular support data and stress-tests the Fourier obstruction across a broad finite parameter range. The finite sweep is not used as a proof of the general theorem.

## Originality

PASS with a residual terminology risk. Horváth and Lángi explicitly pose the full polygonal problem and prove affine regularity only for the \((1,1)\)-extension. Their general Theorem 8 permits higher extensions and does not resolve them; the accessible text contains no equiangular specialization. Targeted searches for equiangular polygons together with illumination bodies, generalized homothety, and \((k,l)\)-extensions found no equivalent rigidity theorem.

Lángi's 2018 circulant-matrix work gives broad vertex-recurrence criteria for affine regularity, but does not state the illumination-body implication and does not supply the support-number recurrence used here. The new step is the conversion of the higher extension condition to a positive two-term support recurrence and the resulting Fourier collapse.

## Value

PASS. The source leaves a concrete polygonal homothety problem open after resolving only the first extension. Equiangular polygons form a natural high-dimensional family containing many nonregular shapes, and the result settles the open implication on that entire family for every admissible higher extension at once. The proof also isolates a reusable rigidity mechanism: equal angular spacing turns homothetic extension geometry into a positive circulant eigenvalue problem with a uniquely constant top mode.

## Closest literature and limitations

The closest source is Horváth–Lángi, arXiv:2012.08955, especially Problem 2 and Theorem 8. Lángi, arXiv:1706.03036, is the closest broader recurrence-rigidity framework. No located source states the equiangular illumination-homothety theorem. The result does not settle non-equiangular polygons.

Same-model review: passed. Independent audit: not yet performed.
