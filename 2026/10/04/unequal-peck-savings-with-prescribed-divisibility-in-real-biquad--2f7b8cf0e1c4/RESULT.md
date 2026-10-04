# Unequal Peck savings with prescribed divisibility in real biquadratic fields
## Finding
Let \(a,b\) be positive integers such that none of \(a,b,ab\) is a square. Put
\[
\alpha_1=\sqrt{ab},\qquad \alpha_2=\sqrt a,\qquad \alpha_3=\sqrt b,
\]
and let
\[
\Lambda=\mathbb Z+\alpha_1\mathbb Z+\alpha_2\mathbb Z+\alpha_3\mathbb Z.
\]
Write \(Z_\Lambda\) for the multiplier ring of \(\Lambda\),
\[
U_m=\{u\in Z_\Lambda^\times:u\equiv1\pmod{mZ_\Lambda}\},
\qquad I_m=[Z_\Lambda^\times:U_m].
\]
There are constants \(C,c>0\), depending only on \(a,b\), such that for every integer \(m\ge1\), every real \(T\) satisfying \(\log T\ge cI_m\), and every pair of real numbers \(f_2,f_3\ge1\) with
\[
f_2f_3=\frac{\log T}{I_m},
\]
there is an integer \(n\) with \(1\le n\le T\) and \(m\mid n\) such that
\[
\|n\alpha_1\|\le Cn^{-1/3},\qquad
\|n\alpha_i\|\le \frac{Cn^{-1/3}}{f_i}\quad(i=2,3).
\]
Since \(I_m\le m^4\), an explicit weaker form is obtained by replacing the product condition by \(g_2g_3=\log T/m^4\) and the threshold by \(\log T\ge cm^4\).

## Assumptions and scope
The field is the real biquadratic field \(K=\mathbb Q(\sqrt a,\sqrt b)\) with the natural basis above. The constants are uniform in \(m,T,f_2,f_3\) but depend on the fixed field. The quantity \(I_m\) is finite because reduction modulo \(mZ_\Lambda\) has finite image on the unit group. No claim of optimality of the factor \(I_m\), the threshold constant \(c\), or the exponent \(4\) in the explicit corollary is made.

## Proof
Dhanda--Flynn--Haynes construct a rank-three lattice \(\Gamma\) from the positive units of \(Z_\Lambda\). For the congruence subgroup \(U_m\), their divisibility argument replaces it by a sublattice \(\Gamma_m\) of index
\[
h_m=[P:P\cap U_m]\le I_m,
\]
so if \(V\) is the covolume of \(\Gamma\), the covolume of \(\Gamma_m\) is \(V_m=h_mV\le I_mV\). Moreover, for \(u\in U_m\), the denominator coordinate
\[
q=\operatorname{Tr}(\alpha_1^*u)
\]
is divisible by \(m\).

In the biquadratic case the source computes the two relevant error coordinates exactly. With \(\boldsymbol\zeta\) in the trace-zero plane, put
\[
y_2=\zeta_1-\zeta_3,\qquad y_3=\zeta_2-\zeta_3.
\]
Then
\[
\Psi_2(\boldsymbol\epsilon)=2\alpha_1^*\alpha_2e^{\zeta_3}(e^{y_2}-1),\qquad
\Psi_3(\boldsymbol\epsilon)=2\alpha_1^*\alpha_3e^{\zeta_3}(e^{y_3}-1).
\]
This is the decoupling that allows completely unequal side lengths.

Apply the source's shaped-box Minkowski argument to \(\Gamma_m\) instead of \(\Gamma\). If \(D\) is the fixed determinant factor in that argument, write
\[
J_m=2DV_m,\qquad J=2DV.
\]
Thus \(J_m\le I_mJ\). Let \(C'\ge2\) be the fixed height-to-denominator constant from the source, set \(S=T/C'\), and define
\[
P_m=\frac{J_m\log T}{I_m\log S}.
\]
For \(T\ge C'^2\), one has \(P_m\le2J\). Let \(i_1\in\{2,3\}\) be an index for which \(f_{i_1}=\max(f_2,f_3)\), let \(i_2\) be the other index, and set
\[
\mu_{i_1}=8P_m,\qquad \mu_{i_2}=\frac18,\qquad
\eta_i=\frac{\mu_i}{f_i}.
\]
Because \(f_2f_3=\log T/I_m\),
\[
\eta_2\eta_3
=\frac{P_m}{f_2f_3}
=\frac{J_m}{\log S},
\]
which is exactly the volume condition for the shaped box over \(\Gamma_m\). Also
\[
f_{i_1}\ge\sqrt{\frac{\log T}{I_m}},\qquad
\mu_{i_1}\le16J,\qquad \eta_{i_2}\le\frac18.
\]
Hence, after choosing \(c\) large enough in terms of the fixed field, the condition \(\log T\ge cI_m\) forces \(\max(\eta_2,\eta_3)\le1/4\). The shaped-box lemma therefore supplies a totally positive \(u\in U_m\) with \(1<u\le S\),
\[
|y_i(\boldsymbol\zeta(u))|\le2\eta_i\quad(i=2,3),\qquad
|\boldsymbol\zeta(u)|\le\frac12.
\]
The displayed exact error factorization and \(|e^w-1|\le2|w|\) for \(|w|\le1\) give
\[
|\Psi_i(\boldsymbol\epsilon)|\le16\alpha_1^*\alpha_i\eta_i\quad(i=2,3),
\]
while the first coordinate stays bounded by an absolute field-dependent constant. Since both \(\mu_i\) are bounded solely in terms of the field, the source's exact denominator/error identity yields
\[
|p_1-q\alpha_1|\ll u^{-1/3},\qquad
|p_i-q\alpha_i|\ll\frac{u^{-1/3}}{f_i}\quad(i=2,3),
\]
with constants independent of \(m,T,f_2,f_3\). Enlarging \(c\) once more makes both latter errors strictly less than \(1\), so the source's argument excluding \(q=0\) applies unchanged. Put \(n=|q|\). Then \(m\mid n\), \(1\le n\le C'u\le T\), and \(u^{-1/3}\ll n^{-1/3}\), proving the theorem.

Finally, the source gives \(I_m\le m^4\). If \(g_2g_3=\log T/m^4\), set \(s=\sqrt{m^4/I_m}\) and \(f_i=sg_i\). Then \(f_2f_3=\log T/I_m\) and \(f_i\ge g_i\), so the theorem implies the stated explicit \(m^4\)-version.

## Verification
The proof is symbolic and uses no finite enumeration. The critical imported ingredients were checked in the primary source: the congruence subgroup gives \(m\mid q\) and has index at most \(I_m\); the shaped-box lemma depends on the covolume only through its volume constant; and the biquadratic error map factorizes coordinatewise. Replacing \(V\) by \(V_m\) changes only the box-volume constant, while \(V_m\le I_mV\) gives the uniform bound needed above.

The boundary checks are explicit: \(m=1\) has \(I_1=1\) and recovers the source's fully unequal biquadratic theorem; the hypothesis \(\log T\ge cI_m\) is used only to make the longer side of the shaped box small enough; and the proof makes no assertion for smaller \(T\).

## Relationship to prior work
Dhanda, Flynn, and Haynes prove two separate results relevant here: prescribed divisibility of denominators with balanced errors, and completely unequal logarithmic savings for the natural basis of a real biquadratic field. Their statements do not provide both constraints simultaneously. The present result combines the congruence sublattice from the former proof with the coordinatewise error factorization and shaped box from the latter proof, and records the quantitative loss of logarithmic budget as the unit-congruence index \(I_m\).

Bugeaud and de Mathan's contemporaneous refinement treats unequal Peck savings in arbitrary real algebraic fields under a comparability condition on the exponents; its stated result does not impose prescribed divisibility on the denominator. De Mathan's earlier divisibility paper treats a different simultaneous-approximation framework in dimension two and does not cover the all-admissible biquadratic weight allocation above.

## Limitations
The theorem is restricted to the natural basis of real biquadratic fields because the exact factorization of the two nonlinear error coordinates is what removes the comparability restriction. The index factor \(I_m\) is a sufficient quantitative cost inherited from the congruence-sublattice argument; no lower bound showing that this cost is necessary is proved. The result does not establish a new optimal \(p\)-adic exponent.

## References
1. K. Dhanda, J. Flynn, A. Haynes, *A geometric proof of Peck's theorem*, arXiv:2609.29469v1, 2026. See Theorem 2, Lemma 10, Theorem 3, and equations (16), (28), and (29).
2. Y. Bugeaud, B. de Mathan, *Refinements of Peck's theorem on simultaneous approximation to algebraic numbers*, arXiv:2609.29360v1, 2026.
3. B. de Mathan, *Simultaneous Diophantine approximation with a divisibility condition*, Journal de théorie des nombres de Bordeaux 36 (2024), 987--1008, DOI:10.5802/jtnb.1303.
