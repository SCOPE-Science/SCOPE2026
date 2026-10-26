# Exact exponential ambiguity rate for distance-two legal-index decompositions

## Finding

Let \((a_n)_{n\ge1}\) be the \(\{2\}\)-legal index-difference sequence: \(a_n\) is the smallest positive integer not representable by a sum of earlier distinct terms with no pair of selected indices differing by \(2\). For each nonnegative integer \(m\), let \(r(m)\) count all legal representations (the empty representation counts once at \(m=0\)), and let
\[
M_n=\frac{1}{a_n}\sum_{m=0}^{a_n-1}r(m).
\]
Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), and set
\[
D_j=F_{\lceil j/2\rceil+2}F_{\lfloor j/2\rfloor+2}\quad(j\ge0).
\]
**Exact finite inequalities:** for every integer \(n\ge4\),
\[
\boxed{\frac{D_{n-3}}{a_n}\le M_n\le\frac{D_{n-1}}{a_n}.}
\]
Let \(\rho\) be the unique real root of \(\rho^3-\rho^2-1=0\), and \(\varphi=(1+\sqrt5)/2\). Then
\[
\boxed{M_n=\Theta((\varphi/\rho)^n),\qquad
\lim_{n\to\infty}M_n^{1/n}=\frac{\varphi}{\rho}\approx1.10402957806295.}
\]
In particular, the mean number of representations increases exponentially, and the maximal number of representations among integers below \(a_n\) grows at least at this rate.

## Assumptions and scope

All indices are positive integers. In a legal decomposition, each term is used at most once, and two distinct chosen indices \(i,j\) satisfy \(|i-j|\ne2\). Distinct subsets count as distinct representations even when their sums coincide. The mean is over all integers \(m\) with \(0\le m<a_n\), including zero. The theorem applies to every \(n\ge4\) for the finite inequalities and to \(n\to\infty\) for the growth statement.

The known recurrence (Moura et al., Proposition 2.3) is
\[
a_1=1,\quad a_2=2,\quad a_3=4,\quad
a_{j+1}=a_j+a_{j-2}\quad(j\ge3).
\]
This established recurrence is used as a premise, not claimed as a new theorem.

## Proof

**1. Exact independent-set count.** On the index set \(\{1,\ldots,j\}\), the only forbidden edges are \(\{i,i+2\}\). The odd indices therefore form a path with \(\lceil j/2\rceil\) vertices, and the even indices form a disjoint path with \(\lfloor j/2\rfloor\) vertices. A path on \(t\) vertices has exactly \(F_{t+2}\) independent sets, including the empty one: splitting according to the last vertex gives the Fibonacci recurrence with initial counts \(1,2\). Hence the total number of legal index subsets within the first \(j\) terms is exactly \(D_j\).

**2. Exact prefix-sum identity.** Rearranging the recurrence yields \(a_{j+3}-a_{j+2}=a_j\) for \(j\ge1\). Telescoping gives
\[
\sum_{i=1}^{t}a_i=a_{t+3}-a_3=a_{t+3}-4\quad(t\ge1).
\]
In particular, for \(n\ge4\), the sum of *all* the first \(n-3\) terms is \(a_n-4<a_n\). Therefore each one of the \(D_{n-3}\) legal subsets of those terms contributes a representation of an integer strictly below \(a_n\). This holds whether or not different subsets yield equal sums.

**3. Upper bound.** Because the sequence is increasing and all its terms are positive, no representation of an integer smaller than \(a_n\) can use a term indexed \(n\) or higher. Thus every counted representation is one of the \(D_{n-1}\) legal subsets of the first \(n-1\) indices. Combining steps 2 and 3 proves both finite inequalities exactly.

**4. Growth of the denominator.** The polynomial \(x^3-x^2-1\) has a unique positive root \(\rho\in(1,2)\). Put \(b_j=a_j/\rho^j\). Its defining equation implies \(\rho^{-1}+\rho^{-3}=1\), so for \(j\ge3\),
\[
b_{j+1}=\rho^{-1}b_j+\rho^{-3}b_{j-2}.
\]
Each new normalized term is a convex combination of preceding normalized terms. Since \(b_1,b_2,b_3\) are strictly positive, they trap every later normalized term between fixed positive constants. Consequently \(a_n=\Theta(\rho^n)\), with no assumption about cancellation of characteristic-root coefficients.

**5. Growth of legal subsets.** Binet's formula \(F_t=(\varphi^t-(-\varphi)^{-t})/\sqrt5\) gives \(F_t=\Theta(\varphi^t)\). Since the Fibonacci indices in \(D_j\) sum to \(j+4\), it follows that \(D_j=\Theta(\varphi^j)\). The two fixed-shift bounds in steps 2 and 3 yield \(M_n=\Theta((\varphi/\rho)^n)\). Taking \(n\)-th roots yields the stated limit. Finally, \(\rho<\varphi\): at \(x=\varphi\), \(x^3-x^2-1=\varphi-1>0\), while the polynomial is negative at \(x=1\). Thus the exponential base is strictly greater than one.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The checker independently constructs terms by the defining least-excluded-positive rule through index \(16\), enumerates every legal index subset through index \(17\), compares the exact \(D_j\) counts, verifies the telescoping identity and both mean bounds, and confirms that every smaller integer has a representation in the tested ranges. These finite checks support the symbolic proof but do not replace its infinite quantifiers. There are no external computation files or dependencies.

## Relationship to prior work

Moura, Keisling, Lilly, Mauro, Miller, Phang and Velazquez Iannuzzelli (arXiv:2210.10577, first posted 2022-10-19) introduced the general \(S\)-legal index-difference construction and established the recurrence for \(S=\{2\}\) (Proposition 2.3). Their Section 4 explicitly raises the growth of the mean number of representations as Question 5. Their Lemma 4.1 treats a different dense family \(S=[k]\setminus\{k-c\}\) under the restriction \(2c<k\); its boundary parameter choice \(k=2,c=1\), which would give \(S=\{2\}\), violates that restriction. The exact parity-path multiplicity \(D_j\), the two-term-shift squeeze and the explicit rate \(\varphi/\rho\) are not stated there.

Catral, Ford, Harris, Miller and Nelson (arXiv:1606.09312) proved exponential average decomposition multiplicity for the *Fibonacci quilt*, with a different forbidden-index rule and different recurrence. Their counting-and-squeezing strategy is an acknowledged methodological precedent, not an instance implying the present numerical constant or exact inequalities. OEIS A164316 records the recurrence sequence \((a_n)\) under an unrelated binary-string interpretation, not the \(\{2\}\)-legal decomposition averages. Search noncoverage does not establish absolute publication priority.

## Limitations

This theorem determines the **exponential growth rate** and explicit nonasymptotic upper/lower bounds, but not a limiting leading multiplier in an asymptotic equivalent for \(M_n\), nor the distribution of \(r(m)\) among individual integers. It does not address general forbidden sets \(S\). An unindexed earlier equivalent derivation may exist. No independent mathematical audit has been conducted.

## References

1. G. Z. Dantas e Moura, A. Keisling, A. Lilly, A. Mauro, S. J. Miller, M. Phang, and S. Velazquez Iannuzzelli, *Recurrence Relations for S-Legal Index Difference Sequences*, arXiv:2210.10577v1 (2022-10-19), especially Proposition 2.3 and Section 4; version 2 (2023-08-28) inspected. https://arxiv.org/html/2210.10577v2
2. M. Catral, P. L. Ford, P. E. Harris, S. J. Miller, and D. Nelson, *Legal Decompositions Arising from Non-positive Linear Recurrences*, arXiv:1606.09312v2 (2016), especially Section 3. https://arxiv.org/html/1606.09312v2
3. OEIS Foundation, A164316, a recurrence sequence with initial values \(1,2,4,5,7,11\). https://oeis.org/A164316
