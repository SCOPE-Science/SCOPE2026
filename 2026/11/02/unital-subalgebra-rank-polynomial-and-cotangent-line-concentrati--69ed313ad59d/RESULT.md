# Unital subalgebra rank polynomial and cotangent-line concentration in free cube-zero local rings

## Finding
Let \(q\) be any prime power and \(d\ge2\). Put
\[
A_{d,q}=\mathbb F_q[X_1,\ldots,X_d]/(X_1,\ldots,X_d)^3,
\qquad D=\binom{d+1}{2}.
\]
Let \(S_{d,q}(z)=\sum_B z^{\dim_{\mathbb F_q}B}\), summed over *all* unital \(\mathbb F_q\)-subalgebras \(B\subseteq A_{d,q}\), including \(\mathbb F_q\) and the full ring. With \({a\brack b}_q\) denoting the Gaussian binomial coefficient, interpreted as zero when \(b\notin[0,a]\), one has the exact finite formula
\[
S_{d,q}(z)=\sum_{s=0}^{d}{d\brack s}_q
\sum_{r=\binom{s+1}{2}}^{D}
 {D-\binom{s+1}{2}\brack r-\binom{s+1}{2}}_q
 q^{s(D-r)}z^{1+s+r}.
\tag{1}
\]
In particular every subalgebra-dimension count is a polynomial in \(q\) with nonnegative integer coefficients. If \(B\) is chosen uniformly from these subalgebras and \(\mathfrak m=(X_1,\ldots,X_d)/(X_1,\ldots,X_d)^3\), then, as \(d\to\infty\) with the field size \(q\) fixed,
\[
\Pr\left(\dim_{\mathbb F_q}\frac{(B\cap\mathfrak m)+\mathfrak m^2}{\mathfrak m^2}=1\right)
=1-\frac{1+o(1)}{{d\brack1}_q}
=1-(q-1+o(1))q^{-d}.
\tag{2}
\]
Thus a uniformly sampled unital subalgebra almost surely has precisely a *line* as its first-order (cotangent) image, despite the ambient embedding dimension tending to infinity.

## Assumptions and scope
All subalgebras are required to contain the original identity and the entire scalar field \(\mathbb F_q\). This is different from counting arbitrary unital subrings that are not \(\mathbb F_q\)-linear. The integer \(d\ge2\) is arbitrary, and the field may have any characteristic, including two. Set \(V=\mathfrak m/\mathfrak m^2\cong\mathbb F_q^d\) and \(Z=\mathfrak m^2\cong\operatorname{Sym}^2(V)\), of dimensions \(d\) and \(D\). The vector-space splitting \(\mathfrak m=V\oplus Z\) comes from homogeneous degree. Multiplication is the natural symmetric product \(V\times V\to Z\), and all products involving \(Z\) and \(\mathfrak m\) vanish. The symbol \(o(1)\) in (2) is for fixed \(q\), not uniform in the field size.

## Proof
**Parametrization and closure.** Every unital \(\mathbb F_q\)-subalgebra has the unique form \(B=\mathbb F_q1\oplus W\) for a vector subspace \(W\le\mathfrak m\). Indeed, the scalar part can be removed because \(1\in B\). Write \(U\le V\) for the projection of \(W\) onto \(V\), and \(T=W\cap Z\le Z\). Let \(s=\dim U\) and \(r=\dim T\). The induced quotient \(W/T\to U\) is an isomorphism, so \(W\) is the graph modulo \(T\) of a unique \(\mathbb F_q\)-linear map \(\phi:U\to Z/T\). Hence, for fixed \(U,T\), there are \(q^{s(D-r)}\) candidate subspaces.

For \(u,u'\in U\), the product of any lifts in \(W\) equals \(uu'\in Z\) independently of the lifts' quadratic parts, because \(Z\mathfrak m=0\). Closure under multiplication is therefore equivalent to \(uu'\in T\) for every \(u,u'\in U\). The span of these products is exactly the embedded \(\operatorname{Sym}^2 U\subseteq\operatorname{Sym}^2 V\), of dimension \(e_s=\binom{s+1}{2}\), even in characteristic two: all basis products \(u_i u_j\) for \(i\le j\) are independent monomials. Thus the necessary and sufficient condition is
\[
\operatorname{Sym}^2 U\subseteq T.
\tag{3}
\]
There are \({d\brack s}_q\) choices of \(U\), and \({D-e_s\brack r-e_s}_q\) choices of a dimension-\(r\) space \(T\) containing \(\operatorname{Sym}^2U\). Multiplying the independent counts and inserting \(\dim B=1+s+r\) proves (1). This classifies each subalgebra uniquely rather than merely counting a covering family.

**Asymptotic concentration.** Let \(H_q(N)=\sum_{j=0}^N{N\brack j}_q\) be the number of subspaces of an \(N\)-space. Denote by \(N_s\) the number of subalgebras in (1) whose projection \(U\) has dimension \(s\). Then
\[
N_0=H_q(D),\qquad
N_1={d\brack1}_q\bigl(H_q(D)-H_q(D-1)\bigr).
\tag{4}
\]
For the second identity, fix \(U\) of dimension one and divide the ambient \(U\oplus Z\) by the compulsory quadratic line \(\operatorname{Sym}^2U\). The resulting vector space has dimension \(D\), with a distinguished \((D-1)\)-space from \(Z\); precisely \(H_q(D)-H_q(D-1)\) subspaces project nontrivially to \(U\).

For fixed \(q\), standard Gaussian-product estimates give positive constants depending only on \(q\) such that
\[
q^{\lfloor N^2/4\rfloor}\le H_q(N)
\le C_q q^{\lfloor N^2/4\rfloor}.
\tag{5}
\]
For completeness, the bounds follow from \(q^{j(N-j)}\le{N\brack j}_q\le c_q^{-1}q^{j(N-j)}\), where \(c_q=\prod_{i=1}^{\infty}(1-q^{-i})>0\), and summing the resulting Gaussian decay away from \(j=N/2\). Thus \(H_q(D-1)/H_q(D)=O_q(q^{-D/2})\) and \(N_1\sim {d\brack1}_q N_0\).

It remains to show that \(\sum_{s=2}^dN_s=o(N_0)\). Set \(a_s=\binom{s}{2}\) and change variables \(t=D-r\) in (1). The Gaussian bounds above yield
\[
N_s\le C_q'(D+1)q^{s(d-s)+(D-a_s)^2/4},\qquad 2\le s\le d,
\tag{6}
\]
with \(C_q'\) independent of \(d,s\). Indeed the exponent from the inner Gaussian coefficient and the graph-map factor is \(t(D-a_s-t)\le(D-a_s)^2/4\). As \(N_0\ge q^{\lfloor D^2/4\rfloor}\), the relative exponent in (6) is bounded by
\[
sd-\frac{a_s(2D-a_s)}4+1
\le sd-\frac{a_sD}{4}+1.
\tag{7}
\]
For \(s=2\), this is \(2d-D/4+1\), which tends to negative infinity quadratically. Uniformly for \(s\ge3\), \(a_s\ge s(s-1)/2\), so (7) is at most \(sd-s(s-1)D/8+1\); summing these bounds over \(s\in[3,d]\) still tends to zero after the polynomial factor \(D+1\). It follows that \(\sum_{s\ge2}N_s=o(N_0)\). Combining with (4) gives
\[
\frac{N_0+\sum_{s\ge2}N_s}{\sum_{s\ge0}N_s}
=\frac{1+o(1)}{{d\brack1}_q},
\]
which proves (2).

## Verification
The standalone program `verify.py` directly constructs *all* subspaces of the nilpotent ideal using reduced row echelon bases for \((d,q)=(1,2),(1,3),(2,2),(2,3)\). It evaluates the multiplication of quadratic-truncated polynomials and independently checks whether each subspace is closed under multiplication. Its exact dimension and first-order-image profiles agree with (1). Specifically, for \(d=2,q=2\), the six dimension strata are \((1,7,19,19,3,1)\), totaling \(50\), and for \(d=2,q=3\) they are \((1,13,49,49,4,1)\), totaling \(117\). Direct enumeration checks all \(374\) vector subspaces in the former case and all \(2664\) in the latter. Larger parameter outputs evaluate the proved formula only; they are not exhaustive censuses and do not support an infinite proof independently. No computational step is required by the symbolic proof.

## Relationship to prior work
F. Franco Muñoz, *The existence of non-thin subalgebras of \(K[x]/x^n\) and related numerical monoids* (2018, arXiv:1812.03576), enumerates and studies unital subalgebras in **one-variable** truncated polynomial rings. The \(d=1\) base example of the present counting scheme is therefore not claimed as new. The work does not supply the multivariable rank polynomial or the fixed-field growing-embedding-dimension law (2). S. Blackburn and K. R. McLean, *The enumeration of finite rings* (2022, DOI:10.1112/jlms.12661), treat cube-zero commutative algebras in the context of counting **isomorphism classes of ambient algebras**, not subalgebras inside the fixed free cube-zero algebra. K. Isham, *Is the number of subrings of index \(p^e\) in \(\mathbb Z^n\) polynomial in \(p\)?* (2022, arXiv:2203.00646), investigates a different ambient ring and finite-index problem.

H. Strade, *Enumeration results in nilpotent algebras* (1975, DOI:10.1090/S0002-9939-1975-0357526-4), is particularly relevant because its accessible bibliographic abstract describes subalgebra enumeration in nilpotent alternative algebras, a category containing associative examples. The full text could not be inspected in this comparison. Therefore no claim is made that this paper is inapplicable, and the novelty comparison to any more general exact theorem in it remains a material risk. A separate existing classification could also imply (1). The result here is offered as a self-contained mathematical argument, not a claim of independently established priority.

## Limitations
This result counts \(\mathbb F_q\)-linear unital subalgebras, not arbitrary unital subrings, not ideals, and not isomorphism classes of subalgebras. The asymptotic holds with \(q\) fixed as \(d\to\infty\). It does not address higher nilpotency lengths or quotients with relations among quadratic monomials. Direct finite verification covers prime fields \(\mathbb F_2\) and \(\mathbb F_3\) in the smallest dimensions, while the proof covers all prime powers. Independent mathematical audit and independent publication-priority verification have not been performed.

## References
1. F. Franco Muñoz, *The existence of non-thin subalgebras of \(K[x]/x^n\) and related numerical monoids*, arXiv:1812.03576, first public 2018-12-09. https://arxiv.org/abs/1812.03576
2. K. Isham, *Is the number of subrings of index \(p^e\) in \(\mathbb Z^n\) polynomial in \(p\)?*, arXiv:2203.00646, first public 2022-03-01. https://arxiv.org/abs/2203.00646
3. S. R. Blackburn and K. R. McLean, *The enumeration of finite rings*, J. London Math. Soc. 106 (2022), DOI:10.1112/jlms.12661. https://doi.org/10.1112/jlms.12661
4. H. Strade, *Enumeration results in nilpotent algebras*, Proc. Amer. Math. Soc. 49 (1975), 20–24, DOI:10.1090/S0002-9939-1975-0357526-4. https://doi.org/10.1090/S0002-9939-1975-0357526-4
