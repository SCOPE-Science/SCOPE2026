# Exact mean and variance of nonbinary two-deletion shadows

## Finding
For every integer \(q\ge 3\) and \(n\ge2\), let \(X\) be uniformly distributed over all length-\(n\) words on a \(q\)-symbol alphabet. Let \(B(X)\) be the number of **distinct** length-\(n-2\) subsequences of \(X\), obtainable by deleting exactly two positions. Put \(m=n-1\), \(p=(q-1)/q\) and \(h=1/q\). Then
\[
\mathbb E B(X)=1+(m-1)p+\binom m2p^2,
\]
and
\[
\boxed{\operatorname{Var}(B(X))=(m-1)ph\left[-1+2p+\frac{mp}{2}+\frac{m(2m-3)p^2}{2}\right].}
\]
In particular, for each fixed \(q\ge3\),
\[
\operatorname{Var}(B(X))=\frac{(q-1)^3}{q^4}n^3+O_q(n^2),
\quad \operatorname{sd}(B(X))\sim\frac{(q-1)^{3/2}}{q^2}n^{3/2}.
\]
This is a finite-length exact second-moment law, not an asymptotic assertion about a coding ensemble or deletion-ball intersections.

## Assumptions and scope
The alphabet consists of \(q\) symbols; no finite-field structure is necessary. The uniform input coordinates are independent. Exactly two arbitrary positions are deleted, and multiple ways of producing the same retained sequence count only once. The result covers all integers \(q\ge3\) and \(n\ge2\), including \(n=2\), where \(B(X)=1\). The known binary case is deliberately excluded from the new theorem.

For a deterministic word \(x=x_1\cdots x_n\), write \(m=n-1\) and
\[
T_i={\bf1}_{\{x_i\ne x_{i+1}\}}\quad(1\le i\le m),\quad M=\sum_{i=1}^{m}T_i,
\]
\[
A_i={\bf1}_{\{x_i=x_{i+1}\ne x_{i+2}\}},\quad
C_i={\bf1}_{\{x_i=x_{i+2}\ne x_{i+1}\}}\quad(1\le i<m).
\]

## Proof
**1. A deterministic canonical-deletion identity.** Each output has a unique *leftmost greedy* embedding in \(x\); its two deleted positions are therefore a unique canonical pair \(i<j\). A pair is canonical precisely when every omitted symbol lies strictly before the first eligible retained copy of that symbol. More explicitly: (a) \((n-1,n)\) is always canonical; (b) \((i,n)\), for \(i\le n-2\), is canonical exactly when \(T_i=1\); (c) a nonadjacent pair \((i,j)\) with \(j<n\) is canonical exactly when \(T_i=T_j=1\); (d) an adjacent pair \((i,i+1)\) with \(i+1<n\) is canonical exactly when both \(x_i\) and \(x_{i+1}\) differ from \(x_{i+2}\). These conditions follow directly by comparing each skipped block with the following retained letter in the greedy matching algorithm. Thus, writing \(J_i={\bf1}_{\{x_i\ne x_{i+2},\ x_{i+1}\ne x_{i+2}\}}\),
\[
B(x)=1+\sum_{i=1}^{m-1}T_i+\sum_{1\le i<j\le m,\ j\ge i+2}T_iT_j+\sum_{i=1}^{m-1}J_i.
\]
For each \(i<m\), the elementary case partition of triples yields \(J_i-T_iT_{i+1}=A_i-C_i\), and hence
\[
\boxed{B(x)=1+F(M)-T_m+\sum_{i=1}^{m-1}(A_i-C_i),\qquad F(v)=v(v+1)/2.}
\]
All identities remain meaningful at \(n=2\), with empty sums.

**2. Independence and local cancellation.** Identify alphabet labels with residues modulo \(q\), and set \(U_i=X_{i+1}-X_i\pmod q\). The invertible map \((X_1,U_1,\ldots,U_m)\leftrightarrow X\) shows that \(U_i\) are independent uniform residues and that \(T_i={\bf1}_{\{U_i\ne0\}}\) are independent Bernoulli\((p)\). Thus \(M\) is binomial with parameters \((m,p)\).

Put \(Z_i=A_i-C_i\) and \(Z=\sum_{i<m}Z_i\). In increment notation, \(A_i\) is \(U_i=0,U_{i+1}\ne0\) and \(C_i\) is \(U_i\ne0,U_{i+1}=-U_i\). Therefore
\[
\mathbb E Z_i=0,\qquad \mathbb E Z_i^2=2ph.
\]
Nonneighboring \(Z_i\)'s depend on disjoint increments and are independent. For neighboring indices the only nonzero signed products are \(-A_iC_{i+1}\) and \(+C_iC_{i+1}\), each of probability \(ph^2\), so their expectations cancel. It follows that
\[
\operatorname{Var}(Z)=2(m-1)ph.
\]
Moreover \(\operatorname{Cov}(T_m,Z)=0\), including at \(i=m-1\), since both \(A_{m-1}\) and \(C_{m-1}\) force \(T_m=1\) and have the same probability \(ph\).

**3. Polynomial moment calculation.** Since \(F(M)=\sum_iT_i+\sum_{i<j}T_iT_j\), grouping products by overlapping index sets gives
\[
\operatorname{Var}(F(M))=mph+\binom m2p^2h(5+p)+6\binom m3p^3h,
\]
\[
\operatorname{Cov}(F(M),T_m)=ph+(m-1)p^2h.
\]
Conditioning on all \(T\)'s except \(T_i,T_{i+1}\), the event \(A_i\) has the pair \((0,1)\), whereas \(C_i\) has \((1,1)\), each with probability \(ph\). The difference in \(F(M)\) is \(-H-2\), where \(H=\sum_{j\notin\{i,i+1\}}T_j\). As \(\mathbb EH=(m-2)p\),
\[
\operatorname{Cov}(F(M),Z)=-(m-1)ph\bigl((m-2)p+2\bigr).
\]
Consequently, applying the deterministic identity and combining the displayed terms,
\[
\begin{aligned}
\operatorname{Var}(B)&=\operatorname{Var}(F(M)) +\operatorname{Var}(T_m)+\operatorname{Var}(Z)\\
&\quad-2\operatorname{Cov}(F(M),T_m)+2\operatorname{Cov}(F(M),Z)\\
&=(m-1)ph\left[-1+2p+\frac{mp}{2}+\frac{m(2m-3)p^2}{2}\right].
\end{aligned}
\]
Taking expectations of \(B=1+F(M)-T_m+Z\) yields \(1+(m-1)p+\binom m2p^2\). The leading cubic coefficient follows immediately and is strictly positive for \(q\ge3\). This completes the proof.

## Verification
The standalone `check.py` enumerates every \(q\)-ary input word in the ranges \(q=2,\ 2\le n\le12\); \(q=3,\ 2\le n\le9\); \(q=4,\ 2\le n\le7\); \(q=5,\ 2\le n\le6\). For each input it directly constructs the set of distinct deletion outputs, independently evaluates the canonical-deletion identity, and compares empirical rational first and second moments against the formulas. The executable was run and checked all \(79{,}073\) inputs, with output recorded in `check_output.txt`. The binary cases serve only as an additional consistency check against existing work; no binary originality is claimed. Exhaustive finite experiments corroborate, but do not replace, the proof for all lengths and alphabet sizes.

## Relationship to prior work
Wang, Li and Fu (2026, arXiv:2609.16837) study extremal *intersections* of \(q\)-ary deletion balls and worst-case reconstruction; neither these extremes nor their asymptotics specify the variance of the **size of one random two-deletion shadow**. A 2026 publicly accessible result titled “Exact variance of binary two-deletion sphere size” establishes the special case \(q=2\), with variance \((n-1)(n-2)(2n-3)/32\); its statement expressly excludes nonbinary alphabets. Substitution \(p=h=1/2\) in the identity above recovers that number without claiming it is new. Swart and Ferreira provide per-word double-deletion combinatorics, and Biers-Ariel and collaborators examine averages of distinct subsequences in random binary strings; neither inspected comparison supplies this exact nonbinary two-deletion variance. The new ingredient is the alphabet-uniform canonical-pair identity and a nonbinary local covariance cancellation.

## Limitations
This establishes only the first two moments of the *exactly two-deletion* shadow of a uniform word, not its full distribution, nonuniform-source variance, higher deletion radii, or intersections of two shadows. The publication comparison covers identifiable relevant results and does not prove the absence of all unindexed or differently formulated earlier work. The proof is self-contained; independent audit has not been performed.

## References
1. X. Wang, H. Li and F.-W. Fu, “On Sequence Reconstruction Problem for q-ary Deletion Channels,” arXiv:2609.16837, first submitted 2026-09-15.
2. T. G. Swart and H. C. Ferreira, “A note on double insertion/deletion correcting codes,” IEEE Trans. Inf. Theory 49(1), 269–273, DOI:10.1109/TIT.2002.806155.
3. N. Biers-Ariel et al., “Expected Number of Distinct Subsequences in Randomly Generated Binary Strings,” arXiv:1704.08643.
4. “Exact variance of binary two-deletion sphere size,” public result (2026), identifier `2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc`.
