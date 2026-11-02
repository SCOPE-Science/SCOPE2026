# Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles

## Finding

Let \(n\ge3\) be an integer and let \(F\) be one complete sequential sweep, in the cyclic vertex order \(1,2,\ldots,n\), of the uniform bi-threshold Boolean network on \(C_n\) with closed-neighborhood activation threshold \(1\) and persistence threshold \(3\). Then

\[
F(\{0,1\}^n)=\mathcal S_n:=\{x\in\{0,1\}^n:x_n=x_1\}.
\]

Under the identification \(\mathcal S_n\cong\{0,1\}^{n-1}\) that drops the repeated last coordinate, the restriction of \(F\) is the one-position left cyclic rotation. Thus exactly \(2^{n-1}\) configurations are periodic; the other \(2^{n-1}\) enter a periodic orbit **after exactly one sweep**. The two fixed configurations are constant. If \(d\mid n-1\), the number of primitive temporal \(d\)-cycles is

\[
N_d=\frac1d\sum_{e\mid d}\mu(d/e)2^e,
\]

and no other primitive periods occur. Here \(\mu\) is the ordinary Möbius function.

There is also a complete **individual attraction-basin formula**. Each constant fixed point has a basin of size \(n\). For a nonconstant cycle, identify its states with the rotations of its primitive binary word of length \(d\). If the cyclic runs of this primitive word have lengths \(s_1,\ldots,s_{2q}\), the number of initial configurations eventually entering that particular orbit is

\[
\boxed{\operatorname{Bas}(w)=\sum_{j=1}^{2q}\frac{s_j(s_j+1)}2.}
\]

Among nonconstant primitive cycles of any fixed realizable period \(d\ge2\), the sharp maximum basin size is \(1+d(d-1)/2\), attained exactly by necklaces with one bit different from all the others (up to complement and rotation). All these statements concern labelled configurations, and each temporal cycle is counted once.

## Assumptions and scope

The graph is the simple undirected labelled cycle with edges \(i\sim i+1\) modulo \(n\). The state at vertex \(i\) is one bit. At its visit, vertex \(i\) reads the **current** bits in its closed neighborhood, with earlier visited vertices already updated and later vertices not yet updated. A zero changes to one if the three-bit population is at least \(1\); a one stays one if the population is at least \(3\), and otherwise changes to zero. Every vertex is visited exactly once in the fixed order \(1,2,\ldots,n\) during each sweep, and sweeps are repeated indefinitely. In particular, this is **not** a simultaneous update and not a majority rule. When \(n=3\), the two neighbors are the other two distinct vertices.

The attraction basin of a periodic orbit is the set of initial bitstrings whose forward trajectory eventually enters the orbit; the orbit states themselves belong to its basin. A cyclic run is a maximal constant-bit block in a circular word. For a nonconstant circular binary word the run count is even. The primitive word of a temporal orbit is the unique shortest repeat block, up to cyclic rotation, of the corresponding \((n-1)\)-bit word.

## Proof

Write the input as \(x=(x_1,\ldots,x_n)\), and the state after a full sweep as \(y=(y_1,\ldots,y_n)\). For two currently visible neighbors \(a,b\) and current central bit \(c\), the local rule is

\[
T(a,c,b)=\begin{cases}a\lor b,&c=0,\\a\land b,&c=1.\end{cases}
\]

Equivalently, \(T(a,c,b)=a\) if \(c=b\), and \(T(a,c,b)=b\) if \(c\ne b\); in the first equality, \(a\) is the *other* neighbor, not the central bit. Indeed, when \(c=b=0\), the rule returns \(a\), and when \(c=b=1\), it also returns \(a\). For the sequential sweep this gives

\[
y_1=T(x_n,x_1,x_2),\quad
y_i=\begin{cases}y_{i-1},&x_i=x_{i+1},\\x_{i+1},&x_i\ne x_{i+1}\end{cases}\quad(2\le i\le n-1),\quad
y_n=T(y_{n-1},x_n,y_1).
\]

Inductively, \(y_i\in\{y_1,x_{i+1}\}\) for \(2\le i\le n-1\). In particular \(y_{n-1}\in\{y_1,x_n\}\). If \(x_n=y_1\), then \(y_{n-1}=y_1\) and the last update gives \(y_n=y_1\). If \(x_n\ne y_1\), the last update gives \(y_n=y_1\) regardless of \(y_{n-1}\). Hence the entire image lies in \(\mathcal S_n\).

Now suppose \(x\in\mathcal S_n\), so \(x_n=x_1\). The first update gives \(y_1=x_2\). If \(y_{i-1}=x_i\), the displayed recurrence gives \(y_i=x_{i+1}\) whether or not \(x_i=x_{i+1}\). Therefore

\[
F(x_1,x_2,\ldots,x_{n-1},x_1)
=(x_2,x_3,\ldots,x_{n-1},x_1,x_2).
\]

This is an invertible left rotation of the first \(n-1\) bits, proving \(F(\mathcal S_n)=\mathcal S_n\). All and only states in \(\mathcal S_n\) are periodic. Every other state enters \(\mathcal S_n\) in one sweep, and cannot itself be periodic. Thus the first-periodic-entry bound is sharp for every \(n\ge3\). Exact-period \(d\) points of a binary rotation of length \(n-1\) number \(\sum_{e\mid d}\mu(d/e)2^e\) for each divisor \(d\) of \(n-1\); dividing by \(d\) gives the orbit census. Every such period occurs, witnessed by the primitive word consisting of \(d-1\) zeros followed by one one when \(d\ge2\), or a constant word when \(d=1\).

It remains to count basins. Fix \(y\in\mathcal S_n\) and put \(a=y_1\). There is exactly one predecessor of \(y\) *inside* \(\mathcal S_n\), by the rotation bijection. Any predecessor \(x\notin\mathcal S_n\) has \(x_1\ne x_n\); the first update then gives \(y_1=x_n=a\), so necessarily \(x_1=1-a\) and \(x_n=a\). Scan the input string \(x_2,\ldots,x_n\). If there is no transition from a bit to a different bit, all its bits equal \(a\), and the intermediate outputs are constant \(a\). Otherwise let \(j\in\{2,\ldots,n-1\}\) be the index of its first transition, \(x_j\ne x_{j+1}\). The displayed recurrence implies \(y_i=a\) for \(2\le i<j\), and \(y_i=x_{i+1}\) for \(j\le i\le n-1\). (Once the first transition occurs, that identity persists at later updates.) Therefore any nonperiodic predecessor requires \(y_{n-1}=a\).

If \(y_{n-1}\ne a\), it has none. If \(y_{n-1}=a\) but \(y\) is not constant, let \(h\in\{2,\ldots,n-2\}\) be the first position at which \(y_h\ne a\). Exactly the positions \(j=2,\ldots,h\) may be the first input transition; each determines a *unique* predecessor: before \(j\) the input tail is constant and opposite to its value at \(j+1\), and after \(j\) it is determined by \(x_{i+1}=y_i\). Thus there are \(h-1\) nonperiodic predecessors. If \(y\) is constant, the first transition can be any \(j=2,\ldots,n-1\), or be absent; thus it has \(n-1\) nonperiodic predecessors. Including its unique periodic predecessor gives the exact one-step fiber size

\[
r(y)=|F^{-1}(y)|=
\begin{cases}
1,&y_{n-1}\ne y_1,\\
h,&y_{n-1}=y_1\text{ and }h=\min\{2\le i\le n-2:y_i\ne y_1\}\text{ exists},\\
n,&y_1=y_2=\cdots=y_{n-1}.
\end{cases}
\]

Every state is either already periodic or maps to a periodic state after one sweep, so the attraction basin of any orbit \(\mathcal O\) has size \(\sum_{y\in\mathcal O}r(y)\). For a constant orbit, this is \(n\). For a nonconstant primitive word \(w\) of length \(d\), the orbit consists of all its \(d\) rotations. Consider any cyclic run of length \(s\) in \(w\). The rotation starting at the **first** bit of that run has different first and last bits and hence fiber size \(1\). The rotations starting at its second through last bits have fiber sizes \(s,s-1,\ldots,2\), respectively, by the displayed fiber formula. That run contributes \(1+2+\cdots+s=s(s+1)/2\). Summing over the runs gives the basin formula.

Finally, since a nonconstant binary circular word has at least two runs of positive lengths summing to \(d\), convexity of \(s(s+1)/2\) shows that the sum is at most \(1+d(d-1)/2\), with equality only for two runs of lengths \(1\) and \(d-1\). These words have primitive period \(d\), so the bound is attained and its equality condition is exact.

## Verification

The standalone scripts `checks/check_python.py` and `checks/check_cpp.cpp` implement the local sequential update directly (rather than using the rotation formula). The first exhaustively checks all inputs for \(3\le n\le12\), including one-step image, predicted fibers, primitive periods, individual run-basin counts and the total basin partition. The second independently exhausts \(3\le n\le18\), including physical updates, image cardinality, preimage counts, rotation on the image and total orbit basins. Outputs are embedded as `checks/python_results.txt` and `checks/cpp_results.txt`. Run the scripts from their own package paths; compile the C++ source with a C++17 compiler and execute it. Both emit `PASS`. No finite computation is used as an infinite proof.

## Relationship to prior work

Kuhlman, Mortveit, Murrugarra and Kumar's *Bifurcations in Boolean Networks* (arXiv:1108.2974, publicly deposited August 15, 2011) presents the full phase space of the single case \(n=4\) in Example 2.1 and Figure 1, and exhibits one \(n-1\)-cycle for general \(n\) in Proposition 3.6, using this exact graph, update order and threshold pair. They do **not** give the full recurrent set, the one-sweep image identity, primitive-period multiplicities for arbitrary \(n\), or the run-dependent basin formula for all sizes. The present theorem strengthens that specific existence example into a complete all-input classification. Macauley and Mortveit's cycle-equivalence theorem for sequential graph dynamics (arXiv:0802.4412) compares update orders at the orbit-structure level without supplying this instance's counts or basins. Defant's study of period-two orbits on complete graphs with arbitrary update functions (arXiv:1509.03907) has a different underlying graph and question.

## Limitations

Only the single cyclic update order and the exact threshold pair \((1,3)\) are covered. Other permutations of the cycle vertices need not produce the same labelled map, and no statement about arbitrary update orders follows. The result is a proof about deterministic finite Boolean dynamics, not a claim about noisy or continuous-time threshold models. No claim of general novelty beyond the cited and searched literature is made: related work that is not indexed or not easily discoverable remains a possible overlap risk.

## References

1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, initially public August 15, 2011; see the definitions in Section 2 and Proposition 3.6. https://arxiv.org/abs/1108.2974
2. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, 2008. https://arxiv.org/abs/0802.4412
3. C. Defant, *Binary Codes and Period-2 Orbits of Sequential Dynamical Systems*, arXiv:1509.03907, initially public September 13, 2015. https://arxiv.org/abs/1509.03907
