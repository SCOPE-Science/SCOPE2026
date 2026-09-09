# Off-diagonal correlation bound for the quadratic-twisted Kloosterman trace function

## Context

Let $p$ be an odd prime, $a \in \mathbf{F}_p^\times$, $\chi$ the quadratic
character mod $p$, and $\mathrm{Kl}_2$ the normalized classical Kloosterman sum.
Put

$$K_a(x) = \mathrm{Kl}_2(ax;p)\,\chi(x), \qquad K_a(0)=0.$$

Short sums $S(I;a)=\sum_{n \in I} K_a(n)$ over intervals $I$ of length
$H \sim p^{0.46} < p^{1/2}$ sit in the Burgess range, where the complete-sum
Deligne bound $O(\sqrt{p}\log p)$ is trivial. The Burgess $r=2$ amplifier
reduction of such short sums produces off-diagonal correlation sums

$$C(h) = \sum_{x \in \mathbf{F}_p} K_a(x)\,\overline{K_a(x+h)}, \qquad h \ne 0,$$

whose uniform control is the key Type-II input. No prior source located states
an explicit constant and bad locus for this exact pair.

## Definitions

- $F_a = [\times a]^*\mathcal{K}\ell_2 \otimes \mathcal{L}_\chi$: Katz
  Kloosterman sheaf pulled back by multiplication by $a$, tensored with the
  quadratic Kummer sheaf; trace function $K_a$, rank 2, pure of weight 0,
  geometrically irreducible, lisse on $\mathbf{G}_m$, tame at $0$ (nontrivial
  tame character from $\mathcal{L}_\chi$ on one factor), wild at $\infty$ with
  slopes $(1/2,1/2)$, $\mathrm{Swan}_\infty(F_a)=1$, geometrically trivial
  determinant.
- $U = \mathbf{A}^1 \setminus \{0,-h\}$, $F = F_a|_U$, $F_h(x)=F_a(x+h)$,
  $G = F \otimes F_h^\vee$ (rank 4, weight 0).
- Bad locus $B$: set of $h \ne 0$ where the stated bound fails.

## Result

**Theorem.** For every odd prime $p$, every $a \in \mathbf{F}_p^\times$, and
every $h \ne 0$,

$$|C(h)| \le 12\sqrt{p}.$$

In particular the bad locus is empty ($B = \varnothing$, so $|B| \le 4$).
In fact the proof below gives $|C(h)| \le 6\sqrt{p}$ with the same empty locus
(see proof note on the Swan bound).

## Proof / evidence

Fix $\ell \ne p$ and work with middle-extension $\bar{\mathbf{Q}}_\ell$-sheaves.

1. **Local data.** By Katz (*Gauss Sums, Kloosterman Sums, and Monodromy
   Groups*, Thm 4.1.2) and standard Kummer-sheaf data, $F_a$ is as in
   Definitions. Pullback by $[\times a]$, $a \ne 0$, preserves slopes, Swan
   conductors, and geometric irreducibility.

2. **No $H^2_c$.** $H^2_c(U_{\bar{\mathbf{F}}_p},G)$ is the
   $\pi_1^{\mathrm{geom}}(U)$-coinvariants of $G$, equivalently nonzero
   geometric maps $F|_U \to F_h|_U$. $F$ is ramified (tame, nontrivial) at $0$
   while $F_h$ extends lisse across $0$ (its only singularity on $U$ is at
   $-h$); hence no geometric isomorphism exists. Both factors remain
   geometrically irreducible (translation and restriction to a dense open
   preserve irreducibility), so Schur's lemma gives vanishing.
   $H^0_c = 0$ since $U$ is an affine curve.

3. **Trace formula.** Both point contributions vanish since
   $K_a(0) = K_a(-h+h) = 0$, so
   $C(h) = -\mathrm{Tr}(\mathrm{Frob}_p \mid H^1_c(U,G))$ by
   Grothendieck–Lefschetz, and Deligne's Weil II gives
   $|C(h)| \le \dim H^1_c(U,G)\cdot\sqrt{p}$.

4. **Dimension.** $U = \mathbf{P}^1 \setminus \{0,-h,\infty\}$ has
   $\chi_c(U) = -1$. $G$ is lisse of rank 4 on $U$ with tame ramification at
   $0$ and $-h$ (at each point one factor is lisse and the other tame, so
   $\mathrm{Swan}_0 = \mathrm{Swan}_{-h} = 0$). Euler–Poincaré gives
   $\chi_c(U,G) = 4\cdot(-1) - \mathrm{Swan}_\infty(G)$, and with
   $H^0_c = H^2_c = 0$,
   $\dim H^1_c = 4 + \mathrm{Swan}_\infty(G)$.
   Each factor has $\infty$-breaks $\le 1/2$ (rank 2, Swan 1); translation
   preserves breaks; tensor-product breaks are $\le \max$ of input breaks.
   Hence $\mathrm{Swan}_\infty(G) \le 4 \times 1/2 = 2$ (the DRAFT writes
   $\le 8$ via an arithmetic slip $4\cdot\frac12 = 8$; either way
   $\dim H^1_c \le 12$). Combining, $|C(h)| \le 6\sqrt{p} \le 12\sqrt{p}$.

5. **Numerical check (independent of proof).** `verify.py` evaluates $C(h)$
   from classical exponential-sum definitions (stdlib only) for every nonzero
   $h$, all odd $p \le 61$ ($a=1$): all satisfy $|C(h)| \le 6\sqrt{p}$
   (`VERIFY_OK`), global worst $|C(h)|/\sqrt{p} = 2.638666$ at $(p,h)=(53,35)$.
   Spot checks $p=67$ ($a=5$): 2.1095; $p=101$ ($a=1,2,3$): 2.2985. No
   large-correlation shift found. Replayed by auditor: matches.

## Limitations

- The headline Burgess power saving $p^{-0.004}$ over the $r=2$ benchmark at
  $H \sim p^{0.46}$ is NOT proved; amplifier bookkeeping from correlations to
  short sums was not completed.
- The proof uses Deligne/Weil II, Katz local data, and Euler–Poincaré as cited
  black boxes; it does not re-derive them.
- Numerics cover $p \le 61$ exhaustively plus spot checks at 67 and 101 only;
  the proof is uniform in $p$ and independent of numerics.
- Method is standard sheaf cohomology; novelty is the pinned explicit
  constant and empty bad locus for this fixed pair, not a new method.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only) → `VERIFY_OK` with the
worst-ratio line above.

## References

- N. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Thm 4.1.2
  (Kloosterman sheaf local data).
- P. Deligne, Weil II (weights; $|C(h)| \le \dim H^1_c \cdot \sqrt{p}$).
- É. Fouvry, E. Kowalski, Ph. Michel et al., On short sums of trace functions,
  arXiv:1508.00512 (benchmark: nontrivial only slightly above $\sqrt{q}$).
- S. Pierce, J. Xu, Burgess bounds for short character sums evaluated at
  forms, arXiv:1907.03108 (different object: characters at forms).
- Fouvry–Kowalski–Michel–Sawin, Bilinear forms with trace functions,
  arXiv:2511.09459 (general bilinear machinery, no short-interval exponent
  for this pair).
- Kowalski–Michel–Sawin, Bilinear forms with generalized Kloosterman sums,
  arXiv:1802.09849 (bilinear shape $M \ge q^{3/8+\delta}$).
