# A complete projective classification of smooth plane-filling quintics over the binary field

## Finding

Exactly \(1512\) homogeneous ternary quintic forms over \(\mathbb F_2\) define geometrically smooth plane curves passing through every point of \(\mathbb P^2(\mathbb F_2)\). They form exactly ten \(\operatorname{PGL}_3(\mathbb F_2)\)-orbits: eight of size \(168\) and two of size \(84\). Consequently the corresponding rational projective stabilizers have orders one and two. Every smooth curve in the list is geometrically irreducible.

The classification concerns embedded curves under **rational projective changes of coordinates**, not abstract isomorphism classes over an algebraic closure. Since \(\mathbb F_2^\times\) consists only of one, no further scalar quotient of nonzero equations is required.

## Assumptions and scope

Let \(V\) be the vector space of all degree-five ternary homogeneous forms over \(\mathbb F_2\) that vanish on all seven rational projective points. The count includes every nonzero member of \(V\) prior to a geometric-smoothness test; no preliminary irreducibility or symmetry restriction is imposed. Smoothness means smoothness over \(\overline{\mathbb F}_2\). A finite-extension singular-point search is used to *exclude* equations, but geometric smoothness of the survivors is independently established by algebraic certificates.

## Proof and complete classification

**1. Exhaustive vector space.** Order the 21 degree-five monomials as \(X^iY^jZ^{5-i-j}\), first by increasing \(i=0,\dots,5\), then by increasing \(j=0,\dots,5-i\). Evaluation at the seven nonzero binary triples gives seven independent linear equations. Therefore \(\dim_{\mathbb F_2}V=14\), and precisely \(2^{14}-1=16383\) nonzero binary coefficient masks must be considered. For a reproducible mask convention, compute a kernel basis by highest-pivot elimination on the seven evaluation rows and enumerate masks with respect to the resulting ordered free columns.

**2. Certified excluded equations.** For each extension degree \(d=1,\dots,6\), construct \(\mathbb F_{2^d}\) by exact polynomial arithmetic. Inspect all projective points in the three standard normalized charts; solve the three derivative equations as binary linear conditions on the fourteen coefficient bits. The numbers of newly excluded nonzero forms at successive degrees are \(14196,147,24,420,0,84\), respectively. Each exclusion is justified by a specific gradient-zero point. Euler's formula \(XF_X+YF_Y+ZF_Z=5F=F\) in characteristic two shows that the gradient-zero point also lies on the curve. The total number of excluded equations is \(14871\), leaving exactly \(1512\) candidates. This bounded search **does not by itself** certify that every remaining equation is geometrically smooth.

**3. Rational projective orbits.** The swaps \(X\leftrightarrow Y\), \(Y\leftrightarrow Z\), together with \(X\mapsto X+Y\), generate the group \(\mathrm{GL}_3(\mathbb F_2)=\mathrm{PGL}_3(\mathbb F_2)\) of order \(168\). Exact substitution of polynomials, reduced modulo two, induces permutations of the surviving coefficient masks. Exhausting their group orbits yields the following table. The polynomials are written with coefficients in \(\mathbb F_2\).

| Mask | Orbit size | Representative quintic |
|---:|---:|---|
| 157 | 168 | \(YZ^4+Y^3Z^2+XZ^4+XYZ^3+XY^4+X^3YZ+X^4Z+X^4Y\) |
| 159 | 168 | \(YZ^4+Y^2Z^3+Y^3Z^2+Y^4Z+XZ^4+XYZ^3+XY^4+X^3YZ+X^4Z+X^4Y\) |
| 174 | 84 | \(Y^2Z^3+Y^3Z^2+XZ^4+XY^2Z^2+XY^4+X^3YZ+X^4Z+X^4Y\) |
| 251 | 168 | \(YZ^4+Y^2Z^3+XZ^4+XYZ^3+XY^2Z^2+XY^3Z+XY^4+X^3YZ+X^4Z+X^4Y\) |
| 410 | 84 | \(Y^2Z^3+Y^4Z+XZ^4+XYZ^3+XY^4+X^2Z^3+X^3YZ+X^4Y\) |
| **413** | **168** | \(YZ^4+Y^3Z^2+XZ^4+XYZ^3+XY^4+X^2Z^3+X^3YZ+X^4Y\) |
| 417 | 168 | \(YZ^4+Y^4Z+XY^2Z^2+XY^4+X^2Z^3+X^3YZ+X^4Z+X^4Y\) |
| 433 | 168 | \(YZ^4+Y^4Z+XYZ^3+XY^2Z^2+XY^4+X^2Z^3+X^4Z+X^4Y\) |
| 463 | 168 | \(YZ^4+Y^2Z^3+Y^3Z^2+Y^4Z+XZ^4+XY^3Z+XY^4+X^2Z^3+X^3YZ+X^4Y\) |
| 684 | 168 | \(Y^3Z^2+Y^4Z+XZ^4+XY^2Z^2+XY^4+X^2YZ^2+X^4Z+X^4Y\) |

In the row for mask **413**, note in particular the **absence** of the monomial \(X^4Z\). The mask-to-polynomial expansion determines this row uniquely. Including that monomial would produce a polynomial nonzero at \([1:0:1]\), hence it would not be plane-filling. The displayed equation is the genuine mask-413 representative. The ten disjoint orbit sizes sum to \(8\cdot168+2\cdot84=1512\), accounting for every survivor.

**4. Geometric smoothness, with no extension cutoff.** For each of the ten representative quintics, compute its three partial derivatives over \(\mathbb F_2\). On each affine projective chart \(X=1\), \(Y=1\), and \(Z=1\), a Gröbner basis of the three specialized derivatives reduces to the unit ideal. Therefore no common gradient zero exists over **any** algebraic extension. Every representative and every curve in its projective orbit is geometrically smooth. Together with the actual singular-point witnesses from step 2, this completes the classification. By Bézout's theorem, a smooth projective plane curve is geometrically irreducible: two positive-degree components would meet and create a singular point.

**5. Stabilizers.** Since \(|\operatorname{PGL}_3(\mathbb F_2)|=168\), the orbit–stabilizer formula gives stabilizers of order one for the 168-element orbits and order two for the 84-element orbits. No other stabilizer sizes occur among smooth binary plane-filling quintics.

## Verification and limitations

The accompanying exact-arithmetic `verify.py` constructs the dimension-fourteen kernel, witnesses singularities over extensions of degrees one through six, enumerates all projective orbits under the stated generators, and checks thirty affine-chart Gröbner unit ideals. It also checks the field moduli. The computed surviving masks and orbit representatives, *not a manually supplied polynomial list*, are authoritative for the mask convention. Additional exact checks confirm that the ten **correctly transcribed** representative equations vanish at all seven rational points and that all thirty chart-wise derivative ideals are the unit ideal. The finite extension cutoff is only an exclusion technique; it is never assumed to give a general bound on the degrees of singular points. This proof does not classify abstract curve isomorphisms, nor curves over other finite fields.

## Relationship to earlier work

Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (2023), investigate the natural \(q+3\) regime and construct relevant families, but the examined theorems do not give a complete rational-projective census over \(\mathbb F_2\). Homma and Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, arXiv:0903.1918 (2009), address degree \(q+2\), which is degree four at \(q=2\). Neither statement implies the ten-orbit quintic census. This is a best-of-knowledge originality judgment, not a claim that all historical tables have been inspected.
