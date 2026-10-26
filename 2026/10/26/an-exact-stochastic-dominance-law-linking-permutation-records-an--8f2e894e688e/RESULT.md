# An exact stochastic dominance law linking permutation records and cycles

## Finding
For a uniformly random permutation, conditioning an upper left-to-right record at a specified position increases the *ordinary disjoint-cycle count of that same permutation* in first-order stochastic order. The entire distributional difference is one explicitly scaled first difference of the law of two independent smaller permutation cycle counts. This yields an exact positive covariance at every noninitial marked position, despite vanishing asymptotic correlation of total cycle and record counts.

For integers \(n\ge1\), \(1\le i\le n\), define
\[
G_m(z)=\frac{z(z+1)\cdots(z+m-1)}{m!}\quad(m\ge1),\qquad G_0(z)=1,\qquad
\varepsilon_{n,i}=\frac{i-1}{i\binom ni}.
\]
Then, with \(C_n\) the number of cycles and \(R_{n,i}\) the upper-record indicator,
\[
\boxed{\mathbb E[z^{C_n}\mid R_{n,i}=1]
=G_n(z)+\varepsilon_{n,i}(z-1)G_{i-1}(z)G_{n-i}(z).}
\]
Let \(T_{n,i}=K_{i-1}+K'_{n-i}\), where independent \(K_m\) have the number-of-cycles law for a uniform permutation of \(m\) objects, including \(K_0=0\). For **each integer \(k\)**,
\[
\boxed{\mathbb P(C_n\ge k\mid R_{n,i}=1)-\mathbb P(C_n\ge k)
=\varepsilon_{n,i}\mathbb P(T_{n,i}=k-1).}
\]
Thus the conditional distribution strictly dominates for every \(i\ge2\) (some tail gap is positive), and coincides for \(i=1\). In addition,
\[
\boxed{\operatorname{Cov}(C_n,R_{n,i})
=\frac{i-1}{i^2\binom ni}.}
\]
Writing \(R_n=\sum_{i=1}^nR_{n,i}\),
\[
\operatorname{Cov}(C_n,R_n)=\sum_{i=2}^{n}\frac{i-1}{i^2\binom ni}
=\frac1n+O(n^{-2}),\qquad
\operatorname{Corr}(C_n,R_n)\sim\frac1{n\log n}.
\]

## Assumptions and scope
The permutation \(\pi\) is uniform among all \(n!\) bijections of \(\{1,\ldots,n\}\), written in one-row notation \((\pi(1),\ldots,\pi(n))\). Its ordinary cycle count \(C_n\) is the number of cycles in the disjoint-cycle decomposition of **this same map**. For each \(i\), \(R_{n,i}=1\) exactly when \(\pi(i)>\pi(j)\) for all \(j<i\). In particular \(R_{n,1}=1\) surely and \(\mathbb P(R_{n,i}=1)=1/i\). A size-zero uniform permutation has cycle count zero by convention. Polynomial generating-function equalities hold formally in \(z\), so also at each complex or real \(z\); all stochastic statements use the real, integer-valued cycle count. There is no large-size restriction on \(n\).

## Proof
Use the standard cycle-insertion construction. From a uniform \(\pi_{n-1}\), choose \(J_n\) uniformly from \(\{1,\ldots,n\}\), independently. If \(J_n<n\), replace the outgoing arrow from \(J_n\) by an arrow to \(n\), and make the outgoing arrow from \(n\) point to the former image of \(J_n\). If \(J_n=n\), make \(n\) a singleton cycle. Every permutation on \(n\) labels has exactly one inverse insertion, so this yields a uniform permutation. The number of cycles increases by one precisely in the singleton case.

For \(G_m(z)=\mathbb E[z^{C_m}]\), insertion gives \(G_0(z)=1\) and \(G_n(z)=(n-1+z)G_{n-1}(z)/n\), establishing the formula above. Define the joint generating function
\[
F_{n,i}(z)=\mathbb E[z^{C_n}R_{n,i}].
\]
When \(n=i\), a record at the final position occurs precisely when the insertion creates singleton \(n\), so
\[
F_{i,i}(z)=\frac{z}{i}G_{i-1}(z).
\]
When \(n>i\), inserting the largest new symbol at position \(J_n=i\) forces a record at \(i\), choosing \(J_n<i\) destroys that record, and choosing \(J_n>i\) preserves the old record status. The final case \(J_n=n\) adds a new cycle. Hence
\[
F_{n,i}(z)=\frac{G_{n-1}(z)}n+\frac{n-i-1+z}{n}F_{n-1,i}(z).
\]
Subtract the product of the marginal record probability \(1/i\) and the cycle polynomial: define \(H_{n,i}(z)=F_{n,i}(z)-G_n(z)/i\). Direct substitution gives
\[
H_{i,i}(z)=\frac{i-1}{i^2}(z-1)G_{i-1}(z),\qquad
H_{n,i}(z)=\frac{n-i-1+z}{n}H_{n-1,i}(z)\quad(n>i).
\]
Multiplying this recursion and using
\[
\prod_{m=i+1}^{n}\frac{m-i-1+z}{m}=
\frac{G_{n-i}(z)}{\binom ni}
\]
yields
\[
H_{n,i}(z)=\frac{i-1}{i^2\binom ni}(z-1)G_{i-1}(z)G_{n-i}(z).
\]
Since conditioning on the record multiplies \(F_{n,i}\) by \(i\), the conditional generating-function identity follows.

If \(p(t)=\mathbb P(T_{n,i}=t)\), the coefficient of \(z^j\) in the conditional-minus-unconditional generating polynomial is \(\varepsilon_{n,i}(p(j-1)-p(j))\), with \(p(t)=0\) outside its support. Summing coefficients at \(j\ge k\) telescopes to \(\varepsilon_{n,i}p(k-1)\). For \(i\ge2\), \(\varepsilon_{n,i}>0\) and \(T_{n,i}\) has nonempty support, proving strict stochastic dominance. For \(i=1\) the coefficient is zero. The conditional-minus-unconditional mean is the derivative of the polynomial difference at \(z=1\), equal to \(\varepsilon_{n,i}\). Multiplication by \(\mathbb P(R_{n,i}=1)=1/i\) gives the exact marked covariance.

Summing covariances over the record positions gives the displayed total covariance. Its \(i=n\) term is \((n-1)/n^2=1/n+O(n^{-2})\). For \(2\le i\le n-1\), each term is bounded by \(1/\binom ni\). The two boundary terms with \(i=2,n-1\) contribute \(O(n^{-2})\), and all remaining \(n-4\) terms (where present) are at most \(1/\binom n3\), contributing \(O(n^{-2})\). Finally the cycle count has the distribution of a sum of independent Bernoulli variables with parameters \(1/j\) for \(1\le j\le n\), by the insertion construction. The upper-record indicators likewise are independent Bernoulli variables with the same parameters, by exchangeability of the independent uniform ranks. Consequently
\[
\operatorname{Var}(C_n)=\operatorname{Var}(R_n)
=\sum_{j=1}^n\left(\frac1j-\frac1{j^2}\right)=\log n+O(1),
\]
which, together with the total covariance, proves the correlation asymptotic.

## Verification
The accompanying standalone `verify.py` uses exact integer and rational arithmetic to enumerate all permutations through \(n=8\), independently computing their ordinary cycle counts and marked upper-record indicators. It compares every probability-generating-function coefficient and every tail gap at every position. It also checks the exact conditional generating-function recurrence for all \(n\le35\). The verification script reports `VERIFY_OK` on successful completion. Enumeration is not a proof for unbounded \(n\); the unrestricted proof is the insertion recurrence above.

## Relationship to prior work
The cycle-insertion/Feller construction, marginal Stirling cycle polynomial, and record-to-cycle transformations are classical; see Najnudel and Pitman and Gnedin. In particular, a Foata transform equates **the number of records of one permutation** with **the number of cycles of a transformed permutation**. That marginal identity does *not* determine their joint dependence on the **same original permutation**. Jin's Euler–Stirling generating functions jointly enumerate several descent and left/right-record statistics but not the ordinary cycle count of the same permutation. These papers provide the natural setting and comparisons, rather than an asserted origin for the present exact marked conditional law. Published mathematical-result searches concerning inversion/cycle covariance and fixed-point/descents did not supply this mixed record/cycle identity; that absence by itself is not a proof of novelty.

## Limitations
The theorem concerns uniform permutations, not a general Ewens parameter or arbitrary permutation measures. First-order stochastic dominance is conditional on one specified upper-record event, and does not assert independence or positive association of the full record-indicator vector with every increasing function of cycle structure. The asymptotic statement concerns the total record count, not an arbitrary subset. No historical uniqueness or independent audit is claimed; an older equivalent identity could exist under another formulation. Finite checks only supplement the analytical proof.

## References
1. J. Najnudel and J. Pitman, *Feller coupling of cycles and Poisson spacings*, arXiv:1907.09587 (first posted 2019-07-22; subsequently revised as *Feller coupling of cycles of permutations and Poisson spacings in inhomogeneous Bernoulli trials*). https://arxiv.org/abs/1907.09587 ; https://arxiv.org/html/1907.09587v2
2. A. Gnedin, *Coherent random permutations with record statistics*, Discrete Mathematics & Theoretical Computer Science (2007), https://dmtcs.episciences.org/en/articles/3551/download .
3. E. Y. Jin, *Symmetric generating functions and Euler-Stirling statistics on permutations*, arXiv:2210.08789 (2022), https://arxiv.org/abs/2210.08789 .
