# Complete power-map fibers in radical-square-zero quiver unit groups

## Finding

Let \(Q\) be any finite quiver, with loops and repeated arrows permitted, having \(n\geq1\) vertices and \(m\geq0\) arrows. Let \(A=\mathbb F_qQ/J^2\), where \(q=p^f\) is any prime power, and put \(G=A^\times\). For every positive integer \(k\) and every \(b\in G\), the number of prescribed roots \(N_k(b)=|\{g\in G:g^k=b\}|\) is determined exactly as follows.

Represent \(b\) by nonzero diagonal coordinates \(u_v\in\mathbb F_q^\times\) and arrow coordinates \(y_e\in\mathbb F_q\). Let \(h=\gcd(k,q-1)\) and \(r=(q-1)/h\). If one \(u_v\) is not a \(k\)-th power in \(\mathbb F_q^\times\), then \(N_k(b)=0\).

If \(p\mid k\), let \(m_{=}(u)=|\{e:u_{s(e)}=u_{t(e)}\}|\), counting loops and repeated arrows. Then
\[
N_k(b)=\begin{cases}
h^n q^{m_{=}(u)}, & y_e=0\ \text{for every arrow with}\ u_{s(e)}=u_{t(e)},\\
0,&\text{otherwise}.
\end{cases}
\]

If \(p\nmid k\), for every distinct diagonal value \(\alpha\) of \(b\), put \(V_\alpha=\{v:u_v=\alpha\}\). Partition arrows internal to \(V_\alpha\) into \(E_\alpha^+=\{e:y_e\neq0\}\) and \(E_\alpha^0=\{e:y_e=0\}\). Then the complete prescribed-root formula is
\[
N_k(b)=\prod_\alpha\ \sum_{\substack{c:V_\alpha\longrightarrow\{1,\ldots,h\}\\
c(s(e))=c(t(e))\ \forall e\in E_\alpha^+}}
q^{|\{e\in E_\alpha^0:c(s(e))\neq c(t(e))\}|}.
\]
A factor for an empty arrow set has its literal coloring-count meaning. Loops impose no nontrivial constraints and contribute zero to the exponent. Arrows joining different diagonal values impose no restrictions.

Define the graph partition function, retaining parallel edges but ignoring loops,
\[
Z_Q(t,q)=\sum_{c:Q_0\to\{1,\ldots,t\}}q^{|\{e\in Q_1:c(s(e))\neq c(t(e))\}|},\quad t\geq1.
\]
The size of the image of the \(k\)-th power map and the number of elements whose \(k\)-th power is the identity are
\[
\boxed{\begin{array}{c|cc}
&|\operatorname{im}(g\mapsto g^k)|&N_k(1)\\\hline
p\nmid k&q^m r^n&Z_Q(h,q)\\
p\mid k&Z_Q(r,q)&h^n q^m
\end{array}}.
\]
These formulas hold with no restriction on the finite quiver, finite-field characteristic, or positive exponent. In particular, if \(o_d\) denotes the number of elements of order exactly \(d\), then
\[
o_d=\sum_{a\mid d}\mu(d/a)N_a(1).
\]
The group exponent is \(q-1\) when \(m=0\) and \(p(q-1)\) when \(m>0\).

Writing \(E_{\ne}\) for the multiset of nonloop arrows, and \(c(S)\) for the number of connected components of the undirected spanning multigraph determined by \(S\subseteq E_{\ne}\), the partition function also has the exact finite subset expansion
\[
\boxed{Z_Q(t,q)=\sum_{S\subseteq E_{\ne}}t^{c(S)}q^{|E_{\ne}|-|S|}(1-q)^{|S|}.}
\]
For an underlying nonloop forest with \(c\) components, this becomes \(Z_Q(t,q)=t^c(1+(t-1)q)^{n-c}\); for a simple undirected cycle on \(\ell\geq3\) vertices, it becomes \(Z_Q(t,q)=(1+(t-1)q)^\ell+(t-1)(1-q)^\ell\).

## Assumptions and scope

The path-algebra convention multiplies vertex idempotents and arrows by their respective tail/head idempotents; reversing the composition convention only exchanges the two endpoint labels in symmetric formulas. The quotient \(J^2\) kills every path of length at least two. Hence every element of \(G\) is uniquely \(g=(d_v,x_e)\) with \(d_v\neq0\). Products satisfy \((d,x)(e,y)_v=d_ve_v\) and \((d,x)(e,y)_a=d_{s(a)}y_a+x_ae_{t(a)}\). No acyclicity, admissibility beyond the explicit quotient, absence of loops, or restriction on parallel-arrow multiplicity is assumed. The formula for \(o_d\) applies to all positive \(d\), and is zero when \(d\) is not an element order.

## Proof

**Power coefficient.** Since products of two arrows vanish, for each arrow \(e\) the coefficient of \(g^k\) is
\[
x_e\,C_k(d_{s(e)},d_{t(e)}),\qquad C_k(a,b)=\sum_{j=0}^{k-1}a^{k-1-j}b^j.
\]
The diagonal coefficient is \(d_v^k\). If \(a\neq b\), telescoping gives \((a-b)C_k(a,b)=a^k-b^k\). If \(a=b\), then \(C_k(a,a)=k a^{k-1}\). Each nonzero \(u_v\) that is a \(k\)-th power has precisely \(h\) distinct roots, since \(\mathbb F_q^\times\) is cyclic.

**Characteristic dividing the exponent.** Suppose \(p\mid k\). On any arrow with equal diagonal targets \(u_{s(e)}=u_{t(e)}\), either the chosen roots coincide and the coefficient is zero by the characteristic assumption, or the roots differ and the telescoping identity gives zero. Thus the arrow coefficient of every power must vanish. On any arrow joining distinct target values, the coefficient is nonzero for every diagonal-root assignment, and the specified arrow target uniquely determines the input arrow coordinate. When it vanishes, the coefficient allows \(q\) choices. All choices are independent because \(J^2=0\), giving the displayed \(h^nq^{m_{=}(u)}\) formula and the vanishing condition.

**Characteristic prime to the exponent.** Suppose \(p\nmid k\). If the diagonal targets differ, the coefficient is always nonzero. For equal target values, it is nonzero if and only if the chosen roots are equal: coincident roots give \(ka^{k-1}\neq0\), whereas distinct roots give zero by telescoping. Consequently a nonzero prescribed arrow target forces its endpoint roots to coincide; a zero prescribed arrow target with distinct endpoint roots gives \(q\) choices of input coordinate; all other arrow situations give exactly one choice. Label the \(h\) roots independently for each value \(\alpha\) to obtain the stated product of weighted constrained colorings. This proves all prescribed fibers.

**Power images and identity fibers.** In the prime-to-characteristic case, every diagonal tuple of \(k\)-th powers has a preimage for every arrow tuple: choose one root for each distinct target diagonal value and use it at all vertices with that value, ensuring every arrow coefficient is nonzero. There are \(r^n\) available diagonal targets and \(q^m\) arrow targets. For the identity, all diagonal values are one, and the weighted-coloring formula is precisely \(Z_Q(h,q)\). In the divisible-characteristic case, each diagonal target is one of \(r\) values, and every arrow between *distinct* values admits all \(q\) possible target coordinates, while an arrow between equal values is forced to zero. Summing over target diagonal colorings yields \(Z_Q(r,q)\). For the identity, all target diagonals are equal and all prescribed arrow coordinates vanish, giving \(h^nq^m\).

**Exact orders, exponent, and subset expansion.** If \(N_k(1)\) counts elements whose order divides \(k\), then \(N_k(1)=\sum_{d\mid k}o_d\); ordinary Möbius inversion gives the claim. Both the diagonal torus and the normal additive arrow subgroup have exponents \(q-1\) and \(p\) (the latter when \(m>0\)). Each element has its \((q-1)\)-th power in the arrow subgroup, so the entire group has exponent dividing \(p(q-1)\), and the two subgroup exponents force equality. Finally, for each nonloop arrow,
\[
q^{\mathbf1_{c(s)\neq c(t)}}=q+(1-q)\mathbf1_{c(s)=c(t)}.
\]
Expanding the product over arrows and counting colorings constant along each selected edge yields the Fortuin--Kasteleyn-type subset formula. For a forest, independent component-root colors and edge transitions give the stated product. For a cycle, diagonalize the \(t\)-color edge-weight matrix: its eigenvalues are \(1+(t-1)q\) once and \(1-q\) with multiplicity \(t-1\), giving the cycle formula. All these arguments are finite exact identities.

## Verification

The standalone Python program `verify_power_fibers.py` independently multiplies pairs of units and forms each complete power-map fiber by exhaustive enumeration; its predictor separately implements the displayed coloring rules. It checks every target for \(14\) small quivers, including loops, repeated arrows, paths, and oriented cycles, over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), for the nine exponents \(1,2,3,4,5,6,8,9,10\). All \(126\) complete-target cases passed. It separately checks image sizes, identity fibers and the subset expansion. The input groups in its cases have an aggregate of \(5298\) elements per exponent. Independently useful evaluations are \(Z_{C_3}(2,5)=152\) and \(Z_{C_3}(4,5)=3904\). The verifier needs only Python 3 and does not prove infinitely many cases: the preceding algebraic proof establishes the general theorem.

## Relationship to prior work

Słowik's 2012 work on involutions in triangular groups describes order-two triangular matrices and counts their total number over finite fields. Gargate and Gargate (2020), especially Theorems 1.1--1.2 and Section 5, describe and count total potent-element solutions in triangular matrix and certain incidence-algebra families, with characteristic restrictions; they reproduce an earlier Słowik total-count identity. Those results explain known **identity-fiber** overlap in restricted circumstances. Their inspected statements do not specify \(k\)-th-root multiplicities for **every prescribed unit target** in arbitrary radical-square-zero quiver algebras, nor the characteristic-dividing-exponent image transition and constrained graph-partition formula. The algebraic method here reduces every prescribed fiber to independent arrow equations; it is not a claim that the polynomial identity for one arrow is itself novel. Earlier implicit coverage remains possible and would require additional priority review.

## Limitations

The theorem concerns finite-dimensional split path algebras with square-zero arrow ideal. If paths of length two survive, off-diagonal power coordinates couple and the proof does not apply. No claim is made about irreducible character degrees, conjugacy-class sizes, full upper-triangular groups with nonzero products of arrows, or scheme-theoretic multiplicities. Historical priority of an equivalent full-fiber theorem is not conclusively established; the 2012 full text was not accessible. No independent mathematical audit was performed.

## References

1. R. Słowik, "Involutions in triangular groups," *Linear and Multilinear Algebra* **61** (2013), 909--916. DOI: `10.1080/03081087.2012.716432`; first made available online 28 August 2012.
2. I. Gargate and M. Gargate, "(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets," arXiv:`2009.04243v1` (30 August 2020), especially Theorems 1.1--1.2, Lemma 2.2, and Section 5.
