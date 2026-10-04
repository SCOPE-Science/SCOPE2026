# A hyperbolic invasion saddle at the first-prey-free equilibrium
## Finding
For the boundary equilibrium \(P_4=(0,\bar x_2,\bar y)\) in Kadhim, Elobaid, Al-Saidi and Jaber's switching-refuge-Allee ecological model, the source displays the factorized characteristic equation
\[
(\bar b_{11}-\lambda)(\lambda^2-B_1\lambda+B_2)=0,
\]
with \(\bar b_{11}=r_1>0\), \(B_1<0\), and \(B_2>0\). These same displayed inequalities force \(P_4\) to be a hyperbolic index-one saddle rather than a saddle-node. The eigenvalue transverse to the first-prey-free boundary is exactly \(r_1\), so the first prey has a strictly positive invasion exponent at every such equilibrium.

## Assumptions and scope
The claim concerns the source model with its stated biological assumption \(r_1>0\), and it takes the paper's local conditions \(B_1<0\) and \(B_2>0\) exactly as displayed for \(P_4\). No assertion is made here about parameter values for which those two block inequalities fail. The result is a local spectral classification and invasion statement; it does not establish global persistence or exclude other bifurcations elsewhere in the model.

## Proof
The source's Jacobian at \(P_4\) is block triangular in the first coordinate and yields
\[
(\bar b_{11}-\lambda)(\lambda^2-B_1\lambda+B_2)=0,
\]
where \(\bar b_{11}=r_1>0\). Thus one eigenvalue is \(\lambda_1=r_1>0\).

Let \(\lambda_2,\lambda_3\) be the roots of the quadratic factor. Vieta's relations give
\[
\lambda_2+\lambda_3=B_1<0,\qquad \lambda_2\lambda_3=B_2>0.
\]
If these roots are real, positive product and negative sum force both to be negative. If they are nonreal, they are a complex-conjugate pair with real part \(B_1/2<0\). Hence in all cases \(\operatorname{Re}\lambda_2<0\) and \(\operatorname{Re}\lambda_3<0\).

Therefore no eigenvalue has zero real part: \(P_4\) is hyperbolic with one unstable and two stable directions. It is an index-one saddle. In particular it cannot be a saddle-node equilibrium, because a saddle-node bifurcation of an autonomous ODE requires a zero eigenvalue at the critical equilibrium. The positive transverse eigenvalue \(r_1\) also gives the ecological interpretation: an infinitesimal introduction of the missing first prey grows to first order at rate \(r_1\).

## Verification
The proof is algebraic and requires no floating-point calculation. It uses only the characteristic factorization and signs printed in the source, Vieta's relations for a quadratic, and the standard necessary zero-eigenvalue condition for a saddle-node bifurcation. The source text was inspected at the equations defining \(J_4\), \(B_1\), and \(B_2\), and at the sentence that labels \(P_4\) a saddle-node.

## Relationship to prior work
The motivating 2025 article explicitly lists MSC 2020 class 92D40 first and studies a two-prey/one-predator ecological model with switching, refuge, and an Allee effect. Its own local calculation already isolates the positive eigenvalue \(r_1\) and the stable two-dimensional block but then assigns the incompatible label “saddle-node.” Standard bifurcation theory requires a zero eigenvalue at a saddle-node. Targeted exact-title, DOI, equilibrium-label, and implication searches found no published correction of this source-specific classification.

A 2021 antecedent studies a related two-prey/one-predator switching model and supplies broader ecological context, but it does not cover this exact 2025 refuge-plus-Allee equilibrium statement. The present result is therefore a correction and structural interpretation of the newer model's displayed spectrum, not a new generic definition of saddle-node bifurcation.

## Limitations
The conclusion \(\operatorname{Re}\lambda_2,\operatorname{Re}\lambda_3<0\) uses the source's stated inequalities \(B_1<0\) and \(B_2>0\). If either inequality fails, the two-dimensional block needs separate classification; nevertheless \(\lambda_1=r_1>0\) still prevents local asymptotic stability for \(r_1>0\). A later erratum could supersede the source wording. No claim is made about nonlinear global dynamics or about the existence of bifurcations at other equilibria.

## References
1. A. J. Kadhim, R. M. Elobaid, N. M. G. Al-Saidi, and A. S. Jaber, “Modeling of the switching effect on two prey and one predator with the presence of Allee effects and refuge,” *Computational and Mathematical Biophysics* 13 (2025), article 20250028, DOI 10.1515/cmb-2025-0028.
2. Y. A. Kuznetsov, “Saddle-node bifurcation,” *Scholarpedia* 1(10):1859 (2006), DOI 10.4249/scholarpedia.1859.
3. S. Saha and G. P. Samanta, “Modelling of a two prey and one predator system with switching effect,” *Computational and Mathematical Biophysics* 9 (2021), 90–113, DOI 10.1515/cmb-2020-0120.
