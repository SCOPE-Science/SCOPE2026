# The residual-contact graph of canonical hyperosculating planes on the characteristic-three Artin–Mumford curve

## Finding
Let \(M\) be the smooth projective completion over \(\mathbb F_3\) of
\[
(x^3-x)(y^3-y)=1.
\]
Its canonical embedding has affine coordinates \([1:x:y:xy]\). Put \(A=x(P)^3-x(P)\) at an affine point \(P\). There are exactly 36 affine canonical hyperosculation points, characterized by \(A^4=1\). At every such point there is a unique hyperosculating hyperplane \(H_P\), and the complete intersection divisor is as follows.

**Double-residual regime.** If \(A^2=1\), write \(Q=P-(A,A)\) in the affine coordinates. Then
\[
H_P\cdot M=4P+2Q.
\]
The correspondence \(P\mapsto Q\) partitions these 18 points into exactly six directed 3-cycles.

**Simple-residual regime.** If \(A^2=-1\), put
\[
Q_{\epsilon}=(x(P)+A+\epsilon,\ y(P)-A+\epsilon),\qquad \epsilon\in\{1,-1\}.
\]
Then \(Q_{+}\ne Q_{-}\), both belong to the hyperosculation locus, and
\[
H_P\cdot M=4P+Q_{+}+Q_{-}.
\]
The symmetric residual-incidence graph is a disjoint union of three undirected 6-cycles on these other 18 points.

For completeness, the canonical Hasse–Wronskian divisor is \(\mathcal R_K=A_{36}+4B_6\), where \(A_{36}\) is the reduced affine locus just described and \(B_6\) is the sum of the six rational points at infinity. Frobenius acts on its 42-point reduced support with cycle type \(1^6 2^9 3^6\), so its reduced-support zeta function is
\[
Z(\operatorname{Supp}(\mathcal R_K)_{\mathrm{red}},T)=\frac{1}{(1-T)^6(1-T^2)^9(1-T^3)^6}.
\]
The residual-contact graph is an additional incidence invariant, not simply the Frobenius count or the published local canonical-order sequence.

## Assumptions and scope
Work over the algebraic closure \(k\) of \(\mathbb F_3\) for geometric statements; finite-field statements refer to the displayed prime-field model. Compactify the affine curve in \(\mathbb P^1\times\mathbb P^1\) as the smooth bidegree-\((3,3)\) curve. Smoothness follows because at finite points both partial derivatives equal nonzero scalar multiples of \(x^3-x\) and \(y^3-y\), and at either infinity divisor one obtains three separate simple branches. Geometric irreducibility follows from the Artin–Schreier extension \(y^3-y=(x^3-x)^{-1}\), since the right side has simple poles. Adjunction yields \(K_M=\mathcal O_M(1,1)\), \(g=4\), and the canonical Segre model \([1:x:y:xy]\). The hyperosculating plane is the unique hyperplane with intersection multiplicity at least four at the given affine point. Section multiplicities are scheme-theoretic intersection multiplicities. The graph vertices are distinct geometric points, without quotienting by curve automorphisms.

## Proof
Write \(U=x^3-x\), \(V=y^3-y=U^{-1}\), and take the local parameter \(s=x-x(P)\). Since \(U(x(P)+s)=A+s^3-s\), the Hasse derivatives \(a_j=D^{(j)}y\) are recovered from
\[
y(x(P)+s)^3-y(x(P)+s)=\frac{1}{A+s^3-s}.
\]
Comparison of coefficients through order three gives
\[
a_1=-A^{-2},\qquad a_2=-A^{-3},\qquad a_3=-A^{-6}-A^{-4}+A^{-2}.
\]
For the basis \(1,x,y,xy\), the canonical Hasse–Wronskian is \(a_2^2-a_1a_3\), hence
\[
\mathcal W=\frac{A^4-1}{A^8}.
\]
It is not identically zero; the generic canonical order sequence is \((0,1,2,3)\). Its affine zeros satisfy \(A^4=1\). Each of the four possible nonzero \(A\) has exactly three roots of \(x^3-x=A\) and three roots of \(y^3-y=A^{-1}\), giving 36 simple points. Simplicity follows from \(dU/dx=-1\) and the nonvanishing derivative of \(A^4-1\).

At an affine such \(P\), switch to \(s=x-x(P)\), \(z=y-y(P)\). The unique plane killing the jets of orders zero through three is
\[
H_P:\quad z+A^{-2}s-A^{-1}sz=0.
\]
Indeed the coefficients of the jets of \(1,s,z,sz\) determine that plane, since \(a_2/a_1=A^{-1}\) and the order-three vanishing is equivalent to \(a_2^2=a_1a_3\). Put \(d=1-A^{-1}s=1-A^3s\) and \(n=-A^{-2}s=-A^2s\), so that the plane is \(z=n/d\). Clearing denominators in the curve equation gives the exact identity (with \(A^4=1\))
\[
\begin{split}
&(A+s^3-s)\bigl(A^{-1}d^3+n^3-nd^2\bigr)-d^3\\
&\qquad=-A\,s^4(As^2-s+A).
\end{split}
\]
Thus the contact at \(P\) is exactly four and the remaining two intersection parameters are the zeros of \(As^2-s+A\). The point \(d=0\) is not a zero of the displayed polynomial, so clearing denominators introduces no spurious intersection. The degree-six intersection is exhausted by the finite roots, with no intersection on the compactification boundary (alternatively, the total degree is \(\deg K_M=6\)).

If \(A^2=1\), the quadratic is \(A(s+A)^2\) in characteristic three; its double root is \(s=-A\), giving \(z=-A\) and \(Q=P-(A,A)\). Because translations by elements of \(\mathbb F_3\) preserve \(x^3-x\) and \(y^3-y\), this map cycles with exact order three on the nine points for each \(A\in\{1,-1\}\). Hence there are six directed 3-cycles.

If \(A^2=-1\), the roots are \(s=A+\epsilon\) for \(\epsilon\in\{1,-1\}\), yielding \(z=-A+\epsilon\). Consequently the two residual points are exactly \(Q_{\epsilon}\) displayed above, and each has \(U(Q_{\epsilon})=-A\). The correspondence is symmetric: from \(Q_{\epsilon}\), the opposite-sign residual shift returns to \(P\). Every vertex has degree two. A two-step path sends \(P\) to \(P+(\epsilon+\eta,\epsilon+\eta)\), where \(\epsilon,\eta\in\{1,-1\}\); the nontrivial two-step translation has order three. Therefore each connected component is a 6-cycle. The 18 vertices form three such components.

At the three points over \(x=\infty\), use \(t=1/x\), \(y=a+v\), with \(a\in\mathbb F_3\). The curve becomes \(v^3-v=t^3/(1-t^2)\), and therefore \(v=-t^3-t^5+O(t^7)\). In a canonical trivialization a basis is \(1,t,v,tv\), whose Hasse–Wronskian has initial term \(t^4\). The three points over \(y=\infty\) are identical by symmetry. Each of the six boundary points has multiplicity four. Hence \(\deg\mathcal R_K=36+6\cdot4=60\), matching the genus-four canonical Plücker degree \(g(g^2-1)=60\).

For the Frobenius claim, \(A^2=-1\) has two roots in \(\mathbb F_9\), both with trace zero to \(\mathbb F_3\). Thus all 18 corresponding affine points lie in \(\mathbb F_9\) and split into nine Frobenius 2-cycles. For \(A\in\{1,-1\}\), both additive equations have first roots in \(\mathbb F_{27}\), with Frobenius acting by nontrivial translation, yielding six 3-cycles. All six points at infinity are \(\mathbb F_3\)-rational. The zeta function is the product of the orbit factors.

## Verification
Run `python3 verify.py` with Python 3 and its standard library. It independently recomputes the rational-function Hasse-jet Wronskian over characteristic three, the fourth-order boundary multiplicity, the residual intersection polynomial on every fourth root of unity over \(\mathbb F_9\), and the two finite incidence graphs. Its exact field arithmetic recovers six 3-cycles and three 6-cycles and finite-field support counts. The proof above does not depend on treating finite enumeration as an infinite completeness argument.

## Relationship to prior work
Arakelian–Korchmáros (2015) provides the Artin–Mumford curve and its genus and prime-field automorphism arithmetic, but not the canonical residual-contact incidence graph. Korchmáros–Montanucci (submitted 2016-12-18, later than the archival source cutoff but relevant to originality) establishes the degree-six space model and local osculating order sequences for the more general Artin–Schreier–Mumford family; those results strongly overlap with the **location** of higher contacts, but do not state the exact residual scheme \(H_P\cdot M-4P\) or classify its directed/undirected incidence cycles. The contribution here is this additional complete residual-contact classification, with the full Wronskian and Frobenius formulas as explicitly identified consequences. General local order sequences alone do not fix the residual quadratic divisor. This comparison does not establish exhaustive historical uniqueness.

## Limitations
The theorem is for the displayed characteristic-three model, not arbitrary twisted forms, coefficients, or all characteristics. The residual hyperplanes and graph concern the 36 affine order-four contact points, not the six boundary points with different canonical orders. Originality comparison is limited to accessible published primary sources and mathematical-record searches; unindexed, unpublished, or otherwise inaccessible prior calculations could overlap. No independent mathematical audit is claimed.

## References
1. N. Arakelian and G. Korchmáros, *A characterization of the Artin-Mumford curve*, arXiv:1501.02616 (first public 2015-01-12). https://arxiv.org/abs/1501.02616
2. G. Korchmáros and M. Montanucci, *The Geometry of the Artin-Schreier-Mumford Curves over an Algebraically Closed Field*, arXiv:1612.05912 (first public 2016-12-18; supporting comparison, not archival anchor). https://arxiv.org/abs/1612.05912
3. G. van der Geer and M. van der Vlugt, *Kloosterman sums and the p-torsion of certain Jacobians* (1991), background on related Artin–Schreier quotient curves.
