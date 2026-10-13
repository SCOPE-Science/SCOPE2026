# An exact interpretability profile for the order-\(840\) class-transposition pair
## Finding
Let
\[
a=\tau_{0(40),18(28)},\qquad b=\tau_{4(42),5(15)},\qquad T=a\circ b,
\]
where \(b\) is applied first. For the structurally admissible words in the eight-letter language used by Iskra, the exact interpretation profile through the decisive length \(7\) is
\[
\begin{array}{c|rrrrrrr}
n&1&2&3&4&5&6&7\\ \hline
\text{all structurally admissible}&8&16&32&64&128&256&512\\
\text{integer-interpretable}&8&8&8&6&4&2&0\\
\text{exactly interpretable}&8&8&8&6&4&2&0.
\end{array}
\]
The two length-\(6\) interpretable words are
\[
\bar\ell q\bar r p\bar q\ell,
\qquad
\bar\ell q\bar p r\bar q\ell.
\]
No structurally admissible word of length \(7\) even has an integer solution to its associated Diophantine chain. By Theorem 6.4 of arXiv:2610.01793v1, \(T\) therefore has finite order.

The same product contains the four integer cycles
\[
(20\ 40\ 46),
\]
\[
(158\ 200\ 760\ 275\ 550),
\]
\[
(410\ 1600\ 575\ 1138\ 560\ 2200\ 1558),
\]
and
\[
(2510\ 10000\ 3575\ 7018\ 3560\ 14200\ 5075\ 9958).
\]
Their lengths are \(3,5,7,8\), so their least common multiple is \(840\). Theorem 7.1 of the source says every finite order of a product of two class transpositions divides \(840\). Hence these finite checks together with the source's symbolic theorems give
\[
\operatorname{ord}(T)=840.
\]
This avoids using the RCWA order computation printed in Example 7.2.

Finally, among certificates consisting of individual cycles and using the source theorem's bound that every cycle of a finite-order product has length at most \(8\), four cycles are necessary and sufficient to certify divisibility by \(840\).

## Assumptions and scope
A class transposition \(\tau_{r_1(m_1),r_2(m_2)}\) interchanges \(r_1+m_1k\) with \(r_2+m_2k\) for every \(k\in\mathbb Z\) and fixes every other integer. The defining residue classes are disjoint because \(\gcd(40,28)=4\nmid18\) and \(\gcd(42,15)=3\nmid1\).

For a letter \(\alpha\), the source associates a linear Diophantine equation \(m_Xu-m_Yv=r_Y-r_X\), with \(XY=\chi(\alpha)\). A structurally admissible word of length \(n\) gives a chain of \(n\) such equations. Exact interpretation additionally requires unequal parameters at every pair of positions of the same parity.

The result concerns only the source's sharpness pair and the source's particular eight-letter interpretation formalism. It does not answer Question 7.3 about which other divisors of \(840\) occur.

## Proof
For each structurally admissible word, solve the associated chain exactly over the integers. After any prefix, all integer solutions can be parameterized as
\[
u_j=A_jk+B_j\qquad(k\in\mathbb Z).
\]
Suppose the next equation is
\[
m_Xu_i-m_Yu_{i+1}=r_Y-r_X.
\]
Substituting \(u_i=A_ik+B_i\) gives one linear congruence in \(k\). If the usual gcd divisibility condition fails, the chain has no integer solution. Otherwise, writing its solution as \(k=k_0+Mk'\) updates every preceding affine parameter and yields an integral affine expression for \(u_{i+1}\). Iterating this gives an exact integer-solvability decision with no bounded search over parameter values.

If the final affine forms for two same-parity positions are identical, exact interpretation is impossible. Otherwise every prohibited equality excludes at most one integer value of the free parameter, so finitely many exclusions cannot exhaust \(\mathbb Z\); an exact interpretation exists. Thus the algorithm decides both integer interpretability and exact interpretability symbolically.

There are exactly \(8\cdot2^{n-1}\) structurally admissible words of length \(n\), because each letter has two admissible successors. Applying the congruence recursion to every word for \(1\le n\le7\) gives the displayed profile
\[
(8,8,8,6,4,2,0)
\]
for both integer and exact interpretation counts. At length \(6\), the only survivors are the two displayed words; at length \(7\), all \(512\) chains fail an integer congruence. The source's Theorem 6.4 therefore implies \(\operatorname{ord}(T)<\infty\).

Direct substitution into the two class transpositions verifies each arrow of the four displayed integer cycles. Their periods are exactly \(3,5,7,8\), so \(840=\operatorname{lcm}(3,5,7,8)\) divides \(\operatorname{ord}(T)\). Theorem 7.1 gives the reverse divisibility because the order is now independently known to be finite. Therefore \(\operatorname{ord}(T)=840\).

For the four-cycle minimum, any set of lengths in \(\{1,\ldots,8}\) whose least common multiple is divisible by \(840=2^3\cdot3\cdot5\cdot7\) must contain \(8\), \(5\), \(7\), and a separate multiple of \(3\), since none of \(5,7,8\) is divisible by \(3\). Hence at least four cycles are required, and lengths \(3,5,7,8\) attain the bound.

## Verification
Running `python3 verify.py` reconstructs the source's eight-letter transition rule and \(\chi\)-table, performs the symbolic congruence recursion for every structurally admissible word through length \(7\), checks the exactness criterion, and reproduces the profile. It separately evaluates the four explicit cycles directly from the class-transposition definition. The recorded run ends with `VERIFY_OK`.

The word census is exhaustive because all \(8\cdot2^6=512\) length-\(7\) structurally admissible words are generated from the exact source transition rule. No finite search is used as a surrogate for an infinite-order argument: finiteness follows from the source's proved equivalence in Theorem 6.4 after the complete length-\(7\) census.

## Relationship to prior work
Iskra's paper proves the general finite-order divisor theorem and the length-\(7\) criterion for infinite order. Its Example 7.2 gives this same pair and reports an RCWA computation with `Order(g)=840` and an aggregate set of cycle lengths for a respected partition. The paper does not give the interpretability profile \((8,8,8,6,4,2,0)\), does not identify the two surviving length-\(6\) words, and does not supply the four explicit integer cycles above. The present calculation therefore gives a different finite certificate for the sharpness example within the paper's own symbolic framework.

Kohl's earlier cycle-structure preprint tabulates computational cases only when all four moduli are at most \(6\), so it cannot include this pair with moduli \(40,28,42,15\). Targeted semantic and exact-string searches found no prior source giving the profile or the surviving words.

## Limitations
The exact order \(840\) is already a result of the cited 2026 paper. The new content is the exact interpretation-depth profile, the two length-\(6\) survivors, and the explicit minimal four-cycle certificate that together replace the source's RCWA sharpness computation by finite congruence checks plus the paper's theorems.

The verifier encodes the source's definitions directly; an independent formalization has not been performed. A residual literature risk remains that equivalent diagnostic data may appear in an unindexed computation or private RCWA session.

## References
1. A. Iskra, *Finite Orders of Products of Two Class Transpositions Divide 840*, arXiv:2610.01793v1, 2026; especially Theorems 6.4 and 7.1 and Example 7.2.
2. S. Kohl, *On the Cycle Structure of Products of Two Class Transpositions*, preprint, 2009, revised 2011.
