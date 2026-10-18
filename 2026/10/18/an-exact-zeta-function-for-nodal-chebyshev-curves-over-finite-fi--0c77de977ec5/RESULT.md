# An exact zeta function for nodal Chebyshev curves over finite fields

## Finding

Let \(m,n\ge 2\) be coprime integers and \(q\) an odd prime power. Suppose that two signs \(\epsilon_m,\epsilon_n\in\{1,-1\}\) satisfy
\[
q\equiv\epsilon_m\pmod{2m},\qquad q\equiv\epsilon_n\pmod{2n}.
\]
Write \(\delta=(m-1)(n-1)/2\) and \(\eta=\epsilon_m\epsilon_n\). The affine plane curve
\[
C_{m,n}:\quad T_n(x)-T_m(y)=0
\]
is geometrically irreducible with normalization \(\mathbb A^1\), and all its \(\delta\) geometric singularities are rational ordinary nodes. Every node has two rational branches if \(\eta=1\) and two conjugate branches over the quadratic extension if \(\eta=-1\). For **every** extension degree \(r\ge1\),
\[
\#C_{m,n}(\mathbb F_{q^r})=q^r-\delta\eta^r,
\qquad Z(C_{m,n}/\mathbb F_q,t)=\frac{(1-\eta t)^\delta}{1-qt}.
\]
In particular, mixed signs give \(q+\delta\) rational points, while equal signs give \(q-\delta\) rational points.

## Assumptions and scope

Here \(T_0(z)=1\), \(T_1(z)=z\), and \(T_{j+1}(z)=2zT_j(z)-T_{j-1}(z)\). They have integer coefficients and are reduced to the base field. The congruences imply that its odd characteristic \(p\) does not divide \(mn\). The theorem is about the **affine, potentially singular** plane curve, not its projective closure, a smoothing, or its normalization. The zeta function is defined by
\[
Z(C/\mathbb F_q,t)=\exp\!\left(\sum_{r\ge1}\#C(\mathbb F_{q^r})t^r/r\right).
\]
No condition \(m<n\) or primality of \(q\) is imposed.

## Proof

**1. Normalization.** Set \(K=\overline{\mathbb F}_q\). The identity \(T_n\circ T_m=T_m\circ T_n\) gives a map \(\nu:\mathbb A^1_K\to C_{m,n,K}\), \(u\mapsto(T_m(u),T_n(u))\). The subfield \(K(T_m(u),T_n(u))\subset K(u)\) has index dividing \(m\) and \(n\), because the degrees of the extensions induced by \(T_m\) and \(T_n\) are respectively \(m\) and \(n\). Coprimality forces index one. Since \(T_m(u)\) has leading coefficient \(2^{m-1}\ne0\), \(u\) is integral over \(K[T_m(u),T_n(u)]\): the monic equation is \((T_m(U)-T_m(u))/2^{m-1}=0\). The morphism is thus finite and birational; its source is normal. To check its image equals the displayed curve rather than a component, note that the minimal polynomial of \(T_n(u)\) over \(K(T_m(u))\) has degree \(m\), equal to the degree in \(y\) of \(T_n(x)-T_m(y)\). The displayed polynomial is irreducible, so \(\nu\) is its normalization.

**2. Singularities over an algebraic closure.** Fix primitive \(2n\)-th and \(2m\)-th roots of unity \(\zeta_n,\zeta_m\in K\), respectively. From \(T_d((z+z^{-1})/2)=(z^d+z^{-d})/2\), the \(d-1\) distinct critical points of \(T_d\) are
\[
 a_{d,k}=(\zeta_d^k+\zeta_d^{-k})/2,\quad1\le k\le d-1,
\]
and \(T_d(a_{d,k})=(-1)^k\). Distinctness follows since \(p\nmid 2d\), and the critical roots exhaust the roots of \(T_d'\). Consequently, the singularities of \(T_n(x)-T_m(y)=0\) are precisely \((a_{n,k},a_{m,\ell})\) with \(1\le k<n\), \(1\le\ell<m\), and \(k\equiv\ell\pmod2\). Their number is \(\delta\) (for coprime \(m,n\), at least one is odd). At a critical point the Chebyshev differential identity
\[
(1-z^2)T_d''(z)-zT_d'(z)+d^2T_d(z)=0
\]
yields \(T_d''(a_{d,k})=-d^2(-1)^k/(1-a_{d,k}^2)\ne0\), since \(p\nmid d\) and \(a_{d,k}\ne\pm1\). Thus the local quadratic part is a nondegenerate binary quadratic form with two distinct tangents. Every singularity is an ordinary node, and there are no others.

**3. Rationality and branch splitting.** By the two congruences, Frobenius sends \(\zeta_d\mapsto\zeta_d^{\epsilon_d}\) for \(d\in\{m,n\}\). It therefore fixes every \(a_{d,k}\), so every node is defined over \(\mathbb F_q\). Define the nonzero elements
\[
 b_{d,k}=\zeta_d^k-\zeta_d^{-k},\qquad
 1-a_{d,k}^2=-b_{d,k}^2/4.
\]
One has \(b_{d,k}^q=\epsilon_db_{d,k}\). At a node with equal parity, the tangent-cone equation in translated local coordinates \(X,Y\) is
\[
T_n''(a_{n,k})X^2-T_m''(a_{m,\ell})Y^2=0.
\]
Its two slopes \(Y/X\) are
\[
\pm\frac{n}{m}\frac{b_{m,\ell}}{b_{n,k}}
\]
(the parity signs cancel). Frobenius multiplies either chosen slope by \(\eta=\epsilon_m\epsilon_n\). Hence all tangents/normalization branches are individually rational exactly when \(\eta=1\), and otherwise are exchanged by Frobenius. This is uniform across all nodes, not a count inferred from isolated examples.

**4. Point counts and zeta.** Over any \(\mathbb F_{q^r}\), the finite normalization \(\mathbb A^1\to C\) is bijective away from the nodes. At a node, the normalization contributes two rational points if \(\eta^r=1\) and zero if \(\eta^r=-1\), whereas the node itself contributes one rational point in either case. Thus each node changes the count of \(\mathbb A^1(\mathbb F_{q^r})\) by \(-\eta^r\). This proves \(q^r-\delta\eta^r\); exponentiating the generating series gives the claimed zeta function. All arguments hold over any odd finite field satisfying the residue conditions.

## Verification

The accompanying standalone `verify.py` enumerates affine points using the defining recurrence, with exact modular arithmetic only. It passed 84 prime-field checks across eight coprime degree pairs and eight quadratic-field checks, including \(\#C_{2,3}(\mathbb F_5)=6\) and \(\#C_{2,3}(\mathbb F_{25})=24\). Execute `python3 verify.py`. These finite tests corroborate but do not replace the all-field proof. The proof independently checks separability, geometric nodes, Frobenius action on tangents, and the local correction from normalization.

## Relationship to prior work

Freudenburg–Freudenburg [1, Proposition 3.1] determine the same characteristic-zero Chebyshev plane curve's normalization and its \(\delta\) ordinary geometric nodes, including their locations; these results are explicitly acknowledged and **not claimed as new**. The present arithmetic result determines which nodes and branches are rational in odd finite characteristic for two simultaneous signed congruences, and consequently the entire Hasse–Weil zeta factor; this is not a statement of [1], which works in characteristic zero. Garcia–Stichtenoth [2] study maximal *smooth Kummer-type curves* described through Chebyshev polynomials; their genus and separability formulas do not give the affine nodal curve's arithmetic branch-identification factor. Kazemifard–Tafazolian–Torres [3, Theorems 9, 13] continue those Kummer-cover maximality results for models \(v^N=\varphi_M(u)\) and shifted models, not \(T_n(x)=T_m(y)\) with coprime two Chebyshev degrees. The 2014 finite-field polynomial study [4] has accessible abstract coverage of trigonometric definitions, symmetries and permutation properties; its full chapter was not available for an exhaustive negative comparison.

## Limitations

No formula is asserted when the signed simultaneous congruences fail, nor when \(m,n\) are not coprime or the characteristic is even. The normalization is affine; point counts of a particular projective closure require accounting for its points at infinity. The result is supported by a self-review, not an independent audit. Residual literature risk remains from the uninspected full text of [4] and from potentially unindexed arithmetic treatments of the same nodal plane curves; these limitations do not affect the proved point-count identity.

## References

[1] Gene Freudenburg and Jenna Freudenburg, *Curves Defined by Chebyshev Polynomials*, arXiv:0902.3440v1, first posted 2009-02-19, Section 3, Proposition 3.1. https://arxiv.org/pdf/0902.3440

[2] Arnaldo Garcia and Henning Stichtenoth, *On Chebyshev polynomials and maximal curves*, Acta Arithmetica 90 (1999), 301–311, DOI:10.4064/aa-90-4-301-311. https://www.researchgate.net/publication/291916695_On_Chebyshev_polynomials_and_maximal_curves

[3] Ahmad Kazemifard, Saeed Tafazolian and Fernando Torres, *On maximal curves related to Chebyshev polynomials*, 2017 report (later Finite Fields Appl. 52 (2018), 200–213), especially §§2–4. https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2017-15.pdf

[4] Juliano B. Lima, Daniel Panario and Ricardo Campello de Souza, *A trigonometric approach for Chebyshev polynomials over finite fields*, chapter in *Applied Algebra and Number Theory* (2014). https://www.cambridge.org/core/books/applied-algebra-and-number-theory/trigonometric-approach-for-chebyshev-polynomials-over-finite-fields/40E46D1021021EC7BB6BABD4CB17CF03
