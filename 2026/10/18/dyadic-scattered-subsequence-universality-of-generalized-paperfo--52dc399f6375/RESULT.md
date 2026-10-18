# Dyadic scattered-subsequence universality of generalized paperfolding words

## Finding
Let \(d=(d_0,d_1,\ldots)\) be any infinite binary instruction sequence and let \(P_d=p_0p_1\cdots\) be the associated binary generalized paperfolding word, as defined below. Write \(W_k=p_0\cdots p_{2^k-1}\). For a finite binary word \(w\), let \(\iota(w)\) denote the greatest \(h\ge0\) such that **every** binary word of length \(h\) is a scattered subsequence of \(w\).

**Theorem.** For every binary instruction sequence \(d\) and every integer \(k\ge3\),
\[
\iota(W_k)=3\cdot 2^{k-3}-\mathbf 1_{\{d_0=d_1\ne d_k\}}.
\]
In particular, \(3\cdot2^{k-3}-1\le\iota(W_k)\le3\cdot2^{k-3}\), and for every fixed instruction sequence,
\[
\lim_{k\to\infty}\frac{\iota(W_k)}{2^k}=\frac38.
\]
The possible one-unit defect is exactly determined by the first two instructions and the instruction at depth \(k\), independently of all intervening instructions. Both values occur. For fixed \(k\), precisely one-quarter of the \(2^{k+1}\) instruction prefixes \((d_0,\ldots,d_k)\) have the lower value.

## Assumptions and scope
Indices of symbols of \(P_d\) start at zero and indices of folding instructions also start at zero. For \(t\ge1\), uniquely write \(t=2^e(2j+1)\) with integers \(e,j\ge0\). Then
\[
p_{t-1}=d_e\mathbin\oplus(j\bmod2),
\]
where \(\oplus\) denotes addition modulo two. This is the standard generalized paperfolding construction, up to interchanging the two binary letter labels. Equivalently, if \(F_0\) is the empty word, define recursively \(F_{i+1}=F_i\,d_i\,\overline{F_i^{\mathrm R}}\) (where the bar interchanges bits and the superscript \(\mathrm R\) reverses order); then \(W_k=F_kd_k\). These definitions agree by induction.

A word \(u=u_1\cdots u_h\) is a scattered subsequence of \(w=w_1\cdots w_n\) if there are indices \(1\le i_1<\cdots<i_h\le n\) with \(u_j=w_{i_j}\) for every \(j\). This theorem concerns binary-alphabet subsequence universality, **not** contiguous factor complexity, binomial equivalence, cyclic universality, or arbitrary nondyadic prefix lengths. No assumption of periodicity or computability of \(d\) is made.

## Proof
**1. Greedy arches compute universality.** Scan a binary word from left to right, maintaining either an empty pending-letter state \(\bot\) or a single bit \(0\) or \(1\). With state \(\bot\), record the newly read bit. With a pending bit \(z\), retain state \(z\) upon reading \(z\), but upon reading \(1-z\), increment an arch counter and reset the state to \(\bot\). The counter is \(\iota(w)\).

For the lower bound, each completed arch contains both letters, so an arbitrary binary sequence of as many letters as arches can be embedded by selecting one desired letter per arch. For the upper bound, choose as a desired subsequence the last letters of successive completed arches, followed by a letter absent from the unfinished final arch (if the final arch is empty, choose either letter). The greedy earliest embedding of these selected last letters ends exactly at the corresponding arch boundaries; no occurrence of the final chosen letter remains. The resulting word of length one more than the arch count is absent. Thus the counter is exact.

**2. Universal eight-symbol block form.** Put \(a=d_0\), \(b=d_1\), and let \(\bar a=1-a\), \(\bar b=1-b\). From the valuation definition, for each integer \(j\ge0\), the eight positions \(8j,\ldots,8j+7\) in \(P_d\) form the block
\[
B_j=a\;b\;\bar a\;x_j\;a\;\bar b\;\bar a\;y_j,
\]
where \(x_j=d_2\oplus(j\bmod2)\) and \(y_j=p_{8j+7}\in\{0,1\}\). There is no restriction on \(y_j\) needed for the following calculation. For \(W_k\), the number of blocks is \(M=2^{k-3}\), and its final symbol is \(y_{M-1}=p_{2^k-1}=d_k\).

**3. Exact block transitions.** Directly scan the eight displayed letters of \(B_j\) using the three-state procedure in step 1. The following transition facts hold for either value of \(x_j\) and \(y_j\):

* If \(a\ne b\), then from **any** incoming pending-letter state, the block completes exactly three arches and leaves pending state \(y_j\).
* If \(a=b\), then the reachable incoming states are only \(\bot\) and \(1-a\). From \(\bot\), the block completes \(3-\mathbf1_{\{y_j\ne a\}}\) arches. From \(1-a\), it completes \(4-\mathbf1_{\{y_j\ne a\}}\) arches. Either way it leaves state \(\bot\) when \(y_j=a\), and state \(1-a\) when \(y_j\ne a\).

These are finite, explicitly checkable transition identities, not hypotheses about the infinite word. They can be verified simply by following the eight symbols or by running the supplied standalone checker on all possible input bits and states.

**4. Summation.** If \(a\ne b\), the initial state is \(\bot\), and every one of the \(M\) blocks contributes exactly three arches. Hence \(\iota(W_k)=3M\).

If \(a=b\), let \(I_j=\mathbf1_{\{y_j\ne a\}}\). The first block contributes \(3-I_0\). For \(j\ge1\), its incoming state is \(1-a\) precisely when \(I_{j-1}=1\), and its contribution is \(3+I_{j-1}-I_j\). Telescoping gives
\[
\iota(W_k)=(3-I_0)+\sum_{j=1}^{M-1}(3+I_{j-1}-I_j)=3M-I_{M-1}.
\]
As \(y_{M-1}=d_k\) and \(a=d_0=d_1\), this is exactly the stated exception. Combining the two cases proves the formula. The limit follows by dividing by \(2^k\); both values occur by choosing \(d_k=a\) or \(d_k=1-a\), with \(d_0=d_1=a\). For uniformly chosen \((d_0,\ldots,d_k)\), precisely two of the eight possible triples \((d_0,d_1,d_k)\), namely \((0,0,1)\) and \((1,1,0)\), cause the exception. Its proportion is therefore \(1/4\). This proves the remaining assertions.

## Verification
The standalone script `verify.py` independently constructs prefixes both from their binary-valuation formula and by iterating the folding recursion. It compares them and checks the theorem on **all** \(2^{k+1}\) instruction choices for each \(3\le k\le10\), plus deterministic pseudo-random instruction samples at \(k=11,13,16,19\). It separately enumerates every possible eight-block state transition, and, for \(k=3,4\), directly constructs scattered subsequence sets rather than relying only on the greedy-arch theorem.

Reproduce using `python3 verify.py`. The checked output ends with `VERIFY_OK`. Finite execution is a check of implementation and algebra; the theorem for arbitrarily large \(k\) and noncomputable \(d\) follows from the block-transition proof, not from extrapolation.

## Relationship to prior work
Generalized paperfolding words and their valuation descriptions are classical. Holub (2012) proves universal existence of abelian powers in all such words, but his examined argument addresses contiguous blocks and their letter counts, not the present scattered-subsequence universality. Barker et al. (2020) formalize the universality index and greedy arch factorization for arbitrary finite words. Schnoebelen and Veron (2023) give general arch-jumping methods; those generic algorithms do not evaluate this invariant for the generalized paperfolding family. Shallit (2024/2025) studies run lengths, positions, and their automatic properties for the family; the accessible complete text does not state the binary scattered-subsequence index or its exact instruction-dependent dyadic formula.

The main distinction is the uniform **closed formula simultaneously for every instruction stream and every dyadic prefix**, with an exact one-symbol boundary defect, rather than a general algorithm applied to finitely many prefixes. The closely related 2015 paper by Goč, Mousavi, Schaeffer, and Shallit on recurrence, appearance and common factors was identified from its abstract but its complete text could not be obtained in this review. An equivalent observation in that or other unindexed work cannot be excluded.

## Limitations
The result is restricted to binary paperfolding words, alphabet \(\{0,1\}\), and prefix lengths \(2^k\) with \(k\ge3\). It gives the maximum length for which **every** binary scattered subsequence is present, but neither counts individual subsequence multiplicities nor classifies all shortest absent subsequences. It does not assert that no stronger theorem is present in inaccessible literature.

## References
1. Š. Holub, *Abelian powers in paper-folding words*, arXiv:1207.3585, first submitted 2012-07-16; Journal of Combinatorial Theory Series A 120 (2013), 872–881. Full text: https://arxiv.org/abs/1207.3585.
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (2020). Full text: https://arxiv.org/abs/2003.04629.
3. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (2023). Full text: https://arxiv.org/abs/2304.11932.
4. J. Shallit, *Runs in Paperfolding Sequences*, arXiv:2412.17930, first submitted 2024-12-23; published online 2025-09-01. Open-access complete text: https://doi.org/10.1017/S0004972725100440.
5. D. Goč, H. Mousavi, L. Schaeffer, J. Shallit, *A New Approach to the Paperfolding Sequences*, CiE 2015, LNCS 9136, pp. 34–43, https://doi.org/10.1007/978-3-319-20028-6_4 (abstract consulted; complete text unavailable).
