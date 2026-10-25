# The first Schenker prime with six nonzero zero-classes

## Finding
For positive integers \(n\), define the Schenker sum
\[
a_n=\sum_{j=0}^{n}\frac{n!}{j!}n^j.
\]
For each prime \(p\), set
\[
R(p)=\{r\in\{1,\dots,p-1\}:a_r\equiv0\pmod p\},
\qquad \lambda(p)=|R(p)|.
\]
The **least prime with \(\lambda(p)\ge6\)** is \(p=2339\), and
\[
R(2339)=\{156,470,520,589,1092,2170\},\qquad \lambda(2339)=6.
\]
Exactly \(345\) primes lie below \(2339\); their root-count histogram for multiplicities \(0,1,2,3,4,5\) is respectively
\[
(121,140,65,14,4,1).
\]
In particular, the largest previous multiplicity is \(5\), attained at \(p=593\). This is a complete, finite answer to the case \(m=6\) of the existence question for the multiplicities of Schenker primes [2, Question 4].

## Assumptions and scope
All sums and congruences are over the ordinary integers. The prime condition is verified by an exhaustive Eratosthenes sieve, not assumed from a probabilistic primality test. The zero classes count nonzero residues only: \(1\le r<p\), as in [2]. The assertion is **finite** and concerns all primes \(p\le2339\), not every prime, higher prime powers, or unboundedness of the function \(\lambda\).

## Proof
Put
\[
B_j(r)=j!\sum_{i=0}^j\frac{r^i}{i!},\qquad B_0(r)=1.
\]
Every \(B_j(r)\) is an integer. Multiplication by \(j\) gives the exact recurrence
\[
B_j(r)=jB_{j-1}(r)+r^j\quad(j\ge1),
\qquad a_r=B_r(r).
\]
For any prime \(p\) and integer \(r\) in the full domain \(1\le r<p\), let \(b_0=w_0=1\) and apply
\[
w_j\equiv r w_{j-1}\pmod p,\qquad
b_j\equiv j b_{j-1}+w_j\pmod p\quad(1\le j\le r).
\]
Induction on \(j\) proves \(w_j\equiv r^j\) and \(b_j\equiv B_j(r)\pmod p\). Thus \(b_r=0\) is **equivalent** to \(r\in R(p)\), with no floating point arithmetic and no omitted summands.

The accompanying `verify_minimum.cpp` first marks every prime in the complete integer interval \([2,2339]\) by the usual sieve. For **each** marked prime it evaluates \(b_r\) for **every** \(r\in\{1,\ldots,p-1\}\) by the preceding recurrence. It checks both that the six and only six roots for \(2339\) are the displayed residues and that every smaller prime has at most five roots. It additionally checks the complete multiplicity histogram and the earliest five-root prime \(593\). The exhaustive integer certificate yields the claimed minimality. The code contains all numerical bounds and assertions needed to replay this finite proof.

For context, the modular reduction to residue classes is valid globally: if \(p\nmid n\) and \(n\equiv r\pmod p\), with \(1\le r<p\), then \(p\mid a_n\) if and only if \(p\mid a_r\), by [1, Proposition 3.2]. Thus \(R(p)\) is precisely the nonzero residue-class zero-set used in the original Schenker-prime definition, rather than merely a truncated selection of candidate indices. This reduction is known and is not claimed as a new lemma.

## Verification
Build and execute from the directory containing `verify_minimum.cpp`:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_minimum.cpp -o verify_minimum
./verify_minimum
```

The output must include `earliest_prime_with_lambda_ge_6=2339`, `lambda_2339=6`, the displayed six roots, `primes_checked_below=345`, the histogram, and `VERIFY_OK`. An independent modular implementation of just the six-root computation is provided in `verify_roots.py`; run `python3 verify_roots.py`. It instead uses factorials and inverse factorials modulo \(2339\), and also asserts the exact six-element zero-set. Both programs were executed on their actual packaged source files before inclusion, with success.

## Relationship to prior work
Amdeberhan, Callan and Moll [1] established the prime-modulus reduction for Schenker sums, and Miska [2] introduced \(\lambda(p)\), tabulated the first \(200\) primes (maximum displayed value \(5\) at \(593\)), and explicitly asked whether arbitrarily large multiplicities occur. This result determines the first example at the next integer level and proves the sharp least-prime cutoff. Miska's later generalized-sequence study [3] and the 2017 published treatment [4] develop modular periodicity and prime-divisor techniques; those general tools do not themselves enumerate the complete \(p\le2339\) classical \(h(X)=X\) root spectrum. The tables in [4] concern different defining polynomials. Searches of the published literature and research-record index did not locate the specific complete cutoff, but absence from search results does not prove uniqueness in the literature.

## Limitations
The result is a finite exact calculation with fully specified integer arithmetic, not a proof of the general unboundedness question (which asks for every \(m\)). It makes no assertion about the full higher prime-power valuation behavior at the six classes. Complete novelty beyond the consulted sources cannot be certified by web/index searches alone, and there has been no independent human audit.

## References
[1] T. Amdeberhan, D. Callan and V. Moll, *Valuations and combinatorics of truncated exponential sums*, Integers **13** (2013), A21; https://emis.de/ft/4841 ; especially Proposition 3.2 and Section 4.

[2] P. Miska, *A note on \(p\)-adic valuations of the Schenker sums*, arXiv:1401.1717v1 (2014-01-08), https://arxiv.org/abs/1401.1717 ; Table 1 and Question 4.

[3] P. Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, arXiv:1508.01987v1 (2015-08-09), https://arxiv.org/abs/1508.01987 ; Section 7.

[4] P. Miska, *Arithmetic properties of generalizations of Schenker sums*, International Journal of Number Theory **13** (2017), 1585–1601, DOI:10.1142/S1793042117500890; Section 3, Tables 1–3 (different polynomials).
