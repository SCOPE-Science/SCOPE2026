# A global torus-slice proof of the unsaturated positive-chart equations

## Finding

Let \(S=\mathbb C[u_1,\ldots,u_n]\) have an integral \(\mathbb Z^r\)-grading, with \(1\le r\le n\). Suppose nonzero polynomials \(F_1,\ldots,F_r\) are homogeneous of respective degrees \(e_1,\ldots,e_r\), the standard basis of \(\mathbb Z^r\). Then
\[
J=(F_1-1,\ldots,F_r-1)\subset S
\]
is a prime ideal defining a smooth, geometrically integral complete intersection of dimension \(n-r\). More precisely, writing \(Y=V(J)\), the scaling action of \(G=(\mathbb G_m)^r\) gives an **explicit scheme isomorphism**
\[
Y\times G\ \xrightarrow{\ \simeq\ }\ D(F_1\cdots F_r)\subset\mathbb A^n.
\]
If \(Y\) meets the coordinate torus, then \(J:(u_1\cdots u_n)^\infty=J\).

In particular, for **every** Laurent-polynomial collection satisfying Assumption 1 of Calvo Cortes–Telen, *Positive Charts of Toric Varieties*, the Cox homogenizations \(F_i=f_i^h\) have these basis degrees. Their positive-chart closure \(U\subset\mathbb A^n\) therefore satisfies
\[
I(U)=(f_1^h-1,\ldots,f_r^h-1).
\]
This proves their Conjecture 3.11 without a saturation computation, including the permutahedral example where their computation did not finish.

## Assumptions and scope

The ground field is \(\mathbb C\). Here an integral grading means each variable \(u_j\) is assigned an integer vector \(w_j\in\mathbb Z^r\), extended additively to monomials. Write \(\lambda^{w_j}=\prod_{i=1}^r\lambda_i^{(w_j)_i}\), interpreted as a regular Laurent monomial on \(G\). The scaling action is \((\lambda\cdot u)_j=\lambda^{w_j}u_j\). The basis-degree assumption says \(F_i(\lambda\cdot u)=\lambda_iF_i(u)\) for all \(i\), \(u\), and \(\lambda\).

For the application, let \(f_1,\ldots,f_r\in\mathbb C[t_1^{\pm1},\ldots,t_d^{\pm1}]\) be nonzero. Their Newton-polytope Minkowski sum must be \(d\)-dimensional with exactly \(d+r\) facets, and the paper's square extension matrix \(M\) must have determinant \(\pm1\) (its Assumption 1). No coefficient-positivity hypothesis is necessary for this ideal-theoretic assertion. The associated divisor classes of the polynomials form a \(\mathbb Z\)-basis of the smooth toric variety's class group (their Lemma 3.3). More explicitly, in the paper's block notation \(M=(R;A)\), \(M^{-1}=(B\ K)\), where the first \(d\) rows \(R\) encode the toric rays, the last \(r\) rows of \(A\) encode the divisor representatives, and \(K\) has \(r\) integer columns. Unimodularity gives \(RK=0\) and \(AK=I_r\) (their equation (10)). Every exponent vector of \(F_i\) is \(R^\mathsf{T}m+a_i\), where \(a_i\) is row \(i\) of \(A\); its multidegree is thus \(K^\mathsf{T}(R^\mathsf{T}m+a_i)=e_i\). The rows of \(K\) are exactly the required integer variable weights. The dense chart parametrization supplies points with every Cox coordinate nonzero.

## Proof

**1. Global slice.** Since \(S\) is a domain and every \(F_i\) is nonzero, the principal open \(D=D(F_1\cdots F_r)\) is nonempty, smooth, and integral. Let \(\Phi:D\to G\) be \(\Phi(u)=(F_1(u),\ldots,F_r(u))\). Basis multihomogeneity gives
\[
\Phi(\lambda\cdot u)=\lambda\,\Phi(u).
\]
Consequently the morphisms
\[
\Psi:Y\times G\longrightarrow D,\quad(y,\lambda)\longmapsto\lambda\cdot y,
\]
and
\[
\Theta:D\longrightarrow Y\times G,\quad
u\longmapsto\big(\Phi(\nu)^{-1}\cdot\nu,\Phi(\nu)\big)
\]
are inverse. The inverse is everywhere regular on \(D\): the negative powers of \(F_i\) that occur are units there. The equality \(F_i(\Phi(\nu)^{-1}\cdot\nu)=1\) holds in the coordinate ring, not merely on closed points. Thus the two morphisms are mutually inverse **as schemes**. Equivalently, there is an explicit algebra isomorphism
\[
S[(F_1\cdots F_r)^{-1}]
\simeq (S/J)[\lambda_1^{\pm1},\ldots,\lambda_r^{\pm1}],
\quad u_j\longmapsto \lambda^{w_j}\bar u_j,
\]
whose inverse sends \(\bar u_j\mapsto u_j\prod_iF_i^{-(w_j)_i}\) and \(\lambda_i\mapsto F_i\).

**2. Primeness, smoothness, and codimension.** The left algebra is a domain. On the right, \(S/J\) injects into its Laurent polynomial extension, and hence \(S/J\) is a domain: \(J\) is prime. Since \(D\) is geometrically integral, the same argument after arbitrary algebraic closure extension proves geometric integrality. The product isomorphism gives \(\dim Y=n-r\). For a direct smoothness check define the weighted Euler derivations
\[
E_a=\sum_{j=1}^n(w_j)_a u_j\frac{\partial}{\partial u_j}.
\]
Multihomogeneity yields \(E_a(F_b)=\delta_{ab}F_b\). Therefore the Jacobian matrix of \((F_1-1,\ldots,F_r-1)\) has rank \(r\) at each point of \(Y\), because its product with the matrix of the \(r\) Euler vectors is the identity there. The Jacobian criterion proves \(Y\) smooth of codimension \(r\); its \(r\) defining equations are a regular sequence and define a complete intersection scheme.

**3. Saturation and the toric application.** If \(Y\cap(\mathbb C^*)^n\neq\varnothing\), no coordinate variable \(u_j\) belongs to the prime ideal \(J\). Thus \(J:(u_1\cdots u_n)^\infty=J\). Under the stated toric assumptions, Calvo Cortes–Telen's Proposition 3.8 identifies the scheme on the dense Cox torus by \(F_i-1\); their Corollary 3.10 identifies the chart's prime closure ideal with precisely that saturation. The original Laurent parametrization is defined on the nonempty open where \(f_1\cdots f_r\neq0\); its Cox coordinates are all nonzero, hence \(Y\) has a dense-torus point. The equality of ideals now follows, with no residual embedded components.

## Verification

The proof is uniform in the number of variables and polynomials; no enumeration supplies its infinite step. For a reproducible small-instance cross-check, run `python checker.py` using Python 3 and its standard library. This verifies the unimodular extension matrix and the basis character degrees in the five-coordinate pentagon example of the initiating paper, plus an explicit rational point on \(Y\) and a nontrivial scaling-and-return test. Expected output: `VERIFY_OK: unimodularity, weight basis, multihomogeneity, exact torus slice`. The script checks only that example; the global scheme isomorphism and Jacobian argument constitute the proof.

A boundary check confirms why the **primitive basis** requirement matters: on \(\mathbb A^1\) with \(\deg u=1\), the homogeneous polynomial \(F=u^2\) has nonprimitive degree \(2\), and \(V(F-1)\) is two reduced points, not irreducible. Linear independence of degrees merely over \(\mathbb Q\) does not suffice for the stated conclusion.

## Relationship to prior work

Calvo Cortes–Telen (2026), Assumption 1, Lemma 3.3, Proposition 3.8, and Corollary 3.10 supply the toric construction and saturation formula; Conjecture 3.11 asks whether saturation is unnecessary. The global slice above answers this explicit question under exactly their Assumption 1. Their Example 4.4 reports a saturation calculation that did not terminate, so the noncomputational uniform argument has immediate practical scope.

Cox (1995) establishes the class-group grading and toric quotient framework, but not the unrestricted unsaturated equations of this construction. Arkani-Hamed, Frost, Plamondon, Salvatori, and Thomas (2025/2026), Theorem 5.3, give a related graded factorization **after localizing at all coordinate variables** for their finite-representation-type family; Theorem 9.2 proves primeness in that family by additional boundary arguments. Neither of those statements asserts primeness of the unlocalized equations for arbitrary toric Newton-polytope data. The decisive distinction here is that the basis-weight trivialization works on \(D(F_1\cdots F_r)\) **before inverting any coordinate variables**.

## Limitations

The general lemma presupposes nonzero homogeneous polynomials with degrees forming an *integral basis*, not just independent or nonprimitive characters. The toric corollary presupposes the initiating paper's unimodularity Assumption 1 and a nonempty dense-torus parametrization. No conclusion is made for torsion-containing class groups, nonunimodular extension matrices, or polynomials of dependent weights. The public literature comparison supports an explicit answer to the stated conjecture but cannot exhaust all differently indexed historical statements; independent validation has not been performed.

## References

1. V. Calvo Cortes and S. Telen, *Positive Charts of Toric Varieties*, arXiv:2602.16414, initial public preprint 2026-02-18; Assumption 1, Lemma 3.3, Proposition 3.8, Corollary 3.10, Conjecture 3.11, Example 4.4. https://arxiv.org/abs/2602.16414 .
2. V. Calvo Cortes and S. Telen, *Positive charts of toric varieties*, supplementary code record, Zenodo 18613405, published 2026-02-11. https://zenodo.org/records/18613405 .
3. D. A. Cox, *The homogeneous coordinate ring of a toric variety*, J. Algebraic Geom. **4** (1995), 17–50; arXiv:alg-geom/9210008, Sections 1–2. https://arxiv.org/abs/alg-geom/9210008 .
4. N. Arkani-Hamed, H. Frost, P.-G. Plamondon, G. Salvatori, and H. Thomas, *Configuration Spaces of Finite Representation Type Algebras*, arXiv:2512.24870, Theorems 5.3, 9.2, 9.4. https://arxiv.org/abs/2512.24870 .
