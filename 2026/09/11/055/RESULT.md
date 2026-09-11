# Slater-dual mod-18 product disproved at n = 3, with full mod-5 dissection log

## Context

Slater's list of Rogers-Ramanujan identities leaves duals of named Bailey
pairs unlisted; the McLaughlin-Sills-Zimmer survey flags such duals as gaps.
The admitted target tested one candidate dual: a mod-3-sensitive gap condition
against the triple product $(q^{18};q^{18})_\infty /
((q^2;q^{18})_\infty (q^7;q^{18})_\infty (q^{12};q^{18})_\infty)$ at level 18,
with prime 5 (smallest dissection prime not dividing the level) as the first
modularity test, and required either the product plus a $c(5n+4) \equiv 0$
family or a certified failing residue.

## Definitions

- $C(n)$: partitions $\lambda_1 \ge \lambda_2 \ge \cdots \ge 2$ of $n$ with
  $\lambda_i - \lambda_{i+1} \ge 2$, strengthened to $\ge 3$ whenever the larger
  part $\lambda_i \equiv 0 \pmod 3$; $C(0) = 1$ (empty partition).
- $P(q) = (q^{18};q^{18})_\infty /
  ((q^2;q^{18})_\infty (q^7;q^{18})_\infty (q^{12};q^{18})_\infty)$,
  with $[q^n]P$ its coefficients; $P(0) = 1$.
- $c(n) = C(n)$; the tested family is $c(5n+4) \equiv 0 \pmod 5$.

## Result

The conjectured identity $\sum_n C(n) q^n = P(q)$ (with any $q$-power
prefactor $q^a$, $0 \le a \le 10$) is **false**, already at $n = 3$:
$C(3) = 1 \ne 0 = [q^3]P$.
The congruence family fails at its first term: $C(4) = 1 \not\equiv 0
\pmod 5$. Every residue class $r \bmod 5$ carries a nonzero mod-5 coefficient
from its first term, so no progression vanishes identically.

## Proof / evidence

Hand proof at $n \le 4$ (the proof; machine data corroborate):
- $[3]$ is the only partition of 3 with parts $\ge 2$ and satisfies the gap
  condition vacuously, so $C(3) = 1$.
- Mod $q^{18}$, $P(q) = 1/(1-q^2) + O(q^7)$: only allowed part $\le 3$ is 2,
  and no partition of 3 uses parts $\{2,7,12\} \bmod 18$, so $[q^3]P = 0$.
- Both series have constant term 1, so any prefactor $q^a$, $a \ge 1$, fails
  at $n = 0$; $a = 0$ fails at $n = 3$.
- $[4]$ is the sole admissible partition of 4 ($[2,2]$ has gap $0 < 2$), so
  $C(4) = 1$, killing $c(5n+4) \equiv 0$ at $n = 0$.
- Corroborating machine expansion to $O(q^{80})$: $C$ by memoized DP
  cross-checked by brute-force partition generation to $n = 30$; $P$ by two
  opposite-order series constructions agreeing to $n = 80$; 77 mismatch
  indices in $0..80$, first at $n = 3$; no shift $a \in 0..10$ matches.
  First-nonzero mod-5 dissection entries: $r=0$: $(n,v) = (0,0,1)$;
  $r=1$: $(1,6,2)$; $r=2$: $(0,2,1)$; $r=3$: $(0,3,1)$; $r=4$: $(0,4,1)$.
  The $c(5n+4) \bmod 5$ row begins $1,3,3,4,1,2,4,0,\dots$.

## Limitations

Disproof concerns the stated residue set $\{2,7,12\} \bmod 18$ and its
mod-5 family only. It does not classify which corrected residue set (if any)
would close the dual-pair product, nor pursue the Bailey lift, which the
$n = 3$ obstruction renders moot for this residue set.

## Reproducibility

`python3 output/artifacts/verify.py` prints `VERIFY_OK` (stdlib only;
A1 == A2 to 30, B1 == B2 to 80, first mismatch $n = 3$ with $C = 1$, $P = 0$).
Full tables in `output/artifacts/verify_results.json`
(`C_dp`, `P`, `dissection_full_mod5`).

## References

- McLaughlin-Sills-Zimmer, Rogers-Ramanujan-Slater Type Identities (expanded
  Slater list survey), https://www.combinatorics.org/files/Surveys/ds15/ds15v1-2008.pdf
- McLaughlin, Ramanujan-Slater Type Identities Related to Moduli 18 and 24,
  https://www.wcupa.edu/sciences-mathematics/mathematics/jMcLaughlin/documents/RamSlatJuly25.pdf
- Rogers-Ramanujan-Slater Data Base, https://rrsdb.github.io/
- Bailey-lemma background (Lovejoy bilateral Bailey lecture),
  https://www.mat.univie.ac.at/~slc/wpapers/s87vortrag/Lovejoy1.pdf
