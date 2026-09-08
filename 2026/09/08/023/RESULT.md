# Exact gap-frequency spectrum of consecutive integers coprime to 30030

## Context
For the primorial $P_6 = 2\cdot 3\cdot 5\cdot 7\cdot 11\cdot 13 = 30030$, consider the
ordered integers coprime to $P_6$ and the gaps between consecutive such integers.
Maximal gaps (Jacobsthal function) and the set of occurring gaps at this scope are
tabled (OEIS A048670, A331118; Ziller arXiv:2007.01808), but Ziller explicitly states
that "existence and frequency of these numbers have not yet been clarified."
$P_6$ is the smallest primorial period exhibiting a missing even gap (20) and the
largest small-primorial period fully enumerable in seconds ($\varphi(P_6)=5760$ gaps).

## Definitions
- $P = 30030$, $\varphi(P) = 1\cdot 2\cdot 4\cdot 6\cdot 10\cdot 12 = 5760$.
- $C = \{1 \le n \le P : \gcd(n,P)=1\} = \{c_1 < c_2 < \dots < c_{5760}\}$, $|C|=5760$.
- Cyclic gaps: $g_i = c_{i+1}-c_i$ for $1 \le i < 5760$, and wrap gap
  $g_{5760} = (P+c_1)-c_{5760}$.
- $N(d) = \#\{i : g_i = d\}$.

## Result (census)
The cyclic consecutive-coprime gap counts modulo 30030 are:

| d | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N(d) | 1485 | 1485 | 1690 | 394 | 438 | 188 | 58 | 12 | 8 | 0 | 2 |

No other gap value occurs. Hence:
- $\sum_d N(d) = 5760$;
- $\sum_d d\cdot N(d) = 30030$;
- every gap is even; the maximum gap is 22;
- 20 is the unique even integer in $[2,22]$ with $N(d)=0$;
  every other even $d$ in $[2,22]$ occurs at least once.
- The exactly two 22-gaps start at 9439 ($9439 \to 9461$) and
  20569 ($20569 \to 20591$); all 21 interior integers in each interval
  share a prime factor with $P$.

## Proof / evidence (finite verification)
1. **Enumeration.** Two independent programs list $C$: (A) $\gcd(n,P)=1$ test;
   (B) boolean sieve striking multiples of 2,3,5,7,11,13. Both yield byte-identical
   ordered lists of length 5760.
2. **Gaps.** The 5759 successive differences plus the cyclic wrap gap
   $g_{5760} = (30030+1)-30029 = 2$ form the multiset $\{g_i\}$;
   $\sum g_i = P = 30030$ telescopically; $|\{g_i\}| = 5760$.
3. **Tally + audits.** Counting gives the table above. Checks:
   $\sum N(d) = 1485+1485+1690+394+438+188+58+12+8+2 = 5760$;
   $\sum d\,N(d) = 2970+5940+10140+3152+4380+2256+812+192+144+44 = 30030$.
   All recorded gaps are even (forced since $P$ is even so all coprimes are odd;
   also verified exhaustively). No gap outside $\{2,\dots,18,22\}$ occurs;
   in particular $N(20)=0$ and the maximum is 22.
4. **Witnesses.** The verifier confirms the exactly two 22-gaps begin at 9439 and
   20569, both endpoints coprime to $P$ with all interior integers non-coprime.
5. **Replay.** `verify.py` re-derives $C$ by both methods, checks list equality,
   recomputes the histogram, asserts equality with the table and all
   moment/parity/missing-20/witness conditions, printing `VERIFY_OK`
   (replayed independently in the audit environment).

## Limitations
- Single-benchmark finite census at $P=30030$ only; no claim about larger
  primorials or asymptotic gap distributions.
- Cyclic-gap convention includes the wrap gap (value 2); a linear (non-cyclic)
  reading over the 5759 interior gaps would report $N(2)=1484$ instead of 1485.
- Proof is by complete machine enumeration with seconds-scale replay; re-run the
  verifier rather than trusting the table second-hand.
- Novelty is the frequency distribution: priors record only the occurring set
  (union), the maximum, single extremal witnesses, and raw totative lists — none
  of which implies the multiplicity vector.

## Reproducibility
```
python3 tally_gcd.py
python3 tally_sieve.py
diff histogram_a.csv histogram_b.csv
python3 verify.py
```
Expected: both tallies print the table with sumN 5760, mom 30030; diff silent;
verifier prints `VERIFY_OK` with `GAP22_STARTS [9439, 20569]`.
Runs in seconds with standard-library Python only.

## References
- Mario Ziller, On differences between consecutive numbers coprime to primorials,
  arXiv:2007.01808 [math.NT], 2020. (Open frequency problem; Table 1: k=6 has
  Nmin=18, missing {20}, h=22; conjectures h(k-1)<=Nmin(k).)
- Mario Ziller and John F. Morack, Algorithmic concepts for the computation of
  Jacobsthal's function, arXiv:1611.03310 [math.NT], 2016-2017. (Jacobsthal maxima
  plus exhaustive maximum-length sequences in ancillaries.)
- OEIS A331118 (primitive first differences in primorial reduced residue systems;
  row 6 is the union {2,...,18,22} via Union@s, discarding multiplicities).
- OEIS A048670 (Jacobsthal function at primorials; a(6)=22, maximum only).
- OEIS A286941 (totatives of primorials; raw ordered coprime rows, no histogram).
- OEIS A049300 (smallest start of longest non-coprime interval; a(6)=9440-adjacent
  extremal witness, not the distribution).
