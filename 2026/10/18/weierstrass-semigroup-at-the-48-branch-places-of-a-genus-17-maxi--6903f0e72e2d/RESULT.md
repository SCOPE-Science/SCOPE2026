# Weierstrass semigroup at the 48 branch places of a genus-17 maximal curve

## Finding

Let \(k=\mathbb F_{121}=\mathbb F_{11}(\alpha)\), where \(\alpha^2=-1\), and let \(G/k\) be the smooth projective curve with function field
\[
 k(x,y,z),\qquad (y^2-1)^2=1-x^{12},\qquad
 z^2=(\alpha+1)f(x)f(\alpha x),\quad f(X)=(X+1)(X^2+X+1).
\]
For every geometric point \(P\) among the **48 rational places lying above the twelve roots** of \(x^{12}-1\), the Weierstrass semigroup is exactly
\[
 \boxed{H(P)=\langle 10,11,12,18,26\rangle.}
\]
Its 17 gaps are
\[
 \boxed{\{1,2,3,4,5,6,7,8,9,13,14,15,16,17,19,25,27\}.}
\]
In particular, the multiplicity is \(10\), the conductor is \(28\), and \(\ell(18P)=5\).

## Assumptions and scope

All function fields and differentials have characteristic \(11\); semigroups are geometric and are computed at the indicated points (not at every point of the curve). The four cubic polynomials \(A=f(x)\), \(B=f(-x)\), \(C=f(\alpha x)\), \(D=f(-\alpha x)\) have disjoint simple zero sets, and \(ABCD=1-x^{12}\). The three independent quadratic characters below define a separable \((\mathbb Z/2)^3\)-cover of the projective \(x\)-line. Riemann–Hurwitz gives \(2g(G)-2=-16+12\cdot4=32\), hence \(g(G)=17\).

For a rational point \(P\), \(H(P)\) is the set of nonnegative pole orders of functions whose only pole is at \(P\); \(\ell(mP)=\dim_k L(mP)\). The 2026 construction proves that the 48 indicated places are rational and lie in one automorphism orbit (Lemma 2.2 and Lemma 4.4 of the source). It therefore suffices to compute the gap sequence at any of the four points over \(x=-1\).

## Proof

**1. Seven quadratic character fields and a complete canonical basis.** Put
\[
 t^2=2CD,\quad u^2=2AB,\quad z^2=(\alpha+1)AC,
\]
where the source's element \(t=y+x^6/y\) and \(u=y-x^6/y\) realize the first two square roots. The seven nontrivial characters can be represented by
\[
 w_t=t,\quad w_u=u,\quad w_z=z,\quad w_{tu}=tu,
 \quad w_{tz}=tz/C,\quad w_{uz}=uz/A,
 \quad w_{tuz}=tuz/(AC).
\]
Their squares, in that order, are \(2CD\), \(2AB\), \((\alpha+1)AC\), \(4ABCD\), \(2(\alpha+1)AD\), \(2(\alpha+1)BC\), and \(4(\alpha+1)BD\). All but \(w_{tu}\) have squarefree degree-six squares and therefore give genus-two hyperelliptic quotients; \(w_{tu}\) has a degree-twelve square and yields a genus-five quotient.

For each character \(\chi\), take \(s^j\,dx/w_\chi\), with \(s=x+1\), with \(0\le j\le1\) for the six degree-six characters and \(0\le j\le4\) for \(\chi=tu\). These are pullbacks of regular differentials from the quadratic quotients. They are linearly independent because the characteristic is prime to eight and they lie in distinct character spaces. Their number is \(6\cdot2+5=17=g(G)\); consequently they form a complete basis of \(H^0(G,\Omega^1)\).

**2. Local parity decomposition at \(x=-1\).** At a point over \(x=-1\), \(u\) is a uniformizer because \(A\) has a simple zero there and \(B(-1)\ne0\). The characters \(u,z,tu,tz\) ramify at that branch, whereas \(t,uz,tuz\) do not. For the first four characters \(dx/w_\chi\) is \(dx/u\) times a unit in \(k[[s]]\), so its vanishing orders are even. For the last three, \(dx/w_\chi\) is \(dx/t\) times a unit in \(k[[s]]\), so its vanishing orders are odd. Here \(v_P(s)=2\), \(v_P(dx/u)=0\), and \(v_P(dx/t)=1\). Constants arising from different square-root signs merely rescale rows and do not change the filtration.

**3. Finite-field expansion certificate.** For the even block, the coefficient series (apart from nonzero scalar factors) are
\[
 s^j\sqrt{\frac{w_u^2/w_\chi^2}{(w_u^2/w_\chi^2)(-1)}},
 \qquad\chi\in\{u,z,tu,tz\},
\]
interpreting each ratio after cancelling its common simple factor \(s\). The dimensions for these four characters are respectively \(2,2,5,2\). For the odd block replace \(u\) by \(t\), use characters \(t,uz,tuz\), and dimensions \(2,2,2\). Every formal square root is normalized to constant term one and is uniquely determined in characteristic eleven by the identity \(h(s)^2=R(s)\). The attached verifier computes the exact coefficients in \(\mathbb F_{11}[\alpha]/(\alpha^2+1)\), constructing an \(11\)-by-\(14\) even matrix and a \(6\)-by-\(8\) odd matrix.

The determinants of the submatrices formed by the pivot columns are \(1\) and \(4\), respectively, in \(\mathbb F_{11}\). Exact Gaussian elimination in the coefficient order \(s^0,s^1,\ldots\) gives the even pivot columns
\[
 0,1,2,3,4,6,7,8,9,12,13
\]
and odd pivot columns
\[
 0,1,2,3,6,7.
\]
Since both matrices have full row rank, the pivot columns give every possible leading order in their respective spaces; no later leading order is omitted. Doubling the even columns and doubling and adding one to the odd columns yields exactly the \(17\) canonical differential orders
\[
 0,1,2,3,4,5,6,7,8,12,13,14,15,16,18,24,26.
\]
For a smooth genus-\(g\) curve, the gaps at a point are precisely one plus the \(g\) orders of vanishing of its regular differentials. The stated gaps follow.

**4. Numerical semigroup.** Taking the complement of the gap set gives the monoid generated minimally by \(10,11,12,18,26\); this can be verified below the conductor \(28\), after which every integer is a sum of these generators. The resulting Riemann–Roch dimension at \(18P\) is \(\ell(18P)=5\). Automorphism transitivity transports the semigroup from the four places over \(x=-1\) to all 48 distinguished places.

## Verification

Run `python3 verify_semigroup.py CERTIFICATE.json` in the directory containing the two named files. The program uses only integer arithmetic and the Python standard library. It builds all four branch polynomials, checks their product identity, constructs the two coefficient matrices, checks every coefficient of each formal square-root identity, performs exact elimination over \(\mathbb F_{121}\), and checks both the reported gaps and generators. The saved `CERTIFICATE.json` contains the exact coefficient matrices and all final pivots. The program returned `VERIFY_OK` on the embedded artifacts. The finite matrices are exhaustive for the full canonical differential space, not experimental samples.

## Relationship to prior work

Beelen–Montanucci–Niemann (arXiv:2609.11679, Sections 2 and 4) introduced the genus-17 maximal curve, determined its full automorphism group, and used a dimension check at \(18P\) to distinguish the special 48-point orbit. Their displayed curve equations and orbit transitivity are inputs here; they do not give the full gap set or semigroup generators. The complete local canonical filtration above determines these exact new invariants.

Beelen–Montanucci–Niemann–Quoos (arXiv:2404.14179) compute semigroups for a different family of Hermitian subfields. Beelen–Montanucci–vom Braucke (arXiv:2602.24015) treat maximal Fermat function fields, likewise Hermitian subfields. In contrast, the present source proves that \(G\) is not a Hermitian subfield. Their families and formulas therefore do not directly specify the semigroup at the indicated places of \(G\).

## Limitations

The claim concerns only the 48 specified ramification points. It does not classify semigroups at the remaining rational or nonrational places, calculate all AG-code minimum distances, or claim a new maximality or automorphism theorem. The finite-field coefficient computation requires the precise defining constants and characteristic \(11\). An equivalent unindexed prior computation may exist. Independent mathematical review has not been performed.

## References

1. P. Beelen, M. Montanucci, J. Niemann, *A maximal function field of genus \(17\) over \(\mathbb F_{11^2}\)*, arXiv:2609.11679v1 (10 September 2026), especially Sections 2 and 4 and Appendix A. https://arxiv.org/html/2609.11679
2. P. Beelen, M. Montanucci, J. T. Niemann, L. Quoos, *Some families of non-isomorphic maximal function fields*, arXiv:2404.14179 (2024), Sections 2–3. https://arxiv.org/abs/2404.14179
3. P. Beelen, M. Montanucci, M. F. vom Braucke, *On Weierstrass semigroups of maximal Fermat function fields*, arXiv:2602.24015 (2026). https://arxiv.org/abs/2602.24015
4. Standard gap theorem: see the formulation cited as Proposition 2.1 in Reference 2 (the vanishing-order formulation used here).
