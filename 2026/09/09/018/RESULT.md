# Dual-verified max-insertion-site profile census for Av(1324,1342) to length 12, with Av(1324) / Av(1342) profiles dual-verified to length 11

## Context
Av(1324) is the notorious unsolved length-4 pattern-avoidance enumeration problem; Av(1342) is its algebraically solved counterpart (Bona 1997, algebraic generating function). The joint class Av(1324,1342) is the large-Schröder class with closed generating function $-x/2+3/2-\\sqrt{x^2-6x+1}/2$. Marginal counts through length 12 and far beyond are prior (OEIS A061552, A022558; PermPAL record 0213_0231). What was not recorded is the bivariate refinement by active max-insertion-site count, the canonical insertion-encoding / generating-tree statistic, with a replayable two-engine certificate.

## Definitions
For $\\pi\\in S_m$, gap $g\\in\\{0,\\dots,m\\}$ is *active* if inserting the new maximum $m+1$ at position $g$ stays in the class $C$. $k(\\pi)$ = number of active gaps. Every $\\sigma\\in C_{m+1}$ has a unique parent (delete its maximum), so the classes form max-insertion trees. Profile: $a_C(n,k)=\\#\\{\\pi\\in C,|\\pi|=n,k(\\pi)=k\\}$. Transfer matrix: $T_m(k\\to j)$ = number of parent-to-child transitions from site-count $k$ at length $m$ to $j$ at length $m+1$. Length convention here: permutation length $n$; OEIS 1-indexed offset is $n+1$ (so OEIS n=7 value 513/512 = length 6 here).

## Result (headline)
For $C=\\mathrm{Av}(1324,1342)$ and every $0\\le n\\le 12$, $a_C(n,k)$ is:

- 0: {1:1}; 1: {2:1}; 2: {3:2}; 3: {2:1, 4:5}; 4: {2:4, 3:4, 5:14}
- 5: {2:16, 3:18, 4:14, 6:42} (sum 90)
- 6: {2:68, 3:78, 4:68, 5:48, 7:132} (sum 394)
- 7: {2:304, 3:350, 4:312, 5:246, 6:165, 8:429} (sum 1806)
- 8: {2:1412, 3:1626, 4:1460, 5:1178, 6:880, 7:572, 9:1430} (sum 8558)
- 9: {2:6752, 3:7770, 4:7000, 5:5698, 6:4356, 7:3146, 8:2002, 10:4862} (sum 41586)
- 10: {2:33028, 3:37974, 4:34276, 5:28038, 6:21640, 7:15990, 8:11284, 9:7072, 11:16796} (sum 206098)
- 11: {2:164512, 3:188982, 4:170792, 5:140174, 6:108812, 7:81198, 8:58604, 9:40664, 10:25194, 12:58786} (sum 1037718)
- 12: {2:831620, 3:954546, 4:863444, 5:710418, 6:553760, 7:415802, 8:303100, 9:215016, 10:147288, 11:90440, 13:208012} (sum 5293446)

Full transfer matrices $T_m$ for $m\\le 11$ (277 cells) are in `artifacts/A_joint12_trans.csv`. The table is certified by two fully independent programs with byte-identical profiles (68 cells) and transfer files (277 cells), transfer identities, and external marginal match (large-Schröder 5293446).

Companion certified data: Av(1324) and Av(1342) profiles dual-verified cell-identical to length 11 (55 cells each class + transfers), extended to length 12 single-engine with exact OEIS b-file marginal pinning (1324 length-12 sum 25431452 = A061552; 1342 length-12 sum 22214707 = A022558). Profiles separate the two singles already at length 5 (1324: 11,22,28,42 vs 1342: 12,21,28,42 across k=3..6). Full rows are in `artifacts/A_1324_12_prof.csv` and `artifacts/A_1342_12_prof.csv`.

Classical 513-vs-512 separation at length 6 is used only as an audit anchor, not claimed as discovery. No growth-rate, rationality, or bijection theorem is claimed; Stanley–Wilf rows are descriptive residuals.

## Proof / evidence
Two independent C engines grow the max-insertion tree: Engine A (`enumA.c`, specialized incremental tests — 1324 forbidden iff prefix before gap contains a 132 triple since new max plays pattern-role 4; 1342 forbidden iff exists i1<i2<g<=i3 with p[i1]<p[i3]<p[i2] since new max plays pattern-role 3) and Engine B2 (`enumB2.c`, localized brute force — every new occurrence must use insertion position g because deleting g recovers the avoiding parent; all index triples from remaining positions tested with ranks recomputed per quadruple; no shared lemma/code path). `verify.py` enforces transfer identities $\\sum_j T_m(k\\to j)=k\\cdot a(m,k)$ and $\\sum_k T_m(k\\to j)=a(m+1,j)$ for $m\\le 11$ all classes, anchor checks, and A-vs-B2 agreement; committed log reports ALL-OK. Audit recompiled both engines and independently reran joint to n=8 (PROF-SAME, TRANS-SAME), Av(1324) to n=9/10, Av(1342) to n=9 (agreement), rechecked all transfer identities in independent Python (0 failures), and confirmed live external marginals (OEIS b-files; PermPAL raw sequence).

## Limitations
Single-class length-12 profiles rest on one engine + OEIS marginal pinning, not completed dual-engine agreement (Av(1342) B2-12 still running at freeze; Av(1324) B2-12 not started); cite those two rows with that qualification. Scope is exactly the three named classes and max-insertion-site statistic. Indexing: DRAFT length n = OEIS index n+1; stated explicitly on every row.

## Reproducibility
Stdlib-only: `gcc -O2 -o enumA enumA.c && gcc -O2 -o enumB2 enumB2.c && ./enumA joint 12 <prefix>` (Engine A ≈ 4–12 s/class; B2 joint-12 ≈ 5 min; singles B2-11 ≈ 1–3 min) then `python3 verify.py`. Artifacts: enumA.c, enumB2.c, verify.py, *_prof.csv, *_trans.csv, verify_A12_Cjoint12.log.

## References
OEIS A061552 b-file (1324-avoiding marginals); OEIS A022558 b-file (1342-avoiding marginals); Bona, Exact enumeration of 1342-avoiding permutations (1997), arxiv:math/9702223; Conway–Guttmann–Zinn-Justin, 1324-avoiding permutations revisited (2017), arxiv:1709.01248; Bevan, Permutations avoiding 1324 and patterns in Lukasiewicz paths (2015), arxiv:1406.2890; PermPAL Database Av(1324,1342) record and raw data 21 (GF, recurrence, specifications; joint marginals).
