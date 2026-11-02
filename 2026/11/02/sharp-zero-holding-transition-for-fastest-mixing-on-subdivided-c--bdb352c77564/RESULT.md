# Sharp zero-holding transition for fastest mixing on subdivided complete bipartite graphs

## Finding

For integers \(2\le p\le q\), let \(S(K_{p,q})\) be the graph obtained by replacing each edge of \(K_{p,q}\) with a path of length two, using a different new vertex for each old edge. Over **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on the edges and diagonal of this graph, an optimizer with zero holding probability at **every original vertex** exists if and only if
\[
(p,q)\notin\{(2,2),(2,3)\}.
\]
More strongly, whenever the condition holds, **every** globally optimal transition matrix has zero holding at every original vertex.

For these parameters, the optimal second-largest eigenvalue modulus is exactly
\[
\boxed{\mu_*(p,q)=\frac{d+\sqrt{d^2+4/p}}2,\qquad d=1-\frac1p-\frac1q.}
\]
One global optimizer gives every edge from a vertex in the \(p\)-vertex original part to its subdivision vertex probability \(1/q\), and every edge from a vertex in the \(q\)-vertex original part to its subdivision vertex probability \(1/p\). Each subdivision vertex holds with probability \(d>0\). In the two excluded graphs this fully saturated transition matrix is strictly suboptimal. No closed formula for the optimum in the two excluded graphs is asserted here.

For fixed \(p\ge2\) and \(q\to\infty\), the exact formula gives
\[
1-\mu_*(p,q)=\frac{p}{(p+1)q}+O_p(q^{-2}).
\]

## Assumptions and scope

Write the original vertex classes as \(U=\{u_1,\ldots,u_p\}\) and \(V=\{v_1,\ldots,v_q\}\), and the \(pq\) subdivision vertices as \(W=\{w_{ij}:1\le i\le p,1\le j\le q\}\). Only \(u_iw_{ij}\) and \(v_jw_{ij}\) are graph edges; self-loops are permitted. All off-edge transitions are zero. The stationary measure is uniform because matrices are symmetric and stochastic. The second-largest eigenvalue modulus \(\mu(P)\) is the maximum absolute eigenvalue on the orthogonal complement of the constant vector.

For the subgroup of automorphisms \(S_p\times S_q\), an invariant feasible transition matrix has edge weights \(a\) on every \(u_iw_{ij}\) and \(b\) on every \(v_jw_{ij}\). Its holding probabilities on \(U,V,W\) are respectively \(1-qa\), \(1-pb\), and \(1-a-b\). Its feasible region is precisely
\[
0\le a\le 1/q,\qquad 0\le b\le1/p;
\]
the third row-sum constraint is automatic since \(1/p+1/q\le1\).

## Proof

**1. Symmetry reduction is globally valid.** The FMMC objective is
\(\mu(P)=\|P-J\|_2\), where \(J\) is orthogonal projection onto the constants. This is convex and invariant under the automorphism group. Averaging any optimal feasible matrix under \(S_p\times S_q\) produces an invariant feasible optimizer. Hence optimizing the two variables \(a,b\) does not assume that every original optimizer is symmetric.

**2. Exact invariant spectral decomposition.** Let \(e=1-a-b\). Decompose the space of functions on \(U\sqcup V\sqcup W\) according to constant, row-zero, column-zero, and doubly centered components of the \(p\)-by-\(q\) array indexed by \(W\). The nontrivial blocks of the transition matrix are
\[
C=\begin{pmatrix}
1-qa&0&\sqrt q\,a\\
0&1-pb&\sqrt p\,b\\
\sqrt q\,a&\sqrt p\,b&e
\end{pmatrix},
\]
\[
X=\begin{pmatrix}1-qa&\sqrt q\,a\\\sqrt q\,a&e\end{pmatrix},\qquad
Y=\begin{pmatrix}1-pb&\sqrt p\,b\\\sqrt p\,b&e\end{pmatrix}.
\]
Here \(C\) occurs once, \(X\) occurs \(p-1\) times, \(Y\) occurs \(q-1\) times, and the scalar block \((e)\) occurs \((p-1)(q-1)\) times. The counts total \(p+q+pq\). The block \(C\) has the stationary eigenvalue \(1\).

**3. Complete spectrum at full original-row saturation.** Set \(a_0=1/q\), \(b_0=1/p\), \(s=1/p+1/q\), and \(d=1-s\). Both \(X\) and \(Y\) now have form
\[
\begin{pmatrix}0&1/\sqrt r\\1/\sqrt r&d\end{pmatrix},
\]
with \(r=q\) and \(r=p\) respectively. Thus their eigenvalues are
\[
\frac{d\pm\sqrt{d^2+4/r}}2.
\]
The constant block has eigenvalues \(1,0,-s\): its determinant is zero, its trace is \(d\), and stochasticity gives eigenvalue \(1\). Since \(p\le q\) and \(d\ge0\), the largest nonstationary eigenvalue is
\[
F=\frac{d+\sqrt{d^2+4/p}}2,
\]
and no other nonstationary eigenvalue has magnitude greater than \(\max\{F,s\}\). Hence the SLEM of the saturated chain is \(\max\{F,s\}\).

The positive root \(F\) satisfies \(F^2-dF-1/p=0\). Because \(s>0\) and \(F>0\), comparison with this quadratic gives
\[
F\ge s\quad\Longleftrightarrow\quad 2s^2-s-1/p\le0.
\]
For \(p\ge3\), \(1/p\le s\le2/p\), and the convex quadratic \(2s^2-s-1/p\) is negative at both endpoints: the values are \((2-2p)/p^2\) and \((8-3p)/p^2\). For \(p=2,q\ge4\), \(1/2<s\le3/4\) and the quadratic is increasing on that interval and at most \(-1/8\). At \((p,q)=(2,3)\) its value is \(1/18\), and at \((2,2)\) its value is \(1/2\). Thus \(F>s\) exactly outside those two cases.

**4. Optimality and strict orbit uniqueness in the main range.** For any \(0\le a\le a_0\) and \(0\le b\le b_0\), the weighted Laplacian \(L(a,b)=I-P(a,b)\) is bounded above in positive semidefinite order by \(L(a_0,b_0)\). This gives \(\lambda_2(L(a,b))\le1-F\), whence \(\mu(P(a,b))\ge F\). Together with Step 3, equality is attained by the saturated chain whenever \(F>s\).

The inequality is strict if either of the two weights is smaller. Indeed, choose any nonzero real vector \((t_j)_{j=1}^q\) with \(\sum_jt_j=0\), and define a test vector on the full graph by
\[
z(u_i)=0,\quad z(v_j)=t_j,\quad z(w_{ij})=Ft_j.
\]
Direct multiplication at \((a_0,b_0)\) shows \(P(a_0,b_0)z=Fz\). Every original-to-subdivision edge type has a strictly positive total squared difference over this vector, because \(F>0\) and \(F<1\). Lowering either \(a\) or \(b\) strictly lowers its Laplacian Rayleigh quotient below \(1-F\). Consequently \(\lambda_2(L(a,b))<1-F\) and \(\mu(P(a,b))>F\). The saturated pair is therefore the unique optimal pair within the invariant family.

If an arbitrary unrestricted optimizer is averaged over \(S_p\times S_q\), this unique invariant pair results. Its holding probability vanishes at all original vertices. Since the original holding probabilities of the unaveraged matrix are nonnegative, an average of zero forces each of them to be zero. This proves the universal assertion for unrestricted optimizers.

**5. The two sharp exceptions.** When \(F<s\), the saturated matrix has SLEM \(s\) attained by its eigenvalue \(-s\), while all remaining nonstationary eigenvalues have modulus at most \(F<s\). For sufficiently small \(\varepsilon>0\), replacing the saturated matrix by \(\varepsilon I+(1-\varepsilon)P(a_0,b_0)\) strictly decreases its SLEM: the eigenvalue \(-s\) moves toward zero and every other eigenvalue remains below \(s\) in modulus. This proves the saturated matrix is not optimal for \((2,2)\) and \((2,3)\). If any optimal matrix had zero holding at all original vertices, its orbit average would equal the saturated matrix, a contradiction. Hence the exceptions are necessary and sharp.

**6. Large-\(q\) expansion.** For fixed \(p\), substitute \(d=1-1/p-1/q\) into \(F^2-dF-1/p=0\) and expand its positive root at \(q^{-1}=0\). The root equals \(1\) at zero, and implicit differentiation gives first derivative \(-p/(p+1)\), yielding the stated expansion.

## Verification

The accompanying `verify.py` builds the full matrix independently of the block decomposition. It verifies the complete spectral list against numerical symmetric eigensolvers, evaluates the exact rational sign of the threshold polynomial for hundreds of integer pairs, checks the saturated formula across finite instances, tests randomized feasible orbit and non-orbit assignments, and checks the large-\(q\) expansion. Run `python verify.py` with Python 3 and NumPy available. Successful execution prints its actual assertion count. These finite calculations check identities and implementation but do not replace the universal proof above.

## Relationship to prior work

Boyd, Diaconis and Xiao established the convex SDP formulation and symmetry-averaging principle for FMMC. Boyd, Diaconis, Parrilo and Xiao analyzed edge-transitive graphs, complete bipartite graphs **without edge subdivision**, and other symmetry reductions. Their formula for \(K_{p,q}\) is not the formula for \(S(K_{p,q})\): the latter has \(pq\) additional edge-specific vertices, two edge orbits, and different spectral blocks. Jafarizadeh examined complete connections between successive vertex layers in pseudo-distance-regular multipartite networks; those layers are not the pair-specific edge-incidence structure studied here. The eight-cycle case \(S(K_{2,2})\) is consistent with existing cycle FMMC formulas and is credited as a pre-existing special case. The claim is the exact two-exception support classification and the infinite-family closed-form optimizer/SLEM for the remaining pairs.

## Limitations

The exact optimal SLEM and edge weights of the two exceptional pairs are not claimed. Unrestricted uniqueness of the entire transition matrix is not claimed; the proof establishes uniqueness only after symmetry averaging, together with the universal absence of original-vertex holding in the main range. The new classification has a same mathematical model proof review but no independent audit. Relevant unindexed or inaccessible specialized prior literature may establish an equivalent statement; the literature comparisons below do not constitute a universal novelty guarantee.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689; DOI: https://doi.org/10.1137/S0036144503423264 ; open PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (public version 2007-09-06); https://arxiv.org/abs/0709.0955 .
3. S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network*, arXiv:1008.2588 (public version 2010-08-16); https://arxiv.org/abs/1008.2588 .
