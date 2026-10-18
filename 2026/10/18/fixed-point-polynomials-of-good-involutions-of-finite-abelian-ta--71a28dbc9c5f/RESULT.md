# Fixed-point polynomials of good involutions of finite abelian Takasaki quandles

## Finding
Let \(A\) be a finite abelian group, with \(x\triangleright y=2y-x\). Denote the set of good involutions \(\mathcal G(A)\), counting distinct functions rather than isomorphism classes, and define
\[F_A(z)=\sum_{\rho\in\mathcal G(A)}z^{|\operatorname{Fix}\rho|}.\]
Let \(T=A[2]\), \(B=A/2A\), and \(\pi:T\to B\) the natural map. Put \(d=\dim_{\mathbf F_2}B\), \(e=\dim_{\mathbf F_2}\pi(T)\), \(K=2^{d-e}\), \(L=2^e\), \(b=2^{d-e}\), and \(h=|2A|\). Then
\[
\boxed{F_A(z)=\left[\sum_{j=0}^{\lfloor L/2\rfloor}
\frac{L!}{2^j j!(L-2j)!}\,K^j(K-1+z^h)^{L-2j}\right]^b.}
\]
In particular, \(F_A(1)\), the total number of good involutions, depends only on the \(2\)-rank \(d\) and the number \(e\) of cyclic direct factors of order exactly \(2\) in the \(2\)-primary subgroup. The fixed-point polynomial also depends on \(h=|A|/2^d\).

For \(A=\mathbf Z/2\mathbf Z\oplus\mathbf Z/4\mathbf Z\),
\[F_A(z)=(3+2z^2+z^4)^2=9+12z^2+10z^4+4z^6+z^8,\]
so \(36\) good involutions exist, of which \(9\) are fixed-point-free. For the elementary abelian group \((\mathbf Z/2\mathbf Z)^3\), the polynomial is \(105+420z^2+210z^4+28z^6+z^8\). For odd-order \(A\) there is only the identity, so \(F_A(z)=z^{|A|}\).

## Assumptions and scope
Every group is finite and abelian. A good involution is a function \(\rho:A\to A\) satisfying \(\rho^2=\mathrm{id}\), \(\rho(x\triangleright y)=\rho(x)\triangleright y\), and \(x\triangleright\rho(y)=x\triangleright y\) for all \(x,y\in A\). This is the usual symmetric-quandle definition specialized to a kei. All multiplicities count actual maps, with no division by automorphism groups.

## Proof
Write \(R_y(x)=2y-x\). The commuting relation \(\rho R_y=R_y\rho\) implies commutation with each translation \(R_yR_0:x\mapsto x+2y\). Thus \(\rho(x)=x+\delta(\bar x)\) for a function \(\delta:B\to A\), where \(\bar x=x+2A\). The remaining good-involution condition is \(2\rho(y)=2y\), forcing \(\delta(B)\subseteq T=A[2]\). Conversely every such function satisfies both good-involution equations: \(\overline{2y-x}=\bar x\) and \(-\delta=\delta\) for elements of \(T\), so \(\rho R_y=R_y\rho\). Its square is the identity if and only if
\[\delta\bigl(c+\pi(\delta(c))\bigr)=\delta(c)\quad\text{for every }c\in B.\]

Set \(H=\pi(T)\), a subgroup of order \(L\) in \(B\). This equation acts separately on the \(b=|B/H|\) cosets of \(H\), each of size \(L\). At a point \(c\), either \(\pi\delta(c)=0\), which makes it a singleton, or \(\pi\delta(c)\ne0\), which pairs it with \(c'=c+\pi\delta(c)\). In the latter case involutivity requires \(\delta(c')=\delta(c)\), and this genuinely is a disjoint matching. Every matching with the following labels conversely defines one valid \(\delta\).

The kernel of \(\pi\) has order \(K\). A singleton may carry any of these \(K\) displacements. The zero displacement fixes every one of the \(h\) group elements in the corresponding coset of \(2A\), while each of the \(K-1\) nonzero choices fixes none: its weight is \(K-1+z^h\). At a matched pair \(\{c,c'\}\), the displacement must lie in the \(K\)-element fiber \(\pi^{-1}(c'-c)\), and neither coset has a fixed point: its weight is \(K\). The number of matchings with \(j\) pairs on \(L\) labeled points is exactly \(L!/(2^jj!(L-2j)!)\). Multiplying the weighted matching sums over the \(b\) independent cosets proves the formula.

Finally, the \(2\)-primary elementary divisors of \(A\) show that \(d\) counts all cyclic \(2\)-power direct factors, while \(e\) counts precisely those of order \(2\). The unique element of order \(2\) in a factor of order at least \(4\) lies in \(2A\), so has zero image under \(\pi\); this proves the rank claims and completes the argument, including the trivial-group boundary.

## Verification
Run `python check.py` with Python 3. It independently enumerates every permutation of groups with cyclic-factor orders \((1)\), \((3)\), \((4)\), \((5)\), \((6)\), \((7)\), \((8)\), \((2,2)\), \((2,4)\), \((2,2,2)\), and \((2,3)\). It directly tests the three defining identities against the quandle operation table, records the fixed-point counts, and compares with a separately coded coefficient formula. A successful run prints `CHECKER_OK`. Finite checks supplement, rather than replace, the all-group proof.

## Relationship to prior work
Taniguchi (arXiv:2302.11138, 2023) treats generalized Alexander quandles and classifies the connected case. Kamada–Oshiro (2010) gives the previously known cyclic-dihedral unrefined counts. Ta's structural work (arXiv:2505.08090 and arXiv:2508.16772, 2025) already characterizes good involutions of core and general Alexander quandles; Theorem 4.2 of the second paper implies the displacement parametrization above, which is **not claimed to be new**. Theorem 5.11 of that paper uses weighted matchings for another family of cyclic Alexander quandles. The new arithmetic assertion assessed here is the evaluated, fixed-point-refined formula for **all finite abelian Takasaki quandles**, including the factorization and exact two-rank dependence; the directly related papers inspected do not state this result.

## Limitations
The formula counts good involution maps, not symmetric-quandle isomorphism classes; it is limited to finite abelian Takasaki quandles. Its structural starting point and matching method have strong literature precedents. An equivalent closed enumeration in an unindexed source remains possible. No independent mathematical audit was performed.

## References
1. Y. Taniguchi, *Good involutions of generalized Alexander quandles*, arXiv:2302.11138 (first public 2023-02-22), https://arxiv.org/abs/2302.11138; J. Knot Theory Ramifications 32 (2023) 2350081.
2. L. Ta, *Good involutions of conjugation subquandles*, arXiv:2505.08090 (2025), https://arxiv.org/abs/2505.08090.
3. L. Ta, *Good involutions of twisted conjugation subquandles and Alexander quandles*, arXiv:2508.16772 (2025), https://arxiv.org/abs/2508.16772; Communications in Algebra, published online 2026-04-30.
4. S. Kamada and K. Oshiro, *Homology groups of symmetric quandles and cocycle invariants of links and surface-links*, Trans. Amer. Math. Soc. 362 (2010), 5501–5527, DOI:10.1090/S0002-9947-2010-05131-1.
