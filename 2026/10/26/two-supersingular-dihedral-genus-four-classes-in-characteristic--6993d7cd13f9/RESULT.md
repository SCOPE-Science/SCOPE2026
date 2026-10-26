# Two supersingular dihedral genus-four classes in characteristic seven

## Finding
Let \(k=\overline{\mathbb F}_7\). Every smooth genus-four hyperelliptic curve over \(k\) admitting the dihedral automorphism configuration classified by Ohashi–Kudo is isomorphic to a member of
\[
 C_a:\quad y^2=x^{10}+a x^5+1,\qquad a\in k,\quad a^2\ne4.
\]
Within this complete one-parameter family, the Jacobian has \(7\)-rank zero precisely at \(a=0\) or \(a^2=-1\), and otherwise has \(7\)-rank four. The rank-zero members have \(a\)-number two and are supersingular but not superspecial. All other smooth members are ordinary. The rank-zero locus consists of precisely **two geometric isomorphism classes**, represented by \(C_0\) and \(C_i\), where \(i^2=-1\); the two signs of \(i\) give the same geometric class.

The \(\mathbb F_7\)-model \(C_0\) has zeta numerator
\[
L(C_0/\mathbb F_7,T)=(1+49T^4)^2.
\]
For either \(i\in\mathbb F_{49}\) with \(i^2=-1\), the \(\mathbb F_{49}\)-model \(C_i\) has zeta numerator
\[
L(C_i/\mathbb F_{49},T)=(1+49T^2)^4.
\]
The base change of \(C_0\) to \(\mathbb F_{49}\) has the same zeta numerator. Both geometric classes attain \(2794\) rational points over \(\mathbb F_{2401}\), the Hasse–Weil upper bound for genus four over that field.

## Assumptions and scope
The field has characteristic seven, all geometric statements are over its algebraic closure, and the hyperelliptic equations always denote their smooth projective completions. The condition \(a^2\ne4\) is necessary and sufficient for separability of \(x^{10}+ax^5+1\). The automorphism-family normal form and its geometric-isomorphism identification are prior theorems of Ohashi and Kudo; the new claim concerns the exact supersingular/ordinary strata and the indicated arithmetic Weil polynomials. Isomorphism classes are geometric, not counts of fixed-coordinate equations. The statement about rank four means the stable Cartier rank on the Jacobian; it does not identify all possible non-isomorphic arithmetic twists.

## Proof
Put \(t=x^5\). Then the branch polynomial is \(t^2+at+1\); it has two distinct nonzero roots if and only if \(a^2\ne4\), whence the degree-ten polynomial has ten distinct roots and its smooth double cover has genus four.

In odd characteristic \(p\), the Cartier–Manin matrix in the basis \(x^{j-1}dx/y\), \(1\le j\le4\), has entries \(M_{ij}=[x^{pi-j}](x^{10}+ax^5+1)^{(p-1)/2}\) (up to the usual Frobenius-semilinear convention, which does not alter ranks). For \(p=7\), expand
\[
(x^{10}+ax^5+1)^3=(t^2+at+1)^3.
\]
The only potentially nonzero matrix entries are
\[
 M_{12}=M_{43}=3a,\qquad M_{24}=M_{31}=3(a^2+1).
\]
Their support is one directed four-cycle: a nonzero entry in every position makes \(M\) invertible, giving \(7\)-rank four and \(a\)-number zero. If \(a=0\) or \(a^2=-1\), precisely two entries remain nonzero, so \(\operatorname{rank}M=2\), giving \(a\)-number two. Because a length-four Cartier cycle has at least one zero arrow in these cases, a sufficiently high semilinear iterate vanishes; the stable Cartier rank and the \(7\)-rank are zero. The two conditions cannot coincide in characteristic seven. Both are compatible with \(a^2\ne4\).

It remains to prove *supersingularity*, which does not follow merely from zero \(7\)-rank. Explicit counting over \(\mathbb F_{2401}\) shows for either \(a=0\) or a chosen \(i^2=-1\) that \(x^{10}+ax^5+1\) has ten zero values, 1391 nonzero square values, and 1000 nonsquare values. There are two rational points above infinity. Hence
\[
\#C_a(\mathbb F_{2401})=10+2(1391)+2=2794
=2401+1+2(4)\sqrt{2401}.
\]
Equality in the upper Hasse–Weil bound forces every geometric Frobenius eigenvalue over \(\mathbb F_{2401}\) to equal \(-49\). Each eigenvalue is therefore a root of unity multiplied by \(\sqrt7\) at the base characteristic, so every Newton slope equals \(1/2\). Thus both classes are supersingular. Their \(a\)-number is two, so neither is superspecial.

Over \(\mathbb F_7\), direct counts for \(C_0\) at extension degrees \(1,2,3,4\) give respectively \(8,50,344,2794\). Newton identities give its first four Weil coefficients as \(0,0,0,98\); the genus-four functional equation fixes the rest, giving \((1+49T^4)^2\). For \(C_i\) over \(\mathbb F_{49}\), the count is \(50\). Every \(\mathbb F_{49}\)-Frobenius eigenvalue has square \(-49\), by maximality over \(\mathbb F_{2401}\), and the trace vanishes since \(\#C_i(\mathbb F_{49})=50\). Equal positive and negative signs give \((1+49T^2)^4\). Squaring the \(\mathbb F_7\)-Frobenius eigenvalues of \(C_0\) gives exactly this same numerator over \(\mathbb F_{49}\).

The normal-form classification and its parameter-isomorphism criterion of Ohashi–Kudo identify \(a\) and \(-a\) geometrically and distinguish the \(a^2=0\) and \(a^2=-1\) parameters. Equivalently the central member has extra symmetry relative to the generic member. Thus the three coefficient parameter values yield exactly two geometric classes.

## Verification
Run \(\texttt{python3 verify.py}\). It uses explicit polynomial-residue finite fields of orders \(7,49,343,2401\), checks their irreducible defining polynomials, performs the full character census for each relevant curve, checks the Cartier–Manin support and rank alternatives, and prints \(\texttt{VERIFY_OK}\). In particular, the \(\mathbb F_{2401}\) enumerations each inspect all 2401 field elements. The proof independently explains why these finite calculations imply the complete infinite geometric classification and the exact Weil polynomials; finite enumeration alone is not taken as a proof of any assertion about all extension degrees.

## Relationship to prior work
Ohashi–Kudo (arXiv:2312.16858; initially public 2023-12-28) supply the family \(C_a\), its dihedral automorphism characterization and its geometric-isomorphism criterion, with an emphasis on **superspecial** rather than the complete **supersingular** locus in characteristic seven. Kudo–Harashita establish that there are no superspecial genus-four curves in characteristic seven; our two strata are consistent because both have \(a\)-number two. Li–Mantovan–Pries–Tang study Newton polygons in cyclic-cover families, but their genus-four order-five row has a different branch-inertia profile, so it does not directly determine this family's characteristic-seven two-class classification. Kudo–Harashita–Senda construct supersingular genus-four Howe curves in all characteristics, but that existence theorem does not classify this dihedral hyperelliptic locus.

## Limitations
No claim of absolute priority is made: an unindexed earlier finite-field census or an indirect application of a broader cyclic-cover result could overlap. Geometric isomorphism classification relies on the cited Ohashi–Kudo theorem; the point counts and ranks are independently verifiable here. This is a classification only within the indicated dihedral genus-four hyperelliptic locus, not all genus-four curves. The genus-four zeta numerator over \(\mathbb F_{49}\) for the two displayed equations does not classify arithmetic twists or imply their Jacobians are geometrically isomorphic.

## References
- Ryo Ohashi and Momonari Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, arXiv:2312.16858 (first public 2023-12-28), https://arxiv.org/abs/2312.16858.
- Momonari Kudo and Shushi Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114, https://arxiv.org/abs/1607.01114.
- W. Li, E. Mantovan, R. Pries and Y. Tang, *Newton Polygons Arising for Special Families of Cyclic Covers of the Projective Line*, arXiv:1805.06914, https://arxiv.org/abs/1805.06914.
- M. Kudo, S. Harashita and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095, https://arxiv.org/abs/1903.08095.
