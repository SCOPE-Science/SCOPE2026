# Exact rational certificates for simultaneous Newton, Halley and Schröder failure on one quartic

## Finding

Consider the integer quartic
\[
Q(z)=395z^4-576z^3-33z+33.
\]
With Newton, Halley and Schröder/Chebyshev maps, respectively,
\[
N(z)=z-\frac{Q(z)}{Q'(z)},\qquad
H(z)=z-\frac{2Q(z)Q'(z)}{2Q'(z)^2-Q(z)Q''(z)},\qquad
S(z)=z-\frac{Q(z)}{Q'(z)}-\frac{Q(z)^2Q''(z)}{2Q'(z)^3},
\]
all three methods have a non-root attracting periodic orbit. Newton has a superattracting orbit of prime period two, Halley has a real attracting orbit of prime period two, and Schröder has a real attracting orbit of prime period three. Each attracting cycle has a nonempty open basin in the complex plane. Therefore no method has the property of root convergence for Lebesgue-almost every complex starting point.

The following rational interval data isolate the two additional attracting cycles. Write each interval as \(I_j=[c_j-r_j,c_j+r_j]\), with a listed decimal interpreted as an **exact rational number**.

| Map | Index | Exact center \(c_j\) | Exact radius \(r_j\) | Strict derivative bound \(L_j\) |
| --- | ---: | ---: | ---: | ---: |
| Halley | 0 | -0.099563100530747 | 1/10000 | 19/250 |
| Halley | 1 | -0.519387031162540 | 1/50000 | 7/5 |
| Schröder | 0 | 0.061148311552933 | 1/100000 | 11/1000 |
| Schröder | 1 | -0.691524324611230 | 1/5000000 | 4/5 |
| Schröder | 2 | -0.347921163893610 | 1/4000000 | 23/10 |

The certified multipliers satisfy
\[
|\mu_H|<\frac{133}{1250}=0.1064,\qquad
|\mu_S|<\frac{253}{12500}=0.02024.
\]
These are safe rational enclosures, not asserted optimal multiplier values.

## Assumptions and scope

All three iterations are rational maps defined where their displayed denominators do not vanish, and are regarded locally as complex holomorphic maps. The interval assertions concern real compact intervals; the open basins arise from complex local attraction. The theorem is for the stated degree-four polynomial only. No assertion is made that the three basins intersect or that every initial value fails.

The discriminant of \(Q\) is the nonzero integer \(-3350378794970691\), so the polynomial has four distinct complex roots.

## Proof

Direct exact substitution gives \(Q(0)=33\), \(Q(1)=-181\), \(N(0)=1\) and \(N(1)=0\). Also \(Q''(0)=0\), so \(N'(0)=Q(0)Q''(0)/Q'(0)^2=0\). This is an exact superattracting, root-free two-cycle.

For the other maps, let \(D(z)=2Q'(z)^2-Q(z)Q''(z)\). Exact polynomial differentiation and cancellation give
\[
H'(z)=\frac{48Q(z)^2U_H(z)}{D(z)^2},\qquad
S'(z)=\frac{12Q(z)^2U_S(z)}{Q'(z)^4},
\]
where
\[
U_H(z)=780125z^4-1137600z^3+497664z^2+13035z-4752,
\]
\[
U_S(z)=2184350z^4-3185280z^3+1244160z^2+13035z-4752.
\]
The polynomial-identity verification in the accompanying standalone checker reconstructs both derivatives directly by integer polynomial multiplication, not by trusting a symbolic simplifier.

On each of the five intervals in the table, exact inclusion interval arithmetic with rational endpoints proves: (a) \(Q\) never vanishes; (b) the corresponding map denominator \(D\) or \(Q'\) never vanishes; (c) the maximum derivative modulus is strictly less than the listed \(L_j\); and (d) the exact-center image discrepancy satisfies
\[
|F(c_j)-c_{j+1}|<10^{-12}
\]
with indices interpreted cyclically for the given map. These inequalities are exact rational comparisons, including the powers of ten.

The mean-value theorem therefore proves
\[
|F(x)-c_{j+1}|\le |F(c_j)-c_{j+1}|+L_j|x-c_j|<10^{-12}+L_jr_j<r_{j+1}
\]
for every \(x\in I_j\). The last strict inequality is checked using the table values (for instance, the tightest Schröder transition uses \(10^{-12}+(11/1000)(1/100000)<1/5000000\)). Consequently each interval maps into the **interior** of its successor.

The intervals within each orbit are pairwise disjoint, and the products of their derivative upper bounds satisfy
\[
\frac{19}{250}\frac75=\frac{133}{1250}<1,\qquad
\frac{11}{1000}\frac45\frac{23}{10}=\frac{253}{12500}<1.
\]
Thus \(H^2\) and \(S^3\) are strict contractions on the first respective intervals. Banach's fixed-point theorem yields one periodic point in the first interval; cycling it yields the remaining points. Disjointness forces exact prime periods two and three. Root/pole exclusion proves these are extraneous finite periodic cycles. The derivative products are strictly smaller than one, hence the holomorphic dynamics has a nonempty open attracting basin near each cycle. Therefore all three root-finding methods fail almost-everywhere root convergence on this quartic. Finally, the exact \(7\times7\) Sylvester determinant check verifies the quoted discriminant.

## Verification

Run `python3 verification/verify_q_cycles.py` using Python 3 and only its standard library. The checker uses `fractions.Fraction` interval arithmetic for all five enclosures; verifies strict center-error, derivative, inclusion, and pole/root inequalities; independently checks the two rational derivative identities by integer polynomial operations; and proves squarefreeness with an exact Bareiss determinant. It prints the marker `VERIFIED` on success. The approximate numerical derivative bounds printed for readability do **not** participate in any assertion.

## Relationship to prior work

Basti and Cremaschi, arXiv:2610.03246v1, Section 5, identify **this exact quartic**, its Newton cycle, and numerical evidence of the Halley two-cycle and Schröder three-cycle; they explicitly state that the rational interval certificates for this second example are not included. Their main theorem proves a different quartic's Newton–Halley failure. The present contribution supplies complete exact-rational certificates upgrading the announced numerical three-method example to a theorem. The quartic itself, the Newton cycle, the numerical locations, and the interval-contraction method are **not** claimed as new.

Collins and Hunter (2025) establish simultaneous three-method failures for degrees at least five; the degree-four situation is not covered by that stated result. This proof does not claim an independent new construction, a classification of degree-four dynamics, or any assertion on the unresolved cubic case.

## Limitations

The source publication already predicts the result numerically and explicitly suggests the style of certification. The added contribution is a complete reproducible exact proof for that natural omitted case, not a new algorithm or general convergence theorem. Historical priority beyond the inspected sources has not been independently certified; the full text of Collins and Hunter (2025) was not accessible for line-by-line comparison. An independent mathematical review has not been performed.

## References

1. Alessio Basti and Tommaso Cremaschi, *Simultaneous Global Convergence Failure of Newton's and Halley's Methods in Degree Four*, arXiv:2610.03246v1 (public October 2, 2026), especially Sections 2, 3, and 5 and Appendix A. https://arxiv.org/html/2610.03246v1
2. Jared Collins and Grant Hunter, *A family of polynomials that defy general convergence in three methods*, *Examples and Counterexamples* **8** (2025), 100191. https://doi.org/10.1016/j.exco.2025.100191
3. J. Milnor, *Dynamics in One Complex Variable*, third edition, Princeton University Press, 2006 (standard holomorphic attraction theory).
