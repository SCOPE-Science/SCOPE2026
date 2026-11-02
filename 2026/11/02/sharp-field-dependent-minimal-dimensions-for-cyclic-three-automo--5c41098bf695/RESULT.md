# Sharp field-dependent minimal dimensions for cyclic-three automorphisms of evolution algebras

## Finding
For every field \(K\), let \(\mu_K(C_3)\) be the least **positive** dimension of an evolution \(K\)-algebra whose group of \(K\)-linear algebra automorphisms is exactly cyclic of order three. Let \(\mu_K^{\mathrm{perf}}(C_3)\) be the corresponding least dimension among *perfect* evolution algebras (those satisfying \(E^2=E\)). Define
\[
\mathcal C(K):\quad |\{t\in K^\times:t^3=1\}|=3\quad\text{and}\quad K^\times\ne (K^\times)^3.
\]
Then both minima exist and satisfy the **exact arithmetic classification**
\[
\boxed{\mu_K(C_3)=\begin{cases}
1,&K\cong\mathbb F_4,\\
2,&K\not\cong\mathbb F_4\text{ and }\mathcal C(K),\\
3,&\text{otherwise},
\end{cases}}
\qquad
\boxed{\mu_K^{\mathrm{perf}}(C_3)=\begin{cases}2,&\mathcal C(K),\\3,&\text{otherwise}.\end{cases}}
\]
In particular, over finite fields the unrestricted minimum equals \(1\) for \(q=4\), equals \(2\) for \(q>4\) with \(q\equiv1\pmod3\), and equals \(3\) otherwise. The perfect minimum equals \(2\) for \(q\equiv1\pmod3\) and \(3\) otherwise.

## Assumptions and scope
An evolution algebra is a finite-dimensional commutative, not necessarily associative \(K\)-algebra with a natural basis \(e_1,\ldots,e_n\) in which \(e_ie_j=0\) whenever \(i\ne j\). The group is the group of actual \(K\)-rational algebra automorphisms, not an automorphism group scheme over an algebraic closure. The scalar field is arbitrary, including characteristic two, finite fields, and imperfect fields. The minimum is over all algebras of **positive** dimension. The conclusion concerns the fixed abstract group \(C_3\), not all finite groups.

## Proof
**1. Dimension one.** In a basis \(e\), either \(e^2=0\), whose automorphism group is \(K^\times\), or \(e^2=ce\) with \(c\ne0\), whose automorphism group is trivial. The group \(K^\times\) has order three exactly when \(K\) has four elements; it then is cyclic. No one-dimensional perfect algebra has automorphism group \(C_3\).

**2. Perfect dimension two.** Write \(e_i^2=\sum_j m_{ij}e_j\), with invertible \(2\times2\) structure matrix. Any automorphism must be monomial: the equation \(f(e_1)f(e_2)=0\), together with linear independence of \(e_1^2,e_2^2\), makes the two columns have disjoint support. The homomorphism from the automorphism group into \(S_2\) recording its permutation has trivial image when the full group is \(C_3\). Thus a putative group \(C_3\) consists solely of diagonal automorphisms.

A diagonal automorphism \(f(e_i)=t_i e_i\) satisfies \(t_j=t_i^2\) at each nonzero coefficient \(m_{ij}\). If the two-vertex support graph has a loop, the looped vertex has \(t_i=1\); invertibility of the structure matrix forces the other vertex either to carry a loop or to point to the looped vertex, so it too has \(t_j=1\) for an element of order three. Therefore the only perfect two-dimensional support that admits diagonal automorphisms of order three is the loopless directed two-cycle. After rescaling notation, it is
\[
 E_\alpha:\quad e_1^2=e_2,\qquad e_2^2=\alpha e_1,\qquad\alpha\in K^\times.
\]
Every diagonal automorphism is \(e_1\mapsto t e_1,\ e_2\mapsto t^2 e_2\), where \(t^3=1\). Every off-diagonal automorphism is \(e_1\mapsto s e_2,\ e_2\mapsto\alpha s^2 e_1\) with \(s^3=\alpha^{-1}\). These are all monomial possibilities. Consequently
\[
|\operatorname{Aut}_K(E_\alpha)|=|\mu_3(K)|\bigl(1+\mathbf1_{\alpha\in(K^\times)^3}\bigr).
\]
It follows that a perfect evolution algebra of dimension two has automorphism group exactly \(C_3\) if and only if \(\mathcal C(K)\) holds. The ``if'' direction uses any \(\alpha\notin(K^\times)^3\); the ``only if'' direction follows from the necessary diagonal element and the absence of off-diagonal elements.

**3. No additional nonperfect two-dimensional examples.** Suppose \(\dim E^2\le1\). If \(E^2=0\), then \(\operatorname{Aut}(E)=\operatorname{GL}_2(K)\), which is never \(C_3\) (already \(\operatorname{GL}_2(\mathbb F_2)\) has six elements, and the larger-field groups are still larger). Otherwise write \(xy=b(x,y)u\), where \(u\ne0\) spans \(E^2\) and \(b\) is a symmetric bilinear form diagonal in a natural basis. An automorphism \(f\) is precisely an invertible linear map satisfying
\[
f(u)=c u,\qquad b(fx,fy)=c\,b(x,y)\quad(\forall x,y\in E),\qquad c\in K^\times.
\]
Write \(r=\operatorname{rank}b\in\{1,2\}\).

If \(r=1\), choose \(e_1\) with \(b(e_1,e_1)\ne0\) and \(e_2\) spanning the radical; write \(u=a e_1+b_0e_2\). Every automorphism has \(f(e_1)=x e_1+y e_2\), \(f(e_2)=z e_2\), with \(x,z\ne0\), and the multiplier is \(c=x^2\). If \(a\ne0\), comparison of \(f(u)=x^2u\) gives \(x=1\) and \(y=(b_0/a)(1-z)\), so the full automorphism group is \(K^\times\). If \(a=0\), it gives \(z=x^2\) with arbitrary \(x\ne0,y\in K\), so the full group has order \(q(q-1)\) for \(K=\mathbb F_q\), and is infinite over infinite fields; it is never \(C_3\).

If \(r=2\), the form is nondegenerate. When \(b(u,u)\ne0\), the equations force \(c=1\) and fixation of \(u\); the group acts by scalars of square one on its one-dimensional perpendicular and therefore has at most two elements. When \(b(u,u)=0\) and \(\operatorname{char}K\ne2\), choose a hyperbolic basis \(u,v\) with \(b(u,v)=1\) and \(b(v,v)=0\). The equations give exactly \(f(u)=c u, f(v)=v\), so the group is \(K^\times\). Finally, when \(b(u,u)=0\) and \(\operatorname{char}K=2\), choose \(v\) with \(b(u,v)=1\). The form is nonalternating because it has a diagonal natural basis of rank two, hence \(b(v,v)\ne0\). The equations give precisely \(f(u)=u, f(v)=v+y u\), for \(y\in K\), so the group is the additive group \((K,+)\), which cannot be cyclic of order three in characteristic two. Thus, except when \(K=\mathbb F_4\), no nonperfect two-dimensional example has group \(C_3\). (For that exceptional field the dimension-one construction is already minimal.)

**4. A perfect dimension-three example over every field.** If \(\operatorname{char}K\ne2\), define the algebra with indices cyclic modulo three by \(e_i^2=e_i+e_{i+1}\). Its structure matrix is \(I+P\), with \(\det(I+P)=2\ne0\), where \(P\) is the three-cycle matrix. If \(\operatorname{char}K=2\) and \(K\not\cong\mathbb F_2,\mathbb F_4\), choose \(a\in K^\times\) with \(a^3\ne1\) (such an element exists because at most three nonzero elements solve \(a^3=1\)). Define \(e_i^2=e_i+a e_{i+1}\); its structure matrix has determinant \(1+a^3\ne0\). In both cases, the directed support graph consists of loops and cyclic successor arrows. It has exactly the three rotations as graph automorphisms; all diagonal automorphisms are trivial because of the loops, and all three rotations lift to algebra automorphisms because the coefficients are constant around the cycle. Perfect natural-basis rigidity therefore gives \(\operatorname{Aut}(E)\cong C_3\).

Over \(\mathbb F_2\), instead use \(e_i^2=e_{i+1}\). This algebra is perfect. Its graph has automorphism group \(C_3\), while its diagonal automorphisms satisfy \(t_{i+1}=t_i^2\), hence \(t_1^7=1\) and \(t_1=1\) in \(\mathbb F_2\). Thus again its full group is \(C_3\). Over \(\mathbb F_4\), the one-dimensional zero-product example suffices; the two-cycle construction also gives a perfect example of dimension two.

**5. Minimality.** Step 1 excludes dimension one except over \(\mathbb F_4\), step 2 exactly characterizes perfect dimension-two occurrences, step 3 excludes further nonperfect dimension-two occurrences outside \(\mathbb F_4\), and step 4 supplies the universal dimension-three upper bound. Combining these proves both stated formulas. The finite-field specialization follows because \(\mathbb F_q^\times\) is cyclic of order \(q-1\): it has three cube roots and a noncube precisely when \(q\equiv1\pmod3\).

## Verification
The included `verify.cpp` independently enumerates all four-coefficient two-dimensional evolution-algebra structures and checks every invertible \(2\times2\) matrix directly against all multiplication identities over \(\mathbb F_q\) for \(q=2,3,4,5,7,8,9\). Observed numbers of structures with full automorphism group of order exactly three were respectively \(0,0,30,0,24,0,0\); the counts for perfect structures were \(0,0,6,0,24,0,0\). The extension fields use explicit irreducible polynomials, and the verification derives group sizes by direct multiplication rather than invoking the classification formula.

The included `verify3.cpp` independently enumerates every invertible \(3\times3\) matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and directly checks it against the specified dimension-three multiplication tables; the number of automorphisms is exactly three in each case. The source files are compilable with standard C++17 (for example, `g++ -O3 -std=c++17 verify.cpp -o verify2` and analogously for `verify3.cpp`). Both executables report success tokens. These finite computations check cases but do not replace any infinite-field argument or the proof for all field sizes.

## Relationship to prior work
Kaygorodov, Martín González and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248, initial public version 2026-10-15), formulate the minimum-dimension invariant as Question 40. They note the absence of perfect examples of dimension at most two with automorphism group \(C_3\) over \(\mathbb C\), and establish general upper bounds. The theorem here computes **both** the unrestricted and perfect minima **over every field**, including the arithmetic two-cycle occurrence and the \(\mathbb F_4\) dimension-one exception.

Gonçalves et al., *Squares and associative representations of two-dimensional evolution algebras* (arXiv:1807.02362), already classify automorphisms of **all** two-dimensional evolution algebras. Cabrera Casado et al., *Hopf algebras and associative representations of two-dimensional evolution algebras* (arXiv:2407.15769), likewise describe the exact group scheme in the two-cycle family, with diagonal cube-root solutions and off-diagonal solutions depending on \(\alpha\). Those **prior automorphism formulas are not claimed as new**. The contribution is the sharp synthesis with uniform three-dimensional constructions and the complete field-dependent minimum-dimension invariant; it is not an assertion that two-dimensional automorphism computations were unknown. Costoya et al., *Automorphism groups of Cayley evolution algebras* (DOI:10.1007/s13398-023-01414-w), supply broad existence bounds over sufficiently large fields, not this field-by-field exact threshold.

## Limitations
This is a theorem about the ordinary group of \(K\)-linear automorphisms, rather than the full group scheme; these can have different behavior after scalar extension or in special characteristics. The sharp dimension result is for \(C_3\), not a conjecture for arbitrary cyclic groups. The automorphism structure in dimension two is known prior work. Although targeted literature comparisons did not reveal the combined exact minimum theorem, unidentified equivalent reformulations or unpublished work remain a historical-priority risk. No independent external mathematical audit has been performed.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (2026-10-15), https://arxiv.org/abs/2610.22248 .
2. M. I. C. Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González, M. Siles Molina, *Squares and associative representations of two dimensional evolution algebras*, arXiv:1807.02362 (2018-07-06), https://arxiv.org/abs/1807.02362 .
3. Y. Cabrera Casado, M. I. C. Gonçalves, D. Gonçalves, D. Martín Barquero, C. Martín González, I. Ruiz Campos, *Hopf algebras and associative representations of two-dimensional evolution algebras*, arXiv:2407.15769 (2024-07-22), https://arxiv.org/abs/2407.15769 .
4. C. Costoya et al., *Automorphism groups of Cayley evolution algebras*, RACSAM (2023), https://doi.org/10.1007/s13398-023-01414-w .
