# Sharp record–occupation covariance range at the first nonuniversal random-walk horizon

## Finding

Let \(X_1,X_2,X_3\) be independent copies of a real-valued, symmetric, atomless random variable, and set \(S_0=0\), \(S_j=\sum_{i=1}^jX_i\). The number of *new strict upper records after time zero* and the strict-positive occupation count are
\[
R_3=\sum_{j=1}^{3}\mathbf 1\{S_j>\max_{0\le i<j}S_i\},\qquad
A_3=\sum_{j=1}^{3}\mathbf 1\{S_j>0\}.
\]
Let \(B_1,B_2,B_3\) be independent copies of \(|X_1|\) and put
\[
t=\Pr(B_1>B_2+B_3).
\]
Then the exact finite-sample covariance is
\[
\boxed{\operatorname{Cov}(R_3,A_3)=\frac{109}{96}-\frac{t}{8}.}
\]
Over all symmetric atomless increment laws, the complete attainable covariance interval is
\[
\boxed{\frac{35}{32}<\operatorname{Cov}(R_3,A_3)\le\frac{109}{96}.}
\]
The upper endpoint is attained whenever \(|X_1|\) is uniform on \((1,3/2)\). The lower endpoint is a strict, sharp infimum: it is approached by continuously distributed magnitudes on increasingly numerous widely separated scales, but cannot be attained. All intermediate values are attained. The two marginal laws of \(R_3\) and \(A_3\) are distribution-free. At one and two steps, the corresponding covariance is also distribution-free, equal respectively to \(1/4\) and \(5/8\). Thus three steps are the first horizon at which this particular joint dependence can detect the increment law.

For example, uniform increments on \((-1,1)\) give \(t=1/6\) and covariance \(107/96\), whereas a standard Gaussian increment law gives
\[
\operatorname{Cov}(R_3,A_3)=\frac{97}{96}+\frac{1}{2\pi}\arcsin\!\frac{1}{\sqrt3},
\]
which differs from \(107/96\). Counting time zero as one additional record does not change any covariance.

## Assumptions and scope

The increments are independent, identically distributed, symmetric about zero, and atomless; no density regularity or moment condition is required. They are almost surely nonzero. Under these conditions every partial sum and difference of partial sums has an atomless law, so strict comparisons have zero-probability ties. The result concerns exactly the three-step discrete-time walk; the sharp envelope is over all such increment distributions, not over correlated jumps or arbitrary horizons. The term occupation count means the number of **positive partial sums**, not the age of a current record.

## Proof

Write \(I_i=\mathbf1\{S_i>\max_{0\le k<i}S_k\}\) and \(J_j=\mathbf1\{S_j>0\}\). The sign of a symmetric nonzero increment is fair and independent of its magnitude. Consequently the three signs are independent fair bits, and the three magnitudes are exchangeable and atomless.

A direct sign enumeration, using \(\Pr(B_1>B_2)=1/2\), establishes the following full mixed-moment matrix (row \(i\), column \(j\)):
\[
\bigl(\mathbb E[I_iJ_j]\bigr)_{1\le i,j\le3}
=
\begin{pmatrix}
\frac12&\frac38&\frac38-\frac t8\\
\frac14&\frac38&\frac5{16}\\
\frac3{16}&\frac{11}{48}&\frac5{16}
\end{pmatrix}.
\]
Here are the two nontrivial evaluations. First, \(I_1J_3\) asks for \(X_1>0\) and \(X_1+X_2+X_3>0\). Conditional on \(X_1=B_1>0\), the four sign choices of \((X_2,X_3)\) yield conditional success probabilities \(1\), \(1-t\), \(1-t\), and \(t\). Each occurs with probability \(1/4\). Multiplying by \(\Pr(X_1>0)=1/2\) gives \(3/8-t/8\).

Second, \(I_3J_2\) is the event \(X_3>0\), \(X_2+X_3>0\), \(X_1+X_2>0\); the condition \(S_3>0\) is then automatic. Let \(F\) be the continuous symmetric distribution function of an increment and put \(u=F(X_2)\). The probability integral transform makes \(u\) uniform on \((0,1)\). When \(X_2>0\), the conditional probability is \(F(X_2)/2=u/2\), and when \(X_2<0\), it is \(F(X_2)^2=u^2\). Hence
\[
\Pr(I_3J_2=1)=\int_{1/2}^1\frac u2\,du+\int_0^{1/2}u^2\,du
=\frac3{16}+\frac1{24}=\frac{11}{48}.
\]
The remaining cells follow from symmetry, conditioning, and three-sign enumeration. In particular \(\Pr(I_2J_3=1)\) equals \(\Pr(S_1>0,S_2>0,S_3>0)\) after swapping the first two increments; this is \(5/16\) by elementary sign enumeration. Indeed, on \(X_1>0\), the four signs of the last two increments give probabilities \(1,1-t,1/2,t\) for remaining strictly positive, totaling \((1+1-t+1/2+t)/8=5/16\). Reversing the increments proves \(\Pr(I_3=1)=5/16\) without invoking any infinite-horizon theorem.

Summing the nine matrix entries gives
\[
\mathbb E[R_3A_3]=\frac{35}{12}-\frac t8.
\]
Also \(\mathbb ER_3=1/2+3/8+5/16=19/16\) and \(\mathbb EA_3=3/2\), whence the covariance formula. The analogous one-step computation gives \(1/4\); at two steps the four mixed probabilities are \(1/2,3/8,1/4,3/8\), giving covariance \(5/8\).

For sharpness, the three events \(\{B_i>B_j+B_k\}\), indexed by \(i\), are disjoint and equiprobable, so \(0\le t\le1/3\). The inequality is strict at the upper bound: every nondegenerate positive magnitude law assigns positive mass to some interval \((a,3a/2)\); on the event that all three magnitudes fall in that interval, none exceeds the sum of the others. Thus \(t<1/3\). If magnitudes lie in \((1,3/2)\), then \(t=0\), proving attainment of the covariance's upper endpoint.

For the opposite endpoint, let \(J\) be uniform on \(\{1,\ldots,m\}\) and \(U\) uniform on \((1,1.003)\), independently, and set \(B=100^J U\). On the event that three independent scale indices are distinct, the unique largest magnitude exceeds the sum of the other two. This event has probability \(m(m-1)(m-2)/m^3\), tending to one. By exchangeability, \(t\to1/3\), proving sharpness of the strict lower bound. Finally, mixing the narrow one-scale magnitude law with a fixed sufficiently spread-out magnitude law varies \(t\) continuously as a cubic polynomial in the mixing weight; the intermediate value theorem gives every \(t\in[0,1/3)\).

## Verification

Run `python3 checker.py` using Python 3 and the standard library. It enumerates all \(2^n n! m^n\) bin/sign/rank cells for selected \(m\) at \(n=3\), and independently at \(n=1,2\), with exact rational weights. Because within-bin magnitudes are continuous and the bin separation preserves every relevant strict inequality, the enumerated rank cells represent the corresponding continuous distributions exactly. The program reconstructs all nine mixed moments, both expectations, the covariance, and the triple-dominance probability for \(m=1,2,3,5,8\), verifies the \(107/96\) uniform-magnitude benchmark algebraically, and checks the separated-scale lower bound. It reports `EXACT_VERIFICATION_OK 73 identity_groups` if successful. These finite-family computations test the proof but do not constitute an exhaustive proof for arbitrary atomless laws; the preceding argument does.

## Relationship to prior work

Sparre Andersen fluctuation theory and the renewal description in Majumdar–Ziff give universal marginal record statistics for continuous symmetric random walks. Godrèche–Majumdar–Schehr and Szabó–Vető further examine record ages, including exact renewal formulas and asymptotic age statistics. The positive-occupation count is a different variable from the time elapsed since the latest record. These published formulas for marginal records/ages do not directly supply the covariance with the number of strictly positive partial sums or its sharp range across increment laws. Later multi-time record treatments concern the record process itself, whereas knowing all record indicators does not reveal occupation signs between records. The first nonuniversal dependence threshold and complete attainable envelope above are the contribution asserted here, not any marginal Sparre Andersen formula.

## Limitations

Only the covariance at horizons one, two and three is classified. Nothing is claimed about the exact joint distribution at arbitrary horizons, conditional correlations, nonsymmetric increments, dependent increments, lattice distributions with ties, or higher-dimensional walks. A published identity in a different fluctuation-theory formulation might imply part of this finite result; archival bibliographic completeness has not been certified. Independent validation has not been performed.

## References

1. S. N. Majumdar and R. M. Ziff, *Universal Record Statistics of Random Walks and Lévy Flights*, arXiv:0806.0057, first submitted 2008-05-31. https://arxiv.org/abs/0806.0057
2. C. Godrèche, S. N. Majumdar and G. Schehr, *Universal statistics of longest lasting records of random walks and Lévy flights*, arXiv:1403.6187, first submitted 2014-03-24. https://arxiv.org/abs/1403.6187
3. R. Szabó and B. Vető, *Ages of records in random walks*, arXiv:1510.01152, first submitted 2015-10-05. https://arxiv.org/abs/1510.01152
4. *Full Record Statistics of 1d Random Walks*, arXiv:2312.14885, https://arxiv.org/abs/2312.14885 (later contextual comparison, not the archival anchor).
