# Exact Sprague-Grundy periodicity for octal heap game 0.057

## Context

Octal heap games are a computable edge of impartial-game theory: full
classification is wild, yet a single ruleset can admit an exact ultimate
periodicity provable by finite computation plus a Guy–Smith induction.
Game 0.057 is the splitting-dominant neighbour of solved Dawson's Kayles
0.07 (differs by forbidding the take-2 singleton leave), sits below 2.00,
and was previously only tabulated as computed-but-unproved. Closing it
gives a durable classification where every large heap is an N-position.

## Definitions

Octal code `0.057` has fractional digits $d_1=0$, $d_2=5=101_2$,
$d_3=7=111_2$, max removal $m=3$. Bit $b_0+2b_1+4b_2$ means removing that
many beans may leave $0$, $1$, or $2$ non-empty heaps. Hence for heap $n$:

- Remove 1: $d_1=0$ — no moves.
- Remove 2: $d_2=5$ — if $n=2$, take whole heap (terminal); if $n>2$,
  move to two non-empty heaps $a+b=n-2$ only (no singleton leave).
- Remove 3: $d_3=7$ — if $n=3$, take whole heap (terminal); if $n>3$,
  move to singleton $n-3$ or to two non-empty heaps $a+b=n-3$.

Let $G(n)$ be the Sprague–Grundy value, $G(0)=0$. For $n\\ge 1$,
$G(n)=\\mathrm{mex}\\,S(n)$ with:

- $S(1)=\\varnothing$ ($G(1)=0$),
- $S(2)=\\{0\\}$, $S(3)=\\{0\\}$ (take-2 splits of $n=3$ need $a+b=1$,
  impossible),
- for $n>3$: $S(n)=\\{G(n-3)\\}\\cup\\{G(a)\\oplus G(n-3-a)\\}
  \\cup\\{G(a)\\oplus G(n-2-a)\\}$ over valid $a$.

## Result (proved)

**Theorem.** The Sprague–Grundy sequence of octal 0.057 is ultimately
periodic with minimal preperiod $N_0=259$ and minimal period $p=148$:

$$G(n+148)=G(n)\\quad\\text{for all }n\\ge 259.$$

The pair is minimal. Periodic values lie in $\\{1,2,4,7,8\\}$ (8 occurs;
0 never occurs in the tail) with counts $1\\!\\times\\!54$,
$4\\!\\times\\!53$, $2\\!\\times\\!17$, $7\\!\\times\\!16$,
$8\\!\\times\\!8$. Global maximum is $8$; overall values to 20000 lie in
$\\{0,1,2,3,4,6,7,8\\}$ (5 never occurs). P-positions are exactly
$\\{0,1\\}$ — every heap $n\\ge 2$ is an N-position.

The cycle $C=G(259)\\dots G(406)$ is:

```
2,7,4,4,4,1,1,1,8,4,4,2,1,1,1,4,4,4,7,2,1,2,8,4,4,1,1,1,2,7,4,4,4,1,1,1,
8,4,4,7,1,1,1,4,4,4,7,2,1,1,1,4,4,4,2,1,2,7,4,4,1,1,1,2,2,4,4,7,8,1,1,4,
4,4,7,2,1,1,1,4,4,4,8,1,1,7,4,4,4,1,1,1,2,7,4,7,8,1,1,4,4,4,7,2,1,1,1,4,
4,4,8,1,1,2,4,4,4,1,1,1,2,7,4,4,4,1,1,1,7,4,7,2,1,1,1,4,4,4,7,1,1,2,8,4,
4,1,1,1
```

Observed prefix: $G(0..40)=0,0,1,1,1,2,2,2,3,1,1,1,4,4,4,3,2,2,2,1,1,1,4,
2,2,2,6,4,4,4,1,1,1,2,2,2,7,1,1,1,4$.

## Proof / evidence

Computation gives $G(0..8000)$ deterministically (0.74 s) with
$G(n+148)=G(n)$ for all $n\\in[259,7852]$ (7594 agreements, ~51 periods,
zero mismatches; stability re-confirmed to 20000, ~133 periods).

**Lemma 1 (self-contained Guy–Smith propagation).** Fix $m=3$. Let
$T^*=2N_0+2p+m$. If $G(n)=G(n-p)$ for all $n\\in[N_0+p,T]$ with
$T\\ge T^*$, then $G(N)=G(N-p)$ for every $N>T$.

*Proof.* Induction on $N$. Assume equality on $[N_0+p,N-1]$. For $N>m$
neither $N$ nor $N-p$ has terminal moves. Singletons match since
$N-3\\in[N_0+p,N-1]$. For splits $A(S)=\\{G(a)\\oplus G(S-a)\\}$ with
$S=N-k$, $S'=S-p$ ($k=2,3$): any $a+b=S$ has
$b=\\max(a,b)\\ge S/2\\ge N_0+p+1/2$, so $b\\ge N_0+p+1$ and $b<N$,
hence $G(b)=G(b-p)$ gives same xor in $A(S')$; conversely any
$c+d=S'$ has $d\\ge S'/2\\ge N_0+1$, $j=d+p$ satisfies $N_0+p<j<N$ so
$G(j)=G(d)$ gives same xor in $A(S)$. Thus $S(N)=S(N-p)$ and mexs agree. ∎

Application: $N_0=259$, $p=148$ gives $T^*=817\\le 7852$, so periodicity
extends to all $n\\ge 259$.

Independent stdlib-only verifier re-reads the CSV and checks integrity,
suffix equality, mex recomputation (full-range 0 mismatches; final two
blocks and base window explicitly logged), reachable-set equality
$S(n)=S(n+148)$ on the final full block (148/148), threshold coverage,
$G(258)=2\\ne 1=G(406)$ blocking smaller preperiod, exact cyclic period
148 (no $p'<148$ divides the cycle), and census. Result:
`CERTIFICATE PASS` in 0.34 s single-core. Minimality follows jointly:
any period of the infinite tail is a multiple of 148, and any
$N_0'<259$ fails at $n=258$ since $G(258+k\\cdot148)=G(406)=1\\ne2$.

Experimental corroboration (not load-bearing): $p\\le1000$ scan shows
only $(259,\\text{multiples of }148)$ with long window; all other $p$
match only at $n\\ge6995$ with window $\\le6$.

## Limitations

- Method (mex + Guy–Smith) is classical; novelty is the exact certificate
  for 0.057 only. General octal conjectures untouched.
- Induction base is computational; trust rests on two independent
  implementations (numpy compute, stdlib verifier) plus logged CSV —
  rerunnable in seconds. No floating point, randomness, or heuristics.
- Neighbouring codes (e.g. Dawson's Kayles 0.07, other $0.05x$) untouched;
  nothing transfers automatically.
- Value 5 never observed to 20000 but no theorem about it beyond
  certified max-8 / cycle-set facts.

## Reproducibility

```
python3 output/artifacts/compute_grundy_0057.py 8000 output/artifacts/grundy_0057_N8000.csv
python3 output/artifacts/detect_period.py output/artifacts/grundy_0057_N8000.csv
python3 output/artifacts/verify_certificate_0057.py output/artifacts/grundy_0057_N8000.csv
```

Total <5 s single-core (compute ~0.74 s, verifier ~0.34 s).

## References (context only; proof is self-contained)

- R. K. Guy and C. A. B. Smith, “The G-values of various games,”
  Proc. Cambridge Philos. Soc. 52 (1956) — periodicity theorem whose
  argument Lemma 1 re-proves with explicit threshold.
- E. R. Berlekamp, J. H. Conway, R. K. Guy, Winning Ways, Vol. 1
  (octal games chapter); A. Siegel, Combinatorial Game Theory —
  background on octal rules and mex.
- A. Flammenkamp, octal-game survey tables
  (http://wwwhomes.uni-bielefeld.de/achim/octal.html) — computed
  (conjectured, unproved) values; this note supplies the missing proof
  window for 0.057.
