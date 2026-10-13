# Subalgebra dimension polynomial for generic scalar Heisenberg-type Leibniz algebras

## Finding

For every field \(K\), integer \(m\ge1\), and parameter \(\lambda\in K^\times\) with \(\lambda^2\ne1\), define the \((2m+1)\)-dimensional algebra
\[
L_{m,\lambda}(K)=X\oplus Y\oplus Kz,\qquad X=K^m,\quad Y=K^m,
\]
with central annihilator \(Kz\) and brackets, for the standard bases,
\[
[e_i,f_j]=\delta_{ij}z,\qquad [f_i,e_j]=\lambda\delta_{ij}z,
\]
all other basis brackets being zero. This is a two-step nilpotent, non-Lie left and right Leibniz algebra. Write \(\pi:L_{m,\lambda}(K)\to X\oplus Y\) for the central quotient map.

Every linear subalgebra \(S\le L_{m,\lambda}(K)\) belongs to exactly one of the following classes:

1. \(z\in S\). Then \(S=\pi^{-1}(W)\) for a unique linear subspace \(W\le X\oplus Y\).
2. \(z\notin S\). Then \(S=\{w+f(w)z:w\in W\}\) for a unique linear subspace \(W\le X\oplus Y\) and a unique linear map \(f:W\to K\), and this is a subalgebra **if and only if** the projection spaces \(U=\operatorname{pr}_X(W)\) and \(T=\operatorname{pr}_Y(W)\) satisfy \(U\perp T\) for the standard nondegenerate pairing \(X\times Y\to K\).

For a prime power \(q\) admitting such a nonzero \(\lambda\in\mathbb F_q\), let \(N_{m,q}(s)\) count all embedded \(s\)-dimensional subalgebras of \(L_{m,\lambda}(\mathbb F_q)\), and define \(P_{m,q}(t)=\sum_{s=0}^{2m+1}N_{m,q}(s)t^s\). Then **the entire distribution is independent of the admissible parameter** and equals
\[
\boxed{
P_{m,q}(t)
=t\sum_{k=0}^{2m}{2m\brack k}_q t^k
+\sum_{a=0}^{m}\sum_{b=0}^{m-a}{m\brack a}_q{m-a\brack b}_q
\sum_{d=0}^{\min(a,b)}{a\brack d}_q{b\brack d}_q
|\operatorname{GL}_d(\mathbb F_q)|\,q^{a+b-d}t^{a+b-d}.
}
\]
The zero-dimensional subalgebra and full algebra are included. The Gaussian coefficients and general linear group orders are defined in the next section. In particular,
\[
P_{1,q}(t)=1+(2q+1)t+(q+1)t^2+t^3,
\]
and
\[
P_{2,4}(t)=1+101t+197t^2+357t^3+85t^4+t^5.
\]
Thus the five-dimensional algebra in this family over \(\mathbb F_4\) has exactly \(742\) subalgebras, of which \(656\) have dimension at most three.

## Assumptions and scope

The only constraints on the field are \(\lambda\ne0\) and \(1-\lambda^2\ne0\); no restriction on characteristic is imposed. Finite-field instances require an admissible parameter (there is none over \(\mathbb F_2\) or \(\mathbb F_3\)). For integers \(n\ge0\) and \(r\in\mathbb Z\), define the Gaussian coefficient \({n\brack r}_q\) to be zero when \(r<0\) or \(r>n\), and otherwise to be
\[
{n\brack r}_q=\prod_{i=0}^{r-1}\frac{q^{n-i}-1}{q^{r-i}-1}.
\]
Set \(|\operatorname{GL}_0(\mathbb F_q)|=1\) and, for \(d\ge1\),
\[
|\operatorname{GL}_d(\mathbb F_q)|=\prod_{i=0}^{d-1}(q^d-q^i).
\]
The counts concern actual embedded linear subalgebras, not isomorphism classes.

## Proof

**Leibniz structure.** Every bracket belongs to \(Kz\), and \(z\) brackets trivially with all elements; consequently all iterated triple brackets vanish, and both Leibniz identities hold. Since \([e_1,f_1]=z\), the derived ideal is exactly \(Kz\). The generic-parameter condition excludes the alternating Lie bracket, and some element has nonzero self-bracket (over a field of any characteristic, \([e_1+f_1,e_1+f_1]=(1+\lambda)z\ne0\)).

**Central dichotomy.** For any linear subalgebra \(S\), the intersection \(S\cap Kz\) is either \(0\) or \(Kz\). In the latter case, \(S\) is necessarily the full inverse image of its quotient space \(W\le X\oplus Y\), and all such inverse images are subalgebras. Otherwise \(\pi|_S\) is injective and \(S\) is the graph of a unique linear map \(f:W\to K\). The graph is closed under brackets precisely when the bilinear form
\[
B((x,y),(x',y'))=x\cdot y'+\lambda y\cdot x'
\]
vanishes for every ordered pair of elements of \(W\), because a nonzero element of \(Kz\) cannot belong to the graph.

For any \(u=(x,y),v=(x',y')\in W\), put \(A=x\cdot y'\) and \(C=x'\cdot y\). The two necessary ordered-bracket equations are \(A+\lambda C=0\) and \(C+\lambda A=0\). Their determinant is \(1-\lambda^2\), which is nonzero. Hence \(A=C=0\) for every \(u,v\in W\), equivalently \(U\perp T\), where \(U=\operatorname{pr}_X(W)\) and \(T=\operatorname{pr}_Y(W)\). The converse follows by reversing this argument. This proves the asserted complete subalgebra classification without any restriction on characteristic.

**Subdirect-product count.** Suppose the field is \(\mathbb F_q\). Fix \(a=\dim U\) and \(b=\dim T\). There are \({m\brack a}_q\) choices of \(U\); then \(T\subseteq U^\perp\), a space of dimension \(m-a\), admits \({m-a\brack b}_q\) choices, forcing \(a+b\le m\).

For fixed \(U,T\), a subspace \(W\le U\oplus T\) has projections onto both \(U,T\) if and only if it is a subdirect product. Put \(I=W\cap U\), \(J=W\cap T\). The natural projections identify \(U/I\) with \(T/J\), so their common dimension is an integer \(d\in[0,\min(a,b)]\), and \(\dim W=a+b-d\). Conversely, any choices of \(I\le U\) of codimension \(d\), \(J\le T\) of codimension \(d\), and an isomorphism \(U/I\to T/J\) determine exactly one subdirect product \(W\), and each \(W\) determines this data uniquely. There are therefore
\[
{a\brack d}_q{b\brack d}_q|\operatorname{GL}_d(\mathbb F_q)|
\]
such subspaces for each \(d\). Each supports exactly \(q^{a+b-d}\) central linear graph maps \(f:W\to\mathbb F_q\).

**Assembly.** For each dimension \(k\in[0,2m]\), there are \({2m\brack k}_q\) subalgebras containing \(z\), each of dimension \(k+1\). Summing these and the disjoint central-free graph classes gives the displayed polynomial, including both endpoints. The derivation also proves independence of \(\lambda\) throughout the admissible region.

## Verification

The standalone file `checker.py` generates all reduced-row-echelon subspaces of the ambient vector space and checks bracket closure on their bases, independently of the subdirect-product argument. It also evaluates the closed Gaussian expression. Run `python checker.py` using standard Python. Exhaustive agreement was obtained for \((m,q,\lambda)=(1,4,2),(2,4,2),(1,5,2),(2,5,2),(1,7,2)\), interpreting \(2\in\mathbb F_4\) as a root of \(u^2+u+1\). Every case returned `VERIFY_OK`; the finite tests independently check instances but are not the proof for all \(m\) and \(q\).

## Relationship to prior work

Mancini and La Rosa's classification of two-step nilpotent Leibniz algebras [1] associates such algebras with bilinear-form data; its Heisenberg-type construction includes scalar-block forms after normalization. The present result uses that structural setting but counts *all embedded subalgebras* and gives a complete dimension generating polynomial for the generic scalar family. Siciliano and Towers [2] study modularity and other order-theoretic properties of subalgebra lattices, including extraspecial Leibniz algebras. Their lattice-theoretic results do not supply the Gaussian rank-by-rank enumeration above. Existing Heisenberg Lie-algebra subalgebra counts concern the alternating boundary parameter, which is excluded by the theorem.

## Limitations

The cases \(\lambda=1\) and \(\lambda=-1\) are not covered; there the two ordered-bracket conditions are dependent and the isotropic geometry changes. The polynomial does not classify subalgebras by abstract isomorphism type or compute their pairwise permutability probabilities. The finite verification is exhaustive only in the specified small instances, and no independent audit of the general proof has been performed. An equivalent enumerative statement in less directly indexed literature remains possible.

## References

[1] M. Mancini and G. La Rosa, *Two-step nilpotent Leibniz algebras*, arXiv:2106.12904v1 (submitted 2021-06-24; full-text revised version arXiv:2106.12904v2). Linear Algebra and its Applications 637 (2022), 119–137. DOI: 10.1016/j.laa.2021.12.013.

[2] S. Siciliano and D. A. Towers, *On the subalgebra lattice of a Leibniz algebra*, arXiv:2010.12254 (2020), Communications in Algebra 50 (2022), 255–267. DOI: 10.1080/00927872.2021.1956510.
