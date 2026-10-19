# Directional sign law and full-rank covariance for opposing permutation records

## Finding
Let \(X_1,\ldots,X_n\) be independent and identically distributed observations from any atomless distribution, with \(n\ge2\). Define the forward lower-record indicators and reverse upper-record indicators by
\[
 A_i=\mathbf 1\{X_i<\min_{k<i}X_k\},\qquad
 B_j=\mathbf 1\{X_j>\max_{k>j}X_k\},
\]
with the empty comparisons true. The entire indexed cross-covariance law is
\[
 \operatorname{Cov}(A_i,B_j)
 \begin{cases}
 =0& i<j,\\
 =0&i=j\in\{1,n\},\\
 <0&2\le i=j\le n-1,\\
 >0&i>j.
 \end{cases}
\]
In particular the square matrix
\[
 C_n=(\operatorname{Cov}(A_{r+1},B_c))_{1\le r,c\le n-1}
\]
has strictly positive determinant, so \(\operatorname{rank}(C_n)=n-1\). More strongly, every matrix having the same entrywise sign pattern, with strict signs retained, also has positive determinant (a sign-nonsingular matrix pattern). Hence no nonzero linear contrast of the nonconstant forward lower-record indicators is uncorrelated with every nonconstant backward upper-record indicator.

For integers \(1\le i,j\le n\), the joint probabilities are exactly
\[
 \Pr(A_i=B_j=1)=
 \begin{cases}
 \dfrac1{i(n-j+1)},&i<j,\\[6pt]
 \dfrac{(i-1)!(n-i)!}{n!},&i=j,\\[6pt]
 \dfrac{(n-i)!}{n!}\displaystyle\sum_{k=0}^{n-i}
 \dfrac{(i+k-1)!}{k!(i-j+k)},&i>j.
 \end{cases}
\]
The corresponding covariance is obtained by subtracting \(1/[i(n-j+1)]\). The formulas hold without asymptotic limits, for every atomless common distribution.

## Assumptions and scope
The observations are i.i.d., and the common distribution has no atoms. Applying their common distribution function preserves all record comparisons and yields i.i.d. uniforms on \((0,1)\), so the argument can use uniforms. Finite \(n\ge2\), indices \(1\le i,j\le n\); forward records detect new *minima*, backward records detect new *maxima*. This is distinct from two record types both scanned left to right, and distinct from position-indexed records in an inverse permutation. The indicators \(A_1\) and \(B_n\) are deterministic and are omitted from \(C_n\).

## Proof
**Marginals and disjoint case.** Exchangeability of independent continuous observations yields \(\Pr(A_i=1)=1/i\), \(\Pr(B_j=1)=1/(n-j+1)\). For \(i<j\), the two flags involve disjoint independent sets of observations, hence have covariance zero.

**The shared pivot.** For \(i=j\), write \(p=n-i\). The joint event says that \(X_i\) is smallest among the first \(i\) observations and largest among the final \(n-i+1\). For uniform observations, integrate over \(X_i=x\):
\[
 \Pr(A_i=B_i=1)=\int_0^1(1-x)^{i-1}x^p\,dx
 =\frac{(i-1)!p!}{n!}.
\]
For \(2\le i\le n-1\), conditionally on \(A_i\), \(X_i\) has distribution \(\operatorname{Beta}(1,i)\) and is strictly stochastically smaller than a fresh uniform variable. Because \(p>0\), \(\Pr(B_i=1\mid A_i)=\mathbb E[X_i^p\mid A_i]<1/(p+1)=\Pr(B_i=1)\). For \(i=1\) or \(i=n\), one indicator is constant; the covariance vanishes.

**Overlapping intervals with different pivots.** Suppose \(j<i\). Set \(d=i-j\ge1\), \(p=n-i\ge0\), and condition on \(A_i\). Then \(M=X_i\) has density \(i(1-m)^{i-1}\) on \((0,1)\). Conditional on \(M=m\), the \(i-1\) earlier observations are independent uniforms on \((m,1)\). In particular, the \(d\) observations from positions \(j\) through \(i-1\) have maximum \(m+(1-m)Z\), where \(Z\) has \(\operatorname{Beta}(d,1)\) distribution and is independent of \(M\). By symmetry, position \(j\) is the location of that block maximum with probability \(1/d\), independently of its value. All \(p\) observations after position \(i\) must be below it. Thus
\[
 \Pr(B_j=1\mid A_i=1)=\frac1d\mathbb E[(M+(1-M)Z)^p].
\]
Since \(M+(1-M)Z\ge Z\),
\[
 \Pr(B_j=1\mid A_i=1)
 \ge\frac1d\mathbb E[Z^p]
 =\frac1{d+p}
 >\frac1{d+p+1}=\Pr(B_j=1).
\]
The second inequality is strict for all \(d+p\ge1\), including \(p=0\), proving strictly positive covariance. Expanding the power in the preceding expectation and using beta integrals yields
\[
 \Pr(A_i=B_j=1)
 =\frac{p!}{n!}\sum_{k=0}^p\frac{(i+k-1)!}{k!(d+k)}.
\]
Indeed \(\mathbb E[M^{p-k}(1-M)^k]=i(p-k)!(i+k-1)!/n!\) and \(\mathbb E Z^k=d/(d+k)\). These establish all joint formulas.

**Sign-nonsingularity.** Put \(m=n-1\) and \(c_{rc}=\operatorname{Cov}(A_{r+1},B_c)\) for \(1\le r,c\le m\). The cases proved above show \(c_{rc}>0\) whenever \(c\le r\), \(c_{r,r+1}<0\) for \(r<m\), and \(c_{rc}=0\) whenever \(c\ge r+2\). The same pattern holds for any real square matrix \(H\) with these signs. Let \(D_0=1\), and let \(D_k\) denote the determinant of the leading \(k\)-by-\(k\) block of \(H\). Expanding \(D_k\) along its last row and then exploiting its upper-Hessenberg zero structure gives
\[
 D_k=\sum_{j=1}^{k} h_{kj}D_{j-1}
 \prod_{t=j}^{k-1}(-h_{t,t+1}),\qquad 1\le k\le m.
\]
The empty product is \(1\). Every \(h_{kj}>0\), every \(-h_{t,t+1}>0\), and induction gives every \(D_k>0\). Thus \(\det C_n>0\), uniformly over all strictly sign-preserving perturbations, proving rank \(n-1\) and the qualitative robustness claim.

## Verification
The standalone script `verify.py` uses exact fractions and exhaustive enumeration of all permutations through size seven to independently check every indexed joint probability. It also checks the predicted signs through size twelve and verifies determinants by two distinct methods (rational Gaussian elimination and the Hessenberg recurrence) through size eight. Run with `python3 verify.py` from the extracted package directory. This is a finite check of the formulas; the preceding conditional-probability and determinant arguments are the proof for every \(n\).

## Relationship to prior work
Classical records are commonly treated through forward initial ranks and their count distributions; see Gnedin's 2006 study of upper and lower records (both evaluated in one direction). Gnedin and Gorin (2012) analyze measures depending on forward record sets. Jin (2022) obtains generating functions for jointly counted left-to-right minima and right-to-left maxima—exactly the two total-count families involved here. Differentiating a joint *count* generating function gives aggregate covariance but does not supply the position-indexed signs or rank without additional work. The present object is the complete indexed opposite-direction record covariance operator; its positivity/negativity region and sign-nonsingular rank assertion are not established by the inspected cited statements. No independent priority determination is claimed.

## Limitations
The cross-covariance matrix is a second-order, linear dependence statement. Full rank does not mean the two record vectors are probabilistically independent or mutually reconstructible. The result assumes identically distributed atomless observations; heterogeneity and ties are not covered. A literature-wide implicit consequence of older, more general position-marked record identities remains possible, including sources not fully accessible during this study. All verification counts are finite, and no independent scientific audit has been performed.

## References
1. A. Gnedin, *Coherent random permutations with record statistics* (first arXiv version 2006-11-17), arXiv:math/0611538, https://arxiv.org/abs/math/0611538.
2. A. Gnedin and V. Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680, https://arxiv.org/abs/1202.3680.
3. E. Y. Jin, *Symmetric generating functions and Euler-Stirling statistics on permutations*, arXiv:2210.08789 (first public version 2022-10-17), https://arxiv.org/abs/2210.08789.
4. K. Borovkov and D. Pfeifer, *On record indices and record times*, Journal of Statistical Planning and Inference (1995), DOI:10.1016/0378-3758(94)00063-8; only bibliographic and abstract-level material was accessible for this study.
