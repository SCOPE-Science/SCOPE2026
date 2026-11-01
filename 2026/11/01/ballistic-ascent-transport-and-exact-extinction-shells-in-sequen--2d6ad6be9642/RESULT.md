# Ballistic ascent transport and exact extinction shells in sequential bi-threshold paths

## Finding
Consider a binary state on a labelled path with vertices read from left to right. Apply one complete sequential sweep of the closed-neighborhood bi-threshold rule with activation threshold \(1\) and persistence threshold \(3\), using the same thresholds at the endpoints. For every length \(n\ge2\), the only recurrent configuration is the all-zero state. More precisely, write
\[
A(x)=\{i\in\{1,\ldots,n-1\}:x_i=0,\ x_{i+1}=1\}.
\]
If \(F_n\) is the complete-sweep map, then
\[
A(F_n(x))=\{i-1:i\in A(x),\ i\ge2\}.
\]
The extinction time \(T_n(x)=\min\{t\ge0:F_n^t(x)=0^n\}\) is exactly
\[
T_n(x)=\begin{cases}0&x=0^n,\\1&A(x)=\varnothing,\ x\ne0^n,\\1+\max A(x)&A(x)\ne\varnothing.\end{cases}
\]
Consequently the complete first-arrival census for all \(2^n\) initial states is
\[
\#\{x:T_n(x)=t\}=\begin{cases}
1&t=0,\\n&t=1,\\(n-t+1)2^{t-2}&2\le t\le n,\\0&\text{otherwise}.
\end{cases}
\]
In particular, the sharp maximum time is \(n\), achieved by precisely \(2^{n-2}\) states, and a uniformly random initial state satisfies
\[
\mathbb E[T_n]=n-2+\frac{n+2}{2^n}.
\]
For each fixed nonnegative integer \(k\), the deficit \(n-T_n\) has, for all \(n\ge k+2\), the *exact* probability
\[
\Pr(n-T_n=k)=\frac{k+1}{2^{k+2}}.
\]
Thus \(n-T_n\) converges in distribution to a negative-binomial variable of shape \(2\) and success probability \(1/2\), with limiting mean \(2\) and variance \(4\).

## Assumptions and scope
The graph is the **open-ended** undirected path \(P_n\) on vertices \(1,\ldots,n\), not a cycle. States lie in \(\{0,1\}^n\). In each sweep, the vertices are updated **once each in ascending order**. The current vertex and its immediate neighbors form its closed neighborhood; neighbors already scanned carry their new bits, while neighbors not yet scanned retain their old bits. A zero switches to one if its closed-neighborhood sum is at least \(1\); a one remains one if that sum is at least \(3\). Out-of-range neighbors are absent, equivalently boundary values zero, and the persistence threshold is **not clipped to the endpoint degree**. The homogeneous thresholds and scan direction are essential; assertions about other update permutations, cycles, or endpoint conventions are not made.

## Proof
Let \(x=(x_1,\ldots,x_n)\) be the pre-sweep word and \(y=F_n(x)\). Define \(y_0=0\) and \(x_{n+1}=0\). At vertex \(i\), the left neighbor has already been updated and the right neighbor has not. Directly from the two thresholds,
\[
y_i=\begin{cases}
y_{i-1}\lor x_{i+1},&x_i=0,\\
y_{i-1}\land x_{i+1},&x_i=1.
\end{cases}\tag{1}
\]
Here \(\lor\) and \(\land\) denote Boolean OR and AND. This holds at both endpoints because their nonexistent neighbors contribute zero.

**Zero-propagation lemma.** If \(x_{i+1}=0\), then \(y_i=0\), for every \(1\le i<n\). Indeed, if \(x_i=1\), the AND case of (1) makes \(y_i=0\). If \(x_i=0\), the OR case gives \(y_i=y_{i-1}\). For \(i=1\), \(y_0=0\); for larger \(i\), the induction hypothesis applied to \(x_i=0\) yields \(y_{i-1}=0\). Also \(y_n=0\): if \(x_n=1\), use the AND case and \(x_{n+1}=0\); otherwise the OR case gives \(y_n=y_{n-1}=0\) by the lemma (or \(y_0=0\) when \(n=1\)).

For \(1\le i\le n-2\), we now have the equivalence
\[
(y_i,y_{i+1})=(0,1)\quad\Longleftrightarrow\quad(x_{i+1},x_{i+2})=(0,1).\tag{2}
\]
For the forward direction, if \(x_{i+1}=1\), the AND case at \(i+1\) gives \(y_{i+1}\le y_i=0\), impossible. Hence \(x_{i+1}=0\), and its OR case implies \(y_{i+1}=x_{i+2}\), so \(x_{i+2}=1\). Conversely, if \((x_{i+1},x_{i+2})=(0,1)\), the lemma gives \(y_i=0\), and the OR case gives \(y_{i+1}=1\). The final possible ascent of \(y\), at index \(n-1\), is excluded by \(y_n=0\). Equation (2) proves the exact leftward shift of ascent positions.

If a word has no ascent, it must be of the form \(1^a0^{n-a}\) with \(0\le a\le n\). Equation (1) then gives \(F_n(x)=0^n\): an initial run of ones is killed starting at \(y_1=0\), and any following run of zeros also stays zero. A nonempty ascent at index \(j\) moves to index \(j-1\) in the next sweep until it reaches index \(1\), when its next sweep removes all ascents. In that last removal sweep, the active pair \(01\) at positions \(1,2\) forces the output's first bit to one by (1), so the output is nonzero. The *following* sweep is zero, proving the time formula, including the distinction between the all-zero word and the \(n\) nonzero ascent-free words.

For \(t\ge2\), write \(j=t-1\). A word has rightmost ascent at \(j\) precisely when its bits at positions \(j,j+1\) are \(01\), its first \(j-1\) bits are arbitrary, and the suffix from position \(j+1\) to \(n\) is ascent-free starting with a one. That suffix has exactly \(n-j\) choices: \(1^a0^{n-j-a}\) with \(1\le a\le n-j\). Hence \(2^{j-1}(n-j)=(n-t+1)2^{t-2}\) words have \(T_n=t\). There are \(n+1\) ascent-free words, one already zero and \(n\) with \(T_n=1\). This proves exhaustive disjointness and the total count.

Summing the time-count formula, or equivalently its tail probabilities, gives \(\sum_xT_n(x)=(n-2)2^n+n+2\), proving the exact mean. With \(t=n-k\) and fixed \(k\le n-2\), division by \(2^n\) gives \((k+1)2^{-k-2}\) exactly. The remaining probability mass, concentrated at times zero and one, is \((n+1)/2^n\to0\). The limiting probability generating function is \(\sum_{k\ge0}(k+1)z^k/2^{k+2}=(2-z)^{-2}\); this gives the claimed negative-binomial law, mean \(2\), and variance \(4\).

## Verification
The proof above covers **all integers** \(n\ge2\). The independent executable checks in `checks/path_exhaustive.py` and `checks/path_exhaustive.cpp` are finite corroboration, not substitutes for that proof. To reproduce: from the containing directory run `python3 checks/path_exhaustive.py`, then `g++ -std=c++17 -O2 checks/path_exhaustive.cpp -o /tmp/path_exhaustive_check && /tmp/path_exhaustive_check`. The first implementation applies the local thresholds to a mutable word and checks every ascent and every arrival time through \(n=15\), totalling 65,532 initial configurations. The independent second implementation uses bitwise neighborhood evaluation, checking all first-arrival times and histograms through \(n=20\), totalling 2,097,148 initial configurations. The exact successful execution outputs are included as `checks/python_output.txt` and `checks/cpp_output.txt`.

## Relationship to prior work
Kuhlman, Mortveit, Murrugarra, and Kumar introduced and studied the relevant bi-threshold dynamics in arXiv:1108.2974v1 (August 15, 2011), including long cycles under sequential updates when the threshold difference equals two; their explicit cycle and branched-tree constructions do not give the open-path state-by-state extinction-time census. The local truth table on interior path vertices is also elementary cellular automaton **Rule 178**. Donoso-Leiva, Goles, Ríos-Wilson, and Sené (arXiv:2509.07797) treat Rule 178 on **periodic rings**, proving that a collection of sequential scan orders can lead configurations to a fixed point. That covering statement does not imply a uniform fixed left-to-right open-path rule, nor the exact extinction-shell counts or the limiting deficit law; indeed the all-ones configuration is fixed on their periodic ring but dies immediately on the open path here. Prior work on update-order cycle equivalence addresses recurrent cycle structures rather than individual transient depths. These distinctions are mathematical scope comparisons, not an assertion of exhaustive global novelty.

## Limitations
The result does not cover other update permutations, parallel updating, periodic boundary conditions, endpoint thresholds clipped to degree, randomized initial-state distributions, or arbitrary graphs. The negative-binomial conclusion is a limiting law for uniform independent initial bits; the finite law is given exactly above. The novelty assessment is based on accessible records and inspected literature, and unindexed equivalent treatments remain possible.

## References
1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1 (first public August 15, 2011), https://arxiv.org/abs/1108.2974 .
2. I. Donoso-Leiva, E. Goles, M. Ríos-Wilson, S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797, https://arxiv.org/abs/2509.07797 .
3. M. Macauley, H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, https://arxiv.org/abs/0802.4412 .
