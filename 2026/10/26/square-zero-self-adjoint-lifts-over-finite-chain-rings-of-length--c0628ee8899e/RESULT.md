# Square-zero self-adjoint lifts over finite chain rings of length two

## Finding
Let \(R\) be **any** finite commutative chain ring of length two with maximal ideal \((\pi)\), residue field \(k=\mathbb F_q\) of odd order, and let \(g\) be any nonsingular symmetric bilinear form on \(R^n\), where \(n\ge2\). Write \(\overline g\) for its reduction and let \(\mathcal Z_g(R)=\{X\in\operatorname{End}_R(R^n):X^2=0,\;g(Xu,v)=g(u,Xv)\}\). For \(0\le r\le\lfloor n/2\rfloor\), let \(Z_{n,r}(R,g)\) count elements of \(\mathcal Z_g(R)\) whose reduction has rank \(r\), and put \(s=n-2r\). Then
\[
\boxed{Z_{n,r}(R,g)=I_{n,r}(q,\overline g)\,S_r(q)\,q^{r^2+rs+s(s+1)/2}.}
\]
Here \(I_{n,r}\) counts totally isotropic \(r\)-subspaces of the nondegenerate quadratic space \((k^n,\overline g)\), and \(S_r\) counts invertible symmetric \(r\times r\) matrices over \(k\). In particular, the answer is **independent of the characteristic and isomorphism type of the length-two coefficient ring**, once \(q\) and the reduced orthogonal type are fixed. The cardinality of \(\mathcal Z_g(R)\) is the sum of these explicitly evaluated quantities.

For completeness, \(I_{n,0}=S_0=1\). If \(n=2m+1\), then
\[
I_{n,r}=\prod_{j=0}^{r-1}\frac{q^{2(m-j)}-1}{q^{r-j}-1}.
\]
For \(n=2m\), let \(\eta=+1\) for hyperbolic type and \(\eta=-1\) for elliptic type, and use
\[
I_{n,r}=\prod_{j=0}^{r-1}\frac{(q^{m-j}-\eta)(q^{m-j-1}+\eta)}{q^{r-j}-1}.
\]
The latter formula yields zero beyond the Witt index. Write \(G_a(q)=\prod_{i=0}^{a-1}(q^a-q^i)\), with \(G_0=1\). Then
\[
S_{2h+1}(q)=\frac{G_{2h+1}(q)}{q^{h^2}\prod_{i=1}^{h}(q^{2i}-1)},\qquad
S_{2h}(q)=\frac{G_{2h}(q)q^{h}}{q^{h(h-1)}\prod_{i=1}^{h}(q^{2i}-1)}\quad(h\ge1).
\]
These are integers although displayed as rational products. The formula concerns a fixed nonsingular form \(g\), not an average over forms.

## Assumptions and scope
A chain ring of length two has ideals \(0\subset(\pi)\subset R\), with \(\pi^2=0\) and \(|R|=q^2\). No coefficient-field embedding is assumed: \(R\) can have characteristic \(p^2\) or \(p\). The residue characteristic is odd, so \(2\in R^\times\). We count labeled endomorphisms on a fixed free module, not similarity or orthogonal-conjugacy classes. The zero endomorphism occurs in the \(r=0\) stratum, along with every \(\pi B\) for self-adjoint \(B\) modulo \(\pi\). Rank refers to the reduced map, not the rank of the underlying finite abelian group.

## Proof
**1. The special fiber.** Let \(A\) be self-adjoint and square-zero on \((k^n,\overline g)\), and let \(U=\operatorname{im}A\) have dimension \(r\). Since \(\overline g(Ax,Ay)=\overline g(x,A^2y)=0\), \(U\) is totally isotropic. Self-adjointness and nondegeneracy imply \(\ker A=U^\perp\). Thus \(A\) factors as an isomorphism \(k^n/U^\perp\to U\), and the canonical duality \(k^n/U^\perp\simeq U^*\) identifies it with a nondegenerate symmetric tensor in \(U\otimes U\). Conversely every totally isotropic \(U\) and every invertible symmetric map \(U^*\to U\) give one such \(A\). The number of rank-\(r\) special-fiber maps therefore is \(I_{n,r}S_r\); in characteristic odd the standard orders of orthogonal groups and the polar-Grassmannian point counts yield the product expressions above.

**2. Existence of lifts.** Fix such an \(A\). Choose a Witt basis \(U\oplus W\oplus U'\) modulo \(\pi\), with \(\dim U=\dim U'=r\) and \(\dim W=s\). Lift the basis to \(R\); correct the lifted isotropic generators by their dual generators using the invertibility of \(2\) and \(\pi^2=0\). This produces an exact hyperbolic decomposition over \(R\) reducing to the given one. Lift the invertible symmetric \(r\times r\) matrix defining \(A\) to a symmetric matrix over \(R\), and define \(X_0\) to map \(U'\) to \(U\) by that matrix and kill \(U\oplus W\). Then \(X_0\) is exactly square-zero, self-adjoint, and reduces to \(A\). This construction also works in mixed characteristic.

**3. Dimension of a lifting fiber.** Every self-adjoint lift of \(A\) is uniquely \(X=X_0+\pi B\), where \(B\) is a self-adjoint \(k\)-endomorphism. The condition \(X^2=0\) is exactly \(AB+BA=0\) modulo \(\pi\). Identifying self-adjoint \(B\) with \(\operatorname{Sym}^2(k^n)\) via \(\overline g\), this is the kernel of the linear map induced by \(A\otimes1+1\otimes A\) on symmetric tensors. As a \(k[t]\)-module, \((k^n,A)\) is the sum of \(r\) length-two Jordan modules and \(s\) trivial modules. Because \(2\ne0\), the induced map has nullity \(1\) on the symmetric square of each length-two summand, nullity \(2\) on each tensor product of two distinct length-two summands, nullity \(1\) on each length-two/trivial pair, and nullity \(1\) on each symmetric or distinct pair of trivial summands. Its kernel dimension is
\[
r+2\binom r2+rs+\frac{s(s+1)}2=r^2+rs+\frac{s(s+1)}2.
\]
There are precisely \(q^{r^2+rs+s(s+1)/2}\) possible \(B\). Multiplication by \(\pi\) identifies matrices over the residue field with the radical layer, so the fiber count holds even without a ring splitting. Summing over the \(I_{n,r}S_r\) special-fiber endomorphisms proves the formula.

**4. Consequences.** For \(n=2\), a hyperbolic form gives \(q^3+2q(q-1)\) solutions while an elliptic form gives \(q^3\). For odd \(n=3\), every nonsingular symmetric form gives exactly \(q^6+(q+1)(q-1)q^3\) solutions. For hyperbolic \(n=4\), the rank-stratum formula yields \(q^{10}+(q+1)^2(q-1)q^6+2(q+1)q^2(q-1)q^4\). The rank-\(r\) stratum of the special fiber lifts to a constant-sized affine torsor of dimension \(r^2+rs+s(s+1)/2\), showing explicitly how singular lifting multiplicities vary with rank.

## Verification
Run `python3 symmetric_checker.py` using only the Python standard library. It independently enumerates every \(2\times2\) self-adjoint square-zero matrix over \(\mathbb Z/9\), \(\mathbb F_3[\varepsilon]/\varepsilon^2\) and \(\mathbb Z/25\), and every \(3\times3\) such matrix over \(\mathbb Z/9\) and \(\mathbb F_3[\varepsilon]/\varepsilon^2\), with standard split Gram matrices. The exact checked rank-stratum counts are \((27,12)\), \((27,12)\), \((125,40)\), \((729,216)\), and \((729,216)\), respectively, for reduced ranks \(0,1\). Exhaustive cases confirm the formulas but the all-dimensional proof is the tensor-Jordan argument above.

## Relationship to prior work
Brouwer, Gow and Sheekey count nilpotent self-adjoint matrices over finite **fields**, with arbitrary nilpotency index and form type, and their paper provides the closest primary field-level context. The present theorem instead counts **square-zero lifts over finite coefficient rings of length two** and resolves every special-fiber rank stratum by a previously absent factor depending on the residue rank. Finite-field counting alone does not imply lifting-fiber sizes. Prasad, Singla and Spallone study similarity of general matrices over length-two rings, not this self-adjoint nilpotent lifting census. Standard orthogonal subspace and symmetric form counts are inputs, not claimed new.

## Limitations
The residue characteristic is assumed odd: in characteristic two the symmetric-tensor argument and isotropic lifting require different treatment. This is a labeled-matrix census, not a similarity classification, and treats coefficient rings of length exactly two only. A general historical publication-priority guarantee and independent mathematical audit have not been obtained.

## References
1. A. E. Brouwer, R. Gow, J. Sheekey, *Counting Symmetric Nilpotent Matrices*, Electronic Journal of Combinatorics 21(2) (2014), P2.4, DOI 10.37236/3810; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p4/pdf/.
2. A. Prasad, P. Singla, S. Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157 (2012); https://arxiv.org/abs/1212.6157.
