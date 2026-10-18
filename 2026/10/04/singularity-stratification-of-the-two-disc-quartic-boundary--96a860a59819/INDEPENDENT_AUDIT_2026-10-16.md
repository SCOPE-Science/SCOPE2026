# Independent mathematical audit

## correctness

PASS

PASS. The exact source quartic is F=(u²+w²)(v²+w²)−4w². Its gradient together with F=0 gives w=0 and uv=0 (the excluded w≠0 case can be verified with Gröbner saturation), so the reduced locus is two crossing lines. Along a line, transverse Hessian determinant 4a²(a²−4) isolates the origin and a=±2; at ±2 invertible factor A and the S=(4−A)/A coordinate with ∂S/∂s≠0 give Whitney pinch germs. Origin factorization in w² with discriminant 16 at zero produces W²−U²V², two smooth tangent sheets. Nonexceptional points split as double curves. These identities were independently recomputed symbolically and checked against the actual artifacts/verify_target.py source.

## originality

PASS

PASS (best of knowledge). The primary Example 3.2 prints the precise quartic as the extreme-point component of a two-disc Minkowski sum. It does not state the two-line singular support, four pinch points or special tangential origin normal form. The separate two-3-disc quartic has a different dimension and branch geometry. A hidden classical projectively equivalent quartic remains possible.

## value

PASS

PASS. The complete singularity stratification (ordinary double curve / pinch / tangential two-branch crossing) of a natural explicit irreducible quartic answers a structurally motivated local geometric question; the differentiated cases and analytic normal forms go beyond a routine formatting of the defining equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
