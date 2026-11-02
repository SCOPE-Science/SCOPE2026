# A triangle-chord extinction law for characteristic-two network dynamics

## Finding
Let \(n\ge4\), let \(q=2^b\) for an integer \(b\ge1\), and label the vertices of the cycle \(C_n\) by \(0,1,\ldots,n-1\). Form \(H_n\) by adding the single chord \(\{0,2\}\). On \(\mathbb F_q^{n}\), perform synchronous neighbor-sum dynamics \(F_nx=A(H_n)x\), with every sum taken in characteristic two. Define \(T(x)\) as the smallest nonnegative time at which the forward orbit of \(x\) is periodic.

**Theorem.** If \(n\) is even, the generalized zero-eigenspace consists of two Jordan blocks of size one. Thus
\[
\#\{T=0\}=q^{n-2},\qquad \#\{T=1\}=(q^2-1)q^{n-2},
\]
and no initial state has a larger entry time.

If \(n\) is odd, set \(s=\nu_2(n-1)\) and \(z=2^s+1\). The generalized zero-eigenspace consists of exactly one Jordan block of size \(z\), and
\[
\#\{T=0\}=q^{n-z},\qquad
\#\{T=t\}=(q-1)q^{n-z+t-1}\quad(1\le t\le z).
\]
All these shells are nonempty and no later entry times occur. In particular, for every \(a\ge2\), the adjacency operator on \(H_{2^a+1}\) is nilpotent of **exact index** \(2^a+1\); every configuration reaches zero, and a fraction \(1-q^{-1}\) of configurations first reach zero at the final step.

This is an exact statement for labelled configurations, with no quotient by graph automorphisms. It also gives the complete normalized distribution under independent uniform initial states by division by \(q^n\).

## Assumptions and scope
The graph is finite, simple, undirected, and contains no self-loops. The chord joins vertices at distance two along the cycle, so \(n\ge4\) ensures it is a genuinely added edge. The update excludes the present state unless it is present as a neighbor (self-loops are absent). The field has characteristic two, not merely arbitrary prime characteristic. The time \(T\) is first entry into any eventual periodic orbit, not necessarily extinction; when the operator is nilpotent, periodicity is equivalent to being zero.

For comparison, the unmodified odd cycle has characteristic polynomial \(Xf_{n-1}(X)\), hence only a simple zero root and a periodic subspace of codimension one. Thus the added chord can turn a system with many recurrent nonzero states into a globally extinguishing one along the unbounded subsequence \(n=2^a+1\).

## Proof
Write \(f_m(X)\) for the characteristic polynomial in characteristic two of the adjacency matrix of a path on \(m\) vertices. Its matching recurrence is
\[
f_0=1,\qquad f_1=X,\qquad f_m=Xf_{m-1}+f_{m-2}\quad(m\ge2).
\]
For any simple graph in characteristic two, the adjacency characteristic polynomial equals the matching polynomial modulo two: nontrivial permutation cycles of length at least three cancel in reverse-oriented pairs in the determinant expansion; fixed points and transpositions contribute the unmatched vertices and matching edges. Consequently, deleting an edge \(e=uv\) gives the polynomial identity \(\chi_G=\chi_{G-e}+\chi_{G-\{u,v\}}\).

Deleting a cycle edge gives \(\chi_{C_n}=f_n+f_{n-2}=Xf_{n-1}\). Deleting the chord from \(H_n\) gives \(C_n\), while deleting its endpoints \(0,2\) leaves one isolated vertex and a path of \(n-3\) vertices. Hence
\[
\chi_{H_n}(X)=Xf_{n-1}(X)+Xf_{n-3}(X)=X^2f_{n-2}(X). \tag{1}
\]

The path recurrence also implies, by simultaneous induction,
\[
f_{2r-1}=X f_{r-1}^2,\qquad f_{2r}=f_r^2+f_{r-1}^2\quad(r\ge1). \tag{2}
\]
The even-index path polynomials have constant term one. If \(n\) is even, \(n-2\) is even and (1) therefore has a zero root of algebraic multiplicity two. If \(n\) is odd, write \(n-1=2^s u\) with \(u\) odd. Repeated use of (2) gives
\[
f_{n-2}=X^{2^s-1}f_{u-1}^{2^s}.
\]
Because \(u-1\) is even, \(f_{u-1}(0)=1\), so the algebraic multiplicity of zero in (1) is exactly \(z=2^s+1\).

It remains to determine the geometric multiplicity, since a characteristic polynomial alone cannot give Jordan-block sizes. Suppose \(A(H_n)x=0\). At vertex \(1\), \(x_0=x_2\). At each vertex except \(0\) and \(2\), the homogeneous recurrence says \(x_{i-1}=x_{i+1}\). Thus the values along the arc \(2,3,\ldots,n-1,0\) alternate between two values \(a=x_2=x_0\) and \(c=x_3\). The equations at vertices \(0\) and \(2\) give \(x_1=a+x_{n-1}=a+c\). When \(n\) is even, the arc parity makes \(x_{n-1}=c\), and \(a,c\) are free, so \(\dim\ker A=2\). When \(n\) is odd, the arc parity gives \(x_{n-1}=a\), forcing \(c=a\), so \(\dim\ker A=1\). These are the only constraints.

The number of Jordan blocks associated with eigenvalue zero equals \(\dim\ker A\). Combining this with its algebraic multiplicity proves that the zero-primary Jordan partition is \((1,1)\) for even \(n\) and \((z)\) for odd \(n\). These blocks are defined over \(\mathbb F_q\), since zero is already in the base field.

Finally apply the Fitting decomposition \(\mathbb F_q^n=U\oplus W\), where \(A|_U\) is the indicated nilpotent operator and \(A|_W\) is invertible. A configuration is periodic exactly when its \(U\)-coordinate vanishes. In the odd case the kernel of the \(t\)-th power on \(U\) has dimension \(\min(t,z)\), giving \(q^{n-z+t}\) states with \(T\le t\) for \(0\le t\le z\). Successive subtraction proves the asserted shells. In the even case the nilpotent part is annihilated in one step and has dimension two. All claimed bounds and their sharpness follow.

## Verification
The attached standard-library program `verify.py` independently reconstructs the binary adjacency matrices, tests their power ranks for all \(4\le n\le150\), independently counts the characteristic polynomial through graph matching enumeration for \(4\le n\le21\), and exhaustively follows every binary microscopic state for \(4\le n\le14\). Its recorded run in `verify_output.txt` reports `TRIANGLE_CHORD_XOR_VERIFY_OK`, 1,071 rank comparisons, 18 matching-polynomial comparisons, and 32,752 exhaustive binary initial states. Finite verification corroborates but is not the proof for arbitrary \(n\) or \(q\); the proof above supplies the all-parameter conclusion.

## Relationship to prior work
Marr and Hütt (2005) motivate studying topological shortcuts in binary network automata, but use degree-dependent nonlinear state-flip rules and statistical pattern measures, not this linear operator or an exact stopping-time law. Macauley and Mortveit (2008) analyze cycle equivalence for *sequential* graph dynamical systems; their update-order theorems do not cover synchronous neighbor sums. Del Rey (2013) treats homogeneous elementary Rule 150 and its circulant inverse, whereas the present graph has an irregular triangular chord and uses neighbor sums without self-state terms. Brouwer, Gow and Sheekey (2014) enumerate symmetric nilpotent matrices and develop the general Fitting/Jordan framework, but do not specify sparse graph supports or the theta-family nilpotent index. The matching-polynomial identity is classical background, not a claimed new lemma. The contribution is the graph-specific all-size zero-primary classification and complete characteristic-two entry-time census, including an infinite sparse nilpotent family.

## Limitations
The theorem does not enumerate the periods of nonzero recurrent orbits on the invertible component. It says nothing about odd-characteristic fields, other chord lengths, or arbitrary network perturbations. Historical exact equivalents cannot be excluded by database searches alone. One relevant article by Ganguly, Sikdar and Pal Chaudhuri (2008) was accessible only through its abstract despite searches for a lawful full-text version; its stated setting is additive cellular automata and it is retained as a literature-access risk. No independent mathematical audit has been performed.

## References
1. C. Marr and M.-T. Hütt, *Topology regulates pattern formation capacity of binary cellular automata on graphs*, arXiv:cond-mat/0502509v1, first submitted 21 February 2005. https://arxiv.org/abs/cond-mat/0502509
2. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412v1, submitted 29 February 2008. https://arxiv.org/abs/0802.4412
3. N. Ganguly, B. K. Sikdar and P. Pal Chaudhuri, *Exploring Cycle Structures of Additive Cellular Automata*, Fundamenta Informaticae 87 (2008), 137–154. https://doi.org/10.3233/FUN-2008-87202
4. A. M. del Rey, *A Note on the Reversibility of Elementary Cellular Automaton 150 with Periodic Boundary Conditions*, Romanian Journal of Information Science and Technology 16 (2013), 365–372. https://www.romjist.ro/content/pdf/08-amdelrey.pdf
5. A. E. Brouwer, R. Gow and J. Sheekey, *Counting symmetric nilpotent matrices*, Electronic Journal of Combinatorics 21 (2014), P2.4. https://doi.org/10.37236/3810
