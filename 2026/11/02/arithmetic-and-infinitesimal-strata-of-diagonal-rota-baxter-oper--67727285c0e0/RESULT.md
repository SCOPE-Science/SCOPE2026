# Arithmetic and infinitesimal strata of diagonal Rota–Baxter operators on cyclic evolution algebras

## Finding
Fix an integer \(n\ge3\) and a field \(k\). Let \(E_n\) be the evolution algebra with natural basis \(e_0,\ldots,e_{n-1}\), pairwise-zero mixed products, and \(e_i^2=e_{i+1}\), with indices interpreted modulo \(n\). For a scalar weight \(\lambda\in k\), let \(\mathcal D_{n,\lambda}\) be the affine \(k\)-scheme of **diagonal** Rota–Baxter operators, i.e. maps \(R(e_i)=r_i e_i\) satisfying
\[
 R(x)R(y)=R\bigl(R(x)y+xR(y)+\lambda xy\bigr).
\]
Put \(M=2^n-1\).

**Nonzero weights.** For every \(\lambda\ne0\), the scheme has the explicit decomposition
\[
 \mathcal D_{n,\lambda}\cong
 \operatorname{Spec}k\ \sqcup\ \operatorname{Spec}k\ \sqcup\
 \operatorname{Spec}\bigl(k[t,(t-1)^{-1}]/(t^M-1)\bigr).
\]
The two isolated points are \(R=0\) and \(R=-\lambda I\). On the last component, set \(t_i=t^{2^i}\) and \(r_i=\lambda/(t_i-1)\). This gives all operators, over every field extension, uniquely. For a field of characteristic \(p>0\), write \(M=p^a M_0\) with \(p\nmid M_0\); in characteristic zero set \(p^a=1\) and \(M_0=M\). The geometric point count is \(M_0+1\), the total scheme length is \(M-p^a+2\), and \(\mathcal D_{n,\lambda}\) is smooth over \(k\) precisely when \(p^a=1\) or \(M_0=1\). Otherwise it has exactly \(M_0-1\) nonreduced geometric points, each of length \(p^a\) and tangent dimension one. In particular, the first modular nonreduced instance occurs at \(n=4\) in characteristic \(3\), where the geometric scheme has six points, four of them of length three.

**Zero weight.** The \(k\)-rational diagonal solutions are just \(R=0\), unless \(\operatorname{char}k=p\ne2\) and \(p\mid M\). In that exceptional case, precisely the \(k\)-points
\[
 R_c(e_i)=2^{-i}c e_i\qquad(c\in k)
\]
occur. This is a statement about field-valued points, **not** a claimed scheme decomposition at zero weight.

**Finite-field conjugacy.** If \(k=\mathbb F_q\), \(\lambda\ne0\), and \(g=\gcd(M,q-1)\), then there are exactly \(g+1\) diagonal operators and exactly
\[
 1+\frac1n\sum_{s=0}^{n-1}\gcd(g,2^s-1)
\]
conjugacy classes under the full algebra automorphism group \(\operatorname{Aut}_k(E_n)\). In the zero-weight exceptional case, set \(d=\operatorname{ord}_p(2)\). Then there are exactly \(q\) operators and \(1+(q-1)/d\) conjugacy classes; in all other zero-weight cases the unique operator and class are zero.

## Assumptions and scope
The multiplication table of \(E_n\) is fixed as above; its structure matrix is a permutation matrix, so \(E_n\) is perfect and is not nilpotent. "Diagonal" means diagonal relative to this natural basis. Counts classify only diagonal Rota–Baxter operators and their conjugacy under **all** algebra automorphisms; non-diagonal Rota–Baxter operators are not classified. The scheme is defined by the exact Rota–Baxter polynomial equations, not by a reduced-point enumeration. All formulas use actual field characteristic, including \(2\).

## Proof
### 1. Diagonal equations
Substituting distinct basis elements into the defining identity yields zero on both sides. Substituting \(e_i,e_i\) gives exactly
\[
 r_i^2=(2r_i+\lambda)r_{i+1}\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Thus the affine coordinate ring of \(\mathcal D_{n,\lambda}\) is the quotient of \(k[r_0,\ldots,r_{n-1}]\) by these \(n\) equations.

### 2. Nonzero weight and scheme decomposition
Suppose \(\lambda\ne0\). If a field-valued solution has one zero coefficient, the next coefficient is zero, hence all coefficients are zero. The Jacobian of the equations at the all-zero solution is the invertible matrix \(-\lambda\) times the cyclic shift. Therefore the origin is a reduced isolated scheme point. Every other geometric solution has all \(r_i\ne0\). A finite-type scheme with only these two types of geometric points is the disjoint union of its origin and the locus obtained by inverting the product of its coordinates: no further scheme component is supported at the origin, because its local ring is reduced of dimension zero.

On the open locus, put \(t_i=1+\lambda/r_i\). The defining equation implies
\[
 \frac\lambda{r_{i+1}}=\frac\lambda{r_i}\left(2+\frac\lambda{r_i}\right)=t_i^2-1,
 \quad\text{hence}\quad t_{i+1}=t_i^2.
\]
Since \(t_i-1=\lambda/r_i\) is invertible, all substitutions hold in coordinate rings, not merely at points. Conversely, any such \(t_i\) reconstructs \(r_i=\lambda/(t_i-1)\). Going around the cycle gives \(t^{2^n}=t\). Because \(t-1\) is invertible, the coordinate ring is
\[
 k[t,(t-1)^{-1}]/\bigl(t(t^M-1)\bigr).
\]
The factors \(t\) and \(t^M-1\) are coprime, giving the second isolated point \(t=0\), which corresponds to \(R=-\lambda I\), and the stated third summand.

In characteristic \(p\), \(t^M-1=(t^{M_0}-1)^{p^a}\), and \(t^{M_0}-1\) is separable. The component supported at \(t=1\) has length \(p^a\) and is deleted by inverting \(t-1\). The remaining \(M_0-1\) roots each have local length \(p^a\) and embedding/tangent dimension one when \(p^a>1\). Together with the two reduced points this gives all geometric counts, scheme lengths and smoothness criteria. Characteristic zero is the separable case.

### 3. Zero weight rational points
If \(\lambda=0\), the equations become \(r_i^2=2r_ir_{i+1}\). In characteristic two they force each \(r_i=0\). Otherwise any nonzero \(r_i\) forces \(r_{i+1}=r_i/2\), then cyclically forces every entry nonzero and \((2^n-1)r_i=0\). Hence nonzero solutions exist precisely when the field has odd positive characteristic dividing \(M\); they then have the displayed form. No scheme-level reducedness claim is inferred.

### 4. All automorphisms and finite-field orbits
Since the basis squares form a basis, applying an automorphism \(F\) to \(e_ie_j=0\) with \(i\ne j\) shows the columns of its matrix have disjoint supports. Invertibility makes \(F\) monomial. Compatibility with \(e_i^2=e_{i+1}\) forces its underlying permutation to be a cyclic rotation \(i\mapsto i+s\), and its nonzero monomial coefficients to obey \(c_{i+1}=c_i^2\) and \(c_0^M=1\). Consequently the diagonal factors act trivially on diagonal operators by conjugation; rotations act by shifting the sequence \((r_i)\). On the nonzero-weight parameter \(t\), the rotation action is generated by \(t\mapsto t^2\) (or its inverse, with the same orbit partition).

For \(\mathbb F_q\), the finite multiplicative roots \(t^M=1\) form a cyclic group of size \(g=\gcd(M,q-1)\). Their squaring action has, by Burnside's lemma, \(n^{-1}\sum_{s=0}^{n-1}\gcd(g,2^s-1)\) orbits. Remove the identity root and insert the two isolated diagonal operators; this changes the total number of orbits by \(+1\). The number of operators is \((g-1)+2=g+1\). At weight zero, rotation multiplies the nonzero parameter \(c\) by a power of \(2\) of exact order \(d\), so each nonzero orbit has size \(d\); adding zero proves the formula.

## Verification
Run \(\texttt{python verify.py}\) using standard Python 3. The checker enumerates all diagonal candidates at 44 small prime-field parameter choices, evaluates the full Rota–Baxter identity on every basis pair, verifies the number of cyclic-rotation orbits, and checks the predicted Jacobian tangent dimension at every prime-field solution with nonzero weight. It also enumerates three finite extensions of the binary field, with independently coded multiplication. Output:

```text
VERIFY_OK prime_field_parameter_cases= 44
VERIFY_OK extension_field_cases=3
```

The scheme-level multiplicities and the uniform formulas are established by the algebraic proof above; finite-field point checks alone would not certify them.

## Relationship to prior work
Qaralleh, Mukhamedov and Khakimov (2026) classify Rota–Baxter operators for **nilpotent** maximal-nilindex evolution algebras, where the natural graph is acyclic and recurrence chains terminate. The present cyclic algebra is perfect and has a directed cycle, not a nilpotent chain. They explicitly introduce the rational map \(f(x)=x^2/(2x+1)\) and periodic-point sets \(\operatorname{Per}_m(f)\) for constraints in the nilpotent problem. Neither this recurrence nor the existence of periodic points is claimed as novel here. The new result here is the closed-cycle arithmetic and exact scheme-theoretic decomposition, modular nonreduced boundary, and conjugacy arithmetic at every rank at least three. Ladra and Murodov (2019) work with Rota–Baxter operators on two-dimensional complex evolution algebras, not these uniform cyclic higher-rank moduli schemes. The 2026 evolution-algebra survey also motivates investigations of scheme smoothness and operator structures. A previously known dimension-two classification of the same cyclic algebra is excluded from the claimed dimensional novelty.

## Limitations
The diagonal restriction is essential; this result does not characterize all linear Rota–Baxter operators, and the scheme structure at weight zero is not determined here. The new arithmetic follows an elementary recurrence after a nontrivial cycle closure, so its broader priority relative to old literature on polynomial dynamical systems or moduli of operators warrants independent review. No claim is made about publication priority or independent verification.

## References
1. I. Qaralleh, F. Mukhamedov, O. Khakimov, "Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex," arXiv:2601.08669, initial public version 2026-01-13. https://arxiv.org/html/2601.08669
2. M. Ladra, S. N. Murodov, "On chains and Rota-Baxter operators of evolution algebras," arXiv:1906.09098, first public version 2019-06-19. https://arxiv.org/abs/1906.09098
3. I. Kaygorodov, C. Martín González, A. Viruel, "Evolution algebras: a survey of results and a list of open problems," arXiv:2610.22248, initial public version 2026-10-15. https://arxiv.org/html/2610.22248
