# A nonmonotone solvability law for four-person Mallows roommates

## Finding

In a four-person complete strict stable-roommates market, fix one common quality order and let each person independently draw a **full four-name** Mallows permutation with dispersion \(q\in[0,1]\), then delete their own name. Let \(U\) be the event that none of the three perfect matchings is stable. The exact law is

\[
\Pr_q(U)=\frac{q^2(3q^8+q^7+3q^6-2q^5+6q^4-2q^3+3q^2+q+3)}{(1+q)^2(1+q^2)^2(1+q+q^2)^3}.
\]

The probability increases strictly until a **unique** \(q_*\in(379/1000,380/1000)\) and then decreases strictly up to \(q=1\). Numerically \(q_*\approx0.379463975606\) and \(\Pr_{q_*}(U)\approx0.062502550194\), compared with \(\Pr_1(U)=1/27\approx0.037037037037\). Thus the maximum unsolvability probability is about \(1.68757\) times its impartial-culture value. For small dispersion, \(\Pr_q(U)=3q^2+O(q^3)\): a total of two full-order inversions is the sharp rare-event threshold.

## Assumptions and scope

The four people are labeled \(1,2,3,4\). Each person's strictly ordered list contains every other person. For a perfect matching \(M\), an unmatched pair \(\{i,j\}\) blocks when both people strictly prefer each other to their partners in \(M\). A matching is stable exactly when it has no blocking pair. There are three perfect matchings.

Choose any common reference order on the four names, and without loss of generality take \(1\prec2\prec3\prec4\). Independently for each person \(i\), first draw a permutation \(\sigma_i\) of **all four** names with probability \(q^{\operatorname{inv}(\sigma_i)}/Z_4(q)\), where \(\operatorname{inv}\) counts inversions against the common order, and

\[
Z_4(q)=(1+q)^2(1+q^2)(1+q+q^2).
\]

Then erase person \(i\) from their own sampled order. At \(q=0\), only the reference order can be sampled; at \(q=1\), every complete four-name order is equally likely. For \(q=0\), the convention \(0^0=1\) is used in the distribution. This full-order-then-delete construction is important: drawing a Mallows order directly on the three other names defines a **different** probability law, not asserted here. Relabeling the common reference order leaves the stated probability unchanged.

## Proof

**1. Unsolvable preference profiles.** Every person has \(3!=6\) possible final lists, hence there are \(6^4=1296\) final profiles. A finite exhaustive decision procedure tests each of the three perfect matchings against all four unmatched pairs. It finds exactly \(48\) unsolvable profiles. An independent structural representation identifies these as two disjoint orbits, each of size \(24\), under simultaneous relabeling of people and names. Representatives, with each row giving the preference order of the corresponding person, are

```
A: 1: 2 3 4     B: 1: 2 3 4
   2: 3 1 4        2: 3 1 4
   3: 1 2 4        3: 1 2 4
   4: 1 2 3        4: 1 3 2
```

For example, in profile A, the three candidate matchings are blocked respectively by the pairs \(\{2,3\}\), \(\{1,2\}\), and \(\{1,3\}\). The companion `verify.py` constructs all \(1296\) profiles by complete Cartesian enumeration, checks blocking pairs directly and confirms that the two full relabeling orbits equal **exactly** the set of all unsolvable profiles. This is a finite exhaustive proof, not a sampling claim; the source code explicitly specifies all loops and predicates.

**2. Full-order Mallows weights.** For each person \(i\) and final three-name list \(\tau\), define

\[
W_i(\tau;q)=\sum_{\substack{\sigma\in S_4\\\sigma\setminus\{i\}=\tau}}q^{\operatorname{inv}(\sigma)}.
\]

There are exactly four insertions of the deleted name into each \(\tau\), and therefore \(\sum_{\tau}W_i(\tau;q)=Z_4(q)\). Independence makes the probability of a final preference profile \((\tau_1,\ldots,\tau_4)\) equal to \(\prod_i W_i(\tau_i;q)/Z_4(q)^4\). Sum this weight over the \(48\) unsolvable profiles identified in step 1. Exact polynomial multiplication yields the coefficient array (ascending powers from zero through \(24\))

```
0,0,3,22,82,208,404,642,870,1038,1129,1162,1168,
1162,1129,1038,870,642,404,208,82,22,3,0,0
```

Its polynomial factorization is

\[
N(q)=q^2(1+q)^6(1+q^2)^2(1+q+q^2)
(3q^8+q^7+3q^6-2q^5+6q^4-2q^3+3q^2+q+3).
\]

Consequently \(\Pr_q(U)=N(q)/Z_4(q)^4\), which simplifies to the stated rational function. At \(q=1\), the numerator is \(12288\) and \(Z_4(1)^4=24^4=331776\), hence \(\Pr_1(U)=1/27\). The lowest nonzero coefficient is \(3q^2\), proving the sharp inversion threshold and small-dispersion expansion. The `verify_independent.cpp` program separately enumerates all \(24^4=331776\) full four-name draws, applies deletion, checks stability and independently reproduces all \(25\) coefficients.

**3. Unique interior maximum.** Differentiating the rational function gives

\[
\frac{d}{dq}\Pr_q(U)=\frac{2q(1-q)H(q)}{(1+q)^3(1+q^2)^3(1+q+q^2)^4},
\]

where

\[
H(q)=3q^{12}+3q^{11}-4q^{10}-30q^9-50q^8-71q^7-74q^6-71q^5-50q^4-30q^3-4q^2+3q+3.
\]

The coefficients of \(H\) are palindromic, so \(q^{12}H(1/q)=H(q)\) for positive \(q\). There are exactly two sign changes in its coefficient sequence; Descartes' rule of signs therefore gives at most two positive roots counted with multiplicity. Since \(H(0)=3\) and \(H(1)=-372\), there is a positive root in \((0,1)\); reciprocity supplies a distinct positive root beyond \(1\). These exhaust the positive roots and are simple. It follows that \(H\) changes sign once in \((0,1)\), from positive to negative, proving strict rise and fall of \(\Pr_q(U)\). Exact integer-rational evaluation gives \(H(379/1000)>0\) and \(H(380/1000)<0\), identifying the bracket for the unique maximum. The exact derivative identity is checked in `verify.py` using only integer polynomial arithmetic.

## Verification

Run `python3 verify.py` using Python 3 standard library; it prints `VERIFY_OK`. For the independent full-draw route run `c++ -O2 -std=c++17 verify_independent.cpp -o check && ./check` (requires a C++17 compiler); it prints `VERIFY_INDEPENDENT_OK`. The Python test enumerates all \(6^4\) three-name profiles, checks two complete unsolvable relabeling orbits, aggregates every four-name insertion into a polynomial and verifies numerator and derivative identities. The C++ test independently traverses \(24^4\) full-name draws and checks the entire inversion histogram. The derivative proof is algebraic for all real \(q\in[0,1]\), not inferred from numerical samples.

## Relationship to prior work

Chin and Michelen (2026) prove asymptotic unsolvability under independent **uniform** preferences. Young and Studebaker (2026) prove sharp asymptotics for the uniform solvability probability. Neither inspected work treats the full-order Mallows perturbation parameter or its nonmonotone small-market law. Boehmer, Heeger and Szufa (2022/2023) introduce the precise full-order-then-delete Mallows culture and report empirical studies of larger roommates instances; their inspected model and experiments do not provide the present exact probability or unique maximum. Glitzner and Manlove (2025) report Mertens' known uniform four-person solvability value \(26/27\), and examine other experimental preference cultures, but not this weighted four-person formula. A published four-person stable-roommates orbit census already gives the two unsolvable relabeling classes and the labeled count \(48\); those *structural counts* are prior work. The new claim is the exact Mallows-weighted law, quadratic low-noise rarity, and provable unique interior peak; it is not a claim to rediscover the two classes.

## Limitations

The result concerns exactly four people with complete strict preferences and independent full-order Mallows draws around one common reference order. No conclusion is established for six or more people, other correlated preference cultures, or a variant in which each person draws a Mallows permutation directly on just the other three names. The unique-peak location is algebraically specified and numerically approximated; only the rational bracket is claimed exactly. The literature comparison is based on the accessible inspected material, published research records and targeted searches; an unindexed equivalent analysis remains possible. Independent scientific audit has not been performed.

## References

1. B. Chin and M. Michelen, “The random stable roommates problem typically has no solution,” arXiv:2601.07612, first publicly submitted 2026-01-12, https://arxiv.org/abs/2601.07612.
2. C. Young and I. Studebaker, “Sharp Asymptotics for the Solvability Probability of Random Stable Roommates,” arXiv:2610.07741, first publicly submitted 2026-10-06, https://arxiv.org/abs/2610.07741.
3. N. Boehmer, K. Heeger and S. Szufa, “A Map of Diverse Synthetic Stable Roommates Instances,” arXiv:2208.04041 (2022); AAMAS 2023, https://arxiv.org/html/2208.04041v1.
4. F. Glitzner and D. Manlove, “Perspectives on Unsolvability in the Roommates Problem,” arXiv:2505.06717 (first public version 2025-05-10), https://arxiv.org/pdf/2505.06717.
5. “Stability-stratified isomorphism census for four-person stable roommates,” publicly available published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-stability-stratified-isomorphism-census-for-four-person-stable-r--0bfa73dccf63.
