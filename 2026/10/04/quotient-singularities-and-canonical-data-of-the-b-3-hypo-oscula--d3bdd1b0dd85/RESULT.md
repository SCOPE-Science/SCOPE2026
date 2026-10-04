# Quotient singularities and canonical data of the \(B_3\) hypo-osculating surface
## Finding
For Szpond's \(B_3\) surface \(X_B\subset\mathbb P^5\), the contraction \(Y=\operatorname{Bl}_Z\mathbb P^2\to X_B\) is the minimal resolution of a normal surface and each of its three singular points is analytically the cyclic quotient singularity \(\frac{1}{3}(1,1)\). Consequently every singularity has local class group \(\mathbb Z/3\mathbb Z\), canonical index \(3\), and discrepancy \(-\frac13\); globally
\[
K_{X_B}^2=1,\qquad K_{X_B}\cdot\mathcal O_{X_B}(1)=-3,
\]
and a general hyperplane section has arithmetic genus \(3\).

## Assumptions and scope
Work over \(\mathbb C\). Let \(Z\) be the nine-point \(B_3\) configuration and let \(Y=\operatorname{Bl}_Z\mathbb P^2\), with pullback of a line denoted \(H\) and exceptional curves \(E_1,\ldots,E_9\). Put
\[
M=4H-\sum_{i=1}^9E_i.
\]
Szpond proves that \(|M|\) is base-point-free and gives a birational morphism \(\varphi_M:Y\to X_B\subset\mathbb P^5\), an isomorphism away from the three strict transforms
\[
N_1=H-E_2-E_3-E_8-E_9,\quad
N_2=H-E_1-E_3-E_6-E_7,\quad
N_3=H-E_1-E_2-E_4-E_5,
\]
which are contracted to the three singular points of \(X_B\). The claim concerns exactly this named surface and these three points.

## Proof
Each \(N_i\) is a smooth rational curve with \(N_i^2=-3\). The three curves are pairwise disjoint: the corresponding coordinate lines meet only at blown-up points, so their strict transforms have intersection zero. Moreover \(M\cdot N_i=0\), as in the source.

The source gives the homogeneous coordinate ring \(R=S/I(X_B)\), for \(S=\mathbb C[u_0,\ldots,u_5]\), with minimal free resolution
\[
0\to S(-5)^3\to S(-4)^6\to S(-2)^3\oplus S(-3)\to S\to R\to0.
\]
Since \(X_B\) is a projective surface, \(\dim R=3\). Auslander--Buchsbaum therefore gives \(\operatorname{depth}R=6-3=3\), so \(R\) is Cohen--Macaulay and \(X_B\) satisfies Serre's condition \(S_2\). Szpond's theorem states that the singular locus consists of exactly the three contracted points; hence every codimension-one point is smooth, so \(X_B\) satisfies \(R_1\). Serre's criterion shows that \(X_B\) is normal.

Thus \(Y\to X_B\) is a resolution whose exceptional locus over each singular point is one smooth rational \((-3)\)-curve. It is minimal. The Hirzebruch--Jung classification identifies a normal surface singularity with this one-vertex resolution graph with the cyclic quotient \(\frac13(1,1)\); equivalently, Iyama--Wemyss explicitly record that a minimal resolution consisting of one \((-3)\)-curve is \(\mathbb C[[x,y]]^{\frac13(1,1)}\).

For \(\frac13(1,1)\), the local divisor class group is \(\mathbb Z/3\mathbb Z\). The canonical two-form transforms by the character \(\zeta^2\), so the canonical index is \(3\). If \(f:Y\to X_B\) and \(N\) is any of the three exceptional curves, write
\[
K_Y=f^*K_{X_B}+aN
\]
locally. Adjunction gives \(K_Y\cdot N=-2-N^2=1\), while \(f^*K_{X_B}\cdot N=0\). Hence \(1=-3a\), so \(a=-\frac13\). In particular the singularities are klt but noncanonical.

Globally, \(K_Y=-3H+\sum E_i\), so \(K_Y^2=0\), \(K_Y\cdot N_i=1\), \(M^2=7\), and \(K_Y\cdot M=-3\). Because the \(N_i\) are disjoint,
\[
f^*K_{X_B}=K_Y+\frac13(N_1+N_2+N_3),
\]
whence
\[
K_{X_B}^2=0+\frac23(3)+\frac19(-9)=1.
\]
Also \(M=f^*\mathcal O_{X_B}(1)\) and \(M\cdot N_i=0\), so
\[
K_{X_B}\cdot\mathcal O_{X_B}(1)=K_Y\cdot M=-3.
\]
A general hyperplane avoids the three singular points. Its pullback is therefore a general member \(C\in|M|\) disjoint from the \(N_i\), and adjunction on \(Y\) gives
\[
p_a(C)=1+\frac{M^2+K_Y\cdot M}2=1+\frac{7-3}2=3.
\]

## Verification
The accompanying verifier checks the divisor-intersection arithmetic, pairwise disjointness of the three exceptional classes, the Hilbert-series numerator implied by the displayed minimal resolution, the discrepancy equation, the canonical-index character calculation, and the global canonical and sectional-genus formulas. It uses exact integer and rational arithmetic only.

The normality step is not inferred from the arithmetic script alone: it uses the published minimal free resolution together with the published statement that the surface has exactly three singular points. The local analytic classification uses the standard Hirzebruch--Jung correspondence, cross-checked against the explicit one-\((-3)\)-curve statement of Iyama--Wemyss.

## Relationship to prior work
Szpond proves that the \(B_3\) morphism is birational, contracts exactly \(N_1,N_2,N_3\), and yields a degree-seven surface with three singular points; she also gives the defining ideal and minimal free resolution. The inspected full text does not classify those singularities as cyclic quotients and does not state their local class groups, canonical indices, discrepancies, \(K^2\), or sectional genus.

Bauer--Malara--Szemberg--Szpond study the same nine-point \(B_3\) configuration and its unexpected quartic, but the inspected article does not give the above local-singularity package for \(X_B\). Iyama--Wemyss is used only for the general identification of a one-\((-3)\)-curve minimal resolution with the \(\frac13(1,1)\) quotient; it does not discuss Szpond's surface.

Targeted searches for the surface name together with “cyclic quotient”, “\(\frac13(1,1)\)”, “canonical index”, “discrepancy”, and “sectional genus” did not locate a source stating this package. This is evidence of non-coverage, not a proof that no equivalent statement exists under different terminology.

## Limitations
The result is specific to Szpond's degree-seven \(B_3\) surface over \(\mathbb C\). It does not classify singularities of other unexpected or hypo-osculating surfaces and does not assert a deformation or smoothing theorem. In particular, \(\frac13(1,1)\) is not a rational double point, and no claim of canonical singularities is made.

## References
1. J. Szpond, *Unexpected curves and Togliatti-type surfaces*, arXiv:1810.06607; Math. Nachr. 293 (2020), 158--168.
2. T. Bauer, G. Malara, T. Szemberg, J. Szpond, *Quartic unexpected curves and surfaces*, arXiv:1804.03610.
3. O. Iyama, M. Wemyss, *A New Triangulated Category for Rational Surface Singularities*, Illinois J. Math. 55 (2011), 325--341; arXiv:0905.3940.
