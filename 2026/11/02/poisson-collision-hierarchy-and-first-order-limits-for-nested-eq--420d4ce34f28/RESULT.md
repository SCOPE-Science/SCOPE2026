# Poisson collision hierarchy and first-order limits for nested equivalence blocks

## Finding
Fix an integer \(h\ge2\) and a real \(\lambda>0\). Consider a finite set partitioned by two equivalence relations \(E\subseteq F\), where there are \(m_n\) distinct \(F\)-classes, precisely \(s_n\) distinct \(E\)-classes in each \(F\)-class, and exactly \(r_n\) elements in each \(E\)-class. Assign an independent fair Boolean colour \(P\) to every element. Assume \(m_n,s_n,r_n\to\infty\), put \(u_n=s_n2^{-r_n}\), and require
\[
m_nu_n^h\longrightarrow\lambda,\qquad
u_nr_n^d\longrightarrow0\quad\text{for every fixed integer }d\ge0.
\]
Write \(X_{n,j}\), for \(0\le j\le h\), for the number of \(F\)-classes containing **exactly** \(j\) entirely non-\(P\) (blue) \(E\)-classes and \(h-j\) entirely \(P\) (red) \(E\)-classes, and no other monochromatic \(E\)-class. Then
\[
(X_{n,0},\ldots,X_{n,h})\ \Longrightarrow\
\bigotimes_{j=0}^h\operatorname{Poisson}\!\left(\frac{\lambda}{j!(h-j)!}\right).
\]
Every first-order sentence over \(\{E,F,P\}\) has a limiting probability. For each sentence that limit is the expectation of a finite Boolean function of the displayed independent Poisson variables. The \(\{E,P\}\)-reduct has a first-order zero-one law. Moreover,
\[
\Pr\left(\exists\text{ an }F\text{-class containing at least }h
\text{ entirely blue }E\text{-classes}\right)
\longrightarrow1-\exp(-\lambda/h!).
\]
For the explicit alternating sequence \(r_n=2n\), \(s_n=2^n\), \(m_n=c_n2^{hn}\) with \(c_n=1\) for even \(n\) and \(2\) for odd \(n\), the \(\{E,P\}\)-reduct still obeys a zero-one law while the full \(\{E,F,P\}\)-language fails to satisfy a first-order convergence law: the displayed sentence has subsequential limits \(1-e^{-1/h!}\) and \(1-e^{-2/h!}\).

## Assumptions and scope
All sequences are indexed by positive integers and all asymptotics are as \(n\to\infty\). The equivalences are reflexive and nested, and \(F\) has no connections between different outer classes. The classes are unlabelled for logical semantics but may be labelled for probability counting. The sampling space consists of all independent fair unary expansions of this fixed uniform \(E,F\)-structure. The condition \(u_nr_n^d\to0\) for every fixed \(d\) is essential to separate counts with an additional nearly monochromatic \(E\)-class. This is a result for regular two-level equivalences, not arbitrary finite equivalence systems or arbitrary colour biases.

## Proof
**Exact rare-profile count.** Write \(p_n=2^{-r_n}\). An \(E\)-class is entirely blue with probability \(p_n\), entirely red with probability \(p_n\), and neither with probability \(1-2p_n\). For nonnegative integers \(j,\ell\) with \(j+\ell\le s_n\), the exact probability that an \(F\)-class has exactly \(j\) entirely blue and \(\ell\) entirely red \(E\)-classes is
\[
Q_n(j,\ell)=\frac{s_n!}{j!\ell!(s_n-j-\ell)!}
 p_n^{j+\ell}(1-2p_n)^{s_n-j-\ell}.
\]
For fixed \(j+\ell=h\), the hypotheses imply \(s_n\to\infty\), \(s_np_n=u_n\to0\), and \(m_nQ_n(j,\ell)\to\lambda/(j!\ell!)\). Since the outer blocks are independent and the various \((j,\ell)\) profiles are mutually exclusive inside a block, their vector is multinomial with category probabilities \(Q_n\). Its joint factorial moments converge to those of independent Poisson variables with the asserted means. In particular, these limits give a joint distributional limit, not just convergence of expectations. The total probability of any \(F\)-class having more than \(h\) monochromatic \(E\)-classes is at most \(m_n(2u_n)^{h+1}/(h+1)!\) up to a harmless fixed factor, and tends to zero.

**Finite-rank normal form.** Fix a quantifier rank \(q\ge1\), and eventually assume \(r_n\ge2q\). For the \(q\)-round Ehrenfeucht–Fraïssé game, an inner \(E\)-class is described by its red and blue cardinalities truncated at \(q\). Its possible descriptions are: \(R_a\), exactly \(a\) red elements and at least \(q\) blue elements; \(B_a\), exactly \(a\) blue elements and at least \(q\) red elements, for \(0\le a<q\); and \(G\), at least \(q\) elements of each colour. The probabilities of the rare descriptions \(R_a\) and \(B_a\) are both \(2^{-r_n}\binom{r_n}{a}\). An outer \(F\)-class is described by the counts of these inner descriptions, again truncated at \(q\); the entire structure is described by its outer-class descriptions, truncated at \(q\). Matching these three levels of truncated counts supplies a duplicator strategy for \(q\) rounds: retain previously chosen outer classes, inner classes and elements, and use an unused matching class whenever the spoiler enters a new class. All atomic \(E,F,P\) statements and equality remain preserved. Thus every rank-\(q\) sentence depends only on this finite profile.

**Asymptotics of all finite-rank profiles.** Let \(\mathbf c=(c_{R_0},\ldots,c_{R_{q-1}},c_{B_0},\ldots,c_{B_{q-1}})\) be a *fixed exact vector* of rare inner-description counts inside one outer class, let \(t=\sum c\) and \(J=\sum_{a=0}^{q-1}a(c_{R_a}+c_{B_a})\). The expected number of outer classes with this exact vector and at least \(q\) generic inner classes is asymptotic to
\[
\frac{m_nu_n^t\prod_{a=0}^{q-1}\binom{r_n}{a}^{c_{R_a}+c_{B_a}}}
{\prod_{a=0}^{q-1}c_{R_a}!c_{B_a}!}.
\]
Here the multinomial factor uses \((s_n)_t\sim s_n^t\), while the probability of all remaining inner classes being generic tends to one because \(\sum_{a<q}2u_n\binom{r_n}{a}\to0\). The expression diverges for \(t<h\); it also diverges for \(t=h\) and \(J>0\); it converges to \(\lambda/(c_{R_0}!c_{B_0}!)\) for \(t=h\) and \(J=0\); and tends to zero for \(t>h\). The last assertion uses \(u_nr_n^d\to0\), not just \(u_n\to0\). More generally, the expected number of \(F\)-classes containing more than \(h\) rare inner descriptions is bounded by a constant multiple of \(m_n(u_nr_n^{q-1})^{h+1}\to0\). Likewise, the expected number of \(F\)-classes containing fewer than \(q\) generic inner classes tends to zero: with \(\epsilon_n=O(r_n^{q-1}2^{-r_n})\), the probability per outer class is bounded by a polynomial in \(s_n\) times \(\epsilon_n^{s_n-q}\), whereas \(\log m_n=O(r_n)\) and \(s_n\to\infty\).

Counts of each noncritical finite vector with diverging expectation concentrate: they are binomial sums over independent outer classes, so variance does not exceed expectation. Vectors with expectation tending to zero disappear by Markov's inequality. For the only critical vectors, \(t=h\), \(J=0\), the types consist precisely of \(j\) all-blue and \(h-j\) all-red inner classes; their counts have the joint Poisson law above. The probability of a critical outer class having any additional nonmonochromatic but \(q\)-rare inner class is \(o(1/m_n)\). A truncated outer-class \(q\)-type is a finite union of the exact rare vectors with total at most \(h\), up to an event of probability \(o(1)\). Consequently its total number among the \(m_n\) outer classes is asymptotically either zero, at least \(q\) with probability tending to one, or a fixed sum of the critical Poisson coordinates, truncated at \(q\). The distribution of the entire global rank-\(q\) profile therefore converges and depends only on the finite Poisson vector. Applying the Ehrenfeucht–Fraïssé criterion proves the asserted convergence for every first-order sentence and the finite Boolean representation.

**Reduct and explicit oscillation.** In the \(\{E,P\}\)-reduct there are \(m_ns_n\) independent inner classes. Every one of the \(2q\) rare inner types has expected multiplicity asymptotic to \(m_nu_n\binom{r_n}{a}\to\infty\), because \(h\ge2\) and \(m_nu_n^h\to\lambda\). The generic type is also abundant. All truncated class-type multiplicities therefore tend to \(q\) in probability, giving a zero-one law by the same back-and-forth argument. The existence of an outer class containing \(h\) distinct all-blue inner classes is first-order expressible: quantify their distinct \(E\)-classes inside one \(F\)-class, and require every element in each \(E\)-class to be non-\(P\). The expected number of outer classes with precisely \(h\) all-blue inner classes tends to \(\lambda/h!\); the possibility of more tends to zero. The stated limit follows. For the alternating sequence, \(u_n=2^{-n}\) and \(m_nu_n^h=c_n\in\{1,2\}\). The same probability argument, applied on the even and odd subsequences, gives the two distinct limits, while the inner-reduct abundance argument holds on the whole sequence.

## Verification
The standalone standard-library script `checker.py` independently enumerates every fair two-colouring for four small nested structures (\(270592\) total assignments), and compares the exact joint rare-profile distribution against a separate rational multinomial computation. It also checks seven mixed factorial-moment instances and sixteen finite threshold probabilities against their predicted limits, reporting `ALL_CHECKS_OK`. These are bounded checks only; all asymptotic and first-order assertions follow from the preceding proof.

## Relationship to prior work
Koponen's *A characterization of the finite model property for \(\omega\)-categorical theories* (arXiv:2610.16163v1; first publicly posted 2026-10-12), especially Example 2.12 and Remark 2.15, motivates the sensitivity of random expansion convergence to the base structures. Its actual claims address finite-model properties, partial closures, and conditions needed for convergence, not this exact regular two-level rare-profile theorem. Koponen–Tousinejad's *Random expansions of trees with bounded height* (arXiv:2410.11775v2), particularly Examples 6.1–6.2, exhibits nonconvergence phenomena with imbalanced branching; its full-text examples do not establish the present critical collision mechanism on regular nested classes. Fiuk's *The Guarded Fragment with Nested Equivalences* (arXiv:2605.15072v1) studies logical decidability and satisfiability complexity for nested equivalences, not probabilistic first-order convergence. A prior one-level coloured-equivalence intensity criterion concerns only \(\{E,P\}\) and does not distinguish multiple inner classes lying in the same outer class. The multinomial and Poisson approximations are standard tools; the joint logical classification and explicit reduct-separation in this regime constitute the claim.

## Limitations
The result assumes uniform outer and inner class sizes, independent unbiased colours, and the stated superpolynomial separation of the rare intensity. It does not classify all possible growth regimes, arbitrary nested-equivalence systems, or general probability biases. The Boolean function describing the limit is existentially specified through finite-rank types; no claimed general polynomial-time compilation procedure is supplied. An equivalent asymptotic logical limit-law theorem might exist under an older hierarchical-occupancy formulation; independent historical-priority verification remains outstanding. No independent audit has been performed.

## References
1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (2026-10-12), https://arxiv.org/html/2610.16163v1.
2. V. Koponen and Y. Tousinejad, *Random expansions of trees with bounded height*, arXiv:2410.11775v2, https://arxiv.org/html/2410.11775v2.
3. O. Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072v1, https://arxiv.org/abs/2605.15072.
