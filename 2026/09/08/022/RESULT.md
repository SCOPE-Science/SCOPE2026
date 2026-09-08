# Inversion-refined census of the exceptional triple {1324,1243,1432}: increase refuted, finite-window decrease certified, two safe shift-lemmas proved

## Context
Let B* = {1324,1243,1432}, the Callan–Mansour Case 237 exceptional triple: the one
triple containing 1324 for which no generating function is known (conjectured
intractable, arXiv:1705.00933). The 2012 Claesson–Jelínek–Steingrímsson
inversion-monotonicity conjecture links fixed-inversion distributions to a new upper
bound on the Stanley–Wilf limit of Av(1324); Claesson et al. (arXiv:2604.01143, 2026)
proved the first nontrivial inversion-monotone sets, characterized limit sequences,
and determined them only for pairs {1324,p}. No prior source treats the triple B* at
inversion-refined level; OEIS A257562 records only univariate totals for the
Wilf-symmetric representative {4123,4231,4312}.

## Definitions
- inv(pi) = number of inversions of pi.
- Av_n(B*) = permutations of {1..n} with no classical occurrence of any pattern in B*.
- av_n^k(B*) = |{pi in Av_n(B*): inv(pi)=k}|.
- Partition numbers p(0..8) = 1,1,2,3,5,7,11,15,22.

## Result
1. **Refutation of increase/stabilization.** The fixed-k increase
   av_8^k <= av_9^k <= av_10^k <= av_11^k is FALSE, as is stabilization
   av_10^k = av_11^k for k<=12. Counterexamples from the dual-verified table:
   av_8^6 = 15 > 11 = av_9^6; av_10^8 = 26 vs av_11^8 = 22.
   Hence no injection Av_8^6 -> Av_9^6 exists (cardinality).
2. **Obstruction mechanism.** Appending the new maximum at the right end
   (the inversion-preserving +0 map) is unsafe. Witness:
   pi = (1,3,4,5,6,7,8,2) in Av_8(B*); pi ++ (9,) contains six 1324-occurrences,
   e.g. positions (0,1,7,8) with values (1,3,2,9).
3. **First bivariate census (n=8..11).** Exact table by two independent enumerators
   in full cell-wise agreement; univariate totals 5150, 21517, 90921, 387595
   (matching OEIS A257562 values for the symmetric representative).
   Rows k=0..12: n=8: 1,1,2,3,5,7,15,21,30,48,74,104,152;
   n=9: 1,1,2,3,5,7,11,19,28,38,56,80,118;
   n=10: 1,1,2,3,5,7,11,15,26,36,50,70,97;
   n=11: 1,1,2,3,5,7,11,15,22,34,48,64,91.
   Extended k=13,14,15 rows: n=8: 199,259,333; n=9: 167,234,318;
   n=10: 133,189,255; n=11: 121,163,222. Full distributions in artifacts.
4. **Certified finite-window decrease (sharp).** For every k<=15:
   av_8^k(B*) >= av_9^k(B*) >= av_10^k(B*) >= av_11^k(B*).
   Sharp in-window: k=16 row (405,422,350,299) is non-monotone.
   Status: computed certificate on n=8..11; no general-n antitonicity proved.
5. **Two proved safe shift-lemmas.** g1(pi)=(n+1)++pi (prepend-max) and
   g2(pi)=(pi+1)++(1) (append-min) map Av_n(B*)->Av_{n+1}(B*) with
   inv shift exactly +n. Proofs: g1's new global maximum cannot be the rank-1
   first entry required by 1324/1243/1432; g2's new global minimum (rank 1)
   cannot be the required last entry (ranks 4,3,2). Machine-audited
   (avoidance, +n shift, injectivity, image subset of Av_{n+1}) on full sets.
   Corollary: av_n^k(B*) <= av_{n+1}^{k+n}(B*) for n=8,9,10.
6. **Partition agreement (empirical).** av_n^k(B*)=p(k) for k<=5 at all
   n=8..11 (1,1,2,3,5,7); at n=11 agreement extends through k=8 (11,15,22).
   Stated as computed data plus conjecture, not proved.

## Proof / evidence
- Enumerator A: left-to-right DFS with inversion tracking; prunes only partial
  perms already containing a forbidden quadruple (hereditary, hence safe).
- Enumerator B (independent): level-by-level extension by inserting the new
  maximum m into avoiders of size m-1, naive C(m,4) standardization check,
  no shared pruning lemma; complete because deleting the maximum preserves
  avoidance. A fast variant's starts-with-minimum pruning (all patterns start
  with rank 1; residual types {132,213,321}) reviewed and sound.
- Exact agreement A==B on every (n,k) cell for n=8..11; independent auditor
  brute-force re-enumeration with a naive checker: n=8 total 5150 with exact
  row match; n=9 total 21517 with FULL 37-cell distribution match; n=10 total
  90921 with k<=15 row match. n=11 rests on A==B==A2 agreement + OEIS match.
- Witness, shift-lemma proofs, and antitone inequalities re-checked by auditor
  (witness occurrences counted; shift maps verified on full brute n=8 set with
  subset-of-Av_9 confirmation; antitone recomputed with sharpness at k=16).

## Limitations
- Decrease certified only for n=8..11, k<=15 (computed certificate); no
  general-n antitonicity proof; no canonical deletion-side injection.
- n=11 not independently brute-forced by the auditor (39.9M raw perms).
- Partition agreement is data plus conjecture.
- OEIS univariate coincidence noted as sanity check, not a theorem.
- Witness minimality ordering not formally specified beyond existential unsafety.

## Reproducibility
- Tables: output/artifacts/distA_n*.json, distB_n*.json, distA2_n11.json,
  cert_antimonotone_k15.json.
- Programs (stdlib-only Python): enumA.py, enumB.py, enum_fast.py, inject.py,
  shift_lemmas_audit.py, verify_Astar.py, certify_monotone.py.
- Regenerate: `python3 enumA.py 8`, `python3 enumB.py 9`, etc.; compare JSON
  cell-wise; check antitone inequalities for k<=15 and failure at k=16.

## References
- D. Callan, T. Mansour, Enumeration of small Wilf classes avoiding 1324 and two
  other 4-letter patterns, arXiv:1705.00933.
- A. Claesson et al., Inversion monotonicity in subclasses of the 1324-avoiders,
  arXiv:2604.01143.
- C. Bean et al., Permutations avoiding bipartite POPs have a regular insertion
  encoding, arXiv:2312.07716.
- OEIS A257562 (avoids {4123,4231,4312}; b-file to n=5000).
