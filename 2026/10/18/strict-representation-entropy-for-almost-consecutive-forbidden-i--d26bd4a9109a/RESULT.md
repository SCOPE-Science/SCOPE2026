# Strict representation entropy for almost-consecutive forbidden-index decompositions

## Finding
For integers \(k,c\) with \(1\le c\) and \(2c<k\), set \(S=[k]\setminus\{k-c\}\). Define the \(S\)-legal index-difference sequence \((a_n)_{n\ge1}\) by \(a_n=\operatorname{mex}_{>0}\{\sum_{i\in I}a_i:I\subseteq[n-1],\ |i-j|\notin S\text{ for distinct }i,j\in I\}\). Assume that the sequence eventually satisfies \(a_{n+1}=a_n+a_{n-k}\). This assumption holds, in particular, for every \(c=1,k\ge11\); it holds for every fixed \(c\) and all sufficiently large \(k\) by the cited recurrence theorem.

Let \(R(m)\) count all finite \(S\)-legal subsets \(I\subseteq\mathbb N\) such that \(\sum_{i\in I}a_i=m\), with \(R(0)=1\). Define the mean representation multiplicity on the natural initial interval
\[
B_n=\frac1{a_n}\sum_{0\le m<a_n} R(m).
\]
Let \(\lambda_k>1\) and \(\rho_{k,c}>1\) denote the unique real roots greater than one of
\[
(x-1)x^k=1,\qquad (x-1)(x^k-x^c)=1,
\]
respectively. Then \(1<\lambda_k<\rho_{k,c}\), and there exist constants \(0<C_1\le C_2<\infty\) and \(N\), depending only on \(k,c\), such that for every integer \(n\ge N\),
\[
C_1\bigl(\rho_{k,c}/\lambda_k\bigr)^n\le B_n\le
C_2\bigl(\rho_{k,c}/\lambda_k\bigr)^n.
\]
In particular,
\[
\lim_{n\to\infty}B_n^{1/n}=\rho_{k,c}/\lambda_k>1.
\]
For the smallest explicitly covered singleton-exception case \(k,c\)=(11,1), the exponential base is approximately \(1.011434032776\).
For each fixed positive integer \(c\), as \(k\to\infty\) through the proved recurrence range, the strict entropy excess has the sharp scale
\[
\log\bigl(\rho_{k,c}/\lambda_k\bigr)\sim W(k)/k^2,
\]
where \(W(k)>0\) is defined by \(W(k)e^{W(k)}=k\). The two limiting processes are distinct: first \(n\to\infty\) for fixed \(k,c\), then optionally \(k\to\infty\) for fixed \(c\).

## Assumptions and scope
All indices are positive integers, \([k]=\{1,\ldots,k\}\), and only finite subsets with distinct indices enter a legal decomposition. The exclusion \(S\) forbids pairwise differences \(1,\ldots,k\) except for the single allowed difference \(k-c\); differences exceeding \(k\) are allowed. The recurrence hypothesis is explicit because its validity for all small \(k,c\) is not established. Its unconditional subfamily \(c=1,k\ge11\) follows from Dantas e Moura et al., Theorem 3.10 and Example 3.11 (arXiv:2210.10577v2). The objects \(R(m)\) and \(B_n\) count decompositions with their multiplicity, not merely representable integers.

## Proof
**1. Number of legal index sets.** Let \(d_n\) count \(S\)-legal subsets of \([n]\), including the empty subset, with \(d_0=1\). Partition them according to whether \(n\) is present. If it is absent, there are \(d_{n-1}\) choices. If \(n\) is present, the only additional index in \([n-k,n-1]\) that may appear is \(n-k+c\). When this index is absent, all further chosen indices lie in \([n-k-1]\), giving \(d_{n-k-1}\) choices. When it is present, the earlier indices form an arbitrary legal subset whose largest index is \(n-k+c\). The number of these is \(d_{n-k+c}-d_{n-k+c-1}\). Indeed, \(2c<k\) guarantees that any index compatible with \(n-k+c\) is also compatible with \(n\): a compatible earlier index is at most \(n-2k+2c\), which is less than \(n-k\). Hence for every \(n>k+1\),
\[
d_n=d_{n-1}+d_{n-k+c}-d_{n-k+c-1}+d_{n-k-1}.
\]
The characteristic polynomial is
\[
P_{k,c}(x)=x^{k+1}-x^k-x^{c+1}+x^c-1=(x-1)(x^k-x^c)-1.
\]

**2. A simple, strictly dominant positive root.** Track the last \(k\) selection bits of an \(S\)-legal index set. Appending zero is always permitted; appending one is permitted exactly when no earlier selected bit has forbidden distance. These rules give a finite nonnegative transfer matrix on the set of admissible length-\(k\) words. Each such word is reachable from the zero word by appending its bits, each state returns to zero by appending \(k\) zeros, and zero has a self-loop. Thus the matrix is primitive. Perron--Frobenius implies
\[
d_n=\beta\rho^n(1+O(\eta^n))
\]
for some \(\beta>0\), \(\rho>1\), \(0<\eta<1\). The inequality \(\rho>1\) follows independently by choosing arbitrary subsets of indices \(1,1+(k+1),\ldots\), yielding \(d_n\ge2^{\lfloor(n-1)/(k+1)\rfloor+1}\). Inserting the asymptotic into the exact recurrence forces \(P_{k,c}(\rho)=0\). Since \((x-1)(x^k-x^c)\) is continuous and strictly increasing from zero to infinity for \(x>1\), this root is the uniquely defined \(\rho_{k,c}\). No assumption of distinct characteristic roots is needed.

**3. Growth of the underlying greedy sequence.** By the stated eventual recurrence, the vector of \(k+1\) consecutive terms is advanced by a nonnegative companion matrix for \(x^{k+1}-x^k-1\). Its directed graph contains cycles of coprime lengths \(1\) and \(k+1\), so it is primitive. (Equivalently, the recurrence has a positive self-loop and a return path from every coordinate.) Because the starting terms are positive, Perron--Frobenius gives \(a_n=\alpha\lambda_k^n(1+o(1))\) with \(\alpha>0\), where \(\lambda_k\) is the unique positive solution \(x^k(x-1)=1\). Both \(\rho_{k,c}\) and \(\lambda_k\) are therefore genuine exponential growth constants.

**4. Strict root separation.** At \(x=\lambda_k\),
\[
P_{k,c}(\lambda_k)=-(\lambda_k-1)\lambda_k^c<0.
\]
By the strict monotonicity of \((x-1)(x^k-x^c)\) on \(x>1\), its unique level-one point must lie strictly above \(\lambda_k\). Hence \(\rho_{k,c}>\lambda_k\).

**5. The truncated multiplicity average.** Since \(a_i\) increases and \(m<a_n\), no representation of \(m\) can use an index at least \(n\). Therefore
\[
\sum_{0\le m<a_n}R(m)\le d_{n-1}.
\]
As \(a_i\sim\alpha\lambda_k^i\) and \(\lambda_k>1\), choose a *fixed* integer \(L\) so large that \(\lambda_k^{1-L}/(\lambda_k-1)<1\). Then
\[
\frac{\sum_{i=1}^{n-L}a_i}{a_n}\longrightarrow
\frac{\lambda_k^{1-L}}{\lambda_k-1}<1.
\]
Thus, for all sufficiently large \(n\), every legal subset of \([n-L]\) has its sum strictly below \(a_n\). In particular, even when distinct subsets share one sum, both are counted and
\[
d_{n-L}\le \sum_{0\le m<a_n}R(m)\le d_{n-1}.
\]
Combine this sandwich with \(d_n\asymp\rho_{k,c}^n\) and \(a_n\asymp\lambda_k^n\). The displayed two-sided exponential estimate and the \(n\)-th-root limit follow.

**6. Large-\(k\) scale for fixed \(c\).** Write \(\lambda_k=1+u_k\) and \(w_k=ku_k\). The defining equation is \(u_k(1+u_k)^k=1\), and taking logarithms gives \(w_k\sim W(k)\), \(w_k\to\infty\), \(u_k=w_k/k\to0\). Put \(\delta_k=\rho_{k,c}-\lambda_k\). The function \(P_{k,c}\) is \(-u_k\lambda_k^c\) at \(\lambda_k\), while
\[
P'_{k,c}(\lambda_k)=u_k^{-1}+k/\lambda_k-\lambda_k^c-c u_k\lambda_k^{c-1}.
\]
For fixed \(c\), Taylor's theorem at \(\lambda_k\), with the second derivative bounded by \(O(k/u_k+k^2)\) throughout the interval \(0\le x-\lambda_k\le2u_k/k\), gives
\[
P_{k,c}(\lambda_k+2u_k/k)
=-u_k\lambda_k^c+\frac{2u_k}{k}
\left(u_k^{-1}+\frac{k}{\lambda_k}-\lambda_k^c-c u_k\lambda_k^{c-1}\right)
+O(u_k^2+u_k/k)=u_k(1+o(1))>0.
\]
(The derivative bound follows directly by differentiating \(P_{k,c}\) twice and using \(\lambda_k^k=1/u_k\); the \(k\)-power changes by a relative \(O(u_k)\) over the short interval.) The unique root therefore has \(0<\delta_k=O(u_k/k)\). Throughout that interval the derivative above varies by relative \(o(1)\), because \(k\delta_k=O(u_k)=o(1)\). The mean-value theorem therefore gives
\[
\delta_k=\frac{u_k^2}{1+ku_k}(1+o(1)).
\]
Since \(\lambda_k\to1\),
\[
\log(\rho_{k,c}/\lambda_k)
=\frac{w_k^2}{k^2(1+w_k)}(1+o(1))\sim W(k)/k^2.
\]
This asymptotic uses only fixed \(c\), not growing \(c\).

## Verification
Run `python3 VERIFY.py` with standard Python 3. The script constructs legal subsets with exact integer sums and independently checks their greedy mex sequence; it compares the resulting subset counts with a finite-state transfer algorithm and with the exact recurrence, evaluates root separation by bisection, and checks explicit finite multiplicity averages. In the executed checks all 18 parameter tests passed, including the greedy recurrence for \((k,c)=(11,1),(12,1),(14,1)\), count recurrences for several \(c>1\), and strict root separation for ten parameter choices. This finite testing is corroboration, not a proof of the universal or asymptotic statements; those are proved in Steps 1--6.

## Relationship to prior work
Dantas e Moura, Keisling, Lilly, Mauro, Miller, Phang, and Velazquez Iannuzzelli (2022/2023), arXiv:2210.10577v2, give the definition of \(S\)-LID sequences, a recurrence criterion (Theorem 3.10), a special bound for \(c=1\) (Example 3.11), and the count recurrence (Lemma 4.1). Their Section 4, Question 5, asks about average representation multiplicities; it describes the *conditional* possibility of an exponential rate when a suitable count root exceeds the sequence root. The present theorem proves that strict inequality uniformly, removes the assumed root simplicity/dominance through a primitive transfer matrix, and establishes an unconditional quantitative answer throughout the published recurrence range, plus its sharp fixed-\(c\) large-\(k\) scale. The count recurrence and the underlying sequence recurrence are prior results and are not claimed as new.

Catral, Ford, Harris, Miller, and Nelson, arXiv:1606.09312v2 (2016), proved analogous exponential mean multiplicity for Fibonacci quilt decompositions, a different admissibility rule. That method motivates the truncation sandwich, but its theorem does not cover the \([k]\setminus\{k-c\}\) family or the explicit strict entropy gap. No claim of global priority is made beyond the inspected evidence.

## Limitations
The universal statement is conditional on eventual recurrence of the greedy sequence, which is established for the cited infinite families but remains unproved for every small \(k,c\). The estimate gives a sharp exponential base, not the limiting multiplicative constant in \(B_n\sim C(\rho/\lambda)^n\). The large-\(k\) asymptotic assumes \(c\) fixed. The search of accessible literature and mathematical records cannot rule out unindexed overlapping work. There has been no independent mathematical audit.

## References
1. G. Z. Dantas e Moura, A. Keisling, A. Lilly, A. Mauro, S. J. Miller, M. Phang, and S. Velazquez Iannuzzelli, *Recurrence Relations for S-Legal Index Difference Sequences*, arXiv:2210.10577v2, first posted 2022-10-19, especially Theorem 3.10, Example 3.11, Lemma 4.1, and Section 4 Question 5. https://arxiv.org/html/2210.10577v2
2. M. Catral, P. L. Ford, P. E. Harris, S. J. Miller, and D. Nelson, *Legal Decompositions Arising from Non-positive Linear Recurrences*, arXiv:1606.09312v2, posted 2016-06-30, especially Theorem 1.11 and Section 3. https://arxiv.org/html/1606.09312v2
