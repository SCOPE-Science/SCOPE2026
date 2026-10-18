# Diagonal relations of finite meet-chains: a product-of-chains theorem
## Finding
For each integer \(n\geq1\), let \(C_n=\{0,1,\ldots,n-1\}\) be the meet-chain semigroup with \(i\cdot j=\min(i,j)\). A *diagonal subsemigroup* is a subset \(\rho\subseteq C_n\times C_n\) containing every \((i,i)\) and closed under coordinatewise minimum. Let \(\operatorname{Diag}(C_n)\) denote its inclusion-ordered lattice, and let \(\operatorname{Cong}(C_n)\) denote its semigroup congruences.

There is an explicit lattice isomorphism
\[
\operatorname{Diag}(C_n)\cong\prod_{r=2}^{n}\bigl([r]\times[r]\bigr),
\]
where \([r]\) denotes the chain with \(r\) elements; the product is a singleton when \(n=1\). In particular,
\[
\bigl|\operatorname{Diag}(C_n)\bigr|=(n!)^2.
\]
More precisely, the complete distribution by number of off-diagonal pairs is
\[
\sum_{\rho\in\operatorname{Diag}(C_n)}z^{|\rho|-n}
=\prod_{r=1}^{n}\left(1+z+\cdots+z^{r-1}\right)^2.
\]
This polynomial is also the square of the inversion-number generating polynomial of the symmetric group \(\mathfrak S_n\): the diagonal subsemigroups correspond bijectively to ordered pairs of permutations and their off-diagonal cardinality equals the sum of the two inversion numbers. The congruences are exactly the equivalence relations with convex (interval) classes, so
\[
|\operatorname{Cong}(C_n)|=2^{n-1},\qquad
\chi(C_n)=\frac{|\operatorname{Cong}(C_n)|}{|\operatorname{Diag}(C_n)|}
=\frac{2^{n-1}}{(n!)^2}.
\]
In particular, \(\chi(C_n)\sim (4\pi n)^{-1}(2e^2/n^2)^n\) as \(n\to\infty\).

## Assumptions and scope
Only the ordinary semigroup multiplication \(\min\) is considered: relations need not preserve a distinguished zero, identity, or any extra algebraic operations. The ground set is the finite linearly ordered set \(C_n\), with \(n\ge1\); no assumptions on fields are involved. Multiplication in \(C_n\times C_n\) takes \((i,j),(k,\ell)\) to \((\min(i,k),\min(j,\ell))\). The inclusion order is the relation order, not the order of the underlying chain. The grading counts \(|\rho|-n\), not the total size \(|\rho|\).

## Proof
**1. Forced prefix form.** For each \(i\in\{0,\ldots,n-2\}\), define the maximum upper and lower reach of a reflexive compatible relation \(\rho\) by
\[
a_i=\max\bigl(\{0\}\cup\{j-i:i<j,\ (i,j)\in\rho\}\bigr),\qquad
b_i=\max\bigl(\{0\}\cup\{j-i:i<j,\ (j,i)\in\rho\}\bigr).
\]
Each is an integer in \(\{0,1,\ldots,n-1-i\}\). If \((i,j)\in\rho\) and \(i<k<j\), multiply by the diagonal pair \((k,k)\). This produces \((i,k)\). Similarly, if \((j,i)\in\rho\), the product with \((k,k)\) is \((k,i)\). Thus the upper and lower portions of \(\rho\) are independent initial segments:
\[
\rho=\Delta\ \cup\ \{(i,j):i<j\le i+a_i\}
\ \cup\ \{(j,i):i<j\le i+b_i\},
\qquad\Delta=\{(i,i):0\le i<n\}.
\]
The sequence pair is uniquely recovered from \(\rho\).

**2. Converse closure.** Choose arbitrary \(a_i,b_i\in\{0,\ldots,n-1-i\}\) and form the displayed relation. Its closure under coordinatewise minimum follows by cases. A diagonal pair multiplied by an upper or lower pair gives that pair, a diagonal pair, or an intermediate pair in the same initial segment. Two upper pairs give an upper pair within the initial segment attached to the smaller first coordinate, or a diagonal pair; two lower pairs are dual. For one upper pair \((i,j)\), \(i<j\), and one lower pair \((k,\ell)\), \(\ell<k\): if \(k<i\), their product is \((k,\ell)\); otherwise the product is \((i,\min(j,\ell))\). When its second coordinate is at least \(i\), it is in the upper prefix of \((i,j)\); when that coordinate is below \(i\), it lies in the lower prefix of \((k,\ell)\), since \(\ell<i\le k\). Hence **every** choice of the two sequences yields a diagonal subsemigroup, proving the bijection.

**3. Lattice and graded count.** Relation containment is precisely coordinatewise comparison of all \(a_i\) and \(b_i\). As coordinate \(i\) has \(n-i\) allowed values, the lattice is the asserted product of chains. Since each upper or lower reach contributes exactly its value to the number of off-diagonal pairs,
\[
|\rho|-n=\sum_{i=0}^{n-2}(a_i+b_i).
\]
Multiplying independent generating polynomials gives the displayed rank polynomial, and evaluating at \(z=1\) gives \(\prod_{i=0}^{n-2}(n-i)^2=(n!)^2\). The permitted digit vectors \((a_i)\) are precisely the Lehmer inversion-code digits for permutations of \(n\) symbols, proving the permutation interpretation without assuming a pre-existing count of these relations.

**4. Congruences.** If an equivalence relation \(\theta\) on \(C_n\) is compatible and \(i<k<j\) with \(i\mathrel\theta j\), multiplying \((i,j)\) by \((k,k)\) gives \(i\mathrel\theta k\). Since \(\theta\) is symmetric, multiplying \((j,i)\) by \((k,k)\) gives \(k\mathrel\theta j\). Hence every congruence class is an interval. Conversely, any partition into consecutive blocks is the kernel of a nondecreasing quotient map from \(C_n\) onto a finite chain; a nondecreasing map preserves minimum and so its kernel is a congruence. There are independently \(n-1\) adjacent gaps to cut or retain, giving \(2^{n-1}\) congruences. The DSC coefficient follows. Stirling's formula \(n!\sim\sqrt{2\pi n}(n/e)^n\) yields the stated asymptotic.

## Verification
The supplied standalone \(\texttt{verify.py}\) performs an exhaustive check of all \(2^{n(n-1)}\) reflexive binary relations for each \(1\le n\le4\). It independently tests coordinatewise-minimum closure, the prefix-code reconstruction, the exact size and rank polynomial, and congruence counts using symmetry and transitivity. For \(2\le n\le5\), a second pass enumerates every pair of prefix codes and verifies closure, injectivity, and graded counts without using brute-force filtering. It returns \(\texttt{VERIFY\_OK}\). These finite checks are not an infinite proof; the four symbolic steps above establish the arbitrary-\(n\) statements.

## Relationship to prior work
Barber and Ruškuc define the DSC coefficient and establish results for Rees matrix semigroups in *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups* (first posted 19 February 2026, arXiv:2602.17286v1; inspected revised full text arXiv:2602.17286v2, 7 October 2026). Their Section 4, especially Theorem 4.2 and its concluding question, bounds the coefficient of a Clifford semigroup by that of its underlying semilattice, and explicitly leaves the possible values for semilattices open. That paper does not give the chain-semigroup product-lattice classification or its factorial-square count. Their earlier *Semigroup Congruences and Subsemigroups of the Direct Square* (arXiv:2504.02428) provides the broader DSC setting rather than this enumeration. The general study of compatible reflexive relations also appears in Fioravanti's 2021 paper; its Mal'cev-condition results are distinct from the present finite-chain census. The congruence count of interval partitions is elementary and is not claimed as an independent novelty.

## Limitations
The result concerns only linearly ordered finite semilattices in the single-operation semigroup signature. It does not classify diagonal subsemigroups for branching semilattices or all possible coefficients of arbitrary semilattices, and it does not give a general Clifford-semigroup equality criterion. Search and source comparisons cannot exclude an equivalent older characterization under different terminology; the originality assessment is therefore subject to historical-overlap risk. No independent audit is claimed by the mathematical result itself.

## References
1. C. Barber and N. Ruškuc, *Comparing Numbers of Diagonal Subsemigroups and Congruences for Semigroups*, arXiv:2602.17286v1 (19 February 2026), full text revised as arXiv:2602.17286v2 (7 October 2026), https://arxiv.org/html/2602.17286v2.
2. C. Barber and N. Ruškuc, *Semigroup Congruences and Subsemigroups of the Direct Square*, arXiv:2504.02428 (2025), https://arxiv.org/abs/2504.02428.
3. S. Fioravanti, *Mal'cev conditions corresponding to identities for compatible reflexive relations*, Algebra universalis 82 (2021), DOI 10.1007/s00012-020-00699-x.
