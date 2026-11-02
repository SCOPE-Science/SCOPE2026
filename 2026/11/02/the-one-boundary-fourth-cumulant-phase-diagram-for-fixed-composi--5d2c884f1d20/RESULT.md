# The one-boundary fourth-cumulant phase diagram for fixed-composition runs

## Finding

Fix integers \(a,b\ge1\), put \(n=a+b\), and sample uniformly from all binary words of length \(n\) having exactly \(a\) ones and \(b\) zeros. Let \(R\) be the total number of maximal constant-symbol runs, and put \(t=ab\). For \(n\ge4\), define
\[
\begin{aligned}
Q_n(t)={}&(240n-288)t^3+(-96n^3-144n^2+288n)t^2\\
&+(8n^5+90n^4-74n^3-36n^2)t\\
&-7n^6-6n^5+19n^4-6n^3.
\end{aligned}
\]
The *fourth cumulant*, \(\kappa_4(R)=\mathbb E[(R-\mathbb ER)^4]-3\operatorname{Var}(R)^2\), is exactly
\[
\boxed{\kappa_4(R)=\frac{2tQ_n(t)}{n^4(n-3)(n-2)(n-1)^2}.}
\tag{1}
\]

**Complete sign classification.** For every \(4\le n\le9\), the fourth cumulant is strictly negative for every feasible positive \(a,b\). For every integer \(n\ge10\), \(Q_n\) has exactly one root \(\tau_n\) in the interval \((n-1,n^2/4)\). For *every* composition \(a+b=n\) with \(a,b\ge1\),
\[
\begin{aligned}
\kappa_4(R)&>0&&\Longleftrightarrow&&ab<\tau_n,\\
\kappa_4(R)&=0&&\Longleftrightarrow&&ab=\tau_n,\\
\kappa_4(R)&<0&&\Longleftrightarrow&&ab>\tau_n.
\end{aligned}
\tag{2}
\]
The positive and negative regions both contain feasible compositions for each \(n\ge10\). At the first transition, \(n=10\), the compositions \(\{a,b\}=\{1,9\}\) have positive fourth cumulant and all other compositions have negative fourth cumulant. For \(n=2\), the run count is constant and \(\kappa_4(R)=0\); for \(n=3\), \(\kappa_4(R)=-2/27\).

The critical product has the universal asymptotic limit
\[
\lim_{n\to\infty}\frac{\tau_n}{n^2}=\frac{6-\sqrt6}{30}.
\tag{3}
\]
Equivalently, for fixed class proportion \(a/n\to p\in(0,1/2]\) away from the critical proportion, the sign changes at
\[
p_* =\frac{1-\sqrt{1-4(6-\sqrt6)/30}}{2}\approx0.1371644200.
\]
Since the variance of \(R\) is strictly positive for \(n\ge3\), these are also exactly the signs of the standardized excess kurtosis.

## Assumptions and scope

All words with the specified counts are equiprobable; this is the conditional null model for the binary Wald--Wolfowitz runs test. The theorem does **not** refer to independent, unconditioned Bernoulli observations with random class counts. The fourth cumulant is defined by a central fourth moment minus three squared variances, not by the raw fourth moment or Pearson kurtosis. The product \(ab\) ranges from \(n-1\) to \(\lfloor n^2/4\rfloor\) over feasible compositions. Equation (2) is an exact criterion, with no assertion that a feasible integer composition necessarily attains equality.

## Proof

Write \(T=R-1=\sum_{i=1}^{n-1}I_i\), where \(I_i=\mathbf 1\{X_i\ne X_{i+1}\}\). Because cumulants of order at least two are translation-invariant, \(\kappa_4(T)=\kappa_4(R)\).

Here is a finite exact derivation of (1), specifying all summands so its polynomial simplification can be checked independently. Write \((z)_{\underline j}=z(z-1)\cdots(z-j+1)\), and let \(\mathcal C(j,c)\) be the set of ordered compositions \((\ell_1,\ldots,\ell_c)\) of \(j\) into \(c\) positive integers. A collection of \(j\) selected path edges has \(c\) consecutive-edge components with these lengths in exactly \(\binom{n-j}{c}\) placements. A component of \(\ell\) edges forces \(\ell+1\) alternating letters. Its two possible orientations each prescribe a pair of counts \((u,v)\) of ones and zeros: for odd \(\ell\), both are \(((\ell+1)/2,(\ell+1)/2)\); for even \(\ell\), they are \((\ell/2+1,\ell/2)\) and its reverse. Retain multiplicities in this two-element collection, written \(\mathcal A(\ell)\).

For \(n\ge9\) and \(1\le j\le4\), the \(j\)-th falling-factorial moment of \(T\) is therefore
\[
F_j:=\mathbb E[(T)_{\underline j}]
=j!\sum_{c=1}^j\binom{n-j}{c}
\sum_{(\ell_1,\ldots,\ell_c)\in\mathcal C(j,c)}
\sum_{((u_i,v_i))\in\prod_i\mathcal A(\ell_i)}
\frac{(a)_{\underline{\sum_i u_i}}(b)_{\underline{\sum_i v_i}}}
{(n)_{\underline{j+c}}}.
\tag{4}
\]
Indeed, each component involves disjoint word positions, and under fixed-content sampling the probability of prescribed values at \(u+v\) positions is exactly \((a)_{\underline u}(b)_{\underline v}/(n)_{\underline{u+v}}\). Formula (4) counts every product of distinct indicators once and includes both alternation orientations.

Obtain the raw moments \(m_j=\mathbb E[T^j]\) from \(m_j=\sum_{k=0}^j\left\{\!\begin{smallmatrix}j\\k\end{smallmatrix}\!\right\}F_k\), with \(F_0=1\), and substitute into
\[
\kappa_4(T)=m_4-4m_1m_3-3m_2^2+12m_1^2m_2-6m_1^4.
\tag{5}
\]
Expanding the **finite** sums in (4) for \(j\le4\), using \(a+b=n\), and collecting powers of \(t=ab\) gives (1). The included symbolic certificate verifies this polynomial identity from the stated independent cluster sum. For \(4\le n\le8\), direct enumeration from the exact elementary composition count
\[
\begin{split}
\#\{R=2k\}&=2\binom{a-1}{k-1}\binom{b-1}{k-1},\\
\#\{R=2k+1\}&=\binom{a-1}{k}\binom{b-1}{k-1}
+\binom{a-1}{k-1}\binom{b-1}{k}
\end{split}
\tag{6}
\]
(with out-of-range binomial coefficients interpreted as zero) verifies (1) in all remaining finitely many cases. For \(n=2,3\), (6) gives the separate values already stated.

To prove the **global** sign property, first note that the denominator in (1) and \(2t\) are positive for \(n\ge4\). For \(4\le n\le9\), the maxima of \(Q_n(a(n-a))\) over \(1\le a<n\), listed in order of \(n\), are exactly \(-96,-792,-2880,-6600,-10080,-7056\), all negative. This is an exhaustive finite check using the displayed cubic, not an inference from numerical samples.

Now let \(n\ge10\) and substitute
\[
t=\frac{n-1+(n^2/4)y}{1+y},\qquad y>0.
\]
A direct expansion gives \((1+y)^3Q_n(t)=A_0+A_1y+A_2y^2+A_3y^3\), where
\[
\begin{aligned}
A_0&=(n-3)(n-2)^2(n-1)(n^2-12n+24),\\
A_1&=\tfrac n2(n-4)(n-3)(n-2)^2(4n^2-17n+12),\\
A_2&=-n^2(n-2)^2(2n^3-12n^2+22n-9),\\
A_3&=-\tfrac{n^3}{4}(n-2)^2(n^2-4n+6).
\end{aligned}
\tag{7}
\]
Every factor establishes \(A_0,A_1>0\) and \(A_2,A_3<0\) when \(n\ge10\); for example \(2n^3-12n^2+22n-9=2n(n-3)^2+4n-9>0\). The transformed cubic has exactly one positive real root, by Descartes' rule of signs (one change in the sequence \(-,-,+,+\)), together with opposite signs at \(y=0\) and as \(y\to\infty\). The substitution is strictly increasing from \(t=n-1\) to \(t=n^2/4\); it follows that \(Q_n\) changes from positive to negative exactly once in this interval. The balanced feasible product also lies beyond the root: when \(n\) is even, \(Q_n(n^2/4)=A_3<0\); when \(n\) is odd and \(n\ge11\),
\[
Q_n((n^2-1)/4)
=-\tfrac14(n-3)(n-1)(n^5-4n^4+12n^3-16n^2-27n-6)<0.
\]
The final bracket is positive for \(n\ge11\) because its first two positive grouped terms \(n^4(n-4)+4n^2(3n-4)\) dominate \(27n+6\). Thus both signs are attained in the discrete composition model and (2) follows.

Finally set \(t=\alpha n^2\). Uniformly on compact subsets of \((0,1/4)\),
\[
\frac{Q_n(\alpha n^2)}{n^7}\longrightarrow
8\alpha(30\alpha^2-12\alpha+1).
\]
The latter expression changes sign exactly once within \((0,1/4)\), at \(\alpha=(6-\sqrt6)/30\). Uniqueness of the finite root and the endpoint sign rule imply (3), and solving \(p(1-p)=\alpha\) with \(p\le1/2\) yields the stated class-proportion threshold.

## Verification

The accompanying standalone file `verify_run_cumulant.py` uses exact integer and rational arithmetic. Run `python3 verify_run_cumulant.py --symbolic` with SymPy installed; omit `--symbolic` for the independent standard-library tests alone. It reconstructs the binomial-count distribution (6) independently by exhaustive word enumeration through length \(13\); compares the fourth cumulant from the counts with (1) for every composition through length \(100\); checks all feasible sign rows through length \(1000\); and verifies the coefficient identity (7). Its optional symbolic phase independently expands the path-edge cluster formula (4) and proves that the difference from (1) simplifies identically to zero under \(a+b=n\). Finite enumerations serve as error checks, not as the proof of the infinite sign classification.

## Relationship to prior work

The exact fixed-composition runs distribution (6), and its mean \(1+2ab/n\) and variance \(2ab(2ab-n)/(n^2(n-1))\), are classical. They are not claimed as discoveries. Kazemi and Jafari (2014, arXiv:1410.8167), whose complete accessible version was read, focus on probability laws and first two moments for order statistics of the counts of the two symbol-run types. Smeeton and Cox (2003) treat the conditional random-arrangement null and test calibration, but do not state the sharp fourth-cumulant phase boundary. A published same-object transition-indicator analysis derives pairwise covariance sign thresholds and recovers the runs variance; its full result does not supply a fourth-cumulant computation or its single-crossing proof.

Equation (6) logically determines all moments, including the fourth, by summation. The specifically assessed mathematical contribution is **the evaluated fourth-cumulant formula together with the proof that its sign has exactly one imbalance boundary for every \(n\ge10\), its sharp onset at \(n=10\), and its limiting critical class proportion**. Directly stated or equivalent coverage of that sign theorem was not identified in the inspected sources; absence from a search is not proof of historical novelty.

## Limitations

A fourth-cumulant sign is not a rigorous bound on a normal-approximation error or on a test's tail probabilities. The theorem does not characterize higher cumulants or multinomial (more than two categories) runs. Classical works by Wald and Wolfowitz, Mood and Barton–David are relevant; their complete historical scans were not available for decisive whole-document comparison, and older runs monographs may implicitly contain the evaluated fourth moment or an equivalent sign principle. The general known exact distribution permits reconstruction of the cumulant through further algebra; the structural phase analysis is the point of interest.

## References

1. A. Wald and J. Wolfowitz, “On a Test Whether Two Samples are from the Same Population,” *Annals of Mathematical Statistics* **11** (1940), 147–162. DOI: 10.1214/aoms/1177731909.
2. A. M. Mood, “The Distribution Theory of Runs,” *Annals of Mathematical Statistics* **11** (1940), 367–392. DOI: 10.1214/aoms/1177731825.
3. N. Smeeton and N. J. Cox, “Do-it-yourself shuffling and the number of runs under randomness,” *The Stata Journal* **3** (2003), 270–277. DOI: 10.1177/1536867X0300300304.
4. M. R. Kazemi and A. A. Jafari, “Characterization of Order Statistics in Two Runs Using Conditional Expectation,” arXiv:1410.8167, first publicly submitted 29 October 2014; subsequently published in *Model Assisted Statistics and Applications*.
5. D. E. Barton and F. N. David, “Multiple runs,” *Biometrika* **44** (1957), 168–178. DOI: 10.1093/biomet/44.1-2.168.
6. “Exact dependence phases of fixed-composition run transitions,” a published exact covariance analysis, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-dependence-phases-of-fixed-composition-run-transitions--c6b28ad6d93d/RESULT.md.
