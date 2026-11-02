# Sharp odds-ratio control of the order defect of two binary conditional expectations

## Finding

On a strictly positive \(2\times2\) probability table, the order defect of row and column conditional expectations admits an exact \(L^\infty\)-operator norm formula. More strikingly, fixing only the odds ratio \(\theta>0\), the *sharp supremum over all strictly positive tables having that odds ratio* is
\[
\sup_{ad/(bc)=\theta}\|E_XE_Y-E_YE_X\|_{L^\infty\to L^\infty}
=2\frac{|\sqrt\theta-1|}{\sqrt\theta+1}.
\]
For \(\theta\ne1\), the strict bound is never attained by a positive table, although the supremum is approached explicitly; at \(\theta=1\) the commutator vanishes identically. The right-hand side is twice the absolute value of Yule's association coefficient \(Y\).

## Assumptions and scope

Let \(a,b,c,d\) be strictly positive real numbers and put probability masses proportional to \((a,b,c,d)\) on \(\Omega=\{00,01,10,11\}\), with the first coordinate called \(X\) and the second \(Y\). Let \(P=E[\cdot\mid X]\) and \(Q=E[\cdot\mid Y]\), acting on the real four-dimensional \(L^\infty(\Omega)\) with norm \(\|f\|_\infty=\max_{\omega\in\Omega}|f(\omega)|\). Scalar rescaling of all four masses is immaterial.

Define four conditional probabilities
\[
 u=\frac b{a+b},\quad v=\frac d{c+d},\quad
 r=\frac c{a+c},\quad s=\frac d{b+d},
\]
and set \(\Delta_X=s-r\), \(\Delta_Y=v-u\). The exact norm for every positive table is
\[
\boxed{\|PQ-QP\|_{\infty\to\infty}
=2\max\Bigl\{|\Delta_X|\max(u,1-u,v,1-v),\;
|\Delta_Y|\max(r,1-r,s,1-s)\Bigr\}.}
\]
The supremum statement quantifies over *all positive tables of a fixed odds ratio*, and does not assert the same bound for larger alphabets, arbitrary probability spaces, or other norms. For each *fixed* table the exact operator norm is attained by a sign vector, while the sharp fixed-odds-ratio bound is not attained if \(\theta\ne1\).

## Proof

**Step 1 (exact commutator).** Conditional expectations are the rowwise and columnwise weighted averages. In the ordered basis \((00,01,10,11)\), direct multiplication gives
\[
PQ-QP=\begin{pmatrix}
0&-u\Delta_X&r\Delta_Y&u\Delta_X-r\Delta_Y\\
(1-u)\Delta_X&0&s\Delta_Y-(1-u)\Delta_X&-s\Delta_Y\\
-(1-r)\Delta_Y&(1-r)\Delta_Y-v\Delta_X&0&v\Delta_X\\
(1-v)\Delta_X-(1-s)\Delta_Y&(1-s)\Delta_Y&-(1-v)\Delta_X&0
\end{pmatrix}.
\]
Notice the exact identities
\[
\Delta_X=\frac{ad-bc}{(a+c)(b+d)},\qquad
\Delta_Y=\frac{ad-bc}{(a+b)(c+d)}.
\]
Consequently the two deltas always have the same sign. For nonnegative \(A,B\), the absolute sum of \((-A,B,A-B)\) equals \(2\max(A,B)\); the same holds after a common sign reversal. Applying this observation to each of the four matrix rows shows that their respective absolute row sums are
\[
\begin{split}
&2\max\{u|\Delta_X|,r|\Delta_Y|\},\\
&2\max\{(1-u)|\Delta_X|,s|\Delta_Y|\},\\
&2\max\{v|\Delta_X|,(1-r)|\Delta_Y|\},\\
&2\max\{(1-v)|\Delta_X|,(1-s)|\Delta_Y|\}.
\end{split}
\]
The induced \(\ell^\infty\)-matrix norm is the greatest of these sums, giving the asserted exact table formula. A sign choice matching the signs of a maximal row attains the norm for each fixed table.

**Step 2 (one-dimensional odds-ratio inequality).** For \(p\in(0,1)\), write its odds \(o(p)=p/(1-p)\). Suppose \(q,p\in(0,1)\) satisfy \(o(q)/o(p)=\theta>0\). With \(t=o(p)>0\), we have \(p=t/(1+t)\), \(q=\theta t/(1+\theta t)\), whence
\[
|q-p|=\frac{|\theta-1|\,t}{(1+t)(1+\theta t)}
\le\frac{|\sqrt\theta-1|}{\sqrt\theta+1}.
\]
For \(\theta\ne1\), the denominator after division by \(t\) is \(t^{-1}+1+\theta+\theta t\), minimized by the arithmetic-geometric mean inequality at \(t=1/\sqrt\theta\); the displayed bound is exact. For \(\theta=1\), both sides are zero.

**Step 3 (universal strict bound).** The pairs \((u,v)\) and \((r,s)\) satisfy
\[
\frac{o(v)}{o(u)}=\frac{o(s)}{o(r)}=\frac{ad}{bc}=\theta.
\]
Step 2 therefore yields \(|\Delta_X|,|\Delta_Y|\le Y_\theta\), where \(Y_\theta=|\sqrt\theta-1|/(\sqrt\theta+1)\). Since all four conditional probabilities lie strictly between zero and one, the two maxima appearing in Step 1 are strictly less than one. Thus \(\|PQ-QP\|<2Y_\theta\) whenever \(\theta\ne1\). When \(\theta=1\), \(ad=bc\), both deltas vanish and \(PQ=QP\).

**Step 4 (sharpness, including nonattainment).** Fix \(\theta\ne1\), put \(\rho=\sqrt\theta\), and consider the strictly positive masses
\[
(a,b,c,d)=(\rho T,T,\rho^{-1},1),\qquad T>0.
\]
They have constant odds ratio \(\rho^2=\theta\), while
\[
 u=\frac1{1+\rho},\quad v=\frac\rho{1+\rho},\quad
 r=\frac1{\rho^2 T+1},\quad s=\frac1{T+1}.
\]
Therefore \(|\Delta_Y|=Y_\theta\), and \(\max(r,1-r,s,1-s)\to1\) as \(T\to\infty\). Step 1 implies \(\liminf_{T\to\infty}\|P_TQ_T-Q_TP_T\|\ge 2Y_\theta\), matching Step 3. The strict inequality of Step 3 proves nonattainment for positive tables. For \(\theta=1\), all such tables are independent and the value zero is attained.

## Verification

The standalone Python 3 checker \(\texttt{verify.py}\) builds both conditional-expectation matrices from the cell masses without using the claimed commutator coefficients. It exhaustively tests every quadruple of positive integers from \(1\) through \(8\), checking 4096 matrix identities, all corresponding row-norm identities, and strict fixed-odds upper bounds by rational integer arithmetic without numerical square roots. Fifteen further exact rational tests check the explicit sharpness family. Run `python3 verify.py` from the directory containing the file; the expected prefix is `VERIFY_OK`.

The general positivity, norm identity, fixed-odds optimum, and nonattainment statements are established by the four algebraic proof steps above; finite checks are not a substitute for those arguments.

## Relationship to prior work

Rehder's analysis of commuting Hilbert-space projections addresses *whether* two projections commute, not their sharp \(L^\infty\) commutator norm on a weighted four-cell table. Warrens studies marginal-invariant association coefficients and records Yule's \(Y\), but does not relate that coefficient to the worst-case order defect of two conditional-expectation operators. Existing published studies of binary conditional-expectation chains and of three-atom commutators address neighboring objects or norms; the present conclusion is a fixed-odds sharp supremum over full-support \(2\times2\) laws together with the complete four-cell matrix norm. The appearance of Yule's coefficient itself is classical and is not asserted to be new.

## Limitations

This is an exact four-state, strictly positive, real \(L^\infty\) result. Allowing zero cell masses changes the conditional expectation's support and attainment conventions. No classification of arbitrary finite partitions, other \(L^p\) norms, or marginal-constrained extremizers is asserted. Mathematical correctness is checked algebraically and computationally here, but publication priority remains subject to older or unindexed literature, including a conditionals-commutativity paper whose full text was not accessible for comparison. Independent scientific audit has not been performed.

## References

- W. Rehder, “When Do Projections Commute?”, *Zeitschrift für Naturforschung A* **35** (1980), 437–441, DOI: [10.1515/zna-1980-0415](https://doi.org/10.1515/zna-1980-0415). Full lawful repository text: <https://depositonce.tu-berlin.de/bitstreams/2364ec9d-954f-4a1d-b827-d9ced0e11a02/download>.
- M. J. Warrens, “On Association Coefficients for 2×2 Tables and Properties That Do Not Depend on the Marginal Distributions,” *Psychometrika* **73** (2008), 777–789, publicly posted July 23, 2008, DOI: [10.1007/s11336-008-9070-3](https://doi.org/10.1007/s11336-008-9070-3).
- O. Kallenberg, “Commutativity Properties of Conditional Distributions and Palm Measures,” *Communications on Stochastic Analysis* **4** (2010), DOI: [10.31390/cosa.4.1.03](https://doi.org/10.31390/cosa.4.1.03). Full text not available in the present literature inspection.
