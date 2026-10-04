# Two minimal counterexamples to a published Carmichael-function formula, with a downstream repair

## Finding
Lebowitz-Lockard and Saunders state in Theorem 2 of *Runs of integers with constant values of the Carmichael function* that, for every positive integer \(n\),
\[
\lambda(n)=
\begin{cases}
\varphi(n),&8\nmid n,\\
\varphi(n)/2,&8\mid n.
\end{cases}
\]
Both branches fail.

The least counterexample to the first branch is \(n=12\):
\[
\lambda(12)=\operatorname{lcm}(\lambda(4),\lambda(3))
=\operatorname{lcm}(2,2)=2,
\qquad
\varphi(12)=4.
\]
The least counterexample to the second branch is \(n=24\):
\[
\lambda(24)=\operatorname{lcm}(\lambda(8),\lambda(3))
=\operatorname{lcm}(2,2)=2,
\qquad
\varphi(24)/2=4.
\]

A correct replacement is the standard formula. If
\[
n=\prod_{j=1}^{r}p_j^{a_j},
\]
then
\[
\lambda(n)=\operatorname{lcm}_{1\le j\le r}\lambda(p_j^{a_j}),
\]
where
\[
\lambda(p^a)=p^{a-1}(p-1)
\]
for odd primes \(p\), while
\[
\lambda(2)=1,\qquad \lambda(4)=2,\qquad
\lambda(2^a)=2^{a-2}\quad(a\ge3).
\]

The published proof of Theorem 3 does not need the false two-branch identity. Its Carmichael-specific step is that if \(p\mid m\) is prime, then \(p-1\mid\lambda(m)\); this follows immediately from the prime-power least-common-multiple formula. Thus replacing Theorem 2 by the correct formula preserves the displayed proof of Theorem 3.

## Assumptions and scope
The claim concerns the definition of the Carmichael function used by the paper: \(\lambda(n)\) is the exponent of the unit group modulo \(n\), equivalently the least positive integer \(m\) such that \(a^m\equiv1\pmod n\) for every \(a\) coprime to \(n\).

The earliest public version of the paper is arXiv:2402.06832v1, dated 9 February 2024. The same incorrect Theorem 2 remains in the version published in *Integers* 24 (2024). The correction here is to Theorem 2 and to its role in the exposition. It does not claim a new formula for the Carmichael function; the prime-power least-common-multiple formula is classical.

## Proof
For \(n=12=2^2\cdot3\), the standard prime-power values give
\[
\lambda(4)=2,\qquad \lambda(3)=2.
\]
Therefore
\[
\lambda(12)=\operatorname{lcm}(2,2)=2,
\]
whereas \(\varphi(12)=4\). Since \(8\nmid12\), this contradicts the first branch.

To see minimality, check the positive integers \(n<12\) with \(8\nmid n\). For
\[
n\in\{1,2,3,4,5,6,7,9,10,11\},
\]
the standard formula gives \(\lambda(n)=\varphi(n)\). The only omitted value below \(12\) is \(8\), which belongs to the other branch. Hence \(12\) is the least counterexample to the first branch.

For \(n=24=2^3\cdot3\),
\[
\lambda(8)=2,\qquad \lambda(3)=2,
\]
so
\[
\lambda(24)=\operatorname{lcm}(2,2)=2.
\]
But \(\varphi(24)=8\), hence \(\varphi(24)/2=4\). Since \(8\mid24\), this contradicts the second branch.

For minimality in the second branch, the only positive multiples of \(8\) below \(24\) are \(8\) and \(16\). The standard formula gives
\[
\lambda(8)=2=\varphi(8)/2
\]
and
\[
\lambda(16)=4=\varphi(16)/2.
\]
Thus \(24\) is the least counterexample to the second branch.

Finally, let \(p^a\parallel m\). If \(p\) is odd, then
\[
p-1\mid \lambda(p^a)\mid\lambda(m).
\]
For \(p=2\), the assertion \(p-1\mid\lambda(m)\) is trivial. Therefore
\[
p-1\mid\lambda(m)
\]
for every prime divisor \(p\) of \(m\). In the published proof of Lemma 3, this is precisely the Carmichael-function implication used after selecting \(p\parallel n+i\). The remainder of Lemma 3 and the deduction of Theorem 3 use that divisibility and the preceding shifted-prime estimate, not the false case split of Theorem 2. Replacing Theorem 2 by the standard formula therefore leaves that proof intact.

## Verification
The accompanying `verify.py` implements the classical prime-power least-common-multiple formula using exact integer arithmetic. It checks all positive integers below the two claimed thresholds, confirms that \(12\) and \(24\) are the first failures of their respective branches, and prints `VERIFY_OK`.

The downstream implication \(p-1\mid\lambda(m)\) is proved symbolically above from the same formula; no finite computation is used as a substitute for that argument.

## Relationship to prior work
The paper attributes its Theorem 2 to Carmichael's computation of \(\lambda\), but the printed two-branch statement is not the classical formula. Standard references give the prime-power least-common-multiple formula instead. The *Integers* publication, dated 9 October 2024, retains the same two-branch Theorem 2.

Targeted searches for the paper title, arXiv identifier, theorem number, the two minimal counterexamples, and combinations of “correction” and “erratum” did not locate an indexed correction of this statement. Semantic searches of the published-finding corpus mathematical record likewise did not return a finding about this error. The originality claim is therefore only that the specific published misstatement, its least counterexamples in both branches, and the downstream dependency check were not located in the searched literature; the underlying Carmichael formula is classical.

## Limitations
A failed literature search is not a proof that no correction exists. An author communication, unindexed note, or later erratum could already contain the same observation.

The downstream statement is deliberately narrow: it verifies that the displayed proof of Theorem 3 survives replacement of Theorem 2 because the needed divisibility follows from the correct formula. It does not independently reprove every external analytic input used in Theorem 3.

## References
1. N. Lebowitz-Lockard and J. C. Saunders, “Runs of integers with constant values of the Carmichael function,” arXiv:2402.06832, first posted 9 February 2024.
2. N. Lebowitz-Lockard and J. C. Saunders, “Runs of integers with constant values of the Carmichael function,” *Integers* 24 (2024), Article A91, DOI 10.5281/zenodo.13909203.
3. E. W. Weisstein, “Reduced Totient Function,” MathWorld, giving the standard prime-power least-common-multiple formula for the Carmichael function.
4. R. D. Carmichael, “Note on a new number theory function,” *Bulletin of the American Mathematical Society* 16 (1910), 232–238.
