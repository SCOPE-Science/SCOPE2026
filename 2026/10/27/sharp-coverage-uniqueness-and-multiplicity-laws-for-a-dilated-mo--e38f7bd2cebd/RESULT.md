# Sharp coverage, uniqueness, and multiplicity laws for a dilated Moser–de Bruijn sumset

## Finding

Let \(\mathcal M\) be the set of all nonnegative integers whose base-four digits lie in \(\{0,1\}\). Equivalently, \(\mathcal M=\{\sum_{j\ge0}\epsilon_j4^j:\epsilon_j\in\{0,1\}\text{ and only finitely many }\epsilon_j\ne0\}\). Define the ordered representation multiplicity
\[
r(n)=\#\{(a,b)\in\mathcal M^2:a+3b=n\},\qquad n\ge0.
\]
For every integer \(k\ge0\), write \(B_k\) for the number of \(n\) with \(0\le n<4^k\) and \(r(n)>0\), \(U_k\) for the number with \(r(n)=1\), and \(M_k\) for the maximum of \(r(n)\) on that interval. Then
\[
\boxed{B_k=\frac{(2+\sqrt2)^{k+1}+(2-\sqrt2)^{k+1}}4,\qquad U_k=3^k,\qquad M_k=F_{k+1},}
\]
where the Fibonacci numbers have \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). In particular,
\[
\#\big((\mathcal M+3\mathcal M)\cap[0,X]\big)=\Theta\big(X^{\log_4(2+\sqrt2)}\big)
\]
for real \(X\ge2\). This exponent is strictly between zero and one. Moreover, among the representable numbers in \([0,4^k)\), the proportion with a unique ordered representation tends to zero: \(U_k/B_k\to0\).

## Assumptions and scope

The symbols \(a,b,n,k\) denote nonnegative integers unless otherwise specified. Representations are *ordered* in that the first summand has coefficient one and the second coefficient three; each pair is counted once. Leading zeros are permitted in base-four digit strings, but they do not create additional representations. All formulas include \(n=0\) and \(k=0\). The result concerns the dilation three, not arbitrary coefficients.

The classical identity \(\mathcal M+2\mathcal M=\mathbb N_0\), with a unique ordered representation of each integer, motivates asking what survives when two is replaced by three. No analogous coverage or uniqueness property for the dilation three is assumed.

## Proof

**1. Exact digit-state recurrence.** Fix \(k\) and read the digits of \(n\in[0,4^k)\) from least significant to most significant. The four possibilities for each pair of digits of \(a,b\in\mathcal M\) contribute \(0,1,3,4\) before the incoming carry, respectively. The incoming and outgoing carries can only be zero or one. Let \((u,v)\) count the number of partial representations whose current carry is respectively zero and one. Starting from \((u,v)=(1,0)\), reading a digit \(d\in\{0,1,2,3\}\) transforms this pair as follows:
\[
\begin{array}{c|c}
 d&(u,v)\longmapsto\\\hline
 0&(u,u+v)\\
 1&(u+v,v)\\
 2&(v,0)\\
 3&(u,0).
\end{array}
\]
The first coordinate after all \(k\) digits is \(r(n)\): a nonzero final carry would force the nonnegative sum \(a+3b\) to be at least \(4^k\). Conversely any representation of \(n<4^k\) has both summands below \(4^k\), so its digits occur in the enumerated states. This proves the exact finite-state counting identity.

**2. Number of representable integers.** Ignore positive multiplicities but retain the set of currently possible carries. Starting from \(\{0\}\), the only nonempty reachable subsets are \(A=\{0\}\) and \(B=\{0,1\}\), with the empty subset dead. The transitions on digits \(0,1,2,3\) are
\[
 A\longmapsto(B,A,\varnothing,A),\qquad
 B\longmapsto(B,B,A,A).
\]
Both nonempty states are accepting because they contain carry zero. Let \(a_k,b_k\) count length-\(k\) strings ending in \(A,B\), with leading zeros included. Then
\[
\binom{a_{k+1}}{b_{k+1}}=
\begin{pmatrix}2&2\\1&2\end{pmatrix}\binom{a_k}{b_k},
\qquad(a_0,b_0)=(1,0),\qquad B_k=a_k+b_k.
\]
The matrix has characteristic polynomial \(x^2-4x+2\). Consequently \(B_0=1\), \(B_1=3\), and \(B_{k+2}=4B_{k+1}-2B_k\). Solving gives exactly the stated expression for \(B_k\). The map from length-\(k\) base-four strings to integers in \([0,4^k)\) is a bijection, including strings with leading zeros; hence no overcounting occurs.

**3. Number of unique representations.** Every reachable counting pair \((u,v)\) is either \((0,0)\), or has \(u\ge1\), \(v\ge0\). For these pairs set
\[
g(u,v)={\bf1}_{u=1},\quad
h(u,v)={\bf1}_{u=1,\ v\ge2}-{\bf1}_{u\ge2,\ v=1}.
\]
Let \(T_d\) be the four transformations in step 1. Direct substitution in the seven exhaustive cases \((0,0)\), \((1,0)\), \((1,1)\), \((1,v\ge2)\), \((u\ge2,0)\), \((u\ge2,1)\), and \((u\ge2,v\ge2)\) proves the two pointwise identities
\[
\sum_{d=0}^3h(T_d(u,v))=h(u,v),\qquad
\sum_{d=0}^3g(T_d(u,v))=3g(u,v)-h(u,v).
\]
Let \(H_k\) be the sum of \(h\) over all \(4^k\) digit strings of length \(k\), counted with multiplicity, and likewise let \(G_k\) be the sum of \(g\). The initial state \((1,0)\) has \(H_0=0\), \(G_0=1\). Summation of the pointwise identities over all strings shows \(H_{k+1}=H_k=0\) and \(G_{k+1}=3G_k-H_k=3G_k\). Since \(g=1\) precisely when the final representation count is one, \(U_k=G_k=3^k\).

**4. Maximum representation multiplicity.** For any reachable nonzero pair \((u,v)\) after \(k\) digits, sort its two coordinates in nonincreasing order. We claim they do not exceed \((F_{k+1},F_k)\) coordinatewise. This holds initially for \((1,0)\). For digit zero or one, the new coordinates are either \((u,u+v)\) or \((u+v,v)\); thus the larger is at most \(F_{k+1}+F_k=F_{k+2}\) and the smaller at most \(F_{k+1}\). Digits two and three reset one coordinate to zero and cannot exceed these bounds. This proves \(M_k\le F_{k+1}\).

Equality is attained at \(k=0,1\) by the initial state and digit zero, respectively. For even \(k\ge2\), the length-\(k\) digit string read least-significant first as repetitions of \(01\) yields \((u,v)=(F_{k+1},F_k)\). For odd \(k\ge3\), begin with \(001\) and continue with repetitions of \(01\); the final pair is again \((F_{k+1},F_k)\). Each identity is checked inductively using the first two digit transformations. Therefore \(M_k=F_{k+1}\).

**5. Growth and relative uniqueness.** Writing \(\lambda=2+\sqrt2\), \(\mu=2-\sqrt2\), we have \(0<\mu<1<\lambda<4\) and \(B_k=(\lambda^{k+1}+\mu^{k+1})/4\). Monotonicity between successive powers of four yields the asserted \(\Theta(X^{\log_4\lambda})\) bound. Finally \(3/\lambda<1\) implies \(U_k/B_k\to0\). This completes the proof.

## Verification

The standalone file `verify.py` independently enumerates all pairs of \(\mathcal M\)-elements with sums below \(4^k\) for \(0\le k\le7\). It checks individual multiplicities against the separate scalar recursion
\[
r(4m)=r(m)+r(m-1),\quad r(4m+1)=r(m),\quad r(4m+2)=0,\quad r(4m+3)=r(m)
\]
for \(m\ge0\), using \(r(-1)=0\), \(r(0)=1\), and avoiding recursive reuse of the \(m=0\) base equation. The verifier also checks the digit transitions by enumerating all four low-digit pairs and tests the three closed formulas by state propagation for \(1\le k\le14\).

The tested values of \(B_k\) for \(k=0,\ldots,7\) are \(1,3,10,34,116,396,1352,4616\). These finite checks are supporting reproducibility tests; the infinite claims follow from the proofs above.

## Relationship to prior work

The Moser–de Bruijn set and its unique representation property for \(\mathcal M+2\mathcal M\) are classical and recorded in OEIS A000695. Dekking's 2021 preprint develops substitution-based techniques for sumsets of automatic or morphic sequences and analyzes other specific examples, principally the Fibonacci, Thue–Morse, and von Neumann words. The numerical sequence \(1,3,10,34,116,\ldots\) is already recorded as OEIS A007052 with its recurrence \(B_{k+2}=4B_{k+1}-2B_k\); the sequence itself is not claimed as newly discovered.

The contribution here is the **joint arithmetic interpretation and theorem** for \(\mathcal M+3\mathcal M\): exact coverage, exact uniqueness count, and sharp Fibonacci maximum representation multiplicity. Neither the classical \(\mathcal M+2\mathcal M\) identity nor the abstract A007052 recurrence directly states these three properties. The argument supplies the base-four carry-state reduction needed to relate them. Prior methods may support alternative derivations; priority is not independently certified.

## Limitations

No classification is asserted for general dilations other than three, nor for arbitrary intervals of prescribed length. The \(\Theta\) counting estimate is an exponent statement, not a claimed constant-times-power asymptotic for arbitrary real cutoffs. The uniqueness count concerns exactly \([0,4^k)\), and the maximum multiplicity counts ordered pairs as defined above. The original literature may contain an unindexed equivalent or a readily derived corollary not isolated in the inspected sources.

## References

1. F. M. Dekking, *Sumsets and fixed points of substitutions*, arXiv:2105.04959, first submitted 11 May 2021; subsequent publication in *Proceedings of the American Mathematical Society, Series B* (2022).
2. OEIS Foundation, A000695, *Moser–de Bruijn sequence: sums of distinct powers of 4*; definitions and classical unique \(\mathcal M+2\mathcal M\) property.
3. OEIS Foundation, A007052, *Number of order-consecutive partitions of n*; numerical sequence and recurrence also arising in the present count.
