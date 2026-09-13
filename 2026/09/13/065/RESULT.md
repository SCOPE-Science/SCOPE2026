# Opposite-warp 4-torus: the second heat coefficient does not vanish

## Context

Let Theta be a fixed Diophantine antisymmetric 4x4 matrix and A_Theta^infty the smooth quantum 4-torus with trace tau, derivations delta_j and generators U_j. For |a|<=1/2 put h_a=a(U_1+U_1^*), k_a=exp(h_a/2), and K_a for left multiplication by k_a. The volume-balanced opposite-warp Laplacian is Delta_a=K_a delta_1^*delta_1 K_a+K_a delta_2^*delta_2 K_a+K_a^{-1} delta_3^*delta_3 K_a^{-1}+K_a^{-1} delta_4^*delta_4 K_a^{-1}. Assume Tr(exp(-t Delta_a))=a0(a) t^{-2}+a2(a)+O(t^eps). The admitted target asks whether a2(a)=0 for all admissible a.

## Definitions

f(x1)=a cos x1, k=e^f, g=diag(e^{-2f},e^{-2f},e^{2f},e^{2f}}), V=-k d11 k=-e^{2f}(f''+f'^2). Delta_g is the scalar Laplacian of g. C_*>0 is the standard positive heat prefactor, conventionally (4pi)^{-2}.

## Result

a2 is not identically zero. With any positive normalization: a2(0)=0; a2(a)<0 for every 0<|a|<=1/2; in particular a*=1/2 gives a2(1/2)<=-pi^2/72<-0.13 (about -1.86 in (4pi)^{-2} normalization).

## Proof / evidence

Theta-independence: h_a depends only on U_1, so K_a shifts only the m_1 Fourier index up to unimodular Theta phases. A fiberwise diagonal unitary W over transverse modes gauges these phases away (discrete primitive along the Z chain), commutes with diagonal derivations, and gives W Delta_a^Theta W^*=Delta_a^0 with identical heat traces. Hence the NC coefficient equals the commutative one. At Theta=0, Delta_a^0=Delta_g+V with sqrt(det g)=1 and dvol=dx. For g above, R=2e^{2f}(-f''-3f'^2), verified by independent Christoffel/Ricci computation and output/artifacts/verify_curvature.py (ALL CHECKS PASSED), so R/6-V=(2/3)f''e^{2f}. With Vol(T^3)=(2pi)^3, J(a)=int(R/6-V)=(2pi)^3 int (2/3)f''e^{2f} and a2=C_*J. Periodic integration by parts gives J(a)=-(4/3)(2pi)^3 int (f')^2 e^{2f}<=0, strict for a!=0. For f=a cos x1 this is -(4/3)(2pi)^3 a^2 int sin^2 x e^{2a cos x}dx. At a=1/2, I=int (sin^2 x/4)e^{cos x}dx>=int_{pi/6}^{pi/3}(sin^2 x/4)dx=pi/48 since e^{cos}>=1 there, so J<=-2pi^4/9 and a2<=-pi^2/72. Quadrature gives about -1.86, consistent with the rigorous bound.

## Limitations

Uses the target-granted two-term expansion with O(t^eps) remainder; the remainder is not re-proved. The sign is normalization-independent; the number -pi^2/72 is in (4pi)^{-2} normalization and rescales by a positive constant otherwise.

## Reproducibility

Run python3 output/artifacts/verify_curvature.py; it checks R, R/6-V, the small-a coefficient -32pi^4/3, and the pi/48 bound. An independent brute-force Christoffel check reproduces the same Ricci components and curvature.

## References

Fathizadeh-Khalkhali, Scalar curvature for noncommutative four-tori, arXiv:1301.6135; Sitarz, Wodzicki residue and minimal operators on a noncommutative 4-dimensional torus, J. Pseudo-Differ. Oper. Appl. 5:305-317 (2014); Gilkey heat-invariant theory and Vassilevich heat-trace review arXiv:0708.4209.
