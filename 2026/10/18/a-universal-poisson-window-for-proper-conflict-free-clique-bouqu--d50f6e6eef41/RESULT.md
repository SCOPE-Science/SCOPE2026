# A universal Poisson window for proper conflict-free clique-bouquet colorings

## Finding

**Theorem (bounded-block Poisson window).** Let \(M\ge1\) be a fixed integer. For each index \(N\), let \(b_N\ge2\) and \(1\le s_{N,i}\le M\) for \(1\le i\le b_N\). Put \(S_N=\sum_i s_{N,i}\), assume \(S_N\to\infty\), and form the graph
\[
W_N=K_1\vee\left(\bigsqcup_{i=1}^{b_N}K_{s_{N,i}}\right).
\]
Let \(q_N\) be an integer palette size, \(r_N=q_N-1\), and assume
\[
\frac{S_N}{r_N}-\log S_N\longrightarrow c\in\mathbb R.
\]
Choose uniformly among all proper vertex colorings \(W_N\to\{1,\ldots,q_N\}\) (unused colors are permitted), and let \(X_N\) be the number of colors appearing exactly once in the open neighborhood of the unique hub. Then
\[
X_N\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}(e^{-c}).
\]
In particular, the probability that a uniformly random proper coloring is also proper conflict-free converges to
\[
\boxed{1-\exp(-\exp(-c))}.
\]
The limit is independent of the number, order, and distribution of clique sizes, provided they are uniformly bounded. The one-vertex-per-block case is the classical singleton-occupancy model; the assertion also holds for arbitrary mixtures of larger clique blocks.

**Exact finite counting identity used in the proof.** For positive clique sizes \(s_1,\ldots,s_b\), any integer \(q\ge1+\max_i s_i\), and \(r=q-1\), write \((a)_{h}=a(a-1)\cdots(a-h+1)\) for \(h\ge1\), with \((a)_0=1\) and \((a)_h=0\) for \(h>a\ge0\). The number \(P_{\mathbf s}(q)\) of named-palette proper conflict-free colorings is
\[
P_{\mathbf s}(q)
=q\sum_{j=1}^{r}(-1)^{j+1}\binom rj j!\,[u^j]
\prod_{i=1}^b\left(\sum_{h=0}^{\min(j,s_i)}\binom{s_i}{h}(r-j)_{s_i-h}u^h\right).
\]
This is a finite supporting identity, not a claim that general proper-coloring generating functions are new.

## Assumptions and scope

All graphs are finite and simple; the join has one distinguished central vertex, and block vertices are labelled. A proper coloring is a map to a named palette in which adjacent vertices receive different colors. A proper conflict-free coloring is proper and, at every nonisolated vertex, some color occurs exactly once in its **open** neighborhood. For the probability statement, \(S_N\to\infty\) with a fixed bound \(M\) on every peripheral clique size. The assumed scaling ensures \(r_N\to\infty\) and \(r_N\ge M\) eventually, so proper colorings exist. There are no assumptions on the relative frequencies of block sizes. Colors may remain unused.

## Proof

**1. Reduction to singleton colors.** Fix a proper coloring. Every peripheral vertex has an open neighborhood consisting of the hub and its own block minus itself, hence a clique. Its neighborhood colors are pairwise distinct. Therefore all peripheral vertices already satisfy the conflict-free condition; only the hub can fail. Since the hub color occurs nowhere else, the hub is satisfied if and only if at least one of the other \(r\) colors appears on exactly one peripheral vertex. Each block receives \(s_i\) pairwise distinct colors chosen from those \(r\) colors. Conditional on the hub color, the ordered block assignments are independent uniform injections.

**2. Exact enumeration.** Fix a set of \(j\) named non-hub colors and require each to appear exactly once. If \(h\) of them occur in block \(i\), assigning these \(h\) distinct labels to \(h\) block positions and filling remaining positions from the other \(r-j\) colors gives \((s_i)_h(r-j)_{s_i-h}\) possibilities for that fixed \(h\)-set. Summing over the choices and assignments of the \(j\) named colors to blocks gives
\[
j![u^j]\prod_i\sum_{h=0}^{\min(j,s_i)}\binom{s_i}{h}(r-j)_{s_i-h}u^h.
\]
Inclusion-exclusion over the \(r\) possible singleton-color events, then the \(q\) hub colors, proves the stated finite identity.

**3. Factorial moments of singleton counts.** Work in the asymptotic regime and abbreviate \(S=S_N\), \(r=r_N\), \(s_i=s_{N,i}\), \(b=b_N\). Fix \(j\ge1\) and select \(j\) distinct non-hub colors. In block \(i\), the probability that none of these colors is used is
\[
p_{0,i}=\frac{(r-j)_{s_i}}{(r)_{s_i}}.
\]
For any specified one of these colors, the probability that it is the only specified color used in the block is
\[
p_{1,i}=\frac{s_i(r-j)_{s_i-1}}{(r)_{s_i}}.
\]
Because \(s_i\le M\) and \(j\) is fixed, uniformly in \(i\),
\[
p_{0,i}=1-\frac{js_i}{r}+O_{j,M}(r^{-2}),\qquad
\frac{p_{1,i}}{p_{0,i}}=\frac{s_i}{r}(1+O_{j,M}(r^{-1})).
\]
We have \(r\asymp S/\log S\), \(b\le S\), and \(S/r^2\to0\). Thus
\[
\prod_i p_{0,i}=\exp(-jS/r+o(1)).
\]
For each of the \(j\) specified colors to be used exactly once, assign it to the block where it appears. Assignments to **distinct** blocks contribute
\[
\left(\prod_i p_{0,i}\right)
\sum_{\phi:[j]\hookrightarrow[b]}\prod_{a=1}^j\frac{p_{1,\phi(a)}}{p_{0,\phi(a)}}
=\left(\prod_i p_{0,i}\right)(S/r)^j(1+o(1)).
\]
Indeed, the unrestricted assignment sum is asymptotic to \((S/r)^j\), while the relative mass of repeated block indices is \(O_{j,M}(\sum_i s_i^2/S^2)=O_{j,M}(1/S)\). If two or more specified colors share one block, the probability of that exact group is \(O_{j,M}(r^{-h})\) for a group of size \(h\). Partitioning the \(j\) colors into fewer than \(j\) nonempty groups and summing assignments of groups to blocks gives at most \(O_{j,M}((\prod_i p_{0,i})S^{j-1}/r^j)\). These contributions are negligible. Consequently, for the \(j\) fixed target colors,
\[
\Pr(\text{all occur exactly once})
=(1+o(1))(S/r)^j\exp(-jS/r).
\]
By symmetry among the \(r\) non-hub colors,
\[
\mathbb E[(X_N)_j]=(r)_j\Pr(\text{all }j\text{ occur exactly once})
=(1+o(1))S^j\exp(-jS/r)
\longrightarrow e^{-jc}.
\]
For every fixed positive integer \(j\), these are the factorial moments of a Poisson random variable of mean \(e^{-c}\). The standard factorial-moment convergence criterion for nonnegative integer random variables yields \(X_N\Rightarrow\operatorname{Poisson}(e^{-c})\). Therefore \(\Pr(X_N\ge1)\to1-\exp(-e^{-c})\), as claimed.

**4. Finite optimal-palette illustration.** If all \(b\ge2\) blocks have size \(s\ge1\), the known block-graph PCF threshold gives \(q=s+2\). Every proper coloring with that palette omits exactly one of the \(s+1\) non-hub colors per block. A color occurs exactly once precisely when it is omitted by exactly \(b-1\) blocks. For \(b=2\), omitted colors must differ; for \(b\ge3\), exactly one color is omitted by \(b-1\) blocks. Thus the exact minimum-palette counts are
\[
P_{(s,s)}(s+2)=(s+2)(s!)^2(s+1)s,
\]
\[
P_{(s,\ldots,s)}(s+2)=(s+2)(s!)^b(s+1)bs\quad (b\ge3).
\]
These are supporting finite specializations; the principal new conclusion is the universal growing-palette Poisson window.

## Verification

The standalone `verify_pcf_bouquets.py` constructs the actual adjacency lists and tests the open-neighborhood PCF predicate directly for 423,262 labelled color assignments across 44 finite cases. It compares the counts with an independent coefficient/inclusion-exclusion implementation. Twenty-one additional proper-coloring enumerations compare against the identity. Twenty-four uniform minimum-palette comparisons check the two explicit formulas, and three bounded-block critical-window examples compare their first two factorial moments with the predicted Poisson moments. Run `python3 verify_pcf_bouquets.py` and compare its output with `verification_output.txt`. All recorded finite tests passed. None of these tests alone establishes the asymptotic theorem: its proof is the factorial-moment argument above.

## Relationship to prior work

Pradhan and Sharma, arXiv:2608.10874 (first submitted 2026-08-11), characterize when a block graph needs one more color than its clique number and give coloring algorithms. Their paper already covers the **minimum number of colors** of these clique bouquets. That parameter is not claimed new here. Tom and Vailaya, arXiv:2503.19344, give general chromatic-symmetric-function machinery for graphs glued at one vertex, including triangles sharing a hub. Their invariant contains proper-color frequency data and can in principle recover fixed finite-palette counts under an appropriate singleton extraction. No independent priority is claimed for the generic fact that proper-coloring frequencies determine finite PCF enumerations. The result here is the explicit bounded-heterogeneity Poisson critical window for uniformly random proper colorings, proved with row-dependent without-replacement assignments.

The case where every peripheral clique has order one is ordinary singleton occupancy and is acknowledged as a classical special case. No inspected relevant source stated the claimed universal growing-palette limit for mixed-size clique bouquets. A more general occupancy theorem might imply this limit; determining definitive priority remains open to independent bibliographic checking.

## Limitations

The theorem is proved only for uniformly bounded peripheral clique sizes and the stated critical scaling; no claim is made for unbounded blocks, list colorings, improper conflict-free colorings, or arbitrary block graphs. The finite formula includes familiar color-frequency information and is not asserted to be novel independently of existing chromatic-symmetric-function machinery. The work has received only self-review; independent mathematical review and definitive bibliographic-priority review have not been performed.

## References

1. D. Pradhan and V. Sharma, *Complexity and algorithms for proper conflict-free coloring in graphs*, arXiv:2608.10874v1, first posted 2026-08-11, https://arxiv.org/abs/2608.10874.
2. F. Tom and A. Vailaya, *The chromatic symmetric function of graphs glued at a single vertex*, arXiv:2503.19344 (2025), Electron. J. Combin. 33 (2026), #P2.9, https://doi.org/10.37236/14403.
3. I. Fabrici, B. Lužar, S. Rindošová, and R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, Discrete Appl. Math. 324 (2023), 80–90, https://arxiv.org/abs/2202.02570.
4. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Adv. Math. 111 (1995), 166–194. General chromatic-symmetric-function background.
