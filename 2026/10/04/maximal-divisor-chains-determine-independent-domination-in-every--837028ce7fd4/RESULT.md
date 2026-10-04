# Maximal divisor chains determine independent domination in every cozero-divisor graph \(\Gamma'(\mathbb Z_n)\)

## Finding

For every composite integer \(n=\prod_{i=1}^r p_i^{a_i}\), independent dominating sets of \(\Gamma'(\mathbb Z_n)\) are in bijection with maximal chains of the poset of nontrivial proper divisors of \(n\): a chain \(C\) corresponds to the union of the gcd-cells \(A_d=\{x\in\mathbb Z_n:\gcd(x,n)=d\}\) for \(d\in C\). Equivalently, if \(\mathcal W(n)\) is the set of distinct words \((q_1,\ldots,q_\Omega)\) formed from the prime multiset of \(n\), then \(D_i(\Gamma'(\mathbb Z_n),z)=\sum_{q\in\mathcal W(n)}z^{\sum_{j=1}^{\Omega-1}\varphi(q_{j+1}\cdots q_\Omega)}\). Thus the number of independent dominating sets is \(\Omega!/(a_1!\cdots a_r!)\); ordering prime factors nonincreasingly minimizes the exponent and ordering them nondecreasingly maximizes it, giving exact formulas for \(\gamma_i\) and \(\alpha\).

Writing the distinct primes in increasing order \(p_1<\cdots<p_r\) and \(\Omega=\sum_i a_i\), the extremal exponents are
\[\gamma_i(\Gamma'(\mathbb Z_n))=p_1^{a_1-1}-1+\sum_{t=2}^r p_t^{a_t-1}\varphi\!\left(\prod_{i<t}p_i^{a_i}\right).\]
and
\[\alpha(\Gamma'(\mathbb Z_n))=p_r^{a_r-1}-1+\sum_{t=1}^{r-1} p_t^{a_t-1}\varphi\!\left(\prod_{i>t}p_i^{a_i}\right).\]
For a prime power this specializes to \(\gamma_i=\alpha=p_1^{a_1-1}-1\).

## Assumptions and scope

The cozero-divisor graph \(\Gamma'(\mathbb Z_n)\) has the nonzero nonunits of \(\mathbb Z_n\) as vertices. Distinct vertices \(x,y\) are adjacent precisely when neither principal ideal contains the other. For every nontrivial proper divisor \(d\mid n\), define
\[
A_d=\{x\in\mathbb Z_n:\gcd(x,n)=d\}.
\]
Then \(|A_d|=\varphi(n/d)\). The standard divisor-cell description says that each \(A_d\) is independent and that every vertex of \(A_d\) is adjacent to every vertex of \(A_e\) exactly when \(d\) and \(e\) are incomparable under divisibility.

The theorem concerns every composite \(n\). No assertion is made for prime \(n\), where the graph has no vertices.

## Proof

Let \(S\) be an independent dominating set and put
\[
C=\{d: S\cap A_d\ne\varnothing\}.
\]
Since edges between distinct gcd-cells are complete exactly for incomparable divisor labels, independence of \(S\) forces every two members of \(C\) to be comparable; hence \(C\) is a chain.

Moreover, if \(S\cap A_d\) were a nonempty proper subset of some cell \(A_d\), then an unchosen vertex of that same cell would have no neighbor in \(S\). It has no neighbor inside \(A_d\), and it has no neighbor in any other selected cell because all labels in \(C\) are comparable with \(d\). Therefore every selected cell is selected in full:
\[
S=\bigcup_{d\in C}A_d.
\]

The chain \(C\) must be maximal in the poset of nontrivial proper divisors. If an outside divisor \(e\) were comparable with every element of \(C\), then \(C\cup\{e\}\) would still be a chain and every vertex of \(A_e\) would be undominated. Conversely, if \(C\) is maximal, every outside label \(e\) is incomparable with some \(d\in C\), so the complete bipartite adjacency between \(A_e\) and \(A_d\) dominates all of \(A_e\). Thus independent dominating sets are exactly the full-cell unions indexed by maximal chains.

A maximal divisor chain extends uniquely to a saturated chain
\[
1=d_0<d_1<\cdots<d_\Omega=n
\]
whose successive quotients are prime. Hence it is equivalent to a distinct ordering \((q_1,\ldots,q_\Omega)\) of the prime multiset of \(n\), with \(d_j=q_1\cdots q_j\). Its independent dominating set has size
\[
\sum_{j=1}^{\Omega-1}|A_{d_j}|
=\sum_{j=1}^{\Omega-1}\varphi\!\left(\frac n{d_j}\right)
=\sum_{j=1}^{\Omega-1}\varphi(q_{j+1}\cdots q_\Omega).
\]
Summing one monomial for each distinct prime word gives the stated polynomial. The number of distinct words is the multinomial coefficient
\[
\frac{\Omega!}{a_1!\cdots a_r!}.
\]

It remains to identify the minimum and maximum word weights. Consider adjacent distinct primes \(a<b\) followed by a fixed suffix product \(T\). Swapping \(a,b\) to \(b,a\) changes exactly one suffix contribution, from \(\varphi(bT)\) to \(\varphi(aT)\). Directly from Euler's product formula,
\[
\varphi(aT)\le\varphi(bT)
\]
for \(a<b\), whether neither, one, or both primes already divide \(T\). Therefore bubbling larger primes left never increases the weight, while bubbling smaller primes left never decreases it. The descending prime word minimizes and the ascending prime word maximizes.

For the descending word, group equal prime blocks and use
\[
\sum_{e=0}^{a-1}\varphi(p^e)=p^{a-1}.
\]
This yields the displayed formula for \(\gamma_i\). Applying the same calculation to the ascending word gives the formula for \(\alpha\).

## Verification

The standalone `verify.py` independently reconstructs the divisor-cell poset and the actual cozero-divisor graph for small moduli. It exhaustively enumerates all vertex subsets for \(n\in\{4,6,8,10,12,14,15,18,20\}\) and confirms that the independent dominating sets are exactly the full gcd-cell unions arising from maximal divisor chains.

It also enumerates distinct prime-multiset words for 28 composite moduli through \(180\), checks their weight polynomials against maximal-chain enumeration whenever the divisor poset is small enough, and verifies the ascending/descending extremal formulas. In particular it reproduces the published examples
\[
D_i(\Gamma'(\mathbb Z_{30}),z)=z^3+z^4+z^5+z^8+z^{10}+z^{12}
\]
and
\[
D_i(\Gamma'(\mathbb Z_{48}),z)=4z^{15}+z^{16}.
\]

The exact script output is:

```text
VERIFY_OK
direct_graph_checks=n in {4,6,8,10,12,14,15,18,20}
word_chain_checks=28 composite moduli through 180
Z30_polynomial=z^3+z^4+z^5+z^8+z^10+z^12
Z48_polynomial=4z^15+z^16
```

The computations are finite stress tests only. The arbitrary-\(n\) statement follows from the chain characterization and adjacent-swap argument above.

## Relationship to prior work

Afkhami and Khashyarmanesh introduced the cozero-divisor graph of a commutative ring and established the principal-ideal viewpoint. Rather's 2024 paper partitions \(\Gamma'(\mathbb Z_n)\) into the same gcd-cells, records their sizes \(\varphi(n/d)\), and uses the fact that two cells are completely adjacent exactly when their divisor labels are incomparable. It then computes the independent domination polynomial for selected factorizations, including \(p_1p_2\), \(p_1p_2p_3\), and \(p_1^{a}p_2\).

The 2024 conclusion explicitly says that the polynomial had been determined only for special values and that the general-\(n\) problem remained difficult. The present theorem turns the divisor-cell structure into a maximal-chain bijection, which supplies a closed expression for every composite \(n\), the exact number of independent dominating sets, and the two extremal exponents. A 2026 follow-up on zeros still analyzes the biprime, triprime, and \(p^a q\) regimes rather than stating the maximal-chain formula for arbitrary \(n\).

## Limitations

The polynomial is expressed as a weighted sum over multiset prime-factor orderings. This is an exact finite formula, but it is not generally compressed into coefficients indexed by exponent without collecting equal weights.

The originality comparison relied on the full text of the 2024 paper and the abstract of the 2026 follow-up; the latter full text was not publicly available in the sources inspected. An unindexed note could independently contain the same maximal-chain observation.

The result concerns the cozero-divisor graph of \(\mathbb Z_n\), not arbitrary finite commutative rings.

## References

1. M. Afkhami and K. Khashyarmanesh, “The cozero-divisor graph of a commutative ring,” *Southeast Asian Bulletin of Mathematics* 35 (2011), 753–762.
2. B. A. Rather, “Independent domination polynomial for the cozero divisor graph of the ring of integers modulo \(n\),” *Discrete Mathematics Letters* 13 (2024), 36–43. DOI: 10.47443/dml.2023.215. Published online 4 April 2024.
3. B. A. Rather, “Zeros of the independent domination polynomial of the cozero divisor graphs of ring \(\mathbb Z_n\),” *Siberian Mathematical Journal* (2026).
