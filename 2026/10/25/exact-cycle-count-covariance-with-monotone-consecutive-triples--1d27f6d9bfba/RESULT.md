# Exact cycle-count covariance with monotone consecutive triples

## Finding
For every integer \(n\ge3\), let \(\pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\). Write \(C\) for the total number of cycles of \(\pi\), including fixed points. Define the increasing-triple and decreasing-triple counts
\[
U=\sum_{a=1}^{n-2}{\bf1}\{\pi(a)<\pi(a+1)<\pi(a+2)\},\qquad
V=\sum_{a=1}^{n-2}{\bf1}\{\pi(a)>\pi(a+1)>\pi(a+2)\}.
\]
Then
\[
\boxed{\operatorname{Cov}(C,U)=\frac{3n-2}{6n(n-1)},\qquad
\operatorname{Cov}(C,V)=\frac{10-3n}{6n(n-1)}.}
\]
More precisely, for **each** location \(1\le a\le n-2\), the individual increasing/decreasing triple indicators have covariances with \(C\) equal to the displayed respective expressions divided by \(n-2\). Thus their cross-covariance is independent of the location. The first covariance is always positive, while the second is positive at \(n=3\) and negative at every \(n\ge4\); both decay as \(1/n\).

## Assumptions and scope
A permutation is viewed simultaneously as the list of its images and as the corresponding bijection for cycle decomposition. A consecutive pattern refers to adjacent **positions** in the image list, not to adjacent elements of a cycle. Expectations and covariances are under the uniform measure on the symmetric group. The result concerns precisely the two monotone length-three patterns, without restrictions on cycles or other entries.

## Proof
**Conditional-cycle contraction lemma.** Specify \(k\) distinct input positions and \(k\) distinct image values, thereby prescribing \(k\) arrows of a bijection. These arrows form vertex-disjoint directed chains and already closed directed cycles. With \(m=n-k\) unprescribed arrows, contract each nonclosed chain to a single vertex. The remaining bijection induces a uniformly random permutation on the \(m\) contracted chains. Each pre-existing closed cycle remains a cycle, and every cycle of the contracted permutation lifts to exactly one original cycle. Therefore
\[
\mathbb E[C\mid\text{prescribed arrows}]=H_{n-k}+c_0,
\]
where \(H_j=\sum_{r=1}^j1/r\), \(H_0=0\), and \(c_0\) is the number of cycles already closed by the prescribed arrows. This also holds when \(k=n\): no contracted chains remain.

Fix \(1\le a\le n-2\). Conditional on either monotone triple event, the three image values form a uniformly random three-element subset \(y_1<y_2<y_3\) of \(\{1,\ldots,n\}\). Every such subset has conditional probability \(\binom n3^{-1}\). By the contraction lemma, it suffices to count cycles made entirely by the three prescribed arrows, then subtract \(H_n\), noting the universal baseline \(H_{n-3}\).

**Increasing triple.** The prescribed arrows are \(a\mapsto y_1\), \(a+1\mapsto y_2\), \(a+2\mapsto y_3\). No nontrivial cycle can occur among these arrows, because their image order agrees with input order. Only fixed points contribute. Counting three-element image sets that force each respective fixed point gives
\[
\binom{n-a}{2}+a(n-a-1)+\binom{a+1}{2}
=\frac{n(n-1)}2.
\]
Consequently, the conditional mean number of already closed cycles is \(3/(n-2)\), independent of \(a\). As \(H_n-H_{n-3}=1/(n-2)+1/(n-1)+1/n\),
\[
\mathbb E[C\mid\pi(a)<\pi(a+1)<\pi(a+2)]-H_n
=\frac{3n-2}{n(n-1)(n-2)}.
\]

**Decreasing triple.** Now the images of \(a,a+1,a+2\) are \(y_3,y_2,y_1\). The numbers of possible image sets forcing an individual fixed point at one of these three positions are, respectively,
\[
\binom{a-1}{2},\quad a(n-a-1),\quad\binom{n-a-2}{2}.
\]
Their sum is \((n^2-5n+8)/2\). A prescribed two-cycle may use positions \(\{a,a+1\}\), \(\{a+1,a+2\}\), or \(\{a,a+2\}\); the respective numbers of image sets that force it are \(a-1\), \(n-a-2\), and \(1\), summing to \(n-2\). No directed three-cycle is compatible with the decreasing order of the images. Therefore the expected number of already closed cycles equals
\[
\frac{(n^2-5n+8)/2+n-2}{\binom n3}
=\frac{3(n^2-3n+4)}{n(n-1)(n-2)}.
\]
Subtracting \(H_n-H_{n-3}\) yields
\[
\mathbb E[C\mid\pi(a)>\pi(a+1)>\pi(a+2)]-H_n
=\frac{10-3n}{n(n-1)(n-2)}.
\]
Each monotone triple event has probability \(1/6\). For any indicator \(J\), \(\operatorname{Cov}(C,J)=\Pr(J=1)(\mathbb E[C\mid J=1]-\mathbb E[C])\); \(\mathbb E[C]=H_n\). This gives each local covariance and, by summing the \(n-2\) locations, the two boxed formulas. \(\square\)

## Verification
`verify_monotone.py` implements independent, exhaustive exact-fraction enumeration of every uniform permutation of sizes \(3\le n\le8\). It checks all local triple/cycle covariances against the two formulas (42 exact assertions) and exits successfully with `VERIFY_OK`. These finite enumerations test the formulas and boundary signs but are not the unrestricted proof; that is the preceding contraction-and-counting argument.

## Relationship to prior work
Godbole and Swickheimer [1] study counts of distinct consecutive patterns in uniform permutations, focusing on pattern-occurrence interactions and Poisson approximation. Butler [2] investigates Stirling/Euler/Mahonian statistic relationships; the cycle count is a Stirling statistic. Neither of the inspected parts establishes this specific covariance with increasing and decreasing **consecutive triples** or its position-independent conditional-cycle calculation. Earlier results on single inversion-indicator covariances give pairwise order information but do not by themselves determine a covariance with a conjunction of two neighboring comparisons.

## Limitations
No claim is made for arbitrary three-letter patterns, higher-length patterns, or the full joint law of \(C,U,V\). The cycle-contraction lemma is a conditional expectation statement, not an independence statement. The result's historical novelty is assessed only against the inspected material; an implicit earlier enumeration or more general joint generating function could cover the identity. No independent audit has been performed.

## References
[1] A. Godbole and H. Swickheimer, *An Alternative Proof for the Expected Number of Distinct Consecutive Patterns in a Random Permutation*, arXiv:2310.14071 (first public submission 2023-10-21; reviewed v4), https://arxiv.org/abs/2310.14071.

[2] F. Butler, *Stirling-Euler-Mahonian Triples of Permutation Statistics*, arXiv:2305.11273 (first public submission 2023-05-18), https://arxiv.org/abs/2305.11273.
