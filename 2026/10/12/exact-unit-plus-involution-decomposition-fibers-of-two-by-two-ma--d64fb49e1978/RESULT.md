# Exact unit-plus-involution decomposition fibers of two-by-two matrices over odd finite fields

## Finding
For every finite field \(F=\mathbb F_q\) of odd cardinality \(q\), define the *ordered unit-plus-involution fiber* of \(A\in M_2(F)\) by
\[
N_q(A)=\#\{(U,V)\in\operatorname{GL}_2(F)\times M_2(F): U+V=A,\ V^2=I_2\}.
\]
The involution convention includes the identity and its negative, both satisfying \(V^2=I_2\). The following cases give \(N_q(A)\) exactly for **every** matrix, including every singular, invertible, scalar, and nonscalar matrix.

Let \(t=\operatorname{tr}A\), \(d=\det A\), \(a=t/2\), \(B=A-aI_2\), \(\delta=a^2-d\), and \(\lambda=(1-d)/2\), with arithmetic in \(F\). Put
\[
E(A)=\mathbf1_{d-t+1\ne0}+\mathbf1_{d+t+1\ne0}.
\]
If \(B=0\), then
\[
\boxed{N_q(A)=q(q+1)\mathbf1_{d\ne1}+E(A).}
\]
If \(B\ne0\), set
\[
H_q(B,\lambda)=\begin{cases}
2q,&\delta=0,\ \lambda=0,\\
q,&\delta=0,\ \lambda\ne0,\\
q-\chi_q(\delta)+q\chi_q(\delta)\mathbf1_{\lambda^2=\delta},&\delta\ne0,
\end{cases}
\]
where \(\chi_q(\delta)\in\{-1,1\}\) is the quadratic character of a nonzero field element. Then
\[
\boxed{N_q(A)=q(q+1)-H_q(B,\lambda)+E(A).}
\]
The formula applies without a choice of coordinates or algebraic closure and is invariant under similarity of \(A\).

It has a sharp robustness consequence: \(N_q(A)=1\) holds **exactly** for \(A=I_2\) or \(A=-I_2\). Every other matrix admits at least \(q^2-q+1\) representations, and this is attained exactly by (i) nonscalar involutions and (ii) nonscalar Jordan blocks with eigenvalue \(+1\) or \(-1\). Exactly \(3q^2+q-2\) matrices attain this second-smallest fiber size. All other scalar matrices have \(q^2+q+2\) representations.

## Assumptions and scope
The field has **odd** characteristic, so \(2\) is invertible and \(V^2-I_2\) is separable. No primality restriction beyond the odd prime-power field cardinality is imposed; the result includes extension fields. The two summands are ordered by their distinct required properties, so one involution \(V\) contributes exactly one pair \((A-V,V)\). We do not count decompositions into two arbitrary units, decompositions involving idempotents, or the characteristic-two case.

## Proof
**1. All involutions.** Every solution of \(V^2=I_2\) in odd characteristic is diagonalizable with eigenvalues in \(\{1,-1\}\). It is one of the two scalar matrices \(\pm I_2\), or it has trace zero and determinant \(-1\). The latter have the unique form
\[
V=\begin{pmatrix}u&v\\w&-u\end{pmatrix},\qquad u^2+vw=1.
\]
For a fixed \(u\), the product \(vw\) has \(2q-1\) solutions when it is zero and \(q-1\) solutions when it is nonzero. As \(u=\pm1\) are the only two zero-product cases, the number of nonscalar involutions is
\[
2(2q-1)+(q-2)(q-1)=q(q+1).
\]
The scalar choices \(V=\pm I_2\) yield an invertible difference precisely when \(\det(A\mp I_2)=d\mp t+1\ne0\). Hence their contribution is \(E(A)\).

**2. The singularity plane for nonscalar involutions.** For every traceless nonscalar involution \(V\), direct expansion of the \(2\times2\) determinant gives
\[
\det(A-V)=d-1+\operatorname{tr}(AV)=d-1+\operatorname{tr}(BV).
\]
The vector space \(T\) of traceless \(2\times2\) matrices carries the nondegenerate quadratic form
\[
Q\left(\begin{pmatrix}u&v\\w&-u\end{pmatrix}\right)=u^2+vw=-\det V.
\]
Its associated symmetric bilinear form is \(\langle X,Y\rangle=\operatorname{tr}(XY)/2\). In particular \(Q(B)=\delta\) and \(Q(V)=1\). Thus the number of nonscalar involutions forbidden by singularity of \(A-V\) is exactly
\[
H=\#\{V\in T:Q(V)=1,\ \langle B,V\rangle=\lambda\}.
\]
If \(B=0\), the trace constraint is either automatic when \(d=1\) (giving \(H=q(q+1)\)) or impossible when \(d\ne1\) (giving \(H=0\)). This proves the scalar case.

**3. The nilpotent section.** Suppose \(B\ne0\) and \(\delta=Q(B)=0\). Since \(B\) is traceless, Cayley–Hamilton gives \(B^2=0\), and every nonzero nilpotent \(2\times2\) matrix is similar to \(E_{12}\). Simultaneous conjugation preserves \(Q\) and \(\langle\ ,\ \rangle\), so take \(B=E_{12}\). For \(V=\left(\begin{smallmatrix}u&v\\w&-u\end{smallmatrix}\right)\), the trace constraint fixes \(w=2\lambda\). If \(\lambda=0\), the conic equation reduces to \(u^2=1\) and leaves \(v\) arbitrary, yielding \(H=2q\). Otherwise \(w\ne0\) and the conic equation determines \(v=(1-u^2)/w\) for each \(u\), yielding \(H=q\).

**4. The nonisotropic section.** Suppose \(\delta\ne0\). The traceless matrix \(B\) satisfies \(B^2=\delta I_2\) and is nonscalar, so it has cyclic companion form \(\left(\begin{smallmatrix}0&\delta\\1&0\end{smallmatrix}\right)\) under conjugation. For each \(V\) in the required trace hyperplane, write uniquely
\[
V=(\lambda/\delta)B+W,\qquad \langle B,W\rangle=0.
\]
The equation \(Q(V)=1\) becomes \(Q(W)=1-\lambda^2/\delta\). Writing \(W=\left(\begin{smallmatrix}u&-\delta w\\w&-u\end{smallmatrix}\right)\) identifies the restriction of \(Q\) to \(B^\perp\) with \(u^2-\delta w^2\).

If \(\delta\) is a square, this binary form splits into a product of two independent linear factors. The level \(0\) contains \(2q-1\) solutions and every nonzero level contains \(q-1\) solutions. If \(\delta\) is a nonsquare, the form is the norm on \(\mathbb F_{q^2}\): only \((0,0)\) has norm zero, and each nonzero field value has \(q+1\) preimages, by the cyclicity of the finite-field multiplicative group. These two cases combine as
\[
H=q-\chi_q(\delta)+q\chi_q(\delta)\mathbf1_{\lambda^2=\delta}.
\]
Subtracting \(H\) from the \(q(q+1)\) nonscalar involutions and adding the two scalar contributions proves the exact formula.

**5. Extremal fibers and their number.** If \(B=0\), then \(A=aI_2\). At \(a=\pm1\), all nonscalar involutions make \(A-V\) singular and exactly one of \(A-I_2,A+I_2\) is invertible, so \(N_q(A)=1\). Otherwise both scalar differences are invertible and all nonscalar differences are invertible, so \(N_q(A)=q(q+1)+2\).

Now suppose \(B\ne0\). For \(\delta=0,\lambda=0\), the identities \(d=1\) and \(a^2=d=1\) make \(A\) a nonscalar Jordan matrix with eigenvalue \(+1\) or \(-1\). Its scalar contribution is \(E=1\), hence \(N=q(q+1)-2q+1=q^2-q+1\). When \(\delta=0,\lambda\ne0\), one instead has \(H=q\) and \(N\ge q^2\). When \(\delta\ne0\), one has \(H\le2q-1\); equality requires \(\delta\) square and \(\lambda^2=\delta\). Consequently \(N\ge q^2-q+1\), with equality precisely when also \(E=0\). Both determinants \(d-t+1\) and \(d+t+1\) then vanish, forcing \(t=0,d=-1\), which by Cayley–Hamilton is exactly \(A^2=I_2\). These are nonscalar involutions because \(B\ne0\). All other possibilities give strictly larger \(N\).

There are \(q(q+1)\) nonscalar involutions by Step 1. Each of the two nontrivial Jordan similarity classes at eigenvalues \(\pm1\) has \(q^2-1\) members: its centralizer in \(\operatorname{GL}_2(F)\) has order \(q(q-1)\), whereas \(|\operatorname{GL}_2(F)|=q(q-1)^2(q+1)\). These classes are disjoint from each other and from the involutions. The total is therefore \(q(q+1)+2(q^2-1)=3q^2+q-2\). This proves both the sharp bound and the classification.

## Verification
The accompanying standalone Python 3 file `verify.py` checks the theorem against every matrix and every involution over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\), and over the quadratic extension \(\mathbb F_9=\mathbb F_3[\theta]/(\theta^2+1)\). It checks the exact fiber count for each of \(81+625+2401+14641+6561=24309\) matrices, the total involution number, and the sharp extremal count. Execute `python3 verify.py` from the extracted files. The successful output ends with `VERIFY_OK`.

## Relationship to prior work
Luo, Lei, and Ji (2025) study the full number of representations of matrices as sums of **arbitrary** units. Their two-summand count depends only on the rank of the matrix; it cannot determine the present restricted fiber, which is sensitive to conjugacy data. For instance, over \(\mathbb F_5\), the invertible matrices \(I_2\) and \(2I_2\) have respectively \(1\) and \(32\) unit-plus-involution representations despite equal rank. Kirova's 2026 English translation and extension of a 2019 study addresses **existence** of unit-plus-involution representations for formal matrix rings rather than exact finite-field multiplicities. McDonald's classical 1972 work counts and classifies involutory matrices over finite local rings but does not provide the cardinality of their intersection with a translate of the singular locus, which is the quantity counted here. The 2026 arXiv version of Kirova's text is not treated as an original 2026 source for older results.

## Limitations
Odd characteristic is necessary for the diagonalization and quadratic-section arguments. No formula is claimed for characteristic \(2\), higher matrix sizes, general finite rings, or counting decompositions up to conjugacy. Exhaustive tests cover only the five explicitly named fields and cannot replace the unrestricted proof. The novelty comparison is limited to the cited sources and searches and is not a certificate that no historical equivalent exists.

## References
1. Y. Luo, K. Lei, and Q. Ji, *On the sumsets of units in a ring of matrices over \(\mathbb Z/m\mathbb Z\)*, Electronic Research Archive 33 (2025), 1323–1332. DOI: 10.3934/era.2025059. First public date verified on publisher website: 2025-03-05. https://doi.org/10.3934/era.2025059
2. V. Kirova, *Formal Matrix Rings with the Involution Property*, arXiv:2610.04709v1 (2026), explicitly described as a translation and extension of a 2019 Russian conference publication. https://arxiv.org/abs/2610.04709
3. B. R. McDonald, *Involutory Matrices Over Finite Local Rings*, Canadian Journal of Mathematics 24 (1972), 369–378. DOI: 10.4153/CJM-1972-030-x. https://doi.org/10.4153/CJM-1972-030-x
