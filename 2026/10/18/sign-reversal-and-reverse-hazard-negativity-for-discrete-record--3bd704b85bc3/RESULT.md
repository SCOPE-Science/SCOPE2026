# Sign reversal and reverse-hazard negativity for discrete record events

## Finding
For iid draws from a finite ordered alphabet, the record indicators need not have the distribution-free independence of continuously distributed iid records. There is a structural sign dichotomy. With at least two positive masses \(p_k\), let \(R_j=\mathbf1\{X_j>\max(X_1,\ldots,X_{j-1})\}\) for \(j\ge2\). If \(h_k=p_k/F_k\), where \(F_k=\sum_{a\le k}p_a\), is nonincreasing, then for **every** pair of integers \(2\le s<t\),
\[\operatorname{Cov}(R_s,R_t)<0.\]
For arbitrary nondegenerate two-symbol laws the same strict inequality holds. However, three symbols already permit strict positive covariance for every fixed pair of times: set \(p_0=p_1=\varepsilon\) and \(p_2=1-2\varepsilon\). For all sufficiently small \(\varepsilon>0\),
\[\operatorname{Cov}(R_s,R_t)>0.\]
Thus three is the exact minimum alphabet size permitting positive covariance. The theorem does *not* assert that reverse-hazard monotonicity is necessary for negative covariance, or that any full vector of record indicators is negatively associated.

## Assumptions and scope
The sample \(X_1,X_2,\ldots\) is independent and identically distributed on a *finite* totally ordered alphabet \(\{0,1,\ldots,m-1\}\), with \(m\ge2\), \(p_k=\Pr(X_j=k)>0\), and \(\sum_k p_k=1\). Nonconsecutive support values may be relabeled in increasing order. Put \(F_{-1}=0\) and \(F_k=\sum_{a=0}^{k}p_a\). A **strict upper record** at time \(j\ge2\) requires the current observation to exceed every previous observation; ties are not records. The reverse hazard is \(h_k=p_k/F_k\), with \(h_0=1\). All record-time quantifiers concern integers \(2\le s<t<\infty\); time 1 is deterministic and omitted.

## Proof
First, elementary conditioning yields exact formulas that apply to any positive alphabet profile:
\[q_r:=\Pr(R_r=1)=\sum_{k=0}^{m-1}p_kF_{k-1}^{r-1},\qquad r\ge2,\]
and, because a record at time \(s\) with value \(a\) and one at time \(t\) with value \(b\) require \(a<b\),
\[J_{s,t}:=\Pr(R_s=R_t=1)=\sum_{0\le a<b<m}p_aF_{a-1}^{s-1}p_bF_{b-1}^{t-s-1}.\]
Consequently \(\operatorname{Cov}(R_s,R_t)=J_{s,t}-q_sq_t\). All sums are finite. An exponent zero is interpreted as one, including when its base is zero.

For a conceptual sign proof let \(M_s=\max_{1\le j\le s}X_j\). Given \(M_s=k\), exchangeability of the first \(s\) observations gives the exact conditional probability
\[u_s(k):=\Pr(R_s=1\mid M_s=k)=\frac{p_k F_{k-1}^{s-1}}{F_k^s-F_{k-1}^s}.\]
For \(k=0\) this equals zero when \(s\ge2\). For every \(k\ge1\), cancel \(p_k=F_k-F_{k-1}\) to obtain
\[u_s(k)=\left[\sum_{r=0}^{s-1}\left(\frac{F_k}{F_{k-1}}\right)^r\right]^{-1}.\]
The map from a positive ratio \(F_k/F_{k-1}\) to this reciprocal is strictly decreasing for \(s\ge2\). The assumption that \(h_k=p_k/F_k\) is nonincreasing is equivalent to \(p_k/F_{k-1}\) being nonincreasing for \(k\ge1\), hence to \(F_k/F_{k-1}\) being nonincreasing. Therefore \(u_s(k)\) is nondecreasing in \(k\), with \(u_s(0)=0<u_s(1)\).

Independence of future observations from the prefix shows
\[g_{s,t}(k):=\Pr(R_t=1\mid M_s=k)=\sum_{b>k}p_bF_{b-1}^{t-s-1}.\]
This function is strictly decreasing in \(k\) along adjacent support points because \(p_{k+1}>0\) and \(F_k>0\). Given \(M_s\), the event \(R_s\) (a function of the prefix) and the future record event \(R_t\) are conditionally independent. Hence
\[\operatorname{Cov}(R_s,R_t)=\operatorname{Cov}(u_s(M_s),g_{s,t}(M_s)).\]
For an independent copy \(M_s'\), the last covariance equals one half of the expectation of \((u_s(M_s)-u_s(M_s'))(g_{s,t}(M_s)-g_{s,t}(M_s'))\). Its integrand is nonpositive, and strictly negative when the pair of maxima consists of levels 0 and 1. Both levels have positive probability; thus the covariance is strictly negative.

For \(m=2\), any two post-initial strict record events are mutually exclusive: the sample maximum can increase only once. Both events individually have positive probability, proving strict negative covariance without a hazard hypothesis. To show positivity with three symbols, take \(p_0=p_1=\varepsilon\), \(p_2=1-2\varepsilon\), where \(0<\varepsilon<1/2\). The only ordered record-value pair at times \(s,t\) is \((1,2)\). Therefore
\[q_r=\varepsilon^r+(1-2\varepsilon)(2\varepsilon)^{r-1},\quad J_{s,t}=(1-2\varepsilon)\varepsilon^s(2\varepsilon)^{t-s-1}.\]
For every *fixed* \(2\le s<t\), as \(\varepsilon\downarrow0\),
\[J_{s,t}\sim2^{t-s-1}\varepsilon^{t-1},\qquad q_sq_t\sim2^{s+t-2}\varepsilon^{s+t-2}.\]
Because \(t-1<s+t-2\) for \(s\ge2\), the joint probability dominates the product of marginals for all sufficiently small \(\varepsilon\). This gives the positive covariance and completes the exact minimal-alphabet classification.

## Verification
The self-contained Python script `verify_records.py` uses only the standard library and `fractions.Fraction`. It independently enumerates complete sample words for 84 finite cases (two, three, and four symbols; three pairs of record times; 28 positive probability profiles), compares the joint and marginal probabilities against the displayed formulas, and checks 2,170 rational negative-covariance instances satisfying the reverse-hazard hypothesis. It also verifies strict positive covariance for 30 pairs of record times under the explicit three-symbol distribution with \(\varepsilon=1/100\). These finite checks corroborate the proof; they do not establish the infinite quantifiers, which follow from the algebra and stochastic monotonicity above.

## Relationship to prior work
Wergen, Volovik, Redner, and Krug (2012, arXiv:1206.4432) explicitly study strict records under rounding, giving marginal record-rate formulas and asymptotics, including for finite alphabets. Their complete five-page paper does not state the two-time reverse-hazard sign theorem or the three-symbol positive-covariance threshold. Oliver and Prodinger (online 2011, DOI 10.1007/s13370-011-0027-9) study **consecutive-value records** in geometric words under a different update rule and calculate associated mean and variance, not covariance of classical strict record events at prescribed sampling times. Prodinger (1996) studies geometric-word left-to-right maxima; a general result there could contain the geometric special case of the present theorem, but the full original text was not inspected. Literature on non-identically distributed continuous record events addresses a different mechanism and does not cover iid discrete ties. No claim that all possible literature equivalents have been excluded is made.

## Limitations
The negative-dependence condition is sufficient, not necessary; the theorem concerns pairwise covariance and not joint negative association. The positive construction depends on the selected finite pair of record times through the sufficiently-small bound on \(\varepsilon\); a common uniform bound for all times is not proved. The scope is finite alphabets with positive masses; no infinite-support extension or general mixture theorem is claimed. Some broad older record monographs and the 1996 geometric-word paper were not inspected in full, leaving a residual originality risk. The results are not independently audited.

## References
1. G. Wergen, D. Volovik, S. Redner, and J. Krug, *Rounding Effects in Record Statistics*, arXiv:1206.4432 (first posted 2012-06-20); *Physical Review Letters* 109, 164102 (2012), DOI 10.1103/PhysRevLett.109.164102.
2. K. Oliver and H. Prodinger, *Consecutive records in geometrically distributed words*, *Afrika Matematika* 23, 163–172 (online 2011-05-13), DOI 10.1007/s13370-011-0027-9.
3. H. Prodinger, *Combinatorics of geometrically distributed random variables: Left-to-right maxima*, *Discrete Mathematics* 153, 253–270 (1996), DOI 10.1016/0012-365X(95)00141-I.
4. B. C. Arnold, N. Balakrishnan, and H. N. Nagaraja, *Records*, Wiley (1998), for classical iid continuous-record independence and record terminology.
