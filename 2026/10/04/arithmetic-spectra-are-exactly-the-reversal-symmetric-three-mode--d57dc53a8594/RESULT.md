# Arithmetic spectra are exactly the reversal-symmetric three-mode CSD exception
## Finding
Consider cyclic steepest descent (CSD) with cycle length \(j=2\) on a strictly convex quadratic whose Hessian has exactly three distinct eigenvalues \(\lambda_1>\lambda_2>\lambda_3>0\). At a cycle boundary let \(P_i\) be the spectral projector for \(\lambda_i\), let \(g\) be the gradient, and define the full-support spectral weights
\[
p_i=\frac{\|P_i g\|_2^2}{\|g\|_2^2}>0,\qquad p_1+p_2+p_3=1.
\]
Call a projective two-cycle reversal-symmetric if one complete CSD cycle maps \((p_1,p_2,p_3)\) to \((p_3,p_2,p_1)\) and the next complete cycle maps it back.

Such a full-support reversal-symmetric projective two-cycle exists if and only if
\[
\lambda_2=\frac{\lambda_1+\lambda_3}{2}.
\]
When this arithmetic-progression condition holds, the two spectral-weight states are uniquely
\[
p_+=\left(\frac38+\frac{\sqrt2}{4},\frac14,\frac38-\frac{\sqrt2}{4}\right),\qquad
p_-=\left(\frac38-\frac{\sqrt2}{4},\frac14,\frac38+\frac{\sqrt2}{4}\right).
\]
Writing \(\lambda_1=m+h\), \(\lambda_2=m\), and \(\lambda_3=m-h\), where \(m>h>0\), the successive cycle-starting exact steepest-descent steps are
\[
t_+=\frac{1}{m+h/\sqrt2},\qquad t_-=\frac{1}{m-h/\sqrt2}.
\]
After the two CSD cycles, hence after four actual CSD updates, the gradient and error are multiplied by the same positive scalar
\[
Q=\frac{h^4}{(2m^2-h^2)^2}
 =\frac{(\kappa-1)^4}{(\kappa^2+6\kappa+1)^2},
\qquad \kappa=\frac{\lambda_1}{\lambda_3}.
\]
Consequently the exact per-update root factor on this orbit is
\[
Q^{1/4}=\frac{\kappa-1}{\sqrt{\kappa^2+6\kappa+1}}>0,
\]
so the orbit is R-linear, not R-superlinear. The special spectrum \((3,2,1)\) gives \(Q=1/49\), recovering the previously reported three-dimensional witness while classifying the whole reversal-symmetric family.

## Assumptions and scope
The objective is \(f(u)=\tfrac12 u^{\mathsf T}Au-b^{\mathsf T}u\) with real symmetric positive-definite \(A\). Exactly three distinct eigenvalues are active and each active spectral projector of the cycle-boundary gradient is nonzero. Eigenvalue multiplicities are allowed: only the three projector norms enter the weight dynamics, while the direction within each eigenspace is unchanged by polynomial iteration. The CSD cycle length is exactly \(j=2\), and the same exact steepest-descent step computed at the start of a cycle is reused for both updates in that cycle.

The classification is only for reversal-symmetric projective two-cycles. It does not classify all exceptional initial conditions, all projective periodic orbits, or the full null exceptional set in the generic convergence theorem.

## Proof
Normalize the spectrum by
\[
\Delta=\lambda_1-\lambda_3,\qquad
\beta=(1,s,0),\qquad
s=\frac{\lambda_2-\lambda_3}{\Delta}\in(0,1),
\]
and put
\[
\mu=p_1+s p_2.
\]
For a cycle of length \(j=2\), the exact CSD spectral-weight map obtained from the component update \(P_i g^+=(1-t\lambda_i)^2P_i g\) is
\[
T_i(p)=\frac{p_i\,|\mu-\beta_i|^4}{Z},\qquad
Z=\sum_{r=1}^3p_r|\mu-\beta_r|^4.
\]
This is the squared-weight form of the spectral component recurrence used in the source paper.

Assume \(T(p)=Rp\), where \(R(p_1,p_2,p_3)=(p_3,p_2,p_1)\), and also \(T(Rp)=p\). Since \(p_2>0\), the middle equation implies
\[
Z=|\mu-s|^4.
\]
The extreme equations therefore give
\[
\frac{p_3}{p_1}=\left(\frac{1-\mu}{|\mu-s|}\right)^4,
\qquad
\frac{p_1}{p_3}=\left(\frac{\mu}{|\mu-s|}\right)^4.
\]
For the reversed state define \(\mu'=p_3+s p_2\). Applying the return equations and comparing positive fourth roots yields
\[
\frac{1-\mu}{\mu}=\frac{\mu'}{1-\mu'},
\]
so \(\mu'=1-\mu\). But
\[
\mu+\mu'=p_1+p_3+2s p_2=1+(2s-1)p_2.
\]
Because \(p_2>0\), equality with \(1\) forces \(s=1/2\), which is exactly
\[
\lambda_2=\frac{\lambda_1+\lambda_3}{2}.
\]
This proves necessity.

Now set \(s=1/2\). Multiplying the two extreme equations gives
\[
\mu(1-\mu)=\left(\mu-\frac12\right)^2,
\]
whence
\[
\mu_\pm=\frac12\pm\frac{\sqrt2}{4}.
\]
For \(\mu_+\), the first ratio equation and \(p_1-p_3=2\mu_+-1=1/\sqrt2\) determine
\[
(p_1,p_2,p_3)=p_+.
\]
The other root gives \(p_-\). Direct substitution into the exact map gives \(T(p_+)=p_-\) and \(T(p_-)=p_+\), proving sufficiency and uniqueness within the stated symmetry class.

For the radial factor, write the arithmetic spectrum as \((m+h,m,m-h)\). The exact-line-search identity gives the two cycle-starting steps
\[
t_\pm=\frac{1}{m\pm h/\sqrt2}.
\]
On the middle eigenspace the two-cycle multiplier is
\[
\left(1-mt_+\right)^2\left(1-mt_-\right)^2
=\frac{h^4}{(2m^2-h^2)^2}.
\]
The same product is obtained on each extreme eigenspace, so the entire gradient is multiplied by \(Q\). Since the error is \(A^{-1}g\), it is multiplied by the same \(Q\). Substituting \(m=(\lambda_1+\lambda_3)/2\), \(h=(\lambda_1-\lambda_3)/2\) gives the stated condition-number formula.

## Verification
The bundled exact checker represents \(\mathbb Q(\sqrt2)\) by rational pairs. It verifies exactly that the two stated weight vectors sum to one, have the stated values of \(\mu\), and are swapped by the fourth-power projective CSD map for normalized spectrum \((1,1/2,0)\). It also verifies the common normalization \(Z=1/64\), positivity of the smaller extreme weight by an exact rational inequality, and the specialization \(Q=1/49\) at \(\kappa=3\). The checker uses no floating-point comparisons for the identities in the claim.

## Relationship to prior work
Gu proves that for CSD with \(q\) distinct eigenvalues and \(2j>q\), the cycle-starting gradient converges doubly exponentially outside a Lebesgue-null exceptional set. The present statement concerns a structured subset of that exceptional set for \(q=3\) and \(j=2\), and gives an exact if-and-only-if spectral condition inside a natural reversal symmetry class.

Li and Wang previously exhibit the concrete three-dimensional case with spectrum \((1,2,3)\), cycle length two, and a full-support projective period-two orbit satisfying four-update scaling by \(1/49\). The present classification contains that witness but is not merely its rescaling: adding a scalar multiple of the identity changes the CSD steps and the radial rate. The result identifies exactly which three-point spectra support this reversal symmetry and supplies its unique spectral weights and condition-number-dependent rate.

## Limitations
This does not claim that arithmetic spectra are necessary for arbitrary exceptional or periodic CSD behavior; necessity is proved only under the explicitly defined reversal-symmetric full-support two-cycle condition. It does not estimate the measure, codimension, or stability of the exceptional set. A highly relevant Li--Wang preprint was available through its public record and detailed abstract, but its full text was not accessible for a line-by-line comparison here; therefore there remains a residual originality risk that their full manuscript contains an unadvertised general arithmetic-spectrum classification. No such classification appeared in the accessible record or in the targeted searches described in the review.

## References
1. Ran Gu, “Doubly exponential convergence of the cyclic steepest descent method for strictly convex quadratics in arbitrary dimensions,” arXiv:2609.25800v1, first public 2026-09-22. MSC 90C25, 65K05, 90C06, 65F10.
2. Yu Li and Qihang Wang, “Exact counterexamples to R-superlinear convergence of cyclic steepest descent,” Zenodo record 22209278, version 3.0, published 2026-08-31, DOI 10.5281/zenodo.22209278.
