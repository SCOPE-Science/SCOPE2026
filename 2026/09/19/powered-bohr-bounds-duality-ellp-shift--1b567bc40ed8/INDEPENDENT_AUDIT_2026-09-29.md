# Independent audit — Powered-Bohr upper bounds and duality for the ell_p shift calculus

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/powered-bohr-bounds-duality-ellp-shift--1b567bc40ed8`  
**Audited tree:** `d5559f6f7287f799e3efc82bff3862b2bb62b408`

## Disposition

**PASSED.** Correctness, originality on the stated boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The operator-theoretic argument is sound. For 1<=s<infinity, polynomial norms of the unilateral left and right shifts equal the bilateral convolution norm: compression gives one inequality and translating finitely supported bilateral vectors beyond the boundary gives the reverse. Banach adjoint duality therefore yields R_p=R_{p'} for 1<p<infinity. For q=min(p,p')<=2, Taylor truncations of phi_a(z)=(a-z)/(1-az), tested on e_N, give exactly a^q+(1-a^2)^q r^q/(1-a^q r^q)<=1 and hence the stated beta_q upper bound. Substituting a=2^{-1/2} simplifies to (2^{q/2}-1)^{1/q}; the endpoint identities R_1=R_infinity=1/3 and R_2=1 are standard coefficient/von-Neumann calculations. Expanding the explicit upper bound and Kania lower bound at q=2 gives the stated log 2/2 and log 3/2 first-order brackets with the correct inequality orientation.

## Originality

**PASS.** Kania supplies the left-shift setting and interpolation lower bound, while Kayumov–Ponnusamy supply the scalar powered-Bohr theorem. The audited contribution is the transfer of the powered-Bohr obstruction to this operator radius together with exact p<->p' symmetry, strictness off p=2, endpoint limits, and the linear Hilbert-point defect bounds. Repository searches over the relevant September 17–19 records found no earlier SCOPE record with this package, and targeted literature searches did not locate an older theorem determining these operator-radius consequences. The originality claim is appropriately narrow because older Matsaev/Toeplitz/convolution literature is broad.

## Scientific value

**PASS.** The result materially sharpens a lower-bound-only radius question: it identifies p=2 as the unique full-radius exponent, proves exact dual-exponent symmetry, connects the operator problem to a known scalar extremal radius, determines both non-Hilbert endpoint limits, and pins down the first-order scale of loss near p=2. These are coherent and reusable structural facts even though the exact interior value of R_p remains open.

## Independent checks

- Reproved unilateral-left/unilateral-right norm equality through the bilateral shift and finite-support translation.
- Re-derived the Möbius truncation inequality and algebraically simplified the a=2^{-1/2} bound.
- Checked endpoint norms and the q=min(p,p') reparameterization of Kania's lower bound.
- Expanded both two-sided bounds at q=2 and verified the constants and inequality directions.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18963 — Tomasz Kania, Spectral constants for algebraic numerical ranges; source for the canonical shift setting and interpolation lower estimate used as prior input.
- https://doi.org/10.5186/aasfm.2019.4416 — Kayumov–Ponnusamy, On a powered Bohr inequality, Ann. Acad. Sci. Fenn. Math. 44 (2019), 301–310; establishes the scalar powered Bohr radius for 1<p<2.
- https://arxiv.org/abs/1809.00157 — Open-access preprint version of the Kayumov–Ponnusamy powered Bohr result.

## Limitations

- The exact value of R_p for 1<p<infinity, p!=2, remains open; the audit does not infer equality with beta_q^{1/q}.
- Older Matsaev-type polynomial-calculus and analytic Toeplitz/convolution literature remains the main residual priority risk; no exact duplicate was found.
- The argument is specific to the canonical unilateral shift and its bilateral transference, not arbitrary contractions.

## Repository identity

The assigned source-tree SHA `d5559f6f7287f799e3efc82bff3862b2bb62b408` matched the current tree at the audited path after comparison at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`, source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`, and current `main`. GitHub was read only during this audit.
