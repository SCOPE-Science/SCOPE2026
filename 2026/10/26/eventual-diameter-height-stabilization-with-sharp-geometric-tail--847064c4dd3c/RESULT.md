# Eventual diameter–height stabilization with sharp geometric tails in Bernoulli recursive trees

## Finding
Consider the Bernoulli recursive tree in which vertex \(v_0\) is joined to \(v_1\), and each subsequent vertex \(v_m\) independently attaches to \(v_{m-1}\) with probability \(p\in(0,1)\) or to \(v_{m-2}\) with probability \(q=1-p\). Let \(T_n\) be the tree with vertices \(v_0,\ldots,v_n\), \(H_n=\max_{v\in T_n}d(v_0,v)\) its rooted height, and \(D_n=\max_{u,v\in T_n}d(u,v)\) its graph diameter.

There exists a finite, nonnegative, integer-valued random variable \(K\) such that
\[
  D_n-H_n=K\qquad\text{for all sufficiently large }n\quad\text{almost surely}.
\]
For every integer \(k\ge1\), its tail satisfies the explicit two-sided bounds
\[
  q^{2k-1}\ \le\ \mathbb P(K\ge k)\ \le\
  \frac{1+q^2}{(1-q^2)^2}\,q^{2k-1}.
\]
Consequently the exponential tail exponent is exact:
\[
  \lim_{k\to\infty}-\frac1k\log\mathbb P(K\ge k)
  =2\log(1/q).
\]
The difference between finite-tree diameter and rooted height therefore *stops changing after a finite random stage*, and its limiting error has a sharp exponential decay rate. The theorem does not assert an explicit probability mass function for \(K\).

## Assumptions and scope
Every edge has unit length. The attachment variables are independent and identically distributed, with the same fixed parameter \(0<p<1\) at all times. The height and diameter refer to the actual finite tree \(T_n\), not to the induced metric on a truncation of an infinite ray. The probabilities in the displayed bounds average over the complete infinite sequence of attachments. No assumption of independent branch lengths is made.

## Proof
**1. Depth increases and the infinite spine.** Write \(h_m=d(v_0,v_m)\), so \(h_0=0\), \(h_1=1\) and, for \(m\ge2\),
\[
 h_m=\begin{cases}1+h_{m-1},&\text{with probability }p,\\
                     1+h_{m-2},&\text{with probability }q.
      \end{cases}
\]
The choices are independent of the previous tree. Inductively \(h_m-h_{m-1}\in\{0,1\}\): the increment is \(1\) for a last-vertex attachment and \(1-(h_{m-1}-h_{m-2})\) for a second-last attachment. Thus \(H_n=h_n\), and \(H_n\ge\lceil n/2\rceil\), so \(H_n\to\infty\).

Call a choice at index \(j\ge1\) a first-predecessor choice if \(v_{j+1}\) attaches to \(v_j\). Such a choice makes \(v_j\) an ancestor of all sufficiently late vertices: \(v_{j+1}\) is its child, and \(v_{j+2}\) attaches to one of these two, after which induction applies. Almost surely there are infinitely many first-predecessor choices. Every infinite ray from \(v_0\) must therefore pass through the corresponding unbounded sequence of ancestors. This proves that the infinite tree has a unique infinite simple ray (its **spine**) and all components off the spine are finite.

Let the spine vertices in order be \(s_0=v_0,s_1,s_2,\ldots\), with \(s_i=v_{\sigma_i}\). Edges only join labels differing by one or two, so \(\sigma_0=0\) and \(\sigma_i\le2i\). A vertex off the spine cannot have a first-predecessor choice at its own index, as that would force it onto the spine. Therefore it has at most one child; each finite component off the spine is a simple path (a **tooth**). Write \(L_i\in\mathbb Z_{\ge0}\) for the length of the tooth at \(s_i\), with \(L_i=0\) if none.

**2. The run-to-tooth rule.** Put \(b_0=1\) for the initial root edge, and for \(j\ge1\) put \(b_j=1\) when \(v_{j+1}\) attaches to \(v_j\), and \(b_j=0\) otherwise. When \(b_{\sigma_i}=0\), the site \(s_i\) has no tooth. When \(b_{\sigma_i}=1\), let \(r_i\) be the number of consecutive zeros immediately following \(b_{\sigma_i}\) before the next one. Then
\[
                 L_i=\lceil r_i/2\rceil.
\]
For completeness, after a first-predecessor choice, successive second-predecessor choices grow two alternating descendant chains from the site; each pair of such choices extends each chain by one. The next first-predecessor choice selects one chain as the continuing spine, leaving the other as a finite tooth. This gives the formula for both parities of \(r_i\), including \(r_i=0\). This deterministic two-chain argument uses only the stated attachment rule. In particular, \(L_i\ge m\) requires a block of at least \(2m-1\) consecutive second-predecessor choices immediately after some index \(\sigma_i\le2i\).

**3. A finite geometric excess.** Define
\[
                   K=\sup_{i\ge0}(L_i-i).
\]
Since \(L_0\ge0\), this supremum is nonnegative. For any \(i\ge0\) and integer \(k\ge1\), if \(L_i-i\ge k\), then a run of \(2(i+k)-1\) consecutive zeros begins just after one of the at most \(2i+1\) indices \(0,\ldots,2i\). Independence and a union bound imply
\[
 \mathbb P(L_i-i\ge k)\le(2i+1)q^{2(i+k)-1}.
\]
Consequently,
\[
 \mathbb P(K\ge k)\le \sum_{i=0}^\infty(2i+1)q^{2(i+k)-1}
 =q^{2k-1}\frac{1+q^2}{(1-q^2)^2}.
\]
This tends to zero with \(k\), so \(K<\infty\) almost surely. Since all \(L_i-i\) are integers and the \(i=0\) term is nonnegative, the supremum is attained at at least one finite index.

For the lower bound, require the first \(2k-1\) random attachment choices following \(b_0\) all to use the second predecessor. This event has probability \(q^{2k-1}\) and creates two alternating chains from the root, each of length at least \(k\). A later first-predecessor choice occurs almost surely and selects exactly one chain as the infinite spine; the other is a tooth of length at least \(k\) at \(s_0\). Thus \(K\ge L_0\ge k\). The two bounds have identical exponential rates, proving the displayed limit.

**4. Eventual diameter identity.** Consider vertices \(u,v\) in teeth at spine positions \(i<j\), at distances \(a\le L_i\) and \(b\le L_j\) from their respective spine sites (spine vertices are allowed by setting the distances to zero). Their graph distance is
\[
                  d(u,v)=j-i+a+b=(j+b)+(a-i)
                  \le H_n+K
\]
whenever \(u,v\in T_n\). Vertices on one tooth are at distance at most \(H_n\). Hence \(D_n\le H_n+K\) for every \(n\). Choose a tooth tip \(u_*\) at some finite index \(i_*\) attaining \(K=L_{i_*}-i_*\) (use the root when \(K=0\) and a zero-length tooth attains it). Because every fixed finite collection of teeth is finite, the spine projection of the latest vertex \(v_n\) eventually lies strictly beyond \(i_*\). Then
\[
                  d(u_*,v_n)=H_n+(L_{i_*}-i_*)=H_n+K,
\]
and \(u_*\in T_n\) for all sufficiently large \(n\). This proves \(D_n-H_n=K\) eventually almost surely.

## Verification
The attached standalone file `verify_diameter.py` enumerates every sequence of zero/one attachment choices of length at most eleven and then continues with first-predecessor choices. It checks 4,095 finite trees, computing graph diameters by breadth-first search independently of the spine/depth formulas. For each tree it reconstructs all teeth and checks the run-to-tooth rule and the exact diameter-excess identity in its eventual continuation. All 4,095 cases passed. These finite enumerations are consistency checks, not a replacement for the infinite-spine, union-bound, or almost-sure stabilization arguments.

## Relationship to prior work
Tang, Wang and Wu (2026, arXiv:2607.02916v1) introduced this nearest/second-nearest recursive tree, proved its almost-sure unique end and the infinite-collision property, and described its trunk and branch lengths. The present claim addresses a different invariant: the full finite-tree diameter relative to root height, including almost-sure eventual equality and a quantitative sharp tail exponent. The run-to-tooth property is an acknowledged existing structural ingredient and is independently derived here for the quantitative proof; neither the one-endedness theorem nor a branch marginal distribution alone states the claimed diameter law.

General deterministic facts about combs and finite-branch trees may subsume the geometric identity, but do not by themselves give the displayed model-specific sharp tail exponent. Related work on geometric teeth and weak topologies addresses a different invariant; a full-text comparison to every potentially relevant general comb reference has not been completed.

## Limitations
The law of \(K\) is bounded rather than identified exactly. The bound's multiplicative constant is not claimed optimal, only its exponential rate. The conclusions require \(p\in(0,1)\) and unit edge lengths; the limit \(p\downarrow0\) is not uniform. The result does not quantify the random time after which equality stabilizes, nor collision probabilities or random-walk mixing.

## References
1. Jia-shan Tang, Feng Wang and Xian-Yuan Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916v1 (first publicly posted 2026-07-03), Sections 1–3. https://arxiv.org/abs/2607.02916
2. Y.-H. Mao, F. Wang and X.-Y. Wu, *Large deviation behavior for the longest head run in an i.i.d. Bernoulli sequence*, Journal of Theoretical Probability 28 (2015), 259–268. This is background on long runs; the proof here uses a direct union bound rather than any theorem from this paper.
