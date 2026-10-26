# The four-letter optimum for mean scattered-palindrome growth

## Finding

Let \(\Sigma\) be any finite alphabet of size \(q\ge 2\), and let \(\boldsymbol\pi=(\pi_a:a\in\Sigma)\) have strictly positive entries summing to one. Draw an independent length-\(n\) word \(W_n\) with letter probabilities \(\pi_a\). Define \(P(W_n)\) as the number of **distinct nonempty palindromic scattered subsequence strings** of \(W_n\); repeated positional realizations count just once. Put

\[
g_a(z)=\frac{\pi_a z}{1-(1-\pi_a)z},\quad
U(z)=\sum_{a\in\Sigma}g_a(z),\quad
V(z)=\sum_{a\in\Sigma}g_a(z)^2.
\]

The exact ordinary generating function of the expectations is

\[
\boxed{\sum_{n\ge0}\mathbb E[P(W_n)]z^n
=\frac{U(z)+V(z)}{(1-z)(1-V(z))}.}
\]

There is a unique \(r\in(0,1)\) with \(V(r)=1\), and

\[
\mathbb E[P(W_n)]\sim C(\boldsymbol\pi)\,r^{-n},\qquad
C(\boldsymbol\pi)=\frac{U(r)+1}{(1-r)rV'(r)}>0.
\]

**Sharp alphabet-independent extremum.** Over every finite alphabet and every positive independent-source probability vector, the exponential growth rate satisfies

\[
\boxed{r^{-1}\le\frac54,}
\]

with equality **if and only if** the source has exactly four letters, each of probability \(1/4\), up to relabeling. For this unique optimizer,

\[
\sum_{n\ge0}\mathbb E[P(W_n)]z^n
=\frac{8z(2-z)}{(1-z)(4-z)(4-5z)},\qquad
\mathbb E[P(W_n)]\sim3\left(\frac54\right)^n.
\]

## Assumptions and scope

A scattered subsequence is obtained by choosing strictly increasing letter positions, without requiring adjacency. A palindrome is invariant under reversal. Distinctness is by **letter string**, not by the number of embeddings. The empty palindrome is excluded, so \(P(W_0)=0\). The source is independent, identically distributed across positions, with all its \(q\ge2\) support probabilities positive; the alphabet is fixed while \(n\) tends to infinity. For alphabets with formally zero-probability letters, remove those letters from the support before applying the theorem.

All formal generating-function identities hold as power series in \(z\). Their analytic interpretation near the dominant positive pole is justified below. The optimization ranges over any finite number of supported source letters, **not** words maximizing the deterministic count.

## Proof

**1. Greedy occurrence of a fixed pattern.** Fix a nonempty string \(u=u_1\cdots u_m\) over \(\Sigma\). Scan an infinite independent sample, greedily matching \(u_1\), then \(u_2\), and so forth. The successive waiting times \(T_j\) have independent geometric distributions supported on the positive integers, with success probabilities \(\pi_{u_j}\). Their probability generating functions are \(g_{u_j}(z)\). The greedy embedding completes by time \(n\) if and only if \(u\) is a scattered subsequence of \(W_n\), hence

\[
\sum_{n\ge0}\Pr\{u\preceq W_n\}z^n
=\frac1{1-z}\prod_{j=1}^m g_{u_j}(z).
\tag{1}
\]

The factor \((1-z)^{-1}\) converts the distribution of the completion time into its cumulative distribution. Independence follows from disjoint successive blocks of independent sampled letters even when pattern symbols repeat.

**2. Sum exactly once over palindrome strings.** For even length \(2j\), \(j\ge1\), each palindrome is uniquely \(v v^{\mathrm{rev}}\) with \(|v|=j\), so summing the product in (1) over such patterns gives \(V(z)^j\). For odd length \(2j+1\), \(j\ge0\), a palindrome is uniquely \(v a v^{\mathrm{rev}}\); summation gives \(U(z)V(z)^j\). Each possible palindrome is included exactly once in this sum of occurrence indicators. Interchanging sums as formal power series is valid because only finitely many patterns can contribute to each coefficient. Consequently

\[
\sum_{n\ge0}\mathbb E[P(W_n)]z^n
=\frac1{1-z}\left(\sum_{j\ge1}V(z)^j+U(z)\sum_{j\ge0}V(z)^j\right)
=\frac{U(z)+V(z)}{(1-z)(1-V(z))}.
\]

**3. Dominant pole and asymptotic constant.** As \(q\ge2\), each \(0<\pi_a<1\); therefore \(g_a\) is analytic on a neighborhood of the closed unit disk and its coefficients at every positive degree are positive. On \([0,1]\), \(V\) is strictly increasing with \(V(0)=0\) and \(V(1)=q>1\). There is a unique \(r\in(0,1)\) with \(V(r)=1\), and \(V'(r)>0\). For any complex \(|z|<r\), positivity implies \(|V(z)|\le V(|z|)<1\), so the generating function has no singularity there. Its coefficients in \(V\) are strictly positive at every degree at least two. Thus equality in \(|V(z)|\le V(r)=1\) for \(|z|=r\) would require \(z/r=1\); there is no competing pole on the circle. Finally \(U(r)+V(r)>0\), so the pole at \(r\) does not cancel. A simple-pole expansion gives

\[
\frac{U(z)+V(z)}{(1-z)(1-V(z))}
=\frac{U(r)+1}{(1-r)rV'(r)}\frac1{1-z/r}+H(z),
\]

where \(H\) is analytic in some disk of radius greater than \(r\). Coefficient extraction proves the asserted asymptotic.

**4. A universal inequality with rigid equality.** At \(z=4/5\), direct substitution yields

\[
g_a(4/5)=\frac{4\pi_a}{1+4\pi_a},\qquad
\pi_a-g_a(4/5)^2
=\frac{\pi_a(4\pi_a-1)^2}{(1+4\pi_a)^2}\ge0.
\]

Summing over all letters gives \(V(4/5)\le\sum_a\pi_a=1\). Since \(V\) is strictly increasing and \(V(r)=1\), this implies \(r\ge4/5\), or \(r^{-1}\le5/4\). Equality requires \(4\pi_a-1=0\) for every supported letter. As the probabilities sum to one, this forces exactly four letters, all of mass \(1/4\). Conversely, those four probabilities give equality.

For \(q=4\), \(\pi_a=1/4\), we have \(g_a(z)=z/(4-3z)\). Substituting \(U=4g_a\) and \(V=4g_a^2\) in the exact identity yields the displayed rational function; its simple pole at \(z=4/5\) has coefficient \(3\). This completes the proof.

## Verification

The self-contained `verify.py` enumerates every source word for five exact rational probability vectors and computes its full set of distinct palindromic scattered subsequences **directly from positional masks**. Its independently computed expectation agrees coefficient-by-coefficient with the rational generating-function prediction for each tested length. The checker evaluates seven exact rational instances of the sharp inequality and symbolically checks the four-letter specialization. Its successful output is:

`VERIFY_OK distributions=5 exhaustive_source_words=15091 sharp_bound_trials=7 exact_q4_gf=true`

These finite calculations test implementation and normalization; the infinite theorem and the unique global optimizer follow from the preceding proof, not from enumeration.

## Relationship to prior work

Biers-Ariel, Godbole and Kelley analyze the mean number of **all** distinct scattered subsequences of random words, including nonuniform sources [1]. Mahalingam and Pandoh study deterministic extremal numbers of **distinct scattered palindromes** in finite words [2]. Kosche, Koß, Manea and Siemer analyze absent scattered subsequences and arch methods, not the present expectation [3]. Rubinchik and Shur study **palindromic contiguous factors** of random words [4], a different occurrence relation with different asymptotic behavior. The present claim combines the scattered-palindrome restriction with random-source weighting and proves an exact rational law and a uniquely four-letter universal optimization; neither its expectation nor the universal \(5/4\) extremum is contained in the inspected relevant sections of [1]–[4].

## Limitations

The result concerns the **mean**, not concentration, variance, or almost-sure growth. It does not solve deterministic maximum-scattered-palindrome problems or extend the i.i.d. assumption to Markov sources. A generic weighted-pattern enumerator may implicitly yield the rational formula; an equivalent unindexed treatment remains possible. No independent mathematical audit is claimed.

## References

1. Y. Biers-Ariel, A. Godbole, E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661 (first public 2017-04-27), especially Sections 2–3. https://arxiv.org/abs/1704.08661
2. K. Mahalingam, P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729 (first public 2021-08-05), especially Sections 3–5. https://arxiv.org/abs/2108.02729
3. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public 2021-08-31), especially Sections 2–4. https://arxiv.org/abs/2108.13968
4. M. Rubinchik, A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043 (first public 2015-05-29), especially Sections 1, 3–5. https://arxiv.org/abs/1505.08043
