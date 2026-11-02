# Complete elliptic splitting of the first wild \(C_6\) boundary curve over \(\mathbb F_2\)

## Finding
For the smooth projective normalization \(C/\mathbb F_2\) of
\[
y^2+y=x^3+x^{-3},
\]
its complete Hasse--Weil numerator is
\[
L_C(T)=(1+2T+2T^2)(1-2T+2T^2)(1+T+2T^2)
=1+T+2T^2+4T^4+4T^5+8T^6.
\]
Consequently \(\operatorname{Jac}(C)\sim_{\mathbb F_2} E_{-2}\times E_{+2}\times E_{-1}\), where each \(E_t\) is an elliptic curve with Frobenius trace \(t\). In particular, \(\#\operatorname{Jac}(C)(\mathbb F_2)=20\), and the geometric \(2\)-rank equals \(1\).

## Assumptions and scope
All schemes and maps are defined over \(\mathbb F_2\) unless a geometric field is specified. The curve is the smooth normalization of the affine Artin--Schreier equation, with both points above the poles included. This is the smallest genus case \(m=3\) in the two-wild-branch family \(y^2+y=c(x^m+x^{-m})\) identified by Kazemifard--Tafazolian (2026, Proposition 5.3). Over the prime field the only possible nonzero coefficient is \(c=1\). The cyclic order-six subgroup is geometric, not asserted to be pointwise defined over \(\mathbb F_2\).

## Proof
**Genus.** The rational Artin--Schreier function has two poles, at \(x=0\) and \(x=\infty\), each of odd order \(3\). Riemann--Hurwitz gives \(2g-2=-4+(3+1)+(3+1)=4\), hence \(g=3\). Each of these totally ramified poles contributes one rational point over every \(\mathbb F_{2^n}\).

**A biquadratic quotient decomposition.** The commuting involutions \(\tau:(x,y)\mapsto(x,y+1)\) and \(\sigma:(x,y)\mapsto(x^{-1},y)\) generate a Klein four-group. The full quotient has rational function coordinate \(t=x+x^{-1}\) because the \(\tau\)-fixed field is \(\mathbb F_2(x)\), and the \(\sigma\)-fixed part of that field is \(\mathbb F_2(t)\). The \(\sigma\) quotient \(E\) has equation \(y^2+y=t^3+t\), since \(x^3+x^{-3}=t^3+t\) in characteristic two. Its sole pole of order three gives genus one. The \(\sigma\tau\) quotient is the genus-two curve \(D\) with \(z=y+x/(x+1)\), satisfying
\[
z^2+z=t^3+t+t^{-1}.
\]
Indeed \(x/(x+1)^2=t^{-1}\), and \(z\) is invariant under the composite involution. Its poles have orders \(1\) and \(3\), giving \(2g(D)-2=-4+(1+1)+(3+1)=2\). The third quotient, by \(\tau\), is the rational \(x\)-line. The standard decomposition of the Jacobian for a Klein-four action with rational total quotient yields \(\operatorname{Jac}(C)\sim E\times\operatorname{Jac}(D)\) over \(\mathbb F_2\). Alternatively, its \(\ell\)-adic representation is the direct sum of the nontrivial character components; this follows by idempotents in \(\mathbb Q_\ell[(\mathbb Z/2)^2]\) for any odd \(\ell\).

**Exact point counts and polynomial.** For \(K=\mathbb F_{2^n}\), the equation \(w^2+w=a\) has two solutions precisely when \(\operatorname{Tr}_{K/\mathbb F_2}(a)=0\). Hence
\[
\#C(K)=2+2\#\{x\in K^\times:\operatorname{Tr}(x^3+x^{-3})=0\}.
\]
The two initial points are above \(0\) and infinity. Exhaustive trace evaluation in \(\mathbb F_2,\mathbb F_4,\mathbb F_8\) gives \((N_1,N_2,N_3)=(4,8,4)\); `verify.py` implements every field operation, without floating-point arithmetic. For the zeta numerator \(L(T)=\sum_{j=0}^{6}a_j T^j\), with \(a_0=1\), Newton identities applied to \(S_n=2^n+1-N_n\) yield \(a_1=1,a_2=2,a_3=0\). The genus-three functional equation gives \(a_{6-j}=2^{3-j}a_j\) for \(0\le j\le3\); therefore the displayed numerator is uniquely forced, and factors into the three shown quadratics.

**Arithmetic structure.** Each quadratic is an elliptic Weil polynomial over \(\mathbb F_2\): the traces are \(-2,+2,-1\). Explicit models are \(E_{-2}:v^2+v=t^3+t\), \(E_{+2}:v^2+v=t^3+t+1\), and \(E_{-1}:v^2+tv=t^3+1\), whose \(\mathbb F_2\)-point counts are respectively \(5,1,4\). By Tate's isogeny criterion and the factorization of Frobenius, \(\operatorname{Jac}(C)\) is \(\mathbb F_2\)-isogenous to their product. Its group order is \(L_C(1)=5\cdot1\cdot4=20\). The \(\pm2\) elliptic traces are supersingular in characteristic two, while trace \(-1\) is ordinary, so the geometric \(2\)-rank is \(1\).

## Verification
Run `python3 verify.py`. It exhaustively computes \(C\), \(E\), and \(D\) point counts over degrees one through six using explicit binary polynomial fields and the Artin--Schreier trace criterion. It verifies \(\#C(K)=\#E(K)+\#D(K)-(\#K+1)\) throughout, checks the degree-six numerator from Newton identities and the three-factor identity, and prints `VERIFY_OK`. This exact finite computation proves the finite initial data; the genus and functional-equation argument establishes all extension degrees.

## Relationship to prior work
Kazemifard and Tafazolian, *Cyclic automorphisms beyond the canonical bound* (first public 2026-10-03, arXiv:2610.04702v1), Proposition 5.3, identify this two-wild-pole family and give its geometric cyclic group and genus. That does not specify the \(\mathbb F_2\)-Frobenius polynomial, its elliptic trace triple, or the full rational isogeny decomposition. Standard biquadratic-Jacobian splitting explains why quotient curves control the answer but does not determine their zeta factors without arithmetic calculation. The computation here supplies exactly those missing arithmetic invariants in the canonical smallest case.

## Limitations
The result is for the specific \(\mathbb F_2\) model \(m=3,c=1\), not all odd \(m\) or parameters over extensions. It proves isogeny, not an explicit isogeny map or a decomposition respecting principal polarizations. It does not determine the abstract group structure of \(\operatorname{Jac}(C)(\mathbb F_2)\), only its order. No definitive claim of historical priority is made; unindexed genus-three tables and alternate presentations may contain overlapping entries.

## References
1. A. Kazemifard and S. Tafazolian, *Cyclic automorphisms beyond the canonical bound* (2026), arXiv:2610.04702v1, Proposition 5.3 and §5.1. https://arxiv.org/abs/2610.04702.
2. E. Kani and M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. **284** (1989), 307–327 (general decomposition principle).
3. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. **2** (1966), 134–144 (Frobenius isogeny criterion).

