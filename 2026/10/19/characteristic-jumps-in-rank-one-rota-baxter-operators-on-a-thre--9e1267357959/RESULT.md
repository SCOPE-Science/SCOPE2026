# Characteristic jumps in rank-one Rota–Baxter operators on a three-generator exterior algebra

## Finding
Let \(K=\mathbb F_q\) be a finite field, let \(V=K^3\), and write \(E=\Lambda_K(V)\), an eight-dimensional unital associative algebra. A linear map \(R:E\to E\) is a weight-zero Rota–Baxter operator when
\[
R(a)R(b)=R\bigl(R(a)b+aR(b)\bigr)\qquad(a,b\in E).
\]
The number \(\mathcal N_q\) of operators of **linear rank exactly one** is
\[
\boxed{\mathcal N_q=(q^2+q+1)\{q^{3+\epsilon_q}(q^4-1)+q(q^6-1)\}+q^7-1,}
\]
where \(\epsilon_q=1\) if \(\operatorname{char}K=2\), and \(\epsilon_q=0\) otherwise. More precisely, each nonzero rank-one operator has the unique form \(R(a)=f(a)u\), after choosing a nonzero representative \(u\) of its image line, with
\[
u^2=0,\qquad f(uE+Eu)=0,\qquad f\ne0.
\]
Its image line has lowest nonzero exterior degree \(1\), \(2\), or \(3\). The respective dimensions of \(uE+Eu\) are exactly \(4,2,1\); the respective numbers of image lines are
\[
\bigl(q^{3+\epsilon_q}(q^2+q+1),\ q(q^2+q+1),\ 1\bigr).
\]
Every such operator satisfies \(R^2=0\). Over an algebraically closed field, the rank-one weight-zero Rota–Baxter locus has dimension \(10\) in characteristic two and dimension \(9\) in every other characteristic. The first finite-field counts are \(\mathcal N_2=2689\), \(\mathcal N_3=58658\), \(\mathcal N_4=1731243\), and \(\mathcal N_5=4917844\).

## Assumptions and scope
All fields in the counting theorem are finite, of arbitrary prime-power cardinality; no assumption of algebraic closure is made. Exterior algebras are unital, including in characteristic two, where the exterior multiplication becomes commutative while every degree-one generator still squares to zero. Rank means rank of the underlying \(K\)-linear map, not exterior degree. The geometric dimension assertion is about the rank-exactly-one locus over algebraically closed fields of the indicated characteristic. Operators of rank zero or ranks at least two are not classified here.

## Proof
**Rank-one reduction.** For \(R(a)=f(a)u\) with \(u\ne0\) and \(f\ne0\), apply the identity with \(a\in\ker f\) and \(f(b)\ne0\). It follows that \(f(au)=0\). Reversing the roles gives \(f(ub)=0\) for \(b\in\ker f\). Therefore the functionals \(a\mapsto f(au)\) and \(b\mapsto f(ub)\) are scalar multiples \(\alpha f\) and \(\beta f\). Substitution into the full identity yields \(u^2=(\alpha+\beta)u\).

The exterior algebra is local, with nilpotent maximal ideal \(J=\bigoplus_{i=1}^3\Lambda^iV\) and residue field \(K\). If \(u^2=cu\) with \(c\ne0\), then \(c^{-1}u\) is a nonzero idempotent, hence equals \(1\). Thus \(u=c1\), forcing \(\alpha=\beta=c\) and hence \(c^2=2c^2\), impossible in any field. Consequently \(u\in J\), \(u^2=0\). Left and right multiplication by \(u\) are square-zero endomorphisms. Since \(\alpha,\beta\) are their eigenvalues on the nonzero functional \(f\), they must both vanish. Thus \(f(J)\) need not vanish, but \(f(uE+Eu)=0\) is necessary. Conversely these two conditions make both sides of the Rota–Baxter identity zero. In particular \(f(u)=0\) and \(R^2=0\).

**Images and ideals.** Write uniquely \(u=v+w+z\), where \(v\in V\), \(w\in\Lambda^2V\), and \(z\in\Lambda^3V\). In odd characteristic, \(u^2=2v\wedge w\), so the square-zero condition is \(v\wedge w=0\). For \(v\ne0\), its wedge map on \(\Lambda^2V\) has a two-dimensional kernel \(v\wedge V\). Hence \(w=v\wedge a\) and \(z=v\wedge b\) for suitable \(a\in V\), \(b\in\Lambda^2V\), and \(u=v(1+a+b)\). The second factor is a unit. As \(vE=Ev\) is a two-sided ideal, \(uE+Eu=vE\), of dimension four.

In characteristic two every \(u\in J\) squares to zero. If \(v\ne0\), choose a basis with first vector \(v\). The generator substitution \(v\mapsto u\), fixing the other two generators, defines an automorphism: all images square to zero and the induced map on \(J/J^2\) is invertible, so the algebra map is surjective and hence bijective. It follows again that \(uE+Eu\) has dimension four.

If \(v=0\) and \(w\ne0\), every nonzero two-form in dimension three is decomposable and generates \(\Lambda^3V\) by multiplication with \(V\). Hence \(u=w(1+a)\) for some \(a\in V\). The factor is a unit, and \(w\) is central in the three-generator exterior algebra, so \(uE=Eu=wE\), of dimension two. Finally, when only \(z\ne0\), the ideal \(zE=Ez=Kz\) has dimension one.

**Projective enumeration.** Image lines, rather than nonzero vectors, index the possible rank-one images; divide every nonzero-vector count by \(q-1\). For \(v\ne0\), odd characteristic permits \((q^3-1)q^2q\) square-zero vectors (choices of \(v,w,z\)); characteristic two permits \((q^3-1)q^3q\). They give \(q^{3+\epsilon_q}(q^2+q+1)\) image lines. For \(v=0,w\ne0\), the vector count is \((q^3-1)q\), giving \(q(q^2+q+1)\) lines. The socle gives one line. For a fixed line with ideal dimension \(r\), precisely \(q^{8-r}-1\) nonzero functionals annihilate the ideal, each producing a distinct rank-one operator after the representative is fixed. Summing at \(r=4,2,1\) proves the stated formula.

**Geometric dimension.** The image-line bases of the three strata have dimensions \((5,3,0)\) in odd characteristic and \((6,3,0)\) in characteristic two. Over each base the permissible nonzero functionals form a Zariski-locally trivial vector-bundle complement with fiber dimensions \((4,6,7)\). Thus the maximal total dimension is \(\max(5+4,3+6,0+7)=9\) in odd characteristic and \(\max(6+4,3+6,0+7)=10\) in characteristic two.

## Verification
The standalone standard-library script `verify.py` uses exterior basis masks and checks both left and right multiplication ideals by finite-field linear algebra. It exhaustively enumerates all square-zero image lines over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), matching each of the three predicted ideal ranks and the total counts. A separate exhaustive test over \(\mathbb F_2\) checks the original Rota–Baxter identity on every pair of basis elements for every rank-one linear map (\(255\) possible image lines times \(255\) nonzero functionals), obtaining exactly \(2689\) valid maps. Execute `python3 verify.py`. These finite checks do not replace the proof over all finite fields or of the algebraic-geometric dimension assertion.

## Relationship to prior work
Benito, Gubarev and Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras* (2018), §5.2, classify weight-zero operators on the **four-dimensional exterior algebra on two generators** up to conjugacy. Shakoor and Noor-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra* (first public version September 7, 2026), Theorem 4.1, also treat the two-generator four-dimensional algebra over the reals. A published finite-field computation gives an exact total and rank distribution for that four-dimensional algebra over \(\mathbb F_2\). None of these statements, as inspected, determines the rank-one stratum of the **eight-dimensional exterior algebra on three generators** or the dimension jump across characteristics. The present proof uses a general elementary rank-one reduction and new three-generator multiplication-ideal and incidence counts; it does not claim those elementary reduction techniques as new.

## Limitations
No classification of higher-rank Rota–Baxter operators on the eight-dimensional algebra is claimed, and there is no claim about exterior algebras on four or more generators. Finite experiments cover only the listed small fields; prime-power generality and geometric dimensions depend on the symbolic proof. An equivalent enumeration in literature using different operator or tensor terminology remains possible. This result has not undergone independent mathematical validation.

## References
1. K. Shakoor and Noor-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra*, arXiv:2609.07377, v1 first posted 2026-09-07; full-text Theorem 4.1. https://arxiv.org/abs/2609.07377
2. P. Benito, V. Gubarev and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037, §5.2, Proposition 1 (2018). https://arxiv.org/abs/1801.07037
3. *Weight-zero Rota–Baxter operators on the four-dimensional exterior algebra over \(\mathbb F_2\)*, public mathematical result, October 4, 2026, published-finding corpus record `2026/10/4/SCOPE-weight-zero-rota-baxter-operators-on-the-four-dimensional-exteri--6ed2dc859a4a`.
