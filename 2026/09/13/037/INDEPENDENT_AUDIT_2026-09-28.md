# Independent Audit — 2026/09/13/037

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `ee6874f88cab03942f0e89ec996ca3fb0aebaacb`  
**Disposition:** **PASSED**

## Correctness

**Verdict:** PASS  
The sharp bound W≥2 for multiplicity 5 and embedding dimension 3 is correct. The Kunz inequalities, atom tests, genus/conductor formulas, and sharp witness k=(1,1,2,2) corresponding to <5,6,7> with c=10, g=6, n=4, W=2 all check independently. The 96-subpiece reduction is exhaustive. Exact rational vertex enumeration gives 76 infeasible pieces, six nonexceptional real minima at least 11/5, and fourteen exceptional real minima in {4/5,6/5,8/5}. All exceptional cases with real minimum >1 already give integer W≥2; the only 4/5 pair has W=4s−2t−2 or W=−6s+8t, hence W is even, so positive W cannot be 1 and again W≥2. This closes the universal integer claim without relying on the bounded scans in audit_exceptional_integers.py / audit_subpiece_integers.py, which are corroborative rather than proofs beyond their scan bounds.

## Originality

**Verdict:** PASS  
Known results prove Wilf nonnegativity for embedding dimension 3, for 2e≥m, and for fixed multiplicity m≤18, but those theorems only imply W≥0. Searches in Wilf-number, Kunz-coordinate, Apéry, and the explicit <5,6,7> formulations found no theorem giving the stronger uniform minimum 2 for the full m=5,e=3 family. The sharp gap therefore is not implied by the broader prior theorems and is not a finite database lookup.

## Scientific value

**Verdict:** PASS  
The result strengthens a qualitative Wilf theorem to a sharp exact quantitative gap on an infinite natural class, with a concrete extremizer and a finite exact polyhedral certificate. That is a reusable refinement of the known W≥0 theory rather than a tiny numerical specialization.

## Evidence

- [Bruns–García-Sánchez–O’Neill–Wilburne, Wilf’s conjecture in fixed multiplicity](https://arxiv.org/abs/1903.04342): Proves Wilf’s inequality W≥0 for m≤18 using Kunz polyhedra, but not the stronger m=5,e=3 minimum W=2.
- [Sammartano, Numerical semigroups with large embedding dimension satisfy Wilf’s conjecture](https://arxiv.org/abs/1111.1863): Covers 2e≥m and therefore m=5,e=3 only at the nonnegativity level W≥0.

## Independent checks

- Independent bounded enumeration through large Kunz boxes found minimum W=2 at k=(1,1,2,2), consistent with the exact proof.
- Inspected the exact rational 96-piece verifier and independently closed all fourteen exceptional integer cases from their LP minima plus integrality/parity, without relying on finite scans.
- Current main directory tree SHA exactly equals the assigned tree SHA; no GitHub writes were made.

## Limitations

- The scripts audit_exceptional_integers.py and audit_subpiece_integers.py scan only bounded boxes; they should be treated as corroboration, not universal proofs.
- The universal claim is nevertheless closed by the exact LP minima plus integrality/parity as described in this audit.

## Repository action

This audit is a guarded change-set only. Source tree `ee6874f88cab03942f0e89ec996ca3fb0aebaacb` still matches current `main`; no GitHub write was performed by this audit.
