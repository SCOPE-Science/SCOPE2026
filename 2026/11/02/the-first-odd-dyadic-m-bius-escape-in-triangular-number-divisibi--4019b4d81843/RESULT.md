# The first odd-dyadic Möbius escape in triangular-number divisibility

## Finding

Put \(T(n)=n(n+1)/2\). Order the positive indices by \(a\preceq b\) precisely when \(T(a)\mid T(b)\), and let \(\mu_T(n)=\mu_{\preceq}(1,n)\) be the incidence Möbius function. The following statements hold.

**Order criterion.** Let \(j\ge2\), write \(T(j)=2^\alpha q\), with \(q\) odd, and let \(k\ge1\) be odd. If \(q>1\), then
\[
T(j)\mid T(2^k)
\quad\Longleftrightarrow\quad
k\ge\alpha+1,\quad
\operatorname{ord}_{p^e}(2)=2u_{p,e}\ \text{with every }u_{p,e}\text{ odd},\quad
\operatorname{lcm}_{p^e\parallel q}u_{p,e}\mid k.
\]
Here \(p^e\parallel q\) means exact prime-power divisibility. If \(q=1\), the condition reduces to \(k\ge\alpha+1\).

**First non-3-divisible divisor.** Among all \(j>1\) for which \(3\nmid T(j)\) and \(T(j)\mid T(2^k)\) for some odd \(k\ge3\), the least index is \(j=43\). More precisely, for every integer \(k\ge1\),
\[
T(43)=946\mid T(2^k)\quad\Longleftrightarrow\quad k\equiv35\pmod{70}.
\]
Thus this first obstruction appears infinitely often. Moreover, for every odd \(k\) with \(3\le k\le33\), every proper triangular divisor \(T(j)>1\) of \(T(2^k)\) is divisible by three; the earliest odd exponent allowing a proper prime-to-three triangular divisor is \(35\).

**Möbius consequence.** On the same odd-exponent dyadic subsequence,
\[
\mu_T(2^k)=0\quad(3\le k\le33,\ k\text{ odd}),
\qquad\mu_T(2^{35})=1.
\]
The exceptional initial exponent \(k=1\) has \(\mu_T(2)=-1\) and is not included in the zero interval.

## Assumptions and scope

All indices and exponents are positive integers. The Möbius function is normalized by \(\mu_T(1)=1\) and, for \(n>1\), \(\mu_T(n)=-\sum_{j<n,\,T(j)\mid T(n)}\mu_T(j)\). There is no assumption about primality of \(2^k+1\), and no asymptotic assertion about the sequence \(\mu_T(n)\). The finite minimality assertions concern all indicated indices and exponents, not sampled values.

## Proof

**1. Order criterion.** For every \(k\ge1\),
\[
T(2^k)=2^{k-1}(2^k+1).
\]
The two factors on the right are coprime. Consequently \(2^\alpha q\mid T(2^k)\) is equivalent to \(k-1\ge\alpha\) and \(2^k\equiv-1\pmod q\). For each odd prime power \(p^e\parallel q\), the multiplicative order \(h=\operatorname{ord}_{p^e}(2)\) is even if \(2^k=-1\). Since the unit group modulo an odd prime power has unique element of order two, that condition is equivalent to \(k\equiv h/2\pmod h\). If \(k\) is odd, necessarily \(h=2u\) with \(u\) odd, and the congruence becomes \(u\mid k\); conversely an odd multiple of such a \(u\) sends \(2\) to \(-1\). Requiring this at every prime power gives exactly the displayed least-common-multiple criterion. When \(q=1\), there are no odd prime-power conditions.

**2. Least exceptional divisor.** Since \(T(j)\equiv0\pmod3\) for \(j\equiv0,2\pmod3\) and \(T(j)\equiv1\pmod3\) for \(j\equiv1\pmod3\), a candidate with \(3\nmid T(j)\) must have \(j\equiv1\pmod3\). For every such index \(4\le j\le40\), the following pair \((p,h)\) gives a prime \(p\mid T(j)\) and its exact order \(h=\operatorname{ord}_p(2)\):

| \(j\) | \((p,h)\) | \(j\) | \((p,h)\) |
|---:|---:|---:|---:|
| 4 | (5,4) | 7 | (7,3) |
| 10 | (5,4) | 13 | (7,3) |
| 16 | (17,8) | 19 | (5,4) |
| 22 | (23,11) | 25 | (5,4) |
| 28 | (7,3) | 31 | (31,5) |
| 34 | (5,4) | 37 | (37,36) |
| 40 | (5,4) | | |

Every listed order is odd or divisible by four. The criterion in Step 1 therefore excludes *every odd exponent* for these indices. In contrast, \(T(43)=946=2\cdot11\cdot43\), and \(\operatorname{ord}_{11}(2)=10\), \(\operatorname{ord}_{43}(2)=14\). Thus an odd \(k\) works exactly when \(5\mid k\), \(7\mid k\), and \(k\ge2\), namely \(k\equiv35\pmod{70}\). The same congruence characterizes all positive \(k\), because both equations \(2^k=-1\) require the odd residue classes \(5\pmod{10}\) and \(7\pmod{14}\).

**3. Exact earliest-exponent boundary.** For each odd exponent \(1\le k\le35\), factor \(2^k+1\), enumerate *all* divisors of \(2^{k-1}(2^k+1)\), and test whether \(8d+1\) is an odd perfect square. This test is equivalent to \(d=T(j)\) for a positive integer \(j\). The complete lists of proper indices \(1<j<2^k\) are:

| \(k\) | Proper triangular-divisor indices \(j\) |
|---:|:---|
| 1 | none |
| 3 | 2, 3 |
| 5 | 2, 3, 11 |
| 7 | 2, 3 |
| 9 | 2, 3, 8, 18 |
| 11 | 2, 3 |
| 13 | 2, 3 |
| 15 | 2, 3, 8, 11, 32 |
| 17 | 2, 3 |
| 19 | 2, 3 |
| 21 | 2, 3, 8, 128 |
| 23 | 2, 3 |
| 25 | 2, 3, 11, 32 |
| 27 | 2, 3, 8, 18, 512 |
| 29 | 2, 3 |
| 31 | 2, 3 |
| 33 | 2, 3, 8, 2048 |
| 35 | 2, 3, 11, 32, 43, 128 |

The enumeration is exhaustive: the supplied `verify.py` builds every divisor from a full prime-power factorization, using integer trial division, checks factors for primality by trial division, and applies the perfect-square test exactly (integer square root, not floating point). It also compares all 18 divisor lists to the displayed table. Every proper \(j\) for odd \(3\le k\le33\) has \(3\mid T(j)\), whereas \(T(43)\equiv1\pmod3\).

**4. Möbius computation.** Fix an odd \(k\) with \(3\le k\le33\). Every proper nonidentity triangular divisor of \(T(2^k)\) is a multiple of three. In particular, \(T(2)=3\) divides all of them. In the interval \([1,2^k]\), induction on the indices now gives \(\mu_T(2)=-1\) and \(\mu_T(j)=0\) for every other proper index \(j>2\): all such lower intervals have the same property, so the sum from \(1\) and \(2\) cancels. Consequently \(\mu_T(2^k)=-(1-1)=0\).

For \(k=35\), the complete triangular-divisor interval has exactly the eight indices
\[
1,\ 2,\ 3,\ 11,\ 32,\ 43,\ 128,\ 2^{35},
\]
with the corresponding triangular values
\[
1,\ 3,\ 6,\ 66,\ 528,\ 946,\ 8256,\ 590295810375885520896.
\]
Their incidence Möbius values, computed successively from the defining recurrence, are
\[
1,\ -1,\ 0,\ 0,\ 0,\ -1,\ 0,\ 1.
\]
These are exact integer calculations on the entire lower interval, not a truncation at small indices. As a check on exhaustion, \(2^{35}+1=3\cdot11\cdot43\cdot281\cdot86171\), so \(T(2^{35})=2^{34}\cdot3\cdot11\cdot43\cdot281\cdot86171\). This completes the proof.

## Verification

`python3 verify.py` uses only the Python standard library. It checked the 18 complete odd-dyadic intervals through exponent 35, the incidence recursion on their finite lower intervals, 3,822 separate small-parameter equivalences between the order criterion and direct divisibility, and the exact congruence for index 43 through exponent 179. The emitted message begins `VERIFY_OK`. These finite checks corroborate the exhaustive finite steps; the order criterion and infinite congruence progression follow from the symbolic argument above.

## Relationship to prior work

Pandey and Richman introduced and investigated this Möbius function, including its two-variable incarnation, numerical behavior, open asymptotic questions, and elementary divisibility patterns (arXiv:2402.07934, first posted 2024-02-06). Their Appendix C proves different divisibility identities, not the odd-dyadic order classification or the exceptional exponent established here. OEIS A350682 records the same Möbius function, first documented on 2022-01-11 and with a published numerical table covering indices through 10,000; the exact index \(2^{35}\) lies far beyond that table. The defining recurrence alone does not supply the new structural order criterion, its least admissible prime-to-three triangular divisor, or the verified full eight-element lower interval at that large index.

## Limitations

This theorem determines a specific dyadic subsequence boundary and does not settle the large-scale conjectures on averages or unboundedness of \(\mu_T\). The finite cutoff at exponent 35 is established by exact exhaustive arithmetic over the explicitly bounded range; it does not assert that later odd exponents must all give nonzero Möbius values. Bibliographic searches did not prove global novelty, and an equivalent statement in older studies of divisibility or multiplicative orders remains possible.

## References

1. Rohan Pandey and Harry Richman, *The Möbius function of the poset of triangular numbers under divisibility*, arXiv:2402.07934, first submitted 2024-02-06. https://arxiv.org/abs/2402.07934
2. OEIS Foundation, A350682, *Möbius values of triangular numbers under divisibility relation*, original sequence entry dated 2022-01-11. https://oeis.org/A350682 and https://oeis.org/history?seq=A350682&start=40
3. OEIS A350682 associated finite table of indices \(1\) through \(10000\), https://oeis.org/A350682/b350682.txt
