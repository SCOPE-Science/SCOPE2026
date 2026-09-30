# Independent Audit — Strictly singular derivations on C*-algebras are compact

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `f39dc2741ff23991a67a3de0b3623043972245ff`  
**Audited current source tree:** `f39dc2741ff23991a67a3de0b3623043972245ff`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment snapshot. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Strict singularity excludes fixing a copy of c0, hence makes the derivation unconditionally converging; Pfitzner's property (V) for C*-algebras then makes it weakly compact. Akemann–Wright's structure theorem represents every weakly compact derivation as ad d for d in a c0-direct sum of pairwise orthogonal elementary ideals K(H_n). If such a derivation is noncompact, some nonzero component k acts on an infinite-dimensional H. Choosing y with ||k*y||=a>0 and an infinite-dimensional subspace M0 on which ||k||<a/2 gives ||[k,theta_{x,y}]||>=a||x||/2. The resulting rank-one column is Hilbertian and 1-complemented. Thus every weakly compact noncompact derivation fails strict singularity, proving compact=FSS=SS. The two witness alternatives follow from the same two cases.

## Originality — PASSED

PASS, narrowly scoped. Akemann–Wright determine compact and weakly compact derivations, and Pfitzner/Krulišová supply property (V); those are prior inputs. Targeted searches of derivation, commutator, multiplication, and strictly-singular literature did not locate the submitted collapse or the c0-versus-complemented-l2 witness dichotomy. The contribution is the short derivation-specific synthesis plus the explicit rank-one Hilbert witness, not any of the underlying structure theorems.

## Scientific value — PASSED

PASS. Strictly singular operators are usually much more numerous than compact operators, so their collapse on the derivation subspace of every C*-algebra is a meaningful rigidity statement. The geometric dichotomy also gives a concrete reason every noncompact derivation fails strict singularity and strengthens the bare equivalence.

## Independent checks

- Verified the property-(V) implication against Krulišová's open paper, which explicitly states Pfitzner's theorem for all C*-algebras.
- Checked the Akemann–Wright weakly compact derivation structure against the publicly accessible 1979 paper and later summaries.
- Reconstructed the compact-component argument: if all infinite-dimensional components vanish, truncations give finite-rank derivations converging in norm.
- Re-derived the rank-one commutator lower bound and the norm-one projection onto the witness Hilbert subspace.
- Searched current literature and the SCOPE repository for an exact compact/FSS/SS derivation collapse; no duplicate was located.
- Verified the current main tree SHA exactly equals the assigned source-tree SHA; the dated audit pair is absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- Akemann–Wright and property (V) are essential prior inputs and receive no novelty credit.
- Older derivation literature is extensive, so an unadvertised equivalent corollary remains a residual risk.
- The theorem is for bounded derivations A→A on complex C*-algebras.

## Evidence and references

- https://msp.org/pjm/1979/85-2/pjm-v85-n2-p01-s.pdf
- https://arxiv.org/abs/1605.04900
- https://doi.org/10.4153/CJM-2005-050-7
- https://doi.org/10.1007/s11856-020-1985-0
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/strictly-singular-cstar-derivations-are-compact--021bd796d7e3

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
