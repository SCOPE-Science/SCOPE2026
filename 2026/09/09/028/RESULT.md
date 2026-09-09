# No uniform mod-49 lift of the d_4 mod-7 tower base at step 343

## Context

Let $d_k(n)$ count partitions from $k$-elongated plane partition diamonds
(Andrews-Paule), with generating function
$\\sum_n d_k(n)q^n = f_2^k/f_1^{3k+1}$ where
$f_m = (q^m;q^m)_\\infty$.
The prime-power tower program asks for infinite Ramanujan-type families
$d_k(A_r n+B_r) \\equiv 0 \\pmod{p^{r+1}}$.
At prime $7$, infinite towers are known for $d_3$ and $d_5$ (Chen-Xu-Yin),
while for $d_4$ only single-level mod-7 progressions
$d_4(343n+j) \\equiv 0 \\pmod 7$, $j \\in \\{39,235,284\\}$, are known
(Baruah-Das-Talukdar, Thm 6.1(6.8)).
The natural question is whether these lift diagonally to mod $49$ at the
same step $343$. This record certifies the negative answer everywhere.

## Definitions

$d_4(n)$ is defined by
$$\\sum_{n\\ge 0} d_4(n)q^n = \\frac{(q^2;q^2)_\\infty^4}{(q;q)_\\infty^{13}}.$$

## Result

**Theorem.** Let $d_4(n)$ be as above.

- (a) For each $j \\in \\{39,235,284\\}$, the progression $343n+j$ does
  **not** vanish identically mod $49$. Minimal witnesses:
  $d_4(39) \\equiv 14 \\pmod{49}$;
  $d_4(235) \\equiv 21 \\pmod{49}$;
  $d_4(970) \\equiv 14 \\pmod{49}$
  (and $d_4(284), d_4(627) \\equiv 0 \\pmod{49}$, so the $j=284$ witness
  needs depth $n=970$).
- (b) No residue class modulo $343$ vanishes identically mod $49$:
  for every $B \\in \\{0,\\dots,342\\}$ there is $n \\equiv B \\pmod{343}$
  with $n \\le 970$ and $d_4(n) \\not\\equiv 0 \\pmod{49}$.
  All $343$ witnesses are minimal in their class.
- (c) No residue class modulo $49$ vanishes identically mod $49$:
  for every $B \\in \\{0,\\dots,48\\}$ there is $n \\equiv B \\pmod{49}$
  with $n \\le 72$ and $d_4(n) \\not\\equiv 0 \\pmod{49}$.

Hence the diagonal mod-49 lift at step $343$ fails everywhere; any
$d_4$ mod-49 tower must use non-diagonal steps or residues.

## Proof / evidence

Exact integer series computation in stdlib Python: form
$A=(q;q)_\\infty$, $B=(q^2;q^2)_\\infty$ by naive products to order $N$,
$B^4$ and $P=A^{13}$ by truncated convolution, solve $D \\cdot P = B^4$
by series division ($P_0=1$). Spot values
$D_0,\\dots,D_4 = 1,13,100,585,2862$ and the identity $D\\cdot P=B^4$
hold exactly through truncation. Witness congruences are read directly
off the exact integers $D_n$.

The verifier (`output/artifacts/verify.py`, stdlib only) independently
re-derives $D_0,\\dots,D_{1000}$, asserts the $D\\cdot P=B^4$ identity and
stored-series agreement, rechecks all $343$ witness rows, and re-runs the
$343$-class scan. It prints
`VERIFY_OK N=1000 rows=343 identity=D*P=B4 spot=D[:5]=[1, 13, 100, 585, 2862]`.
Witness data: `witness_table.json` (343 rows, max $n=970$),
`witness_table49.json` (49 rows, max $n=72$),
`d4_series.json` (logged $d_4$ series to $2500$).
Replay: `python3 output/artifacts/verify.py` (~60-120 s).

Reproduction check (finite window, not claimed as new): on
$0 \\le n \\le 2500$, $d_4(343n+j) \\equiv 0 \\pmod 7$ holds for all
terms with $j \\in \\{39,235,284\\}$ (8, 7, 7 terms), and these are the
only residues mod $343$ with this property — consistent with
Baruah-Das-Talukdar Thm 6.1(6.8).

## Limitations

- One witness per mod-343 class refutes lifts of step exactly $343$ to
  mod $49$; it does not rule out finer steps. E.g. within $343n+284$,
  $n=1754$ has $d_4 \\equiv 0 \\pmod{49}$, so $2401$-step subprogression
  questions are left open (each $2401$-class has $\\le 2$ terms in the
  window — no conclusion drawn).
- The mod-7 singles are reproduced only on the $0$..$2500$ window
  (credited to Baruah-Das-Talukdar, not claimed); the infinite mod-7
  theorem is prior work. Residue uniqueness is window-sensitive
  (at $N=1000$ residue $23$ is also all-$0$ mod $7$).
- No infinite tower and no $U_7$ recurrence are proved here.
- No conclusion beyond mod $49$ or beyond the $n=1000$/$2500$ windows.

## Reproducibility

```
python3 output/artifacts/verify.py
```

Expected: `VERIFY_OK N=1000 rows=343 identity=D*P=B4 spot=D[:5]=[1, 13, 100, 585, 2862]`
(stdlib only, ~60-120 s).

## References

- Baruah, Das, Talukdar, Congruences for $k$-elongated plane partition diamonds, arXiv:2207.06264 (Thm 6.1(6.8): $d_4(343n+j)\\equiv0\\pmod7$, $j\\in\\{39,235,284\\}'; mod-49 (6.7) is for $d_3$ only).
- Chen, Xu, Yin, Congruences modulo powers of $7$ for $k$-elongated plane partitions, arXiv:2508.09723 (infinite 7-power towers for $d_3$, $d_5$ only).
- da Silva, Hirschhorn, Sellers, Elementary Proofs of Infinitely Many Congruences for $k$-Elongated Partition Diamonds, arXiv:2112.06328.
- Guadalupe, The $k$-elongated plane partition function modulo small powers of $5$, arXiv:2504.08627.
