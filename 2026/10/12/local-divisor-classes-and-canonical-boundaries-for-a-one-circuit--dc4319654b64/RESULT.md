# Local divisor classes and canonical boundaries for a one-circuit-hyperplane matroid toric variety

## Finding
For integers \(n\ge6\), \(3\le k\le n-3\), and a selected \(k\)-set \(H\subseteq[n]\), write \(\mathcal B=\{B\subseteq[n]:|B|=k,\ B\ne H}\). This is the basis family of a one-circuit-hyperplane sparse paving matroid. Let \(P=\operatorname{conv}\{\mathbf1_B:B\in\mathcal B}\) and let \(X_P\) be the normal projective toric variety with normal fan of \(P\), over \(\mathbb C\). Its fixed point corresponding to \(B\) is \(p_B\), and put \(c(B)=|B\cap H|\).

**Theorem (local divisor-class and canonical boundary classification).** The complete *integral* local divisor-class groups satisfy
\[
\operatorname{Cl}(\mathcal O_{X_P,p_B})\cong
\begin{cases}
\mathbb Z,&c(B)\le k-2,\\
\mathbb Z^2,&c(B)=k-1.
\end{cases}
\]
These groups are torsion-free. There are precisely \(k(n-k)\) fixed points of rank two and \(\binom nk-1-k(n-k)\) of rank one. Moreover, a fixed-point local ring is \(\mathbb Q\)-Gorenstein if and only if it is Gorenstein, and this occurs exactly if
\[
 n=2k\quad\text{and}\quad(c(B)\le k-2\quad\text{or}\quad k=3).
\]
Consequently \(X_P\) is globally Gorenstein, equivalently globally \(\mathbb Q\)-Gorenstein, if and only if \((n,k)=(6,3)\). Every fixed point is singular. The structural contribution is the local integral class-group jump and the pointwise canonical Cartier stratification, rather than merely the global Gorenstein yes/no corollary.

## Assumptions and scope
All schemes and groups are over \(\mathbb C\). The base polytope lives in the affine lattice \(\sum_i x_i=k\) and has dimension \(n-1\). Its dual toric ray lattice is \(N=\mathbb Z^n/\mathbb Z(1,\ldots,1)\), paired with \(M=\{m\in\mathbb Z^n:\sum_i m_i=0}\). We use the outward normal fan convention; simultaneously negating all ray vectors gives the equivalent opposite convention. The statements classify torus-*fixed-point* local rings; they do not classify the entire singular locus or every local class group away from the fixed points. The inequality \(3\le k\le n-3\) ensures all coordinate facets remain facets after deleting one vertex.

## Proof
**1. The matroid and the truncated hypersimplex.** All \(k\)-subsets other than \(H\) satisfy basis exchange: for two such sets and an element to be exchanged, there is at most one excluded choice, while if there is only one choice the exchanged set equals the other given basis and hence is permitted. Let
\[
 \Delta(k,n)=\{x\in[0,1]^n:\sum_i x_i=k}.
\]
Its edges join precisely two indicator vectors differing by one element. The half-space \(x(H)=\sum_{i\in H}x_i\le k-1\) eliminates exactly the vertex \(\mathbf1_H\). Each edge from that vertex meets the cutting hyperplane at its *other* endpoint, since such an edge replaces exactly one member of \(H\). Hence there are no new fractional vertices and
\[
 P=\Delta(k,n)\cap\{x(H)\le k-1}.
\]
Its facets are precisely the \(2n\) original coordinate facets \(x_i=0\), \(x_i=1\), and the new facet \(x(H)=k-1\). Indeed every coordinate face has dimension \(n-2\) after the removal: it is a hypersimplex \(\Delta(k,n-1)\) or \(\Delta(k-1,n-1)\) with at most one vertex omitted, within the displayed range, and the remaining vertices still affinely span. The new face is the product \(\Delta(k-1,k)\times\Delta(1,n-k)\) and has dimension \(n-2\). No additional facet can be created by intersecting a polytope with one half-space.

**2. Integral normal rays and class groups.** At the vertex \(\mathbf1_B\), exactly the \(n\) coordinate facets indexed by \(i\in B\) with \(x_i=1\) and \(i\notin B\) with \(x_i=0\) meet. Their primitive outward normals are \(s_i\bar e_i\), where \(s_i=1\) for \(i\in B\), \(s_i=-1\) otherwise and \(\bar e_i\) is the image of the standard basis vector in \(N\). The new facet meets \(\mathbf1_B\) exactly when \(c(B)=k-1\), with primitive normal \(h=\overline{\sum_{i\in H}e_i}\). Primitivity follows because \(H\) and its complement are nonempty and the coordinate difference of an entry in \(H\) with an entry outside \(H\) equals one. These are *all* rays of the corresponding normal cone.

Let \(\varepsilon=1\) if \(c(B)=k-1\), otherwise \(0\). The affine toric divisor sequence at this vertex is
\[
 M\longrightarrow\mathbb Z^{n+\varepsilon}
 \longrightarrow\operatorname{Cl}(\mathcal O_{X_P,p_B})\longrightarrow0.
\]
The first map sends \(m\in M\) to the coordinates \((s_1m_1,\ldots,s_nm_n)\), followed, if \(\varepsilon=1\), by \(\sum_{i\in H}m_i\). The first \(n\) coordinates are a signed copy of the saturated sublattice \(M\subset\mathbb Z^n\), whose quotient is \(\mathbb Z\) via signed summation. The extra coordinate is the integral linear combination \(\sum_{i\in H}s_i(s_im_i)\) of them, so it adds one independent free factor to the cokernel and **cannot introduce torsion**. This proves the two class groups. The condition \(c(B)=k-1\) describes the \(k(n-k)\) neighbors of the removed basis: choose the removed element from \(H\) in \(k\) ways and its replacement from the complement in \(n-k\) ways. The total number of permitted bases is \(\binom nk-1\).

**3. Cartier canonical class and its rational obstruction.** In a normal affine toric chart, the canonical divisor is Cartier, respectively \(\mathbb Q\)-Cartier, exactly when a character \(m\in M\), respectively \(m\in M_\mathbb Q\), has pairing one with *every primitive ray* of its cone. From the \(n\) coordinate rays the unique possible character has \(m_i=s_i\) for every \(i\). Its coordinate sum is \(\sum_i s_i=2k-n\), so it belongs to \(M_\mathbb Q\) precisely when \(n=2k\), in which case it is automatically integral. If the extra ray is present, its pairing with this candidate is
\[
\left\langle m,h\right\rangle
 =\sum_{i\in H}s_i
 =(k-1)-1=k-2,
\]
which equals one precisely when \(k=3\). Thus the displayed local Gorenstein criterion is necessary and sufficient for both rational and integral Cartier conditions. For global \(\mathbb Q\)-Gorenstein, every maximal toric chart must pass the test. The exceptional neighbors always exist, so \(n=2k\) and \(k=3\) are both necessary and sufficient. Finally, a regular local ring is factorial, whereas every computed local class group has positive rank, so every fixed point is singular.

## Verification
The standalone standard-library script `CHECKER.py` performs exact-rational affine facet-rank calculations for all \(6\le n\le9\) and \(3\le k\le n-3\), checks the two classes of ray-incidence counts, and evaluates the unique canonical character in every case. The output in `CHECKER_OUTPUT.txt` records 682 fixed-point charts and 170 supporting facet checks; all assertions pass. To reproduce, run `python3 CHECKER.py` with Python 3 and compare stdout to `CHECKER_OUTPUT.txt`. These finite computations *do not prove* the all-parameter assertions or check the infinite cokernel formula; those follow from the integral lattice argument above.

## Relationship to prior work
Katz, *Matroid theory for algebraic geometers* (arXiv:1409.3503v1, first public 2014-09-11), supplies the matroid/polytope and toric orbit-closure framework. Lasoń and Michałek, *Gorenstein matroids* (arXiv:2005.08359, initially 2020), provide a much broader classification of the Gorenstein property of matroid base semigroup rings and facet theorems; the present **global Gorenstein special case is not asserted to be independently new**. Ferroni and Schröter, *Face enumeration for split matroid polytopes* (arXiv:2310.05487, initially 2023), Corollary 2.10, calculate the complete face enumerators for sparse paving matroid polytopes, including the one-circuit-hyperplane case. Such enumerators recover aggregate face counts but do not themselves determine the integral local Weil-class cokernels at each vertex or the pointwise canonical Cartier obstruction. The known hypersimplex case has uniform fixed-point class rank one and a balanced Gorenstein threshold; deleting one basis adds a new facet and causes the asserted rank-two and Cartier stratification. The theorem does not claim that the matroid facet inequalities or the formal toric divisor exact sequence are new.

## Limitations
No local analytic normal forms, resolutions, non-fixed-point singular strata, or full Chow-ring presentation are determined. A finite checker is supporting evidence only. Published matroid-polytope and toric literature may include an equivalent specialized class-group calculation not found in the inspected materials; independent literature verification is outstanding. The global Gorenstein condition can overlap known general Gorenstein matroid results.

## References
1. E. Katz, *Matroid theory for algebraic geometers*, arXiv:1409.3503v1 (2014), https://arxiv.org/abs/1409.3503.
2. M. Lasoń and M. Michałek, *Gorenstein matroids*, arXiv:2005.08359 (2020 first version), https://arxiv.org/abs/2005.08359.
3. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487 (2023 first version), https://arxiv.org/abs/2310.05487.
4. D. Cox, J. Little and H. Schenck, *Toric Varieties*, American Mathematical Society (2011), section on the toric divisor-class exact sequence.
