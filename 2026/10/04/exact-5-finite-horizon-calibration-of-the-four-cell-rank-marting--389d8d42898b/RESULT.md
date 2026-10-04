# Exact 5% finite-horizon calibration of the four-cell rank martingale
## Finding
Consider the fixed-grid rank martingale of Henzi and Law with \(d=2\), hence \(q=d^2=4\) cells. Under independence, the randomized sequential ranks fall independently and uniformly into the four cells. If \(C_{i,n}\) is the count in cell \(i\) after \(n\) observations, then the published martingale specializes to
\[
M_n=\frac{4^n3!}{(n+3)!}\prod_{i=1}^4 C_{i,n}!.
\]
For a truncated test with horizon \(N=128\), define the practical calibrated threshold to be the smallest *attained martingale support value* \(T\) for which
\[
\Pr_0\!\left(\max_{1\le n\le128}M_n\ge T\right)\le0.05.
\]
That threshold is exactly
\[
T_*=\frac{10384593717069655257060992658440192}{710974957562660933407217865583125}
=14.606131491142460\ldots,
\]
and its exact null crossing probability is
\[
\frac{722292119311606566081769787391006390193180146380181087536030674324200797387}{14474011154664524427946373126085988481658748083205070504932198000989141204992}
=0.049902691907131\ldots.
\]
The immediately preceding support value is
\[
T_-=\frac{33554432}{2297295}=14.606061476649712\ldots,
\]
with exact crossing probability
\[
\frac{725033551291536480794788624328660593220615976076935941023195541953032226367}{14474011154664524427946373126085988481658748083205070504932198000989141204992}
=0.050092095656419\ldots>0.05.
\]
There is no attainable martingale value strictly between \(T_-\) and \(T_*\) through time \(128\). Thus \(T_*\) is the exact smallest support-attained threshold giving a \(5\%\) truncated test. It is about \(26.97\%\) below the Ville threshold \(20\).

## Assumptions and scope
The result assumes the null setting used for the rank construction: the randomized sequential ranks are iid uniform on \([0,1]^2\). It concerns only the published fixed-grid martingale with \(d=2\), a uniform Dirichlet initial count of one in each of four cells, significance level \(0.05\), and a hard horizon of \(128\). It does not calibrate the Sinkhorn-corrected martingale, mixtures over grid depths, derandomized versions, or alternatives to the uniform Dirichlet prior.

The threshold is called support-attained because a discrete martingale does not in general possess a smallest valid threshold over all real numbers: every real value strictly above \(T_-\) and at most \(T_*\) induces the same rejection event as \(T_*\). The support convention selects the natural reproducible boundary value actually assumed by the martingale.

## Proof
For any sorted occupancy vector \(\lambda=(\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4)\) with \(|\lambda|=n\), the martingale depends only on \(\lambda\):
\[
m_n(\lambda)=\frac{4^n3!}{(n+3)!}\prod_{i=1}^4\lambda_i!.
\]
Fix a threshold \(T\). Let \(A_n(\lambda;T)\) be the number of labeled four-symbol sequences of length \(n\) whose sorted occupancy vector at time \(n\) is \(\lambda\) and whose martingale remains strictly below \(T\) at every time through \(n\). Start with \(A_0((0,0,0,0);T)=1\).

Suppose a predecessor partition \(\lambda\) contains a distinct count value \(v\) with multiplicity \(m_v\). Incrementing any one of those \(m_v\) labeled cells produces, after sorting, the same successor partition \(\mu\). Therefore, whenever \(m_n(\mu)<T\), the exact recurrence adds
\[
A_n(\mu;T)\mathrel{+}=m_vA_{n-1}(\lambda;T).
\]
Under the null, every labeled four-symbol path of length \(N\) has probability \(4^{-N}\). Consequently,
\[
\Pr_0\!\left(\max_{1\le n\le N}M_n\ge T\right)
=1-4^{-N}\sum_{\lambda}A_N(\lambda;T).
\]
This recurrence is exact; sorting only quotients by cell-label symmetry, and the multiplicity factor restores the number of labeled transitions.

Applying the recurrence at \(N=128\) with exact integer arithmetic gives the two crossing probabilities displayed above. Separately enumerating every partition of every \(n\le128\) into at most four parts verifies that the two stated levels are consecutive in the martingale support over the entire horizon. Since the lower level exceeds size \(0.05\) while the next level does not, \(T_*\) is the smallest support-attained valid threshold.

## Verification
The standalone verifier uses only integer arithmetic and `fractions.Fraction`. It checks the closed-form martingale at the first two sample sizes, compares the symmetry-compressed recurrence with brute-force enumeration of all \(4^8\) labeled paths at a nontrivial threshold, exhaustively searches every four-part occupancy partition through time \(128\) for an intermediate support value, and recomputes both exact crossing probabilities. A clean replay prints `VERIFY_OK`.

## Relationship to prior work
Henzi and Law derive the fixed-grid martingale above and identify it as a Bayes factor for the uniform multinomial null against a uniform Dirichlet mixture. Their Section 4.4 explicitly studies the finite-horizon gap in Ville's inequality by simulation: for their Sinkhorn variant they estimate corrected thresholds from \(100000\) null simulations. Their public replication materials likewise describe the finite-horizon threshold routine as an estimator. The result here addresses the same finite-horizon calibration question for the canonical fixed-grid \(d=2\) martingale, but replaces simulation by an exact finite-state recurrence and gives a certified boundary at \(N=128\).

Targeted searches for exact Dirichlet-multinomial martingale boundary crossing, sequential uniform-multinomial Bayes-factor calibration, and equivalent finite-horizon recurrences did not locate this statement or threshold. Older sequential multinomial and Bayes-factor literature remains a residual originality risk because an equivalent orbit-compressed dynamic program could appear under different terminology.

## Limitations
The calculation is exact only for the specified fixed-grid process and horizon. It does not establish that the same amount of Ville-gap correction holds for other grid depths, priors, Sinkhorn corrections, martingale mixtures, or alternative horizons. The numerical percentage reduction from \(20\) is a calibration fact, not a general power theorem. The originality conclusion is literature-search based rather than a proof of absence from all historical sources.

## References
Henzi, A. and Law, M. (2024). *A Rank-Based Sequential Test of Independence*. Biometrika 111(4). arXiv:2305.13818. DOI: 10.1093/biomet/asae023.

Henzi, A. and Law, M. Public replication repository for *A Rank-Based Sequential Test of Independence*, including the finite-horizon Ville-gap simulation code.
