# Rigid shortest one-marker supersequences under a zero-run limit

## Finding

For every integer \(n\ge4\), consider the family of one-marker binary strings
\[
\mathcal U_n=\{0^i1 0^{n-1-i}:0\le i<n\}.
\]
Let \(L_n\) be the minimum length of a binary word \(w\) that simultaneously contains every member of \(\mathcal U_n\) as a **scattered subsequence**, while avoiding the **contiguous** factor \(000\). Then
\[
\boxed{L_n=\left\lceil\frac{3n}{2}\right\rceil}.
\]
The **complete optimizer classification** is as follows.

* If \(n=2m\ge4\), the unique optimizer is \((010)^m\).
* If \(n=2m+1\ge5\), exactly \(m+3\) distinct optimizers exist. Three are
  \[(001)^m00,\qquad 1(001)^m0,\qquad 01(001)^m.\]
  The remaining \(m\) are
  \[
  01\,0^{d_1}1\,0^{d_2}1\cdots 0^{d_m}1\,0,
  \qquad d_1,\ldots,d_m\in\{1,2\},\quad
  \#\{j:d_j=1\}=1.
  \]
Every optimizer also avoids the contiguous factor \(111\), even though this is not imposed.

## Assumptions and scope

Words are finite, linear, over the binary alphabet \(\{0,1\}\), and different positions of identical bits are not distinguishable. A *scattered subsequence* selects strictly increasing indices; a *contiguous factor* uses consecutive indices. The host is restricted by at most two consecutive zeros, whereas its one-marker **targets are not restricted**. The claim covers all and only integer lengths \(n\ge4\). All minima and optimizer counts use distinct host words, with no quotient by rotations or reversal.

## Proof

**1. Exact criterion for one marker.** Let a host \(w\) have \(Z\) zeros and \(K\) ones. For each occurrence of \(1\), write \(a\) for the number of zeros strictly before it, so that \(Z-a\) zeros are strictly after it. The target \(0^i1 0^{n-1-i}\) is a scattered subsequence using that occurrence of \(1\) if and only if
\[
  a\ge i\quad\text{and}\quad Z-a\ge n-1-i.
\]
Write \(s=Z-(n-1)\). Since the target \(0^{n-1}1\) embeds, \(s\ge0\). An occurrence with zero-rank \(a\) therefore covers exactly the integer indices
\[
  I_a=[\max(0,a-s),\min(n-1,a)]\cap\mathbb Z.
\]
Every such interval has at most \(s+1\) elements; the \(K\) occurrences together must cover the \(n\) indices, so
\[
 K(s+1)\ge n. \tag{1}
\]

**2. Universal lower bound.** The host has \(K+1\) zero runs (including possibly empty boundary runs). Avoiding \(000\) bounds the size of each by two, hence
\[
 Z\le2(K+1),\qquad K\ge\left\lceil\frac{Z-2}{2}\right\rceil. \tag{2}
\]
If \(s=0\), (1) forces \(K\ge n\), giving \(|w|\ge2n-1>\lceil3n/2\rceil\) for \(n\ge4\). If \(s=1\), then \(Z=n\) and (1) gives \(K\ge\lceil n/2\rceil\), so \(|w|\ge\lceil3n/2\rceil\). If \(s\ge2\), then \(Z\ge n+1\), and (2) yields
\[
 |w|=Z+K\ge n+1+\left\lceil\frac{n-1}{2}\right\rceil
 \ge\left\lceil\frac{3n}{2}\right\rceil.
\]
The last inequality is strict for even \(n\). For odd \(n\), equality in the last display requires \(s=2\); if \(s\ge3\), then \(Z\ge n+2\), so (2) makes the bound strict. Thus equality is possible only at \(s=1\), or at \(s=2\) when \(n\) is odd.

**3. Even lengths.** Put \(n=2m\). Equality requires \(Z=2m\), \(K=m\) and \(s=1\). Each of the \(m\) marker occurrences covers at most two of the \(2m\) indices. Consequently, all \(m\) intervals are disjoint two-element intervals partitioning \(\{0,1,\dots,2m-1\}\). Necessarily the zero-ranks of the successive ones are
\[
 a_1,a_2,\ldots,a_m=1,3,\ldots,2m-1.
\]
Those ranks uniquely determine \(w=(010)^m\). Conversely, the displayed ranks cover all marker indices and the word avoids \(000\). Its length is \(3m\).

**4. Odd lengths, surplus two.** Put \(n=2m+1\). If \(s=2\), equality requires \(Z=2m+2\) and \(K=m\). The inequality \(Z\le2(K+1)\) is tight, so **all** the \(m+1\) zero runs have length two. The unique word is \((001)^m00\), with one-ranks \(2,4,\ldots,2m\). Their intervals of width three cover all \(2m+1\) marker indices.

**5. Odd lengths, surplus one.** If \(s=1\), equality requires \(Z=2m+1\) and \(K=m+1\). List the zero-ranks of the ones in nondecreasing order as \(a_1,\ldots,a_{m+1}\). Covering the two endpoint indices forces
\[
 a_1\in\{0,1\},\qquad a_{m+1}\in\{2m,2m+1\}.
\]
Moreover, all intervals \(I_{a_j}=[a_j-1,a_j]\cap[0,2m]\) must jointly cover consecutive integers, which forces \(a_{j+1}-a_j\le2\). Across \(m\) increments, the endpoints \((0,2m+1)\) are impossible. If the endpoints are \((0,2m)\), every increment is two, yielding \(1(001)^m0\). If they are \((1,2m+1)\), every increment is two, yielding \(01(001)^m\). If they are \((1,2m)\), exactly one of the \(m\) increments equals one, all others equal two, producing precisely the \(m\) displayed \(01\,0^{d_1}1\cdots0^{d_m}1\,0\) words.

Conversely, every listed zero-rank sequence covers all marker indices. Its internal zero gaps have lengths one or two; its boundary gaps have lengths at most two. Thus it satisfies the contiguous-factor restriction and has exactly \(3m+2=\lceil3(2m+1)/2\rceil\) symbols. The three families are disjoint, and the \(m\) choices of the shorter internal gap are distinct. This gives exactly \(m+3\) optimizers.

**6. Stronger run restriction.** All listed words have separated ones, so none contains \(11\), and a fortiori none contains \(111\). This completes the proof.

## Verification

Run `python3 verify_onehot_rll.py` in the same directory as this document. The standalone checker generates all binary hosts avoiding `000` of every length from \(n\) to \(\lceil3n/2\rceil\), independently tests each one-marker target by a direct subsequence-matching algorithm, compares the **complete set** of optimal hosts against the expressions above and checks that all optima avoid `111`. The finite exhaustive check covers every \(4\le n\le14\), examines **1,640,493 host candidates**, and finishes with `CHECK_OK total_candidate_hosts_examined=1640493`. It is a corroborating finite experiment. The proof in Sections 1–6 establishes all lengths.

## Relationship to prior work

This is a constrained shortest-common-supersequence problem. General binary SCS complexity and no-identical-adjacent-letter **input** restrictions appear in Lagoutte and Tavenas (2013), but neither addresses the complete one-marker input family together with an output constraint of avoiding `000`. The run-pattern-avoidance enumerations of Bilotta, Pergola and Pinzani (2011) do not impose the all-one-marker subsequence coverage condition. Elishco and Huleihel (2022) study random homopolymer-constrained DNA *source strands* and optimal reference sequences in a probabilistic model. Ma et al. (2025) study shortest-common-supersequence batch costs for all *balanced* input strings; their exact bounds and constructions do not imply this sparse one-marker classification. No claim of guaranteed global novelty follows from literature search alone.

## Limitations

No classification is asserted for \(n<4\), marker weight at least two, arbitrary alphabets, cyclic hosts, or a nonzero noise budget. The host restriction concerns only `000`; avoidance of `111` is a conclusion about minimum-length solutions. The prior-work comparison is subject to unindexed or otherwise unavailable manuscripts and has not been independently audited.

## References

1. S. Bilotta, E. Pergola, R. Pinzani, *Pattern \(1^j0^i\) avoiding binary words*, arXiv:1108.3621, first version 18 August 2011. https://arxiv.org/html/1108.3621v1
2. A. Lagoutte, S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422, first version 2 September 2013. https://arxiv.org/abs/1309.0422
3. O. Elishco, W. Huleihel, *Optimal Reference for DNA Synthesis*, arXiv:2204.07013, first version 14 April 2022. https://arxiv.org/html/2204.07013v1
4. Y. Ma et al., *Batch optimization for balanced binary sequences and DNA sequences*, BMC Bioinformatics 26, 300 (2025). https://doi.org/10.1186/s12859-025-06336-5
