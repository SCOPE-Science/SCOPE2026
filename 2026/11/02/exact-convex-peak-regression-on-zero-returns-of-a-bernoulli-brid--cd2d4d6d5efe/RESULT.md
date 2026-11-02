# Exact convex peak regression on zero returns of a Bernoulli bridge

## Finding

A uniformly selected simple symmetric random-walk bridge of \(2n\) steps, for any integer \(n\ge2\), has a strictly increasing and strictly convex (where at least three conditioning values exist) conditional expected peak count as a function of the number of interior zero returns. Specifically, writing \(P\) for the number of upward steps immediately followed by downward steps, and \(R\) for the number of strictly interior visits to zero,

\[\mathbb E[P\mid R=r]=\frac{n-1}{2}+\frac{r(r+2)}{4(2n-r-2)},\qquad 0\le r\le n-1.\]

For every set \(A\subseteq\{1,\ldots,n-1\}\) of prescribed zero-return indices there is also the time-location-independent pinning identity

\[\mathbb E[P\mid S_{2j}=0\text{ for every }j\in A]=\frac n2+\frac{|A|}{4}.\]

The pinning event allows *additional* returns outside \(A\); it is not the same as conditioning on the complete zero set. Consequently,

\[\operatorname{Cov}(P,R)=\frac14\left(\frac{4^n}{\binom{2n}{n}}-2\right)>0.\]

## Assumptions and scope

Fix \(n\ge2\). Let \(S_0=0\), let increments \(\xi_i=S_i-S_{i-1}\in\{-1,1\}\), and draw the increment sequence uniformly from all \(\binom{2n}{n}\) sequences with exactly \(n\) plus and \(n\) minus steps; equivalently, condition a fair simple random walk on \(S_{2n}=0\). Define

\[P=\sum_{i=1}^{2n-1}\mathbf1\{(\xi_i,\xi_{i+1})=(1,-1)\},\qquad R=\sum_{j=1}^{n-1}\mathbf1\{S_{2j}=0\}.\]

Every conditioning value \(r\in\{0,\ldots,n-1\}\) has positive probability. For the pinning identity take any fixed, deterministic subset \(A\) of the \(n-1\) potential interior return times. The strict discrete convexity assertion means \(\mathbb E[P\mid R=r+2]-2\mathbb E[P\mid R=r+1]+\mathbb E[P\mid R=r]>0\) for all \(0\le r\le n-3\).

## Proof

**Step 1: peak expectation in a single bridge.** In a bridge of \(2m\) steps with \(m\ge1\), exchangeability of the increments gives

\[\mathbb P((\xi_i,\xi_{i+1})=(1,-1))=\frac{m}{2(2m-1)}\]

for every \(1\le i<2m\). Summing shows that the expected number of peaks internal to this bridge is exactly \(m/2\).

**Step 2: exact pinning at arbitrary interior zero times.** Given \(S_{2j}=0\) for all \(j\in A\), the resulting \(|A|+1\) blocks are independent uniformly distributed bridges, with half-lengths summing to \(n\). By Step 1, their internal peak expectations sum to \(n/2\). At each of the \(|A|\) boundaries the last increment of the left block is equally likely to be up or down, and the first increment of the independent right block is equally likely to be up or down. Thus a boundary is an extra peak with probability exactly \(1/4\). This proves the pinning identity, including boundary blocks of half-length one.

**Step 3: translate the pinning identity into a generating-function derivative.** Write \(q_r=\mathbb P(R=r)\) and \(G(z)=\mathbb E[z^R]\). Expanding the product

\[z^R=\prod_{j=1}^{n-1}\bigl(1+(z-1)\mathbf1\{S_{2j}=0\}\bigr)\]

and using Step 2 on each subset gives the polynomial identity

\[\mathbb E[Pz^R]=\frac n2G(z)+\frac{z-1}{4}G'(z).\]

Comparing coefficients yields, with \(q_n=0\),

\[\mathbb E[P\mid R=r]=\frac n2+\frac{r q_r-(r+1)q_{r+1}}{4q_r}.\]

**Step 4: exact return-count distribution.** A first-return excursion of positive semilength \(m\) consists of a positive or negative primitive Dyck path; its number of possible signed shapes is \(2C_{m-1}\), where \(C_j=\frac1{j+1}\binom{2j}{j}\). Therefore its semilength enumerator is

\[F(t)=\sum_{m\ge1}2C_{m-1}t^m=1-\sqrt{1-4t},\qquad F=\frac{2t}{1-F/2}.\]

Exactly \(r\) interior returns means \(r+1\) consecutive primitive excursions. Lagrange inversion, or the binomial-series coefficient extraction, gives their count

\[a_{n,r+1}=[t^n]F(t)^{r+1}=\frac{r+1}{n}\,2^{r+1}\binom{2n-r-2}{n-r-1}.\]

Hence \(q_r=a_{n,r+1}/\binom{2n}{n}\), and, for \(r<n-1\),

\[\frac{(r+1)q_{r+1}}{q_r}=\frac{2(r+2)(n-r-1)}{2n-r-2}.\]

The same substitution holds at \(r=n-1\) when \(q_n=0\). Simplifying the result of Step 3 gives the claimed conditional mean.

**Step 5: strict increase, convexity, and covariance.** Put \(a=2n-2>0\). On \(0\le x\le n-1\), the nonconstant correction can be written

\[h(x)=\frac{x(x+2)}{4(a-x)}=\frac14\left(\frac{a(a+2)}{a-x}-x-a-2\right).\]

Its derivatives are

\[h'(x)=\frac14\left(\frac{a(a+2)}{(a-x)^2}-1\right)>0,\qquad h''(x)=\frac{a(a+2)}{2(a-x)^3}>0,\]

using \(a(a+2)>a^2\) and \(0\le x\le n-1<a\) for \(n\ge3\); the \(n=2\) two-value increase is direct. Thus the regression is strictly increasing and discretely convex wherever the latter is defined.

Applying the pinning identity to one index gives \(\operatorname{Cov}(P,\mathbf1\{S_{2j}=0\})=\mathbb P(S_{2j}=0)/4\). Summing gives \(\operatorname{Cov}(P,R)=\mathbb E[R]/4\). The convolution identity

\[\sum_{j=0}^n\binom{2j}{j}\binom{2n-2j}{n-j}=4^n\]

implies \(\mathbb E[R]=4^n/\binom{2n}{n}-2\); this is positive for \(n\ge2\). Finally, Stirling's expansion \(\binom{2n}{n}=4^n(\pi n)^{-1/2}(1+O(n^{-1}))\) gives

\[\operatorname{Cov}(P,R)=\frac{\sqrt{\pi n}}4-\frac12+O(n^{-1/2}).\]

## Verification

The accompanying Python 3 standard-library script `bridge_peak_verifier.py` enumerates all \(66{,}196\) balanced bridges for \(1\le n\le9\), checks the complete conditional expectation table and covariance for these sizes, and checks all subset-pinning expectations through \(n=7\). It also verifies the exact return-count coefficient formula and mean identity through \(n=80\). Execution passed \(3{,}707\) exact assertions. This is finite reproducibility evidence only; the proof above establishes the unrestricted claims.

To reproduce: run `python3 bridge_peak_verifier.py` in the same directory as this file. There are no external dependencies.

## Relationship to prior work

Labarbe and Marckert (2006; arXiv:math/0601624, Proposition 1) established the exact peak-count marginal for Bernoulli bridges and studied their shape when conditioned on peaks. Godrèche (2016; arXiv:1611.01434, Section 2.5) studies the marginal number of excursions and their lengths in tied-down walks. Those marginal results alone do not state the pinning identity, the exact peak regression conditional on the return count, or its monotone convexity.

Mortimer and Prellberg (2012; arXiv:1208.3061, Theorems 1 and 3) provide a peak/odd-height-step bijection for Dyck and bilateral Dyck paths; contact count is preserved for nonnegative Dyck paths in Theorem 1, while the bilateral extension does not establish joint contact-preserving peak enumeration. The result here concerns unconstrained signed bridges and conditions on visits to zero. Older joint-statistics work by Kreweras (1986) on nonnegative bridges warrants a historical-priority check; its full text was not accessible in this investigation.

## Limitations

The result assumes a fair simple random walk conditioned to end at zero after an even number of steps. It asserts only the first conditional moment of peaks, not stochastic ordering of the complete conditional peak distributions. Pinning at specified times permits other zero visits; it is distinct from conditioning on the *exact* set of return times. No independence is asserted between peaks and returns. Historical coverage may exist in older multi-parameter path-enumeration literature; independent audit has not been performed.

## References

1. J.-M. Labarbe and J.-F. Marckert, *Asymptotics of Bernoulli random walks, bridges, excursions and meanders with a given number of peaks*, arXiv:math/0601624, first public version January 25, 2006; *Electronic Journal of Probability* 12 (2007), 229–261.
2. P. R. G. Mortimer and T. Prellberg, *A Bijection on Bilateral Dyck Paths*, arXiv:1208.3061, initially August 15, 2012.
3. C. Godrèche, *Longest interval between zeros of the tied-down random walk, the Brownian bridge and related renewal processes*, arXiv:1611.01434, initially November 4, 2016.
4. G. Kreweras, *Joint distributions of three descriptive parameters of bridges*, in *Combinatoire énumérative*, Lecture Notes in Mathematics 1234 (1986), 177–191, DOI:10.1007/BFb0072516 (full text not accessed).
