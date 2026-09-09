# First certified beyond-tables local-global exception block for the Coins Apollonian packing in (5e8, 5.2e8]

## Context

Let $P_C$ be the primitive integral Apollonian circle packing with root Descartes
quadruple $(-11,21,24,28)$. The thin-group local-global conjecture (Graham et
al.; Sarnak; Bourgain-Kontorovich) predicts that every sufficiently large
integer satisfying the packing's congruence obstructions occurs as a circle
curvature. For the Coins packing the threshold $X_{P_C}$ is unknown: Fuchs-Sanden
(arXiv:1001.1406) report violations above $10^8$ and completeness only to
$5\times 10^8$ (1e8-entry Matlab chunking over $[10^6,5\times10^8)$), while
Graham et al. (math/0009113) tabulate exceptions only below $10^6$. Density and
asymptotic theorems (Bourgain; Kontorovich-Oh, $N_P(x)\sim c_Px^\delta$ with
$\delta=1.30568\ldots$, $c_{P_C}=0.0176\ldots$) imply no exact finite list.

## Definitions

- Descartes equation: $(a+b+c+d)^2=2(a^2+b^2+c^2+d^2)$.
- Vieta move: for a quadruple with sum $s$, replacing entry $w$ by
  $w'=2(s-w)-w$ preserves the Descartes equation.
- Admissibility (used as stated, Fuchs-Sanden Lemma 3.3(ii)):
  $n$ is admissible for $P_C$ iff $n\bmod 24\in P_{C,24}=\{0,4,12,13,16,21\}$.
- Window: $\mathrm{LO}=500000000$, $\mathrm{BOUND}=520000000$;
  $(500000000,520000000]$ contains $20000000$ integers.
- Exception: an admissible integer in the window absent from the curvature
  orbit of $P_C$.

## Result

**Theorem (certified census).** For the Coins packing $P_C$ in
$(500000000,520000000]$:

- exactly $5000001$ integers are admissible;
- exactly $4999652$ distinct admissible integers occur as curvatures;
- exactly the $349$ integers listed in `artifacts/E_short_5e8_52e8.txt`
  (least $500004300$, greatest $519931204$) are admissible but absent.

Residue breakdown of the $349$ exceptions: $101$ in class 12, $101$ in class 0,
$74$ in class 4, $73$ in class 16, $0$ in classes 13 and 21.

## Proof / evidence (computational certification)

1. **Enumeration.** Depth-first Descartes-tree search from $(-11,21,24,28)$
   following all child moves $w'>w$ with $w'\le 520000000$, marking birth
   curvatures in $(\mathrm{LO},\mathrm{BOUND}]$ into a $2500000$-byte bitmap.
   Every visited quadruple passes an exact `__int128` Descartes check
   ($\mathrm{sum}^2=2\cdot\mathrm{sumsq}$; abort on failure).
2. **Triple recount.** Engine AB (iterative explicit-stack, incremental
   sum/sumsq) run twice with opposite child orders (ascending/descending,
   duplicate-position skipping) plus independent Engine C (recursive,
   descending, no dedup so shared subtrees are revisited). All three report
   $4219560868$ nodes, window popcount $4999652$, FNV-1a64 `73b4bb3c821b2bd3`,
   exit 0; the three bitmaps are byte-identical
   (sha256 `a3e7646a0a7a5230011c0f98b962f210d2dc5bc64df65a3192c4ba52f6cc12b6`).
3. **Completeness argument.** Every non-root orbit quadruple with all entries
   $\le\mathrm{BOUND}$ has a unique parent obtained by replacing its maximum by
   its smaller Vieta conjugate (strictly smaller maximum), so iterating reaches
   the root and the DFS visits every orbit quadruple with an entry
   $\le\mathrm{BOUND}$. An instrumented audit to $520000000$ confirmed the
   maximality premise over all $4219560868$ child births
   ($\mathrm{nonmax}=0$, $\mathrm{ties}=0$). Duplicate-position skipping in AB
   is guarded by Engine C with no dedup giving the identical bitmap.
4. **Admissibility diff.** The bitmap was diffed against $P_{C,24}$: admissible
   total $5000001$, present $4999652$, absent $349$. A residue audit over all
   $4999652$ marked values found $0$ outside $\{0,4,12,13,16,21\}$.
5. **Witnesses.** Positive witness: the least present window value $500000004$
   (mod 24 = 12) carries a logged 20-frame root-to-birth chain in
   `artifacts/chain_present_500000004.txt` ending in birth quadruple
   $(10295941,360255213,500000004,1103644)$, each frame Descartes-valid with
   consecutive frames single Vieta moves. A full-tree FIND scan for the least
   exception $500004300$ reports absence.
6. **Independent audit replay.** The auditor recompiled both C engines,
   reproduced AB-vs-C agreement on $(0,10^6]$, re-ran the full-bound
   enumeration to $520000000$ reproducing nodes/popcount/FNV/sha, and ran
   `artifacts/verify_short.py` (stdlib only) to `VERIFY_OK`.

## Limitations

- Admissibility uses the record-stated residue table $P_{C,24}$ as given; the
  table itself is not re-derived here.
- "Complete" means complete relative to the stated tree-completeness argument
  plus triple byte-agreement recount; it rests on the correctness of the two
  short C engines, mitigated by structural independence, identical node counts,
  per-node exact-integer verification, and the maximality audit.
- Claims apply strictly to $\mathrm{BOUND}=520000000$. The wider target window
  $(5\times10^8,6\times10^8]$ was not claimed.
- Bitmaps ($2.5$ MB each) are verification-critical but omitted from
  `output/artifacts/` for compactness; they are exactly reproducible by the
  two-line build-and-run recipe below (auditor-verified sha above).

## Reproducibility

```sh
gcc -O3 -o engAB output/artifacts/coins_engine_AB.c
gcc -O3 -o engC  output/artifacts/coins_engine_C.c
./engAB 500000000 520000000 0 bitmap_A.bin
./engAB 500000000 520000000 1 bitmap_B.bin
./engC  500000000 520000000 bitmap_C.bin
cmp bitmap_A.bin bitmap_B.bin && cmp bitmap_A.bin bitmap_C.bin
sha256sum bitmap_A.bin   # expect a3e7646a0a7a5230011c0f98b962f210d2dc5bc64df65a3192c4ba52f6cc12b6
python3 output/artifacts/verify_short.py   # expect VERIFY_OK (needs bitmaps beside it)
```

(`verify_short.py` expects the three bitmaps as `bitmap_shortA/B/C_5e8_52e8.bin`
alongside it; rename or regenerate accordingly. Artifact sha256:
`E_short_5e8_52e8.txt` `92e397da9b2924df36cb307c79c17a9afae570d39d7f0adcbe010a0ec3388b0f`.)

## References

- R. L. Graham, J. C. Lagarias, C. L. Mallows, A. R. Wilks, C. H. Yan,
  Apollonian Circle Packings: Number Theory. arXiv:math/0009113.
- E. Fuchs, K. Sanden, Some experiments with integral Apollonian circle
  packings. arXiv:1001.1406.
- J. Bourgain, Integral Apollonian circle packings and prime curvatures.
  arXiv:1105.5127.
- A. Kontorovich, H. Oh, Apollonian circle packings and closed horospheres on
  hyperbolic 3-manifolds. arXiv:0811.2236.
- A. Kontorovich, From Apollonius to Zaremba: local-global phenomena in thin
  orbits. arXiv:1208.5460.
