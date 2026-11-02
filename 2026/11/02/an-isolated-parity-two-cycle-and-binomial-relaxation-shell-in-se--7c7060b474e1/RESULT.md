# An isolated parity two-cycle and binomial relaxation shell in sequential bi-threshold cliques

## Finding

Consider sequential Boolean bi-threshold dynamics on the complete graph with \(n\ge3\) vertices and a fixed permutation update order. At each vertex update, a currently zero vertex becomes one if the total number of ones (including that vertex) is at least \(k\), and a currently one vertex remains one if that total is at least \(k+2\). Here \(k\) is an integer satisfying \(1\le k\le n-2\). Let \(F\) be the map after one full permutation sweep, and let \(T(x)\) denote the smallest nonnegative integer at which \(F^{T(x)}(x)\) belongs to a periodic orbit.

There are exactly two fixed configurations: all zero and all one. The only other periodic orbit is a **single primitive two-cycle**, and it exists **if and only if** \(n\) is odd and \(k=(n-1)/2\). In update-order coordinates, its states are the two alternating words \(0101\cdots0\) and \(1010\cdots1\). Its basin consists solely of those two configurations. No primitive period exceeds two.

Set \(\varepsilon_{n,k}=1\) when \(n\) is odd and \(k=(n-1)/2\), and \(\varepsilon_{n,k}=0\) otherwise. The complete labelled first-periodic-entry census is
\[
\begin{aligned}
\#\{x:T(x)=0\}&=2+2\varepsilon_{n,k},\\
\#\{x:T(x)=1\}&=2^n-2-\binom{n-1}{k},\\
\#\{x:T(x)=2\}&=\binom{n-1}{k}-2\varepsilon_{n,k}.
\end{aligned}
\]
There are no larger entry times. The maximal entry time is two for \(n\ge4\), and one for \(n=3\).

An exact statewise test also holds. Write the initial coordinates in update order as \((x_1,\ldots,x_n)\) and let \(m=\sum_i x_i\). Apart from the four or two periodic configurations just described, \(T(x)=2\) exactly for those with \((m,x_1,x_2)=(k,0,1)\) or \((k+1,1,0)\); all other nonperiodic states have \(T(x)=1\).

For a uniformly chosen initial binary vector, \(\Pr(T=2)=[\binom{n-1}{k}-2\varepsilon_{n,k}]/2^n\). Consequently, if \(k=(n-1)/2+s\sqrt n+O(1)\) along an admissible integer sequence with fixed \(s\in\mathbb R\), then
\[
\sqrt n\,\Pr(T=2)\longrightarrow \frac{e^{-2s^2}}{\sqrt{2\pi}}.
\]
The period-two orbit has probability exactly \(2^{1-n}\) at its exceptional parameters and zero otherwise.

## Assumptions and scope

The graph is the simple complete graph \(K_n\), with each vertex's input its *closed* neighborhood, thus all \(n\) states. The update order is one fixed permutation repeated each sweep. All vertices share the same constant integer thresholds \(k\) and \(k+2\), with \(n\ge3\) and \(1\le k\le n-2\). This restriction guarantees that both constant configurations are fixed. One unit of time means one **complete** sequential sweep, not a single vertex update. The formula is about deterministic labelled states, without equivalence under vertex permutations. Relabeling the vertices converts any update permutation to the order \(1,2,\ldots,n\) without changing the census.

## Proof

**1. Total-population escape.** Work in update order. Let \(M\) be the number of ones just before a local update. If \(M\le k-1\), a zero cannot activate and a one deactivates, so \(M\) never increases thereafter and every remaining vertex becomes zero. If \(M\ge k+2\), a one remains active and a zero activates, so \(M\) never decreases and all remaining vertices become one. Thus if the initial population is outside \(\{k,k+1\}\), one sweep reaches a constant fixed configuration.

At \(M=k\), an encountered zero flips to one and moves the population to \(k+1\), while an encountered one flips to zero and escapes to \(k-1\). At \(M=k+1\), an encountered one flips to zero and moves to \(k\), while an encountered zero flips to one and escapes to \(k+2\). Therefore, staying in the two-level band forces every encountered bit to flip and forces successive input bits to alternate.

**2. Exact two-bit gate.** If the initial total is \(m=k\), then \(x_1=1\) makes the first update escape downward and yields all zeros after one sweep. If \(x_1=0\), the first update raises the population to \(k+1\); should \(x_2=0\), the second update escapes upward and yields all ones. Thus the only remaining candidates for nontrivial behavior have \((m,x_1,x_2)=(k,0,1)\). Likewise, for \(m=k+1\), either \(x_1=0\) causes immediate upward escape or \((x_1,x_2)=(1,1)\) causes downward escape on the second update. Its only remaining candidates have \((m,x_1,x_2)=(k+1,1,0)\).

In either remaining case the first two bits flip to the opposite mixed pair. Hence the image is not a fixed configuration. If at a later local step the population leaves the band, the final population is outside the band and the **next** full sweep reaches a constant configuration, by Step 1. If no later step leaves the band, the entire input word must alternate and the output is its bitwise complement.

**3. Alternating boundary.** A fully alternating word starting with zero has \(\lfloor n/2\rfloor\) ones and can remain in the band only for \(k=\lfloor n/2\rfloor\). A fully alternating word starting with one has \(\lceil n/2\rceil\) ones and can remain in the band only for \(k+1=\lceil n/2\rceil\). For odd \(n=2r+1\), these two conditions agree at \(k=r\); each alternating word maps to the other, producing a primitive two-cycle.

For even \(n=2r\), the starting-zero word requires \(k=r\), whereas its complement starts with one with population \(r=k\), so the first update of the next sweep escapes downward. Similarly, the starting-one word can survive one sweep only when \(k=r-1\); its complement immediately escapes upward during the next sweep. They therefore reach a fixed state on the second sweep, not a cycle. For odd \(n\) and noncentral \(k\), no full alternating word stays in the band. All candidate states consequently either enter the unique alternating two-cycle immediately or reach a fixed configuration by sweep two. The case analysis proves that there are no other periodic states and that the two-cycle has no transient predecessors.

**4. Counting.** The two-bit candidate sets have sizes \(\binom{n-2}{k-1}\) and \(\binom{n-2}{k}\), respectively: in each case the remaining \(n-2\) bits have the indicated total. Pascal's identity makes their union size \(\binom{n-1}{k}\). Exactly two of these states are already periodic in the odd-central case and none otherwise. Thus the size of the second-entry shell is \(\binom{n-1}{k}-2\varepsilon_{n,k}\). The first shell follows by subtracting that quantity and the \(2+2\varepsilon_{n,k}\) periodic states from \(2^n\). At \(n=3,k=1\), the binomial shell vanishes; for every \(n\ge4\) the second shell is positive. This proves all exact counts.

**5. Probabilistic scale.** For uniform independent bits, divide the second-shell count by \(2^n\). In the stipulated central window, the local de Moivre–Laplace estimate for \(\binom{n-1}{k}/2^{n-1}\) is \(\sqrt{2/[\pi(n-1)]}\exp(-2s^2)(1+o(1))\), and the exceptional subtraction \(2/2^n\) is negligible. This gives the displayed limit.

## Verification

The standalone `verify.py` independently implements each local update (recomputing the closed-neighborhood population from the current state), classifies every initial configuration for all \(3\le n\le14\) and every \(1\le k\le n-2\), and checks the statewise test, cycle set, and three binomial formulas. It additionally checks 196 nonidentity-permutation/threshold cases up to \(n=9\). Run `python3 verify.py` using the Python standard library. The recorded output in `VERIFY_OUTPUT.txt` begins `SEQ_BITHRESHOLD_ALL_CHECKS_PASSED` and reports 360456 identity-order initial states and 78 dimension-threshold pairs. Finite enumeration is corroboration, not the proof for arbitrary \(n\).

## Relationship to prior work

Kuhlman, Mortveit, Murrugarra and Kumar introduced the relevant static bi-threshold framework, including the critical difference of two between down- and up-thresholds. Their sequential results construct long cycles on cycles and trees, rather than classifying this complete-graph threshold family. Their synchronous period-two restriction is inapplicable to the sequential update considered here.

Defant studied arbitrary homogeneous Boolean vertex functions on complete graphs and established the extremal number of period-two orbits through binary coding theory. His universal lemma that a complete-graph sequential two-cycle complements all bits is consistent with Step 3, but his extremal characterization supplies neither the unique parity window for this fixed bi-threshold rule nor its exact transient shells. Other subsequent studies of dynamic and multi-threshold networks have different or broader state/threshold mechanisms; inaccessible material leaves a residual historical-equivalence risk, not a proved uniqueness claim.

## Limitations

The theorem assumes **static**, homogeneous critical-gap-two thresholds, a completely connected graph, and a repeated permutation update. It does not cover arbitrary graph topology, block-sequential scheduling, dynamically changing thresholds, or larger threshold gaps. The finite verification is not an independent mathematical audit. The literature search does not rule out equivalent statements in unindexed or inaccessible sources, notably the 2015 generalized multi-threshold treatment by Kuhlman and Mortveit.

## References

1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, first arXiv posting 2011-08-15; open-access DMTCS text, DOI:10.46298/dmtcs.2975. https://arxiv.org/abs/1108.2974 ; https://dmtcs.episciences.org/en/articles/2975/download
2. C. Defant, *Binary Codes and Period-2 Orbits of Sequential Dynamical Systems*, arXiv:1509.03907, first posting 2015-09-13; DMTCS 19:3 (2017), DOI:10.23638/DMTCS-19-3-10. https://arxiv.org/abs/1509.03907 ; https://dmtcs.episciences.org/en/articles/2654/download
3. S. Wu, A. Adiga, H. S. Mortveit, *Limit cycle structure for dynamic bi-threshold systems*, Theoretical Computer Science 559 (2014), 34–41, DOI:10.1016/j.tcs.2014.06.042.
4. C. J. Kuhlman, H. S. Mortveit, *Limit Sets of Generalized, Multi-Threshold Networks*, Journal of Cellular Automata 10 (2015), 161–193 (complete text not retrieved).
