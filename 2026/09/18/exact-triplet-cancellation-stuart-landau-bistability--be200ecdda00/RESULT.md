# Exact triplet cancellation collapses the second-order sync–splay stability overlap

## Statement

Consider the three-oscillator Stuart–Landau system and mixed-order coupling design of Muolo, Nakao and Bick (2026), in the straight-isochrone setting \(d=0\), with no self-coupling. Their second-order phase reduction for linearly coupled oscillators contains three explicit three-phase Fourier harmonics for oscillator 1,
\[
A_1=\sin(2\theta_2-\theta_3-\theta_1),\qquad
A_2=\sin(2\theta_3-\theta_2-\theta_1),
\]
and
\[
S_1=\sin(\theta_2+\theta_3-2\theta_1+2\rho),
\]
with second-order coefficients proportional to
\[
w_{12}w_{23},\qquad w_{13}w_{32},\qquad -2w_{12}w_{13},
\]
respectively. The engineered physical nonpairwise coupling in their Eq. (19) produces the same three harmonics at first order in its own strength \(\eta\), with coefficients
\[
-w_{1232},\qquad -w_{1323},\qquad +w_{1213}.
\]

With the source scaling
\[
\eta=\frac{\varepsilon^2}{4a},
\]
all three explicit triplet harmonics cancel simultaneously if the physical motif weights are chosen as
\[
\boxed{
 w_{1232}=w_{12}w_{23},\qquad
 w_{1323}=w_{13}w_{32},\qquad
 w_{1213}=2w_{12}w_{13},
}
\]
with the corresponding cyclic choices for oscillators 2 and 3.

For the unweighted pairwise triangle, this means unit weights for the two asymmetric physical motifs and weight \(2\) for the symmetric physical motif. Thus one global strength \(\eta\) is sufficient for exact coefficient-wise cancellation once the motif weights already present in the engineered coupling are used as design variables.

This statement concerns the explicit three-phase Fourier harmonics. Some remaining second-order terms have an emergent nonpairwise origin encoded in path-dependent weights even though their phase dependence involves only one phase difference, so the result does not erase the physical provenance of every emergent term.

## Coefficient proof

From Eqs. (8), (17), (18) and (20) of the source, the total coefficients of \(A_1,A_2,S_1\) in the mixed-order phase equation are
\[
\frac{\varepsilon^2}{4a}w_{12}w_{23}-\eta w_{1232},
\]
\[
\frac{\varepsilon^2}{4a}w_{13}w_{32}-\eta w_{1323},
\]
and
\[
-\frac{\varepsilon^2}{4a}\,2w_{12}w_{13}+\eta w_{1213}.
\]
Substitution of \(\eta=\varepsilon^2/(4a)\) gives the boxed choices above. Since the three harmonics are distinct Fourier modes on the phase torus, these equalities are also the coefficient-wise cancellation conditions for fixed \(\eta\).

The source's numerical design sets all nonzero weights to one. Under that additional restriction the asymmetric harmonics cancel while only half of the symmetric harmonic cancels. The weight-2 symmetric motif removes the remaining half without introducing a second global coupling scale.

## Pairwise-additive residual for the unweighted triangle

Take \(w_{ij}=1\) for \(i\ne j\), set the asymmetric physical motif weights to \(1\), the symmetric motif weights to \(2\), and retain terms through second order. After the triplet cancellation, the phase equation has the pairwise-additive functional form
\[
\dot\theta_i=\omega+\sum_{j\ne i}H(\theta_j-\theta_i)+O(\varepsilon^3),
\]
where
\[
\boxed{
H(\phi)=\varepsilon\sin(\phi+\rho)
+\frac{\varepsilon^2}{4a}
\left[
\sin 2\rho+\sin 2\phi+\sin(\phi+2\rho)-\sin(2\phi+2\rho)
\right].
}
\]
This is an identity for the retained mixed-order phase truncation. It does not say that the full physical system is pairwise coupled: the cubic physical terms used for cancellation remain genuinely nonpairwise.

## Exact collapse of the local sync–splay stability overlap

Let
\[
c=\cos\rho,
\qquad
F(c)=4ac+3\varepsilon-2\varepsilon c^2.
\]
For full synchrony, the two nontrivial phase eigenvalues coincide and are
\[
\boxed{
\lambda_{\mathrm{sync}}
=-3H'(0)
=-\frac{3\varepsilon}{4a}F(c).
}
\]

For the three-oscillator splay state \((0,2\pi/3,4\pi/3)\), the two nontrivial eigenvalues form a complex-conjugate pair. Their common real part is
\[
\boxed{
\operatorname{Re}\lambda_{\mathrm{splay}}
=-\frac32\left[H'(2\pi/3)+H'(-2\pi/3)\right]
=\frac{3\varepsilon}{8a}F(c).
}
\]
Consequently,
\[
\boxed{
\lambda_{\mathrm{sync}}
=-2\operatorname{Re}\lambda_{\mathrm{splay}}.
}
\]

Therefore synchrony and splay cannot both be linearly stable in this exactly canceled second-order phase model. Their local stability boundaries coincide exactly: the sync–splay linear-stability overlap that is present in the uncanceled second-order model collapses to a single transition.

For \(0<\varepsilon<4a\), the relevant root of \(F(c)=0\) is the unique root with \(c\in(-1,0)\),
\[
\boxed{
 c_*=\frac{a-\sqrt{a^2+\tfrac32\varepsilon^2}}{\varepsilon},
 \qquad
 \rho_*=\arccos c_*.
}
\]
Synchrony is linearly stable for \(F(c)>0\), while splay is linearly stable for \(F(c)<0\). In the weak-coupling limit,
\[
\rho_*=\frac{\pi}{2}+\frac{3\varepsilon}{4a}+O\!\left((\varepsilon/a)^3\right).
\]
Thus exact triplet cancellation does not restore the first-order Kuramoto threshold \(\rho=\pi/2\): residual pairwise second-order corrections shift the common transition.

## Relation to prior results

Muolo, Nakao and Bick derive the second-order emergent harmonics and the engineered physical nonpairwise coupling used here. Their simplest unweighted design uses the same global scaling \(\eta=\varepsilon^2/(4a)\) with all nonzero physical motif weights equal to one; it cancels the asymmetric triplet harmonic exactly and half of the symmetric one, and the paper studies the resulting stability regions numerically. The present result uses the independent motif weights already appearing in their Eq. (19) to match the unequal emergent coefficients exactly, then derives the resulting closed stability relation.

Analytic second-order stability formulas for synchrony and splay in uncanceled Stuart–Landau phase reductions are already part of the literature, including Bick, Böhle and Kuehn (2024); they are not claimed here. Likewise, general design of pairwise and higher-order interaction functions to realize prescribed Kuramoto-type phase harmonics is established by Namura, Muolo and Nakao (2026); general harmonic realization is not claimed here.

The source-specific contribution claimed here, to the best of our knowledge, is the simultaneous motif-weight cancellation of all explicit triplet Fourier modes in this 2026 construction, the resulting pairwise-additive phase dependence for the unweighted triangle through second order, and the exact identity forcing coincidence of the synchronization and splay stability thresholds.

## Verification

`artifacts/verify_triplet_cancellation.py` symbolically reconstructs the retained phase vector field from the source formulas, verifies its pairwise-additive residual form after the 1:1:2 motif choice, and checks
\[
\lambda_{\mathrm{sync}}+2\operatorname{Re}\lambda_{\mathrm{splay}}=0
\]
as an exact symbolic identity.

## Limitations

- The derivation uses the three-oscillator Stuart–Landau setting of the source with straight isochrones \(d=0\) and no self-coupling.
- The cancellation is exact for the retained mixed-order phase model through \(O(\varepsilon^2)\). It does not imply exact cancellation in the full physical oscillator system at finite coupling; mixed and higher-order terms begin beyond the retained order.
- The stability result concerns local linear stability of synchrony and the three-oscillator splay state. It does not rule out other attractors or other forms of multistability.
- The result cancels explicit three-phase Fourier harmonics, not every second-order correction and not every term whose network provenance is emergent nonpairwise.
- The common threshold remains shifted from \(\rho=\pi/2\); only the sync–splay stability overlap is removed at this order.
- The usual weak-coupling assumptions behind the phase reduction remain in force.
- The primary source is very recent, so unindexed revisions or discussions remain a residual originality risk.

## References

1. R. Muolo, H. Nakao, C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1 (2026). https://arxiv.org/abs/2609.20632
2. C. Bick, T. Böhle, C. Kuehn, *Higher-Order Network Interactions Through Phase Reduction for Oscillators with Phase-Dependent Amplitude*, Journal of Nonlinear Science 34, 77 (2024). https://doi.org/10.1007/s00332-024-10053-3
3. N. Namura, R. Muolo, H. Nakao, *Optimal interaction functions realizing higher-order Kuramoto dynamics with arbitrary limit-cycle oscillators*, Chaos 36, 023120 (2026). https://doi.org/10.1063/5.0307452
