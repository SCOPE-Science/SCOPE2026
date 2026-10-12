# The one-variable rank Nullstellensatz has sharp coefficient \(\ell\)

## Finding
Let \(K\) be an algebraically closed field of characteristic \(0\), let \(\ell\ge 1\), and let \(f_1,\ldots,f_\ell,g\in K[x]\). Then the following are equivalent:

1. there is \(C\in\mathbb N\) such that, for every \(n\ge1\) and every \(X\in M_n(K)\),
   \[\operatorname{{rank}}g(X)\le C\max_i\operatorname{{rank}}f_i(X);\]
2. \(g\in(f_1,\ldots,f_\ell)\).

If the generators are not all zero and \(d=\gcd(f_1,\ldots,f_\ell)\) is monic, condition 2 is \(d\mid g\). When it holds, \(C=\ell\) always works. This coefficient is sharp as a bound depending only on \(\ell\).

Thus the rank Nullstellensatz conjecture is true for arbitrary, possibly nonhomogeneous, generators in one variable. Together with the two-variable counterexample \(f=xy-1\), \(g=yx-1\) of Yan--Yang, this gives a sharp variable-count boundary for the general conjecture.

## Assumptions and scope
The field assumptions match the setting of the motivating conjecture: \(K\) is algebraically closed of characteristic \(0\). The conclusion covers every number \(\ell\ge1\) of generators and every polynomial choice, including constant and zero polynomials. If all \(f_i\) are zero, both conditions reduce to \(g=0\); below assume at least one generator is nonzero.

No assertion is made here for two or more noncommuting variables beyond the already known two-variable counterexample.

## Proof
Let \(d=\gcd(f_1,\ldots,f_\ell)\), normalized to be monic. Since \(K[x]\) is a principal ideal domain,
\[(f_1,\ldots,f_\ell)=(d).\]

Suppose first that \(g\in(d)\). Write \(g=hd\). Bézout's identity gives polynomials \(a_1,\ldots,a_\ell\in K[x]\) with
\[d=\sum_{i=1}^{\ell}a_i f_i.\]
For every square matrix \(X\), polynomial evaluations in \(X\) commute, and elementary rank inequalities give
\[
\operatorname{{rank}}g(X)
=\operatorname{{rank}}(h(X)d(X))
\le\operatorname{{rank}}d(X)
\le\sum_{i=1}^{\ell}\operatorname{{rank}}(a_i(X)f_i(X))
\le\ell\max_i\operatorname{{rank}}f_i(X).
\]
Hence \(C=\ell\) works.

Conversely suppose \(d\nmid g\). Because \(K\) is algebraically closed, there is \(\lambda\in K\) for which the multiplicity \(a\) of \(x-\lambda\) in \(d\) is strictly larger than its multiplicity \(b\) in \(g\). Let \(X=J_a(\lambda)\), the size-
\(a\) Jordan block with eigenvalue \(\lambda\). Every \(f_i\) is divisible by \((x-\lambda)^a\), so \(f_i(X)=0\) for all \(i\). On the other hand write
\[g=(x-\lambda)^b u,\qquad u(\lambda)\ne0.\]
The matrix \(u(X)\) is invertible, while \((X-\lambda I)^b\ne0\) because \(b<a\). Therefore \(g(X)\ne0\), so \(\operatorname{{rank}}g(X)>0\) whereas every \(\operatorname{{rank}}f_i(X)=0\). No finite \(C\) can satisfy the domination inequality. This proves the equivalence.

It remains to show that the universal coefficient \(\ell\) cannot be improved. Choose distinct scalars \(\lambda_1,\ldots,\lambda_\ell\in K\), put
\[f_i(x)=\prod_{{j\ne i}}(x-\lambda_j),\qquad g(x)=1,\]
and let \(X=\operatorname{{diag}}(\lambda_1,\ldots,\lambda_\ell)\). The greatest common divisor of the \(f_i\) is \(1\), so \(g\) belongs to their ideal. Yet each \(f_i(X)\) has rank \(1\), whereas \(g(X)=I_\ell\) has rank \(\ell\). Thus every valid coefficient for this tuple satisfies \(C\ge\ell\). Together with the upper bound, the best universal coefficient is exactly \(\ell\).

## Verification
The proof uses only the principal-ideal structure of \(K[x]\), Bézout's identity, elementary rank inequalities, and the standard Jordan-block test for polynomial multiplicity. The companion file `verify.py` checks the sharpness construction for \(1\le\ell\le7\) and several obstruction witnesses over the rationals; its output is recorded in `VERIFY_OUTPUT.txt`. These computations are sanity checks, not substitutes for the proof.

## Relationship to prior work
Volčič formulated the dimension-free rank-domination conjecture for arbitrary noncommutative polynomials and arbitrary numbers of generators. His survey states the conjecture as equivalence between uniform rank domination and two-sided ideal membership, and notes only the easy membership-to-domination direction. Yan--Yang prove the conjecture when the generators are homogeneous and give the nonhomogeneous two-variable counterexample \(xy-1\), \(yx-1\). Their full text does not state a one-variable theorem.

Shamovich--Volčič classify rank *equality* of two noncommutative polynomials via stable association; this does not supply the one-sided multi-generator domination criterion above. Pop--Negrescu prove a rank identity involving the greatest common divisor and least common multiple of two one-variable complex polynomials evaluated at one matrix. That identity concerns two polynomial values at a fixed matrix and does not state the all-sizes, arbitrary-generator ideal-membership equivalence or the sharp universal coefficient \(\ell\).

A prior finding treats a different two-variable product-reversal family \(p(xy),q(yx)\); it neither implies nor contains the arbitrary-generator one-variable theorem here.

## Limitations
The originality search found no source stating this exact one-variable rank Nullstellensatz with arbitrary generators and sharp coefficient \(\ell\), but literature search cannot prove absence from all published or unpublished sources. The argument is elementary once the one-variable boundary is isolated. No claim is made that the sharp coefficient remains meaningful for multivariable free algebras, where the general conjecture is false.

## References
1. S. Yan and J. Yang, *On a Rank Nullstellensatz Conjecture for Noncommutative Polynomials*, arXiv:2610.01804v1 (2026).
2. J. Volčič, *Dimension-free matricial Nullstellensätze for noncommutative polynomials*, arXiv:2403.06270v1; later conference version (2025).
3. E. Shamovich and J. Volčič, *Global structure behind pointwise equivalences of noncommutative polynomials*, arXiv:2505.07469v2.
4. V. Pop and A. Negrescu, *Three New Proofs of a Matrix-Polynomial Rank Identity*, Mathematics 12 (2024), 360, DOI:10.3390/math12030360.
