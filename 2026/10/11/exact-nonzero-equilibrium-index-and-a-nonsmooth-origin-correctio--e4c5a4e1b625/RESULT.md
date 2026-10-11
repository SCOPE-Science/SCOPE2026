# Exact nonzero-equilibrium index and a nonsmooth-origin correction in a financial flow
## Finding
For the financial flow
\[\dot x_1=x_3+(x_2-a)x_1,\qquad \dot x_2=1-bx_2-|x_1|-x_1^2,\qquad \dot x_3=-x_1-x_3,\]
with \(a,b>0\), the nonzero equilibria admit a complete exact local classification. Set \(c=1-b(a+1)\). A nonzero symmetry pair exists exactly when \(c>0\). Then
\[r=\frac{\sqrt{1+4c}-1}2>0,\qquad E_\pm=(\pm r,a+1,\mp r),\]
and each member has characteristic polynomial
\[\chi(\lambda)=\lambda^3+b\lambda^2+\alpha\lambda+\alpha,\qquad \alpha=r(2r+1)>0.\]
Every such nonzero equilibrium is hyperbolic with exactly two eigenvalues in the open right half-plane and one in the open left half-plane.

At the source parameters \((a,b)=(1,1/25)\),
\[r=\frac{3\sqrt{13}-5}{10},\qquad \alpha=\frac{117}{50}-\frac{3\sqrt{13}}{10},\]
and the spectrum is approximately
\[-0.7199352974,\qquad 0.3399676487\pm1.2776016734i.\]
The source's always-present equilibrium \(E_0=(0,1/b,0)\) is a nonsmooth point of the printed vector field because \(|x_1|\) is not differentiable at \(x_1=0\). Hence a classical Jacobian does not exist there, and the matrix displayed in the source as the Jacobian at \(E_0\) is not a Jacobian of the printed ODE.

## Assumptions and scope
The statement concerns the printed three-dimensional autonomous system, real state variables, and positive parameters \(a,b\). The hyperbolic-index theorem applies only to the nonzero equilibria, where the absolute-value term is smooth. No classical linearization theorem is invoked at \(E_0\). The result does not assert absence or presence of chaotic invariant sets away from the equilibria.

## Proof
At equilibrium, the third equation gives \(x_3=-x_1\). Substitution into the first equation yields
\[x_1(x_2-a-1)=0.\]
If \(x_1=0\), then the second equation gives \(x_2=1/b\), producing \(E_0\). If \(x_1\ne0\), then \(x_2=a+1\), and the second equation becomes
\[x_1^2+|x_1|=1-b(a+1)=c.\]
This has nonzero real solutions exactly for \(c>0\), with \(|x_1|=r=(\sqrt{1+4c}-1)/2\), proving the equilibrium formula.

At \(E_\sigma=(\sigma r,a+1,-\sigma r)\), where \(\sigma\in\{-1,1\}\), the vector field is smooth and its Jacobian is
\[J_\sigma=\begin{pmatrix}1&\sigma r&1\\-\sigma(2r+1)&-b&0\\-1&0&-1\end{pmatrix}.\]
A direct determinant expansion gives
\[\det(\lambda I-J_\sigma)=\lambda^3+b\lambda^2+r(2r+1)\lambda+r(2r+1).\]
Thus \(\alpha=r(2r+1)>0\). Since \(c>0\) means \(b(a+1)<1\) and \(a>0\), necessarily \(0<b<1\). The Routh array has first column
\[1,\qquad b,\qquad \frac{\alpha(b-1)}b,\qquad \alpha.\]
None of these entries vanishes, and their signs are \(+,+,-,+\), so the Routh criterion gives exactly two roots in the open right half-plane. The remaining root lies in the open left half-plane. Therefore both nonzero equilibria are hyperbolic of unstable dimension two.

For \((a,b)=(1,1/25)\), \(c=23/25\), hence \(1+4c=117/25=(3\sqrt{13}/5)^2\), giving the displayed exact \(r\) and \(\alpha\). Numerical root evaluation of the exact cubic gives the displayed spectrum.

Finally, the second component contains \(-|x_1|\). Its right derivative with respect to \(x_1\) at zero is \(-1\), whereas its left derivative is \(+1\). Therefore the vector field is not differentiable at \(E_0\), so no classical Jacobian exists there.

## Verification
The accompanying dependency-free checker verifies the exact baseline identities in the quadratic field \(\mathbb Q(\sqrt{13})\), the Routh sign count, and the unequal one-sided derivatives of the absolute-value term. It also evaluates the exact nonzero-equilibrium cubic numerically as a consistency check. The proof itself is symbolic and does not depend on floating-point output.

## Relationship to prior work
Sukono, Yuningsih, Rusyaman, Vaidyanathan, and Sambas introduced the printed absolute-value financial-risk system and listed three baseline equilibria. Their equilibrium section assigns the same numerical spectrum to multiple equilibria and displays a classical Jacobian at the nonsmooth equilibrium \(E_0\). The present result instead derives the exact nonzero branch for all \(a,b>0\), proves its invariant unstable index throughout its full existence region, and isolates the differentiability obstruction at \(E_0\).

Searches for the DOI, the exact model terms, equilibrium corrections, nonsmooth linearization, and the reported baseline coordinates found no source stating this full branch-and-index theorem. Related finance models in the cited literature use different nonlinearities and therefore do not imply the result.

## Limitations
This is a local equilibrium classification plus a differentiability correction. It does not classify global attractors, prove or disprove the source's reported chaotic trajectory, or supply a nonsmooth stability theorem for \(E_0\). An unindexed correction or later treatment of the identical printed vector field could reduce originality; none was found in the inspected sources.

## References
1. Sukono, S. H. Yuningsih, E. Rusyaman, S. Vaidyanathan, and A. Sambas, “Investigation of chaos behavior and integral sliding mode control on financial risk model,” *AIMS Mathematics* 7(10) (2022), 18377–18394. DOI: 10.3934/math.20221012. Published 16 August 2022.
