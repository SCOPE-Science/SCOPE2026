# One-step real relative Caporaso–Harris recursion off the F2 (−2)-section: signed count 8 vs complex 12 for profile (2)_moving in class E+4F

## Context

The Hirzebruch surface F2 = P(O ⊕ O(2)) is distinguished from F0 and the plane by its rigid (−2)-section E with E² = −2. Let B denote the disjoint section in class E+2F, with B² = +2, and F the fibre class. Relative enumerative geometry of the pair (F2, B+E) governs how rational curves meet these sections. Complex relative Caporaso–Harris recursions (Caporaso–Harris, Vakil degeneration, Cooper Fock-space operators, Cavalieri–Johnson–Markwig–Ranganathan floor-diagram correspondence) compute complex Severi and Gromov–Witten numbers but prescribe no real signs at section contacts. Real analogues exist for toric Del Pezzo surfaces (Itenberg–Kharlamov–Shustin) and for quantum-index refined counts with boundary point conditions (Blomme), but no Welschinger-signed relative step off the F2 (−2)-section with an explicit tangency-distribution rule was recorded. This gap blocks real degeneration arguments along E.

## Definitions

Work in genus 0 with primary insertions (no ψ-classes). Fix curve class β = E+4F = B+2F, i.e. B-basis (a,b) = (1,2), so β·B = 4 and β·E = 2. Impose the transverse fixed profile (1⁴) on B: four distinct fixed left ends of weight 1. On E (right side) consider total weight 2 with five profiles: A fixed (2), B fixed (1,1), C moving (2), D moving (1,1), E mixed (1 fixed + 1 moving).

Use CJMR floor-diagram conventions: connected loop-free graphs on an ordered vertex set with one white vertex of size s = 1 (all others black of size 0); divergence −k·s = −2 at white and 0 at black for k = 2; thickening rules for primary invariants (white 0 thick flags; black exactly 2; each compact edge exactly one thick side); fixed ends normal, moving ends thick. Complex multiplicity mult_C(D) = ∏ w(e) over compact edges (rational primary vertex factors equal 1 for size ≤ 1 floors). Refined multiplicity mult_q(D) = ∏ [w(e)]_q with [m]_q = (q^{m/2}−q^{−m/2})/(q^{1/2}−q^{−1/2}). Signed (tropical Welschinger) multiplicity mult_R(D) = mult_q(D)|_{q=−1}: 0 if any w(e) even, else ∏ (−1)^{(w(e)−1)/2}.

## Result

THEOREM (fixed target profile C = moving (2) on E, vertex count n = n₂+1 = 2). The complex and signed floor-diagram counts are N_C^C = 12 and N_C^R = 8 over exactly 10 labelled diagrams, distributed by white position p ∈ {0,1} and compact-edge weight w ∈ {1,2} as:

- (p,w) = (0,1): 4 diagrams, complex 4, signed 4;
- (p,w) = (0,2): 1 diagram, complex 2, signed 0;
- (p,w) = (1,1): 4 diagrams, complex 4, signed 4;
- (p,w) = (1,2): 1 diagram, complex 2, signed 0.

Hence N_C^C = Σ N(p,w)·w and N_C^R = Σ N(p,w)·w* with w* = 0 for w even and w* = (−1)^{(w−1)/2}·w for w odd. The two even-weight diagrams contribute 2+2 = 4 to the complex count and 0 to the signed count; this 4 is exactly the real-versus-complex divergence, isolated in two explicit diagrams. The refined total 2q^{−1/2}+8+2q^{+1/2} = 8+2[2]_q interpolates the two (q=1 → 12, q=−1 → 8). This is a one-step real relative Caporaso–Harris recursion off E for the fixed tangency profile (2)_moving.

Supporting ledgers (not part of the theorem): A fixed (2): 1/1/1; B fixed (1,1): 1/1/1; D moving (1,1): 180 diagrams, 288 complex, 104 signed; E mixed: 22 diagrams, 30 complex, 14 signed (including a w=3 diagram contributing +3 complex but −1 signed, same parity mechanism).

## Proof / Evidence

Setup and dimension count: in B-basis β=(1,2), the relative formula n = n₂+2a+g−1 with g=0, a=1 gives n=2 for profile C (n₂=1 moving end): one white size-1 and one black size-0 vertex. The B-side contributes 4 fixed weight-1 ends; the E-side one moving weight-2 end on the black vertex (white takes no moving ends by thickening). The single compact edge has weight w ≥ 1; divergence equations give w = L₀−2 (white at 0) or w = 2−L₁ (white at 1) with total left weight 4, hence w ≤ 2 analytically.

Exhaustive enumeration: script enumerate_f2.py enumerates all labelled trees on the ordered vertex set, all compact-edge weights 1..8, all assignments of 4 distinct left ends and distinct right ends, and both thick sides for black–black edges, filtering by divergence and thickening. For C it leaves exactly 10 diagrams in the grouped subtotals above. Completeness is certified analytically (used weights ≤ 2 < cap 8) and computationally (max-used-weight check). Independent audit replay reproduced all five profile totals and the per-(p,w) grouping exactly, with all refined(q=1)=complex and refined(q=−1)=signed assertions passing.

Multiplicities: for rational primary size-≤1 floors the CJMR one-point vertex factor is 1, so mult_C = w, mult_q = [w]_q, mult_R = w*. Summation yields 12/8 with the stated splitting, which has the shape of a relative degeneration step: fixed-profile count equals the sum over splittings (p,w) of combinatorial labelled counts times section-contact factor w (complex) resp. w* (signed). The correction w ↦ w* is the new real content.

## Limitations

Proves only the fixed profile (2)_moving in class E+4F with B-side (1⁴), genus 0, primary insertions; no general-profile, higher-genus, or descendant recursion is claimed. Signed multiplicity is the tropical Welschinger sign via Block–Göttsche refinement at q=−1 for the standard real structure. Vertex factors = 1 justified only for the rational primary size-≤1 floors in this census. Profiles D and E are supporting data, not part of the theorem.

## Reproducibility

Run `python3 output/artifacts/enumerate_f2.py` from the lane root. Expected stdout: A_fix2 n=1 ndiag=1 complex=1 signed=1; B_fix11 n=1 ndiag=1 complex=1 signed=1; C_mov2 n=2 ndiag=10 complex=12 signed=8 refined={-0.5:2, 0.0:8, 0.5:2}; D_mov11 n=3 ndiag=180 complex=288 signed=104; E_mix11 n=2 ndiag=22 complex=30 signed=14; plus per-profile q=1/q=−1 check lines, all passing. Totals archived in output/artifacts/ledger.json.

## References

- R. Cavalieri, P. Johnson, H. Markwig, D. Ranganathan, Counting curves on Hirzebruch surfaces: tropical geometry and the Fock space, arXiv:1706.05401.
- Y. Cooper, Fock space approach to Severi degrees of Hirzebruch surfaces, Trans. AMS B 12 (2025).
- R. Vakil, Counting curves on Hirzebruch surfaces (thesis survey).
- F. Ardila, E. Brugallé, Double Gromov–Witten invariants of Hirzebruch surfaces are piecewise polynomial, IMRN 2017.
- I. Itenberg, V. Kharlamov, E. Shustin, Caporaso–Harris type formula for Welschinger invariants of real toric Del Pezzo surfaces, Comment. Math. Helv. 84 (2009).
- T. Blomme, Caporaso–Harris type formula for relative refined invariants, Ann. Inst. Fourier 75 (2025).
- Y. Ding, J. Hu, Refined floor diagrams relative to a conic and Caporaso–Harris type formula, J. London Math. Soc. 2026 / arXiv:2509.06004.
