# Cubic holonomy controls splitting in an infinite family of simple evolution algebras

## Finding

**Theorem (cubic holonomy and the splitting boundary).** Let \(K\) be a field of characteristic different from \(2\) and \(3\), and assume that \(K\) contains a primitive cube root of unity. Fix \(n\ge3\) and \(c_i\in\mu_3(K)\) for \(i\in\mathbb Z/n\mathbb Z\). Define an evolution algebra \(E_{n,\mathbf c}\) by
\[
a_i^2=b_i+c_i b_{i+1},\qquad b_i^2=a_i,
\]
with products between any two distinct natural basis elements zero. Set \(P=\prod_{i=0}^{n-1}c_i\).

Then \(E_{n,\mathbf c}\) is perfect exactly when \(n\) is odd or \(P\ne1\). Every perfect member is simple, and
\[
\operatorname{Aut}(E_{n,\mathbf c})\cong
\begin{cases}
 C_3\times C_n,&P=1,\\
 C_{3n},&P\ne1.
\end{cases}
\]
The sequence of abstract groups of \(K\)-automorphisms
\[
1\longrightarrow C_3\longrightarrow \operatorname{Aut}(E_{n,\mathbf c})
\longrightarrow C_n\longrightarrow1
\]
splits **if and only if** \(P=1\) or \(3\nmid n\). In particular, choosing \(c_0=\zeta\ne1\) and all other \(c_i=1\) yields a nonsplit simple example for every multiple of three \(n\ge3\), in unbounded dimension. For every odd multiple of three, choosing all \(c_i=1\) instead gives a simple split example with the identical directed support graph.

## Assumptions and scope

Indices are read modulo \(n\). The group \(\mu_3(K)=\{t\in K^\times:t^3=1}\) has exactly three members under the stated field conditions. The classification concerns ordinary \(K\)-algebra automorphisms as an abstract finite group, not the full automorphism group scheme or extensions over arbitrary field changes. The coefficients are constrained to \(\mu_3(K)\); no claim is made for unrestricted weights. At even \(n\) with \(P=1\), the algebra is not perfect and the asserted automorphism classification does not apply.

## Proof

**1. Perfection and simplicity.** Order the natural basis with all \(a_i\) first, then all \(b_i\). Its structure matrix has block form \(\left(\begin{smallmatrix}0&B\\I&0\end{smallmatrix}\right)\), where \(B=I+\operatorname{diag}(c_i)S\) and \(S\) is the cyclic shift. In the permutation expansion of \(\det B\), only the identity permutation and the full cyclic shift survive, so
\[
\det B=1-(-1)^nP,\qquad
\det M=(-1)^n-P.
\]
If \(n\) is even this determinant vanishes precisely when \(P=1\). If \(n\) is odd, it is \(-1-P\ne0\): an element of order dividing three cannot equal \(-1\) in characteristic different from two. Hence the perfection criterion. The directed graph has \(b_i\to a_i\), \(a_i\to b_i\) and \(a_i\to b_{i+1}\), and is strongly connected for every \(n\ge3\). A perfect evolution algebra with strongly connected graph is simple: any nonzero ideal contains a basis square through coordinate multiplication and, from a nonzero basis-square component, reaches all basis elements by successive squares. Equivalently this is the standard graph simplicity criterion [1, Section 1.1, Theorem 6].

**2. Monomiality and the graph quotient.** For a perfect evolution algebra the squares of its natural basis are linearly independent. If \(F\) is an automorphism, the natural basis \(F(a_i),F(b_i)\) has pairwise zero mixed products; expanding two such products in the old basis and using independence of all basis squares shows their supports are disjoint. Since their number equals the dimension and all are nonzero, each support is a singleton. Thus \(F\) is monomial and its permutation is an automorphism of the directed support graph. The \(a_i\) are exactly the vertices of outdegree two and \(b_i\) those of outdegree one; each \(b_i\) points uniquely to \(a_i\). The additional arrow \(a_i\to b_{i+1}\) forces the permutation of indices to preserve the directed cycle \(i\to i+1\). Therefore the graph automorphism group is precisely the cyclic rotation group \(C_n\), with rotations \(i\mapsto i+k\).

**3. The diagonal kernel.** If \(F(a_i)=\alpha_i a_i\) and \(F(b_i)=\beta_i b_i\), the relations \(b_i^2=a_i\) and \(a_i^2=b_i+c_i b_{i+1}\) imply
\[
\alpha_i=\beta_i^2,\qquad \beta_i=\alpha_i^2=\beta_{i+1}.
\]
All \(\beta_i=t\) are equal, and the remaining equation is \(t^3=1\). Hence the diagonal kernel is \(\mu_3(K)\cong C_3\), with \(\delta_t(a_i)=t^2a_i\) and \(\delta_t(b_i)=tb_i\).

**4. A lift and its holonomy.** Define
\[
\phi(a_i)=c_i^2a_{i+1},\qquad \phi(b_i)=c_ib_{i+1}.
\]
The identity \(c_i^3=1\) gives \(\phi(b_i)^2=\phi(b_i^2)\) and
\[
\phi(a_i)^2=c_i^4(b_{i+1}+c_{i+1}b_{i+2})
=c_i b_{i+1}+c_ic_{i+1}b_{i+2}=\phi(a_i^2).
\]
Thus \(\phi\) is an automorphism lifting the one-step rotation. Going round the cycle gives
\[
\phi^n(a_i)=P^2a_i,\quad\phi^n(b_i)=Pb_i,\quad
\phi^n=\delta_P.
\]
Every \(\delta_t\) commutes with \(\phi\). Since every monomial automorphism projects to a power of the rotation and its kernel is exactly \(\mu_3(K)\), the full group is \(\langle\phi,\delta_t:t^3=1\rangle\) of cardinality \(3n\).

**5. Splitting.** If \(P=1\), then \(\phi^n=1\), and \(\phi\) has exact order \(n\) from its permutation; consequently \(\langle\phi\rangle\) is a complement to the central kernel, so the group is \(C_n\times C_3\). If \(P\ne1\), then \(P\) has order three and \(\phi^n=\delta_P\) generates the diagonal kernel. Therefore \(\phi\) has order \(3n\) and is a generator of the entire group \(C_{3n}\). An element of order \(n\) in \(C_{3n}\) maps onto its quotient \(C_n\) precisely when \(\gcd(3,n)=1\), which proves the sharp splitting criterion. All assertions follow. \(\square\)

## Verification

The standalone script `verify.py` evaluates multiplication tables over \(\mathbb F_7\), \(\mathbb F_{13}\) and \(\mathbb F_{19}\). It confirms the determinant and perfection criteria for 1,314 coefficient tuples, verifies 15,390 explicit monomial lifts directly against all defining square relations, and in 81 small cases exhaustively enumerates all rotation-permitted monomial coefficient choices and recovers precisely \(3n\) automorphisms. Run: `python3 verify.py`; expected final marker `VERIFY_OK`. These are finite checks of the formulas; the proof above is uniform in all allowed fields and integers.

## Relationship to prior work

Kaygorodov, Martín González and Viruel [1, Proposition 21] explicitly construct a **six-dimensional** perfect evolution algebra with nonsplit automorphism extension \(C_3\to C_9\to C_3\). Their example agrees, after cyclic relabelling, with the case \(n=3\), \(P\ne1\) here, and **is not claimed as a new case**. Their Question 33 explicitly asks for the splitting conditions in the Elduque–Labra sequence. The present result supplies an infinite family with an exact multiplicative holonomy criterion; for odd multiples of three the same graph realizes both split and nonsplit groups. Elduque and Labra [2] introduce the general graph-dependent automorphism exact sequence and earlier small nonsplitting phenomena, without this particular arbitrary-length criterion. Sriwongsa and Zou [3] study automorphism groups of perfect evolution algebras and cycle-type constructions, but do not state this two-cycle-linked weighted holonomy family. The related previously indexed work on single oriented-cycle algebras concerns a different graph (one basis element per cycle vertex), not this strongly connected doubled graph.

## Limitations

Only coefficients in \(\mu_3(K)\) are treated, and only the ordinary automorphism group on field points is classified. The case \(n=3\), \(P\ne1\) was already known [1]. There may be earlier general machinery from graph automorphism extensions that can derive the new family without its explicit formulation; that is the principal residual originality risk. No independent mathematical audit is claimed.

## References

[1] I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 15 October 2026, Sections 2.1.9 and 2.2.5, Proposition 21 and Question 33. https://arxiv.org/html/2610.22248v1

[2] A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191v1 (2019), published in Linear and Multilinear Algebra. https://arxiv.org/abs/1902.02191

[3] S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333v1 (2022). https://arxiv.org/abs/2202.01333
