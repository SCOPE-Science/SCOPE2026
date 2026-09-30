# Independent audit — Exact parametrization of deficient-perfect numbers of the form 2^a p q

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/deficient-perfect-three-prime-squarefree-slice--3e91eb00b44d`  
**Assigned and audited tree:** `82cdba88049f74c1f677f506463923950e7f760c`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The claim survives independent review without a substantive research-file edit.

## Correctness

PASS. Re-deriving D(n)=2n-σ(n) gives D=pq-M(p+q+1)=(p-M)q-M(p+1), with M=2^(a+1)-1. Positivity forces p>M. Modulo q, D≡-M(p+1), and because M<p<q and p+1<q for distinct odd primes, q cannot divide D. Since D is a positive divisor of 2^a p q, the only cases are D=2^e or D=2^e p. In the first case s=p-M gives s(q-M)=M(M+1)+2^e; in the second p|(q+1), q+1=kp and ks=2^(a+1)+2^e. Both converses substitute back exactly. Independent enumeration for a=1,…,7 reproduces the record's counts 0,1,3,5,9,8,24 and its listed initial examples.

## Originality

PASS with a bounded-literature caveat. Tang–Ren–Li (2013) classify deficient-perfect numbers with at most two distinct prime factors, and Tang–Feng (2014) exclude odd deficient-perfect numbers with exactly three distinct prime divisors; neither statement covers the even squarefree-odd-part slice 2^a p q. Targeted searches for the two-family divisor parametrization, the exclusion q∤D, and synonymous formulations did not locate prior coverage, and a search of the SCOPE repository did not locate an obvious duplicate. Older literature under variant terminology remains a residual priority risk, so the conclusion is literature-bounded rather than absolute.

## Scientific value

PASS. The theorem converts an open-ended prime search in the first even three-prime squarefree slice into two finite divisor searches for each exponent a, proves the larger odd prime can never occur in the deficient divisor, and gives exact effective enumeration. This is a substantive structural refinement beyond tables of examples.

## Independent checks

- Reconstructed both necessity and sufficiency cases algebraically, including the q∤D step and the ordering condition s^2<A_e.
- Implemented the two parametrized families independently for a=1,…,7; the solution counts are 0,1,3,5,9,8,24 and include 884, 17176, 18632, and 18904 with the stated deficiencies.
- Checked current main-path tree identity against the assigned tree; all record blobs and the artifacts subtree match the assignment snapshot.

## Literature and evidence

- https://doi.org/10.4064/cm133-2-8 — Tang, Ren and Li (2013), prior classification with at most two distinct prime factors.
- https://doi.org/10.1017/S0004972714000082 — Tang and Feng (2014), exclusion of odd deficient-perfect numbers with exactly three distinct prime divisors.
- https://oeis.org/A271816 — Current deficient-perfect sequence data; useful for example cross-checking but not a proof of originality.

## Limitations

- The theorem assumes the odd part is squarefree and does not classify 2^a p^b q^c with b>1 or c>1.
- Originality remains bounded by searchable/indexed literature; an older equivalent statement under different terminology cannot be ruled out absolutely.
- The finite enumeration is corroborative only; the audit verdict rests on the symbolic proof.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `82cdba88049f74c1f677f506463923950e7f760c`. This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels remain byte-for-byte semantically identical to the pre-audit file.
