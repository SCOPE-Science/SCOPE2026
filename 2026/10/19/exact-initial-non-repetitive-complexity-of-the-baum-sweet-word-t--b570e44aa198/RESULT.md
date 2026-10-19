# Exact initial non-repetitive complexity of the Baum–Sweet word through length \(8192\)

## Finding

Let \(B=b_0b_1b_2\cdots\) be the Baum–Sweet binary word, indexed from zero, with \(b_0=1\) and, for positive \(i\), \(b_i=1\) exactly when every run of zeroes in the ordinary binary expansion of \(i\) has even length. Write \(B[i,n]=b_i\cdots b_{i+n-1}\). The *initial non-repetitive complexity* \(R(n)\) is the smallest \(j\ge1\) for which \(B[j,n]=B[i,n]\) for some \(0\le i<j\); at this first collision the earlier index \(P(n)=i\) is unique.

**The finite classification theorem.** For every integer \(1\le n\le8192\), the following table gives \(R(n)\) and \(P(n)\) **exactly**, constant on each listed inclusive interval. No values outside this domain are claimed.

| Factor lengths \(n\) | First repeated position \(R(n)\) | Unique earlier position \(P(n)\) |
|---:|---:|---:|
| 1–1 | 1 | 0 |
| 2–3 | 3 | 0 |
| 4–5 | 9 | 4 |
| 6–7 | 14 | 2 |
| 8–8 | 24 | 8 |
| 9–12 | 28 | 4 |
| 13–16 | 48 | 16 |
| 17–25 | 56 | 8 |
| 26–32 | 96 | 32 |
| 33–48 | 112 | 16 |
| 49–64 | 192 | 64 |
| 65–97 | 224 | 32 |
| 98–128 | 384 | 128 |
| 129–192 | 448 | 64 |
| 193–256 | 768 | 256 |
| 257–385 | 896 | 128 |
| 386–512 | 1536 | 512 |
| 513–768 | 1792 | 256 |
| 769–1024 | 3072 | 1024 |
| 1025–1537 | 3584 | 512 |
| 1538–2048 | 6144 | 2048 |
| 2049–3072 | 7168 | 1024 |
| 3073–4096 | 12288 | 4096 |
| 4097–6145 | 14336 | 2048 |
| 6146–8192 | 24576 | 8192 |

The table has precisely 25 maximal intervals of constancy for the ordered pair \((R(n),P(n))\). At all displayed dyadic lengths \(8,16,\ldots,8192\), \(R(2^k)=3\cdot2^k\) and \(P(2^k)=2^k\), but this is a **finite observation**, not an infinite formula. Above length seven the displayed first-repetition positions alternate between dyadically scaled multiples of three and seven, with sharp transition lengths given by the table.

## Assumptions and scope

The word is the classical Baum–Sweet word beginning \(1101100101001001\cdots\), not its shift or complement. All factors are ordinary contiguous factors; factor occurrences are indexed from zero, and only lengths \(1\le n\le8192\) are in scope. The construction of the verifying finite prefix uses the two-uniform morphism \(A\mapsto AB,\ B\mapsto CB,\ C\mapsto BD,\ D\mapsto DD\), started at \(A\), followed by the coding \(A,B\mapsto1\), \(C,D\mapsto0\). The independent check instead uses the direct binary zero-run definition.

## Proof

**1. Collision monotonicity and unique predecessor.** If two length-\(m\) factors at indices \(i<j\) agree, then their prefixes of any smaller positive length agree. Consequently \(R(n)\) is nondecreasing. At \(j=R(n)\) there cannot be two distinct earlier indices \(i_1<i_2<j\) matching the factor at \(j\), since then the two factors at \(i_1,i_2\) would already collide before \(j\). Thus \(P(n)\) is well-defined and unique.

**2. Exact boundary reduction.** Suppose an inclusive integer interval \([a,b]\) and two positions \(p<r\) satisfy \(R(a)=r\) and \(B[p,b]=B[r,b]\). For any \(a\le n\le b\), monotonicity gives \(R(n)\ge R(a)=r\); the displayed equality at length \(b\) gives \(R(n)\le r\). Hence \(R(n)=r\) throughout. The same equality forces \(P(n)=p\) throughout by uniqueness. It is therefore enough to verify the first repetition and matching predecessor at the two endpoints of each of the 25 intervals.

**3. Exhaustive finite endpoint certificate.** `verify_endpoints.cpp` directly computes the first repeat at the 50 endpoints from the direct binary-digit definition, using a finite prefix of length \(4\cdot8192+2=32770\). For each factor length it scans starting positions \(j=0,1,\ldots\) in increasing order. Polynomial 64-bit substring hashes only partition candidate comparisons: *all* previous positions with the same hash are retained, and each possible equality is decided with an exact bytewise comparison. Equal factors necessarily have equal hashes; a hash collision cannot create an accepted false equality or conceal a genuine earlier equality. All endpoint pairs match `profile8192.csv`. The largest reported first repetition is \(24576\), so no position or symbol beyond the generated finite prefix is needed. By Step 2, the 25 endpoint certificates prove every table row for every integer in its interval.

**4. Independent structural reconstruction.** `profile.cpp` builds a length-\(65536\) prefix by the four-state morphism, constructs its suffix array and longest-common-prefix array, and evaluates for each position \(j\) the largest common prefix with an earlier suffix. The maximum is attained at one of the two lexicographically adjacent earlier suffixes: all intervening suffixes constrain common prefixes by the minimum adjacent LCP. A sparse-table range minimum gives exact suffix LCP values. For each factor length, the first index \(j\) whose maximum earlier LCP reaches that length is its first repetition. This independently yields the 25 intervals and earlier indices in the CSV; the direct verifier reproduces all endpoint facts without reliance on the suffix-array implementation.

## Verification

The reproducible package includes `profile8192.csv`, `profile.cpp`, and `verify_endpoints.cpp`. With a C++17 compiler, execute:

```sh
g++ -O2 -std=c++17 profile.cpp -o profile
./profile 8192 > profile8192_recomputed.csv
cmp profile8192.csv profile8192_recomputed.csv
g++ -O2 -std=c++17 verify_endpoints.cpp -o verify_endpoints
./verify_endpoints 8192 profile8192.csv
```

The last command outputs `VERIFY_OK M=8192 intervals=25 boundary_cases=50`. Both generators agree on the Baum–Sweet prefix used. A finite exhaustive calculation is an exact proof for this specified finite domain, **not** an infinite proof for all factor lengths.

## Relationship to prior work

Nicholson and Rampersad introduced systematic analysis of the initial non-repetitive complexity invariant and gave formulas for the Thue–Morse, Fibonacci, and Tribonacci words, but not for Baum–Sweet [1]. Medková, Pelantová, and Vandomme studied the invariant on standard Arnoux–Rauzy words and related structures [2]; the non-uniformly recurrent Baum–Sweet word is not covered by their hypotheses. The automatic definition of the Baum–Sweet word and its four-state morphism are classical [3,4]. These results establish the object and invariant, not the 25-interval collision-time and predecessor classification above.

## Limitations

No theorem is asserted beyond factor length \(8192\). The visible powers-of-two and alternating plateau patterns are finite evidence rather than proved asymptotic laws, and the exact global factor complexity or other word complexity is not deduced here. A mathematical computation carried out by code, even when reproduced by an independent algorithm, has not received an independent scientific audit. A literature-equivalent spectrum that is not indexed by the inspected sources remains possible.

## References

[1] J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206 (first posted 2015-07-29), Discrete Applied Mathematics 208 (2016), 114–122. https://arxiv.org/abs/1507.08206

[2] K. Medková, E. Pelantová, and E. Vandomme, *On non-repetitive complexity of Arnoux–Rauzy words*, arXiv:2002.12593 (2020). https://arxiv.org/abs/2002.12593

[3] L. E. Baum and M. M. Sweet, *Continued fractions of algebraic power series in characteristic 2*, Annals of Mathematics 103 (1976), 593–610. https://doi.org/10.2307/1970953

[4] J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), Example 5.1.7.
