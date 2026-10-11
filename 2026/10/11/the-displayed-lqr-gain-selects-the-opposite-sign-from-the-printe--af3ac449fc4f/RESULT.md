# The displayed LQR gain selects the opposite sign from the printed Riccati convention
## Finding
In the synchronization section of Fu, Xu, and Xiao, the linearized error model uses
\[
\dot e=Ae+Bu_L,
\]
with \(B=I_4\), and the article subsequently displays
\[
A=\begin{pmatrix}
1&0&0&0\\
-10&0&1&0\\
0&0&0&1\\
0&1&0&0
\end{pmatrix},
\qquad Q=100I_4,\qquad R=I_4,
\]
together with the four-decimal matrix
\[
P=K=\begin{pmatrix}
13.9065&-4.1415&-0.2871&-0.1351\\
-4.1415&9.1334&0.4281&0.5049\\
-0.2871&0.4281&10.0164&0.5123\\
-0.1351&0.5049&0.5123&10.0244
\end{pmatrix}.
\]
The displayed matrix selects the standard LQR sign convention, not the sign convention printed in the article's Riccati and gain formulas. With the displayed decimals treated exactly,
\[
\left\|A^{\mathsf T}P+PA-P^2+100I_4\right\|_{\max}=0.0008945,
\]
while
\[
\left\|A^{\mathsf T}P+PA+P^2-100I_4\right\|_{\max}=221.28644292.
\]
The first expression is the standard continuous-time algebraic Riccati equation residual and is at the scale expected from rounding a gain to four decimals; the second is incompatible with a rounded solution.

Moreover, the displayed positive gain is stabilizing: \(A-P\) is Hurwitz. If the printed negative gain formula is applied literally, then \(K=-P\) and the article's own closed-loop expression \(A-BK\), with \(B=I_4\), becomes \(A+P\); this matrix has every eigenvalue in the open right half-plane. Thus the reproducible convention is \(K=P\) together with \(u_L=-Ke\), while the printed negative sign in the gain formula is inconsistent with both the listed matrix and stability.

## Assumptions and scope
The statement is about the linear error model and numerical gain printed in Section 4 of the source. The matrix entries shown above are treated as exact four-decimal rationals for verification. Standard continuous-time LQR uses
\[
A^{\mathsf T}P+PA-PBR^{-1}B^{\mathsf T}P+Q=0,
\qquad
K=R^{-1}B^{\mathsf T}P,
\qquad
u=-Ke.
\]
For the source's \(B=R=I_4\), these reduce to the formulas used in the residual calculation.

No assertion is made about an unprinted higher-precision matrix. The conclusion does not require such a matrix because the two candidate residuals differ by more than five orders of magnitude and the exact stability tests below have large margins.

## Proof
Let \(P_4\) denote the displayed four-decimal matrix. Direct rational arithmetic gives
\[
\left\|A^{\mathsf T}P_4+P_4A-P_4^2+100I_4\right\|_{\max}
=\frac{1789}{2000000}=0.0008945,
\]
and
\[
\left\|A^{\mathsf T}P_4+P_4A+P_4^2-100I_4\right\|_{\max}
=\frac{5532161073}{25000000}=221.28644292.
\]
Therefore the listed matrix is numerically consistent with the standard CARE and inconsistent with the printed-sign CARE.

For stability, exact characteristic-polynomial arithmetic gives
\[
\chi_{A-P_4}(\lambda)=\lambda^4+42.0807\lambda^3+684.8928096\lambda^2
+5075.824905837459\lambda+14355.1090592111890521.
\]
All coefficients are positive, and the quartic Routh–Hurwitz determinants satisfy
\[
\Delta_2=23744.94394709726>0,
\qquad
\Delta_3=95105361.59314738>0.
\]
Hence \(A-P_4\) is Hurwitz.

For the literal printed gain sign, \(K=-P_4\), so the closed-loop matrix is \(A+P_4\). Equivalently, consider \(-(A+P_4)\), whose characteristic polynomial is
\[
\lambda^4+44.0807\lambda^3+657.5206096\lambda^2
+3923.873869437459\lambda+7621.2541773651250521.
\]
Its coefficients are positive and
\[
\Delta_2=25060.094866157262>0,
\qquad
\Delta_3=83523730.59155181>0.
\]
Thus \(-(A+P_4)\) is Hurwitz, so every eigenvalue of \(A+P_4\) lies in the open right half-plane. Literal use of the negative gain sign therefore reverses the intended stability.

## Verification
The bundled verifier reconstructs the displayed matrices with exact rational arithmetic. It checks both Riccati residuals, derives both quartic characteristic polynomials by the Faddeev–LeVerrier recursion, and certifies the two Routh–Hurwitz tests. Its terminal success condition is `VERIFY_OK`.

The standard CARE sign was independently compared with an established continuous-time Riccati implementation and with a published LQR derivation, both of which use the negative quadratic term and positive state penalty, followed by the feedback law \(u=-Kx\) with \(K=R^{-1}B^{\mathsf T}P\).

## Relationship to prior work
The primary article states the source model, the synchronization construction, the closed-loop matrix \(A-BK\), the choices \(Q=100I_4\), \(R=I_4\), and the displayed matrix \(P=K\). A previous source-specific result on the same oscillator concerns the equilibrium's zero eigenvalue and center drift; it explicitly does not analyze the controller equations and does not imply the sign result here. Database searches for the DOI, title, printed matrix entries, Riccati terminology, gain-sign aliases, and the combinations \(A-P\) and \(A+P\) returned no source-specific prior statement of this controller-sign inconsistency. An analogous published sign inconsistency found for a different gyrostat model concerns different equations and gives no implication for this LQR calculation.

The standard continuous-time LQR formulas are prior theory; originality is claimed only for identifying which sign convention the source's displayed numerical matrix actually satisfies and for the exact stable-versus-unstable comparison of the two literal interpretations.

## Limitations
The finding is limited to the printed Section 4 linear error model and the displayed four-decimal gain. It does not infer which sign was used inside unavailable simulation code. The source's reported synchronization plots are therefore not declared false; they are compatible with use of the displayed positive gain and standard negative-feedback convention. The result also does not revisit the oscillator's equilibrium analysis, global hyperchaos claims, hardware implementation, or robustness experiments.

## References
Fu, Q.; Xu, X.; Xiao, C. *LQR Chaos Synchronization for a Novel Memristor-Based Hyperchaotic Oscillator*. Mathematics 2023, 11(1), 11. DOI: 10.3390/math11010011. Published 2022-12-20; primary MSC 34C28.

Valencia-Rivera, G. H.; Merchan-Villalba, L. R.; Tapia-Tinoco, G.; Lozano-Garcia, J. M.; Ibarra-Manzano, M. A.; Avina-Cervantes, J. G. *Hybrid LQR-PI Control for Microgrids under Unbalanced Linear and Nonlinear Loads*. Mathematics 2020, 8(7), 1096. DOI: 10.3390/math8071096. Its continuous-time LQR equations use \(u=-Kx\), \(K=R^{-1}B^{\mathsf T}P\), and the standard CARE sign.

SciPy documentation for `solve_continuous_are`, which states the standard continuous-time algebraic Riccati equation \(XA+A^{\mathsf H}X-XBR^{-1}B^{\mathsf H}X+Q=0\).
