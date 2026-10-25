# Sharp entropy-scale deviations of reflexive worlds in uniform finite KD45 frames

## Finding

Fix an integer \(n\ge1\) and choose uniformly among all labelled \(n\)-world Kripke relations satisfying seriality, transitivity and right-Euclideanness (the \(\mathsf{KD45}\) frame conditions). Let \(M_n\) count the reflexive worlds. For each fixed \(\alpha\in(0,1)\) and any integer sequence \(m_n\) with \(m_n/n\to\alpha\),
\[
 \lim_{n\to\infty}\frac1n\log\Pr(M_n=m_n)
 =-I(\alpha),\qquad
 I(\alpha)=\alpha\log(2\alpha)+(1-\alpha)\log(2(1-\alpha)).
\]
All logarithms are natural. Consequently \(M_n/n\) tends in probability to \(1/2\), with the exact exponential tail rate: for every fixed \(0<\delta<1/2\),
\[
 \lim_{n\to\infty}\frac1n\log\Pr\bigl(|M_n/n-1/2|\ge\delta\bigr)
 =-I(1/2+\delta).
\]
This is an entropy-scale local large-deviation law, **not** a Gaussian local limit theorem and not an assertion of relative-error equivalence to the binomial law.

The exact finite distribution and its bivariate exponential generating function were already recorded combinatorially (not new claims):
\[
 T(n,m)=\binom nm\sum_{k=1}^{m}\left\{\begin{matrix}m\\k\end{matrix}\right\}k^{n-m},\quad
 \Pr(M_n=m)=\frac{T(n,m)}{\sum_{j=1}^nT(n,j)},
\]
\[
 \sum_{n\ge0}\sum_{m=0}^nT(n,m)y^m\frac{z^n}{n!}
 =\exp\bigl(e^{(1+y)z}-e^z\bigr).
\]
Here the curly bracket is the Stirling number of the second kind, \(1\le m\le n\) for positive \(n\), and \(T(0,0)=1\). The newly assessed assertion is the complete exponential rate for the reflexive-world statistic.

## Assumptions and scope

A frame is a finite nonempty labelled set \(W\), together with a relation \(R\subseteq W\times W\). Seriality means \(\forall u\,\exists v\,uRv\). Transitivity means \(uRv\land vRt\Rightarrow uRt\). Right-Euclideanness means \(uRv\land uRt\Rightarrow vRt\). There are no additional accessibility, valuation or connectedness restrictions. The sampling measure assigns equal probability to each admissible relation, *not* to each isomorphism class or to each partition. A world is reflexive when \(uRu\).

## Proof

**1. Canonical frame decomposition.** Write \(S(u)=\{v:uRv\}\). Seriality makes every \(S(u)\) nonempty. If \(uRv\), transitivity implies \(S(v)\subseteq S(u)\), while right-Euclideanness implies \(S(u)\subseteq S(v)\). Hence \(S(v)=S(u)\). Distinct successor sets are disjoint: if \(x\in S(u)\cap S(t)\), equality along both edges forces \(S(u)=S(x)=S(t)\). For each distinct successor set \(C\), the fiber \(B_C=\{u:S(u)=C\}\) is a block containing \(C\). The \(B_C\) form a partition and \(C\) is precisely the set of reflexive vertices of its block. Conversely, any set partition with a designated nonempty subset \(C_B\) of each block, with \(S(u)=C_B\) for all \(u\in B\), gives exactly one serial, transitive, right-Euclidean relation. Thus the distribution of \(M_n\) is the distribution of the number of marked elements in a uniformly chosen partition with one nonempty marked subset per block. The preceding exact formulas follow, agreeing with the established table OEIS A143396 and its row sums A143405.

**2. A coupling with unbiased independent marks.** First choose a uniform ordinary set partition \(\Pi_n\) of \(W\) and, independently, mark each world with probability \(1/2\). Let \(A_n\) be the event that every block has at least one mark, and write \(Z_n\) for the number of marks before conditioning. Since every pair consisting of a partition and a marking has the same unconditioned probability, conditioning on \(A_n\) produces exactly the uniform marked-partition model, so
\[
 \Pr(M_n=m)=\binom nm 2^{-n}\frac{\Pr(A_n\mid Z_n=m)}{\Pr(A_n)}.
\]

**3. The random ordinary partition has sublinear block count.** Denote by \(K_n\) the number of blocks of \(\Pi_n\), and let \(B_n\) be the Bell number. We prove \(\kappa_n=\mathbb E K_n=o(n)\) without assuming a delicate Bell asymptotic. For \(q=\lfloor n/\log n\rfloor\), a uniformly random function from the \(n\)-set onto \(q\) labelled boxes fails surjectivity with probability at most \(q\exp(-n/q)=O(1/\log n)\). Dividing the number of surjections by \(q!\) yields
\[
 \log B_n\ge(n-q)\log q+o(1)
 =n\log n-n\log\log n-O(n).
\]
For fixed \(\varepsilon>0\), the number of partitions having at least \(\varepsilon n\) blocks is at most
\[
 \sum_{k\ge\lceil\varepsilon n\rceil}\frac{k^n}{k!}
 \le\frac{n^{n+1}}{\lceil\varepsilon n\rceil!}.
\]
Comparing logarithms gives \(\Pr(K_n\ge\varepsilon n)\to0\); indeed the log ratio is at most \(-\varepsilon n\log n+O(n\log\log n)\). Since \(0\le K_n/n\le1\), the expectation ratio tends to zero. Thus \(\kappa_n=o(n)\).

**4. Conditioning costs no exponential factor in the interior.** For any fixed partition with \(K_n=k\), independent marking has probability \(\prod_{B\in\Pi_n}(1-2^{-|B|})\ge2^{-k}\) of marking every block. Jensen's inequality gives
\[
 1\ge\Pr(A_n)\ge\mathbb E[2^{-K_n}]
 \ge2^{-\kappa_n}=\exp(-o(n)).
\]
Now fix \(m_n/n\to\alpha\in(0,1)\). By Markov's inequality, \(\Pr(K_n\le2\kappa_n+1)\ge1/2\). Select one representative from each block. Conditional on \(Z_n=m_n\), the selected marks form a uniform \(m_n\)-subset. The probability it contains those representatives is \((m_n)_{K_n}/(n)_{K_n}\). For all sufficiently large \(n\), on \(K_n\le2\kappa_n+1\), this is at least \((\alpha/2)^{K_n}\). Therefore
\[
 1\ge\Pr(A_n\mid Z_n=m_n)
 \ge\tfrac12(\alpha/2)^{2\kappa_n+1}=\exp(-o(n)).
\]
Substituting into the displayed conditional probability yields
\[
 \frac1n\log\Pr(M_n=m_n)
 =\frac1n\log\left(\binom{n}{m_n}2^{-n}\right)+o(1)
 \longrightarrow-I(\alpha)
\]
by Stirling's formula. The same bounds are uniform when the ratios stay in any fixed compact subset of \((0,1)\).

**5. Sharp tails.** The upper bound \(\Pr(A_n)\ge\exp(-o(n))\) implies
\[
 \Pr(|M_n/n-1/2|\ge\delta)
 \le\exp(o(n))\Pr(|Z_n/n-1/2|\ge\delta).
\]
The classical binomial Chernoff bound gives the upper logarithmic rate \(-I(1/2+\delta)\). For the reverse rate choose the single admissible integer \(m_n=\lceil n(1/2+\delta)\rceil\) and apply step 4; symmetry of \(I\) supplies the displayed two-sided tail limit. This also proves convergence in probability.

## Verification

The standalone standard-library program `verify_kd45_core_ldp.py` enumerates *all serial relations* on up to four labelled worlds and checks transitivity and right-Euclideanness against the marked-partition formula. The observed reflexive-core profiles are \((1)\), \((2,2)\), \((3,9,5)\), and \((4,30,40,15)\) for one through four worlds. It also independently verifies the Stirling formula against the known decorated-partition recurrence for sizes five through ten. Expected final signal: `KD45_REFLEXIVE_CORE_FORMULAS_OK`. These finite checks do not establish the large-deviation limit; steps 2–5 above are its proof.

## Relationship to prior work

The labelled decorated-partition enumeration is *already known*: OEIS A143396 gives precisely the \(T(n,m)\) triangle and its bivariate generating function (recorded in 2008); OEIS A143405 gives its row sums and states the related transitive Euclidean relational interpretation in a 2026 contribution. Kotěšovec (2022) derived precise asymptotics for the total A143405 count using analytic generating-function methods. The present result does not claim novelty for the decompositions, enumeration, or totals; it establishes the exponential law for the number of reflexive worlds under uniform \(\mathsf{KD45}\) sampling. Nishimura (2026) supplies recent broader motivation concerning the representation of weak modal semantics by relational frames; its theorems concern representation rather than this probability law.

## Limitations

The asymptotic is only at logarithmic \(n\)-scale. It does not give a central limit theorem, a multiplicative local limit, fine finite-size error bounds, or a rate at \(\alpha=0\). The \(\alpha=0\) event is impossible by seriality; \(\alpha=1\) is not included in the stated interior local-deviation theorem. The result concerns uniform labelled frames and cannot be directly transferred to uniform isomorphism classes. A general historical large-deviation theorem for conditioned combinatorial assemblies could imply the rate; no claim of exhaustive priority is made. Independent mathematical review remains outstanding.

## References

1. OEIS A143396, *Triangle counting rooted forests by the number of labels used for root nodes*; includes exact \(T(n,m)\) and bivariate generating function (2008): https://oeis.org/A143396 .
2. OEIS A143405, *Number of labelled rooted forests of height at most one with nonempty root labels*; includes the September 5, 2026, relational interpretation: https://oeis.org/A143405 .
3. V. Kotěšovec, *Asymptotics for a certain group of exponential generating functions* (2022), arXiv:2207.10568, https://arxiv.org/abs/2207.10568 .
4. Y. Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations* (October 1, 2026), arXiv:2610.01433, https://arxiv.org/abs/2610.01433 .
