# A double-exponential staircase for successive root-to-leaf distances in the binary Kesten tree

## Finding

Let \(\mathcal K\) be the critical binary Kesten tree: every vertex on its infinite spine has exactly two children, one continuing the spine and one rooting an independent Galton–Watson tree whose offspring count is zero or two with equal probabilities. List the distances from the root to all leaves in nondecreasing order, with multiplicities for distinct leaves at equal distance, as \(R_1\le R_2\le\cdots\). For a fixed integer \(m\ge0\), set

\[
B_{r,m}=2^{-2^{r-m+1}+r-2m+2},\qquad r\ge m+1.
\]

**Theorem (multi-leaf protection staircase).** For every fixed \(m\ge0\), as the integer radius \(r\to\infty\),

\[
\Pr(R_{m+1}>r)=B_{r,m}\left(1+O_m\left(r^m 2^{-2^{r-m}}\right)\right).
\]

In fact the following explicit non-asymptotic inequality holds for every \(r\ge m+1\):

\[
1\le\frac{\Pr(R_{m+1}>r)}{B_{r,m}}
\le 1+\left(5^m-1+2^m(m+1)r^m\right)2^{-2^{r-m}}.
\]

For \(m=0\) there is equality \(\Pr(R_1>r)=B_{r,0}\) at every \(r\ge1\), reproducing the known first-leaf tail. For successive fixed orders \(m+1\), the leading double-exponential exponent halves each time one more nearby leaf is permitted. In particular, \(\Pr(R_2>r)\sim2^{-2^r+r}\), whereas \(\Pr(R_3>r)\sim2^{-2^{r-1}+r-2}\).

There is also a conditional structural conclusion. Define \(E_{r,m}\) to be the event that the ordinary side-subtrees attached to the first \(m\) spine vertices are single-vertex leaves and that every later side-subtree attached before depth \(r\) contains no leaf within root distance \(r\). Then \(\Pr(E_{r,m})=B_{r,m}\) and

\[
\Pr(E_{r,m}\mid R_{m+1}>r)\longrightarrow1.
\]

Thus the rare event is asymptotically realized by one specific comb-like initial configuration, not by a diffuse mixture of many protective shapes.

**Finite-tree interpretation.** Let \(\mathcal T_N\) be a uniformly chosen rooted plane full binary tree with \(N\) internal vertices (equivalently, a critical zero-or-two Galton–Watson tree conditioned to have \(2N+1\) vertices). For each fixed \(r,m\), its root's \((m+1)\)-st closest-leaf distance converges in distribution at that threshold to the corresponding \(R_{m+1}\) in \(\mathcal K\). Consequently the same staircase holds in the explicitly *iterated* limit \(N\to\infty\) followed by \(r\to\infty\). No simultaneous growth regime for \(N\) and \(r\) is asserted.

## Assumptions and scope

The offspring law for normal vertices is \(\Pr(\xi=0)=\Pr(\xi=2)=1/2\). Size-biased offspring along the spine is deterministically two; its extra child has the independent normal offspring law. Each distinct leaf is counted once even if several leaves have the same depth. The spine itself contains no leaves. Almost surely there are infinitely many leaves because the independent side-subtree roots are leaves with probability \(1/2\). The order parameter \(m\) remains fixed when \(r\) increases. The result is a probability statement about the local limit, with an iterated-limit corollary for finite conditioned trees.

## Proof

**Step 1: exact generating functions.** For a normal binary Galton–Watson tree, let \(X_h\) count leaves at relative levels at most \(h\), including its root if it is a leaf. Its probability generating polynomial is

\[
f_0(z)=\frac{1+z}{2},\qquad f_h(z)=\frac{z+f_{h-1}(z)^2}{2}\quad(h\ge1).
\]

The constant term \(a_h=\Pr(X_h=0)\) satisfies \(a_0=1/2\), \(a_h=a_{h-1}^2/2\), whence

\[
a_h=2^{-(2^{h+1}-1)}.
\]

The coefficient \(b_h=\Pr(X_h=1)\) satisfies \(b_0=1/2\) and \(b_h=1/2+a_{h-1}b_{h-1}\) for \(h\ge1\); in particular

\[
\frac12\le b_h\le\frac12+a_{h-1}.
\]

The \(r\) normal subtrees visible along the first \(r\) spine vertices independently contribute \(X_{r-1},X_{r-2},\ldots,X_0\) to the number of leaves at root distance at most \(r\). Therefore

\[
\Pr(R_{m+1}>r)=\sum_{j=0}^{m}[z^j]\prod_{h=0}^{r-1}f_h(z).
\]

This identity holds for every pair of nonnegative integers \(r,m\), with the empty-product convention for \(r=0\).

**Step 2: the leading configuration.** Put \(S_* =\{r-m,\ldots,r-1\}\), the indices of the first \(m\) side-subtrees encountered from the root; here \(r\ge m+1\). If each such subtree's root is itself a leaf and each other visible side-subtree has no leaf at its remaining visible depth, then exactly \(m\) leaves are present. The probability is

\[
\Pr(E_{r,m})=2^{-m}\prod_{h=0}^{r-m-1}a_h
=2^{-m-(2^{r-m+1}-2-(r-m))}=B_{r,m}.
\]

Thus \(\Pr(R_{m+1}>r)\ge B_{r,m}\).

**Step 3: exclusion of all competing support patterns.** For any configuration with at most \(m\) visible leaves, let \(S\subseteq\{0,\ldots,r-1\}\) be the set of side-subtree indices that contribute at least one leaf. Then \(|S|\le m\). Write \(w_h=2^{h+1}-1\) and \(W(S)=\sum_{h\in S}w_h\). Among all sets with at most \(m\) elements the unique maximizer is \(S_*\). For any other \(S\),

\[
W(S_*)-W(S)\ge w_{r-m}-w_{r-m-1}=2^{r-m}.
\]

(If \(|S|<m\) the gap is even larger.) The probability of the contribution pattern \(S\) is at most \(\prod_{h\notin S}a_h\), since the omitted positive-count constraints are probabilities at most one. Dividing by \(B_{r,m}\) and using the gap yields at most \(2^m2^{-2^{r-m}}\) per competing support. There are no more than \((m+1)r^m\) supports with at most \(m\) elements.

For the single maximizing support \(S_*\), the total leaf count can be at most \(m\) only if each included subtree contributes exactly one leaf. Its probability is

\[
\left(\prod_{h=0}^{r-m-1}a_h\right)
\left(\prod_{h=r-m}^{r-1}b_h\right).
\]

For \(h\ge r-m\ge1\), the bound on \(b_h\) gives

\[
1\le2b_h\le1+4\cdot2^{-2^{r-m}}.
\]

Writing \(\varepsilon=2^{-2^{r-m}}\in(0,1]\), we use \((1+4\varepsilon)^m\le1+(5^m-1)\varepsilon\), a direct consequence of the binomial expansion. Adding the competing supports proves the claimed explicit upper bound. Since \(r^m2^{-2^{r-m}}\to0\), this proves the sharp asymptotic. Moreover \(E_{r,m}\subseteq\{R_{m+1}>r\}\) with probability \(B_{r,m}\), so its conditional probability is \(B_{r,m}/\Pr(R_{m+1}>r)\to1\).

**Step 4: conditioned plane trees.** Conditioning the critical binary Galton–Watson law on \(2N+1\) vertices gives the uniform plane full binary tree with \(N\) internal vertices. Its local weak limit as \(N\to\infty\) is \(\mathcal K\). Whether there are at most \(m\) leaves at depth at most \(r\) depends only on the finite neighborhood through depth \(r+1\). Therefore local convergence implies convergence of this event's probability at each fixed \(r,m\). The iterated-limit statement follows, without exchanging the two limits.

## Verification

The standalone script `verification.py` implements the truncated polynomial recurrence over exact rational numbers and checks the displayed exact \(m=0\) formula, non-asymptotic bounds for small radii, and the support-gap inequality for exhaustive sets. Run `python3 verification.py` from this directory. The recorded output is contained in `verification_output.txt`. These finite computations are consistency checks only; the infinite theorem follows from Steps 1–4.

## Relationship to prior work

Maciá and Stufler, *Uniform integrability of the distance to the nearest leaf in random trees* (arXiv:2606.15339, first posted 2026-06-13), prove root nearest-leaf tail bounds and moment convergence for simply generated trees. Their Section 4.5, Proposition 4.15 establishes the one-leaf-avoidance recurrence and Section 4.6, equations (4.15)–(4.16), gives the exact zero-or-two offspring nearest-leaf formula \(\Pr(R_1>r)=2^{-2^{r+1}+r+2}\). That \(m=0\) case is fully prior art, not a new claim. The theorem above concerns all fixed higher-ranked leaf distances \(m+1\ge2\), with a sharp staircase, explicit relative-error inequality and conditional configuration concentration.

Maciá, *The distance to the border of a random tree* (arXiv:2205.10645, 2022), and the prior protection-number literature study the minimum root-to-leaf distance and related single-threshold distributions. These source statements alone do not determine the order-statistic tail \(\Pr(R_{m+1}>r)\) for \(m\ge1\); the new theorem uses the complete vector of shallow leaf counts and an elementary-symmetric support gap. The local-limit passage for finite conditioned trees is standard and not asserted as novel.

## Limitations

The offspring model is exactly critical binary with probabilities \(1/2\) and \(1/2\), and the order \(m\) is fixed. No simultaneous \(m,r\to\infty\) regime, general offspring-law universality, or uniform finite-size approximation in a growing radius is proved. Historical-priority screening cannot exclude every implicit formulation elsewhere, particularly papers on protected subtrees and branching-process small balls. Numerical tests do not certify the infinite theorem. Independent mathematical review has not been performed.

## References

1. V. J. Maciá and B. Stufler, *Uniform integrability of the distance to the nearest leaf in random trees*, arXiv:2606.15339 (first public 2026-06-13), https://arxiv.org/html/2606.15339v2 . Relevant: §§4.2, 4.5–4.6, esp. (4.15)–(4.16).
2. V. J. Maciá, *The distance to the border of a random tree*, arXiv:2205.10645 (2022), https://arxiv.org/abs/2205.10645 . Relevant: Introduction, §6.
3. L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, Electronic Communications in Probability 19 (2014), cited in Reference 1; related background on first-nearest protection numbers.
