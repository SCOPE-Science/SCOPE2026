# Binary-quadratic trichotomy and exact census for two-dimensional stable squares

## Finding

Let \(S\) be any two-dimensional commutative algebra over a field \(K\), and assume \(S^2=S\), where \(S^2\) means the linear span of all products. Its multiplication tensor is a surjection \(\mu:\operatorname{Sym}^2_K(S)\rightarrow S\). The kernel is a line. Choosing a basis \(u,v\), identify that line with a binary homogeneous quadratic \(F(X,Y)\) (well defined up to nonzero scalar and invertible change of variables).

**Trichotomy.** The algebra \(S\) has a natural basis (equivalently, is an evolution algebra) if and only if \(F\) is a product of two *linearly independent* linear forms over \(K\). A repeated factor never permits a natural basis, even after field extension. An irreducible kernel has none over \(K\), but acquires one over its splitting field when the quadratic is separable (in particular, for every finite field).

**Sharp ambient realization.** Every \(S\) as above, including repeated-factor and irreducible types, is isomorphic to a stable derived square \(E^2=(E^2)^2\) of some three-dimensional evolution algebra \(E\) over the *same* field \(K\). Its least possible ambient evolution-algebra dimension is \(2\) when \(S\) is evolution and \(3\) otherwise.

**Exact finite-field count.** Fix a labeled two-dimensional vector space over \(\mathbb F_q\). Put \(g_q=|\operatorname{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\). Among commutative multiplications with full square, the numbers of structures with distinct split kernel, repeated kernel, and irreducible kernel are respectively

\[
 g_q\frac{q(q+1)}2,\qquad g_q(q+1),\qquad g_q\frac{q(q-1)}2.
\]

Their sum is \((q^3-1)(q^3-q)\). Exactly the distinct-split class consists of evolution algebras. Each such multiplication has exactly \(2(q-1)^2\) **ordered** natural bases. Over \(\mathbb F_{q^2}\), all irreducible kernels split into distinct factors; repeated kernels remain repeated under every extension.

## Assumptions and scope

A commutative algebra here is an arbitrary symmetric bilinear product: **associativity is not assumed**. The field is unrestricted, including characteristic two. A natural basis is a vector-space basis \(a,b\) with \(ab=0\). A labeled multiplication means an actual bilinear product on a fixed two-dimensional vector space, not an isomorphism class. The derived sequence is \(E^{(1)}=E\), \(E^{(r+1)}=(E^{(r)})^2\). The count is for **surjective multiplication tensors** only. In an arbitrary field, irreducible inseparable quadratic kernels can behave differently upon extension, so the extension assertion in the theorem is restricted to finite fields.

## Proof

**Kernel criterion.** The domain \(\operatorname{Sym}^2_K(S)\) has dimension three and the codomain has dimension two. Surjectivity gives a unique one-dimensional kernel. For linearly independent vectors \(a,b\), their symmetric product \(a\odot b\) is nonzero, and its image under \(\mu\) is \(ab\). Therefore \(ab=0\) holds exactly when \(a\odot b\) spans the kernel. Identifying \(a\odot b\) with a homogeneous binary quadratic, this is equivalent to a factorization into two nonproportional linear forms. This argument is valid even when \(2=0\); it does not use polarization of a square map. A split kernel determines precisely two lines of possible natural-basis vectors. Thus over \(\mathbb F_q\) there are two orders and \(q-1\) scalar choices on each line, yielding \(2(q-1)^2\) ordered natural bases.

**Explicit three-dimensional realization.** Choose any basis \(u,v\) of \(S\), and abbreviate \(a=u^2\), \(b=uv\), \(c=v^2\). On a three-dimensional vector space \(E\) with basis \(e_1,e_2,e_3\), define \(i(u)=e_1+e_3\), \(i(v)=e_2+e_3\), and

\[
 e_1^2=i(a-b),\qquad e_2^2=i(c-b),\qquad e_3^2=i(b),\qquad e_ie_j=0\quad(i\ne j).
\]

These equations define an evolution algebra. Direct expansion gives \(i(u)^2=i(a)\), \(i(u)i(v)=i(b)\), and \(i(v)^2=i(c)\). Thus \(i\) is an injective algebra homomorphism. The span of the three basis squares equals \(i(\operatorname{span}\{a,b,c\})=i(S)\), so \(E^2=i(S)\) and \((E^2)^2=i(S^2)=i(S)\). If \(S\) is non-evolution, it cannot equal the square of a two-dimensional evolution algebra with stabilized dimension two: such an algebra's square is its entire evolution algebra. Hence ambient dimension three is optimal; evolution \(S\) itself gives ambient dimension two otherwise.

**Enumeration.** Homogeneous quadratics up to scalar on a two-dimensional vector space comprise \(q^2+q+1\) projective points. There are \(q+1\) rational projective linear forms. Unordered pairs of *distinct* forms number \(\binom{q+1}{2}=q(q+1)/2\), giving exactly the split square-free quadratic points; squares of one rational linear form give \(q+1\) repeated points. Every remaining point is irreducible, giving \(q(q-1)/2\). For each chosen one-dimensional kernel, the quotient of the three-dimensional symmetric square has dimension two; a surjective multiplication tensor with that kernel is exactly an isomorphism of this quotient with the labeled codomain. There are \(g_q\) choices, proving the three counts and their sum. Every irreducible degree-two polynomial over a finite field is separable and splits over its quadratic extension; multiplicities of a repeated factor persist after any extension.

**Witnesses.** Over \(\mathbb F_2\), the multiplication \(u^2=u\), \(uv=v\), \(v^2=u+v\) has kernel generated by \(X^2+XY+Y^2\), irreducible over \(\mathbb F_2\). The ambient construction becomes \(e_1^2=e_1+e_2\), \(e_2^2=e_1+e_3\), \(e_3^2=e_2+e_3\). The square is a stabilized non-evolution algebra over \(\mathbb F_2\) but acquires a natural basis over \(\mathbb F_4\). The example \(u^2=0\), \(uv=u\), \(v^2=v\) has kernel generated by \(X^2\) and never becomes evolution under any field extension.

## Verification

Run `python verify.py` with Python 3 (standard library only). The script enumerates every surjective symmetric multiplication tensor \(\mathbb F_q^3\to\mathbb F_q^2\) for \(q=2,3,4,5\); \(\mathbb F_4\) uses actual quotient-field arithmetic. It independently enumerates every ordered basis to check orthogonality and checks the ambient three-dimensional construction. Observed counts \((N_{\mathrm{split}},N_{\mathrm{double}},N_{\mathrm{irreducible}})\) are \((18,18,6)\), \((288,192,144)\), \((1800,900,1080)\), and \((7200,2880,4800)\), respectively. All checks end in `VERIFY_OK`. Exhaustive finite computation checks only these four fields; the all-field and all-prime-power statements follow from the proof above.

## Relationship to prior work

Hu and Wen explicitly ask when the stable derived term of an evolution algebra is itself evolution, and give a three-dimensional complex counterexample. The present classification resolves the **entire two-dimensional perfect stable-term stratum**, including repeated, split, and irreducible field-arithmetic behavior, and supplies a sharp realization for each type and an exact labeled finite-field census. The established classification of two-dimensional perfect **evolution** algebras by Cabrera Casado, Martín Barquero, and Martín González already includes natural-basis uniqueness (used here, not claimed as a separate discovery). General embedding results of Costoya, Fernández Ouaridi, and Viruel concern commutative algebras as ideals of evolution algebras; the theorem here concerns specifically **the stable full square** and the distribution of all surjective two-dimensional commutative multiplication tensors.

## Limitations

This describes two-dimensional stabilized squares \(E^2\) with \((E^2)^2=E^2\), not all higher-dimensional stabilized terms, and enumerates labeled multiplication tensors rather than isomorphism classes. The finite-field quadratic splitting assertion does not extend verbatim to inseparable irreducible quadratics over imperfect fields. The general embedding paper cited below could not be fully inspected, so unrecognized historical overlap remains possible.

## References

1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over \(\mathbb C\)*, arXiv:2609.25023v1 (2026); earlier publicly posted on Preprints.org, manuscript 202609.0078 (September 1, 2026), especially the question on stable derived terms and its two-dimensional example.
2. Y. Cabrera Casado, D. Martín Barquero, and C. Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics 58 (2023), 569–587, DOI:10.1007/s10801-022-01196-1.
3. E. Costoya, A. Fernández Ouaridi, and A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784 (2026); abstract consulted, full text not verified.
