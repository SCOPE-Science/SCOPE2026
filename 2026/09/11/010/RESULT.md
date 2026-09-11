# Index–degree obstruction on the b2 = 2 intermediate cell (leg O of the Gauduchon–foliation shell dichotomy)

## Context
Minimal class VII surfaces with b2 > 0 (VII0+) are conjectured to be Kato (global spherical shell conjecture). Teleman proves a rational cycle exists at b2 = 2; Brunella proves b2 = 2 plus one singular foliation implies Kato, reducing GSS at b2 = 2 to foliation existence. What was missing is a test that does not assume a foliation: a Gauduchon pluripotential current with prescribed Lelong behavior along the Teleman cycle, transferred through foliation indices.

## Definitions
- S minimal VII0+, b2(S) = 2, Donaldson basis e0, e1 with ei·ej = −δij, c1(K) = e0 + e1. For [L] = (a0, a1): [L]^2 = −a0² − a1², K·L = −a0 − a1.
- Teleman cycle Γ in the cell ♯(Γ) − Γ² = 2 (intermediate branch; half-Inoue would give 2n = 4).
- Gauduchon metric g with vol_g(S) = 1, Lee class [θ] logged; vol_g(C) = ∫_C ω_g; V = Σ vol_g(Γi) > 0.
- Closed positive (1,1)-current T directed by a singular holomorphic foliation with generic Lelong number ν(T, Γi) ≥ 1 per component; deg_g(T) = ∫ T ∧ ω_g.
- CS(Γ) = Σ Γi² (sum of Camacho–Sad sums once invariance holds).

## Result
On this fixed cell, leg (O) holds with explicit gaps:
- (i) single nodal Γ = C, C² = −1: deg_g(T) ≥ V = CS(Γ) + δ, δ = V + 1 > 1 (uniform floor 1);
- (ii) two smooth Γ = D0 + D1, Dj² = −2, D0·D1 = 2, Γ² = 0: deg_g(T) ≥ V = CS(Γ) + δ, δ = V + 4 > 4 (uniform floor 4).
Hence deg_g(T) > 0 always: no shell-compatible directed current with deg ≤ 0 and no transfer identity deg = CS < 0 exist; (C) is excluded and (O) is established. Under the total-square reading CS = Γ², gaps are V + 1 > 1 and V > 0.

## Proof / evidence
1. Cell enumeration (Donaldson-exact): adjunction gives smooth rational ⇔ Σ ai(ai+1) = 2, nodal ⇔ Σ = 0. Nodal classes exactly (−1,−1), (−1,0), (0,−1), (0,0); smooth exactly the 8 with one entry in {1,−2}, other in {0,−1} (self-ints −1,−2,−4,−5). Negative-definiteness forces ♯ ≤ 2; hence (i) nodal C² = −1, [C] = (−1,0)/(0,−1); (ii) smooth D0·D1 = 2, D0² + D1² = −4 forcing −2,−2 with {[D0],[D1]} = {(−1,1),(1,−1)}, [Γ] = (0,0), Γ² = 0.
2. Foliation numerics (Lemma 3.15 analogue): Det(F) = 2 − Σ ai(ai+1), Tr(F) = −Σ ai². Empty singular locus impossible (Tr = 0 forces all ai = 0, then Det = 2). So Det ≥ 2 even, forcing Σ = 0: Det = 2 and [N_F] ∈ {(0,0),(−1,0),(0,−1),(−1,−1)}, Tr ∈ {0,−1,−1,−2}.
3. Automatic invariance (Lemma 3.31: non-invariant rational ⇒ N_F·C ≥ 2): N·C ∈ {0,−1} in (i), ±(a0−a1) ∈ {−1,0,1} in (ii), all < 2 — every Γ component invariant under every foliation. Camacho–Sad gives CS(Γ) = −1 in (i), −4 in (ii).
4. Degree gap (Siu + positivity): T = Σ νj[Dj] + R, νj ≥ 1 along Γ, R ≥ 0 closed, deg ≥ 0; so deg_g(T) ≥ V > 0; subtract CS. Vacuous if no directed T exists.
Integer combinatorics replayed by output/artifacts/verify_cell.py (ALL VERIFY_OK).

## Limitations
Decides the fixed b2 = 2 intermediate cell only. No shell construction; no statement for b2 ≥ 3; no claim if vol-1 normalization or Lee-class logging dropped. Metric-explicit δ via logged V; uniform floors 1 and 4. CS notation has sum-of-squares vs total-square readings (both stated). Universal (O) vacuous when no such directed T exists.

## Reproducibility
Run `python3 output/artifacts/verify_cell.py` → ALL VERIFY_OK. Inputs: Donaldson basis, vol-1 Gauduchon normalization, Lee class, Γ classes above.

## References
- Kurnosov–Spicer, Class VII surfaces with b2=3 and two foliations are Kato (Aug 2026), arXiv:2608.29047 — Lemmas 3.15/3.31, Donaldson bases, Dloussky criteria.
- Brunella, On a class of foliated non-Kählerian compact complex surfaces (Tohoku 2011) — b2=2 + foliation ⇒ Kato.
- Teleman, Donaldson theory on non-Kählerian surfaces (Invent. 2005) + cycle theorems — b2=2 cycle input.
- Dloussky Thm 4.2 (twisted log 1-form ⇒ Kato); Dloussky–Oeljeklaus–Toma (b2 curves ⇒ GSS); Apostolov–Dloussky (twisted currents/LCS).
