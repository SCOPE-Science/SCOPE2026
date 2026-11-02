# Rational bitangent-contact spectrum of smooth Ciani quartics over \(\mathbb F_5\)

## Finding

For the complete six-monomial Ciani family

\[F_{A,B,C,D,E,F}(X,Y,Z)=AX^4+BY^4+CZ^4+DX^2Y^2+EX^2Z^2+FY^2Z^2\]

over \(\mathbb F_5\), take coefficient sextuples modulo simultaneous multiplication by a nonzero scalar, with no further identification under coordinate changes. Among its exactly 800 geometrically smooth members, define the **bitangent-contact signature** \((h,r,s)\): the numbers of \(\mathbb F_5\)-rational lines cutting twice a quadratic divisor whose support, respectively, is one double point (a hyperflex), two distinct \(\mathbb F_5\)-points, or a conjugate pair over \(\mathbb F_{25}\). The complete distribution is:

| \(h\) | \(r\) | \(s\) | Number of equations |
| ---: | ---: | ---: | ---: |
| 0 | 0 | 0 | 126 |
| 0 | 0 | 2 | 120 |
| 0 | 2 | 0 | 168 |
| 2 | 0 | 0 | 72 |
| 0 | 0 | 4 | 28 |
| 0 | 2 | 2 | 48 |
| 0 | 4 | 0 | 72 |
| 2 | 0 | 2 | 24 |
| 4 | 0 | 0 | 30 |
| 2 | 0 | 4 | 36 |
| 2 | 2 | 2 | 24 |
| 2 | 4 | 0 | 12 |
| 0 | 2 | 6 | 24 |
| 8 | 0 | 0 | 9 |
| 0 | 0 | 16 | 7 |

Thus the number \(b=h+r+s\) of rational bitangent lines has the exact frequency distribution

\[b=0,2,4,6,8,16:\qquad 126,360,202,72,33,7.\]

In particular, the maximum over the stated family is \(16\); precisely seven scalar-normalized coefficient sextuples attain it, and all sixteen contact pairs for each are nonsplit (there are no rational curve points). In the coefficient order \((A,B,C,D,E,F)\), these seven sextuples are

\[(1,1,1,0,0,0),\ (1,1,3,1,0,0),\ (1,1,3,4,0,0),\]
\[(1,2,2,0,0,2),\ (1,2,2,0,0,3),\ (1,3,1,0,1,0),\ (1,3,1,0,4,0).\]

This is a classification of equations in the marked Ciani coordinate family, **not** a classification up to \(\mathbb F_5\)-isomorphism, nor a statement about every plane quartic.

## Assumptions and scope

Work over \(k=\mathbb F_5\). A sextuple is normalized by dividing all coefficients by its first nonzero coefficient, so each projective parameter has exactly one representative. A **rational bitangent** is a line \(L\) defined over \(k\) for which the degree-four scheme \(L\cap C\) equals \(2D\) after geometric base extension, for a degree-two effective divisor \(D\). This includes hyperflexes. Since \(k\) is perfect, the contact divisor \(D\) descends to \(k\); its binary quadratic has discriminant zero, nonzero square, or nonsquare, giving the three signature types. A smooth plane quartic is geometrically integral of genus three and has twenty-eight geometric bitangents in characteristic five.

## Proof

**Geometric smoothness criterion.** Write \(a=A,b=B,c=C,d=D,e=E,f=F\). The gradient is

\[\frac{\partial F}{\partial X}=2X(2aX^2+dY^2+eZ^2),\]

and likewise cyclically. If only one homogeneous coordinate is nonzero, a singularity occurs exactly when a corresponding one of \(abc\) vanishes. On a coordinate axis, a singularity with two nonzero coordinates occurs precisely when one of \(d^2-4ab\), \(e^2-4ac\), or \(f^2-4bc\) vanishes. For three nonzero coordinates the squared coordinates must lie in the kernel of

\[M=\begin{pmatrix}2a&d&e\\d&2b&f\\e&f&2c\end{pmatrix}.\]

When the three axis discriminants are nonzero, any nonzero vector of \(\ker M\) has three nonzero entries: otherwise the two active equations produce a vanishing axis discriminant. Every nonzero element in an algebraically closed field has a square root. Thus the curve is geometrically smooth if and only if \(abc\ne0\), all three axis discriminants are nonzero, and \(\det M\ne0\). This is an exact algebraic criterion, not a rational-point smoothness test.

**Exact finite classification.** There are \((5^6-1)/4=3906\) scalar-normalized sextuples. Enumerating them by the preceding criterion gives exactly \(800\) smooth ones. Every \(k\)-line is uniquely represented by one of the 31 normalized nonzero triples \([u:v:w]\) in the dual projective plane. Fix an explicit \(k\)-basis \(U,V\) for that line. Restrict the quartic to a binary quartic \(R(U,V)\). It cuts an even geometric divisor if and only if its projective coefficient vector equals the square of a nonzero binary quadratic \(Q(U,V)\) up to scalar. Over \(k\), the quadratic Veronese map

\[[\alpha:\beta:\gamma]\longmapsto[\alpha^2:2\alpha\beta:\beta^2+2\alpha\gamma:2\beta\gamma:\gamma^2]\]

has exactly 31 distinct projective images; these are all the possibilities. The discriminant \(\beta^2-4\alpha\gamma\) distinguishes the three contact types. Looping through all \(800\) smooth coefficient sextuples and all \(31\) rational lines produces precisely the table above. Consequently all totals and the sharp maximum follow, with no probabilistic or partial-enumeration step. The seven maximum sextuples are listed above; direct substitution on the 31 rational projective points establishes that each is pointless over \(k\).

The attached verifiers implement independent arithmetic routes: `verify_modular.py` uses this determinant criterion and the projective quadratic Veronese test, whereas `verify_independent.py` tests geometric smoothness by chartwise Gröbner bases and tests bitangency by factoring the restricted binary quartics. Both exhaust the full parameter space and reproduce all fifteen signature frequencies.

## Verification

With Python 3, run `python3 verify_modular.py` (standard library only) and `python3 verify_independent.py` (requires SymPy). Successful runs end with `MODULAR_VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. The complete exact data are `spectrum.csv` and `extremizers.csv`. Neither script relies on random samples, floating point, external databases, or network requests. The proof of the geometric smoothness criterion and the equivalence of the Veronese test to the bitangent definition are independent of the enumeration.

## Relationship to prior work

Janasz–Pokora–Zieliński (2023) studies geometric line arrangements of bitangents, including complex Ciani pencil members. Bethea–Brazelton (2024) determines automorphism-group orbit structures of the twenty-eight complex bitangents for symmetric quartic types, including Ciani forms. Neither inspected full-text analysis yields the fixed-coordinate \(\mathbb F_5\) bitangent-contact signature frequencies. Betten–Kaplan–Karaoglu's posted finite-field quartic tables begin with \(\mathbb F_9\), not \(\mathbb F_5\). Earlier classifications of **pointless** quartics over \(\mathbb F_5\) and a known count of the 800 smooth Ciani equations do not furnish this entire contact-type distribution over the whole Ciani family: the former treats isomorphism classes with no rational points, whereas the latter does not distinguish bitangent rationality. The Fermat quartic's sixteen rational bitangents are pre-existing; their presence is not claimed as a new individual example.

## Limitations

This finite-field census addresses scalar-normalized equations in fixed Ciani coordinates, not abstract isomorphism classes, all quartic equations, or the distribution over other fields. An earlier unindexed computational table could overlap some or all of the counts. The verifiers are independently implemented computations but independent *external* mathematical validation has not been performed. The result does not classify full Frobenius orbit structures of all 28 geometric bitangents, only rational lines and their contact splitting.

## References

- Marek Janasz, Piotr Pokora and Marcin Zieliński, *On arrangements of smooth plane quartics and their bitangents*, first public 2023-08-31, arXiv:2308.16514, https://arxiv.org/abs/2308.16514.
- Candace Bethea and Thomas Brazelton, *Bitangents to symmetric quartics*, first public 2024-10-11, arXiv:2410.09242, https://arxiv.org/html/2410.09242v1.
- Anton Betten, Nathan Kaplan and Fatma Karaoglu, *Classification of Quartic Curves Over Small Finite Fields*, 2021-10-29, https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html.
