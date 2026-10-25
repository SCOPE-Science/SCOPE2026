# Exact parity-walk kernel and sharp extinction for even-branching rooted trees

## Finding

**Theorem (parity-walk kernel).** Let \(T\) be any finite, nonempty rooted tree in which every vertex has either zero children or a **positive even** number of children. Let \(A\) be the loopless, undirected adjacency matrix with entries in \(\mathbb F_2\). For vertices \(u,v\), write \(i=d(o,u)\), \(j=d(o,v)\), \(b=d(o,\operatorname{lca}(u,v))\), and \(\delta=i+j-2b\), where \(o\) is the root and \(\operatorname{lca}\) is the unique lowest common ancestor. Then the full time-generating kernel of synchronous neighbour-XOR dynamics is the finite polynomial

\[
\sum_{t\ge0}(A^t)_{uv}z^t
=z^{\delta}\sum_{s=0}^{b}z^{2s}
\quad\text{in }\mathbb F_2[z].
\]

In particular, the parity of the number of length-\(t\) walks from \(u\) to \(v\) is odd **if and only if** \(\delta\le t\le i+j\) and \(t\equiv\delta\pmod2\). Thus *all* walk parities depend only on the two vertex depths and their lowest common ancestor depth, not on the numbers or arrangement of the even branches.

Let \(h=\max_{v\in V(T)}d(o,v)\) and let \(\ell\in\mathbb F_2^{V(T)}\) be the indicator of the vertices at depth \(h\). Then

\[
A^{2h}=\ell\ell^{\mathsf T}\ne0,
\qquad A^{2h+1}=0.
\]

Consequently **every** initial binary configuration extinguishes within \(2h+1\) synchronous updates, this universal bound is attained, and exactly \(2^{|V(T)|-1}\) of the \(2^{|V(T)|}\) initial configurations require all \(2h+1\) updates (equivalently, initially have odd parity on the vertices at depth \(h\)). The case \(h=0\) is included: the sole vertex has zero neighbours and vanishes after one update.

## Assumptions and scope

The tree is finite, nonempty, simple, undirected and loopless. Its root is fixed and depth is the number of edges from the root. The children of a vertex are its neighbours one level farther from the root. Every nonleaf has **strictly positive even** child count; child counts, heights and branching multiplicities otherwise vary arbitrarily. A state \(x_t\in\mathbb F_2^{V(T)}\) evolves by \(x_{t+1}=Ax_t\); no self-input and no threshold or randomization is used. Arithmetic, coefficients and power-series identities are throughout characteristic two. Time \(t\) ranges over all nonnegative integers. If this even-child hypothesis is dropped, the formula and extinction need not hold: on the two-vertex path rooted at an endpoint, the adjacency update exchanges the two states indefinitely.

## Proof

For \(r\ge0\), set \(S_r(z)=\sum_{s=0}^{r}z^{2s}\) and put \(S_{-1}(z)=0\). The elementary identity

\[
S_r+z^2S_{r-1}=1
\qquad(r\ge0)
\]

holds in \(\mathbb F_2[z]\) because all the intermediate powers cancel pairwise.

Fix a target vertex \(v\). Define for each vertex \(u\) the proposed resolvent column

\[
g_u(z)=z^{d(u,v)}S_{d(o,\operatorname{lca}(u,v))}(z).
\]

We prove \((I+zA)g=e_v\) by checking its equation \(g_u+z\sum_{w\sim u}g_w=\mathbf1_{u=v}\) at each vertex.

**Case 1: \(u\) lies off the unique root-to-\(v\) path.** Its parent \(p\) has \(g_u=zg_p\), since the last common ancestor with \(v\) does not change when moving from \(p\) to \(u\). Each child \(w\) similarly has \(g_w=zg_u\). There is an even number of children; their sum is therefore zero in characteristic two. Hence \(g_u+z\sum_{w\sim u}g_w=g_u+zg_p=0\).

**Case 2: \(u\) is a proper ancestor of \(v\).** Write \(r=d(o,u)\) and \(q=d(u,v)>0\). Then \(g_u=z^qS_r\). Its one child toward \(v\) has \(g=z^{q-1}S_{r+1}\). All other children are off the path; their number is odd, because the *total* number of children is even, and each has \(g=z^{q+1}S_r\). For \(r>0\), the parent contributes \(z^{q+1}S_{r-1}\); for \(r=0\), this term vanishes by \(S_{-1}=0\). Thus the left side is

\[
z^q\bigl(S_r+S_{r+1}+z^2S_{r-1}+z^2S_r\bigr)
=z^q(1+1)=0.
\]

**Case 3: \(u=v\).** Here \(g_v=S_r\) for \(r=d(o,v)\). Each child has \(g=zS_r\), so the sum over the even number of children cancels. If \(r>0\), the parent has \(g=zS_{r-1}\), while for \(r=0\) there is no parent and \(S_{-1}=0\). Consequently

\[
g_v+z\sum_{w\sim v}g_w=S_r+z^2S_{r-1}=1.
\]

The three cases exhaust all vertices, establishing \((I+zA)g=e_v\). Over the formal power series ring \(\mathbb F_2[[z]]\), the matrix \(I+zA\) has the unique inverse \(\sum_{t\ge0}z^tA^t\), because the alternating-sign geometric series becomes the all-positive series in characteristic two. Therefore the polynomial column \(g\) equals this actual resolvent column. Taking coefficients proves the asserted kernel, for every \(u,v,t\), not just for finitely many computed times.

Since the highest degree in \(z^{\delta}S_b\) equals \(\delta+2b=i+j\le2h\), every coefficient of \(A^t\) with \(t>2h\) is zero. At \(t=2h\), a coefficient is nonzero precisely when \(i=j=h\), because \(i,j\le h\), and its coefficient there is one. Thus \(A^{2h}=\ell\ell^{\mathsf T}\) and \(A^{2h+1}=0\). Because \(h\) is the maximum attained depth, \(\ell\ne0\), and the outer product is nonzero even in characteristic two. For any initial \(x\),

\[
A^{2h}x=\ell(\ell^{\mathsf T}x),
\]

so the time \(2h\) state is nonzero exactly when the initial deepest-level parity \(\ell^{\mathsf T}x\) is one. This nonzero linear functional takes each value on exactly half of \(\mathbb F_2^{V(T)}\). Such states first reach zero at time \(2h+1\), while all other states are already zero by time \(2h\). This proves every assertion, including \(h=0\). \(\square\)

## Verification

The standalone file `verify.py` performs direct bit-matrix iteration, independently computing the graph from a parent list. It compares the predicted \((A^t)_{uv}\) with all source-to-target parity walk coefficients through \(t=2h+1\), checks both final powers, and for small trees exhausts all initial binary configurations and the exact half-at-last-step count. It tests 145 unlabelled rooted even-branching shapes through 13 vertices, 6,858 exhaustive labelled configurations through nine vertices, and 120 additional seeded nonuniform examples of greater size. Its output is saved as `verification_output.txt`. These tests corroborate, but do not substitute for, the all-tree formal-resolvent proof above.

Run with Python 3.10 or newer: `python verify.py`.

## Relationship to prior work

Finite-field walk matrices and powers of graph adjacency are classical. Work on cellular automata on **infinite** regular rooted trees, such as Ceccherini-Silberstein, Coornaert, Fiorenzi and Šunić (arXiv:1205.6785, first publicly submitted 2012-05-30), analyzes tree shifts, soficity and surjectivity, not this finite undirected root-parity identity. Akın (arXiv:1211.7362, first publicly submitted 2012-11-30) studies reversibility and entropy of cellular automata on Cayley trees with distinct branching assumptions and does not establish the complete finite adjacency-power kernel. The proof here specializes neither a stated infinite-tree surjectivity result nor an ordinary one-step invertibility test: it supplies an exact formula for **every** time and pair of vertices. The standard walk-counting interpretation alone does not supply the even-child cancellations used in the proof.

## Limitations

The theorem is restricted to finite trees with even child count at every nonleaf and binary **neighbour-XOR** dynamics. It is not a theorem for arbitrary odd-degree graphs, general trees, threshold dynamics, or non-binary coefficients. It does not classify the individual Jordan block multiplicities or cycles of perturbed update rules. The historical originality check is bounded: unindexed publications may contain an equivalent parity-walk kernel. One examined open-access Cayley-tree paper was read in a 2017 revision, although its original preprint date is 2012. No independent human or external mathematical audit has been conducted.

## References

1. T. Ceccherini-Silberstein, M. Coornaert, F. Fiorenzi and Z. Šunić, *Cellular automata on regular rooted trees*, arXiv:1205.6785, version first publicly submitted 2012-05-30, https://arxiv.org/abs/1205.6785.
2. H. Akın, *The entropy and reversibility of cellular automata on Cayley tree*, arXiv:1211.7362, version first publicly submitted 2012-11-30, https://arxiv.org/abs/1211.7362.
