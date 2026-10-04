# Exact triple-root locus in the cooperative May–Holling–Tanner equilibrium cubic
## Finding
For the reduced predator–prey system studied by Reyes-Bahamón et al., positive equilibria in the paper's Case 3 are controlled by the monic cubic
\[
p(u)=u^3+(L-1)u^2+(D-E)u+(N-A).
\]
Assume
\[
N-A<0,\qquad L<1,\qquad D-E>0,
\]
and write \(J=1-L>0\) and
\[
D_1=J^2-3(D-E).
\]
The triple-root boundary is exactly
\[
D_1=0,\qquad \Delta_2=0,
\]
where \(\Delta_2\) is the cubic discriminant expression printed in the source. Equivalently,
\[
D-E=\frac{J^2}3,\qquad N-A=-\frac{J^3}{27},
\]
and then
\[
p(u)=\left(u-\frac J3\right)^3.
\]
Thus the unique root is positive and has multiplicity three at \(u=J/3\).

The source's Lemma 7(b) instead assigns the triple root to \(D_1=0\) and \(\Delta_2<0\). That parameter case is empty. The source's own formula for \(\Delta_2\) becomes a perfect square when \(D_1=0\), so \(\Delta_2<0\) is impossible. The displayed derivative in its Eq. (37) is also incompatible with the cubic: the correct identity is
\[
p'(u)=3\left(u-\frac J3\right)^2,
\]
not a square involving \(Q/B\).

## Assumptions and scope
The claim concerns only the algebraic equilibrium classification in Case 3 of the dimensionless system, under \(N-A<0\), \(L<1\), and \(D-E>0\). The coefficients used by the source are
\[
L=B+P+M,\qquad D=A+BM+2MP,\qquad E=B+P,\qquad N=P^2M+BMP.
\]
The parameter \(Q\) multiplies the predator equation in the reduced vector field but does not occur in the equilibrium cubic \(p(u)\). No claim is made here about stability, Hopf or Bogdanov–Takens coefficients, global basins, or the cases analyzed later in the source.

## Proof
Since \(L-1=-J\), the cubic is
\[
p(u)=u^3-Ju^2+(D-E)u+(N-A).
\]
Its derivative is
\[
p'(u)=3u^2-2Ju+(D-E).
\]
If \(D_1=J^2-3(D-E)=0\), then \(D-E=J^2/3\), and completing the square gives
\[
p'(u)=3\left(u-\frac J3\right)^2.
\]
This identity is forced directly by the coefficients and contains no \(Q\).

For the source's discriminant quantity,
\[
\Delta_2=\bigl(3D_1(L-1)-(L-1)^3+27(N-A)\bigr)^2-4D_1^3.
\]
At \(D_1=0\) and \(L-1=-J\), this reduces to
\[
\Delta_2=\bigl(J^3+27(N-A)\bigr)^2\ge0.
\]
Therefore \(D_1=0\) and \(\Delta_2<0\) cannot occur. Moreover, \(\Delta_2=0\) holds exactly when
\[
N-A=-\frac{J^3}{27}.
\]
Combining this with \(D-E=J^2/3\) yields
\[
p(u)=u^3-Ju^2+\frac{J^2}3u-\frac{J^3}{27}=\left(u-\frac J3\right)^3.
\]
Because \(J>0\), the triple root \(J/3\) is positive. Conversely, if \(p\) has a triple root, comparison with \((u-r)^3\) forces \(r=J/3\), \(D-E=J^2/3\), and \(N-A=-J^3/27\), hence \(D_1=\Delta_2=0\). This proves the equivalence.

## Verification
The accompanying `verify.py` expands the factorization, differentiates the cubic symbolically, substitutes \(D_1=0\) into \(\Delta_2\), and checks both directions of the coefficient identities. It also verifies that \(Q\) is absent from the equilibrium cubic and its derivative. The check is exact symbolic algebra; no floating-point or finite-enumeration inference is used.

## Relationship to prior work
The 2026 source states the Case-3 cubic, its derivative, \(D_1\), and \(\Delta_2\), but Lemma 7(b) places the triple root under \(\Delta_2<0\) while the proof itself says that \(D_1=0\) implies \(\Delta_2\ge0\) and that the triple root occurs at \(\Delta_2=0\). The source also prints an Eq. (37) containing \(Q/B\), although \(Q\) is absent from the equilibrium polynomial. The exact locus above resolves both inconsistencies in one coefficient-level statement.

A closely related 2025 May–Holling–Tanner cooperation model studies a different reduced cubic and reports at most two positive equilibria for its analyzed parameter case. It does not give the Case-3 cubic, discriminant \(\Delta_2\), or the triple-root locus above.

## Limitations
This is a correction and completion of a specific equilibrium-multiplicity boundary. It does not establish that a generic one-parameter ecological path crosses the codimension-two triple-root locus, nor does it identify the local bifurcation normal form there. The biological admissibility assumptions are those of the source's dimensionless system; the result is algebraic and does not by itself prove stability or persistence.

## References
1. F. J. Reyes-Bahamón, A. D. Galindo-Leiva, J. C. Duarte-Vidal, et al., “Bistability and Periodicity in an Amended May–Holling–Tanner Model Involving Generalist Predators and Hunting Cooperation,” *Journal of Nonlinear Science* 36, 65 (2026). DOI: 10.1007/s00332-026-10272-w.
2. F. J. Reyes-Bahamón, C. A. Rodríguez-Cifuentes, E. González-Olivares, et al., “Hunting Cooperation: Its Impact in a modified May–Holling–Tanner model,” *Qualitative Theory of Dynamical Systems* 24, 111 (2025). DOI: 10.1007/s12346-025-01267-1.
