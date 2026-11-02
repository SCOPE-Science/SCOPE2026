# Nilpotent Jordan fusion in binary lollipop dynamics

## Finding
For integers \(n\ge3\) and \(m\ge1\), let \(L_{n,m}\) be the labelled lollipop consisting of a cycle \(v_0v_1\cdots v_{n-1}v_0\) and a pendant path \(v_0u_1u_2\cdots u_m\). Let \(F_{n,m}\) be synchronous binary open-neighborhood parity updating: the new bit at a vertex is the sum of its neighbors' previous bits in \(\mathbb F_2\). Put
\[
e=2^{\nu_2(n)},\qquad s=2^{\nu_2(m+2)},\qquad D=n+m-e-s+2.
\]
The complete multiset \(B_{n,m}\) of Jordan-block sizes belonging to eigenvalue zero is as follows (empty means no such blocks):

| Parameters | \(B_{n,m}\) |
|---|---|
| \(n,m\) both odd | empty |
| \(n\) odd, \(m\) even | \(\{s-1\}\) |
| \(n\) even, \(m\) odd | \(\{e-1\}\) |
| \(n\) even, \(m\equiv2\pmod4\) | \(\{1,e+s-3\}\) |
| \(n\) even, \(4\mid m\) | \(\{d,e-d\}\), where \(d=\min\{e/2,2^{\nu_2(m)}-1\}\) |

These are positive sizes in every nonempty case. Exactly \(2^D\) configurations are periodic, and the number whose trajectory has *entered* the periodic set by update \(t\), for every integer \(t\ge0\), is
\[
C_{n,m}(t)=2^{D+\sum_{b\in B_{n,m}}\min(t,b)}.
\]
Consequently, exactly \(C_{n,m}(t)-C_{n,m}(t-1)\) configurations enter the periodic set for the first time at update \(t\ge1\); the maximum transient length is \(\max B_{n,m}\), with the maximum of the empty multiset interpreted as zero.

An unexpected spectral equivalence holds over \(\mathbb F_2\): writing \(P_j\) for the path on \(j\) vertices,
\[
\det(xI-F_{n,m})=\det(xI-A_{P_{n-1}\sqcup P_{m+1}}).
\]
Nevertheless, these two dynamics can have different transient structures. For \(n=m=2^k\), \(k\ge2\), the lollipop has zero-primary blocks \(\{2^{k-1},2^{k-1}\}\), whereas the disconnected paths have blocks \(\{2^k-1,1\}\). Thus their maximum transient lengths are respectively \(2^{k-1}\) and \(2^k-1\), even though their characteristic polynomials and periodic-state populations agree. Conversely, for \(n=2^k\), \(m=2\), the lollipop has blocks \(\{1,2^k+1\}\) versus \(\{2^k-1,3\}\) for the paths.

## Assumptions and scope
All graph edges are simple, undirected, and unweighted; the update uses the **open** neighborhood, no self-loop, no forcing, and simultaneous (not sequential) updates. All states are in \(\mathbb F_2^{n+m}\). The term *periodic* means a state lying on a cycle of \(F_{n,m}\), not merely a state eventually entering a cycle. A transient length counts updates preceding the first periodic state, and \(\nu_2(r)\) denotes the exponent of two dividing a positive integer \(r\). The result is exact for all stated \(n,m,t\), without asymptotic or genericity assumptions.

## Proof
Set \(p_0(x)=1\), \(p_1(x)=x\), and \(p_{j+1}(x)=xp_j(x)+p_{j-1}(x)\) over \(\mathbb F_2[x]\). These are the characteristic polynomials of the open-neighborhood adjacency matrices of paths \(P_j\). Pendant-vertex deletion and the cycle identity \(\det(xI-A_{C_n})=xp_{n-1}(x)\) in characteristic two give
\[
\begin{aligned}
\det(xI-F_{n,m})
&=p_m(x)\det(xI-A_{C_n})+p_{m-1}(x)p_{n-1}(x)\\
&=p_{n-1}(x)\bigl(xp_m(x)+p_{m-1}(x)\bigr)\\
&=p_{n-1}(x)p_{m+1}(x).
\end{aligned}
\]
Here the contribution of traversing an entire undirected cycle twice cancels in characteristic two; the deletion identity can alternatively be proved directly by a determinant expansion.

We now determine *Jordan structure*, which the characteristic polynomial alone does not specify. Regard the state space as an \(R=\mathbb F_2[x]\)-module, with \(x\) acting as \(F_{n,m}\). A standard presentation is the cokernel of \(xI-F_{n,m}\). The equations at the internal vertices of the cycle express every \(v_j\), \(2\le j<n\), in terms of generators \(v_0,v_1\) using the recurrence for \(p_j\). The equations on the pendant path likewise express all \(u_j\) in terms of \(v_0,u_1\). The equation at \(v_0\) eliminates \(u_1\), leaving the following *exact* two-generator square presentation:
\[
M_{n,m}(x)=
\begin{pmatrix}
1+p_{n-2}&p_{n-1}\\
p_{m-1}+p_m(x+p_{n-3})&p_m(1+p_{n-2})
\end{pmatrix}.
\]
Indeed the cycle closure supplies \((1+p_{n-2})v_0+p_{n-1}v_1=0\), while the pendant boundary condition is \(p_{m-1}v_0+p_mu_1=0\) and \(u_1=(x+p_{n-3})v_0+(1+p_{n-2})v_1\). Every eliminated relation contains a unit coefficient, so the resulting presentation preserves the entire \(R\)-module, rather than merely its determinant.

Write \(v_x(f)\) for the order at \(x=0\), with \(v_x(0)=+\infty\). For a two-by-two square presentation with determinant having \(x\)-order \(q\), its local Smith invariant exponents are \(\delta,q-\delta\), where \(\delta\) is the minimum \(x\)-order among its four entries; a zero exponent contributes no zero-primary Jordan block. The recurrence gives the Frobenius identity \(p_{2r-1}=xp_{r-1}^2\). Repeatedly applying it proves, for every positive integer \(r\),
\[
v_x(p_{r-1})=2^{\nu_2(r)}-1.
\]
In particular, the determinant has zero multiplicity \(q=e+s-2\).

If \(n,m\) are both odd, \(q=0\). If \(n\) is odd and \(m\) even, the upper-left entry \(1+p_{n-2}\) has constant coefficient one, giving one block of size \(s-1\). If \(n\) is even and \(m\) odd, the lower-left entry has constant coefficient one, giving one block of size \(e-1\). If \(n\equiv2\pmod4\) and \(m\) is even, all entries vanish at zero, while \(p_{n-1}\) has exact order one; hence \(\delta=1\), and the blocks are \(1\) and \(e+s-3\).

It remains to take \(4\mid n\). Define
\[
Q(x)=\begin{pmatrix}x&1\\1&0\end{pmatrix},\qquad Q(x)^2=I+xQ(x),\qquad
Q(x)^n=\begin{pmatrix}p_n&p_{n-1}\\p_{n-1}&p_{n-2}\end{pmatrix}.
\]
Since \(n/e\) is odd, \(e\ge4\), and \(Q(0)^{e/2}=I\), the characteristic-two Frobenius rule applied to \(Q^n=(I+xQ)^{n/2}\) yields
\[
Q(x)^n\equiv I+x^{e/2}I\pmod{x^{e/2+1}}.
\]
Thus \(a=1+p_{n-2}\) has \(v_x(a)=e/2\). The path recurrence also gives
\[
x+p_{n-3}=p_{n-1}+xa,
\]
so \(v_x(x+p_{n-3})\ge e/2+1\), because \(v_x(p_{n-1})=e-1\ge e/2+1\). For even \(m\), \(p_m(0)=1\) and \(v_x(p_{m-1})=2^{\nu_2(m)}-1\). If \(m\equiv2\pmod4\), this last valuation is one, so the lower-left entry of \(M\) has valuation one and \(\delta=1\). If \(4\mid m\), the minimum valuation among the four entries of \(M\) is exactly
\[
\delta=\min\bigl(e/2,2^{\nu_2(m)}-1\bigr)=d.
\]
Since \(s=2\) here, \(q=e\) and the two blocks have sizes \(d,e-d\). This establishes every row of the classification.

Finally, the Fitting decomposition separates a nilpotent generalized zero-eigenspace of dimension \(q\) from an invertible subspace of dimension \(D=n+m-q\). A Jordan block of nilpotent size \(b\) contributes \(\min(t,b)\) independent coordinates to the kernel of the \(t\)-th iterate. A state has entered the periodic subspace by time \(t\) precisely when its nilpotent component has vanished. This proves the claimed formulas for \(C_{n,m}(t)\), all first-entry populations, the total periodic population, and the sharp maximum transient time. The disconnected-path comparison follows because \(P_{n-1}\) and \(P_{m+1}\) separately have zero-primary block sizes \(e-1\) and \(s-1\), omitting size zero.

## Verification
The standalone standard-library program `verify.py` builds the actual binary adjacency matrices without using the presentation matrix. For all \(3\le n\le32\), \(1\le m\le32\) it compares predicted zero-primary kernel dimensions with row-reduction ranks of successive matrix powers (960 pairs, 7,413 rank comparisons). For all pairs with \(n+m\le11\), it independently constructs \(\det(xI-F)\) by subset-based determinant expansion and directly explores every binary state until recurrence (36 parameter pairs and 28,688 states). All comparisons passed; `verification_output.txt` records the exact output of `python3 verify.py`. The proof above, rather than these finite tests, establishes the assertion for unbounded parameters.

## Relationship to prior work
Boulet and Jouve, *The lollipop graph is determined by its spectrum* (first posted February 7, 2008, arXiv:0802.1035), give a comprehensive real-adjacency-spectrum analysis and the general pendant-deletion and cycle characteristic-polynomial identities. Their work motivates the present lollipop family and supplies algebraic background; it does not classify characteristic-two nilpotent Jordan blocks or binary orbit-entry populations. Martin, Odlyzko, and Wolfram (1984) developed finite linear cellular-automaton transition-diagram techniques, largely for homogeneous one-dimensional rules; their method is background, not a lollipop classification. Li, Wang, and Zhang (arXiv:2410.09833) address binary adjacency annihilators for graphs with all vertex degrees even; the lollipops here have a pendant vertex of degree one and attachment vertex of degree three, so their Eulerian hypotheses do not apply. The periodic-set equality with disconnected paths alone is not claimed as the new contribution: the new result is the exact zero-primary block fusion and sharp transient populations on the connected lollipop.

## Limitations
The theorem determines the periodic *population*, nilpotent Jordan structure, and all transient-entry populations, but it does not specify the complete primitive-period distribution inside the invertible component or all nonzero-eigenvalue elementary divisors. The novelty comparison covers explicitly identified primary works and searched records; an equivalent classification in differently indexed literature cannot be excluded without independent historical review. No independent audit has been performed.

## References
1. R. Boulet and B. Jouve, *The lollipop graph is determined by its spectrum*, arXiv:0802.1035 (initial version 2008-02-07), https://arxiv.org/abs/0802.1035 ; *Electronic Journal of Combinatorics* 15 (2008), R74, https://doi.org/10.37236/798 .
2. O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic properties of cellular automata*, *Communications in Mathematical Physics* 93 (1984), 219–258, https://doi.org/10.1007/BF01223745 .
3. K. Li, W. Wang, and H. Zhang, *Annihilating polynomial, Jordan canonical form, and generalized spectral characterizations of Eulerian graphs*, arXiv:2410.09833 (2024), https://arxiv.org/abs/2410.09833 .
