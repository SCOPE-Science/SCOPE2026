# The singularity profile of the minimal-degree constant-width octic

## Finding
Let \\(C\\subset\\mathbb P^2_{\\mathbb C}\\) be the projective closure of the degree-eight curve displayed by Martinez-Maure for the support function \\(h(\\theta)=8-\\sin(3\\theta)\\). Then \\(C\\) is irreducible and rational, and its complete singular locus has exactly eleven points: three real unibranch singularities with Puiseux pair \\((3,4)\\), six nonreal ordinary nodes, and two unibranch singularities at infinity with Puiseux pair \\((2,7)\\). The two points at infinity are \\([1:i:0]\\) and \\([1:-i:0]\\). The three real singularities are the orbit under rotation by \\(2\\pi/3\\) of \\((0,9)\\), and the six nodes are the two rotation orbits of \\((0,-9+6i\\sqrt{3})\\) and \\((0,-9-6i\\sqrt{3})\\).

## Assumptions and scope
The ground field for the projective singularity calculation is \\(\\mathbb C\\). The real curve considered in the source is the real locus of this projective octic in the affine chart \\(z=1\\). The claim concerns the particular minimal-degree constant-width example with support function \\(8-\\sin(3\\theta)\\), not all algebraic curves of constant width.

## Proof
Put \\(t=\\tan(\\theta/2)\\). The source parametrization becomes the degree-eight projective map
\[
[X:Y:Z]=[-8(t-1)^3(t+1)(t^4+2t^3+6t^2+2t+1):-(3t^8-16t^7-36t^6-48t^5+50t^4-48t^3-36t^2-16t+3):(t^2+1)^4].
\]
The three coordinate forms have no common zero. Direct substitution gives the homogenization of the source equation. For the affine parametrization, exact differentiation gives
\[
\\frac{dy}{dx}=\\frac{t^2-1}{2t}.
\]
At a generic smooth image point, two distinct parameters would therefore have to satisfy \\(u=-1/t\\); however
\[
y(t)-y(-1/t)=\\frac{32t}{1+t^2},
\]
so this is not an identity. Hence the map is birational. Since it is given by base-point-free forms of degree \\(8\\), its image is an irreducible plane octic and its normalization is \\(\\mathbb P^1\\).

At \\(t=1\\), which maps to \\((0,9)\\), the local expansions are
\[
x=-12e^3+18e^4+O(e^5),\\qquad y-9=-9e^4+18e^5+O(e^6),\\qquad e=t-1.
\]
Thus the branch has Puiseux pair \\((3,4)\\) and delta invariant \\(3\\). Threefold rotational symmetry gives exactly three such real branches.

The factor \\(R(t)=t^4+2t^3+6t^2+2t+1\\) of \\(X(t)\\) is reciprocal. Its roots pair as \\(t\\leftrightarrow1/t\\), and their images satisfy
\[
y^2+18y+189=0.
\]
The two points on the axis \\(x=0\\) are therefore \\((0,-9\\pm6i\\sqrt3)\\). The tangent slopes of paired branches differ by \\((t^2-1)/t\\), which is nonzero at a root of \\(R\\), so these are ordinary nodes. Rotating by \\(2\\pi/3\\) gives six nonreal nodes.

At \\(t=i\\), use the affine chart \\(Y\\ne0\\) and put \\(U=X/Y+i\\). With \\(e=t-i\\), exact expansion gives \\(\\operatorname{{ord}}_e U=2\\). If \\(V=Z/Y-U^2/8+iU^3/16\\), then \\(\\operatorname{{ord}}_e V=7\\). Thus \\([1:i:0]\\) has Puiseux pair \\((2,7)\\) and delta invariant \\(3\\). Complex conjugation gives the same type at \\([1:-i:0]\\).

Finally, the listed singularities contribute
\[
3\\cdot3+6\\cdot1+2\\cdot3=21.
\]
A plane octic has arithmetic genus \\((8-1)(8-2)/2=21\\), while the normalization already has genus \\(0\\). Therefore the delta budget is exhausted, proving that there are no further singularities.

## Verification
The bundled checker `artifacts/verify.py` uses exact integer, rational, and Gaussian-rational arithmetic. It verifies the projective parametrization has no common factor, substitutes it into the homogeneous source equation, checks the tangent-slope identity, verifies the axis factorization and node certificate, reconstructs the local orders \\((3,4)\\) and \\((2,7)\\), and checks the genus-delta budget. A fresh replay from the extracted package returned `VERIFY_OK`.

## Relationship to prior work
Martinez-Maure gives the explicit degree-eight equation and trigonometric parametrization, proving that its real affine locus is a noncircular convex curve of constant width \\(16\\). Bardet and Bayen prove general degree and proper-parametrization results for trigonometric-support-function curves, including the degree-eight lower bound relevant here. Their paper therefore covers the general rational-parametrization framework, which is not claimed as new. Neither inspected source gives the complete projective singularity profile above; searches for the explicit equation together with genus, normalization, nodes, cusps, or singularities did not locate such a computation.

## Limitations
The originality conclusion is literature-search based, not an exhaustive theorem that no equivalent computation exists under different terminology. The statement classifies the singularities of this one explicit octic over \\(\\mathbb C\\); it does not classify singularities for the full family of constant-width support functions.

## References
Y. Martinez-Maure, “Noncircular algebraic curves of constant width: an answer to Rabinowitz,” Canadian Mathematical Bulletin 65 (2022), 552–556. DOI 10.4153/S0008439521000473. First public online date verified as 2021-07-05. Primary MSC 14H50.

M. Bardet and T. Bayen, “On the degree of the polynomial defining a planar algebraic curves of constant width,” arXiv:1312.4358; the inspected version gives the general rational implicitization and degree framework.
