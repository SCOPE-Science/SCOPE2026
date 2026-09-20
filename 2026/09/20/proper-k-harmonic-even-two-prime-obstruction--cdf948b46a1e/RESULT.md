# No even two-prime proper power-harmonic numbers

For a positive integer `k`, write

\[
\sigma_k(n)=\sum_{d\mid n} d^k,\qquad
H_k(n)=\frac{n^k\tau(n)}{\sigma_k(n)}.
\]

Following Cohen and Deng, `n>1` is `k`-harmonic if `H_k(n)` is an integer, and it is proper power-harmonic if it is `k`-harmonic for some `k>=2`.

## Theorem

Let `k>=2`, `a,b>=1`, and let `p` be an odd prime. Then

\[
\boxed{\sigma_k(2^a p^b)\nmid (2^a p^b)^k\tau(2^a p^b)}.
\]

Equivalently, there is no proper `k`-harmonic number of the form

\[
2^a p^b.
\]

Hence every even proper power-harmonic number, if one exists, has at least three distinct prime factors. In particular, every hypothetical proper power-harmonic number with exactly two distinct prime factors must be odd.

## Proof

Put

\[
m=a+1,\qquad c=b+1,
\]

and

\[
A=\sigma_k(2^a)=\frac{2^{km}-1}{2^k-1},\qquad
B=\sigma_k(p^b)=\frac{p^{kc}-1}{p^k-1}.
\]

Assume for contradiction that `2^a p^b` is `k`-harmonic. Multiplicativity of `sigma_k` gives

\[
AB\mid 2^{ak}p^{bk}mc. \tag{1}
\]

First apply the Bang--Zsigmondy theorem to `p^{kc}-1`. Since `p` is odd and `kc>=4`, none of the exceptional cases occurs. Therefore there is a primitive prime divisor `s` of `p^{kc}-1`. Because `s` is primitive and `k<kc`, it does not divide `p^k-1`, so `s|B`. Moreover

\[
\operatorname{ord}_s(p)=kc,
\]

hence

\[
kc\mid s-1,
\qquad s\ge kc+1>c. \tag{2}
\]

The prime `s` is neither `2` nor `p`. From (1), `s` must therefore divide `m c`. Since `s>c`, it cannot divide `c`; hence

\[
s\mid m,
\qquad m\ge s\ge kc+1. \tag{3}
\]

In particular `m>kc`, and therefore `m>c`.

Now apply Bang--Zsigmondy to `2^{km}-1`. If `km!=6`, there is a primitive prime divisor `r`. It divides `A`, and

\[
\operatorname{ord}_r(2)=km,
\qquad r\ge km+1>m>c. \tag{4}
\]

Thus (1) shows that `r` can divide neither `2`, `m`, nor `c`; the only remaining prime factor on the right side of (1) is `p`. Consequently

\[
r=p.
\]

From (4), `km|p-1`, so in particular

\[
m\mid p-1. \tag{5}
\]

But (3) gives `s|m`, and therefore (5) gives `p=1 (mod s)`. This says `ord_s(p)=1`, contradicting `ord_s(p)=kc>=4`.

It remains to treat the sole possible Zsigmondy exception for the base `2`, namely `km=6`. Since `k,m>=2`, the possibilities are `(k,m)=(2,3)` and `(3,2)`. But (3) requires `m>=kc+1`, which is respectively at least `5` or at least `7`, an immediate contradiction. Thus no exceptional case survives, proving the theorem. \(\square\)

## Relation to earlier work

Cohen and Deng introduced `k`-harmonic numbers in 1998. The standard summary in Sándor and Crstici's *Handbook of Number Theory II* records, for a hypothetical proper `k`-harmonic number `2^a p^b`, the necessary restrictions

- if `k` is even, then `b = 7 (mod 8)`;
- if `k` is odd, then `b` is odd and `(p+1)(b+1)=0 (mod 16)`.

The theorem above eliminates the entire even two-prime-support case rather than imposing congruence conditions on `b`. The mechanism is different: primitive prime divisors of the two geometric sums force incompatible multiplicative orders.

To the best of our knowledge, searches under `k`-harmonic, power-harmonic, `2^a p^b`, two distinct prime factors, and primitive-divisor/Zsigmondy formulations did not locate this nonexistence theorem or a stronger result that implies it. The complete text of the 1998 Cohen--Deng paper was not available in the sources inspected; its bibliographic page, later citations, and the handbook's detailed summary of its relevant necessary conditions were checked. This leaves a residual possibility that an equivalent argument appears in the original paper or in literature using different terminology.

## Verification

A standalone exact-integer check in `artifacts/verify.py` tests

\[
2\le k\le8,\quad 1\le a,b\le8,
\]

for every odd prime `p<500`. It evaluates the defining divisibility directly and finds no hits among `42112` parameter quadruples. This computation is supporting evidence only; the theorem is proved without a finite cutoff.

## Limitations

The result concerns even integers with exactly two distinct prime factors. It does not rule out odd proper `k`-harmonic numbers with two prime factors, nor even candidates with at least three distinct prime factors. No proper `k`-harmonic number with `k>=2` is presently known in the literature sources inspected.

## References

1. G. L. Cohen and Deng Moujie, "On a generalisation of Ore's harmonic numbers," *Nieuw Archief voor Wiskunde* (4) 16 (1998), 161--172, MR1680101. Bibliographic page: https://www.researchgate.net/publication/266699253_On_a_generalisation_of_Ore%27s_harmonic_numbers
2. J. Sándor and B. Crstici, *Handbook of Number Theory II*, Kluwer, 2004, pp. 44--45. Accessible scan containing the quoted summary: https://cjhb.site/Files.php/Books/%28Uncategorized%29/Handbook/Sandor-Crstici2004_Book_HandbookOfNumberTheoryII.pdf
3. K. Zsigmondy, "Zur Theorie der Potenzreste," *Monatshefte für Mathematik und Physik* 3 (1892), 265--284. DOI: https://doi.org/10.1007/BF01692444
4. E. W. Weisstein, "Zsigmondy Theorem," MathWorld: https://mathworld.wolfram.com/ZsigmondyTheorem.html
