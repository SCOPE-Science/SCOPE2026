# Local log-concavity forces geometricity in the three-record identity
## Finding
Let \(X_1,X_2,\ldots\) be i.i.d. positive-integer-valued random variables with \(p_k=\Pr(X_1=k)>0\) for every \(k\), and let \(R_1<R_2<R_3<\cdots\) be their ordinary upper record values. Suppose
\[
R_1+R_2+R_3\overset{d}{=}X_1+2X_2+3X_3.
\]
If only the two adjacent log-concavity inequalities
\[
p_2^2\ge p_1p_3,\qquad p_3^2\ge p_2p_4
\]
hold, then the law is necessarily geometric: for some \(p\in(0,1)\),
\[
p_k=p(1-p)^{k-1}\qquad(k\ge1).
\]
In particular, the \(m=3\) instance of the record-sum characterization conjecture of Arnold and Villasenor holds throughout the class of strictly positive log-concave mass functions.

## Assumptions and scope
The support is exactly the positive integers and every mass \(p_k\) is positive. The record values are ordinary strict upper records. Full log-concavity is not required: only the inequalities at indices \(2\) and \(3\) are used. The statement does not settle the conjecture without these local inequalities, nor any case \(m>3\).

Write \(Q_j=\Pr(X_1>j)\). Positivity of the mass function gives \(Q_1,Q_2>0\).

## Proof
For \(1\le i<j<k\), the standard record transition law gives
\[
\Pr(R_1=i,R_2=j,R_3=k)
=p_i\frac{p_j}{Q_i}\frac{p_k}{Q_j}.
\]
Compare the two distributions at their two smallest possible totals.

At total \(6\), the record side has only \((R_1,R_2,R_3)=(1,2,3)\), while the weighted-i.i.d. side has only \((X_1,X_2,X_3)=(1,1,1)\). Hence
\[
p_1\frac{p_2}{Q_1}\frac{p_3}{Q_2}=p_1^3,
\qquad
p_3=\frac{p_1^2Q_1Q_2}{p_2}.
\]
At total \(7\), the only record triple is \((1,2,4)\), and the only weighted-i.i.d. triple is \((2,1,1)\). Thus
\[
p_1\frac{p_2}{Q_1}\frac{p_4}{Q_2}=p_2p_1^2,
\qquad
p_4=p_1Q_1Q_2.
\]
Define the two local log-concavity defects
\[
D_2=p_2^2-p_1p_3,
\qquad
D_3=p_3^2-p_2p_4.
\]
Substitution of the preceding formulas gives the exact sign-reversal identity
\[
D_3=-\frac{p_1Q_1Q_2}{p_2}D_2.
\]
The coefficient is strictly positive. Since the assumptions give \(D_2\ge0\) and \(D_3\ge0\), both defects must vanish.

Put \(p=p_1\), \(q=1-p\), and \(r=p_2/(pq)\). From \(D_2=0\),
\[
p_2^3=p_1^3Q_1Q_2.
\]
Because \(Q_1=q\) and \(Q_2=q-p_2=q(1-pr)\), division by \(p^3q^2\) yields
\[
qr^3+pr-1=0
=(r-1)(qr^2+qr+1).
\]
For \(r>0\), the second factor is positive, so \(r=1\). Therefore \(p_2=pq\).

It remains to propagate this initial condition. For every \(n\ge3\), compare the common mass at total \(n+3\). On the record side the only term containing \(p_n\) is the triple \((1,2,n)\), with strictly positive coefficient
\[
\frac{p_1p_2}{Q_1Q_2}.
\]
Every other record term uses masses with indices below \(n\). On the weighted-i.i.d. side, any positive solution of \(x_1+2x_2+3x_3=n+3\) has \(x_1,x_2,x_3<n\), so that side also depends only on earlier masses. Thus the equality in distribution determines \(p_n\) uniquely from \(p_1,\ldots,p_{n-1}\).

The geometric mass function with first mass \(p\) satisfies the full three-record identity: its record spacings are i.i.d. geometric, and reversing the coefficients \(3,2,1\) does not change the law of a weighted sum of three i.i.d. spacings. Since it has the already forced values \(p_1=p\) and \(p_2=pq\), the preceding triangular uniqueness argument forces \(p_n=pq^{n-1}\) for every \(n\ge3\).

## Verification
The included `verify.py` checks with exact symbolic algebra that the two low-total identities imply the displayed sign-reversal formula, checks the factorization that forces \(r=1\), verifies the triangular occurrence of the new mass \(p_n\), and confirms the distributional identity for exact rational geometric data over a finite range. These calculations are consistency checks; the proof above is the infinite argument.

## Relationship to prior work
Arnold and Villasenor formulate the general record-sum characterization as Conjecture 2 and explicitly state that its proof remains elusive. For \(m=3\), they derive the total-6 relation giving \(p_3\) in terms of \(p_1,p_2\), observe that later coefficient comparisons recursively determine further masses, and speculate that non-geometric solutions may exist. Their paper does not impose log-concavity and does not identify the sign-reversal relation between the two adjacent log-concavity defects. The present result therefore gives a structural regime in which their \(m=3\) conjecture is forced.

A 2026 paper on characterisation by record-like observations was also checked because it cites Arnold--Villasenor. It studies a different martingale property for \(\delta\)-records and associated difference equations; it does not state or imply the three-record weighted-sum identity used here.

## Limitations
The argument requires \(p_k>0\) on the full positive-integer support and the two local log-concavity inequalities at indices \(2\) and \(3\). It does not decide whether convergent non-geometric solutions exist when those inequalities fail, which is the unresolved direction emphasized by Arnold and Villasenor. It also does not address \(m>3\).

## References
1. B. C. Arnold and J. A. Villasenor, “Characterization of the Geometric Distribution Via Linear Combinations of Observations and of Records,” *Sankhya A* 85 (2023), 651–657. DOI: 10.1007/s13171-021-00271-2. First published online 2021-12-16. Primary MSC 60E05.
2. R. Gouet, M. Lafuente, F. J. Lopez, and G. Sanz, “Characterisation of distributions via record-like observations,” *Statistical Papers* (2026). DOI: 10.1007/s00362-026-01845-8.
