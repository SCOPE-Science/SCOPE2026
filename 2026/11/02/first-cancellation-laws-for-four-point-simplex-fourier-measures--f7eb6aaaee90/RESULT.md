# First-cancellation laws for four-point simplex Fourier measures at integer scales

## Finding
For an integer \(b\ge2\), let \(U_1,U_2,\ldots\) be independent, uniformly distributed on \(D=\{0,e_1,e_2,e_3\}\subset\mathbb R^3\), and let \(\mu_b\) be the law of \(\sum_{j\ge1}b^{-j}U_j\). For an integer frequency \(m\in\mathbb Z^3\), define the first cancellation level
\[
J_b(m)=\inf\big\{j\ge1:1+\sum_{i=1}^3\exp(2\pi i m_i/b^j)=0\big\},
\]
with value \(\infty\) if the set is empty. The vanishing of \(\widehat\mu_b(m)\) is equivalent to \(J_b(m)<\infty\).

For odd \(b\), every integer Fourier coefficient is nonzero. For every **even** integer \(b\ge2\), the natural density of integer frequencies whose *first* cancellation occurs at level \(j\ge1\) is
\[
q_{b,j}=\frac{3}{b-1}\left(b^{-3j}+(b-2)b^{-2j}\right).
\]
Consequently the first-cancellation generating function and total null-frequency density are
\[
G_b(z)=\sum_{j\ge1}q_{b,j}z^j
=\frac{3z((b-1)b^2-z)}{(b^3-z)(b^2-z)},
\qquad
\delta_b=G_b(1)=\frac{3(b^3-b^2-1)}{(b^3-1)(b^2-1)}.
\]
All assertions about density use centered boxes \([-N,N]^3\cap\mathbb Z^3\) as \(N\to\infty\), with \(b\) and \(j\) fixed.

A frequency can have **at most two distinct vanishing mask factors**. The density of frequencies with exactly two such factors is
\[
\delta_b^{(2)}=\frac{3}{(b^3-1)(b^2-1)},
\]
and that with exactly one is \(\delta_b-\delta_b^{(2)}\). In particular, among integer Fourier-null frequencies, the conditional density having two cancellation levels is \(1/(b^3-b^2-1)\).
For the first even composite scale, \(b=4\), these densities are \(\delta_4=47/315\), \(\delta_4^{(2)}=1/315\), and \(\delta_4^{(1)}=46/315\). The scale \(b=2\) case is consistent with previously studied dyadic simplex counting; the general even-scale formulas, particularly \(b\ge4\), are the focus here.

## Assumptions and scope
The four digits have equal weights, the scalar contraction is \(b^{-1}\), and Fourier frequencies are integer triples. The Fourier transform uses \(\widehat\mu_b(m)=\int e^{-2\pi i m\cdot x}\,d\mu_b(x)\). Changing the sign in the Fourier exponential does not change its zeros. A cancellation level counts a zero factor in the defining infinite product, **not** an analytic order of vanishing of the transform in three real variables. No assertion is made about noninteger frequencies, unequal weights, anisotropic scales, or other digit configurations.

## Proof
**1. Fourier product and four-unit-vector geometry.** Independence yields
\[
\widehat\mu_b(m)=\prod_{j\ge1}\frac{1+\sum_{i=1}^3\exp(-2\pi i m_i/b^j)}4.
\]
For fixed \(m\), the factors approach \(1\), with summable deviations. A product of nonzero factors is therefore nonzero; the product vanishes precisely when some individual factor does. Four complex numbers of modulus one sum to zero only if they split into two antipodal pairs. To prove this, pair the first two, with sum \(s\). If \(s=0\), both chosen pairs are antipodal. Otherwise, for any unit-modulus pair \(u,v\) with \(u+v=s\), the identity \(\overline s=s/(uv)\) fixes the product \(uv=s/\overline s\); hence \(\{u,v\}\) is uniquely determined as the root multiset of \(t^2-st+s/\overline s\). The pair summing to \(-s\) must be \(\{-u,-v\}\). In the present four-term sum, \(1\) is necessarily paired with \(-1\).

If \(b\) is odd, no \(b^j\)-th root equals \(-1\), so no cancellation occurs. For even \(b\), write \(h_j=b^j/2\). A cancellation at level \(j\) occurs exactly when, for one index \(i\in\{1,2,3\}\) and the other indices \(r,s\),
\[
m_i\equiv h_j\pmod{b^j},\qquad m_r-m_s\equiv h_j\pmod{b^j}.
\tag{1}
\]
Multiple choices of \(i\) at the same level count as one vanishing factor.

**2. The two-state count.** Read the base-\(b\) digits of a uniformly chosen integer-frequency residue triple from least significant upward. A future cancellation beyond digit level \(\ell\) is possible only in the following live states: \(A\), all three residues are zero modulo \(b^\ell\); or \(B_i\), residue \(i\) is zero and the other two have the same nonzero residue modulo \(b^\ell\). All other residue classes are dead for later cancellation. At level \(\ell=0\) the state is \(A\).

From \(A\), exactly \(3(b-1)\) of the \(b^3\) next digit triples produce a cancellation under (1). If none occurs, exactly one triple (all zero) preserves \(A\), and exactly \(3(b-2)\) triples enter one of the \(B_i\) states: \((0,u,u)\) up to permutation with \(u\notin\{0,b/2\}\). From each \(B_i\), exactly \(b\) next triples produce a cancellation, exactly \(b\) noncancelling triples preserve \(B_i\), and every other triple is dead. These alternatives are disjoint. The distinction among the three \(B_i\)'s does not affect the transition probabilities.

Let \(F_A(z)\) and \(F_B(z)\) be the probability generating functions for the first future cancellation from these states, with each new digit level weighted by \(z\). The transitions yield
\[
F_B(z)=\frac{z}{b^2}+\frac{z}{b^2}F_B(z)=\frac{z}{b^2-z},
\]
\[
F_A(z)=\frac{3(b-1)z}{b^3}+\frac{z}{b^3}F_A(z)
+\frac{3(b-2)z}{b^3}F_B(z).
\]
Solving gives \(F_A=G_b\) as in the statement. Partial fractions yield the asserted \(q_{b,j}\), and summing yields \(\delta_b\).

**3. At most two levels, and their density.** A cancellation arising from a \(B_i\) state leaves no live state for further cancellations. A cancellation arising from \(A\) leaves a live state only in the three digit patterns \((0,b/2,b/2)\) up to permutation, and that state is a \(B_i\). Hence no frequency has more than two vanishing mask factors. To have two, the first cancellation must occur from \(A\) after \(j-1\) all-zero digit triples, with one of those three patterns; then a later cancellation must occur from \(B_i\). The conditional eventual absorption probability from \(B_i\) equals \(F_B(1)=1/(b^2-1)\). Therefore
\[
\delta_b^{(2)}=\sum_{j\ge1}b^{-3(j-1)}\frac3{b^3}\frac1{b^2-1}
=\frac3{(b^3-1)(b^2-1)}.
\]

**4. Existence of lattice natural densities.** Every event involving only the first \(L\) levels is a union of classes modulo \(b^L\), and thus has the asserted density obtained from uniform residue counting. Any cancellation at a later level requires that modulo \(b^L\) either all coordinates vanish or one coordinate vanishes while the other two agree. There are exactly \(1+3(b^L-1)\) such residue triples out of \(b^{3L}\). Their density tends to zero with \(L\), bounding uniformly the upper natural density of all omitted later-level events. This passes the finite-level probabilities and their intersections to the stated infinite-scale natural densities.

## Verification
The accompanying self-contained `checker.py` uses exact integer polynomial division to construct cyclotomic polynomials and test Fourier-mask zeros independently of the antipodal congruence lemma. It exhaustively compares all integer frequency residue triples at \((b,L)=(2,4),(3,2),(4,3),(6,2)\), including first-cancellation counts and the number of simultaneous cancellation levels. It reported `FOUR_ATOM_SIMPLEX_EXACT_CYCLOTOMIC_OK`. For instance, at \(b=4,L=3\), the exact counts of classes with zero, one, or two vanishing factors were \((223039,38277,828)\) out of \(4^9=262144\). The proof above, not this finite enumeration, establishes the claims for every integer scale and arbitrarily many levels.

## Relationship to prior work
The infinite convolution and its Fourier product are standard in affine iterated function systems, as in Dutkay–Jorgensen (2006). Lam–Leung (1995) develops vanishing sums of roots of unity, although the four-unit-vector lemma needed here admits the direct geometric proof given above. For the exact four-digit three-dimensional simplex, Li (2012) analyzes spectrality, and Lu–Dong–Zhang (2019), referring to Li's earlier work, explicitly gives the *continuous Fourier-zero locus* as a union of three families of affine congruence conditions (its Section 2, formula (2.3)). Thus the zero-locus description and the elementary mask product are **not asserted to be new**. The claim here is the explicit first-cancellation distribution over the full integer lattice for all even scales, its sharp two-level restriction and double-cancellation density. Existing spectrality and zero-locus theorems do not directly state these lattice counting laws. The \(b=2\) specialization also overlaps earlier dyadic simplex enumerations; the new scope concerns other even scales.

## Limitations
A closely relevant 2012 primary article was accessible through its publisher abstract but not its full text, and equivalent earlier lattice-density calculations in the self-affine Fourier literature cannot be ruled out. The result makes no independent-validation or publication-priority claim. It is restricted to scalar integer expansions and integer Fourier frequencies; general orthogonality of exponentials and the spectrality of the measures are different questions. The number of vanishing mask factors must not be confused with the analytic multiplicity of a zero.

## References
- T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, arXiv:math/9511209, first posted 1995-11-13; Journal of Algebra 224 (2000), 91–109, DOI 10.1006/jabr.1999.8089.
- D. E. Dutkay and P. E. T. Jorgensen, *Fourier Frequencies in Affine Iterated Function Systems*, arXiv:math/0604547, first posted 2006-04-25; Journal of Functional Analysis 247 (2007), 110–137.
- J.-L. Li, *Spectrality of Self-Affine Measures on the Three-Dimensional Sierpinski Gasket*, Proceedings of the Edinburgh Mathematical Society 55 (2012), 477–496, DOI 10.1017/S0013091511000502.
- Z.-Y. Lu, X.-H. Dong and P.-F. Zhang, *Non-Spectrality of Self-Affine Measures on the Three-Dimensional Sierpinski Gasket*, Forum Mathematicum 31 (2019), DOI 10.1515/forum-2019-0062.
