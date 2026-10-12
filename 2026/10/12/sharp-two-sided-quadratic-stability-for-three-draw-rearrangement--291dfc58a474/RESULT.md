# Sharp two-sided quadratic stability for three-draw rearrangement diversity

## Finding
Let \(q\ge2\) be an integer, let \(p=(p_1,\ldots,p_q)\) be any probability vector, and draw \(X_1,X_2,X_3\) independently with common law \(p\). If \(N_i\) is the number of appearances of letter \(i\), let \(M=3!/\prod_{i=1}^qN_i!\) be the number of distinct rearrangements of the sampled triple. Put
\[
F_q(p)=\mathbb E_p M,\qquad A_q=6-\frac9q+\frac4{q^2},\qquad V_q(p)=\sum_{i=1}^q\left(p_i-\frac1q\right)^2.
\]
The exact best global lower and upper quadratic constants are
\[
\boxed{\left(5-\frac4q\right)V_q(p)\le A_q-F_q(p)\le\left(9-\frac{12}q+\frac{4(q-2)}{q(q-1)}\right)V_q(p).}
\]
For \(q=2\), both constants are \(3\) and equality holds throughout the probability simplex. For every \(q\ge3\), equality on the lower side holds precisely when \(p\) is uniform or concentrated at one letter. Equality on the upper side holds precisely when \(p\) is uniform or is uniform on exactly \(q-1\) of the \(q\) letters. Each coefficient is best possible because its nonuniform equality class is nonempty.

## Assumptions and scope
The alphabet has any finite cardinality \(q\ge2\), not necessarily a prime power, and all probability coordinates may vanish. Draws are independent and identically distributed; the score counts distinct permutations of *positions*, not the number of distinct observed letters. Variance \(V_q(p)\) is squared Euclidean distance from the uniform law on the *full* alphabet, including zero-probability letters. This is a discrete-probability result and requires no finite-field Fourier assumptions.

## Proof
Write \(s_2=\sum_i p_i^2\) and \(s_3=\sum_i p_i^3\). The probability that all three letters agree is \(s_3\); the probability of exactly one equal pair is \(3(s_2-s_3)\); the remainder \(1-3s_2+2s_3\) has three distinct letters. The respective rearrangement counts are \(1,3,6\). Consequently,
\[
F_q(p)=s_3+9(s_2-s_3)+6(1-3s_2+2s_3)=6-9s_2+4s_3.
\]
Writing \(\delta_i=p_i-1/q\) and \(V=V_q(p)\) gives
\[
A_q-F_q(p)=\left(9-\frac{12}q\right)V-4\sum_i\delta_i^3.
\]

**Sharp lower coefficient.** A direct pair expansion using \(\sum_i p_i=1\) yields
\[
\sum_{i<j}(p_i-p_j)^2=q s_2-1,\qquad
\sum_{i<j}(p_i-p_j)^2(p_i+p_j)=q s_3-s_2.
\]
Subtracting, one obtains the exact nonnegative certificate
\[
\boxed{A_q-F_q(p)-\left(5-\frac4q\right)V_q(p)
=\frac4q\sum_{i<j}(p_i-p_j)^2(1-p_i-p_j).}
\]
Every summand is nonnegative because \(p_i+p_j\le1\). If \(q\ge3\) and \(p\) is nonuniform, vanishing forces every pair with unequal masses to have total mass \(1\). If at least two coordinates are positive and \(p\) is not uniform, there is an unequal pair with total mass less than \(1\): choose a positive coordinate smaller than \(1\) and a zero coordinate when possible, or choose two unequal positive coordinates when all are positive (a third positive coordinate supplies slack). Therefore vanishing holds only for uniform vectors or simplex vertices. At a vertex the variance is positive, showing optimality of the lower constant. For \(q=2\), the only pair has total mass \(1\), so the certificate is identically zero.

**Sharp upper coefficient.** For nonnegative \(a,b,c\) define the cubic Schur form
\[
S(a,b,c)=a(a-b)(a-c)+b(b-a)(b-c)+c(c-a)(c-b).
\]
When \(a\ge b\ge c\), direct expansion gives
\[
S(a,b,c)=(a-b)^2(a+b-c)+c(a-c)(b-c)\ge0.
\]
Equality holds exactly when \(a=b=c\), or when, up to permutation, \((a,b,c)=(t,t,0)\) for some \(t\ge0\). Let \(e_3=\sum_{i<j<k}p_ip_jp_k\). Expanding all triples, using \(6e_3=1-3s_2+2s_3\), gives
\[
2\sum_{i<j<k}S(p_i,p_j,p_k)
=q(q-1)s_3-(2q-1)s_2+1.
\]
It follows, by substituting the power-sum formula for \(F_q\), that
\[
\boxed{\left(9-\frac{12}q+\frac{4(q-2)}{q(q-1)}\right)V_q(p)-(A_q-F_q(p))
=\frac8{q(q-1)}\sum_{i<j<k}S(p_i,p_j,p_k)\ge0.}
\]
For \(q=2\), the triple sum is empty, so this is an identity. For \(q\ge3\), equality requires every three-coordinate subvector to be constant or, after permutation, \((t,t,0)\). A nonuniform vector with no zero coordinates violates this requirement for some triple. A vector with two or more zeros and at least one positive coordinate contains a triple \((t,0,0)\), which violates it. With exactly one zero coordinate, each pair of the remaining positive coordinates must be equal, hence \(p\) is uniform on the other \(q-1\) letters. Conversely such a vector makes every Schur form vanish. Since its \(V_q\) is positive, the upper coefficient is optimal. This also establishes all claimed equality cases and both inequalities for every admissible probability vector.

## Verification
The independent standard-library script `verify.py` evaluates the two certificate identities using exact rational arithmetic for all probability vectors on a prescribed finite rational grid, checks their signs and sharpness cases, and separately enumerates all ordered length-three samples on smaller grids to reproduce the expectation polynomial. Run `python verify.py` from the extracted package. Its observed output was `VERIFY_OK exact_simplex_cases=12854 independent_expectation_cases=251`. The grid is not an exhaustive test over the real simplex and is **not** an infinite proof. The universal statements follow from the two exact certificates and elementary sign/equality analyses above.

## Relationship to prior work
Biswas, Carneiro, Flock, Madrid, Oliveira e Silva, Stovall, and Tautges (arXiv:2609.29882v1, Theorem 3) proved that the uniform distribution uniquely maximizes the expected rearrangement count for *every* sample length, using two-point symmetrization. Their paper provides the motivating three-draw functional, but its statements give neither the two best global quadratic constants nor their opposite-boundary equality classes. The probabilistic theorem here strengthens their qualitative result in the first nontrivial cubic instance; it is not an improvement to the full arbitrary-length theorem.

Two related published analyses of the same functional establish, respectively, a uniform lower quadratic coefficient \(d(d-1)/2\) and the exact local isotropic Hessian at the uniform distribution. For three draws, the former gives coefficient \(3\), strictly below the optimal \(5-4/q\) when \(q\ge3\); the latter does not supply a global upper envelope or its extremizers. Gonçalves's component-wise permutation-match comparison (arXiv:2609.31979v1) yields a broader qualitative majorization statement; its abstract, not its complete manuscript, could be inspected here, so the possibility of a stronger hidden quantitative implication is recorded as a priority risk. Earlier results by Peskir and Rinott concern Schur concavity/majorization and do not establish the displayed sharp two-sided bounds in the material accessible for comparison.

## Limitations
The result is restricted to three independent identically distributed draws. It does not determine sharp distance remainders for four or more draws, arbitrary dependent sampling, or nonidentical categorical distributions. The constants are optimal for squared Euclidean distance and are not claimed to be optimal for total variation, relative entropy, or other metrics. The broad older majorization literature and the inaccessible full manuscript arXiv:2609.31979v1 leave a residual originality risk; absence from search results is not proof of priority.

## References
1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1 (24 September 2026), Theorem 3 and Sections 4–5.
2. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1 (25 September 2026).
3. *Quadratic stability for endpoint finite-field moment-curve extension*, public result dated 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-quadratic-stability-for-endpoint-finite-field-moment-curve-exten--e3a60ec2aa94 .
4. *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer*, public result dated 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-isotropic-quadratic-stability-at-the-uniform-finite-field-moment--49b4f93ca348 .
5. G. Peskir, *Best constants in Kahane–Khintchine inequalities for complex Steinhaus functions*, Proceedings of the American Mathematical Society 123 (1995), 3101–3111.
6. Y. Rinott, *Multivariate majorization and rearrangement inequalities with some applications to probability and statistics*, Israel Journal of Mathematics 15 (1973), 60–77.
