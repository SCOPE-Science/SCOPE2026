# Knödel-depth spectrum of composites to 5M with maximal simultaneous-pseudoprimality witness

## Context

Knödel classes $C_k$ generalize Carmichael numbers ($k=1$) and $D$-numbers ($k=3$).
Makowski (1962/63) proved each $C_k$, $k \geq 2$, is infinite; Ribenboim surveys
the hierarchy. Prior tables cover only $k=1$ at scale (Pinch; Shallue–Webster to
$10^{22}$) or per-$k$ initial segments (MathWorld; OEIS A050990, A033553, A002997).
No source states the joint depth/multiplicity distribution over all composites in
a range, or a maximal simultaneous-membership witness.

## Definitions

Let $\lambda(n)$ be the Carmichael function (exponent of $(\mathbb{Z}/n\mathbb{Z})^\times$):
$\lambda(p^e)=p^{e-1}(p-1)$ for odd primes $p$; $\lambda(2)=1$, $\lambda(4)=2$,
$\lambda(2^e)=2^{e-2}$ for $e \geq 3$; $\lambda(\prod p_i^{e_i})=\mathrm{lcm}_i \lambda(p_i^{e_i})$.

$n$ is Knödel for parameter $k$ (class $C_k$) iff every unit mod $n$ satisfies
$a^{n-k} \equiv 1 \pmod n$, equivalently $\lambda(n) \mid (n-k)$.
For composite $n$:

$$K(n)=\{k \in [1,n-1] : \lambda(n) \mid (n-k)\},\quad k_{\min}(n)=\min K(n),\quad m(n)=|K(n)|.$$

## Result

Among all $4{,}651{,}486$ composites $n \le 5{,}000{,}000$:

- (a) The Knödel multiplicity $m(n)$ takes exactly $13{,}509$ distinct values.
  The full histogram (rows $(m,\#\{n:m(n)=m\})$, summing to $4{,}651{,}486$) is
  committed in `mhist.csv`.
- (b) The unique maximizer of $m(n)$ is
  $$n^*=4{,}935{,}060=2^2\cdot 3^3\cdot 5\cdot 13\cdot 19\cdot 37,$$
  with $\lambda(n^*)=36$, $m(n^*)=137{,}084$,
  $K(n^*)=\{36,72,\dots,4{,}935{,}024\}$ ($k_{\min}=36$).
- (c) Least composite members of $C_1,\dots,C_{10}$ are
  $561, 4, 9, 6, 25, 8, 15, 12, 21, 12$.
- (d) Slice checks: $|C_1 \cap [4,5\mathrm{M}]|=74$ with heads
  $561,1105,1729,2465,2821$; $|C_3 \cap [4,5\mathrm{M}]|=126{,}029$ with heads
  $9,15,21,33,39,51,57,63,69$.

Distribution notes from `mhist.csv`: median $m=15$; $42.1\%$ have $m \le 10$;
fraction with $m=1$ is $407/4{,}651{,}486$; $131{,}805$ composites have
$m \ge 1000$; count at max is $1$.

## Proof / evidence

**Lemma (reduction to one division).** For composite $n$,
$m(n)=\lfloor (n-1)/\lambda(n)\rfloor$ and
$k_{\min}(n)=n-m(n)\lambda(n)=((n-1)\bmod\lambda(n))+1$.

*Proof.* $k \in K(n) \iff n-k=j\lambda(n)$ for some $j \ge 1$ (since
$1 \le k \le n-1$ gives $1 \le n-k \le n-1$). Admissible $k$ are
$n-\lambda(n),n-2\lambda(n),\dots$, exactly $\lfloor (n-1)/\lambda(n)\rfloor$
of them. ∎

Hence the census needs only $\lambda(n)$ per composite — no per-$k$ scan.

**Witness certificate (hand-checkable).** Prime-power contributions at $n^*$:
$\lambda(4)=2$, $\lambda(27)=18$, $\lambda(5)=4$, $\lambda(13)=12$,
$\lambda(19)=18$, $\lambda(37)=36$.
$\mathrm{lcm}(2,18,4,12,18,36)=36$, so $\lambda(n^*)=36$.
$2^2\cdot 3^3\cdot 5\cdot 13\cdot 19\cdot 37=4\cdot 27\cdot 5\cdot 13\cdot 19\cdot 37=4{,}935{,}060$.
$(n^*-1)/36=4{,}935{,}059/36=137{,}084$ remainder $35$; thus $m=137{,}084$,
$k_{\min}=4{,}935{,}060-137{,}084\cdot 36=36$.
$K(n^*)$ is the progression $36,72,\dots,n^*-36$ (all $137{,}084$ values);
$37 \notin K(n^*)$ since $(n^*-37)\bmod 36 \neq 0$.

**Computation.** Census (`census.c`, C, `gcc -O2`): sieve smallest-prime-factor
to 5M, exact $\lambda$ via prime-power/lcm in 64-bit integers, one division per
composite; emits max witness, $C_1$..$C_{10}$ first occurrences, full
multiplicity histogram, $C_1$/$C_3$ slice counts and heads. Runtime seconds.
Independent recount (`top20.c`, trial division, no sieve): same maximum
$(n^*,m)=(4{,}935{,}060,137{,}084)$, same $C_1$ count $74$, same top-20 list
(all $\lambda \in \{36,48,60\}$). Verifier (`verify.py`): re-derives
$\lambda(n^*)$, replays full $137{,}084$-element $K(n^*)$, proves minimality of
each $C_1$..$C_{10}$ least member by exhaustive composite scan below it,
spot-checks $\lambda$, checks histogram sums to $4{,}651{,}486$ and slice heads.
Independent audit recompiled and re-ran both C programs and re-proved
$C_1$..$C_{10}$ minimality and histogram statistics with separate Python code.

## Limitations

- Window $5\mathrm{M}$ is the assigned scope; maximality is certified only
  within range (larger simultaneous pseudoprimes exist beyond it).
- $C_1$ count $74$ agrees between two independent implementations but was
  cross-checked externally only at heads ($561,1105,1729,2465,2821$), not by a
  full published-table file join.
- Census is exhaustive computation with dual implementation, not a deductive
  proof of a general theorem.

## Reproducibility

`gcc -O2 census.c -o census && ./census` reproduces total, max, histogram
(`mhist.csv`), slice lists, least-member table, and factorization.
`gcc -O2 top20.c -o top20 && ./top20` independently reproduces the maximum and
$C_1$ count. Artifact SHA-256 hashes: `mhist.csv`
`db1f60061fb1ce94b6acec9e6e7967e0f1b38a6b8d8f0f9b750c276887576f26`,
`c1_list.txt` `77cb782394670828ac8d993e653d6c707fbbb37a1c7d0e7612dd88b20afba643`,
`c3_list.txt` `c1fd538c9d2607e4e92c7766906c490f6eadea47f3194dc8d17a410119796869`,
`census.c` `5d397981b2ed04300fb1097bd5a74ff3230de5efcce77819946f2f266e2ea888`,
`top20.c` `21ab4f63beb8bf3ba5711fc72ce6b881b43d72317d3c5c19d661227045a9ef13`,
`verify.py` `557199c11536cfce1ec7fbf58b6fd7d8c03f72e81c825c7cdf74c5c6211f8996`.

## References

- MathWorld, Knödel Numbers. https://mathworld.wolfram.com/KnoedelNumbers.html
- OEIS A050990 (2-Knödel), A033553 (3-Knödel/D-numbers), A002997 (Carmichael).
  https://oeis.org/A050990 https://oeis.org/A033553 https://oeis.org/A002997
- A. Shallue, J. Webster, Advances in Tabulating Carmichael Numbers,
  arXiv:2401.14495. https://arxiv.org/abs/2401.14495
