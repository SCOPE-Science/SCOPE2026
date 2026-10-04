# A Catalan ternary law for line counts on critical hypersurfaces
## Finding
For each integer \(n\ge2\), let \(L_n\) denote the number of complex lines on a general hypersurface of degree \(2n-3\) in \(\mathbb P^n_{\mathbb C}\). This is the zero-dimensional critical line problem: the Grassmannian of lines has dimension \(2n-2\), and the condition that a degree-\(2n-3\) equation vanish on a line has rank \(2n-2\).

Let
\[
C_m=\frac{1}{m+1}\binom{2m}{m}
\]
be the \(m\)-th Catalan number. Then the complete reduction modulo three is
\[
L_{3m}\equiv0\pmod3\qquad(m\ge1),
\]
\[
L_{3m+1}\equiv C_m\pmod3\qquad(m\ge1),
\]
and
\[
L_{3m+2}\equiv C_m\pmod3\qquad(m\ge0).
\]
Thus the two nonzero residue classes of the ambient dimension are not merely equal modulo three, as was previously known: their common row is exactly the Catalan sequence modulo three.

This gives an explicit ternary description. For \(n\not\equiv0\pmod3\), let \(m\) be defined by \(n=3m+1\) or \(n=3m+2\), and write
\[
m+1=a_0+3a_1+\cdots+3^r a_r,
\qquad a_j\in\{0,1,2\}.
\]
Then
\[
L_n\not\equiv0\pmod3
\]
if and only if
\[
a_j\in\{0,1\}\quad\text{for every }j\ge1.
\]
When this holds,
\[
L_n\equiv(-1)^{a_1+\cdots+a_r}\pmod3.
\]
Consequently, for every \(r\ge1\), exactly
\[
3\cdot2^r-1
\]
integers \(n\) with
\[
2\le n\le3^{r+1}
\]
have line count not divisible by three. Hence
\[
3\mid L_n
\]
for a natural-density-one set of ambient dimensions.

## Assumptions and scope
The hypersurface is general over \(\mathbb C\), and \(n\ge2\). The case \(n=2\) is the degree-one hypersurface in \(\mathbb P^2\), which contains one line and fits the stated congruence. For \(n\ge3\), the problem is the classical finite Fano-scheme problem for lines on a degree-\(2n-3\) hypersurface.

The claim concerns the enumerative degree over characteristic zero. It does not assert that reduction of an individual hypersurface modulo three has the same number of geometric lines, nor does it address multiplicities or pathologies of Fano schemes in characteristic three.

## Proof
Debarre and Manivel give the general coefficient formula for the Pluecker degree of a Fano scheme of linear spaces. Specializing their formula to lines on one hypersurface of degree
\[
d=2n-3
\]
with expected dimension zero gives
\[
L_n=[x^ny^{n-1}](x-y)\prod_{i=0}^{2n-3}\bigl(ix+(2n-3-i)y\bigr).
\]
Equivalently, after setting \(y=1\), this is the one-variable coefficient formula used by Gruenberg and Moree.

First suppose
\[
n=3m.
\]
Then
\[
d=6m-3\equiv0\pmod3.
\]
Whenever \(i\equiv0\pmod3\), both coefficients in the factor
\[
ix+(d-i)y
\]
are divisible by three. Therefore the entire product is zero modulo three, and
\[
L_{3m}\equiv0\pmod3.
\]

Next suppose
\[
n=3m+1.
\]
Then \(d=6m-1\equiv2\pmod3\), and each residue class of \(i\) modulo three occurs exactly \(2m\) times in the range \(0\le i\le6m-1\). Modulo three the three factor types are
\[
-y,\qquad x+y,\qquad -x.
\]
Hence
\[
\prod_{i=0}^{6m-1}\bigl(ix+(6m-1-i)y\bigr)
\equiv x^{2m}y^{2m}(x+y)^{2m}\pmod3.
\]
The desired coefficient is therefore
\[
\binom{2m}{m}-\binom{2m}{m+1}=C_m,
\]
which proves
\[
L_{3m+1}\equiv C_m\pmod3.
\]

Finally suppose
\[
n=3m+2.
\]
Now \(d=6m+1\equiv1\pmod3\). The residue classes \(0,1,2\) occur respectively \(2m+1,2m+1,2m\) times. The corresponding factor types are
\[
y,\qquad x,\qquad -(x+y),
\]
so
\[
\prod_{i=0}^{6m+1}\bigl(ix+(6m+1-i)y\bigr)
\equiv x^{2m+1}y^{2m+1}(x+y)^{2m}\pmod3.
\]
The same coefficient difference gives
\[
L_{3m+2}\equiv C_m\pmod3.
\]

Deutsch and Sagan give a complete description of Catalan numbers modulo three. In the notation above, their result says that \(C_m\) is nonzero modulo three precisely when every ternary digit of \(m+1\) above the units digit belongs to \(\{0,1\}\), and then its residue is
\[
(-1)^{a_1+\cdots+a_r}.
\]
Combining this with the preceding congruence yields the stated ternary rule for \(L_n\).

For the counting consequence, among
\[
0\le m<3^r,
\]
exactly \(3\cdot2^{r-1}\) values have \(C_m\not\equiv0\pmod3\): the units digit of \(m+1\) is unrestricted, each of the next \(r-1\) digits has two choices, and the endpoint \(m+1=3^r\) replaces the excluded zero. Each such \(m\) contributes the two dimensions \(3m+1\) and \(3m+2\). Removing the formal dimension \(n=1\) leaves exactly
\[
3\cdot2^r-1
\]
nondivisible line counts in \(2\le n\le3^{r+1}\). Dividing by \(3^{r+1}-1\) and letting \(r\to\infty\) proves density one for divisibility by three.

## Verification
The proof is symbolic and does not rely on finite experimentation. The coefficient formula specializes correctly to the classical initial values
\[
L_2=1,\quad L_3=27,\quad L_4=2875,\quad L_5=698005,\quad L_6=305093061,
\]
which are printed in the published congruence literature and in independent computer-algebra documentation. Their residues modulo three begin
\[
1,0,1,1,0,
\]
in agreement with the theorem.

The key boundary checks are exact: the residue counts of the factors are \((2m,2m,2m)\) for \(n=3m+1\) and \((2m+1,2m+1,2m)\) for \(n=3m+2\); in both cases the remaining coefficient after removing the monomial factor is the Catalan difference
\[
\binom{2m}{m}-\binom{2m}{m+1}.
\]

## Relationship to prior work
Debarre--Manivel give a general coefficient formula for the degree of Fano schemes, and explicitly note that the line-on-a-hypersurface case goes back to van der Waerden. Their formula supplies the enumerative input but contains no modulus-three or Catalan classification.

Gruenberg--Moree--Zagier study exactly the sequence \(L_n\) and its congruences. Their modulus-three table displays two equal nonzero rows and one zero row, and their Theorem 3.1 proves equality of the first two rows and vanishing of the third. They do not identify the common first-two-row sequence with Catalan residues. Their appearances of Catalan numbers concern a different divisibility argument involving \((2n-3)^3\), not the modulus-three row.

Deutsch--Sagan independently determine Catalan residues modulo three from ternary digits. Their paper does not concern Fano schemes, hypersurface line counts, or the sequence \(L_n\). The bridge proved here therefore turns the previously implicit nonzero rows of the enumerative modulus-three table into an explicit Catalan automatic sequence and yields the density-one divisibility consequence.

A later paper of Basu, Lerario, Lundberg, and Peterson again records the coefficient formula for the same complex line counts and cites the congruence literature while pursuing random real enumerative geometry and asymptotics. Its inspected text does not state the Catalan identification or the ternary classification.

## Limitations
The theorem is specific to modulus three. The factorization works unusually cleanly because the critical hypersurface degree is \(2n-3\), so the three residue classes of the factors collapse to monomials and \(x+y\). Other primes lead to different coefficient problems and are not covered here.

The density statement concerns ambient dimensions, not a density on the moduli space of hypersurfaces. The result is enumerative over \(\mathbb C\); no claim is made about line counts after reduction to characteristic three.

The literature comparison found no explicit Catalan identification for the modulus-three line-count rows, but an unindexed observation or lecture note could contain the same short reduction.

## References
Olivier Debarre and Laurent Manivel, *Sur la variete des espaces lineaires contenus dans une intersection complete*, Math. Ann. 312 (1998), 549--574; first public preprint *Schemas de Fano*, arXiv:alg-geom/9611033, 26 November 1996.

Daniel B. Gruenberg and Pieter Moree, with an appendix by Don Zagier, *Sequences of Enumerative Geometry: Congruences and Asymptotics*, Experimental Mathematics 17 (2008), 409--426; arXiv:math/0610286, 9 October 2006.

Emeric Deutsch and Bruce E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, Journal of Number Theory 117 (2006), 191--215; arXiv:math/0407326, 19 July 2004.

Saugata Basu, Antonio Lerario, Erik Lundberg, and Chris Peterson, *Random fields and the enumerative geometry of lines on real and complex hypersurfaces*, arXiv:1610.01205, 4 October 2016; Math. Ann. 374 (2019), 1773--1810.
