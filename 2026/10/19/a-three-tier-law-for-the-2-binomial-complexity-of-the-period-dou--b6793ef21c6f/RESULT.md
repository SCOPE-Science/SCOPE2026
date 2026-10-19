# A three-tier law for the 2-binomial complexity of the period-doubling word

## Finding

Let \(p=0100010101000100\cdots\) be the fixed point starting in \(0\) of the substitution \(0\mapsto01\), \(1\mapsto00\). Define \(b_2(n)\) as the number of 2-binomial-equivalence classes among all contiguous length-\(n\) factors of \(p\). Two binary words are 2-binomially equivalent when every binary scattered subsequence of length at most two occurs with the same multiplicity.

**Theorem.** For every integer \(k\ge0\),
\[
b_2(3\cdot2^k)=2^{k+1}+k+3.
\]
More precisely, write \(n=3\cdot2^k\) and associate to each length-\(n\) factor \(w\) the signature \((z(w),t(w))\), where \(z(w)\) is the number of zeros and \(t(w)=\binom{w}{01}\) is the number of scattered `01` subsequences. Exactly three zero counts occur: \(2^{k+1}-1\), \(2^{k+1}\), and \(2^{k+1}+1\). The two outer zero-count classes contain exactly \(2^k\) different signatures each. The middle zero-count class contains exactly \(k+3\) signatures, and its \(t\)-coordinates form a nonempty arithmetic progression with common difference \(2^k\).

## Assumptions and scope

All counts are over the binary alphabet and refer to contiguous factors occurring anywhere in the one-sided infinite word, not merely inside a selected finite prefix. Within each factor, the coefficient \(\binom{w}{v}\) counts scattered subsequences of pattern \(v\), including all choices of positions. The assertion includes \(k=0\) and every larger integer. It does not assert a formula for lengths outside \(3\cdot2^k\).

## Proof

**Signatures suffice.** For a fixed binary length \(m\), put \(z=\binom{w}{0}\) and \(t=\binom{w}{01}\). Then \(\binom{w}{1}=m-z\), \(\binom{w}{00}=\binom z2\), \(\binom{w}{11}=\binom{m-z}2\), and \(\binom{w}{10}=z(m-z)-t\). Hence the complete degree-at-most-two binomial data are equivalent to \((z,t)\).

**Substitution lift.** The period-doubling fixed point satisfies \(p_{2j}=0\) and \(p_{2j+1}=1-p_j\) at each position \(j\ge0\). For any length-\(m\) factor \(u=u_0\cdots u_{m-1}\), set \(q_j=1-u_j\), and form
\[
A(u)=0q_0\,0q_1\cdots0q_{m-1},\qquad B(u)=q_00\,q_10\cdots q_{m-1}0.
\]
Every length-\(2m\) factor is of exactly one of these forms (according to the parity of its starting position). Conversely, for every occurrence of \(u\), both lifted factors occur at the corresponding even and odd positions, so the collection of length-\(2m\) factors equals the union of all these lifts.

If \((z,t)\) is the signature of \(u\), then both lifts have \(2m-z\) zeros. Counting for each one of the complemented word the preceding inserted zeros and preceding complemented zeros gives
\[
T_B=\binom z2+2\bigl(z(m-z)-t\bigr),\qquad T_A=T_B+z.
\]
Indeed, the number of complementary zeros preceding complementary ones is \(\binom{u}{10}=z(m-z)-t\); the sum of the positions of complementary ones is \(\binom z2+\binom{u}{10}\). These two contributions yield \(T_B\); the additional \(z\) preceding separator zeros yield \(T_A\). The formulas depend only on the old signature and therefore apply directly to sets of signatures, without requiring a bijection of individual factors.

**Base.** All length-three factors are `000`, `001`, `010`, `100`, and `101`. The pairs \((z,t)\) are \((3,0)\), \((2,2)\), \((2,1)\), \((2,0)\), and \((1,1)\), respectively. Thus the zero counts \(1,2,3\) have sizes \(1,3,1\), and the central \(t\)-set is \(\{0,1,2\}\).

**Induction.** Suppose the three-tier assertion holds for \(m=3\cdot2^k\), and write \(r=2^{k+1}\). The substitution lift changes each old zero count \(z\) to \(2m-z\). The old three counts \(r-1,r,r+1\) therefore become the three counts \(2^{k+2}+1,2^{k+2},2^{k+2}-1\), in reverse order, with no interference between tiers.

In either outer tier, \(z\) is odd. For fixed \(z\), both maps \(t\mapsto T_B\) and \(t\mapsto T_A\) are injective. Their images are disjoint because \(T_B\) has a fixed parity for fixed \(z\), whereas \(T_A=T_B+z\) has the opposite parity. Thus the number of signatures in either outer tier doubles from \(2^k\) to \(2^{k+1}\).

In the middle tier, \(z=r=2^{k+1}\) is even and the old values of \(t\) form an arithmetic progression of length \(k+3\) and step \(2^k=z/2\). The \(T_B\) images form an arithmetic progression of length \(k+3\) and step \(z\); the \(T_A\) images are exactly a translate of that progression by one step \(z\). Their union is one progression of length \(k+4\) and step \(z=2^{k+1}\). This proves the middle tier and completes the induction. Adding the three tier sizes gives \(2\cdot2^k+(k+3)\), the stated formula. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the period-doubling word independently by substitution and by the parity of the 2-adic valuation of the position-plus-one. It enumerates all length-\(3\cdot2^k\) factors in a length-\(32768\) prefix for \(0\le k\le8\), computes signatures directly, and compares them to an independent factor-lifting recurrence. It checks the three exact tier sizes, the middle arithmetic progression, and the total formula, returning `VERIFY_OK`. The proof above, not these finite tests, establishes the infinite claim. Run with `python3 verify.py`.

## Relationship to prior work

Binomial equivalence and binomial complexity were introduced by Rigo and Salimov (2013); their treatment covers Sturmian and Thue–Morse words but does not evaluate period-doubling factors. The 2-abelian complexity of the period-doubling word studied by Parreau, Rigo, Rowland, and Vandomme (2015) uses contiguous-factor frequencies, a different invariant. Lejeune's thesis (2021, Section 4.5, pp. 115–116) proves that period-doubling 2-binomial complexity coincides with factor complexity precisely at powers of two, exhibits finite numerical data for lengths up to 70, and explicitly states that the full 2-binomial complexity could not be precisely computed. The theorem here gives an exact infinite **non-dyadic** ray and the complete signature-tier structure; it does not claim the already-known dyadic result. Published computational data for finitely many lengths are not an infinite proof.

## Limitations

The result covers only lengths \(3\cdot2^k\), not an arbitrary-length closed form. The source comparisons do not exclude equivalent theorems in unindexed work. The provided experimental verification is finite and not a machine-checked proof of the induction.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, 217–228; openly accessible extended preprint, https://orbi.uliege.be/handle/2268/149313 (publicly available 2013-05-27).
2. A. Parreau, M. Rigo, E. Rowland and E. Vandomme, *A New Approach to the 2-Regularity of the ℓ-Abelian Complexity of 2-Automatic Sequences*, Electronic Journal of Combinatorics 22 (2015), #P1.27, https://orbi.uliege.be/handle/2268/178495.
3. M. Lejeune, *On the k-binomial equivalence of finite words and k-binomial complexity of infinite words*, doctoral thesis, Université de Liège (2021), Section 4.5, https://orbi.uliege.be/handle/2268/259266.
