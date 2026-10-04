# Exact evolution dimension of split square-zero local algebras
## Finding
Let \(K\) be a field with \(\operatorname{char}K\ne2\), let \(V\) be an \(r\)-dimensional \(K\)-vector space with \(r\ge1\), and let
\[
A=K\oplus V,\qquad (a,u)(b,v)=(ab,av+bu).
\]
Thus \(A\) is the canonical split local commutative algebra with radical \(V\) and \(V^2=0\). Its minimal evolution dimension is
\[
\operatorname{edim}(A)=2r+1.
\]
Here \(\operatorname{edim}(A)\) is the least dimension of an evolution \(K\)-algebra containing \(A\) as an ideal. Equivalently, the simultaneous Waring rank of the squaring map \(H(a,u)=(a^2,2au)\) is exactly \(2r+1\).

## Assumptions and scope
The result holds for every field of characteristic different from \(2\) and every finite \(r\ge1\). It concerns split local commutative algebras with square-zero radical. Over an algebraically closed field, every finite-dimensional local commutative algebra with residue field \(K\) and square-zero radical is of this form. Characteristic \(2\) is excluded because both polarization and the displayed square decomposition use division by \(2\).

## Proof
Choose a basis \(e_1,\ldots,e_r\) of \(V\), write \(e_0=1\), and let \(x_0,x_1,\ldots,x_r\) be the dual coordinates. The coordinate quadrics of the squaring map span
\[
W=\operatorname{span}\{x_0^2,x_0x_1,\ldots,x_0x_r\}\subseteq \operatorname{Sym}^2(A^*),
\]
so \(\dim W=r+1\).

For the upper bound, define
\[
\ell_0=x_0,\qquad \ell_{i,+}=x_0+x_i,\qquad \ell_{i,-}=x_0-x_i\quad(1\le i\le r).
\]
Then
\[
H=\ell_0^2e_0+\frac12\sum_{i=1}^r\bigl(\ell_{i,+}^2-\ell_{i,-}^2\bigr)e_i.
\]
This is a simultaneous Waring decomposition with \(2r+1\) squares, hence \(\operatorname{wr}(H)\le2r+1\).

For the lower bound, suppose
\[
H=\sum_{j=1}^N\ell_j^2w_j
\]
is any simultaneous Waring decomposition and put \(L=\operatorname{span}\{\ell_1^2,\ldots,\ell_N^2\}\). Every coordinate quadric of \(H\) lies in \(L\), hence \(W\subseteq L\). Write \(\ell_j=a_jx_0+v_j\) with \(v_j\in V^*\), and let
\[
\pi:\operatorname{Sym}^2(Kx_0\oplus V^*)\longrightarrow\operatorname{Sym}^2(V^*)
\]
be the map obtained by setting \(x_0=0\). Since \(\pi(W)=0\),
\[
\dim L\ge \dim W+\dim\pi(L)=r+1+\dim\operatorname{span}\{v_j^2:1\le j\le N\}.
\]
The mixed \(x_0V^*\)-part of \(\ell_j^2\) is \(2a_jx_0v_j\). Because \(W\) contains all of \(x_0V^*\), the vectors \(v_j\) with \(a_j\ne0\) must span \(V^*\). Choose \(r\) linearly independent ones. Their squares are linearly independent in \(\operatorname{Sym}^2(V^*)\): after an invertible change of basis they become the distinct coordinate squares. Therefore \(\dim\pi(L)\ge r\), whence
\[
N\ge\dim L\ge(r+1)+r=2r+1.
\]
Thus \(\operatorname{wr}(H)=2r+1\).

Costoya, Fernández Ouaridi, and Viruel prove for unital finite-dimensional commutative algebras in characteristic different from \(2\) that the minimal evolution dimension equals the simultaneous Waring rank of the squaring map. Applying that bridge gives \(\operatorname{edim}(A)=2r+1\).

## Verification
There is an independent lower-bound check through algebraic complexity. The algebra \(A\) is local of dimension \(r+1\), so the Alder--Strassen bound gives multiplication-tensor rank at least \(2(r+1)-1=2r+1\). Polarizing any simultaneous Waring decomposition of \(H\) produces a bilinear multiplication decomposition of the same length, so \(\operatorname{wr}(H)\) cannot be smaller than \(2r+1\). This agrees with the direct kernel-projection argument above. For \(r=1\), the formula gives \(3\), matching the dual-number case \(K[t]/(t^2)\) covered by the truncated-polynomial family in the motivating preprint.

No finite computation is used to infer the arbitrary-\(r\) statement; the proof is symbolic over every field of characteristic different from \(2\).

## Relationship to prior work
The motivating preprint arXiv:2609.32784v1 establishes the general embedding theory and the Waring-rank interpretation, and its stated application is the one-generator truncated-polynomial family \(K[t]/(t^n)\). Its full-text terminology and section structure do not state the split square-zero radical family above. The present result evaluates the Waring rank exactly for that canonical family and therefore supplies a new closed formula for its minimal evolution dimension.

Classical Alder--Strassen theory gives the lower bound \(2\dim(A)-1\) for the bilinear multiplication rank of a local algebra, and later work characterizes when this bilinear bound is sharp. Those results predate the evolution-envelope problem and do not determine the simultaneous Waring rank or the minimal evolution dimension. Here they serve as an independent lower-bound consistency check rather than as coverage of the claim.

## Limitations
Characteristic \(2\) is not covered. The theorem treats the split square-zero local family; it does not classify evolution dimensions for arbitrary nonsplit local algebras, higher nilpotency index, or nonlocal commutative algebras. The literature searches did not locate an equivalent evolution-dimension formula under the aliases checked, but very recent work may not yet be comprehensively indexed.

## References
1. Cristina Costoya, Amir Fernández Ouaridi, Antonio Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1, first submitted 2026-09-26.
2. A. Alder, V. Strassen, *On the algorithmic complexity of associative algebras*, Theoretical Computer Science 15 (1981), 201--211, DOI:10.1016/0304-3975(81)90070-0.
3. Markus Bläser, *A complete characterization of the algebras of minimal bilinear complexity*, SIAM Journal on Computing 34 (2004), 277--298, DOI:10.1137/S0097539703438277.
