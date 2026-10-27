# Unbounded covariance sign reversals between hapaxes and runs in iid words

## Finding

For every integer \(q\ge2\), there exists a strictly positive probability vector on \(q\) letters for which, as the word length \(n\) increases through the positive integers, the covariance between the number of letters occurring exactly once and the number of maximal constant-letter runs alternates strict sign at least \(2q-3\) times. Thus there is no bound on the number of reversals uniform over finite alphabet sizes. The binary case admits only one possible reversal. Already for three letters, the rational distribution \((1/19,6/19,12/19)\) has positive, negative, positive, and negative covariance at lengths \(2,8,11,19\), respectively.

Let \(X_1,\ldots,X_n\) be iid with \(\Pr(X_t=i)=p_i>0\) for \(1\le i\le q\), \(\sum_i p_i=1\). Write \(H_n=\sum_i\mathbf1\{\#\{t:X_t=i\}=1\}\) for the number of hapax symbols and \(R_n=1+\sum_{t=1}^{n-1}\mathbf1\{X_t\ne X_{t+1}\}\) for the number of runs. For \(n\ge2\), put

\[
s=\sum_{i=1}^q p_i^2,\qquad h_i=\frac{s-p_i^2}{(1-p_i)^2}.
\]

Their exact covariance is

\[
\operatorname{Cov}(H_n,R_n)=(n-1)\sum_{i=1}^q p_i(1-p_i)^{n-1}\bigl[n(s-h_i)+2h_i\bigr]. \tag{1}
\]

For \(q=2\) with masses \((a,1-a)\), equation (1) becomes

\[
2(n-1)\bigl[1-na(1-a)\bigr]\bigl[a(1-a)^{n-1}+(1-a)a^{n-1}\bigr], \tag{2}
\]

so its sign is exactly that of \(1-na(1-a)\). For the uniform law on \(q\) letters it simplifies to

\[
\operatorname{Cov}(H_n,R_n)=\frac{(n-1)(2q-n)(q-1)^{n-2}}{q^n}. \tag{3}
\]

## Assumptions and scope

The theorem concerns independent identically distributed symbols from a finite alphabet of size \(q\ge2\), each with positive probability. The probability vector is held fixed while \(n\) ranges over positive integers. A strict sign reversal means two successive selected increasing sample lengths have strictly opposite nonzero covariance; intervening zero values are allowed. The existence theorem allows a different probability vector for each alphabet size. All statements of covariance are finite and exact; there is no assertion of eventual oscillation for one fixed finite law.

## Proof

**Exact covariance identity.** For each letter \(i\), set \(I_i=\mathbf1\{\#\{t:X_t=i\}=1\}\), so \(H_n=\sum_iI_i\). Then

\[
\Pr(I_i=1)=np_i(1-p_i)^{n-1},\qquad \mathbb E[R_n]=1+(n-1)(1-s).
\]

Conditionally on \(I_i=1\), the unique occurrence position of \(i\) is uniform over the \(n\) positions. For any given adjacent pair, the probability neither position is \(i\) is \((n-2)/n\). Conditionally on that event, the two letters are independent with masses \(p_j/(1-p_i)\), \(j\ne i\); their equality probability is \(h_i\). A pair involving the unique \(i\) cannot be equal. Therefore

\[
\mathbb E[R_n\mid I_i=1]=1+(n-1)\left(1-\frac{n-2}{n}h_i\right).
\]

It follows that

\[
\operatorname{Cov}(I_i,R_n)
=np_i(1-p_i)^{n-1}(n-1)
\left(s-\frac{n-2}{n}h_i\right),
\]

and summing over \(i\) gives (1). Substituting two complementary probabilities gives (2), and substituting all \(p_i=1/q\) gives (3). Thus two letters have at most one strict sign reversal, achieved for the uniform binary law between lengths \(2\) and \(5\).

**Rare-letter induction.** Suppose that for a positive \(q\)-letter law \(p=(p_1,\dots,p_q)\) there exist fixed increasing integers \(2\le n_1<\dots<n_{2q-2}\) at which the covariance signs alternate beginning positive and ending negative. For \(q=2\), take \(p=(1/2,1/2)\) and \((n_1,n_2)=(2,5)\).

Fix \(0<\varepsilon<1\) and add a new rare letter by defining

\[
p^{(\varepsilon)}=((1-\varepsilon)p_1,\dots,(1-\varepsilon)p_q,\varepsilon).
\]

For every previously selected fixed \(n_j\), equation (1) is continuous as \(\varepsilon\downarrow0\), so the old strict signs persist for all sufficiently small \(\varepsilon\). Write \(S=\sum_{i=1}^q p_i^2>0\). For the newly added letter, the quantities in (1) are \(h_{q+1}=S\) and \(s_\varepsilon=(1-\varepsilon)^2S+\varepsilon^2\). Its exact contribution is

\[
T_\varepsilon(n)=(n-1)\varepsilon(1-\varepsilon)^{n-1}
\left[2S+n\bigl(-2S\varepsilon+(S+1)\varepsilon^2\bigr)\right]. \tag{4}
\]

Choose the two integer lengths

\[
u_\varepsilon=\lfloor\varepsilon^{-1/2}\rfloor,\qquad
v_\varepsilon=\lfloor 2/\varepsilon\rfloor.
\]

At \(n=u_\varepsilon\), equation (4) gives \(T_\varepsilon(u_\varepsilon)/\sqrt\varepsilon\to2S>0\). At \(n=v_\varepsilon\), it gives \(T_\varepsilon(v_\varepsilon)\to-4Se^{-2}<0\). Indeed \((u_\varepsilon-1)\varepsilon/\sqrt\varepsilon\to1\), \((1-\varepsilon)^{u_\varepsilon-1}\to1\), and \((v_\varepsilon-1)\varepsilon\to2\), \((1-\varepsilon)^{v_\varepsilon-1}\to e^{-2}\), with bracket limits \(2S\) and \(-2S\), respectively.

The sum of all *old-letter* contributions in (1) is exponentially negligible at both lengths, uniformly for small \(\varepsilon\). To see this, choose \(\delta>0\) smaller than half the minimum old probability. Each old mass \((1-\varepsilon)p_i\ge\delta\) and stays bounded away from \(1\); each corresponding \(h_i\), \(s_\varepsilon\) stays bounded. The absolute value of its contribution is bounded by \(C n^2(1-\delta)^n\). This is \(o(\sqrt\varepsilon)\) at \(u_\varepsilon\), and \(o(1)\) at \(v_\varepsilon\). Hence the new total covariance is positive at \(u_\varepsilon\) and negative at \(v_\varepsilon\), for all sufficiently small \(\varepsilon\).

The lengths \(u_\varepsilon<v_\varepsilon\) both tend to infinity; hence they may be chosen strictly larger than all earlier \(n_j\). The old alternating sign list ending negative extends by a positive sign and then a negative sign. This adds two reversals and proves the induction: \(2q-3\) strict sign reversals on \(q\) letters. The upper and lower limits above hold along *integer* lengths, so rounding does not introduce any continuum approximation assumption.

**Exact three-letter example.** For \(p=(1/19,6/19,12/19)\), direct rational substitution into (1) yields the signs

\[
\operatorname{sgn}\operatorname{Cov}(H_n,R_n)=
\begin{cases}
+,&n=2,\\ -,&n=8,\\ +,&n=11,\\ -,&n=19.
\end{cases}
\]

These are exact rational evaluations rather than simulations; the standalone verifier reproduces them.

## Verification

Run \(\texttt{python verify_hapax_runs.py}\) in an environment supporting Python 3 and its standard library. The verifier independently enumerates complete words, using exact rational arithmetic, for five probability vectors and lengths \(2\) through \(6\), and compares directly computed covariance with (1). It separately checks the binary and uniform closed forms over parameter grids and the exact three-letter sign witness. The recorded execution produced \(1050\) passing exact assertions. This finite computation checks the formula and witness only. The proof of arbitrarily many sign reversals is the preceding induction and its two asymptotic estimates.

## Relationship to prior work

Run statistics and finite-state word-count distributions are classical. Johnson and Fu (2014) examine run and pattern distributions in multi-state iid sequences and approximation methods. Kong (2018, online publication; open preprint 2024) develops multivariate generating functions jointly tracking letter specifications and rises/falls/runs, so exact fixed-length covariance values can in principle be extracted from this broader joint-distribution machinery. Neither finite covariance formulas nor the availability of a generating function is claimed as independently new. The claim assessed here is the global *unbounded number of strict sign reversals* realized as both alphabet size and nonuniformity change, together with a constructive rare-letter induction and the sharp binary obstruction. The inspected results do not state this parameter-uniform sign-reversal construction. A possible implicit deduction from general joint-distribution theory is a remaining priority risk.

## Limitations

The existence construction is not an optimal maximum-count classification at fixed \(q\); \(2q-3\) is a lower bound, not an upper bound. The probabilities produced by induction may be extremely nonuniform and the sign-reversal lengths very large. No claim is made for Markov letters, random-length words, or any one fixed law having infinitely many reversals. The exact covariance identity follows elementary conditional counting, and the novelty assessment specifically excludes claiming that generic fixed-length joint moments were previously inaccessible. Historical priority, especially implicit consequences of multivariate generating functions, is not independently certified.

## References

1. Johnson, B. C. and Fu, J. C. *Approximating the distributions of runs and patterns.* Journal of Statistical Distributions and Applications 1, article 5 (first published June 11, 2014). DOI: 10.1186/2195-5832-1-5. https://doi.org/10.1186/2195-5832-1-5
2. Kong, Y. *Joint distribution of rises, falls, and number of runs in random sequences.* Communications in Statistics—Theory and Methods 48(3), 493–499 (online January 5, 2018). DOI: 10.1080/03610926.2017.1414261. Accessible preprint: arXiv:2405.01748v1 (May 2, 2024). https://arxiv.org/abs/2405.01748
