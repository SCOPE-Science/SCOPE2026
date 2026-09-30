# Independent audit — Exact norm and essential-norm power profiles for irreducible weighted shifts

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/20/irreducible-weighted-shift-essential-power-profiles--d5ae263f185c`  
**Assigned and audited tree:** `8b079295a5ddc03c28ba58c9c74e36226d9da6d3`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review without a substantive research-file edit.

## Correctness

PASS. The recurrent-prefix construction is valid. Submultiplicativity makes the Wallen ratio weights bounded and gives every internal length-n product at most a_n; at each finite concatenation step only finitely many new crossing products contain the new positive bridge, so the bridge can be chosen small enough to preserve every bound. Repeating longer Wallen prefixes produces arbitrarily far-out length-n products equal to a_n, yielding both the operator norm and, via a weakly null sequence of basis vectors, the essential norm. Positivity of every weight gives irreducibility. For a_n=rho_n^n with rho_n positive and nonincreasing, submultiplicativity is immediate, and the ordinary/Calkin spectral-radius conclusions and non-power-compact Riesz consequence follow.

## Originality

PASS on the record's stated narrow boundary. The ordinary power-norm realization is classical Wallen/Halmos and is explicitly excluded. Targeted searches of weighted-shift power norms, essential norms/Calkin norms, submultiplicative profiles, irreducibility, and prescribed spectral-radius rates did not locate the simultaneous identity ||W^n||=||W^n||_e=a_n with the recurrent irreducible construction or its exact-rate essential-spectral-radius corollary. Because the strengthening is elementary once Wallen's ratio construction is known, older weighted-shift folklore remains a real residual priority risk; the verdict is not a broad first-discovery claim.

## Scientific value

PASS. The result upgrades a classical norm-profile theorem to simultaneous ordinary and essential power norms inside irreducible unilateral weighted shifts and turns arbitrary positive monotone convergence rates into exact spectral-radius and essential-spectral-radius rates. The quasinilpotent case supplies explicit irreducible Riesz shifts with no compact positive power, so the strengthening has clear operator-theoretic content beyond a cosmetic reformulation.

## Independent checks

- Reconstructed the bridge induction and verified that every newly created crossing product is controlled by choosing one positive bridge against finitely many constraints.
- Verified the essential-norm lower bound using repeated norming prefixes on an orthonormal weakly-null sequence and compactness of K e_j.
- Checked that the current main-path tree is unchanged from the assignment snapshot.

## Literature and evidence

- https://doi.org/10.1007/978-1-4684-9330-6 — Halmos, A Hilbert Space Problem Book, Solution 92: classical Wallen power-norm characterization.
- https://doi.org/10.1090/surv/013/02 — Shields (1974), classical weighted-shift survey and principal residual historical source.
- https://doi.org/10.1017/S0305004100057406 — Young (1980), arbitrary slowness context for the spectral-radius formula in Banach algebras.

## Limitations

- The ordinary power-norm characterization itself is classical and is not part of the originality claim.
- The historical search cannot exclude an equivalent simultaneous essential-norm observation under older weighted-shift terminology; Shields's long survey was not exhaustively reconstructed page by page in this audit.
- The exact-rate corollary assumes a positive nonincreasing sequence; it does not characterize arbitrary nonmonotone nth-root profiles.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `8b079295a5ddc03c28ba58c9c74e36226d9da6d3`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
