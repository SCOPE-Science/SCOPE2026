# Sharp active–passive tomography of finite reflexive non-contingency frames

## Finding

A single non-contingency observation reports which worlds **know whether** an atomic proposition holds. For a fixed labelled frame with a reflexive accessibility relation, varying only the atomic valuation is sufficient to recover the entire relation. The exact minimum number of valuations differs radically between chosen and randomly generated probes.

**Theorem.** Let \(n\ge1\) and \(W=[n]\). For any reflexive \(R\subseteq W\times W\), put \(R(w)=\{v:wRv\}\). A query is a subset \(X\subseteq W\), interpreted as the truth set of one atomic proposition \(p\). Its answer is the fully labelled vector \(D_R(X)\subseteq W\), where
\[
D_R(X)=\{w\in W:R(w)\subseteq X\ \text{or}\ R(w)\cap X=\varnothing\}.
\]
This is exactly the world set satisfying \(\Delta p=\Box p\lor\Box\neg p\). A query scheme *universally identifies* the unknown frame if it reconstructs the exact relation \(R\) for every reflexive relation on the labelled carrier, with no error; adaptive schemes may choose the next query from previous answers.

The least worst-case query count of either deterministic adaptive or fixed nonadaptive schemes is
\[
q_n=\begin{cases}0,&n=1,\\1,&n=2,\\n,&n\ge3.\end{cases}
\]
For \(n\ge3\), a fixed query family \(\mathcal Q\subseteq\mathcal P(W)\) is universally identifying **if and only if**
\[
\forall v\in W:\quad\{v\}\in\mathcal Q\quad\text{or}\quad W\setminus\{v\}\in\mathcal Q.
\]
In particular, \(n\) fixed singleton queries are optimal even against adaptive strategies.

For \(n\ge3\) and \(m\ge0\), suppose \(X_1,\ldots,X_m\) are independent uniformly sampled subsets of \(W\). The exact probability that this nonadaptive query multiset universally identifies every reflexive relation is
\[
P_{n,m}=\sum_{j=0}^{n}(-1)^j\binom nj\bigl(1-j2^{1-n}\bigr)^m.
\]
For any fixed real \(t\), along \(m_n=\lfloor 2^{n-1}(\log n+t)\rfloor\) (and sufficiently large \(n\) to make \(m_n\ge0\)),
\[
\lim_{n\to\infty}P_{n,m_n}=\exp(-e^{-t}).
\]
Thus the random passive test budget is of order \(2^{n-1}\log n\), versus exactly \(n\) deliberately selected probes.

## Assumptions and scope

All worlds are individually labelled and their identities are known. The observer knows \(n\) and reflexivity but not the off-diagonal edges. A *single query* chooses the valuation of one atom on all worlds and returns the entire labelled truth set of **one un-nested** formula \(\Delta p\), not just one world's answer. Within the scheme, valuations can be changed and observed without noise. No nested modalities, additional propositional variables, Boolean combinations of observations as new queries, or unlabelled-frame identification are allowed. Only deterministic zero-error adaptive schemes are considered in the worst-case result; the random-query law is for independent uniform valuations with universal (all-frames) identification.

The bound concerns a worst-case guarantee over every reflexive relation, not a probability distribution on the unknown relation. The random event is the success of a *single sampled family* for **all** reflexive relations; it is not a Bayesian average over random frames.

## Proof

**1. Single-row information.** Given any successor set \(S\subseteq W\), let \(f_S(X)=1\) exactly when \(S\subseteq X\) or \(S\cap X=\varnothing\). When \(|S|\le1\), \(f_S\) is identically one. When \(|S|\ge2\), for any \(v\in W\),
\[
f_S(\{v\})=0\quad\Longleftrightarrow\quad v\in S.
\]
Indeed, in that case a singleton splits \(S\) into two nonempty truth classes precisely when its element belongs to \(S\). Consequently, distinct successor sets of size at least two have distinct one-step observation functions, and every empty or singleton successor set has the same constant observation function. In a reflexive frame, the singleton ambiguity is harmless because a row with one successor must be \(\{w\}\) at world \(w\).

**2. Upper bound and explicit reconstruction.** Fix distinct worlds \(w\ne v\). Reflexivity ensures \(w\in R(w)\), so querying \(X=\{v\}\) gives
\[
w\notin D_R(\{v\})\quad\Longleftrightarrow\quad wRv.
\]
The implication holds even when \(R(w)=\{w\}\). Therefore the queries \(\{v\}\), one per \(v\in W\), reconstruct every off-diagonal entry; all diagonal entries are known to equal one. For \(n=1\), there is only one reflexive relation, so no query is necessary. For \(n=2\), \(\{v\}\) and its complement are the same unordered two-colour partition and produce identical truth vectors; a single such query recovers both off-diagonal edges. Since there is more than one reflexive relation on two worlds, zero queries cannot suffice.

**3. Necessity of every singleton partition.** Assume \(n\ge3\). Fix \(v\in W\), and choose \(w_v\ne v\). Let \(U=W\times W\) be the universal relation, and let \(U^{(v)}=U\setminus\{(w_v,v)\}\); both are reflexive. Their answers differ only possibly at world \(w_v\), where the successor sets are respectively \(W\) and \(W\setminus\{v\}\). The latter has at least two elements. For any \(X\subseteq W\), the row answers differ **exactly when** \(X=\{v\}\) or \(X=W\setminus\{v\}\): only then is the altered successor set monochromatic but the universal successor set split. Therefore any fixed universally identifying query family must contain a representative from every complementary singleton pair. For \(n\ge3\), these are \(n\) distinct pairs, proving the necessity and sufficiency criterion and the \(n\)-query nonadaptive optimum.

For a deterministic adaptive protocol, trace its execution on the universal relation \(U\). Until it asks one of the two singleton-partition queries corresponding to \(v\), its answers on \(U^{(v)}\) are identical to those on \(U\). If the protocol terminates on \(U\) without asking that query, the complete transcript and output are identical on both frames, contradicting zero-error reconstruction. Hence the execution on \(U\) must contain a query from each of the \(n\) distinct pairs. Adaptivity cannot reduce the worst-case bound.

**4. Exact passive success probability.** For \(n\ge3\), each required pair \(\{v\},W\setminus\{v\}\) comprises two of the \(2^n\) possible valuations; the pairs for different \(v\) are disjoint. Thus each uniformly random query hits any given required pair with probability \(p_n=2^{1-n}\). The event of universal identification is exactly that all \(n\) designated pairs have been seen. By inclusion–exclusion over absent pairs,
\[
\Pr(\text{all }n\text{ pairs seen})=\sum_{j=0}^n(-1)^j\binom nj(1-jp_n)^m,
\]
where \(jp_n\le1\) for \(n\ge3\), so every term is well defined.

Set \(m=m_n\), and let \(Z_n\) count required pairs never seen. For each fixed positive integer \(r\),
\[
\mathbb E[(Z_n)_{\underline r}]=(n)_{\underline r}(1-rp_n)^{m_n}\longrightarrow e^{-rt}.
\]
Indeed \(m_np_n=\log n+t+o(1)\), \(m_np_n^2=o(1)\), and \((n)_{\underline r}\sim n^r\). The limiting factorial moments identify a Poisson distribution with mean \(e^{-t}\); hence \(Z_n\) converges in distribution to \(\operatorname{Poisson}(e^{-t})\) and \(\Pr(Z_n=0)\to e^{-e^{-t}}\). The theorem follows.

## Verification

The standalone, dependency-free `checker.py` directly enumerates all directed relations on carriers of sizes one through three and all reflexive relations on carriers of sizes one through four. It derives the distinct arbitrary-row operator counts \(1,4,125\), tests minimal nonadaptive query families (including exhaustive four-world families), verifies every fixed-family characterization for three and four worlds, and checks the universal-relation deletion adversaries for sizes three through seven. It additionally reconstructs random five-world reflexive relations and exhaustively compares the exact inclusion–exclusion formula to explicit random-valuation sequences in small cases.

Run `python3 checker.py`; the final expected marker is `ALL_CHECKS_OK`. All finite tests executed successfully. The statements for unrestricted \(n\) and the limiting probability are established by the preceding proof, not inferred from finite enumeration.

## Relationship to prior work

Non-contingency and knowing-whether Kripke semantics are standard. The recent labelled-sequent analysis of Wang and Zenger (2026) provides a motivating modal setting and defines the reflexive frame class. Fan, Wang and van Ditmarsch (2013/2015), especially their section on reflexive models, establish expressive connections between knowing-whether and ordinary knowledge operators; Humberstone and Zolin studied the non-contingency semantics and definability. None of those established semantic or proof-theoretic results is here claimed as novel. The specific new question is the minimal number of **raw atomic-valuation truth-vector probes** needed for uniform labelled-frame inversion, including the adaptive lower bound and the independent-random-probe critical window.

The quotient of empty and singleton successor sets under one-step non-contingency is a direct observation from these established semantics. For additional context, all relations on a labelled \(n\)-world carrier realize exactly \((2^n-n)^n\) distinct one-step non-contingency operators, since per row there is one indistinguishable small-successor type and \(2^n-n-1\) larger distinguishable types. This supporting count is not asserted as an independent historical-priority discovery. The quantitative identification theorem is assessed separately from the familiar coupon-collector calculation.

## Limitations

There is no claim about query complexity when one can interrogate the full propositional or modal language, when outputs are restricted to a single world, when only a fixed initial valuation is available, when noise occurs, or when worlds are unlabelled. The exact random success event is *universal identification of every reflexive relation* and may differ from success on a randomly sampled relation. Although primary sources and relevant literature were examined, equivalent older work under knowledge-acquisition or active-learning terminology remains a historical-priority risk; an independent literature or proof audit has not been performed.

## References

1. Yunsong Wang and Lukas Zenger, *Proof Theory for Non-Contingency Logic* (first posted 2026-09-30), arXiv:2609.38975, https://arxiv.org/abs/2609.38975.
2. Jie Fan, Yanjing Wang and Hans van Ditmarsch, *Knowing Whether* (2013), arXiv:1312.0144, https://arxiv.org/abs/1312.0144; journal version *Contingency and Knowing Whether* (2015), DOI 10.1017/S1755020314000343.
3. Lloyd Humberstone, *The Modal Logic of Agreement and Noncontingency*, DOI 10.1305/ndjfl/1071509431.
4. Evgeny Zolin, *Completeness and Definability in Logic of Noncontingency*, DOI 10.1305/ndjfl/1012429717.
