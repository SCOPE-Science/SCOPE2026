# Exact oscillatory basins for a balanced complete-graph majority–minority system

## Finding
Consider a complete graph on \(2k\) labelled vertices, \(k\ge1\), split into \(k\) **conformists** and \(k\) **contrarians**. All states are binary. At every synchronous update, a conformist adopts the strict majority state of its \(2k-1\) neighbors, and a contrarian adopts the strict minority state. There are no ties because each degree is odd. Let \(T(x)\) denote the least nonnegative first-entry time into a periodic orbit of the global map \(F\).

Put
\[
 B_k=\begin{cases}\displaystyle\binom{k}{k/2}^2,&k\text{ even},\\0,&k\text{ odd},\end{cases}
 \qquad C_k=\binom{2k}{k}.
\]
There are **no fixed states**, exactly **one primitive period-four orbit**, and exactly \(B_k/2\) distinct primitive period-two orbits. The latter occur precisely at states with exactly \(k/2\) ones among the conformists and exactly \(k/2\) ones among the contrarians (requiring even \(k\)). No nonperiodic state ever enters a two-cycle. Every other state eventually enters the unique four-cycle, in at most two updates. The exact first-entry census is
\[
 \#\{T=0\}=4+B_k,\qquad
 \#\{T=1\}=4^k-C_k-2,\qquad
 \#\{T=2\}=C_k-2-B_k.
\]
All other entry-time classes are empty. The upper bound two is attained exactly when \(k\ge3\). In particular the entire system satisfies \(F^6=F^2\) for every \(k\ge1\).

If initial bits are independent \(\operatorname{Bernoulli}(p)\), then the probability of eventually entering a period-two orbit is exactly
\[
 \Pr_p(\text{period two})=B_k[p(1-p)]^k.
\]
For even \(k\to\infty\) and fixed real \(s\), taking \(p=1/2+s/\sqrt{k}\) gives the sharp critical-window law
\[
 \Pr_p(\text{period two})\sim\frac{2}{\pi k}e^{-4s^2}.
\]
For odd \(k\), this probability is identically zero. This parity contrast concerns the **basin of attraction**, not merely the existence of a cycle.

## Assumptions and scope
The graph is loopless and complete; conformist and contrarian groups each have exactly \(k\) vertices. At every step all vertices update simultaneously using their neighbors **excluding themselves**. Bits \(0\) and \(1\) are interchangeable. A primitive period is the least positive return time of a periodic configuration. Initial configurations are labelled; only temporal rotation identifies states into one periodic orbit. The Bernoulli law is independent across all \(2k\) vertices. The asymptotic statement runs through even positive integers \(k\), with fixed \(s\) and sufficiently large \(k\) to keep \(p\) in \([0,1]\).

## Proof
Write a state as \((X,Y)\), with \(X,Y\in\{0,1\}^k\) giving respectively the conformist and contrarian bits. Put \(a=|X|\), \(b=|Y|\) and \(r=a+b\). A vertex currently in state one sees \(r-1\) ones among its neighbors, whereas a vertex currently in state zero sees \(r\). Strict majority means at least \(k\) neighboring ones; strict minority means fewer than \(k\) neighboring ones. Accordingly, direct evaluation of **both current-bit cases in each group** yields the exact update identity
\[
 F(X,Y)=\begin{cases}
 (\mathbf0,\mathbf1),&r<k,\\
 (\overline X,Y),&r=k,\\
 (\mathbf1,\mathbf0),&r>k.
 \end{cases} \tag{1}
\]
Here the bars are bitwise complementation and bold zero/one denote all-constant length-\(k\) words. Equation (1) is exhaustive and remains valid for \(k=1\).

Name four configurations \(U=(\mathbf0,\mathbf1)\), \(W=(\mathbf1,\mathbf1)\), \(V=(\mathbf1,\mathbf0)\), and \(Z=(\mathbf0,\mathbf0)\). Equation (1) gives
\[
 U\longmapsto W\longmapsto V\longmapsto Z\longmapsto U.
\]
The four states are distinct, establishing a primitive four-cycle. Every configuration with \(r<k\) is sent to \(U\) and every configuration with \(r>k\) is sent to \(V\).

Now take a configuration with \(r=k\). Its first successor is \((\overline X,Y)\), with total number of ones
\[
 r'=(k-a)+b=2(k-a).
\]
If \(a<k/2\) then \(r'>k\), and the second update reaches \(V\). If \(a>k/2\) then \(r'<k\), and the second update reaches \(U\). If \(a=k/2\), which requires even \(k\), the first successor still has \(r'=k\), so the next update complements \(X\) again and restores the original state. As \(X\ne\overline X\) for any nonempty binary word, every such state has **least period two**, not one. Conversely no other configuration can belong to a period-two orbit or have a period-two eventual attractor, because it enters the displayed four-cycle. This also rules out fixed states.

There are exactly \(\binom{k}{k/2}^2=B_k\) such two-periodic labelled configurations when \(k\) is even; each primitive orbit consists of two states. The rest of the \(4^k\) configurations have the four-cycle as attractor. The periodic states are precisely its four members and the \(B_k\) two-periodic states. Among the \(\binom{2k}{k}=C_k\) configurations with \(r=k\), precisely two (\(U,V\)) lie on the four-cycle, and \(B_k\) lie on two-cycles; all other states in this layer have first-entry time two. Outside that layer, exactly \(W,Z\) are already periodic, while every other state has first-entry time one. This gives all three stated census formulas and the global iterate identity. For \(k=1,2\) the time-two class is empty; it is nonempty for \(k\ge3\), as follows from the strict inequality \(C_k>2+B_k\) there (or by explicit states with \(r=k\), \(0<a<k\), \(a\ne k/2\)).

Finally, period-two attraction requires \(|X|=|Y|=k/2\), and these two independent binomial events each have probability \(\binom{k}{k/2}p^{k/2}(1-p)^{k/2}\). Squaring proves the probability formula. For even \(k\), Stirling's formula yields
\[
 \binom{k}{k/2}^2/4^k\sim 2/(\pi k).
\]
At \(p=1/2+s/\sqrt{k}\), we have \(4p(1-p)=1-4s^2/k\), whose \(k\)-th power tends to \(e^{-4s^2}\). Multiplication gives the critical-window limit. No finite simulation is needed for any infinite-family assertion.

## Verification
The included standalone Python 3 program `verify.py` implements the original vertexwise rule by counting each vertex's other neighbors, independently of the three-case quotient identity (1). It enumerates all \(4^k\) labelled states for each \(1\le k\le8\) (87,380 states in total), directly determines first periodic entry and least period, and compares the counts and cycle numbers to the closed formulas. `verification_output.txt` records successful checks. This finite computation is a regression test of the all-size proof above, not its justification.

## Relationship to prior work
Cannings's 2009 study introduced and analyzed complete-network majority/minority games. Its previously reported period restrictions and balanced-population four-cycle phenomenon are **not** claimed new. Haslegrave and Cannings (2016, introduction) explicitly credit Cannings with the complete-graph restriction to periods one, two and four and with a special balanced case for four-cycles. Cao, Qin, Yang and Zhang (2013) study conformist/rebel synchronous best-response dynamics with the same strict-neighbor choice on an arbitrary graph and principally analyze graph-structure conditions for recurrent fashion cycles. The contribution isolated here is the **exact number of microscopic two-cycle orbits, their complete basins, the first-entry-time census, and the parity-dependent and critical-window probabilistic law** under a balanced complete-graph assignment. The accessible inspected statements do not imply those counts; a full-document overlap comparison with Cannings (2009) remained unavailable, so historic duplication cannot be ruled out.

## Limitations
The theorem concerns only equal-sized groups on a loopless complete graph with synchronous strict majority/minority updates. It does not classify arbitrary group proportions, heterogeneous thresholds, random update orders, stochastic mistakes, or tie behavior on odd-order graphs. The original Cannings (2009) conference full text could not be inspected completely; its treatment of exactly this graph and agent rule is a material residual originality risk. No claim of independent validation or historical uniqueness is made.

## References
1. C. Cannings, *The majority and minority models on regular and random graphs*, GameNets (2009), DOI: 10.1109/GAMENETS.2009.5137464. Public bibliographic record: https://eudl.eu/doi/10.1109/gamenets.2009.5137464 (dated 2009-06-26).
2. J. Haslegrave and C. Cannings, *Majority dynamics with one nonconformist*, arXiv:1606.05496 (first posted 2016-06-17), later *Discrete Applied Mathematics* 219 (2017), 32–39. Open accepted manuscript: https://wrap.warwick.ac.uk/id/eprint/84436/7/WRAP-majority-dynamics-nonconformist-Haslegrave-2017.pdf.
3. Z.-G. Cao, C.-Z. Qin, X.-G. Yang and B.-Y. Zhang, *A Heterogeneous Network Game Perspective of Fashion Cycle*, working paper, 2013, DOI: 10.2139/ssrn.2260025; accessible text: https://studylib.net/doc/8848534/a-heterogeneous-network-game-perspective-of-fashion-cycle-%E2%88%97.
