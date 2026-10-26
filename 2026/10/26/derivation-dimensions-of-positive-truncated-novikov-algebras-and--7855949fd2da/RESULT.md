# Derivation dimensions of positive truncated Novikov algebras and a mod-four exceptional direction

## Finding
For a field \(k\) and an integer \(n\geq2\), define the \(n\)-dimensional algebra \(N_n(k)\) with basis \(e_1,\ldots,e_n\) and product
\[
e_i\circ e_j=\begin{cases}j e_{i+j-1},&i+j-1\leq n,\\0,&i+j-1>n.\end{cases}
\]
This is a Novikov algebra: it is the positive-degree truncation of the product \(f\circ g=f g'\) on polynomials. Its ordinary algebra derivation space has dimension
\[
\boxed{\dim_k\operatorname{Der}(N_n(k))=
\begin{cases}
1,&\operatorname{char}k=0,\\
1+\lfloor n/p\rfloor+\lfloor(n-2)/p\rfloor,&\operatorname{char}k=p>2,\\
3\lfloor n/2\rfloor-\bigl(\lfloor n/2\rfloor\bmod2\bigr),&\operatorname{char}k=2,\ n\text{ even},\\
3\lfloor n/2\rfloor,&\operatorname{char}k=2,\ n\text{ odd}.
\end{cases}}
\]
The characteristic-two formula can also be written \(\lfloor3n/2\rfloor-1+\mathbf 1_{4\mid n}\). The extra degree-lowering derivation exists precisely for \(4\mid n\) in characteristic two. Over a finite field \(\mathbb F_q\), the number of derivations is exactly \(q^{\dim\operatorname{Der}(N_n)}\).

## Assumptions and scope
The product is interpreted as a bilinear operation on the vector space with the given basis. Equivalently, take polynomials with no constant term modulo terms of degree exceeding \(n\), and use \(f g'\) before truncating. This is well-defined even when differentiation itself does not descend to the quotient \(k[t]/(t^{n+1})\): a representative change contributes a term of degree at least \(n+1\) after multiplication by \(f\in tk[t]\). All fields, including nonperfect fields and finite extensions of prime fields, are covered. Derivations are arbitrary \(k\)-linear maps satisfying \(D(a\circ b)=D(a)\circ b+a\circ D(b)\); no grading-preservation hypothesis is imposed.

The product is Novikov because its associator on polynomial representatives is \(f\circ(g\circ h)-(f\circ g)\circ h=fgh''\), symmetric in \(f,g\), and \((f\circ g)\circ h=(f\circ h)\circ g\). These identities survive truncation. (The displayed associator uses the sign convention with \(f\circ(g\circ h)\) first.)

## Proof
**1. Homogeneous reduction and the odd-characteristic basis.** Give \(e_i\) degree \(i-1\). Every linear map has a unique sum of components of degree \(s\in\{1-n,\ldots,n-1\}\); since the multiplication is homogeneous, a map is a derivation if and only if all of its homogeneous components are. Write such a component as \(D_s(e_i)=c_i e_{i+s}\), with missing indices interpreted as zero.

The right-identity relation \(e_i\circ e_1=e_i\) gives \(e_i\circ D_s(e_1)=0\) and hence \((s+1)c_1=0\) whenever the corresponding coefficient exists. The left multiplication relation \(e_1\circ e_j=j e_j\) gives, for each active coefficient, \(s c_j=-j c_1\). If \(s\neq0\) in \(k\), a nonzero homogeneous derivation therefore requires \(s=-1\) in \(k\); in that case its coefficients are proportional to \(c_j=j\). This yields the degree-\(s\) derivation
\[
B_s(e_i)=i e_{i+s}\qquad(s\geq0,\ s+1\equiv0\pmod p),
\]
for each \(s\leq n-1\). In characteristic zero this case never occurs; in characteristic \(p>0\), its degrees are \(p-1,2p-1,\ldots\) through \(n-1\).

If \(s=0\) in \(k\), the same identities give \(c_1=0\). When \(\operatorname{char}k\ne2\), applying the derivation identity to \(e_i\circ e_2=2e_{i+1}\) gives \(c_{i+1}=c_i+c_2\) on every consecutive active index. For \(s\geq0\) the resulting nonzero solution is a scalar multiple of
\[
A_s(e_i)=(i-1)e_{i+s}\qquad(s\geq0,\ s\equiv0\pmod p,\ s\leq n-2),
\]
where \(p\) denotes the positive field characteristic; in characteristic zero only \(A_0\) remains. For negative \(s=-h\) with \(h>0\), the equality \(s=0\) in the field implies \(p\mid h\); then \(c_2=0\) and the same recurrence starting at \(i=h\) gives \(c_{h+1}=0\), followed by all remaining coefficients zero. Hence no negative-degree derivations exist when the characteristic is not two. Direct substitution in the defining product verifies each \(A_s\) and \(B_s\): the discrepancy terms are multiples of \(s\) and \(s+1\), respectively. They have disjoint degrees and are independent. In odd characteristic, their number is
\[
1+\lfloor(n-2)/p\rfloor+\lfloor n/p\rfloor.
\]

**2. Characteristic two: an associative splitting.** Put \(n=2m\) or \(n=2m+1\), and set \(u=t^2\). The odd-degree and even-degree subspaces give a canonical direct sum \(N_n=A\oplus B\) with
\[
A=k[u]/(u^a),\quad B=k[u]/(u^b),\qquad
(a,b)=\begin{cases}(m,m),&n=2m,\\(m+1,m),&n=2m+1.\end{cases}
\]
Here an element of \(A\) represents \(t\) times a polynomial in \(u\), and an element of \(B\) represents \(t^2\) times such a polynomial. Because the derivative of every even power vanishes in characteristic two, the product is exactly
\[
(a_1,b_1)\circ(a_2,b_2)=(a_1a_2,b_1a_2),
\]
with components truncated in their respective quotient modules. Thus this Novikov algebra is in fact associative with right identity \((1,0)\). Its right annihilator is precisely \(B\), so every derivation preserves \(B\).

Write a derivation in block form
\[
D(a,b)=(\delta(a),F(a)+T(b)).
\]
The derivation identity is equivalent, without omitted conditions, to: \(\delta\) is a derivation of the commutative ring \(A\); \(F:A\to B\) is \(A\)-linear; and \(T:B\to B\) satisfies \(T(bc)=T(b)c+b\delta(c)\). Consequently \(F(a)=va\) for a unique \(v\in B\). The map \(T\) exists precisely when \(\delta\) preserves the annihilator ideal \((u^b)\subseteq A\), in which case \(T(b)=\overline{\delta(\widetilde b)}+wb\) for an arbitrary \(w\in B\), where \(\widetilde b\) is any lift to \(A\). The allowed \(\delta\) are therefore parametrized by their value \(f=\delta(u)\in A\), subject to
\[
a u^{a-1}f=0\text{ in }A,\qquad b u^{b-1}f=0\text{ in }B\quad(\text{when }a>b).
\]
The second equality means that the derivative of the kernel generator vanishes after projection to \(B\), equivalently \(\delta(u^b)\in(u^b)\subseteq A\).

For \(n=2m\), the allowed \(f\) has dimension \(m\) if \(m\) is even and \(m-1\) if \(m\) is odd; each of \(v,w\) contributes \(m\), giving \(3m-(m\bmod2)\). For \(n=2m+1\), the ring-derivation condition and the ideal-stability condition together force \(f\in uA\), which has dimension \(m\); together with \(v,w\in B\), this gives \(3m\).

**3. The exceptional negative-degree direction.** When \(n=4h\), the even integer \(m=2h\) makes \(\delta(u)=1\) a valid derivation of \(A\). Taking \(v=w=0\) yields an additional degree-\(-2\) derivation, explicitly
\[
D(e_{2r+1})=r e_{2r-1},\quad D(e_{2r+2})=r e_{2r}\qquad(r\geq1),
\]
with \(D(e_1)=D(e_2)=0\) and indices truncated at \(n\). If \(4\nmid n\), no constant term in \(f\) is allowed, so there is no degree-\(-2\) derivation. This proves the sharp mod-four exception and the theorem.

## Verification
The standalone file `verify.py` independently constructs the full linear system for a completely unrestricted endomorphism to satisfy the Leibniz rule. It computes modular ranks, checks every proposed homogeneous basis map in odd characteristic, and checks the explicit splitting basis maps in characteristic two. Execute `python3 verify.py` from the directory containing this file. The reported successful check covered \(65\) positive-characteristic dimension-and-basis cases, \(7\) characteristic-zero dimension cases, and two larger characteristic-two boundary cases. These are finite corroborations; the arbitrary-\(n\) result follows from the proof above.

## Relationship to prior work
The general theory of Novikov products, their Lie-admissibility, and low-dimensional classifications appears in the sources below. Bai and Meng studied automorphisms in low dimensions; Burde, Dekimpe, and Vercammen studied ideals and Lie-algebra structures; Burde and de Graaf classify low-dimensional Novikov algebras in characteristic zero. None of those inspected accessible treatments gives the present all-dimensional, characteristic-dependent derivation formula. Strachan's explicit derivations concern the **underlying commutative associative algebra**, not the derivations of the Novikov product. The 2026 work on truncated polynomial Novikov cohomology considers the full quotient with a constant basis vector and computes second cohomology, whereas this result concerns ordinary derivations of the positive-degree ideal for arbitrary truncation lengths. The comparison does not assert uniqueness or independent priority certification.

## Limitations
The theorem concerns the specified positive truncated one-variable family, not all Novikov algebras, their automorphism group schemes, or derivations of an unrelated associative quotient. In positive characteristic, the identity between the automorphism-group tangent space and ordinary derivations may require group-scheme care. Earlier literature on low-dimensional automorphisms was not completely available in full text; broader unpublished or non-indexed formulae could imply pieces of the result. No independent mathematical audit has been performed.

## References
1. C. Bai and D. Meng, *The automorphisms of Novikov algebras in low dimensions*, Journal of Physics A 36 (2003), 7715–7731, DOI `10.1088/0305-4470/36/28/303` (published 2003-07-01).
2. D. Burde, K. Dekimpe, and K. Vercammen, *Novikov algebras and Novikov structures on Lie algebras*, arXiv:`0705.1316v1` (first posted 2007-05-09).
3. D. Burde and W. A. de Graaf, *Classification of Novikov algebras*, arXiv:`1106.5954v1` (first posted 2011-06-29).
4. I. A. B. Strachan, *A construction of multidimensional Dubrovin–Novikov brackets*, Journal of Nonlinear Mathematical Physics 26 (2019), 202–213, DOI `10.1080/14029251.2019.1591716`.
5. *Cohomology and extensions of Novikov algebras of truncated polynomials*, arXiv:`2608.25372v1` (2026), Sections 1 and 8 (distinct full-quotient cohomological setting).
