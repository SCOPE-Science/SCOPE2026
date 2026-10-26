# The exact four-world law for finite-valued max–min fuzzy preorders

## Finding
On four distinct labelled worlds, choose a linearly ordered set of \(q\) membership values, where \(q\ge1\) is an integer. Fix every diagonal value to the greatest membership value and choose the twelve off-diagonal values freely. The number of resulting max–min transitive fuzzy relations is exactly

\[
F_4(q)=\frac{q(160q^8+1206q^7+3156q^6+1134q^5-8736q^4+4914q^3+974q^2-639q-279)}{1890}.
\]

For example, \(F_4(1)=1\), \(F_4(2)=355\), \(F_4(3)=9040\), \(F_4(4)=89786\), and \(F_4(5)=541667\). If the off-diagonal entries are independent uniform draws from the membership levels, then

\[
\Pr(\text{max--min transitive})=\frac{F_4(q)}{q^{12}}=\frac{16}{189q^3}+O(q^{-4})\quad(q\to\infty).
\]

This determines the first four-world, multi-level exact acceptance probability for direct random generation of transitively consistent fuzzy relations. It is distinct from determining a transitive closure *after* a matrix has been drawn.

## Assumptions and scope
The universe is the fixed labelled set \(W=\{1,2,3,4\}\). Let \(L_q=\{\lambda_0<\cdots<\lambda_{q-1}\}\subseteq[0,1]\) be any strictly ordered set of \(q\) real membership levels, with \(\lambda_{q-1}=1\). A relation \(R:W\times W\to L_q\) is reflexive when \(R(i,i)=1\) for each world. It is max--min transitive exactly when

\[
R(i,k)\ge\min\{R(i,j),R(j,k)\}\qquad (i,j,k\in W).
\]

The theorem counts *labelled matrices*, not isomorphism classes. Neither symmetry nor antisymmetry is assumed. The probability assertion uses independent uniform draws only for the twelve off-diagonal entries. The values \(\lambda_j\) matter through their order alone.

## Proof
**Step 1: Convert each matrix into a multichain of crisp preorders.** Number the membership levels by \(0,\ldots,q-1\), retaining their order. For each \(s\in\{1,\ldots,q-1\}\), define its threshold relation \(P_s\) on \(W\) by \(iP_sj\) iff \(R(i,j)\ge\lambda_s\). The diagonal is present at every threshold. The displayed max--min inequality is equivalent to *every* \(P_s\) being a reflexive transitive relation (a preorder). Indeed, if two edges lie in a threshold cut, their composite must lie there; conversely, if the inequality failed, choosing the lower of the two antecedent membership levels as a threshold yields a violated crisp transitivity implication. The thresholds form an ordered multichain

\[
P_1\supseteq P_2\supseteq\cdots\supseteq P_{q-1}.
\]

Every such multichain conversely determines exactly one fuzzy matrix, by assigning to each off-diagonal pair the greatest threshold in which it occurs (or the least value if it occurs in none). For \(q=1\) the empty multichain corresponds to the unique all-ones matrix.

**Step 2: Express the exact count through strict chains.** Write \(\Delta\) for the diagonal-only preorder, and let \(a_k\) denote the number of *strict* length-\(k\) inclusion chains of nonidentity preorders on four labelled elements, with \(a_0=1\). Selecting the \(k\) distinct positive threshold levels at which the multichain changes and then the strictly nested preorders gives a bijection, so

\[
F_4(q)=\sum_{k\ge0}a_k\binom{q-1}{k}.
\]

For completeness, there are no nonidentity strict chains longer than nine: for any preorder \(P\), let \(c(P)\) be the number of unordered pairs of different points comparable in at least one direction, and let \(e(P)\) be the number of equivalence classes for \(i\sim_Pj\) iff both directions hold. The integer \(c(P)+4-e(P)\) strictly increases under proper inclusion of preorders and lies between zero and nine. A newly related pair either creates a new comparable unordered pair or joins two equivalence classes. Thus the sum terminates at \(k=9\).

**Step 3: Exhaustively certify the ten integer coefficients.** Encode each off-diagonal crisp relation by its twelve-bit mask. Iterate over *every* one of the \(2^{12}=4096\) masks; include the four diagonal pairs and test all \(4^3=64\) instances of crisp transitivity. Exactly \(355\) masks are preorders. For each nonzero preorder mask \(P\), initialize \(b_1(P)=1\) and recursively compute

\[
b_{k+1}(P)=\sum_{\substack{Q\ne\Delta\\Q\subsetneq P}}b_k(Q),\qquad a_k=\sum_{P\ne\Delta}b_k(P).
\]

All sums range over the finite, explicitly enumerated masks. The resulting complete coefficient vector \((a_0,\ldots,a_9)\) is

\[
(1,354,8331,63730,235344,488760,604752,444192,179328,30720).
\]

The included standalone `checker.py` implements exactly these finite loops and independently cross-checks the three-valued case by enumerating pairs of nested crisp preorders. Substituting these coefficients in the finite binomial sum and collecting terms gives the stated rational polynomial. The checker verifies the identity at ten distinct integer inputs; as both polynomials have degree at most nine, these evaluations independently verify the algebraic identity over the rationals. Its exact enumeration and recurrence provide a terminating exhaustive certificate for the integer coefficients, rather than finite sampling.

**Step 4: Derive the probability.** There are exactly \(q^{12}\) independently selectable off-diagonal assignments. The polynomial's leading term is \((16/189)q^9\), hence division by \(q^{12}\) gives the exact probability and asymptotic expression.

## Verification
From a fresh copy of this package, run `python3 checker.py`. The code requires only standard Python and enumerates all \(4096\) crisp masks. It reports the entire strict-chain coefficient vector, the values of \(F_4(q)\) for \(1\le q\le5\), and `ALL_CHECKS_OK`. An additional comparison enumerates all \(355^2\) nested pairs of binary-cut preorders for \(q=3\). The checker also independently brute-forces three-world fuzzy matrices for \(1\le q\le5\), checking its threshold-chain interpretation in a smaller system. It does not attempt to count arbitrary-size fuzzy matrices.

## Relationship to prior work
Li, Yu and Liu study Bernoulli and continuous probabilistic models for *max--min transitive closure* of random fuzzy matrices, with distributional and algorithmic results. Their work motivates distinguishing an input matrix that already obeys max--min transitivity from its closure; the exact four-world \(q\)-level fixed-point acceptance polynomial above is not among the examined formulas. Moerman previously determined the maximum length of chains in the finite preorder lattice. That established length bound explains the degree ceiling here and is **not claimed as a new result**. Earlier work by Erné and Reinhold studies heights of quasiorder-lattice intervals. The new assertion is the full four-world enumeration of all strict chains and its exact acceptance law, not the previously known chain height or the standard cut representation. Ferrari and coauthors independently motivate finite fuzzy accessibility matrices for Gödel modal semantics, but do not assert this combinatorial enumeration.

## Limitations
The count fixes the diagonal to the greatest level and treats worlds as labelled. It does not count symmetric fuzzy equivalences, models up to relabelling, arbitrary diagonal values, non-min transitive t-norms, or random outputs of the closure operation. Four-world coefficients were produced by finite exhaustive computation; they do not provide a closed formula for five or more worlds. The manuscript does not claim that the known strict-chain method or maximal preorder-chain length is novel. A prior full census of multichains of the four-world preorder lattice under another terminology is a remaining priority risk. No independent external audit has been performed.

## References
- N. Li, X. Yu, W. Liu, “Max–Min Transitive Closure of Randomly Generated Fuzzy Matrix: Bernoulli and Classical Probabilistic Models,” *Axioms* **14** (2025), article 690, DOI: 10.3390/axioms14090690. First public date verified here: 2025-09-11.
- J. Moerman, “Chains of Preorders,” 2022-08-26, https://joshuamoerman.nl/2022/8/Chains-of-Preorders.html.
- M. Erné, J. Reinhold, “Intervals in lattices of quasiorders,” *Order* **12** (1995), 375–403, DOI: 10.1007/BF01110380.
- M. Ferrari, C. Fiorentini, P. Giardini, R. O. Rodriguez, “A Gödel Modal Logic Over Witnessed Models,” arXiv:2606.31906, first posted 2026-06-30.
