# Likelihood-ratio ordering of fixed points by cycle count in uniform permutations

## Finding

Let \(C\) count cycles and \(F\) count singleton cycles (fixed points) in a uniform random permutation of \([n]\). The \((C,F)\) joint count matrix is totally positive of order two: for all \(1\le k_1<k_2\le n\) and \(0\le f_1<f_2\le n\),
\[
J_n(k_1,f_1)J_n(k_2,f_2)\;\ge\;J_n(k_1,f_2)J_n(k_2,f_1).
\]
Consequently \(F\mid(C=k)\) is nondecreasing in the *monotone likelihood-ratio* (MLR) order as \(k\) increases. Each adjacent minor with all four cells positive is strictly positive. This is a global distributional order, not just positive covariance or stochastic monotonicity. The joint enumeration itself and the real-rootedness input are classical; the assertion is the TP2/MLR comparison across both statistics.

## Assumptions and scope

Fix an integer \(n\ge2\). Let \(\pi\) be uniformly distributed on all \(n!\) permutations of \([n]\). Write \(C(\pi)\) for its number of cycles and \(F(\pi)\) for its number of fixed points. Define \(d(m,r)\) as the number of fixed-point-free permutations of \([m]\) with \(r\) cycles. Set \(d(0,0)=1\), \(d(1,r)=0\), and \(d(m,r)=0\) for impossible indices. The known exact enumeration is
\[
J_n(k,f)=\binom nf d(n-f,k-f),\qquad 0\le f\le n,\quad 1\le k\le n.
\]
For \(1\le k<n\), the positive support of the \(k\)-th row is exactly
\[
\max(0,2k-n)\le f\le k-1.
\]
The last row \(k=n\) has its sole positive entry at \(f=n\). The column \(f=n-1\) is identically zero for \(n\ge2\). MLR order is understood via cross-product inequalities, allowing zero cells; no division by zero is needed.

## Proof

**1. Derangement coefficients and a strict log-concavity input.** Removing or reinserting the greatest label from a derangement gives, for \(m\ge2\),
\[
d(m,r)=(m-1)\bigl(d(m-1,r)+d(m-2,r-1)\bigr).
\]
Let \(D_m(z)=\sum_r d(m,r)z^r\). Then \(D_2(z)=z\), \(D_3(z)=2z\), and \(D_m(z)=(m-1)(D_{m-1}(z)+zD_{m-2}(z))\). Define \(P_m(z)=D_m(z)/((m-1)!z)\) for \(m\ge2\). Thus \(P_2=P_3=1\) and
\[
P_m(z)=P_{m-1}(z)+\frac{z}{m-2}P_{m-2}(z),\qquad m\ge4.
\]
This is the weighted-matching generating polynomial of the path on \(m-2\) vertices, whose consecutive edges indexed \(j=1,\ldots,m-3\) have weights \(1/(j+1)\). If \(H\) is the symmetric tridiagonal matrix with zero diagonal and off-diagonal entry \(1/\sqrt{j+1}\) on edge \(j\), determinant expansion gives the polynomial identity
\[
\det(tI-H)=t^{m-2}P_m(-t^{-2}).
\]
All eigenvalues of \(H\) are real, occurring in \(\pm\) pairs, so \(P_m(z)\) is a product of factors \(1+\lambda z\) with \(\lambda>0\). Hence its coefficients are nonnegative and strictly log-concave on their positive support by Newton's inequalities. In particular, for every \(m\ge2\) and integer \(r\),
\[
L_m(r):=d(m,r)^2-d(m,r-1)d(m,r+1)\ge0,
\]
with strict inequality if \(d(m,r)>0\). This rederives a known real-rootedness consequence; it is not itself a novelty claim.

**2. A mixed-order inequality not furnished by single-row log-concavity alone.** For \(m\ge1\) define
\[
\begin{aligned}
R_m(r)&=d(m,r)d(m-1,r-1)-d(m,r-1)d(m-1,r),\\
T_m(r)&=d(m,r)d(m-1,r)-d(m,r+1)d(m-1,r-1).
\end{aligned}
\]
Expanding the recurrence in Step 1, with zero conventions at boundaries, gives the two *exact* identities
\[
R_m(r)=(m-1)T_{m-1}(r-1),\qquad
T_m(r)=(m-1)\bigl(L_{m-1}(r)+R_{m-1}(r)\bigr).
\]
For \(m=1,2\), \(T_m(r)=0\) identically. At \(m=3\), \(R_3(r)=0\) for every \(r\) and \(T_3(r)\ge0\). The identities and \(L\ge0\) prove by simultaneous induction that \(R_m(r),T_m(r)\ge0\) for every \(m\ge3\) and integer \(r\). Moreover \(T_m(r)>0\) whenever \(d(m-1,r)>0\), since then \(L_{m-1}(r)>0\).

**3. Adjacent determinants.** For \(1\le k<n\) and \(0\le f<n\), the exact enumeration yields
\[
\begin{aligned}
&J_n(k,f)J_n(k+1,f+1)-J_n(k,f+1)J_n(k+1,f)\\
&\hspace{10mm}=\binom nf\binom n{f+1}
T_{n-f}(k-f)\ge0.
\end{aligned}
\]
Terms with \(n-f=1\) or \(n-f=2\) vanish under the stated conventions and the base values above. The displayed determinant is strictly positive when its four cells are all positive: then \(d(n-f-1,k-f)>0\), so Step 2 supplies strictness.

**4. All minors, including support boundaries.** For every row \(k<n\), its positive columns constitute the interval given in the scope section; both endpoints are nondecreasing in \(k\). Consider any rows \(k_1<k_2\) and columns \(f_1<f_2\). If either cross-cell \(J_n(k_1,f_2)\) or \(J_n(k_2,f_1)\) is zero, the desired determinant is nonnegative immediately. If both cross-cells are positive, every cell of the intervening rectangular range of rows and columns is positive. All adjacent inequalities from Step 3 can then be divided and telescoped to compare the ratios \(J_n(k,f+1)/J_n(k,f)\) and obtain the required nonnegative minor. The isolated terminal row \(k=n\) also satisfies all cross-product inequalities directly because its only positive column is \(f=n\). Thus the full matrix is TP2. Dividing rows by their positive unsigned-Stirling cycle-count totals preserves these inequalities and proves the conditional MLR statement.

## Verification

The accompanying standard-library Python script `verify.py` independently enumerates each permutation for \(2\le n\le8\), reconstructs the joint count cells, checks all pairwise TP2 minors for \(2\le n\le41\), checks the mixed-determinant recurrences through \(m=49\), and independently enumerates weighted path matchings through \(m=16\). It reports 6,171,849 exact assertion instances without numerical tolerances. Exhaustive checks are finite evidence only; the proof above establishes the theorem for all \(n\ge2\).

## Relationship to prior work

Ma (2011/2012) gives a trivariate excedance/fixed-point/cycle generating function and explicitly gives the full fixed-point coefficient identity (equation on p. 420). Hence the displayed joint enumeration is **prior work**, not the contribution. Bóna (2006), attributing a theorem to Brenti (1995), documents the real-rootedness of derangement cycle polynomials; real-rootedness is also not new. Lugo (2009) studies cycle profiles, and Diaconis--Fulman--Guralnick (2007) analyze fixed-point laws. None of the inspected relevant passages establishes the adjacent mixed-size determinant inequalities or the global conditional MLR comparison proved here. Earlier monotone refinements of Ewens partitions imply ordinary stochastic order but do not, by themselves, imply MLR order. The difference is an implication comparison, not a claim of uniqueness of formula or technique.

## Limitations

Historical priority is provisional. A sufficiently strong unpublished or inaccessible total-positivity theorem, or a previously unnoticed corollary of Brenti's 1995 work, might subsume the claimed matrix inequality. The 1995 full text was not available for complete inspection. No independent scientific audit has been performed. The theorem concerns only uniform permutations, integer \(n\ge2\), and the two specified statistics; there is no asserted extension to nonuniform Ewens parameters or general permutation patterns.

## References

1. M. Bóna, *On a Balanced Property of Derangements*, arXiv:math/0606277 (public preprint 2006-06-12), especially introduction and Theorem 1.1 citing Brenti.
2. S.-M. Ma, *Counting Permutations by Numbers of Excedances, Fixed Points and Cycles*, Bulletin of the Australian Mathematical Society 85 (2012), 415–421, DOI:10.1017/S0004972711002760; full accessible text, especially p. 420.
3. M. Lugo, *Profiles of Permutations*, arXiv:0907.5351 (2009), concerning cycle-profile enumeration.
4. P. Diaconis, J. Fulman and R. Guralnick, *On Fixed Points of Permutations*, arXiv:0708.2643 (2007).
5. F. Brenti, *Combinatorics and Total Positivity*, Journal of Combinatorial Theory, Series A 71 (1995), 175–218. Full text was not inspected.
