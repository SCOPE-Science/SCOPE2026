# Disproof of a Certified Second-Gap Opening Threshold for a Double-Cosine Hill Operator

## Context

Periodic Schrödinger (Hill) operators on the line have band-gap spectra whose gap edges are the periodic and antiperiodic eigenvalues on one period cell. For the one-frequency Mathieu potential all gaps are open (Ince), while for two-frequency cosine potentials gaps may close for special parameter relations (Ince, Magnus–Winkler, Djakov–Mityagin). The admitted target asked for a certified threshold statement: for the π-periodic double-mode potential u_a(x)=a(cos 2x+cos 4x), with second finite gap width w_2(a) above energy 0, the first amplitude reaching width 0.2, a_c=inf{a>0:w_2(a)≥0.2}, exists and lies in [0.5,1.5].

## Definitions

Let a>0, u_a(x)=a(cos 2x+cos 4x), and H_a=-d²/dx²+u_a on L²(R). By Floquet theory the spectrum is a union of bands [E_0,E_1],[E_2,E_3],… where {E_j} in nondecreasing order is the union with multiplicity of the π-periodic and π-antiperiodic eigenvalues on [0,π]. Closed gaps are degenerate pairs E_{2k+1}=E_{2k+2}. Let w_2(a) denote the length of the second finite open gap above E=0 and a_c=inf{a>0:w_2(a)≥0.2}.

## Result

Theorem: The threshold claim is false. At a=2/5<1/2, the first two finite gaps of H_a above E=0 are both open, and w_2(2/5)≥83/20−19/5=7/20=0.35≥0.2. Hence a_c≤2/5<1/2, contradicting a_c∈[0.5,1.5]. In particular w_2(a)<0.2 for all a<0.5 fails at a=2/5. No monotonicity or continuity of gap widths is used.

## Proof / Evidence

Parity split: V=a(cos2x+cos4x) is even, so each (anti)periodic eigenspace splits into even/odd sectors where min–max applies; ‖V‖≤2a=4/5 shifts each ordered sector eigenvalue by at most 4/5 from its free value. Free sector spectra: even-periodic cos2kx: 0,4,16,…; odd-periodic sin2kx: 4,16,…; even/odd-antiperiodic cos(2k+1)x, sin(2k+1)x: 1,9,25,….

Ritz upper bounds (exact trigonometric integrals at a=2/5): periodic ground ≤0 (trial 1); odd-periodic o_0≤4−a/2=19/5 (trial sin2x); even-periodic η=4+a/2=21/5 (trial cos2x); even-anti η=1+a/2=6/5 (trial cosx); odd-anti ≤1−a/2=4/5 (trial sinx).

Residuals: (H−η)cos2x has normalized variance ρ=a²=4/25; (H−η)cosx has ρ=(5/4)a²=1/5. A proved one-sided Temple lemma (eigen-expansion weight bound Σ_{≠*}w≤ρ/d² plus S+ estimate giving η−μ*≤ρd/(d²−ρ)) yields: even-periodic second eigenvalue μ_1≥21/5−68/1425=5917/1425≥83/20 with d=17/5; even-anti ground ν_0≥6/5−1/4=19/20 with d=1.

Ordering: E_0≤0<E_1 (all antiperiodic ≥1/5); antiperiodic pair τ_0∈[1/5,4/5], ν_0∈[19/20,9/5] with 4/5<19/20 so the first gap above 0 is open; periodic pair o_0≤19/5<83/20≤e_1 with next edges ≥76/5 (periodic) and ≥41/5 (antiperiodic). Thus globally E_1<E_2<E_3<E_4<E_5 with (E_3,E_4)=(o_0,e_1) the second gap above 0, of width ≥7/20. Every numerical inequality is exact rational arithmetic rechecked by output/artifacts/verify_disproof.py (all-Fractions, ALL PASS). A labeled non-rigorous float diagonalization (gap ≈0.418) is intuition only.

## Limitations

Single-point disproof at a=2/5; determines neither the exact a_c nor the full function w_2(a); no monotonicity/continuity claims. Bounds are deliberately crude; certified 0.35 is weaker than numerical ≈0.418. Floquet edge-ordering and min–max invoked as standard textbook theorems.

## Reproducibility

Run python3 output/artifacts/verify_disproof.py (integers/Fractions only): all rational equalities and inequalities PASS. Ritz integrals and residuals independently recomputable by hand trigonometric identities listed in the proof.

## References

Magnus–Winkler, Hill's Equation; Teschl, Mathematical Methods in Quantum Mechanics Ch. 5 (Floquet/min–max); Djakov–Mityagin, J. Approx. Theory 135 (2005) 70–104 (two-term Hill coexistence/asymptotics, background only); Luo, arXiv:2007.09575 (Whittaker–Hill asymptotics, background only); Volkmer, J. Comput. Appl. Math. 213 (2008) 488–500 (Ince polynomial bounds, background only); DLMF 28.31 (Whittaker–Hill/Ince definitions).
