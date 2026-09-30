# Independent Audit — Fixed-support exponent lattices and primitive density for weak Carmichael numbers

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `fcfc716652d81ba72c48cc867683fa7a913a3add`  
**Audited current source tree:** `fcfc716652d81ba72c48cc867683fa7a913a3add`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment inventory snapshot, so the audited source tree remains exactly the assigned tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. For an admissible fixed support S, the weak-Carmichael criterion (p_i-1)|(n-1) is exactly the kernel condition Psi_S(e)=1, because every other support prime is a unit modulo p_i-1. Thus the exponent set is the positive part of a full-rank finite-index lattice. Unique factorization shows n(e)=m^f with m weak Carmichael iff e/f is an integral positive vector in the same kernel, i.e. e lies in f Lambda_S; in lattice-basis coordinates this is exactly gcd(c_1,...,c_s)>1. Standard fixed-lattice simplex counting gives the W_S main term, and Möbius inversion over lattice content gives the 1/zeta(s) primitive density with the stated boundary-error sums. I independently enumerated bounded exponent grids for S={3,5} and S={3,11,17}; in particular (2,2,6) is weak Carmichael and lattice-primitive while (1,1,3) is not weak Carmichael.

## Originality — PASS

PASS, strengthened by resolving the package's main source-access residual. Wong's 1997 thesis was lawfully obtained in full text this run and its relevant p.17 proposition was visually inspected: it gives the normal-support obstruction and a sufficient rectangular family with exponents divisible by r_i=lcm_{j!=i} phi(p_j), but it does not give the exact kernel lattice, lattice-primitivity criterion, fixed-support asymptotic, or 1/zeta(s) density. Meštrović (2013) supplies the weak-Carmichael criterion, primitive definition, and exact two-prime divisibility criterion. Targeted searches found no arbitrary-support kernel-lattice/density theorem. Those prior support and two-prime results receive no novelty credit.

## Scientific value — PASS

PASS. The kernel-lattice formulation gives a canonical exact model for every fixed admissible support, explains why ordinary exponent gcd can fail to detect primitive weak Carmichael numbers, and yields a universal primitive proportion depending only on support size. The result is a meaningful structural and asymptotic synthesis while making no claim about varying-support global counts.

## Independent checks

- Re-derived the Borwein--Wong/Meštrović congruence criterion as the kernel of Psi_S and checked admissibility is exactly what makes all residue coordinates units.
- Reproved lattice primitiveness from unique factorization and checked basis-coordinate gcd invariance.
- Recomputed bounded weak/primitive exponent examples independently for S=(3,5) and S=(3,11,17); the submitted square-but-primitive example behaved exactly as claimed.
- Rechecked the simplex covolume main term and the Möbius-inversion error sums: O(L log L) for s=2 and O(L^{s-1}) for s>=3.
- Read Wong's 1997 thesis openly from Library and Archives Canada and screenshot-inspected the relevant pseudo-Carmichael proposition; it is a sufficient exponent-multiple construction, not the exact lattice/density result.
- Compared with Meštrović's full accessible 2013 text, including Definition 2.25 and Proposition 2.36, which supply the prior primitive definition and two-prime exponent criterion.
- Inspected the package's exact-grid verification output (2,184 vectors, 508 weak, 363 primitive, zero reported mismatches) but did not use it as a substitute for the proof audit.
- GitHub compare reports no changed files under the assigned path from inventory to current main; the tree and verification guard remain unchanged.

## Limitations

- The asymptotic keeps the prime support fixed; it does not address support growth or global weak-Carmichael counting.
- Implicit error constants depend on the support.
- The lattice-point and primitive-vector density machinery is classical; novelty is only its exact weak-Carmichael application and synthesis.

## Evidence and references

- https://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp04/mq24272.pdf
- https://doi.org/10.1090/crmp/011/02
- https://arxiv.org/abs/1305.1867
- https://oeis.org/A225498
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/weak-carmichael-fixed-support-lattice-density--301b67b881e5

This guarded change set changes only the independent-audit channel in `VERIFICATION.md`; the Lean-verification and expert-attestation channels remain exactly as previously recorded.
