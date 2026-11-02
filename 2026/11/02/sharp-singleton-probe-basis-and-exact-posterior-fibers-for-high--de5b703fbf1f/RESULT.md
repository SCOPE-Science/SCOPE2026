# Sharp singleton-probe basis and exact posterior fibers for high-threshold knowing value

## Finding
Fix a finite, labelled nonempty world set \(W=\{1,\ldots,n\}\). At one fixed agent/world, let \(\mu=(\mu_1,\ldots,\mu_n)\) be an arbitrary probability distribution. Assume the **same fixed term-value assignment** supplies a binary term \(t_S\) taking value \(1\) precisely on each subset \(S\subseteq W\), and value \(0\) elsewhere. Observe only high-threshold knowing-value statements \(Kv^\eta(t_S)\), for every rational \(\eta\in(1/2,1]\). The following three equivalence conditions hold for arbitrary distributions \(\mu,\nu\):

1. All binary terms \(t_S\) have the same high-threshold knowing-value profile under \(\mu\) and \(\nu\).
2. It suffices to check **only the \(n\) singleton terms** \(t_{\{i\}}\), for all rational high thresholds.
3. \(\mu_i\mu_j=\nu_i\nu_j\) for every pair of different coordinates \(i,j\).

Every nontrivial observational equivalence class has exactly one of two forms: (a) the class of **all \(n\) Dirac measures**, or (b) the **two** measures with positive support \(\{i,j\}\) and unequal weights \(a,1-a\), obtained by exchanging those two positive weights. All other measures, including equal-weight two-point measures and every measure of support at least three, have singleton observational classes. When \(n=1\), the unique Dirac class is a singleton.

On the rational denominator-\(d\) grid, with \(d\ge1\) and all \(d\mu_i\) nonnegative integers, the number of distinct high-threshold observational signatures is exactly
\[
\binom{d+n-1}{n-1}-(n-1)-\binom n2\left\lfloor\frac{d-1}{2}\right\rfloor.
\]
For \(n\ge3\), no proper subset of the prescribed singleton-probe family suffices to determine all-subset observational equivalence, even when every rational high threshold is available. For \(n=2\), one singleton probe suffices, and for \(n=1\), none is required.

## Assumptions and scope
A distribution is an element of the real simplex \(\Delta_{n-1}\), without strictly positive or rational-mass assumptions except in the finite-grid count. Fix one agent at one evaluation world. We vary only its local measure, keeping the world set and all term-value assignments identical. The language is assumed to contain terms with exactly the binary fibers \(S,W\setminus S\) for all \(S\). The operator semantics is \(Kv^\eta(t)\) true iff exactly one value fiber has probability at least \(\eta\), with \(\eta\in\mathbb Q\cap(1/2,1]\). Since \(\eta>1/2\), uniqueness is automatic. Nothing is claimed about a vocabulary lacking these binary terms or about observations using the separate propositional thresholds \(K^\theta\), additional modalities, or changing term assignments. These richer observations can distinguish measures in the nontrivial fibers described here.

## Proof
Put \(m_\mu(S)=\sum_{i\in S}\mu_i\). The two fibers of \(t_S\) have masses \(m_\mu(S)\) and \(1-m_\mu(S)\). Thus the high-threshold truth profile is exactly the upper-cut profile of
\[
M_\mu(S)=\max\{m_\mu(S),1-m_\mu(S)\}=\frac{1+|2m_\mu(S)-1|}{2}.
\]
Two such real values in \([1/2,1]\) have identical upper cuts at all rational thresholds strictly greater than \(1/2\) if and only if they are equal, including at the endpoint \(1/2\). Therefore complete agreement of the \(Kv\) profiles is equivalent to \(M_\mu(S)=M_\nu(S)\) for all subsets.

In particular, singleton agreement says \(|2\mu_i-1|=|2\nu_i-1|\), so at each coordinate \(\nu_i=\mu_i\) or \(\nu_i=1-\mu_i\). Let \(F\) consist of coordinates at which they are actually different. Normalization gives
\[
0=\sum_{i\in F}(\nu_i-\mu_i)=|F|-2\sum_{i\in F}\mu_i.
\]
A nonempty \(F\) cannot have cardinality one, since the required mass \(\mu_i=1/2\) would make that coordinate unchanged. It cannot have cardinality at least three, since \(\sum_{i\in F}\mu_i=|F|/2>1\). Consequently \(F\) contains exactly two indices, say \(i,j\), and \(\mu_i+\mu_j=1\); all remaining masses vanish, and the two weights are exchanged. Conversely, exchanging weights on a two-element support preserves \(M(S)\) for every subset: if \(S\) contains zero or both support points its mass is unchanged; if it contains exactly one its mass is complemented. All Dirac measures are an included special case; their binary-term fiber maxima equal one for all \(S\). Hence singleton equality implies all-subset equality, and the classes listed above are exhaustive.

For the equivalence with pair products, assign to a subset its sign vector \(\varepsilon_i(S)=1\) on \(S\) and \(-1\) outside. Then
\[
(2m_\mu(S)-1)^2
=\left(\sum_i\varepsilon_i(S)\mu_i\right)^2
=\sum_i\mu_i^2+2\sum_{i<j}\varepsilon_i(S)\varepsilon_j(S)\mu_i\mu_j.
\]
Orthogonality of the quadratic Walsh characters on \(\{-1,1\}^n\) gives the exact reconstruction identity, for \(i\ne j\),
\[
2\mu_i\mu_j=2^{-n}\sum_{S\subseteq W}
(2m_\mu(S)-1)^2\varepsilon_i(S)\varepsilon_j(S).
\]
Thus complete observations determine all off-diagonal products. Conversely, those products determine \(\sum_i\mu_i^2=1-2\sum_{i<j}\mu_i\mu_j\) from normalization, hence determine all the squared signed sums and all the observations. This proves all three equivalences even at the degenerate boundaries \(n=1,2\).

The number of gridded measures is \(\binom{d+n-1}{n-1}\). Collapsing the \(n\) different Dirac measures into one signature decreases this count by \(n-1\). For each unordered pair of support positions, the positive integer pairs \((a,d-a)\) with \(1\le a\le d-1\) yield exactly \(\lfloor(d-1)/2\rfloor\) distinct unequal-weight transpositions, each decreasing the signature count by one. These classes are disjoint and exhaust all collisions, proving the formula. The rational thresholds \(\eta=k/d\), \(\eta>1/2\), already capture every possible grid fiber maximum, so the same census holds on this finite threshold list.

Finally, take any omitted singleton index \(i\) with \(n\ge3\), and distinct remaining indices \(j,k\). Set the respective coordinate masses of \(\mu\) at \((j,i,k)\) to \((6/10,3/10,1/10)\) and those of \(\nu\) to \((4/10,5/10,1/10)\), with all others zero. Every remaining singleton term has equal profiles because the two masses at \(j\) are complements; the omitted term detects a difference, since its maxima are \(7/10\) and \(1/2\). The distributions are not globally observationally equivalent. For \(n=2\), singleton terms are complements and hence have identical observations within one measure, so either singleton alone suffices; for \(n=1\), all measures coincide. This establishes the sharp probe count within the prescribed singleton family.

## Verification
The accompanying dependency-free `checker.py` enumerates all nonnegative integer compositions of \(d\) into \(n\) parts for \(1\le n\le5\), \(1\le d\le7\), constructs the actual \(Kv\) truth tables for every subset and threshold \(k/d>1/2\), compares their equivalence-class partitions with those from singleton truths and pair products, and checks the exact census and class sizes. It independently verifies the quadratic Walsh recovery identity for \(2\le n\le5\), \(1\le d\le5\), and checks explicit minimality witnesses for \(3\le n\le9\). Its recorded run reports 35 grid cases, 1,281 distributions, 3,445 Walsh pair checks, 42 witnesses, and `ALL_CHECKS_OK`. The infinite theorem follows from the proof, not from finite enumeration.

## Relationship to prior work
Wang, *A Dual-Threshold Probabilistic Knowing Value Logic* (arXiv:2603.24865v1, 25 March 2026), Definition 3.4 and Proposition 4.3, supplies the exact non-factive high-threshold knowing-value semantics and automatic uniqueness. Its principal results concern soundness and structured weak completeness; the relevant semantic, theorem, and concluding sections inspected do not state this complete posterior-observation fiber classification or its sharp singleton-probe and rational-grid consequences.

There is a strong structural connection with phaseless recovery under Bernoulli sign measurements: for all subsets, the squared signed mass is the full quadratic sign-measurement profile. Krahmer and Liu, *Phase Retrieval Without Small-Ball Probability Assumptions* (arXiv:1604.07281v3), explicitly describe Dirac ambiguities for constant-modulus measurements and establish random-measurement recovery theorems on nonpeaky signal classes, rather than the precise nonnegative unit-simplex fibers and their minimal singleton-probe basis. The quadratic Walsh computation is standard algebra; novelty is asserted only for the combined complete modal observational classification, sharp restricted probe basis, and exact rational-grid census, within the inspected sources.

## Limitations
This is an exact result about one local probability measure observed through the specified non-factive \(Kv\) fragment at all rational high thresholds with a rich, fixed binary-term vocabulary. It does not claim indistinguishability for the full dual-threshold modal language, whose \(K^\theta\) formulas can directly distinguish posterior masses, nor for arbitrary restricted term languages. Neither the number of observations at a finite threshold list for arbitrary real distributions nor any noise-robust reconstruction is treated. Earlier phase-retrieval results may contain equivalents under different terminology.

## References
1. Shanxia Wang, *A Dual-Threshold Probabilistic Knowing Value Logic*, arXiv:2603.24865v1 (first public 25 March 2026), https://arxiv.org/html/2603.24865v1 . Definition 3.4, Proposition 4.3, and Sections 7–8.
2. Felix Krahmer and Yi-Kai Liu, *Phase Retrieval Without Small-Ball Probability Assumptions*, arXiv:1604.07281v3, https://arxiv.org/html/1604.07281v3 . Sections I-A, I-C, III, V and X.
