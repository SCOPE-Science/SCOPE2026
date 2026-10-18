# Six is the least prime-support size for odd squarefree strongly pseudoperfect integers

## Finding
A positive integer \(n\) is **strongly pseudoperfect** if there is a set \(S\) of positive divisors of \(n\) such that
\[
 d\in S\quad\Longleftrightarrow\quad n/d\in S,
 \qquad \sum_{d\in S}d=2n.
\]
Every **odd squarefree** strongly pseudoperfect integer \(n\) has at least six distinct prime divisors. This lower bound is attained by
\[
 n=937365=3\cdot5\cdot11\cdot13\cdot19\cdot23.
\]
The assertion is about the minimum *number of distinct prime factors*, not the least such integer by numerical value.

## Assumptions and scope
All integers, divisors and primes are positive; \(n>1\). Squarefree means that no square of a prime divides \(n\), so the number \(\omega(n)\) of distinct prime factors equals the total number of prime factors counted with multiplicity. The conclusion is **\(\omega(n)\ge6\)** under the conjunction of oddness, squarefreeness, and strongly pseudoperfectness. It does not assert the same minimum for odd integers with repeated prime factors.

## Proof
**1. Abundancy bounds.** Let \(p_1<\cdots<p_k\) be the distinct odd prime factors. Since the selected positive divisors sum to \(2n\), necessarily
\[
 \frac{\sigma(n)}n=\prod_{j=1}^{k}\left(1+\frac1{p_j}\right)\ge2.
\]
The product decreases as any prime increases. For \(k\le4\), it is bounded above by
\[
 \frac43\frac65\frac87\frac{12}{11}=\frac{768}{385}<2.
\]
Thus \(k\ge5\). If \(k=5\), the three smallest prime factors must be \(3,5,7\): otherwise one of the ordered prime-tuples \((5,7,11,13,17)\), \((3,7,11,13,17)\), and \((3,5,11,13,17)\) gives an upper bound below \(2\). The increasing fourth and fifth primes therefore have the form \(r<s\). The tuple \((3,5,7,23,29)\) also has abundancy below \(2\), hence
\[
 r\in\{11,13,17,19\}.
\]
The necessary inequality
\[
 192(r+1)(s+1)\ge210rs
\]
is equivalent, for these four values of \(r\), to
\[
 s\le\left\lfloor\frac{64(r+1)}{6r-64}\right\rfloor.
\]
Consequently the four complete upper bounds for \(s\), indexed by \(r=11,13,17,19\), are respectively \(384,64,30,25\). Enumeration of primes \(s>r\) in precisely these bounded ranges leaves \(71,12,3,1\) choices: \(87\) in total.

**2. The modulus-four exclusion.** If an odd integer \(n\equiv3\pmod4\), the two divisors in each complementary pair \((d,n/d)\) are one congruent to \(1\) and the other to \(3\pmod4\). Each pair sum is divisible by \(4\), whereas \(2n\equiv2\pmod4\). No union of complementary pairs can have sum \(2n\). Discarding these cases leaves respectively \(37,6,1,1\) pairs \((r,s)\), totaling **45**, with \(n\equiv1\pmod4\).

**3. Complete finite exclusion of five-prime support.** For each of the remaining candidates put
\[
 n=105rs,\qquad \Delta=\sigma(n)-2n
 =192(r+1)(s+1)-210rs.
\]
The integer \(n\) is squarefree and not a square. Its \(32\) divisors form exactly \(16\) disjoint complementary pairs, with weights
\[
 w_d=d+\frac nd,\qquad d\mid n,\quad d<\sqrt n.
\]
A strongly pseudoperfect representation exists if and only if some subset of these **16** pair weights sums exactly to \(\Delta\): one omits that union of pairs from the full divisor set. There is no condition on the size of the omitted subset. The executable `certificate.py` constructs every pair exactly, uses integer subset-sum recursion implemented as a finite-state dictionary, and finds **no** solution in all 45 cases. An independent `independent_check.py` uses a prime sieve, combinations of prime factors to build the divisors, and a bitset of reachable sums; it independently obtains exactly the same 45 unsatisfiable cases. Each computation is finite and exhaustive because the prime ranges in Step 1 are proved bounds, and each reachable-sum update considers both including and excluding the corresponding pair. This rules out \(k=5\), without an unproved infinite-search assumption.

**4. Sharpness.** All six displayed factors of \(937365\) are distinct primes. Its divisor sum is
\[
 \sigma(937365)=(4)(6)(12)(14)(20)(24)=1935360,
\]
so \(\Delta=\sigma(n)-2n=60630\). The following five complementary divisor pairs are disjoint:
\[
 (55,17043),\quad(57,16445),\quad(65,14421),
 \quad(143,6555),\quad(165,5681).
\]
Each pair multiplies to \(n\); their ten entries sum to exactly \(60630\). Thus the set of **all divisors of \(n\) except these ten** is closed under complementation and sums to \(1935360-60630=1874730=2n\). This proves strong pseudoperfectness and sharpness.

## Verification
Using Python 3, run `python certificate.py` and `python independent_check.py` in the directory containing these two files. Both require only the Python standard library and use exact integers and rational numbers. The first certificate confirms the four abundancy upper-bound examples, all 87 prime candidates, all 45 modulus-four survivors, the impossibility of each finite pair-subset sum, and the six-prime witness. The independent checker recreates the candidate list through an Eratosthenes sieve and repeats the 45 pair-subset tests using a different algorithm. Both were executed successfully. The scripts do not stand in place of Steps 1–2 proving that all possible five-prime integers have entered the finite test.

## Relationship to prior work
Wang and Zelinsky, *Strongly Pseudoperfect Numbers* (2026), define the property, study constraints on possible representations, and provide the six-prime odd squarefree example \(937365\) in their discussion of primitive strongly pseudoperfect numbers. Their Proposition 3 provides the congruence exclusion used in Step 2, while Propositions 15–17 bound the omitted-divisor excess under additional hypotheses. The present claim is the complementary **sharp support lower bound**: no odd squarefree strongly pseudoperfect number with five or fewer distinct primes exists. The six-prime witness itself is credited to Wang and Zelinsky, rather than claimed as new.

McCormack and Zelinsky (2023; updated 2026) introduced and studied the same strongly pseudoperfect property and its modulus-four restriction. Their general criteria do not classify the odd squarefree five-prime layer. The OEIS list A334405 is an enumerative record of individual integers and does not itself establish the unrestricted five-prime exclusion. The proof does not rely on any claimed uniqueness of the displayed witness.

## Limitations
The finite exclusion has been independently implemented but has not undergone an independent mathematical audit. No assertion is made about the smallest **numerical value** of an odd squarefree strongly pseudoperfect integer, the number of such integers, their density, or the minimum number of prime factors for odd nonsquarefree strongly pseudoperfect integers. Earlier unindexed computations or less explicit corollaries might establish the five-prime exclusion; this cannot be ruled out by searching alone.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v2 (2026), https://arxiv.org/abs/2609.36068, especially Proposition 3, Propositions 15–17, and the paragraph on \(937365\) in Section 4.
2. Tim McCormack and Joshua Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661v4 (2026 revision), https://arxiv.org/abs/2312.11661, Section on strongly pseudoperfect numbers, including Proposition 36.
3. OEIS Foundation, sequence A334405, *Strongly pseudoperfect numbers*, https://oeis.org/A334405.
