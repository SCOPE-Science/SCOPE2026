# A four-dimensional solvable Lie family with uniform subalgebra commutativity degree

## Finding
For any finite field \(K=\mathbb F_q\) with \(q>2\) and any \(\lambda\in K\setminus\{0,1\}\), consider the four-dimensional Lie algebra \(L_\lambda\) with basis \(e,u_1,u_2,v\) and independent nonzero brackets
\[
[e,u_1]=u_1,\qquad [e,u_2]=u_2,\qquad [e,v]=\lambda v.
\]
Its subalgebra lattice has
\[
N(q)=2q^3+5q^2+4q+5
\]
members. Exactly
\[
B(q)=q^2(q-1)(q+1)^2(3q+1)
\]
ordered pairs of subalgebras fail to be permutable. Consequently, with permutability defined by \([A,B]\subseteq A+B\),
\[
\operatorname{sd}(L_\lambda)
=1-\frac{q^2(q-1)(q+1)^2(3q+1)}{(2q^3+5q^2+4q+5)^2}
=\frac{q^6+16q^5+43q^4+64q^3+67q^2+40q+25}{(2q^3+5q^2+4q+5)^2}.
\]
The degree tends to \(1/4\) as \(q\to\infty\), independently of \(\lambda\). For fixed \(q>2\), the \(q-2\) choices of \(\lambda\) give pairwise nonisomorphic Lie algebras with this same degree.

## Assumptions and scope
All subalgebras and vector spaces are over \(K\). A pair of Lie subalgebras \((A,B)\) is *permutable* when its vector-space sum \(A+B\) is a Lie subalgebra, equivalently \([A,B]\subseteq A+B\). The degree \(\operatorname{sd}\) is the fraction of ordered pairs that are permutable, including the zero subalgebra and the whole algebra. The characteristic is unrestricted; \(q>2\) is necessary only to admit \(\lambda\ne0,1\).

Put \(V=\langle u_1,u_2,v\rangle\), \(X=\langle u_1,u_2\rangle\), \(Y=\langle v\rangle\), and let \(T=\operatorname{ad}_e|_V\). Thus \(V=X\oplus Y\) is abelian and \(T\) acts as \(1\) on \(X\) and as \(\lambda\) on \(Y\). Since \(\lambda\ne0\), \([L_\lambda,L_\lambda]=V\).

## Proof
**1. Parametrizing all subalgebras.** Every subalgebra contained in \(V\) is an arbitrary subspace of this three-space, giving
\[
I(q)=\sum_{k=0}^{3}{3\brack k}_q=2q^2+2q+4.
\]
Every subalgebra not contained in \(V\) is uniquely of the form \(K(e+w)+W\), where \(W\le V\) is \(T\)-invariant and \(w\in V/W\). Because \(\lambda\ne1\), spectral projections show that each invariant \(W\) decomposes as \(W_X\oplus W_Y\), with \(W_X\le X\) and \(W_Y\in\{0,Y\}\). For \(\dim W_X=i\), there are \({2\brack i}_q\) choices, and the number of corresponding external subalgebras, summed over the two choices of \(W_Y\), is
\[
E(q)=\sum_{i=0}^2{2\brack i}_q
\bigl(q^{3-i}+q^{2-i}\bigr)
=(q+1)(2q^2+q+1).
\]
Thus \(N(q)=I(q)+E(q)=2q^3+5q^2+4q+5\).

**2. Pairs with one subalgebra inside \(V\).** Two subalgebras contained in \(V\) always permute. Let \(A\le V\) and \(B=K(e+w)+W\). Their sum is a subalgebra precisely when \(A+W\) is \(T\)-invariant; the choice of \(w\) is immaterial. All \(A\) work whenever \(W\supseteq Y\) or \(W\supseteq X\), because \(V/W\) then carries a scalar action.

For \(W=0\), exactly \(2(q^2-1)\) internal subalgebras are not invariant: all \(I(q)\) subspaces minus the \(2(q+3)\) direct sums of subspaces of \(X\) and \(Y\). This \(W\) has \(q^3\) external choices. For a line \(W\le X\), there are \(q+1\) such \(W\), each with \(q^2\) external choices. The quotient \(V/W\) has two distinct one-dimensional eigenspaces. Of its four invariant subspaces, the zero subspace has two preimages \(A\) under projection, each eigenspace has \(q+1\), and the full quotient has \(q^2+1\); thus exactly \(q^2+2q+5\) subspaces \(A\) give invariant \(A+W\). The number that fail is \(I(q)-(q^2+2q+5)=q^2-1\).

Hence the number of *ordered* nonpermutable pairs with one subalgebra inside \(V\) and the other outside is
\[
B_{IE}=2\bigl(2q^3(q^2-1)+(q+1)q^2(q^2-1)\bigr)
=2q^2(q^2-1)(3q+1).
\]

**3. Pairs with both subalgebras outside \(V\).** Write \(B_i=K(e+w_i)+W_i\), with invariant \(W_i\). Put \(Z=W_1+W_2\) and \(d=w_2-w_1\bmod Z\). Their sum is a subalgebra precisely when \(Td\in Kd\) in \(V/Z\). Since \(T\) has two distinct eigenvalues, this fails exactly when the images of \(d\) in both \(X/Z_X\) and \(Y/Z_Y\) are nonzero. If \(Z\) has eigenspace quotient dimensions \(a,b\), the number of bad difference classes is \((q^a-1)(q^b-1)\). Each specified difference class occurs for exactly \(q^{3-\dim(W_1\cap W_2)}\) pairs \((w_1,w_2)\).

Failures require \(W_{1,Y}=W_{2,Y}=0\) and \(W_{1,X}+W_{2,X}\ne X\). The only possibilities for \((W_{1,X},W_{2,X})\) are: two zero subspaces; zero and a line in either order; or the same line twice. Their respective contributions are
\[
q^3(q^2-1)(q-1),\qquad
2(q+1)q^3(q-1)^2,\qquad
(q+1)q^2(q-1)^2.
\]
It follows that
\[
B_{EE}=q^2(q-1)^2(q+1)(3q+1).
\]
Adding \(B_{IE}\) and \(B_{EE}\) yields precisely \(B(q)\).

**4. Isomorphism types and limit.** The derived ideal \(V\) is characteristic. An isomorphism \(L_\lambda\cong L_\mu\) must intertwine \(T_\lambda\) with a nonzero scalar multiple of \(T_\mu\). The repeated eigenvalue has multiplicity two and is uniquely distinguished from the other eigenvalue; hence the scalar is \(1\) and \(\lambda=\mu\). The leading terms of \(B(q)\) and \(N(q)^2\) are \(3q^6\) and \(4q^6\), respectively, establishing the limit \(1/4\).

## Verification
The standalone program `artifacts/verify.py` enumerates every vector subspace of \(K^4\) in reduced row-echelon form, tests closure under the original Lie bracket, then checks all ordered pairs of genuine subalgebras by taking their vector-space sum. Full exhaustive checks give \((N,B)=(116,2880)\) for \((q,\lambda)=(3,2)\), \((N,B)=(229,15600)\) for both admissible choices over \(\mathbb F_4\), and \((N,B)=(400,57600)\) for all three admissible choices over \(\mathbb F_5\). The extension field is implemented with \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\). Execution ends with `VERIFY_OK`. The general finite-field result is proved algebraically, not inferred from finite checks.

## Relationship to prior work
Muhie, Otera, and Russo introduced the subalgebra commutativity-degree problem for finite-dimensional Lie algebras over finite fields, including a study of Heisenberg algebras. A published full proof of the three-dimensional classification relates the degree to the number of subalgebra planes. A separate exact four-dimensional calculation concerns \(\mathfrak h_3\oplus K\), a nilpotent algebra with a two-dimensional center, rather than the center-free solvable algebra here. Its formula and subalgebra count are different. None of those inspected statements implies the present two-eigenspace four-dimensional count. The motivating 2026 article's abstract was available, but its complete text could not be retrieved: a previously unstated example inside it remains a comparison risk.

## Limitations
The count applies only to the four-dimensional split family with eigenvalue multiplicities two and one and \(\lambda\ne0,1\). It does not cover singular actions, scalar actions, nonsplit Jordan operators, or arbitrary four-dimensional solvable Lie algebras. The proof does not establish historical novelty against inaccessible or unindexed sources, and no independent mathematical audit has been carried out.

## References
1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1, first public 2026-09-16, https://arxiv.org/abs/2609.19086.
2. *Plane counts control subalgebra commutativity in dimension three*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c.
3. *Exact subalgebra commutativity degree after a one-dimensional central stabilization of the Heisenberg algebra*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-subalgebra-commutativity-degree-after-a-one-dimensional-ce--246d7542fd6a.
