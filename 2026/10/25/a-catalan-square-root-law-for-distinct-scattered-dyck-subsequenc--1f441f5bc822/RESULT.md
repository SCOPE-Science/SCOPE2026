# A Catalan square-root law for distinct scattered Dyck subsequences of Bernoulli words

## Finding

Let \(W_n\) be a length-\(n\) word drawn independently over \(\{0,1\}\), with \(\Pr(1)=p\in(0,1)\) and \(\Pr(0)=q=1-p\). Let \(D_n\) be the number of **distinct nonempty Dyck words** occurring as scattered subsequence strings of \(W_n\), counted once per string. Here \(0\) is an opening parenthesis and \(1\) is a closing parenthesis; a Dyck word has equally many of each and every prefix has at least as many \(0\)s as \(1\)s.

Put \(t=pq\), \(g_0(z)=qz/(1-pz)\), \(g_1(z)=pz/(1-qz)\), and \(u(z)=g_0(z)g_1(z)=tz^2/(1-z+tz^2)\). With the Catalan generating function \(C(v)=(1-\sqrt{1-4v})/(2v)\), continued at \(C(0)=1\), the exact all-length expectation generating function is
\[
\boxed{\sum_{n\ge0}\mathbb E[D_n]z^n=\frac{C(u(z))-1}{1-z}.}
\]
Set
\[
r=\frac{2}{1+\sqrt{1+12t}},\qquad h=\frac{3(2-r)}{4(1-r)}.
\]
For every fixed \(p\in(0,1)\),
\[
\boxed{\mathbb E[D_n]\sim\frac{\sqrt{h}}{(1-r)\sqrt\pi}\,r^{-n}n^{-3/2}.}
\]
The exponential growth base is uniquely maximized over Bernoulli biases at \(p=1/2\); in that case
\[
\boxed{\mathbb E[D_n]\sim3\sqrt{\frac3\pi}\,\frac{(3/2)^n}{n^{3/2}}.}
\]
Thus imposing both global balance and the prefix-nonnegative constraint leads to an extra inverse-linear suppression relative to unrestricted balanced scattered subsequence patterns, rather than merely changing the exponential base.

## Assumptions and scope

For a source word \(w=w_1\cdots w_n\), a scattered subsequence is \(w_{i_1}\cdots w_{i_k}\) for increasing indices. If a Dyck pattern has multiple positional embeddings, it is counted only once. The empty Dyck pattern is excluded. The finite alphabet is precisely two parentheses symbols; probabilities are strictly between zero and one and remain fixed as \(n\to\infty\). Every generating-function identity is valid for all nonnegative integer source lengths, and the asymptotic statement concerns expectations rather than typical sample values.

## Proof

**Step 1: first-occurrence waiting times.** For any fixed nonempty pattern \(v=a_1\cdots a_k\), greedily match its letters from left to right in the independent infinite source. The waiting times to each required symbol are independent geometric random variables with success parameter \(\pi_{a_i}\), supported on \(\{1,2,\ldots\}\). Their probability generating functions are \(g_a(z)=\pi_a z/(1-(1-\pi_a)z)\). Writing \(T_v\) for the first completion index, the event \(v\) is a subsequence of \(W_n\) is exactly \(T_v\le n\). Consequently
\[
\sum_{n\ge0}\Pr(v\text{ is a subsequence of }W_n)z^n
=\frac{\prod_{i=1}^kg_{a_i}(z)}{1-z}.
\]
Linearity of expectation over distinct pattern strings is valid at every source length, since only finitely many patterns can be embedded.

**Step 2: Catalan enumeration.** Every Dyck word of length \(2m\) has precisely \(m\) zeros and \(m\) ones, and there are \(\operatorname{Cat}_m=(m+1)^{-1}\binom{2m}{m}\) of them. Accordingly, for \(m\ge1\), summing the previous identity over these distinct patterns gives \(\operatorname{Cat}_m g_0(z)^m g_1(z)^m/(1-z)\). Summing over \(m\ge1\) yields the exact asserted generating function \((C(u(z))-1)/(1-z)\). No probabilistic independence between *different* Dyck patterns is assumed or used.

**Step 3: locate and isolate the dominant branch point.** Since \(u(0)=0\), \(u(1)=1\), and \(u\) is strictly increasing for real \(z\in(0,1)\), the first positive solution of \(4u(r)=1\) lies in \((0,1)\). The equation reduces to \(3tz^2+z-1=0\), giving the displayed \(r\). Each coefficient of \(u(z)\) is strictly positive at all lengths at least \(2\), hence on the circle \(\lvert z\rvert=r\), strict triangle inequality shows \(\lvert u(z)\rvert<u(r)=1/4\) unless \(z=r\). The poles of \(g_0,g_1\) are at real points beyond \(1\), and \(1/(1-z)\) is analytic at \(r\). Thus \(r\) is the unique dominant singularity; the same inequalities yield a suitable slit neighborhood for the standard square-root transfer.

**Step 4: compute the exact singular constant.** Differentiating \(u(z)=tz^2/(1-z+tz^2)\),
\[
u'(z)=\frac{tz(2-z)}{(1-z+tz^2)^2}.
\]
Using \(4u(r)=1\) and \(3tr^2=1-r\), one gets
\[
1-4u(z)=h(1-z/r)+O((1-z/r)^2),\quad
h=4r u'(r)=\frac{3(2-r)}{4(1-r)}.
\]
The Catalan function satisfies \(C(v)=2-2\sqrt{1-4v}+O(1-4v)\) near \(v=1/4\). Hence the singular term of \((C(u(z))-1)/(1-z)\) is
\[
-\frac{2\sqrt{h}}{1-r}(1-z/r)^{1/2}.
\]
The elementary square-root coefficient transfer \([z^n](1-z/r)^{1/2}\sim-r^{-n}/(2\sqrt\pi\,n^{3/2})\) gives the asserted asymptotic constant. The displayed \(r\) is strictly decreasing in \(t\), while \(t=p(1-p)\le1/4\) with equality only at \(p=1/2\); this proves the unique exponential optimizer. At \(p=1/2\), \(r=2/3\) and \(h=3\), giving \(3\sqrt{3/\pi}\).

## Verification

The accompanying standalone `verify.py` computes the Catalan-substitution rational-power-series coefficients by exact fraction arithmetic, and separately enumerates actual sets of distinct scattered subsequences of every binary word up to recorded finite lengths, retaining precisely the nonempty prefix-balanced words. It checks four rational source distributions and verifies the unique singular radius and its fair-source constant symbolically using exact formulas. Finite enumeration confirms instances, while Steps 1–4 prove the infinite identities and asymptotics.

## Relationship to prior work

Biers-Ariel, Godbole and Kelley study expectations for unrestricted distinct scattered subsequences of independent sources, without restricting patterns to Dyck language. Collins treats the unrestricted fair-binary mean and length restrictions. Mol, Rampersad and Shallit investigate Dyck **contiguous factors** of automatic sequences, notably Thue–Morse, rather than distinct **scattered subsequences of random** sources. Catalan enumeration and square-root transfer are classical, and neither component is claimed as new independently. The result is their precise combination for a nonregular pattern language with biased source probabilities and an explicit asymptotic constant. An equivalent instance within general weighted-context-free-language analyses remains a possible unindexed prior result.

## Limitations

The result applies to finite iid Bernoulli sources and the standard one-type Dyck language. It does not establish concentration, a limit distribution, a corresponding theorem for arbitrary stationary dependent sources, or a multitype Dyck language. The originality assessment is limited to the recorded comparisons and inspected works, not a proof that no equivalent result exists anywhere.

## References

1. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661 (first posted 2017-04-27), https://arxiv.org/pdf/1704.08661.
2. M. J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288 (first posted 2013-10-28), https://arxiv.org/abs/1310.7288.
3. L. Mol, N. Rampersad and J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145 (2023), https://arxiv.org/pdf/2301.06145.
4. Classical Catalan enumeration: \(\operatorname{Cat}_m=(m+1)^{-1}\binom{2m}{m}\) and \(C(v)=1+vC(v)^2\).
