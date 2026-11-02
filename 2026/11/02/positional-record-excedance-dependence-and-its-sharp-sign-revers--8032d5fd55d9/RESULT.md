# Positional record–excedance dependence and its sharp sign reversal

## Finding
Let \(\pi\) be uniform on the permutations of \(\{1,\ldots,n\}\), with \(n\ge2\). Write \(R_i=\mathbf1\{\pi_i=\max(\pi_1,\ldots,\pi_i)\}\), \(E_j=\mathbf1\{\pi_j>j\}\), \(R=\sum_i R_i\), and \(X=\sum_j E_j\). For every \(1\le i,j\le n\), the full cross-covariance matrix is
\[
\operatorname{Cov}(R_i,E_j)=
\begin{cases}
0,&i=1\text{ or }j>i,\\
-\dfrac{j}{ni(i-1)},&2\le i\text{ and }j<i,\\
\dfrac1n-\dfrac1{i\binom ni},&j=i\ge2.
\end{cases}
\tag{1}
\]
Consequently,
\[
\operatorname{Cov}(R_i,X)=\frac1{2n}-\frac1{i\binom ni}\quad(2\le i\le n),
\qquad \operatorname{Cov}(R_1,X)=0.
\tag{2}
\]
For every \(n\ge4\), this covariance is strictly positive at every interior record position \(2\le i\le n-1\) and strictly negative at the final position \(i=n\). At \(n=3\) the interior value is zero. The full record/excedance covariance has a sharp sign transition:
\[
\operatorname{Cov}(R,X)=\frac{n-1}{2n}
-\frac1n\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}
\begin{cases}<0,&2\le n\le4,\\>0,&n\ge5,\end{cases}
\tag{3}
\]
with respective values \(-1/4,-1/6,-1/24\) for \(n=2,3,4\), and
\[
\operatorname{Cov}(R,X)=\frac12-\frac3{2n}+O(n^{-2}).
\tag{4}
\]
The covariance limit is \(1/2\), whereas \(\operatorname{Corr}(R,X)\sim\sqrt3/\sqrt{n\log n}\), using the classical record and Eulerian marginal variances.

## Assumptions and scope
The permutations are fully uniform; record means a **strict upper left-to-right record**, and excedance means a value strictly exceeding its absolute one-based position. The entries \(R_i,E_j\) are indicator random variables. All formulas are exact for the stated integer indices, including the cases \(i=1\), \(i=n\), and \(j=n\). In particular, the first record indicator is constant and the final excedance indicator is zero. Equation (3) concerns uniform permutations only, not arbitrary nonuniform record-biased permutations or pattern-avoiding families.

## Proof
For each \(i\), let \(S_i=\{\pi_1,\ldots,\pi_i\}\). The unordered set \(S_i\) is a uniformly sampled \(i\)-subset of \(\{1,\ldots,n\}\), independent of the relative ordering of the first \(i\) entries. Thus \(\Pr(R_i=1)=1/i\), and conditioning on \(R_i=1\) does not change the uniform law of \(S_i\).

If \(1\le j<i\), conditional on \(R_i=1\), the value \(\pi_j\) is uniform among the \(i-1\) elements of \(S_i\) other than \(\max S_i\). As \(i>j\), every \(i\)-subset contains an element above \(j\), so \(\max S_i>j\) surely. The number of selected elements above \(j\) has expectation \(i(n-j)/n\). Removing the certain maximum yields
\[
\Pr(E_j=1\mid R_i=1)=\frac{i(n-j)/n-1}{i-1}.
\]
Subtracting \(\Pr(E_j=1)=(n-j)/n\) and multiplying by \(\Pr(R_i=1)=1/i\) gives the strictly negative lower-triangular entry in (1).

For \(j=i\), the record value is \(\max S_i\). Its excedance fails precisely when all \(i\) selected values lie at most \(i\), which occurs with probability \(\binom ni^{-1}\). Therefore
\[
\Pr(E_i=1\mid R_i=1)=1-\binom ni^{-1}
\]
and the diagonal entry follows. For \(j>i\), the relative ordering of the first \(i\) values is uniformly distributed even after fixing \(\pi_j\); hence \(R_i\) is independent of \(E_j\). The case \(i=1\) is constant. This proves every entry of (1).

For \(i\ge2\), sum (1) over \(j\). Since \(\sum_{j=1}^{i-1}j=i(i-1)/2\), the row sum is exactly (2). When \(2\le i\le n-1\), \(i\binom ni=n\binom{n-1}{i-1}\ge n(n-1)\). Hence (2) is positive for \(n\ge4\), vanishes at the only interior case \(n=3,i=2\), and is negative at \(i=n\), where it equals \(-1/(2n)\).

Summing (2) over \(i\), and using \(i\binom ni=n\binom{n-1}{i-1}\), proves the exact sum in (3). Direct substitution gives its three negative small-size values. For \(n\ge5\), put \(h=n-1\ge4\). Since \(\binom hk\ge\binom h2\) for \(2\le k\le h-2\),
\[
\sum_{k=1}^h\binom hk^{-1}
\le1+\frac2h+\frac{2(h-3)}{h(h-1)}<2\le\frac h2.
\]
The strict middle inequality follows from \(h^2-5h+8>0\); it proves positivity in (3) for all \(n\ge5\). Moreover the displayed bound and the obvious lower bound \(1\) imply \(\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}=1+O(1/n)\), yielding (4).

For the last assertion, the independent initial-rank representation of uniform permutations gives \(\operatorname{Var}(R)=H_n-\sum_{i=1}^n i^{-2}=\log n+O(1)\). The classical Eulerian variance is \(\operatorname{Var}(X)=(n+1)/12\) for \(n\ge2\). Combining these known marginals with (4) gives the stated correlation asymptotic. None of the marginal variance formulas is claimed as new.

## Verification
Run the standalone Python 3 standard-library script `verify.py` from the same directory. It independently enumerates all \(n!\) permutations for every \(1\le n\le8\), computes the entire record–excedance cross-moment table, and compares its exact rational covariances with (1)–(3). It separately tests each rational finite-size sign and row formula through \(n=1000\). This program reports 500825 exact assertions passed. Enumeration is finite corroboration, not a proof of the all-size claims: those follow from the preceding subset argument and inequalities.

## Relationship to prior work
Ehrenborg and Steingrímsson (2000) give the excedance-set enumerator and recurrences, not a conditional record/excedance cross-covariance matrix. Gnedin's record-statistics study (first publicly posted in 2006) develops the independent initial-rank viewpoint and record-biased permutation laws, without the absolute-position excedance conditioning used here. Brändén and Claesson (2011) represent both left-to-right maxima and excedances as mesh-pattern statistics, but their general expansion does not itself evaluate their position-resolved joint moments or prove the sign boundary at five. Classical record independence and Eulerian moments are used only as acknowledged inputs to the correlation consequence. The result concerns mixed dependence of these specific statistics, not new marginal distributions, a new Eulerian enumerator, or a new record generating function.

## Limitations
The model is uniform and one-line, so the asserted signs are not claimed for nonuniform random permutations, multiset permutations, inverse records, generalized excedances, or separately weighted record positions. This analysis does not establish a joint central limit theorem. The exact sign classification and covariance kernel have been checked against the cited closely relevant accessible primary texts and searchable literature, but historical priority cannot be certified exhaustively; earlier general joint refinements might encode specializations requiring further comparison. No independent audit has been performed.

## References
- Richard Ehrenborg and Einar Steingrímsson, *The Excedance Set of a Permutation*, Advances in Applied Mathematics 24 (2000), 284–299, DOI: https://doi.org/10.1006/aama.1999.0671 ; author-hosted text: https://www.ms.uky.edu/~jrge/Papers/Excedance.pdf.
- Alexander Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first submitted 2006-11-17, https://arxiv.org/abs/math/0611538 ; DMTCS proceedings full text: https://dmtcs.episciences.org/en/articles/3551/download.
- Petter Brändén and Anders Claesson, *Mesh Patterns and the Expansion of Permutation Statistics as Sums of Permutation Patterns*, Electron. J. Combin. 18(2) (2011), #P5, arXiv:1102.4226 first submitted 2011-02-21, https://arxiv.org/abs/1102.4226.
