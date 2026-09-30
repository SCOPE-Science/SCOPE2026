# Independent Audit — An effective criterion for Zumkeller numbers of the form 2^a p q

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `0e66ba1be414456a4fbfff0e8beeb1eb2c124429`  
**Audited current source tree:** `0e66ba1be414456a4fbfff0e8beeb1eb2c124429`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source tree. GitHub was used read-only, and the dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. For n=2^a p q and M=2^{a+1}-1, the excess (sigma(n)-2n)/2 simplifies exactly to D=[M(M+1)-(p-M)(q-M)]/2. When p>M and n is abundant, 0<=D<M^2<pq, so no divisor containing pq can enter a subset sum for D. The remaining proper divisors split into independent blocks 2^i, p2^i, q2^i; binary subsets of each block realize every coefficient x,y,z from 0 to M, giving the stated iff D=x+py+qz. If p<=M, the classical 2^a p criterion plus the coprime-prime product closure gives automatic Zumkeller status. The abundance inequality yields the finite bounds on u=p-M and v=q-M. Independent exact enumeration reproduces all displayed exceptional pairs for a=1,2,3,4, and exact divisor-subset dynamic programming had zero mismatches with the coefficient criterion on every finite candidate checked.

## Originality — PASS

PASS, narrowly scoped. Bhaskara Rao–Peng supply the foundational excess/subset-sum criterion and product closure. Mahanta–Saikia–Yaqubi completely characterize Zumkeller numbers with only two distinct prime factors and separately study k-layered 2^alpha p q families for k>=3; their public full article does not give the submitted classical Zumkeller (k=2) classification for the three-distinct-prime family 2^a p q. Later surfaced Zumkeller papers address other additive/generalized questions. The new content credited here is the explicit three-coefficient iff, fixed-a finite reduction, and exhaustive low-a exception tables, not the general divisor-partition machinery.

## Scientific value — PASS

PASS. The criterion converts an infinite three-prime divisor-partition family into a finite, transparent integer feasibility problem for every fixed binary exponent and yields complete low-exponent classifications. It is a useful next-step structural result beyond the known two-distinct-prime classification, with independently reproducible exact verification.

## Independent checks

- Re-derived the excess D algebra and proved the pq-containing divisor blocks are too large to participate when p>M.
- Reconstructed the independent binary-block representation x+py+qz with 0<=x,y,z<=M.
- Re-derived the fixed-a bounds u<sqrt(M(M+1)) and v<=floor(M(M+1)/u).
- Independently enumerated the entire bounded prime candidate region for a=1,2,3,4; the abundant non-Zumkeller exception lists exactly match the record.
- Independently ran exact divisor-subset-sum dynamic programming on all bounded candidate pairs for a<=4 and found zero disagreements with the coefficient criterion.
- Compared with the open Mahanta–Saikia–Yaqubi 2020 article, which characterizes two-distinct-prime Zumkeller numbers and discusses k-layered 2^alpha p q results rather than this k=2 three-prime criterion.
- GitHub current main has exactly the assigned directory tree SHA; the dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem treats a squarefree odd part pq; higher odd prime powers and four-or-more-prime families are not classified.
- For general a the result is an effective finite criterion rather than a closed-form exception list.
- Equivalent specializations of broad divisor-partition criteria under older terminology remain a residual risk; novelty is restricted to the exact formulation and classifications compared.

## Evidence and references

- https://arxiv.org/abs/0912.0052
- https://doi.org/10.1016/j.jnt.2020.05.003
- https://arxiv.org/abs/2310.14149
- https://oeis.org/A083207
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/zumkeller-two-odd-prime-effective-criterion--7e2e978c2daf

This guarded change set changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
