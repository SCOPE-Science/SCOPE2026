# Conditional sign reversal for fixed points and inversions in a packet-reversal shuffle

## Finding

**Theorem (one-pass dependence reversal and its Gaussian scaling).** Fix an integer \(n\ge 2\), a cut probability \(p\in(0,1)\), and the identity ordering of \(n\) distinct cards. Independently cut each of the \(n-1\) interior gaps with probability \(p\), and reverse each resulting packet in its original location. Let \(F_n\) denote the number of fixed card positions, \(I_n\) the number of inversions of the resulting permutation, and \(M_n\) the number of packets. Then:

1. **Unconditional dependence.** For every \(n\ge2\) and \(p\in(0,1)\),
   \[\operatorname{Cov}(F_n,I_n)<0.\]
2. **Conditioning reverses the sign.** For every \(m\in\{1,\ldots,n\}\),
   \[\operatorname{Cov}(F_n,I_n\mid M_n=m)\ge0,\]
   and equality holds precisely when \(m<2+(n\bmod 2)\) or \(m>n-2\). Thus strict positivity holds for \(2+(n\bmod 2)\le m\le n-2\). The event \(M_n=m\) has strictly positive probability. Writing \(f\) for any feasible value of \(F_n\), put \(s=(n-2m+f)/2\). The exact conditional regression is
   \[\mathbb E[I_n\mid F_n=f,M_n=m]
   =m-f+\left(5-\frac{2f}{m}\right)s+\frac{4s(s-1)}{m+1}.\]
   Its successive feasible values increase strictly:
   \[g_{n,m}(f+2)-g_{n,m}(f)
   =\frac{2n(m-1)-m^2+3m-4f-4}{m(m+1)}>0.\]
   The exact conditional support and probabilities are
   \[\Pr(F_n=f\mid M_n=m)=
   \frac{\binom mf\binom{s+m-1}{m-1}}{\binom{n-1}{m-1}},\]
   for integers \(0\le f\le m\), \(f\equiv n\pmod 2\), \(s\ge0\); otherwise the probability is zero.
3. **Joint fluctuations.** Keep \(p\in(0,1)\) fixed and let \(n\to\infty\). With \(q=1-p\) and
   \[\boldsymbol\mu_p=\begin{pmatrix}p/(2-p)\\q/p\end{pmatrix},\]
   one has
   \[\frac{1}{\sqrt n}\left(\begin{pmatrix}F_n\\I_n\end{pmatrix}-n\boldsymbol\mu_p\right)
   \Longrightarrow N_2(0,\Sigma_p),\]
   where
   \[\boxed{\Sigma_p=\begin{pmatrix}
   \dfrac{4pq}{(2-p)^3}&-\dfrac{2q(p^2-2p+2)}{p(2-p)^3}\\
   -\dfrac{2q(p^2-2p+2)}{p(2-p)^3}&\dfrac{q(2-p)}{p^3}
   \end{pmatrix}.}\]
   In particular,
   \[\lim_{n\to\infty}\operatorname{Corr}(F_n,I_n)
   =-\frac{1+q^2}{(1+q)^2},\]
   a strictly negative value between \(-1\) and \(-1/2\). This correlation limit is for fixed \(p\) and is not uniform in parameters approaching the endpoints.

The conditioning variable has a direct observable interpretation. Between distinct packets every adjacent pair in the resulting permutation is increasing, while within a packet of length \(\ell\) all its \(\ell-1\) adjacent pairs are decreasing. Therefore the number of descents is exactly \(n-M_n\). The positive conditional relationship is thus observable by conditioning on descent count, not on a latent variable supplied by the construction.

## Assumptions and scope

The result concerns **one** independent-cut, within-packet reversal pass from the identity ordering, not arbitrary starting permutations or repeated shuffles. The packet-reversal convention matters: the physically ordered overhand operation is the resulting deck composed with a global reversal, which preserves mixing distances but generally changes fixed-point and inversion statistics. Every assertion is finite-sample unless explicitly marked as \(n\to\infty\). In the limit, \(p\) is constant in \((0,1)\). All probabilities are ordinary probability over the \(n-1\) independent Bernoulli cut bits. The count \(M_n\) ranges from \(1\) to \(n\).

If the packet lengths form a positive composition \((\ell_1,\ldots,\ell_m)\) of \(n\), direct inspection gives the two basic identities
\[F_n=\sum_{j=1}^m \mathbf1_{\{\ell_j\ \mathrm{odd}\}},\qquad
I_n=\sum_{j=1}^m\binom{\ell_j}{2}.\]
No between-packet inversions are created, because the packet order is unchanged and all labels in an earlier packet precede all labels in every later packet.

## Proof

### 1. Unconditional strict negative dependence

View the cut indicators as a product of \(n-1\) Bernoulli variables ordered coordinatewise. Turning one zero bit into a one splits a packet of length \(a+b\) into lengths \(a,b\), with \(a,b\ge1\). The inversion count changes by \(-ab<0\). If \(a+b\) is odd, the odd-packet count is unchanged; if it is even, the count is unchanged or increases by two. Hence \(F_n\) is nondecreasing and \(I_n\) is strictly decreasing in every cut bit. Harris's product-measure covariance inequality gives \(\operatorname{Cov}(F_n,I_n)\le0\).

For strictness, condition on all cut bits except one. The conditional covariance at that bit is \(pq(F_1-F_0)(I_1-I_0)\le0\). It is strictly negative on the positive-probability event that all the other gaps are cut: the chosen gap joins two singleton packets, so changing zero to one raises \(F_n\) by two and reduces \(I_n\) by one. The remaining covariance of the two conditional expectations is nonpositive by Harris's inequality on the remaining product bits, since the expectations retain opposite monotonicities. Thus the total covariance is strictly negative for every \(n\ge2\) and \(0<p<1\).

### 2. Uniform compositions at a fixed packet count

A composition with \(m\) packets has exactly \(m-1\) cuts and therefore probability \(p^{m-1}(1-p)^{n-m}\), independent of the locations of the cuts. Consequently its conditional law given \(M_n=m\) is uniform on the \(\binom{n-1}{m-1}\) positive ordered compositions of \(n\) into \(m\) parts.

Suppose exactly \(f\) parts are odd. For each odd part write \(\ell=1+2x\), and for each even part write \(\ell=2+2x\), with \(x\ge0\) integral. The constraint on the sum becomes \(\sum x_j=s=(n-2m+f)/2\). There are \(\binom mf\) choices for the odd parts and \(\binom{s+m-1}{m-1}\) weak compositions of \(s\), yielding the asserted conditional probability and the exact feasible support.

Condition on a feasible \(f\) and on which parts are odd. The vector \((x_1,\ldots,x_m)\) is uniform over weak compositions of \(s\) into \(m\) parts. By stars-and-bars or the elementary uniform Dirichlet-multinomial representation,
\[\mathbb E x_j=\frac{s}{m},\qquad
\mathbb E[x_j(x_j-1)]=\frac{2s(s-1)}{m(m+1)}.\]
For an odd part its baseline \(b\) equals one, and for an even part it equals two. Expand
\[\binom{b+2x}{2}=\binom b2+(2b-1)x+2x^2.\]
Summing the expectations of this identity gives
\[g_{n,m}(f)=m-f+\left(5-\frac{2f}{m}\right)s+\frac{4s(s-1)}{m+1}.\]
Substituting \(f+2\) and \(s+1\) gives the displayed increment. For any two successive feasible values, \(m\ge2\), \(f\le m-2\) and \(n\ge m\); hence its numerator is at least
\[2m(m-1)-m^2+3m-4(m-2)-4=m^2-3m+4>0.\]
Thus the conditional mean of \(I_n\) is strictly increasing in \(F_n\) on its support. The identity
\[\operatorname{Cov}(F_n,I_n\mid M_n=m)
=\operatorname{Cov}(F_n,g_{n,m}(F_n)\mid M_n=m)\]
and an independent-copy covariance representation establish nonnegativity, with strictness exactly when the conditional support contains two or more values.

The feasible values are precisely those integers of parity \(n\) between \(\max(0,2m-n)\) and \(m\). There are at least two exactly when \(2+(n\bmod2)\le m\le n-2\). This proves the complete equality classification, including every small-size boundary.

### 3. Gaussian limit and constants

Let \((L_j)_{j\ge1}\) be independent geometric random variables with \(\Pr(L_j=\ell)=pq^{\ell-1}\), \(\ell\ge1\). The finite packet composition has the law of these renewal lengths stopped at \(n\), with the final length possibly truncated. Define the two-component reward
\[R_j=\begin{pmatrix}\mathbf1_{\{L_j\ \mathrm{odd}\}}\\\binom{L_j}{2}\end{pmatrix}.\]
The number of complete renewal intervals up to \(n\) divided by \(n\) tends to \(p\), and the terminal residual length has a uniformly geometric tail, because it requires an uninterrupted run of uncut gaps. Its contribution to either reward and the length-centering correction is \(O_{\Pr}(1)\). The multivariate renewal-reward central limit theorem (alternatively, the iid functional CLT followed by the renewal random-time change) therefore gives covariance
\[\Sigma_p=p\,\mathbb E[(R_j-\boldsymbol\mu_pL_j)(R_j-\boldsymbol\mu_pL_j)^{\mathsf T}],\qquad
\boldsymbol\mu_p=\frac{\mathbb ER_j}{\mathbb EL_j}.\]
The needed geometric moments are
\[\begin{aligned}
\mathbb EL&=1/p,& \mathbb EL^2&=(2-p)/p^2,\\
\mathbb E\mathbf1_{\{L\ \mathrm{odd}\}}&=1/(2-p),&
\mathbb E[L\mathbf1_{\{L\ \mathrm{odd}\}}]&=(p^2-2p+2)/(p(2-p)^2),\\
\mathbb E\binom L2&=q/p^2,&
\mathbb E[L\binom L2]&=q(3-p)/p^3,\\
\mathbb E\left[\mathbf1_{\{L\ \mathrm{odd}\}}\binom L2\right]&=q^2(p^2-2p+4)/(p^2(2-p)^3),&
\mathbb E\left[(\binom{L}{2})^2\right]&=q(p^2-6p+6)/p^4.
\end{aligned}\]
These follow by differentiating finite geometric-series rational functions and summing absolutely convergent series. Substitution gives exactly \(\Sigma_p\). Its diagonal entries are positive and its correlation has absolute value strictly below one for \(0<p<1\), since \((1+q^2)<(1+q)^2\). Convergence of second moments and covariance growth to these constants follows also from exponential-moment renewal-reward bounds; to avoid relying on a bare weak-limit claim, one can use the rational bivariate reward generating function and differentiate at the unit marks, which has a simple dominant pole and supplies the same \(O(n)\) covariance asymptotics. Therefore the stated limiting correlation is justified. \(\square\)

## Verification

The standalone standard-library checker `verify.py` enumerates all ordered compositions for every \(2\le n\le12\) and every packet count \(1\le m\le n\). It verifies the conditional positive/zero covariance classification, the exact regression and its increments, strict unconditional negative covariance for four rational cut probabilities, normalization, and six exact-rational evaluations of the limiting moment identities. It completes 536 exact-rational assertions. The file `CHECK_OUTPUT.txt` records the observed run result. These checks are finite evidence; the all-size sign theorem and the central limit are analytical statements proved above.

## Relationship to prior work

Y. Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1 (first publicly available September 10, 2026), defines exactly the independent-cut packet-reversal convention and proves sharp mixing/coupling results. Its introduction, model, exact one-card spectral section, and relevant results were inspected in full HTML. The fixed-point/inversion sign reversal, conditional regression and explicit bivariate covariance theorem are not stated there. The source's one-card spectrum is insufficient to imply the conditional two-statistic result without further combinatorial analysis.

R. Pemantle's original overhand shuffle work and later shuffle-cutoff analyses concern mixing rather than these finite joint statistics. Bender and Canfield's work on random compositions includes general asymptotic normality principles; generic renewal-reward limit theorems likewise cover a general mechanism of the Gaussian limit and are treated as established tools, not novel contributions. The new content assessed here is the exact contrasting sign classification for both conditioning regimes, its observable descent-count interpretation and the explicit covariance coefficients for this natural shuffle statistic.

Archibald, Blecher, Knopfmacher and Mays, *Inversions and Parity in Compositions of Integers* (2020), study inversions between composition parts, a different quantity from within-packet card inversions \(\sum\binom{\ell_j}{2}\). The closest statistical permutation literature on fixed points and inversions commonly concerns uniform random permutations, not independent packet reversals. Historic precedence is not conclusively established merely by failure of searches.

## Limitations

The theorem does not apply unchanged to the physical packet-order reversing convention, repeated shuffles, nonidentity starting decks, dependent cuts, or a cut probability varying with \(n\). Although exact finite conclusions hold for every admissible \(p\), the Gaussian limit holds for fixed \(p\in(0,1)\). No claim is made of independent validation or definitive historical priority. The finite verifier does not prove the infinite-size statements. General composition theorems may contain the Gaussian component implicitly; the claimed structural contribution is the contrasting finite conditional and unconditional covariance signs and exact conditional regression.

## References

1. Yunjiang Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1, https://arxiv.org/html/2610.00137v1 (source model and full-text comparison).
2. R. Pemantle, *Randomization time for the overhand shuffle*, Journal of Theoretical Probability 2 (1989), 37–49, https://doi.org/10.1007/BF01048267.
3. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions II: General Restrictions and Infinite Matrices*, Electronic Journal of Combinatorics 16 (2009), R108, https://doi.org/10.37236/197.
4. M. Archibald, A. Blecher, A. Knopfmacher and M. E. Mays, *Inversions and Parity in Compositions of Integers*, Journal of Integer Sequences 23 (2020), 20.4.1, https://cs.uwaterloo.ca/journals/JIS/VOL23/Archibald/arch3.html.
5. Standard Harris product-measure association and multivariate renewal-reward central limit theorem (classical tools, not asserted as new results).
