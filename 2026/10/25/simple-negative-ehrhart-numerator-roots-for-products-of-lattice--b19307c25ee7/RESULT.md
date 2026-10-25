# Simple negative Ehrhart numerator roots for products of lattice polygons

## Finding

Let \(P,Q\subset\mathbb R^2\) be any two full-dimensional lattice polygons. The Ehrhart numerator \(h^*_{P\times Q}(t)\) of their Cartesian product in \(\mathbb R^4\) has **only simple strictly negative real zeros**, regardless of whether either factor numerator is real-rooted. The statement includes all lattice polygons having exactly three boundary lattice points.

Writing \(I_P,B_P,I_Q,B_Q\) for the interior and boundary lattice-point counts of the respective polygons, set
\[
 a=I_P+B_P-3,\qquad b=I_P,\qquad c=I_Q+B_Q-3,\qquad d=I_Q.
\]
Then \(h^*_{P\times Q}(t)=1+p t+q t^2+r t^3+s t^4\), where
\[
\begin{aligned}
p&=a(c+3)+3c+4,\\
q&=a(4c+3d+3)+b(3c+d+6)+3c+6d+1,\\
r&=a(c+3d)+b(3c+4d),\\
s&=bd.
\end{aligned}
\]
Its degree is \(4\) if both polygons have interior lattice points; otherwise it can be \(3\) or \(2\). In every case all roots of the actual-degree polynomial are distinct.

For example, \(T=\operatorname{conv}\{(0,0),(2,1),(1,2)\}\) has \(I_T=1\) and \(B_T=3\), hence \(h_T^*(t)=1+t+t^2\) with two nonreal roots. Nevertheless
\[
h^*_{T\times T}(t)=1+11t+30t^2+11t^3+t^4
=(t^2+4t+1)(t^2+7t+1),
\]
with four distinct negative roots.

## Assumptions and scope

All polygons are convex, full-dimensional in their own integer-coordinate planes, and have vertices in \(\mathbb Z^2\). There are no restrictions on lattice width, symmetry, number of vertices, or positivity of the interior count. The Cartesian product is taken with the product lattice \(\mathbb Z^4\). We define
\[
L_K(n)=\#(nK\cap\mathbb Z^{\dim K}),\qquad
\sum_{n\ge0}L_K(n)t^n=\frac{h_K^*(t)}{(1-t)^{\dim K+1}}.
\]
The root assertion concerns the nonzero roots of the actual-degree numerator; zero trailing coefficients are not counted as roots.

## Proof

**Step 1 — Ehrhart data.** Pick's theorem and Ehrhart's formula yield
\[
L_P(n)=\left(I_P+\frac{B_P}{2}-1\right)n^2+\frac{B_P}{2}n+1,
\quad h_P^*(t)=1+a t+b t^2,
\]
where \(a\ge b\ge0\), since \(B_P\ge3\). Analogous formulas hold for \(Q\). By the Cartesian-product counting identity \(L_{P\times Q}(n)=L_P(n)L_Q(n)\) and the binomial basis
\[
L_P(n)=\sum_{i=0}^2 h_i^*(P)\binom{n+2-i}{2},
\]
coefficient extraction gives precisely the four displayed coefficients \(p,q,r,s\). These identities also follow by applying the finite-difference formula
\[
 h_k^*(P\times Q)=\sum_{j=0}^k(-1)^j\binom{5}{j} L_P(k-j)L_Q(k-j),\qquad 0\le k\le4.
\]

**Step 2 — an exact discriminant certificate.** The following positivity assertions are identities in polynomial rings over \(\mathbb Z\), certified by complete monomial expansions. The adjoining `coefficient_certificate.json` stores **every** nonzero monomial and its strictly positive integer coefficient. The standalone `verify.py` recomputes both sides from the formulas above using exact symbolic arithmetic and tests all coefficients; it does not sample parameters.

When \(b,d\ge1\), put
\[
 X=a-b=B_P-3,\quad Y=b-1=I_P-1,\quad U=c-d=B_Q-3,\quad V=d-1=I_Q-1.
\]
All four variables are nonnegative. In these variables the quartic discriminant \(\operatorname{disc}_t(h^*_{P\times Q})\) has exactly **784** nonzero monomials, all with positive integer coefficients and positive constant term \(43740\). Also, \(p^2-4q\) and \(pr-2s\) each have exactly **36** monomials with positive integer coefficients. In particular \(p^2>4q\) and \(pr>2s\). Consequently
\[
 h^*_{P\times Q}(-2/p)
 =-1+\frac{4q}{p^2}-\frac{8r}{p^3}+\frac{16s}{p^4}<0.
\]
Since the quartic has positive leading coefficient and value \(1\) at zero, it has at least two distinct negative real roots. A real quartic with strictly positive discriminant has either four distinct real roots or no real roots, so here all four are distinct and real. All coefficients are positive, excluding nonnegative roots.

When \(b=0<d\), set \(X=a=B_P-3\), \(U=c-d=B_Q-3\), \(V=d-1=I_Q-1\). If \(X>0\), the numerator is cubic, and its cubic discriminant has **75** monomials with positive integer coefficients (constant term \(900\)). The cubic therefore has three distinct real roots, necessarily strictly negative. If \(X=0\), it is quadratic, and its discriminant is
\[
 3(3U^2+6UV+10U+3V^2+2V+3)>0.
\]
The case \(d=0<b\) follows by exchanging the two polygons.

When \(b=d=0\), set \(X=a=B_P-3\), \(U=c=B_Q-3\). If \(XU>0\), the numerator is cubic and its discriminant has **25** monomials with positive integer coefficients, hence three distinct negative roots. If \(XU=0\), the numerator is quadratic; assuming \(X=0\) by symmetry, its discriminant is \(9U^2+12U+12>0\). This exhausts all admissible polygons and proves the theorem.

**How the finite certificate is verified.** Each discriminant is the univariate discriminant of the explicitly displayed numerator, expanded as a polynomial in the nonnegative parameters. The certificate records complete integer exponent vectors and coefficients, not a numerical sample or a truncated enumeration. `verify.py` independently constructs the numerator from the Ehrhart binomial formula, generates all seven coefficient lists, checks their lengths and positivity, and compares each against the stored exhaustive list. The only external mathematical fact used for the degree-four root count is the standard sign classification of real quartic discriminants.

## Verification

Place `verify.py` and `coefficient_certificate.json` together, install SymPy 1.12 or later, and run `python3 verify.py`. The expected success marker is `POLYGON_PRODUCT_CERTIFIED`, followed by monomial counts `784,36,36,75,25,6,3`. The command computes exact integers and rational polynomials; it performs no numerical root fitting. The stored coefficient lists make the machine-assisted algebra independently inspectable. The proof is universal because the checked polynomial coefficient inequalities imply positivity for every admissible integer parameter tuple, rather than because any finite selection of polygons was enumerated.

## Relationship to prior work

Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338 (first submitted October 5, 2026), Section 2, records the Hadamard-product formula and the Wagner real-rootedness preservation theorem when **both input numerators are already real-rooted**. Yanxin Liu and Jianxi Mao, arXiv:2609.11589, prove preservation of log-concavity under products, which is weaker than the present simple real-rootedness conclusion. Brändén, Ferroni and Jochemko, arXiv:2408.12386, prove preservation of ultra log-concavity and related coefficient properties; their real-rootedness preservation still requires real-rooted input factors. Nill, arXiv:2608.03635, proves real-rootedness at sufficiently large lattice width, without addressing every product of lattice polygons of width one.

In fact, the individual polygon numerator \(1+(I_P+B_P-3)t+I_Pt^2\) is real-rooted unless \(B_P=3\) and \(I_P\in\{1,2,3\}\). Thus existing product-preservation theorems already cover every pair outside those three exceptional factor types. The non-implied content here is that **even the exceptional, non-real-rooted primitive-edge triangle factors** produce a simple real-rooted numerator when multiplied by the Ehrhart polynomial of *any* lattice polygon. The complete all-polygon formulation and exact simplicity statement package this exceptional-factor principle.

## Limitations

No corresponding assertion is proved for arbitrary three-dimensional factors, products of three or more lattice polygons, arbitrary quadratic polynomials with real nonintegral Ehrhart-like parameters, or rational nonlattice polygons. Historical priority of the exceptional-factor statement is subject to further literature scrutiny. The algebraic positivity certificate is an exact finite symbolic computation, not a human-expanded proof of every one of its 784 quartic discriminant terms; independent audit has not been performed.

## References

1. F. Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, first public October 5, 2026, https://arxiv.org/abs/2610.06338.
2. Y. Liu and J. Mao, *Preservation of log-concavity under Hadamard products*, arXiv:2609.11589, September 10, 2026, https://arxiv.org/abs/2609.11589.
3. P. Brändén, L. Ferroni and K. Jochemko, *Preservation of inequalities under Hadamard products*, arXiv:2408.12386, August 22, 2024, https://arxiv.org/abs/2408.12386.
4. B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635, August 4, 2026, https://arxiv.org/abs/2608.03635.
5. D. G. Wagner, *Total positivity of Hadamard products*, Journal of Mathematical Analysis and Applications **163** (1992), 459–483; discussed and cited in References 1–3.
