# Logarithmic marked-seed double-star rarity in random friend trees

## Finding

Let \(T_n\) be the random friend tree grown from the labeled edge \(\{1,2\}\). For \(n\ge4\) let \(D_n\) be the event that **every subsequent vertex attaches directly to one of the two original seed vertices**, and \(S_n\) the event that the resulting tree is a star. Put \(R_n=\mathbb P(D_n\setminus S_n)\). Hence \(R_n\) measures the probability that the **two original seed vertices**, not an arbitrary pair of vertices, are the only nonleaves.

For integers \(k\ge1\) set
\[
 g(k)=\prod_{j=k}^{\infty}\left(1-\frac1{j(j+1)}\right)^{-1},\qquad
 K=g(1)=3.370690303601868\ldots,
\]
and put \(H_j=\sum_{i=1}^j i^{-1}\). Then, for **every integer \(n\ge4\)**,
\[
 \boxed{\frac{2(H_{n-2}-1)}{(n-1)(n-2)}\le R_n\le
 \frac{2K}{(n-1)(n-2)}\sum_{m=3}^{n-1}\frac{g(m-2)}{m-1}.}
\]
In particular the rare-event scale is sharp:
\[
 \boxed{R_n=\Theta\!\left(\frac{\log n}{n^2}\right),\qquad
 2\le\liminf_{n\to\infty}\frac{n^2R_n}{\log n}
 \le\limsup_{n\to\infty}\frac{n^2R_n}{\log n}\le2K.}
\]
Moreover \(\mathbb P(S_n)=2/(n-1)\), so
\[
 \mathbb P(D_n)=\frac2{n-1}+\Theta\!\left(\frac{\log n}{n^2}\right),\qquad
 \mathbb P(D_n\setminus S_n\mid D_n)
 =\Theta\!\left(\frac{\log n}{n}\right).
\]
This is a *marked-seed* statement. It is not a statement about unrestricted two-hub trees or the whole diameter-three event.

## Assumptions and scope

The initial tree consists of vertices labeled \(1,2\) joined by one edge. At integer size \(m\ge2\), independently of the past, select one vertex uniformly from the \(m\) existing vertices and then select one of its neighbors uniformly. Attach a new leaf labeled \(m+1\) to the chosen neighbor. All graphs are simple and undirected. On \(D_m\), let \(a,b\) count vertices among \(3,\dots,m\) attached to original vertices \(1,2\), respectively; thus \(a,b\ge0\) and \(a+b=m-2\). For \(m\ge4\), the event \(D_m\setminus S_m\) is exactly \(a,b\ge1\).

The big-Theta statement holds with absolute positive constants for all sufficiently large integer \(n\). It does **not** assert that the normalized expression converges or specify its exact limiting constant.

## Proof

**1. Killed two-center chain.** In a state \((a,b)\) at size \(m=a+b+2\), the probability that the next vertex attaches to original center \(1\), respectively \(2\), is
\[
 p_1(a,b)=\frac{a+1/(b+1)}m,\qquad
 p_2(a,b)=\frac{b+1/(a+1)}m.
\]
Indeed, attachment to center \(1\) occurs if the provisional target is one of its \(a\) leaves, or is vertex \(2\) and chooses center \(1\) among its \(b+1\) neighbors. The remaining probability attaches to a nonseed vertex and permanently destroys \(D\). The two-center chain is therefore substochastic.

**2. Exact star mass and entrance flux.** On the star boundary \(b=0\), \(a=m-2\), the probability of preserving that same boundary at size \(m+1\) is \((m-1)/m\). By symmetry and induction, for each \(m\ge3\),
\[
 \mathbb P(D_m,a=m-2,b=0)=\mathbb P(D_m,a=0,b=m-2)=\frac1{m-1}.
\]
The first transition from either boundary to the interior occurs by attaching to the seed vertex with no new leaves, with conditional probability \(1/[m(m-1)]\). Thus the total mass of **first entrance into the interior at size \(m+1\)** is
\[
 e_m=\frac2{m(m-1)^2},\qquad m\ge3.
\]
The resulting interior states are \((m-2,1)\) and its reversal, each with half this entrance mass.

**3. Lower bound.** While \(a,b\ge1\), the one-step survival probability is
\[
 p_1+p_2=1-\frac{2-1/(a+1)-1/(b+1)}m\ge1-\frac2m.
\]
The chance of continuing within the interior from size \(m+1\) to size \(n\) is therefore at least
\[
 \prod_{j=m+1}^{n-1}\frac{j-2}j
 =\frac{m(m-1)}{(n-1)(n-2)}.
\]
Summing the mutually exclusive first-entrance times \(m=3,\ldots,n-1\) gives
\[
 R_n\ge\sum_{m=3}^{n-1}e_m\frac{m(m-1)}{(n-1)(n-2)}
 =\frac2{(n-1)(n-2)}\sum_{m=3}^{n-1}\frac1{m-1}.
\]
This is the stated harmonic lower bound.

**4. A positive supersolution.** The infinite product for \(g(k)\) converges because \(\sum_{j\ge k}1/[j(j+1)]<\infty\) and all factors are positive. It obeys
\[
 g(k+1)=g(k)\left(1-\frac1{k(k+1)}\right),\qquad
 1\le g(k)\le g(1)=K,\qquad g(k)=1+O(k^{-1}).
\]
Define \(h(a,b)=g(a)g(b)\) for positive integers \(a,b\). Direct substitution into the killed-chain transition proves
\[
\begin{aligned}
 &p_1(a,b)h(a+1,b)+p_2(a,b)h(a,b+1)\\
 &=\left(1-\frac2m\right)h(a,b)
 -\frac{h(a,b)}m\left(\frac1{a(a+1)(b+1)}
 +\frac1{b(b+1)(a+1)}\right)\\
 &\le\left(1-\frac2m\right)h(a,b).
\end{aligned}
\]
On interior states, \(h\ge1\). Iteration from either interior entrance state at size \(m+1\), where \(h=K g(m-2)\), bounds the probability of surviving within the interior until size \(n\) by
\[
 K g(m-2)\prod_{j=m+1}^{n-1}\left(1-\frac2j\right)
 =\frac{K g(m-2)m(m-1)}{(n-1)(n-2)}.
\]
Multiplying by \(e_m\), summing the first entrance times, and applying Step 2 yields the advertised upper bound.

**5. Asymptotic consequence.** Because \(g(k)=1+O(k^{-1})\),
\[
 \sum_{m=3}^{n-1}\frac{g(m-2)}{m-1}=\log n+O(1),\qquad
 H_{n-2}-1=\log n+O(1).
\]
The two bounds prove the logarithm-over-square scale and the displayed liminf/limsup inequalities. The star probability from Step 2 yields the other two conclusions. For reference, with \(\varphi=(1+\sqrt5)/2\), the product can also be evaluated as \(K=\Gamma(1+\varphi)\Gamma(1-1/\varphi)\), by factoring \(j^2+j-1=(j+\varphi)(j-1/\varphi)\) and taking gamma-function ratios.

## Verification

The accompanying standalone `checker.py` independently constructs the full labeled attachment-history distribution through size eight and matches it to the killed two-center recurrence at every marked state. It checks the star identities, exact rational harmonic lower bounds through size 35, the exact one-step supersolution inequality over 576 rational parameter pairs, and three nonexhaustive numerical asymptotic probes. It passes 720 assertions. These computations are finite supporting tests; the infinite result is established by Steps 1–5.

To reproduce: run `python3 checker.py` using standard-library Python. There are no external package dependencies, random seeds, or network calls.

## Relationship to prior work

The original complete-redirection model and its rare star and double-star configurations were analyzed by Redner in *Emergent Network Modularity* (2017, arXiv:1706.01514, especially Sections 2 and 4), including recurrences for **unmarked** two-hub configurations. Cannings and Jordan (2013, arXiv:1303.1052) established general properties of one-step random-walk attachment graphs. Addario-Berry and coauthors' *Random friend trees* (publicly posted March 29, 2024, arXiv:2403.20185) supplies the modern model and its degree/diameter analysis.

The present question fixes **which** edge survives as the two-hub bridge: the original labeled seed edge, rather than a bridge created at an arbitrary later step. This extra chronological requirement makes the first interior-entrance mass \(2/[m(m-1)^2]\), which leads to the new logarithmic-over-square scale. The prior unmarked recurrence and global two-hub estimates do not by themselves identify this marked-seed event. Literature comparison does not establish absolute historical priority.

## Limitations

The bounds determine the sharp order, but not a single limiting constant for \(n^2R_n/\log n\). The theorem is for a labeled two-vertex seed, one-neighbor (complete-redirection) attachment, and an event forcing **all** nonseed vertices to remain leaves. It does not cover multiple-neighbor attachment, arbitrary initial trees, the entire double-star class, or exact unmarked diameter probabilities. Independent review remains to be performed.

## References

1. L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou, G. Lugosi, *Random friend trees*, arXiv:2403.20185 (first posted 2024-03-29), https://arxiv.org/abs/2403.20185.
2. S. Redner, *Emergent Network Modularity*, arXiv:1706.01514 (2017), https://arxiv.org/html/1706.01514v2.
3. C. Cannings, J. Jordan, *Random walk attachment graphs*, arXiv:1303.1052 (2013), https://arxiv.org/abs/1303.1052.
