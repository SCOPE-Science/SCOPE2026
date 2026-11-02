# Finite-field point-orbit and local-symmetry census for null-filiform Leibniz algebras

## Finding

For every field \(k\) and integer \(n\ge2\), let \(N_n(k)\) have basis \(e_1,\ldots,e_n\) with the only nonzero basis products
\[
[e_i,e_1]=e_{i+1}\quad(1\le i<n).
\]
Write \(G=\operatorname{Aut}_k(N_n(k))\). Define a *linear local automorphism* to be a \(k\)-linear map \(T:N_n(k)\to N_n(k)\) such that for each \(v\) some \(g_v\in G\) satisfies \(T(v)=g_v(v)\). Let \(H_i=(k^\times)^i\subseteq k^\times\).

**Theorem (point orbits and linear pointwise closure).** For nonzero \(v=\sum_{j=1}^n v_j e_j\) put \(h(v)=\min\{j:v_j\ne0\}\). Two nonzero vectors \(v,w\) are in the same \(G\)-orbit if and only if
\[
h(v)=h(w)=i\quad\text{and}\quad w_i/v_i\in H_i.
\]
Zero is a singleton orbit. The group of all linear local automorphisms is *exactly* the group of invertible lower triangular matrices with their \(i\)-th diagonal entry in \(H_i\) (columns are images of the basis vectors). Equivalently it is the linear point-orbit-preserving closure of \(G\) in \(\operatorname{GL}_n(k)\). There are no restrictions on entries strictly below the diagonal.

When \(k=\mathbb F_q\), put \(g_i=\gcd(i,q-1)\). Every nonzero orbit of height \(i\) has
\[
\frac{q-1}{g_i}q^{n-i}\quad\text{elements},
\]
its point stabilizer in \(G\) has \(g_iq^{i-1}\) elements, and there are exactly \(g_i\) such orbits. In particular, the total number of vector orbits is
\[
\boxed{\mathcal O_{q,n}=1+\sum_{i=1}^{n}g_i
 =1+\sum_{d\mid(q-1)}\varphi(d)\left\lfloor\frac nd\right\rfloor}.
\]
The exact group orders are
\[
\boxed{|G|=(q-1)q^{n-1},\qquad
|\operatorname{LocAut}_{\mathrm{lin}}(N_n(\mathbb F_q))|
=q^{n(n-1)/2}\prod_{i=1}^{n}\frac{q-1}{g_i}}.
\]
Thus the index of genuine automorphisms in the linear pointwise closure is
\[
q^{(n-1)(n-2)/2}\prod_{i=2}^{n}\frac{q-1}{g_i}.
\]
The first difference \(\mathcal O_{q,n}-\mathcal O_{q,n-1}\) is periodic of period dividing \(q-1\) (for \(n\ge2\)). This gives a uniform arithmetic orbit profile rather than an algebraically-closed-field orbit profile.

## Assumptions and scope

The algebra has the displayed right-Leibniz multiplication, with no restrictions on the characteristic or perfection of \(k\). All automorphisms and local automorphisms are \(k\)-linear; a possibly nonlinear map satisfying a pointwise condition is not classified. For the finite-field enumeration, \(q\) is any prime power and \(n\ge2\). No assertion about scheme-theoretic point-orbit closures is made.

## Proof

Let \(S(e_i)=e_{i+1}\) for \(i<n\), with \(S(e_n)=0\). Multiplication is \([x,y]=y_1 S(x)\). If an algebra homomorphism \(f\) sends \(e_1\) to \(b=\sum_{j=1}^n b_j e_j\), its values are forced by \(e_{i+1}=[e_i,e_1]\):
\[
f(e_i)=b_1^{i-1}S^{i-1}(b)
=b_1^{i-1}\sum_{j=1}^{n-i+1}b_j e_{i+j-1}.
\tag{1}
\]
Conversely, this formula preserves all basis products: every \(f(e_j)\) with \(j\ge2\) has first coordinate zero, and products against \(f(e_1)\) reproduce the shift recurrence. Its matrix is lower triangular with diagonal \((b_1,b_1^2,\ldots,b_1^n)\). Therefore \(f\in G\) exactly when \(b_1\ne0\); the remaining \(b_2,\ldots,b_n\) are arbitrary. This also proves \(|G|=(q-1)q^{n-1}\) over a finite field.

Fix nonzero \(v\) of height \(i\). Every \(f\in G\) preserves height and sends the first nonzero coordinate \(v_i\) to \(b_1^i v_i\). For the converse, take \(w\) of the same height with \(w_i/v_i=b_1^i\) for some \(b_1\in k^\times\). At coordinate \(i+t\), for \(1\le t\le n-i\), formula (1) gives
\[
(f(v))_{i+t}=v_i b_1^{i-1}b_{t+1}
 +P_t(b_1,\ldots,b_t;v),
\]
where \(P_t\) depends only on already selected parameters. The coefficient \(v_i b_1^{i-1}\) is nonzero, so \(b_{t+1}\) is uniquely chosen to attain \(w_{i+t}\). Parameters with higher indices remain unrestricted. Hence the displayed orbit criterion holds, with no assumption on \(k\).

If a linear map \(T\) is locally an automorphism, applying it to each \(e_i\) and using the orbit criterion forces \(T(e_i)\in\operatorname{span}\{e_i,\ldots,e_n\}\) and its \(i\)-th coordinate \(d_i\in H_i\). Conversely, any lower triangular map with all \(d_i\in H_i\) maps a vector of height \(i\) to a vector of the same height, multiplying its first nonzero coordinate by \(d_i\); the orbit criterion supplies an automorphism agreeing with \(T\) at that vector. Zero is automatic. This proves both necessity and sufficiency, as well as invertibility.

For \(k=\mathbb F_q\), the power map on the cyclic group \(k^\times\) has kernel of size \(g_i=\gcd(i,q-1)\) and image of size \((q-1)/g_i\). The freely attainable \(n-i\) trailing coordinates give the orbit size. In (1), each of the \(g_i\) choices of \(b_1\) fixing the first nonzero coordinate determines \(b_2,\ldots,b_{n-i+1}\) uniquely, and \(b_{n-i+2},\ldots,b_n\) are free. Thus every stabilizer has \(g_iq^{i-1}\) elements. There are \(g_i\) cosets of \(H_i\) and thus that many orbits at height \(i\). Summing over heights and zero gives \(1+\sum_i g_i\). The divisor form follows from \(\gcd(i,Q)=\sum_{d\mid\gcd(i,Q)}\varphi(d)\) for \(Q=q-1\). Finally, there are \(q^{n(n-1)/2}\) possibilities below the diagonal of a lower triangular local map, and \((q-1)/g_i\) choices at diagonal position \(i\). Multiplication gives the claimed order and division by \(|G|\) gives the index. All statements include the smallest allowed dimension \(n=2\).

## Verification

The standalone program `verify.py` builds the multiplication of \(N_n(\mathbb F_q)\) directly, enumerates *every* linear endomorphism in each test dimension, tests each for the defining automorphism identity, constructs every actual vector orbit and tests the defining local-automorphism condition on all vectors. It separately compares the claimed orbit/stabilizer formulas and the triangular criterion.

Six exhaustive configurations were checked: \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\), with \(\mathbb F_4\) implemented by polynomial arithmetic. They returned, respectively, \((|G|,\mathcal O,|\operatorname{LocAut}_{\rm lin}|)=(2,3,2),(4,4,8),(8,5,64),(6,4,6),(18,5,108),(12,3,36)\). The run prints `NULL_FILIFORM_FINITE_LOCAL_AUT_OK 6 exhaustive matrix configurations`. The infinite-family results rest on the algebraic proof, not on these examples.

## Relationship to prior work

Khudoyberdiyev and Omirov's 2013 work establishes the null-filiform object and studies its deformations and cohomology, not the finite-field automorphism action on individual elements. Normurodovna's 2026 study gives the ordinary-automorphism matrix formula and the triangular local-automorphism criterion *over the complex numbers*, and explicitly notes a real-field sign obstruction. These known formulas and complex conclusions are not claimed as new. The present statement determines the actual power-class obstruction over every field, the entire vector-orbit partition and stabilizers over every finite field, and the exact linear orbit-preserving group order, which do not follow as statements about finite fields from a complex-field theorem. Related studies of direct sums and solvable Leibniz extensions concern different settings; some directly relevant full texts could not be checked and are noted below.

## Limitations

These formulas do not address nonlinear local maps, two-local maps, general filiform Leibniz algebras, or point-orbits in larger solvable extensions. The ordinary automorphism parameterization is an antecedent, not a novelty claim. The 2022/2023 article on local automorphisms of direct sums was available only through its abstract, so undiscovered overlapping coverage remains possible. Publication priority and all claims await independent review.

## References

1. A. Kh. Khudoyberdiyev and B. A. Omirov, *Infinitesimal deformations of null-filiform Leibniz superalgebras*, arXiv:1304.0126, first public 2013-03-30. https://arxiv.org/abs/1304.0126
2. J. O. Normurodovna, *Derivations, Automorphisms And Local Derivations of Null-Filiform Leibniz Algebras*, 2026, DOI:10.55640/eijmrms-06-06-16. https://eipublication.com/index.php/eijmrms/article/download/4968/4501/6483
3. J. Q. Adashev and B. B. Yusupov, *Local Derivations and Automorphisms of Direct Sum Null-Filiform Leibniz Algebras*, Lobachevskii Journal of Mathematics 43 (2022), pp.3407-3413; online 2023-03-17. DOI:10.1134/S1995080222150021. https://link.springer.com/article/10.1134/S1995080222150021
4. F. N. Arzikulov, I. A. Karimjanov and S. M. Umrzaqov, *Local and 2-local automorphisms of some solvable Leibniz algebras*, arXiv:2105.09001, 2021. https://arxiv.org/abs/2105.09001
