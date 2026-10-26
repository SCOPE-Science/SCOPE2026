# The first reducibility transition for commuting pairs in exterior algebras

## Finding

Let \(k\) be an algebraically closed field of characteristic different from \(2\), let \(V\) be a vector space of dimension \(n\), and write \(E_n=\bigwedge_k V\). Give the **reduced** commuting-pair variety its induced Zariski topology:
\[
\mathcal C_n=\{(a,b)\in E_n\times E_n:ab=ba\}_{\mathrm{red}}.
\]
The variety \(\mathcal C_n\) is geometrically irreducible for \(1\le n\le5\). At \(n=6\) it has **exactly two geometrically irreducible components**, of respective dimensions \(112\) and \(115\). Consequently the six-generator commuting variety is not equidimensional. Both components are rational.

More explicitly, write the odd portions of \(a,b\in E_6\) as \(a_1+a_3+a_5\) and \(b_1+b_3+b_5\), with subscripts denoting exterior degree. One component is the closure of the locus \(a_1\ne0\), with dimension \(112\). The other is the closed locus \(a_1=b_1=0\) and \(a_3\wedge b_3=0\), of dimension \(115\). Even portions are unrestricted.

For every odd prime power \(q\), the same stratification yields the exact ordered-pair counts
\[
|\mathcal C_5(\mathbb F_q)|=q^{56}+q^{55}+q^{54}-q^{51}-q^{50},
\]
\[
|\mathcal C_6(\mathbb F_q)|=q^{115}+q^{112}+q^{111}-q^{106}-q^{105}+q^{96}-q^{95}.
\]
The five-generator counting identity is included for comparison with earlier inner-derivation rank data; the new geometric transition and six-generator classification are the substantive conclusions.

## Assumptions and scope

The field is algebraically closed of characteristic \(\ne2\) for the geometric assertions, or a finite field \(\mathbb F_q\) of odd order for point counts. There is no requirement that the characteristic exceed the number of generators. \(E_n\) is the **unital associative exterior algebra**, not a Clifford deformation or its graded-commutator Lie superalgebra. The commutator is the ordinary associative one. Irreducibility concerns the reduced variety; no claim about reducedness or normality of the defining commuting scheme is made. Ordered pairs, not pairs up to conjugation, are counted.

For \(n\ge1\), \(E_n\) has even and odd vector-space parts \(E_n^{\mathrm{ev}}\) and \(E_n^{\mathrm{odd}}\), each of dimension \(2^{n-1}\). In odd characteristic, the ordinary commutator of arbitrary elements is twice the exterior product of their odd parts. Therefore
\[
\mathcal C_n\cong\mathbb A^{2^n}\times X_n,\qquad
X_n=\{(u,v)\in(E_n^{\mathrm{odd}})^2:u\wedge v=0\}_{\mathrm{red}}.
\]
Every geometric statement below reduces to \(X_n\).

## Proof

**1. Explicit equations.** For \(n=5,6\), write \(u=u_1+u_3+u_5\), \(v=v_1+v_3+v_5\). The product \(u\wedge v\) is zero if and only if
\[
u_1\wedge v_1=0,\qquad
u_1\wedge v_3+u_3\wedge v_1=0,
\]
and, only when \(n=6\), also
\[
u_1\wedge v_5+u_3\wedge v_3+u_5\wedge v_1=0.
\]
For \(n\le4\), terms in nonexistent exterior degrees are omitted. Because \(\operatorname{char}k\ne2\), every odd element \(v\) satisfies \(v\wedge v=0\), so the deformation \((u,v)\mapsto(u+t v,v)\) preserves these equations.

**2. The main open stratum.** Let \(U_n\subseteq X_n\) be the locus \(u_1\ne0\). The first equation forces \(v_1=c u_1\) for a unique scalar \(c\). For \(n=5\), the second equation says \(v_3=c u_3+w_3\) where \(w_3\in\ker(u_1\wedge-:\bigwedge^3V\to\bigwedge^4V)\). By splitting \(V=ku_1\oplus W\), this kernel is \(u_1\wedge\bigwedge^2W\), of dimension \(\binom42=6\). Thus \(U_5\) is an affine-bundle tower over \(V\setminus\{0\}\) with free parameters \(c,u_3,w_3,u_5,v_5\) of respective dimensions \(1,10,6,1,1\). It is irreducible, rational and has dimension \(5+1+10+6+1+1=24\).

For \(n=6\), the same kernel has dimension \(\binom52=10\). The final equation is a **single independent linear equation** on \(v_5\), since \(u_1\wedge-:\bigwedge^5V\to\bigwedge^6V\) is surjective. Hence \(v_5\) varies in an affine fiber of dimension \(5\). The free parameter dimensions are now \(6,1,20,10,6,5\), totaling \(48\). Accordingly \(U_6\) is irreducible and rational of dimension \(48\). Its closure \(Y_6\) is irreducible of dimension \(48\).

**3. Closure for one nonzero linear part.** If \(u_1=0\), \(v_1\ne0\) and \(u\wedge v=0\), the polynomial arc \((u+t v,v)\) lies in \(U_n\) for \(t\ne0\) and specializes to \((u,v)\) at \(t=0\). Thus every such point belongs to \(\overline{U_n}\), for every \(n\) in scope.

**4. Irreducibility through five generators.** Suppose \(n\le5\) and \(u_1=v_1=0\). The pair commutes automatically, as products of its odd degree-at-least-three portions have degree at least six. Choose a nonzero \(w\in V\) with \(w\wedge v_3=0\). This is always possible: for \(n\le4\), the map \(V\to\bigwedge^4V\) has rank less than \(n\); for \(n=5\), the wedge map \(w\mapsto w\wedge v_3\) identifies via a volume form with a skew-symmetric \(5\times5\) matrix, necessarily singular. Thus \((u+t w,v)\) remains commuting and belongs to \(U_n\) for \(t\ne0\). By Step 3, every point of \(X_n\) lies in \(\overline{U_n}\). The same affine-bundle reasoning as Step 2 gives irreducibility of \(U_n\) for all \(1\le n\le4\); \(n=1\) is also immediate because \(E_1\) is commutative. Therefore \(X_n\) and \(\mathcal C_n\) are irreducible for all \(1\le n\le5\). For \(n=5\), \(\dim\mathcal C_5=2^5+24=56\).

**5. The second six-generator component.** The complementary closed linear-degree-zero locus is
\[
Z_6=\{(u,v)\in X_6:u_1=v_1=0\}.
\]
Here the only remaining equation is \(u_3\wedge v_3=0\). Exterior multiplication induces a perfect alternating pairing \(\bigwedge^3V\times\bigwedge^3V\to\bigwedge^6V\), with \(\dim\bigwedge^3V=20\). After choosing symplectic coordinates the equation is \(\sum_{i=1}^{10}(x_i y'_i-x'_i y_i)=0\). It is an irreducible quadratic polynomial over every algebraically closed field of odd characteristic, since its associated symmetric polar form has rank \(40\), whereas a product of two linear forms has polar rank at most \(2\). Its zero set in \(\mathbb A^{40}\) is irreducible of dimension \(39\). Since \(u_5,v_5\) contribute \(12\) independent coordinates, \(Z_6\) is irreducible and rational of dimension \(39+12=51\). Rationality follows, for example, by solving the equation for one \(y'_i\) on an open chart where \(x_i\ne0\).

Every point of \(X_6\setminus Z_6\) lies in \(\overline{U_6}\) by Step 3, so \(X_6=Y_6\cup Z_6\). The irreducible subsets \(Y_6\) and \(Z_6\) are distinct: \(Y_6\) contains \(u_1\ne0\), whereas \(Z_6\) does not, and \(\dim Z_6=51>48=\dim Y_6\), so \(Z_6\not\subseteq Y_6\). Hence they are exactly the two irreducible components. The even-coordinate factor \(\mathbb A^{2^6}=\mathbb A^{64}\) gives dimensions \(48+64=112\) and \(51+64=115\).

**6. Finite-field counts.** All preceding rank and fiber statements are valid over any odd finite field. For \(n=5\), split \(X_5(\mathbb F_q)\) into disjoint strata by \(u_1\ne0\), \(u_1=0,v_1\ne0\), and \(u_1=v_1=0\); their cardinalities are respectively \((q^5-1)q^{19}\), \((q^5-1)q^{18}\), and \(q^{22}\). Multiply the sum by \(q^{32}\) for the two even portions.

For \(n=6\), the analogous three strata have cardinalities \((q^6-1)q^{42}\), \((q^6-1)q^{41}\), and
\[
q^{12}\bigl(q^{20}+(q^{20}-1)q^{19}\bigr)
=q^{51}+q^{32}-q^{31}.
\]
For the last expression, fix \(u_3\). If \(u_3=0\), there are \(q^{20}\) possible \(v_3\); if \(u_3\ne0\), the perfect exterior pairing gives exactly \(q^{19}\) choices. The \(u_5,v_5\) coordinates contribute \(q^{12}\). Multiplying the sum by \(q^{64}\) proves the displayed six-generator polynomial. These are exact finite-field counts, not asymptotic approximations.

## Verification

The standalone script `verify.py` uses the exterior monomial basis, literal signs in wedge multiplication, and finite-field row elimination; it requires only Python 3. Run `python3 verify.py`. It checks multiplication-map ranks for the two relevant generator numbers across fields of prime orders \(3,5,7\), the perfect alternating \(20\times20\) middle-degree pairing in six generators, singularity of the five-generator \(V\to\bigwedge^4V\) map, and independent stratum-count identities. The expected marker is `VERIFY_OK_EXTERIOR_COMMUTING_COMPONENT_TRANSITION`. These tests do not by themselves establish irreducibility; the polynomial-arc and quadric arguments above do so over arbitrary algebraically closed fields of characteristic different from two.

## Relationship to prior work

Domokos and Zubor, *Commutative subalgebras of the Grassmann algebra* (first posted 12 March 2014, arXiv:1403.2916), establish the correspondence between commutative subalgebras and square-zero subspaces of the odd part, and identify the perfect top-degree alternating pairing in even generator number (Sections 2 and 7). Their results concern maximal commutative subalgebras and do not state the decomposition, dimensions, or finite-field count of the variety of **individual ordered commuting pairs**. This work uses the same classical exterior pairing but studies its full pairwise vanishing locus, which is not fixed by maximal-subspace dimensions.

Bovdi and Leung, *Maximal commutative subalgebras of a Grassmann algebra* (arXiv:1803.03457, 2018), construct maximal commutative subalgebras via intersecting systems. Their Sections 1–2 address subalgebra families, not the rank-6 commuting-pair variety or its component dimensions. Earlier work on inner-derivation ranks for five generators already determines the **five-generator point-count polynomial**; that polynomial is supplied here as a consistency check, not claimed to be new. The six-generator decomposition and its non-equidimensionality do not follow from the five-generator rank profile.

## Limitations

The theorem treats the **reduced** algebraic set of ordered pairs only. It does not prove that the commuting-pair scheme defined by commutator-coordinate equations is reduced, normal, Cohen–Macaulay, or a complete intersection. It makes no classification for \(n\ge7\), no higher-tuple claims, and no statements for characteristic two, where the exterior algebra is commutative. The finite-field verification is illustrative and does not replace the geometric proof. Historical novelty still carries a risk of equivalent earlier formulations under exterior-product incidence or commuting-variety terminology.

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916 (first public version 12 March 2014), https://arxiv.org/abs/1403.2916.
2. V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457 (first public version 9 March 2018), https://arxiv.org/abs/1803.03457.
