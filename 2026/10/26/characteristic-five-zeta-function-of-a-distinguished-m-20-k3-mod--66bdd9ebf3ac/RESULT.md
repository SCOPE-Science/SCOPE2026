# Characteristic-five zeta function of a distinguished \(M_{20}\) K3 model

## Finding
Let \(k=\mathbb F_5\), and let \(X\subset\mathbb P^5_k\) be cut out by
\[
\begin{aligned}
q_1&=x_1^2+x_4^2-3x_5^2+3x_6^2,\\
q_2&=x_2^2-3x_4^2+x_5^2-3x_6^2,\\
q_3&=x_3^2+3x_4^2-3x_5^2+x_6^2.
\end{aligned}
\]
This is the literal characteristic-five reduction of the diagonal model of Bonnafé–Sarti (2019, Section 5), with its golden-ratio parameter specializing to \(3\). The surface is a smooth geometrically integral K3 surface, and
\[
\#X(\mathbb F_5)=96,\qquad \#X(\mathbb F_{25})=1176.
\]
Its entire zeta function is
\[
\boxed{Z(X/\mathbb F_5,T)=\frac{1}{(1-T)(1-25T)(1-5T)^{18}(1+5T)^4}.}
\]
In particular, for every integer \(m\ge1\),
\[
\#X(\mathbb F_{5^m})=1+5^{2m}+5^m(18+4(-1)^m).
\]
All 22 Frobenius eigenvalues on degree-two \(\ell\)-adic cohomology have slope one; thus the surface is supersingular in the Newton-polygon sense. The formula makes no claim that the characteristic-zero group action specializes faithfully in characteristic five.

## Assumptions and scope
The ground field is precisely \(\mathbb F_5\) and its finite extensions; the surface is defined by the displayed *three* homogeneous quadrics, not by an unspecified twist or Kummer presentation. The parameter \(3\) is the unique root modulo \(5\) of \(\phi^2-\phi-1\). All point counts are of the projective smooth complete-intersection surface, not of a quotient or resolution. Cohomological statements use an auxiliary prime \(\ell\ne5\).

## Proof
**Smoothness and K3 geometry.** Write \(y_i=x_i^2\). The coefficient matrix of \((q_1,q_2,q_3)\), reduced modulo \(5\), is
\[
M=\begin{pmatrix}1&0&0&1&-3&3\\0&1&0&-3&1&-3\\0&0&1&3&-3&1\end{pmatrix}.
\]
Its 20 three-column minors, for the lexicographic order of column triples, are nonzero modulo \(5\); the exact verifier computes their residues, with distribution \(1:7,\ 2:4,\ 3:6,\ 4:3\). Thus any point of the common zero locus has at least four nonzero coordinates: three or fewer nonzero squares would contradict the independence of any three columns. The projective Jacobian has columns \(2x_iM_i\), so has rank three at every geometric point. The coordinatewise square map is finite, and the linear kernel of \(M\) is \(\mathbb P^2\), proving that the zero locus has dimension two. As a smooth connected complete intersection of three ample divisors in \(\mathbb P^5\), it is geometrically integral. Adjunction gives \(\omega_X\cong\mathcal O_X\), while the Koszul resolution gives \(H^1(X,\mathcal O_X)=0\), so \(X\) is K3.

**Two exact point counts.** Write \((a:b:c)=(y_4:y_5:y_6)\). The remaining squares are forced to be
\[
(y_1,y_2,y_3)=(-a+3b-3c,\ 3a-b+3c,\ -3a+3b-c).
\]
For any odd-order finite field \(K\supset\mathbb F_5\), consider a projective base point \((a:b:c)\in\mathbb P^2(K)\) and its six square-coordinate values. Suppose exactly \(r\) of them are nonzero. If they all belong to the same quadratic-character class of \(K^\times\), a common projective rescaling makes them all squares, giving exactly \(2^{r-1}\) projective lifts; otherwise there are no lifts. Here \(r\ge4\) by the minor argument. Exact enumeration of normalized base points gives, over \(\mathbb F_5\), exactly six contributing points with \(r=5\); hence \(6\cdot16=96\). Over \(\mathbb F_{25}\), the contributing points are exactly fifteen with \(r=4\), six with \(r=5\), and thirty with \(r=6\); hence \(15\cdot8+6\cdot16+30\cdot32=1176\). The complete reproducible program uses \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\) and additionally checks the first point count by direct independent enumeration of \(\mathbb P^5(\mathbb F_5)\).

**Full zeta function from a sharp cohomological bound.** Let \(\alpha_1,\ldots,\alpha_{22}\) denote Frobenius eigenvalues on \(H^2_{\mathrm{\acute et}}(X_{\bar k},\mathbb Q_\ell)\). For a smooth projective K3 surface, odd cohomology vanishes, \(b_2=22\), and the Weil bound gives \(|\alpha_i|=5\) under each complex embedding. Lefschetz's trace formula and the two counts give
\[
\sum_i\alpha_i=96-1-25=70,\qquad
\sum_i\alpha_i^2=1176-1-625=550=22\cdot25.
\]
The last equality saturates the triangle inequality for 22 complex numbers of absolute value \(25\); because the sum is positive real, every \(\alpha_i^2=25\). Thus each \(\alpha_i=\pm5\), and the first trace forces precisely 18 plus signs and four minus signs. The zeta expression and extension-field point formula follow. These same algebraic Frobenius eigenvalues have valuation one, proving the stated Newton slopes.

## Verification
Run `python3 verify.py` with Python's standard library. Its output terminates in `VERIFY_OK`, after independently checking 20 nonzero three-column minors, the \(\mathbb F_5\) and \(\mathbb F_{25}\) square-cover counts, direct projective enumeration over \(\mathbb F_5\), and the two Frobenius multiplicities. This finite calculation supplies exact inputs to, rather than a substitute for, the cohomological argument determining all extensions.

## Relationship to prior work
Bonnafé–Sarti introduced the characteristic-zero \(M_{20}\) complete-intersection model and proved its smoothness and its Kummer description; the defining equations above are their Section 5, specialized at the ramified prime \(5\). Their proofs and complex-lattice computations are not an exact \(\mathbb F_5\)-zeta computation. Brandhorst–Hashimoto classified complex K3 surfaces with maximal symplectic automorphism subgroups and does not compute this reduction's finite-field Frobenius. Bonnafé–Sarti's later study of other reflection-group K3 surfaces gives supersingular examples at other primes for other models, not the present point-count pair and degree-22 Frobenius polynomial. The claimed contribution is specifically the exact characteristic-five arithmetic and the resulting uniform extension-field formula; it does not claim the model or its K3 structure are newly discovered.

## Limitations
The zeta computation applies to the displayed integral model specialized at \(5\); it does not identify the Artin invariant of its geometric Néron–Severi lattice, or determine which characteristic-zero automorphisms extend. It does not furnish a characteristic-zero Frobenius formula or a classification of all reductions of related K3 surfaces. A literature search cannot rule out unindexed arithmetic calculations, so historical overlap remains a residual risk. Independent mathematical audit has not been performed.

## References
1. C. Bonnafé and A. Sarti, *K3 surfaces with maximal finite automorphism groups containing \(M_{20}\)*, arXiv:1910.05955 (first public 2019-10-14), especially Section 5, Propositions 5.5, 5.7, 5.10 and 5.12. https://arxiv.org/abs/1910.05955
2. S. Brandhorst and K. Hashimoto, *Extensions of maximal symplectic actions on K3 surfaces*, arXiv:1910.05952 (first public 2019-10-14); *Annales Henri Lebesgue* 4 (2021), 785–809. https://arxiv.org/abs/1910.05952
3. C. Bonnafé and A. Sarti, *Complex reflection groups and K3 surfaces II: The groups \(G_{29},G_{30},G_{31}\)*, arXiv:2112.12400 (2021), especially Remark 6.17 on supersingular reductions of distinct models. https://arxiv.org/abs/2112.12400
