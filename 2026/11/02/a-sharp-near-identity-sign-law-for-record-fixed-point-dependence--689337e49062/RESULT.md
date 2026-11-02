# A sharp near-identity sign law for record–fixed-point dependence in uniform permutations

## Finding

For a uniformly random permutation \(\pi\) of \([n]\), let \(R\) be its number of strict left-to-right upper records, let \(F\) be its number of fixed points, and let
\[
w_n(r,f)=\#\{\pi\in S_n:R(\pi)=r,\ F(\pi)=f\}.
\]
For every integer \(n\ge3\) and every integer \(1\le r\le n-1\), the exact near-identity rows are
\[
 w_n(r,n-2)=r,\qquad
 w_n(r,n-3)=(2r-1)n-2r^2.
\]
For every integer \(1\le r\le n-2\), their adjacent two-by-two minor is
\[
\boxed{w_n(r,n-3)w_n(r+1,n-2)-w_n(r,n-2)w_n(r+1,n-3)=2r(r+1)-n.}
\]
Consequently, the conditional mass ratio \(\Pr(R=r\mid F=n-2)/\Pr(R=r\mid F=n-3)\), when read in increasing order of \(r\), decreases where \(2r(r+1)<n\) and increases where \(2r(r+1)>n\), with equality at the possible integer threshold \(n=2r(r+1)\). All these masses are positive for \(1\le r\le n-1\).

The full joint \((R,F)\) count matrix is totally positive of order two (TP2) for \(2\le n\le4\) but **fails TP2 for every \(n\ge5\)**, because its minor at \(r=1\) equals \(4-n<0\). Five is the sharp first failure.

Despite that likelihood-ratio-order failure, for every integer \(n\ge2\),
\[
\boxed{\operatorname{Cov}(R,F)=\frac1n\sum_{j=1}^{n-1}\binom{n-1}{j}^{-1}>0.}
\]
Thus positive linear association does not force total positivity or conditional likelihood-ratio monotonicity. The contrast is especially sharp because permutation cycle counts and record counts have equal *marginal* distributions, whereas their respective joint dependences on fixed points differ.

## Assumptions and scope

Each permutation of \([n]=\{1,\dots,n\}\) has probability \(1/n!\); positions and values use one-based indexing. An index \(i\) is an upper record precisely if \(\pi(i)>\max\{\pi(1),\dots,\pi(i-1)\}\), with position one always a record. A fixed point satisfies \(\pi(i)=i\). The TP2 convention for this statement is
\[
 w_n(r,f)w_n(s,g)-w_n(r,g)w_n(s,f)\ge0
 \quad\text{whenever }r<s\text{ and }f<g.
\]
Structural formulas apply for all \(n\ge3\); the covariance identity applies also at \(n=2\). The all-minor positive boundary is explicitly checked for \(n=2,3,4\), while the negative witness is analytic for all larger \(n\). No independence or asymptotic approximation is assumed.

## Proof

**1. One transposition.** A permutation with exactly \(n-2\) fixed points consists of one transposition interchanging values at positions \(a<b\). The record positions removed from the identity permutation are exactly \(a+1,\dots,b\); hence \(R=n-(b-a)\). Exactly \(n-d\) transpositions have span \(d=b-a\). Taking \(d=n-r\) proves \(w_n(r,n-2)=r\) for \(1\le r\le n-1\).

**2. One three-cycle.** A permutation with exactly \(n-3\) fixed points consists of one three-cycle on \(a<b<c\). Each triple admits two orientations. The orientation \(a\mapsto b,b\mapsto c,c\mapsto a\) has \(R=n-(c-a)+1\); the other orientation \(a\mapsto c,b\mapsto a,c\mapsto b\) has \(R=n-(c-a)\). For a given span \(d=c-a\), there are \((n-d)(d-1)\) triples. Their contributions to the count with \(R=r\) are therefore \((r-1)(n-r)\) and \(r(n-r-1)\), respectively. Summing gives \(w_n(r,n-3)=(2r-1)n-2r^2\). Both terms are nonnegative on the stated range and their sum is positive.

**3. Exact minors and sharp TP2 boundary.** Write \(A_r=(2r-1)n-2r^2\) and \(B_r=r\). Direct cancellation yields
\[
 A_rB_{r+1}-B_rA_{r+1}=2r(r+1)-n.
\]
Because \(A_r>0\), consecutive differences in \(B_r/A_r\) have precisely this sign. Conditioning multiplies \(B_r/A_r\) by the same positive constant for every \(r\), so the conditional likelihood-ratio sequence has the same sign changes. At \(r=1\), the minor is \(4-n\), strictly negative for \(n\ge5\). For the remaining cases, exhaustive finite enumeration gives the following complete joint count tables (rows are \(r=1,2,\dots,n\); columns are \(f=0,1,\dots,n\)):

\[
 n=2:\quad\begin{pmatrix}1&0&0\\0&0&1\end{pmatrix},
 \qquad n=3:\quad
 \begin{pmatrix}1&1&0&0\\1&2&0&0\\0&0&0&1\end{pmatrix},
\]
\[
 n=4:\quad\begin{pmatrix}
3&2&1&0&0\\5&4&2&0&0\\1&2&3&0&0\\0&0&0&0&1
\end{pmatrix}.
\]
Every ordered two-by-two minor of each displayed table is nonnegative (direct complete integer checking); hence the first full-TP2 failure is exactly \(n=5\). The explicit witness at \(n=5\) is \(w_5(1,2)w_5(2,3)-w_5(1,3)w_5(2,2)=3\cdot2-1\cdot7=-1\).

**4. Exact covariance.** Set \(I_i=\mathbf1\{i\text{ is an upper record}\}\) and \(J_j=\mathbf1\{\pi(j)=j\}\), so \(R=\sum_i I_i\) and \(F=\sum_jJ_j\). Here \(\Pr(I_i=1)=1/i\) and \(\Pr(J_j=1)=1/n\). For \(i\ge2\), conditioning on \(J_j=1\) gives
\[
 \Pr(I_i=1\mid J_j=1)=
 \begin{cases}
 1/(i-1),& j<i,\\
 \binom{n-1}{i-1}^{-1},&j=i,\\
 1/i,&j>i.
 \end{cases}
\]
For \(j<i\), the fixed value \(j\) cannot be the maximum of the first \(i\) values because \(i-1\) others would then have to be less than \(j<i\), so exchangeability of the other \(i-1\) positions gives \(1/(i-1)\). For \(j=i\), a record occurs exactly when all \(i-1\) earlier values are drawn from \(\{1,\dots,i-1\}\), with probability \(\binom{n-1}{i-1}^{-1}\). For \(j>i\), the fixed position lies outside the prefix, which remains exchangeable. Summing conditional-minus-unconditional probabilities over \(j\), the \(i-1\) lower-index contributions total \(1/i\), cancelling the \(-1/i\) term at \(j=i\); the upper-index contributions vanish. Since \(I_1=1\), this yields
\[
 \operatorname{Cov}(R,F)=\frac1n\sum_{i=2}^n\binom{n-1}{i-1}^{-1}.
\]
All terms are positive, completing the proof.

## Verification

Run the attached standard-library-only checker with `python verify_record_fixed_signs.py`. It independently enumerates all \(\sum_{n=2}^9 n!\) permutations, recomputes \((R,F)\), checks the near-identity strata and their minors, exhaustively tests all ordered two-by-two minors for \(n\le4\), verifies the exact covariance using rational arithmetic, and checks polynomial identities for \(3\le n\le249\). The checker reports **31,317 exact assertions passed**. Finite enumeration is used only for the explicitly bounded \(n\le4\) assertion; it is not being substituted for the all-\(n\) transposition/three-cycle or covariance proofs.

## Relationship to prior work

Diaconis, Evans and Graham study fixed-point events and equidistribution of unseparated pairs for uniform permutations, giving the probabilistic baseline and its classification. Sokal and Zeng give vastly more general record-and-cycle master generating polynomials, whose specialization can enumerate the joint \((R,F)\) cells; the present statement concerns the **sign of cross-stratum minors**, rather than a new full enumeration formula. Deb and Sokal also develop record/cycle-refined continued fractions without the displayed sign cutoff. Dubach studies record statistics conditional on permutation cycle type, but its high-record limit theorem assumes the number of non-fixed points tends to infinity; here that number is fixed at two or three. Classical record/cycle equidistribution concerns a one-variable marginal and does not imply fixed-point-preserving joint equivalence. The known TP2 relation for cycle count versus fixed-point count is specifically not being asserted for record count; the negative determinant explains the distinction.

## Limitations

The sign law is for the two natural highest *nontrivial* fixed-point strata, not a complete classification of every minor of the full \((R,F)\) joint array. The statement that TP2 fails for all \(n\ge5\) uses just one explicit negative witness and does not imply a stronger distributional non-ordering for every pair of fixed-point strata. Exact covariance is for the uniform permutation law, not general weighted or conjugation-invariant laws. The search for historical priority is bounded, and an implicit derivation from older master-polynomial identities or an unlocated specialized paper remains possible. No independent audit has been performed.

## References

1. P. Diaconis, S. N. Evans, R. L. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822, August 1, 2013. https://statistics.berkeley.edu/tech-reports/822
2. A. D. Sokal and J. Zeng, *Some multivariate master polynomials for permutations, set partitions, and perfect matchings, and their continued fractions*, arXiv:2003.08192; see Section 2.3. https://arxiv.org/abs/2003.08192
3. S. Deb and A. D. Sokal, *A remark on continued fractions for permutations and D-permutations with a weight -1 per cycle*, arXiv:2306.11500. https://arxiv.org/abs/2306.11500
4. V. Dubach, *A geometric approach to conjugation-invariant random permutations*, *Probability Theory and Related Fields*, 2025, Section 2.3. https://doi.org/10.1007/s00440-025-01449-7
