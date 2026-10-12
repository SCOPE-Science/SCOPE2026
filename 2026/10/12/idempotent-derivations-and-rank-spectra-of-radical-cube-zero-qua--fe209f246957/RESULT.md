# Idempotent derivations and rank spectra of radical-cube-zero quantum exterior algebras

## Finding
Let \(K\) be a field, \(n\ge2\), and let every skew commutation parameter satisfy \(c_{ij}\in K^\times\setminus\{1,-1\}\), \(i<j\). The quotient of the quantum exterior algebra by all cubic monomials has a complete classification of composition-idempotent associative derivations \(D^2=D\). Each one is conjugate to a diagonal idempotent \(D_S\) indexed by a subset \(S\subseteq\{1,\ldots,n\}\). When \(\operatorname{char}K\ne2\), only the empty and singleton subsets occur; when \(\operatorname{char}K=2\), every subset occurs. The conjugacy classes are precisely the orbits of these subsets under the parameter-preserving permutation group (defined below).

Over a finite field of odd size \(q\) (thus \(q\ge5\)), the full rank-counting polynomial is
\[
\mathcal R_{n,q}(T)=1+nq^{(n-1)^2+\binom{n-1}{2}}T^n.
\]
Over a finite field of even size \(q\) (thus \(q\ge4\)), it is
\[
\mathcal R_{n,q}(T)=\sum_{r=0}^{n}\binom nr q^{E(n,r)}T^{r(n-r+1)},\quad
E(n,r)=r\left[\binom r2+\binom{n-r}2+(n-r)^2\right].
\]
The rank is that of the full \(K\)-linear operator, and coefficients count labeled derivations, not automorphism orbits. These counts do not depend on the particular allowed skew parameters.

## Assumptions and scope
The algebra is
\[
A=K\langle x_1,\ldots,x_n\rangle/
\langle x_i^2,\ x_jx_i-c_{ij}x_ix_j\ (i<j),\ x_ix_jx_k\ (1\le i,j,k\le n)\rangle.
\]
It is associative, unital, and local with radical \(J=(x_1,\ldots,x_n)\), \(J^3=0\), and basis
\[
1;\quad x_i\ (1\le i\le n);\quad y_{ij}=x_ix_j\ (i<j).
\]
The only nonzero products between positive-degree basis elements are \(x_ix_j=y_{ij}\) and \(x_jx_i=c_{ij}y_{ij}\) for \(i<j\). We use ordinary \(K\)-derivations satisfying \(D(ab)=D(a)b+aD(b)\), not twisted derivations or algebra endomorphisms. Composition-idempotence means \(D\circ D=D\). The hypotheses exclude \(K=\mathbb F_2\) and \(K=\mathbb F_3\), for which no admissible parameter exists.

For distinct \(a,b\), set \(c_{ba}=c_{ab}^{-1}\) if \(a<b\). Define
\[
\Gamma_{\mathbf c}=\{\sigma\in\mathfrak S_n:\ c_{\sigma(i),\sigma(j)}=c_{ij}\ \text{for all }i<j\}.
\]
When all parameters for increasing indices have a common value \(c\ne\pm1\), this group is trivial: reversing any pair forces \(c^{-1}=c\), hence \(c^2=1\), a contradiction.

## Proof
**1. Shape of all derivations.** Write a general generator image as
\[
D(x_i)=\alpha_i1+\sum_j m_{ji}x_j+\sum_{p<q}b_{pq,i}y_{pq}.
\]
For each pair \(i<j\), apply \(D\) to \(x_jx_i-c_{ij}x_ix_j=0\). Its degree-one part is \((1-c_{ij})(\alpha_j x_i+\alpha_i x_j)\), and \(1-c_{ij}\ne0\), so \(\alpha_i=\alpha_j=0\). Since \(n\ge2\), every scalar part vanishes. Apply \(D\) to \(x_i^2=0\). The degree-two coefficient of \(y_{ij}\) for \(j\ne i\) is a nonzero scalar multiple of \((1+c_{\min(i,j),\max(i,j)})m_{ji}\), forcing every off-diagonal \(m_{ji}=0\). Thus every derivation has a unique expression
\[
D(x_i)=a_i x_i+\sum_{p<q}b_{pq,i}y_{pq}.
\]
All \(a_i,b_{pq,i}\in K\) are arbitrary: this assignment respects every quadratic relation (which becomes a scalar multiple of itself under its diagonal part) and every cubic relation (which differentiates into degree at least three). Consequently, differentiation of \(y_{pq}=x_px_q\) yields
\[
D(y_{pq})=(a_p+a_q)y_{pq},\qquad D(1)=0.
\]

**2. Idempotence equations.** Since the basis in the preceding section is independent, \(D^2=D\) is equivalent to
\[
a_i^2=a_i,\qquad(a_p+a_q)^2=a_p+a_q,\qquad
(a_i+a_p+a_q-1)b_{pq,i}=0
\]
for all \(i,p<q\). Thus every \(a_i\in\{0,1\}\). For odd characteristic, no pair of \(a_i\) can both equal one because \(2\notin\{0,1\}\), giving the empty and singleton sets. In characteristic two, every subset of diagonal ones is admissible. For every such subset \(S\), put \(a_i=\mathbf1_{i\in S}\). Exactly those coefficients \(b_{pq,i}\) for which \(a_i+a_p+a_q=1\) may vary freely, giving all idempotent derivations without exceptions.

**3. Reduction by quadratic shears.** For arbitrary coefficients \(h_{pq,i}\in K\), the assignment \(\psi_h(x_i)=x_i+\sum_{p<q}h_{pq,i}y_{pq}\) is an algebra automorphism fixing every \(y_{pq}\), because \(J^3=0\). Let \(D_S(x_i)=a_i x_i\). Direct composition gives
\[
(\psi_hD_S\psi_h^{-1})(x_i)=a_i x_i+\sum_{p<q}(a_i-a_p-a_q)h_{pq,i}y_{pq}.
\]
If \(b_{pq,i}\ne0\) is admissible, then \(a_i\ne a_p+a_q\) as field elements; their difference is \(1\) or \(-1\), hence invertible. Taking \(h_{pq,i}=b_{pq,i}/(a_i-a_p-a_q)\) on admissible indices, and zero otherwise, produces every idempotent derivation with the given \(S\). This is an explicit conjugation, not merely an orbit-count argument.

**4. Which diagonal classes coincide?** An algebra automorphism preserves the radical and gives an invertible matrix \(M=(m_{ji})\) on \(J/J^2\). The square-zero relations, applied to each column, give \((1+c_{pq})m_{pi}m_{qi}=0\) for every \(p<q\). Since \(c_{pq}\ne-1\), each column has at most one nonzero entry. Invertibility forces \(M\) to be monomial. Comparing the skew-commutation relations shows that its underlying permutation lies in \(\Gamma_{\mathbf c}\), and conversely every such permutation defines an automorphism. The diagonal support of a derivation is therefore carried to its image under \(\Gamma_{\mathbf c}\). Combined with Step 3, this proves that conjugacy classes are exactly the specified subset orbits. In the constant-parameter case \(\Gamma_{\mathbf c}=1\), whence the class counts are \(n+1\) and \(2^n\).

**5. Ranks and multiplicities.** Since \(D^2=D\), its linear rank is the number of ones among the eigenvalues displayed in Step 1. If \(|S|=r\) and \(u=n-r\), the generator contribution is \(r\). In odd characteristic, an admissible nonempty \(S\) has \(r=1\); exactly \(u=n-1\) mixed quadratic basis elements have eigenvalue one, giving rank \(n\). The number of free \(b\)-parameters is \(u^2+\binom u2\): for the unique selected generator, the unselected pairs may appear, and for each unselected generator, all \(u\) mixed pairs may appear. Thus each singleton contributes \(q^{(n-1)^2+\binom{n-1}{2}}\) derivations.

In characteristic two, a quadratic basis element has eigenvalue one exactly when its indices lie on opposite sides of \(S\), so there are \(ru\) such elements, giving rank \(r+ru=r(n-r+1)\). The free \(b\)-coefficients occur in three disjoint situations: \(i\in S\) and \(p,q\) both in \(S\); \(i\in S\) and \(p,q\) both outside \(S\); or \(i\notin S\) and \(p,q\) are mixed. These contribute \(r\binom r2\), \(r\binom u2\), and \(ru^2\) independent coefficients. There are \(\binom nr\) choices of \(S\), giving the displayed polynomial. When distinct \(r\) yield the same rank, their terms add as usual.

## Verification
The self-contained `checker.py` uses prime fields and a binary representation of \(\mathbb F_4\) with \(\omega^2+\omega+1=0\). For \(n=2\) and \((q,c)=(4,2),(4,3),(5,2),(5,3)\), it enumerates **all** assignments of two generator images (including scalar parts), directly tests every basis-pair Leibniz identity and operator idempotence, and computes ranks by finite-field Gaussian elimination. It obtains \(1+24T^2\) in each \(\mathbb F_4\) case and \(1+10T^2\) in each \(\mathbb F_5\) case. It independently enumerates admissible diagonal choices and free quadratic parameters for \(2\le n\le6\), \(q=4,5,7\), and checks the closed rank polynomial. All tests print `VERIFY_OK`. The proof above, not these finite computations, establishes the claims for arbitrary fields and all \(n\ge2\).

## Relationship to prior work
Jin and Zhang (arXiv:2208.05687, first released 2022-08-11, §2.3 and §5) define quantum complete intersections/exterior algebras and study bi-Frobenius and Hopf structures, rather than composition-idempotent derivations or their rank distributions. Our algebra is specifically their quantum exterior type with the additional radical-cube-zero quotient; its truncation is material to the shear normal forms. Grimley (arXiv:1606.01727, introduction and §3) computes Hochschild cohomology of related quantum complete intersections and group extensions; its general derivation/cohomology setting is relevant but the inspected calculations do not imply the idempotent equations, parameter-preserving conjugacy, or rank polynomial here. Bergh, Erdmann, and Jorgensen (arXiv:1910.06714, introduction and §2) study constant Jordan type for multiplication operators on modules over quantum complete intersections, not idempotent derivations on the algebra. The general linear idempotent/conjugation identities used here are elementary and are not claimed as new; the joint all-parameter orbit classification and enumerator are the asserted additional result.

## Limitations
The restrictions \(c_{ij}\ne1,-1\) are essential in the proof: at exceptional parameters scalar or off-diagonal linear terms need not be forced to vanish, and additional conjugacies can occur. The theorem does not concern untruncated quantum exterior algebras, higher nilpotence truncations, semilinear derivations, or characteristics in fields lacking admissible parameters. There is no claim of uniqueness among all unpublished results or independent verification. Possible equivalent statements in specialized literature on algebra gradings or radical-cube-zero quantum algebras remain a bibliographic risk.

## References
1. H. Jin and P. Zhang, *Bi-Frobenius algebra structure on quantum complete intersections*, arXiv:2208.05687 (v1 2022-08-11), https://arxiv.org/abs/2208.05687 and https://arxiv.org/html/2208.05687v2.
2. L. Grimley, *Hochschild cohomology of group extensions of quantum complete intersections*, arXiv:1606.01727 (2016), https://arxiv.org/html/1606.01727v1.
3. P. A. Bergh, K. Erdmann, and D. Jorgensen, *Modules of constant Jordan type over quantum complete intersections*, arXiv:1910.06714 (2019), https://arxiv.org/html/1910.06714v1.
