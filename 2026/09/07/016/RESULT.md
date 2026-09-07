# Cyclic Hadamard (51,25,12) Orbit Census: Multiplier-13 Nonexistence Certificate

## Statement

There is no cyclic $(51,25,12)$ difference set in $\\mathbb{Z}_{51}$.

Equivalently, among the $924$ multiplier-$13$-fixed $25$-subsets of $\\mathbb{Z}_{51}$ forced by orbit counting (contain $0$, exclude $17,34$, choose $6$ of $12$ four-orbits), none has each non-zero difference exactly $12$ times; equivalently none has ideal periodic autocorrelation $R(t)=-1$ for all $t\\ne 0$. The full $2772$-set fixed census (all three singleton choices) is also empty.

## Context

Hadamard difference sets have parameters $v=4n-1$, $k=2n-1$, $\\lambda=n-1$ and give binary sequences with ideal periodic autocorrelation. The triple $(51,25,12)$ with $n=13$ is the smallest composite Hadamard case in $v=41$--$73$ outside all three known infinite families: $51=3\\cdot 17$ is not prime (Paley), not a twin-prime product, and not $2^m-1$ (Singer). Counting $k(k-1)=600=\\lambda(v-1)$ and Bruck-Chowla-Ryser ($z^2=13x^2-12y^2$, solved by $1=13-12$) both pass, so elementary tests do not eliminate it.

Non-existence is already listed non-constructively in the Baumert-Gordon $k\\le 150$ existence table. The contribution certified here is **not** first knowledge of absence; it is the first explicit, rerunnable multiplier-$13$ union catalog with per-candidate spectra and replay scripts for this boundary triple.

## Definitions

Work in $\\mathbb{Z}_{51}$ additively. $D\\subset\\mathbb{Z}_{51}$, $|D|=25$, is a cyclic $(51,25,12)$ difference set if the multiset of $25\\cdot 24=600$ ordered differences $d_1-d_2$ ($d_1\\ne d_2$) contains each of the $50$ non-zero residues exactly $12$ times.

$m$ with $\\gcd(m,51)=1$ is a multiplier if $\\{md:d\\in D\\}=D+g$ for some $g$. A translate with $mD=D$ is $m$-fixed.

For $s_i=-1$ if $i\\in D$ else $+1$, $R(t)=\\sum_i s_i s_{i+t}$ and $N(t)=|D\\cap(D+t)|$ satisfy $R(t)=v-4k+4N(t)$. For $(51,25,12)$, $N(t)=12$ iff $R(t)=-1$ for all $t\\ne 0$.

## Result

- Multiplier $13$ partitions $\\mathbb{Z}_{51}$ into $3$ singletons $\\{0\\},\\{17\\},\\{34\\}$ and $12$ four-orbits:
  $\\{1,4,13,16\\}$, $\\{2,8,26,32\\}$, $\\{3,12,39,48\\}$, $\\{5,14,20,29\\}$, $\\{6,24,27,45\\}$, $\\{7,10,28,40\\}$, $\\{9,15,36,42\\}$, $\\{11,23,41,44\\}$, $\\{18,21,30,33\\}$, $\\{19,25,43,49\\}$, $\\{22,31,37,46\\}$, $\\{35,38,47,50\\}$.
- Any $13$-fixed $25$-set is one singleton plus six four-orbits ($1+6\\cdot 4=25$). Up to translation by $H=\\{0,17,34\\}$ it suffices to check the $\\binom{12}{6}=924$ unions containing $0$.
- $0$ of $924$ pass the difference test, cross-checked by autocorrelation. Max-deviation histogram: $2{:}48$, $3{:}96$, $4{:}558$, $5{:}80$, $6{:}36$, $7{:}40$, $8{:}36$, $9{:}16$, $10{:}8$, $12{:}6$. Global min count $7$, max $24$.
- Closest: combo $(0,1,2,3,8,9)$, block $\\{0,1,2,3,4,5,8,12,13,14,16,18,19,20,21,25,26,29,30,32,33,39,43,48,49\\}$, counts in $[10,14]$, maxdev $2$, $L_2=56$, $n_{\\rm bad}=20$. Furthest: combo $(0,2,3,8,10,11)$, counts in $[8,24]$, maxdev $12$, $L_2=744$, $n_{\\rm bad}=50$.
- Full $2772$ fixed census: $0$ pass, histogram $2{:}144$, $3{:}288$, $4{:}1674$, $5{:}240$, $6{:}108$, $7{:}120$, $8{:}108$, $9{:}48$, $10{:}24$, $12{:}18$.

## Proof / Evidence

*Proved (modulo cited multiplier theorem):* Prime $13$ divides $n=13$, $13>12$, $\\gcd(13,51)=1$, so by the First Multiplier Theorem (Beth-Jungnickel-Lenz Thm VI.2.5, used as black box) $13$ is a multiplier; some translate of any hypothetical set is $13$-fixed. Multiplication by $13$ has order $4$ (order $1$ mod $3$, order $4$ mod $17$ since $13^2=-1$), fixed set solving $12x=0$ gives $\\{0,17,34\\}$; $13^2x=x$ gives $15x=0$ so $17|x$, already fixed, hence no $2$-orbits and $48/4=12$ four-orbits. Size lemma $s+4t=25$, $s\\le 3$ forces $s=1$, $t=6$. $H$ is pointwise fixed ($13\\cdot 17=17$, $13\\cdot 34=34$), so $13(D+h)=D+h$ and $D-s$ normalises the singleton to $0$ while preserving the difference property. Thus existence implies a witness in $F_0$.

*Computed (replayable, doubly implemented):* Canonical lex enumeration of all $924$ unions via `itertools.combinations` (no RNG), $O(v^2)$ histogram per candidate plus independent autocorrelation loop; the two tests always agree. Independent cold verifier with separate `Counter` path, partition/closure/lex/fixedness checks, $H$-shift check, and group-ring spot check ($N_0=25$, $\\sum N=625$) reproduces $0/924$. Audit replay independently confirmed $0/924$ and $0/2772$, histogram, best/worst, SHA-16 `8a7eae3826de5c31`, and orbit table.

Hence no member of $F_0$ is a difference set; contrapositively no cyclic $(51,25,12)$ exists.

## Limitations

- Bare nonexistence was already table-listed by Baumert-Gordon; novelty is only the explicit rerunnable catalog and scripts.
- First Multiplier Theorem is cited, not reproved.
- Computation trusts deterministic Python integer arithmetic via two agreeing implementations, not a proof kernel; joint bug not formally excluded.
- Covers cyclic $\\mathbb{Z}_{51}$ only, not non-cyclic symmetric $(51,25,12)$ designs.
- No contracted $w=3,17$ $b$-vector analysis is needed; spectra subsume it.

## Reproducibility

Stdlib-only Python 3, ~0.4 s, replayable in minutes:

```
python3 output/artifacts/enumerate_51_25_12.py
python3 output/artifacts/verify_independent.py  # expect 0/924
```

Artifacts: `orbit_table.json`, `summary.json`, `blocks_F0.json` (SHA-16 `8a7eae3826de5c31`), `spectrum_F0.csv`, `spectrum_full2772.csv`, both scripts. Seed `39051` documented; enumeration is canonical seed-free lex order.

## References

- T. Beth, D. Jungnickel, H. Lenz, Design Theory, 2nd ed., Thm VI.2.5 (First Multiplier Theorem).
- L. D. Baumert, D. M. Gordon, On the existence of cyclic difference sets with small parameters, arXiv:math/0304502; publisher record doi:10.1090/fic/041/05 (k<=150 frontier context).
- H. Y. Song, S. W. Golomb, On the existence of cyclic Hadamard difference sets, IEEE Trans. Inform. Theory 40 (1994) 1266-1268, doi:10.1109/18.335939 (Hadamard-family context).
- N. A. Carella, Cyclic Difference Sets And Cyclic Hadamard Matrices, arXiv:1110.1322 (global claim, no triple-specific enumeration).
- Bruck-Chowla-Ryser theorem (odd-order symmetric designs).
