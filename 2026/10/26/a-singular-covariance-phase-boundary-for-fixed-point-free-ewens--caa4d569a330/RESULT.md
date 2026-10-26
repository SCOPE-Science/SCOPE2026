# A singular covariance phase boundary for fixed-point-free Ewens permutations

## Finding

Let \(\Pi_n\) be an Ewens random permutation on \(\{1,\ldots,n\}\) with weight proportional to \(\theta^{K(\Pi_n)}\), where \(\theta>0\) and \(K\) is the number of cycles. Condition on \(\Pi_n\) having no fixed points. For distinct fixed integers \(a,b\ge2\), let \(C_a,C_b\) count cycles of lengths \(a,b\). Whenever \(n\ge a+b\), define \(H_m(\theta)=[z^m]\exp(-\theta z)(1-z)^{-\theta}\), with \(H_0=1\), \(H_1=0\). The exact covariance is

\[
\operatorname{Cov}(C_a,C_b)=\frac{\theta^2}{ab}\left(\frac{H_{n-a-b}}{H_n}-\frac{H_{n-a}H_{n-b}}{H_n^2}\right).
\]

The **new quantitative dependence classification** has two sharply different regimes:

1. For fixed \(\theta\ne1\) and fixed distinct \(a,b\ge2\),
\[
\operatorname{Cov}(C_a,C_b)=\frac{\theta^2(1-\theta)}{n^2}+O_{\theta,a,b}(n^{-3}).
\]
Thus every distinct pair of short-cycle counts has the *same* leading covariance constant, positive eventually for \(0<\theta<1\) and negative eventually for \(\theta>1\), independently of its two cycle lengths.

2. At the exceptional parameter \(\theta=1\), **for every finite** \(n\ge a+b\),
\[
\operatorname{sgn}\operatorname{Cov}(C_a,C_b)=(-1)^{n-a-b},
\]
with strict nonzero covariance. For fixed distinct \(a,b\) and \(n\to\infty\),
\[
\operatorname{Cov}(C_a,C_b)\sim(-1)^{n-a-b}\frac{e}{ab\,(n-a-b+1)!}.
\]
Here the last asymptotic is a *signed asymptotic*: the quotient of the two signed expressions tends to one. The critical covariance alternates at every sample-size increment and is factorially, rather than polynomially, small.

The exact moment identity is classical; the contribution is its all-pairs sign classification, universal second-order constant, and singular factorial-versus-polynomial change of scale.

## Assumptions and scope

An Ewens-\(\theta\) permutation of \(n\) labels has probability \(\theta^{K(\pi)}/\theta^{\overline n}\), where \(\theta^{\overline n}=\theta(\theta+1)\cdots(\theta+n-1)\). The conditioned event is \(C_1=0\), which has positive probability for \(n\ge2\). All covariance statements concern this *conditional* probability measure. The theorem requires distinct integer lengths \(a,b\ge2\) and \(n\ge a+b\). The limits keep \(a,b,\theta\) fixed; nothing is asserted about joint regimes where these vary with \(n\). In the noncritical regime, eventual signs are not claimed uniformly over \(\theta\) near one.

## Proof

**1. Generating function and factorial moments.** The exponential formula for cycles with length one excluded gives
\[
H(z)=\sum_{m\ge0}H_m(\theta)z^m
=\exp\left(\theta\sum_{j\ge2}\frac{z^j}{j}\right)
=e^{-\theta z}(1-z)^{-\theta}.
\]
All \(H_m(\theta)>0\) for \(m\ge2\), while \(H_0=1,H_1=0\). Marking a cycle of length \(a\), or independently marking one of length \(b\), gives
\[
\mathbb EC_a=\frac{\theta}{a}\frac{H_{n-a}}{H_n},\quad
\mathbb EC_b=\frac{\theta}{b}\frac{H_{n-b}}{H_n},\quad
\mathbb E(C_aC_b)=\frac{\theta^2}{ab}\frac{H_{n-a-b}}{H_n}
\]
for \(a\ne b\). Subtraction proves the exact formula. This step is equivalent to the already-published factorial-moment identity of da Silva, Jamshidpey and Tavaré (2020, Equation (6)); it is not claimed as new.

**2. Second-order asymptotic for arbitrary positive parameter.** Put \(\alpha=\theta-1\). The standard coefficient-transfer expansion, applied to \(e^{-\theta z}(1-z)^{-\theta}\) by expanding its analytic factor at \(z=1\) and using the gamma-ratio expansion, yields for each fixed \(\theta>0\)
\[
H_n=\frac{e^{-\theta}n^{\alpha}}{\Gamma(\theta)}
\left(1+\frac{A_\theta}{n}+\frac{B_\theta}{n^2}
+O_\theta(n^{-3})\right),
\]
where
\[
A_\theta=\frac{3\theta(\theta-1)}2,\qquad
B_\theta=\frac{\theta(\theta-1)(\theta-2)(27\theta-13)}{24}.
\]
For completeness, the coefficients follow by retaining the first three terms of
\[
e^{-\theta z}(1-z)^{-\theta}=e^{-\theta}\bigl((1-z)^{-\theta}+\theta(1-z)^{1-\theta}+\tfrac12\theta^2(1-z)^{2-\theta}+\cdots\bigr),
\]
and using \([z^n](1-z)^{-\beta}=\Gamma(n+\beta)/(\Gamma(\beta)\Gamma(n+1))\), interpreted by analytic continuation whenever a gamma denominator has a pole. The remainder is controlled to one further order by the same coefficient-transfer expansion. At positive integer parameters the expansion terminates algebraically; any remaining entire-factor coefficients are superpolynomially small.

For every fixed nonnegative integer \(m\), elementary division of these expansions gives
\[
\frac{H_{n-m}}{H_n}=1-\frac{\alpha m}{n}
+\frac{\alpha(\alpha-1)m^2/2+A_\theta m}{n^2}
+O_{\theta,m}(n^{-3}).
\]
Substitute \(m=a+b,a,b\) into Step 1. The constant and \(n^{-1}\) terms cancel, and the \(n^{-2}\) coefficient of the parenthesis is
\[
\alpha(\alpha-1)ab-\alpha^2ab=-\alpha ab=(1-\theta)ab.
\]
Multiplication by \(\theta^2/(ab)\) proves the universal \(\theta^2(1-\theta)/n^2\) coefficient. In particular the sign is eventually strict when \(\theta\ne1\). The same coefficient occurs without fixed-point conditioning; the prohibition of singleton cycles first affects smaller-order terms in this regime.

**3. Exact critical signs.** At \(\theta=1\), define \(q_m=H_m(1)=\sum_{j=0}^{m}(-1)^j/j!\), for every \(m\ge0\). Put \(N=n-a-b\). The covariance sign is the sign of
\[
D=q_Nq_{N+a+b}-q_{N+a}q_{N+b}.
\]
For every \(m\ge0\), the integral form of the exponential Taylor remainder gives
\[
q_m=e^{-1}+(-1)^m r_m,\quad
r_m=\frac1{m!}\int_0^1 e^{-t}(1-t)^m\,dt>0.
\]
Moreover \(0<r_m\le1\), \(r_m\sim1/(m+1)!\), and
\[
0<\frac{r_{m+1}}{r_m}\le\frac1{m+1}.
\]
The ratio bound follows simply by comparing the two integrands, including the factorial denominators. For \(N\ge2\), this gives \(r_{N+k}\le3^{-k}r_N\) for every integer \(k\ge0\). Expanding the determinant with \(s=(-1)^N\), we obtain
\[
D=s e^{-1}B+(-1)^{a+b}(r_Nr_{N+a+b}-r_{N+a}r_{N+b}),
\]
where
\[
B=r_N+(-1)^{a+b}r_{N+a+b}-(-1)^a r_{N+a}-(-1)^b r_{N+b}.
\]
Since \(a,b\ge2\), regardless of their parities,
\[
B\ge r_N(1-3^{-a}-3^{-b}-3^{-(a+b)})\ge\frac{62}{81}r_N,
\]
and
\[
\left|r_Nr_{N+a+b}-r_{N+a}r_{N+b}\right|\le\frac{2}{81}r_N^2.
\]
The first term has strictly larger magnitude than the second because \(e^{-1}>1/3\), \(r_N\le1\), and \(62/243>2/81\). Consequently \(\operatorname{sgn}(D)=s\) for every \(N\ge2\). If \(N=1\), then \(q_1=0\) and \(D=-q_{a+1}q_{b+1}<0\). If \(N=0\), the elementary alternating-series bounds \(1/3\le q_m\le1/2\) for all \(m\ge2\) give \(D=q_{a+b}-q_aq_b\ge1/3-1/4>0\). This proves the exact sign for all sizes.

Finally, as \(N\to\infty\) with \(a,b\) fixed, \(r_{N+k}/r_N\to0\) for each \(k\ge1\), \(r_N\to0\), and therefore \(D\sim(-1)^N e^{-1}r_N\). Since \(q_n\to e^{-1}\) and \(r_N\sim1/(N+1)!\), the claimed signed factorial asymptotic follows.

## Verification

The standalone Python 3 program `checker.py` uses exact rational arithmetic to check the coefficient recurrence against an independent finite expansion at seven rational parameter values, the critical parity law for all unequal length pairs in a broad finite range, and the exact covariance formula against complete enumeration of every derangement on five through eight labels. It also checks algebraically equivalent rational covariance expressions over seven parameters and many indices. The verified program reports 4,883 exact assertions. The all-\(n\), all-\(\theta\) conclusions are proved in the preceding argument, not inferred from the finite checks.

## Relationship to prior work

Da Silva, Jamshidpey and Tavaré (arXiv:2006.04840, first public version June 8, 2020) give general factorial moments of Ewens derangement cycle counts (Equation (6)) and their asymptotic independent Poisson limits. These formulas imply the exact starting covariance identity here, but the inspected article does not provide the universal nonzero second-order coefficient, the all-finite-size critical parity sign, or its factorial prefactor. This result supplies those additional asymptotic and sign analyses; it does not claim to originate the Ewens cycle model or factorial-moment formula.

Tavaré (2021, Section 7.2.2) revisits the conditioned Ewens model and its Markov representation, without a covariance sign classification in the inspected section. Cavenagh, Greenhill and Wanless (2008) study the cycle structure of two rows in a random Latin square; that distribution is not exactly a uniform derangement or the fixed-point-conditioned Ewens law studied here. Classical coefficient asymptotics and the derangement alternating-series bounds are used as tools, not presented as novel facts.

## Limitations

The error term and eventual noncritical sign statements fix \(\theta,a,b\) first; they do not give a finite-size transition bound uniform as \(\theta\to1\) or when cycle lengths grow with \(n\). The covariance is not addressed on the diagonal \(a=b\), where an additional factorial-moment term appears. Exact finite-\(n\) noncritical sign boundaries are not classified. The published general factorial-moment formula is a strong predecessor, and an unlocated earlier analysis of its covariance consequences could affect historical priority. The 2008 Latin-square work was checked through its accessible abstract rather than full text; it cannot certify absence of related results. No independent scientific audit has been performed.

## References

1. P. H. da Silva, A. Jamshidpey, S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1 (June 8, 2020), https://arxiv.org/abs/2006.04840 .
2. S. Tavaré, *The magical Ewens sampling formula*, Bulletin of the London Mathematical Society **53** (2021), 1563–1582, doi:10.1112/blms.12537, https://doi.org/10.1112/blms.12537 .
3. N. J. Cavenagh, C. Greenhill, I. M. Wanless, *The cycle structure of two rows in a random Latin square*, Random Structures & Algorithms **33** (2008), 286–309, doi:10.1002/rsa.20216, https://doi.org/10.1002/rsa.20216 .
4. R. Arratia, A. D. Barbour, S. Tavaré, *Logarithmic Combinatorial Structures: A Probabilistic Approach*, EMS Monographs in Mathematics (2003), background on the conditioning relation and cycle-count asymptotics.
