# Sharp cyclic-gap thresholds for digit-appending walks on periodically perturbed powers

## Finding

Fix an integer base \(b\ge2\), a positive period \(h\), and integers \(u_0,\ldots,u_{h-1}\). Extend the corrections by \(u_{n+h}=u_n\), and consider the eventually positive, eventually strictly increasing integer sequence
\[
a_n=b^n+u_{n\bmod h}\qquad(n\ge0).
\]
Let \(S_0=\{r\in\mathbb Z/h\mathbb Z:u_r=0\}\) and \(S_{-1}=\{r\in\mathbb Z/h\mathbb Z:u_r=-1\}\). For a nonempty subset \(S\) of residues, its *largest circular gap* \(g(S)\) is the maximum positive difference between consecutive members in cyclic increasing order, including the wraparound gap. A singleton has gap \(h\); define \(g(\varnothing)=+\infty\). Set
\[
N_*=\min\{g(S_0),g(S_{-1})\}.
\]
**Theorem.** For every integer \(N\ge1\), an infinite walk obtained by appending between one and \(N\) base-\(b\) digits at every step exists if and only if \(N\ge N_*\). Thus the least such cap is precisely \(N_*\), with \(N_*=+\infty\) interpreted as impossibility for any finite cap. If both distinguished sets are empty, no infinite walk exists even when the number of appended digits is unbounded.

Furthermore, put \(U=\max_{0\le r<h}|u_r|\), and choose an integer \(M\ge0\) with \(b^M>4(U+1)\). If \(N<N_*\), **every** walk starting at any positive term has at most \(M+h-1\) steps, independently of the starting index. The threshold \(N_*\) depends only on the circular positions of zero and minus-one corrections, not on \(b\) or the sizes of the remaining corrections.

## Assumptions and scope

A walk is an increasing sequence of indices \(m_0<m_1<\cdots\) such that all chosen terms are positive, and for each \(j\) there are integers \(k_j=m_{j+1}-m_j\ge1\), \(t_j\ge1\), and \(0\le d_j<b^{t_j}\) satisfying
\[
a_{m_{j+1}}=b^{t_j}a_{m_j}+d_j.
\]
The appended block may begin with zero, as in the standard digit-appending convention. An at-most-\(N\)-digit walk requires \(1\le t_j\le N\). An infinite walk need only exist from *some* positive term, not from every starting residue.

This family obeys an integral linear recurrence with characteristic polynomial dividing \((X-b)(X^h-1)\). Repetitions among the corrections, nonminimal periods, negative corrections, and the zero correction are all allowed.

## Proof

**Step 1: Uniform eventual rigidity, including unbounded append lengths.** Let \(m\ge M\), \(k,t\ge1\), and write \(p=b^t\), \(q=b^k\). The putative appended integer is
\[
\frac{a_{m+k}-b^t a_m}{b^t}=b^m(b^{k-t}-1)+\frac{u_{m+k}}{b^t}-u_m.
\]
Since \(b^m>4(U+1)\), if \(k>t\) the right side is at least \(b^m-U-U/b>1\). If \(k<t\), it is at most \(-b^m(1-1/b)+U+U/b<0\). Therefore the digit condition \(0\le a_{m+k}-b^t a_m<b^t\) forces \(k=t\) for every starting index \(m\ge M\), regardless of the size of \(t\). Conversely, if \(k=t\), the digit condition is exactly
\[
0\le u_{m+t}-b^t u_m<b^t.\tag{1}
\]
Because \(b^M>4(U+1)\), all terms with index at least \(M\) are positive.

**Step 2: Cycles can use only zero or minus-one corrections.** Equation (1) defines a finite directed graph on the \(h\) residue states, with an edge \(r\to r+t\pmod h\) for each allowed \(t\) satisfying the inequality. For any valid edge, if \(u_r\ge1\), then \(u_{r+t}\ge b^t u_r\ge2u_r\): positive corrections strictly increase along any subsequent path. If \(u_r\le-2\), then \(u_{r+t}<b^t(u_r+1)\le2(u_r+1)\le u_r\): corrections below minus one strictly decrease along any subsequent path. If \(u_r=0\), then \(u_{r+t}\ge0\), so a path cannot enter the negative correction states. If \(u_r=-1\), then \(u_{r+t}<0\), so a path cannot enter nonnegative correction states. Consequently, every directed cycle has correction identically \(0\) or identically \(-1\). Conversely, for two states of equal correction \(0\) or equal correction \(-1\), every positive index increment \(t\) connecting them satisfies (1), with digit block respectively \(d=0\) or \(d=b^t-1\).

**Step 3: Circular-gap criterion.** For any nonempty \(S\subseteq\mathbb Z/h\mathbb Z\), consider the directed graph with arrows \(r\to r+t\pmod h\) for \(r,r+t\in S\) and \(1\le t\le N\). It has a directed cycle if and only if \(N\ge g(S)\). For sufficiency, traverse all members of \(S\) in increasing cyclic order, using their positive circular gaps as increments; the largest is \(g(S)\). For necessity, if \(N<g(S)\le h\), lift any hypothetical directed cycle to a strictly increasing walk on the integers, with total displacement a positive multiple of \(h\). It must traverse each translate of a maximal empty circular interval of length \(g(S)-1\). Since no intermediate member of \(S\) is available, at least one successive positive jump has length \(g(S)\) or more, contradicting \(t\le N\). This also covers singleton sets, for which the shortest return increment is \(h\).

Combining Steps 2 and 3, the eventual residue graph has a directed cycle exactly when \(N\ge\min\{g(S_0),g(S_{-1})\}\). A cycle can be repeated indefinitely, choosing an initial index \(m\ge M\) in its starting residue class and using the legitimate all-zero or all-\((b-1)\)-digit blocks from Step 2. Conversely, an infinite walk eventually lies above \(M\), producing an infinite path in a finite residue graph and hence a directed cycle. This proves the exact existence and nonexistence assertions, including the case of unbounded digits when \(S_0=S_{-1}=\varnothing\).

**Step 4: Uniform finite-walk bound.** If \(N<N_*\), the eventual graph is acyclic; any path on its \(h\) vertices has at most \(h-1\) edges. Each step before reaching an index at least \(M\) strictly increases the index by at least one, so there are at most \(M\) such steps from any starting index \(m_0\ge0\). Thus the entire walk has at most \(M+h-1\) steps. (The bound is sufficient, not asserted sharp.)

## Verification

The accompanying dependency-free `verify.py` performs exhaustive independent finite graph-cycle versus circular-gap comparisons for all disjoint zero/minus-one placements through period \(10\), and randomized comparisons for periodic integer corrections and bases \(2,3,7,10\). It independently checks the exact digit-append identity over many finite indices and append lengths. Its successful run printed `VERIFY_OK subset_graph_comparisons=930021 sampled_recurrence_and_graph_checks=825308`. These checks do not substitute for the all-parameter proof above.

For a concrete nontrivial instance, \(h=5\) and correction tuple \((-1,3,-1,5,7)\) give \(S_{-1}=\{0,2\}\) with circular gaps \(2,3\), hence \(N_*=3\). With no correction \(0\) or \(-1\), infinite walks are impossible even without a digit budget.

## Relationship to prior work

Kominers (arXiv:2512.06446v1, first public December 6, 2025) proves uniform termination for bounded-digit walks along Fibonacci numbers and specified Lucas sequences, using recurrence rigidity. Its Theorems 3.1 and 4.2 treat a noninteger dominant root and Lucas-sequence hypotheses, not a dominant root *equal to the appending base* together with arbitrary periodic integer corrections. The theorem here characterizes exactly that resonant family and gives a sharp threshold determined by two correction level sets.

Miller, Peng, Popescu, and Wattanawanichkul (arXiv:2204.08138) analyze bounded digit-appending walks along Fibonacci numbers. The wider number-theory-walk investigation of Miller and collaborators (arXiv:2010.14932) addresses primes, square-free integers, perfect squares, and Fibonacci sequences. Neither paper states this cyclic-gap classification or a uniform cap for all periodic perturbations of powers.

## Limitations

The family of recurrences is restricted to one expanding characteristic root equal to the base and bounded *periodic integer* corrections; results for general bounded aperiodic perturbations or other expanding roots are not claimed. Existence means existence from some sufficiently large starting term. The finite upper bound \(M+h-1\) is generally not optimized. The proof is self-contained; independent external mathematical validation has not been performed. Earlier implicit versions of the classification cannot be categorically excluded by literature searches.

## References

1. S. D. Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446v1, publicly submitted 2025-12-06, https://arxiv.org/abs/2512.06446.
2. S. J. Miller, F. Peng, T. Popescu, and N. Wattanawanichkul, *Walking to Infinity on the Fibonacci Sequence*, arXiv:2204.08138, https://arxiv.org/abs/2204.08138.
3. S. J. Miller, F. Peng, T. Popescu, J. M. Siktar, N. Wattanawanichkul et al., *Walking to Infinity Along Some Number Theory Sequences*, arXiv:2010.14932, https://arxiv.org/abs/2010.14932.
