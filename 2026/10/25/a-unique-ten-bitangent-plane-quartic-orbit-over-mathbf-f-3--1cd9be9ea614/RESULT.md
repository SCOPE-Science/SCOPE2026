# A unique ten-bitangent plane quartic orbit over \(\mathbf F_3\)

## Finding
For a geometrically smooth plane quartic \(C/\mathbf F_3\), let \(b(C)\) count rational projective lines whose intersection divisor with \(C\) is twice a degree-two geometric divisor. The count includes lines with contact order four at a hyperflex. **If \(b(C)\geq8\), then \(b(C)=10\)**, and \(C\) is \(\mathbf F_3\)-projectively equivalent to
\[
X^3Z-XZ^3+Y^4-Y^2Z^2+Z^4=0.
\]
The equivalence class contains exactly 312 scalar-normalized equations in fixed homogeneous coordinates, with a projective stabilizer of order 18. Every such curve has exactly one rational point, and the three rational lines which are not bitangents form a pencil at that point. In particular, no smooth ternary quartic over \(\mathbf F_3\) has 8, 9, 11, 12 or 13 rational bitangents.

## Assumptions and scope
Work throughout over the field \(k=\mathbf F_3\); geometric smoothness means smoothness after extension to an algebraic closure. All 13 rational projective lines are considered. A line \(L\) is an \(k\)-rational bitangent of a smooth quartic if the quartic restricts to the line as a **nonzero scalar multiple of a square** of a binary quadratic over \(k\). This is equivalent to the geometric intersection divisor being \(2D\) for a \(k\)-rational effective divisor \(D\) of degree two; its geometric support may be conjugate, and a double point of \(D\) yields a hyperflex. The zero polynomial is excluded: its occurrence would mean the line is a component, impossible for a smooth plane quartic.

The theorem is about rational bitangent **lines**, not necessarily individual rational contact points and not geometric bitangents over arbitrary extensions. Projective equivalence means the action of \(\operatorname{PGL}_3(k)\) on equations, modulo \(k^\times\)-scaling.

## Proof
**1. Exhaustive candidate space.** Use the 15 monomials \(X^iY^jZ^h\) with \(i+j+h=4\), ordered with \(i\) descending and then \(j\) descending. Each nonzero coefficient vector is normalized so that its first nonzero coefficient equals 1. Hence the complete search contains
\[
\sum_{i=0}^{14}3^{14-i}=\frac{3^{15}-1}{2}=7,174,453
\]
quartic equations up to scalar.

**2. Rational line restrictions.** Enumerate 13 normalized \(k\)-points in the dual plane. On every rational line, select the first two distinct normalized points \(u,v\) on the line. Restrict each monomial by substituting \((X,Y,Z)=su+tv\), obtaining a 5-by-15 matrix. In the resulting five-dimensional binary quartic coefficient space, the 26 distinct nonzero scalar multiples of squares of binary quadratics are enumerated directly from all 26 nonzero quadratics. Membership in this 26-element set determines the bitangent predicate exactly.

The complete enumeration, implemented in `enumerate.cpp` using the matrices built in `build_restrictions.py`, yields the following histogram (number of bitangents: number of scalar-normalized equations): 0:1,355,341; 1:3,141,762; 2:1,709,760; 3:633,776; 4:208,182; 5:87,750; 6:25,740; 7:9,360; 8:1,404; 9:702; 10:312; 11:78; 12:13; 13:273. These add to 7,174,453. The program writes **all** 2,782 coefficient vectors with at least eight rational bitangents to `high_forms.tsv`, which is included as a finite checkable certificate.

**3. Complete projective orbit reduction.** Substitution by five explicit invertible three-by-three matrices generates the entire \(\operatorname{PGL}_3(\mathbf F_3)\), of order 5,616 (checked separately in `group_check.py`). Their induced transformations on coefficient vectors partition all 2,782 high-bitangent equations into seven disjoint orbits. Each orbit representative is specified by its 15-digit ternary coefficient vector; the triples below are (number of bitangents, orbit size, normalized coefficient vector):

| Bitangents | Orbit size | Coefficients | Geometrically smooth? |
| ---: | ---: | --- | --- |
| 13 | 39 | `000000000010201` | No |
| 13 | 234 | `000001010010000` | No |
| 12 | 13 | `000000000000001` | No |
| 11 | 78 | `000000000000100` | No |
| 10 | 312 | `001000000210201` | Yes |
| 9 | 702 | `000010000011211` | No |
| 8 | 1,404 | `000001000010200` | No |

The six non-smooth representatives are singular at \([1:0:0]\), as immediate direct substitution into the form and all first partials verifies. Since projective substitution preserves geometric smoothness, their complete orbits are singular.

**4. Smoothness of the remaining orbit.** Its representative is
\[F=X^3Z-XZ^3+Y^4-Y^2Z^2+Z^4.\]
In characteristic three its three partial derivatives simplify to
\[F_X=-Z^3,\qquad F_Y=Y^3+YZ^2,\qquad F_Z=X^3+Y^2Z+Z^3.\]
If all three vanish over the algebraic closure, then \(Z=0\) from \(F_X=0\), then \(Y=0\), then \(X=0\), which is not a projective point. Thus \(F\) is geometrically smooth. The orbit therefore consists of exactly 312 geometrically smooth high-bitangent equations, and no other smooth form has at least eight rational bitangents. Orbit-stabilizer gives stabilizer size \(5616/312=18\).

**5. Rational incidence geometry.** Direct substitution in the 13 normalized points shows that the representative has only \([1:0:0]\) as a rational curve point. The 13 rational line restrictions identify exactly three nonbitangent lines: \(Y=0\), \(Y+Z=0\), and \(Y-Z=0\). All pass through \([1:0:0]\), and the remaining ten rational lines are bitangents. This is preserved under projective equivalence.

## Verification
The included source files reconstruct restrictions from scratch, enumerate every projectively normalized coefficient vector, preserve the 2,782 high-bitangent vectors, independently recalculate the restriction-square predicates on all seven orbit representatives, check the orbit partition, confirm the group order, and perform Jacobian Gröbner-basis checks on every affine chart. A second direct derivative argument above proves smoothness without relying on the computer algebra library. For a clean reproduction using Python 3, SymPy and a C++17 compiler, execute in the directory containing the included files:

```
python3 build_restrictions.py > setup_log.txt
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate > census_log.txt
python3 orbit_check.py > orbit_log.txt
python3 group_check.py > group_log.txt
python3 verify.py > verification_log.txt
```

The finite computations are exhaustive only for \(k=\mathbf F_3\). They are not claims about larger fields or higher degrees.

## Relationship to prior work
Bergvall's 2021 paper on arithmetic and topology of structures associated to plane quartics develops marked-bitangent moduli and arithmetic point counts. His 2022 paper gives Frobenius-class counts for degree-two del Pezzo surfaces, which are double covers branched along smooth quartics; via the 28 odd theta characteristics, these counts may already imply parts of a rational-bitangent **numerical** distribution. The present statement is the explicit fixed-coordinate high-contact projective-orbit classification together with its stabilizer and three-line incidence complement. Neither inspected article states this explicit unique ternary quartic orbit or the complement-pencil configuration. The counts alone should not be presented as independently novel from Frobenius-enumeration theory.

Oyono and Ritzenthaler study quartic line intersections, flexes and rationality constraints more broadly, but do not give this explicit characteristic-three high-bitangent orbit census.

## Limitations
The rational-bitangent **maximum and gap**, the unique high-bitangent projective orbit and its incidence arrangement are established by finite exhaustive enumeration. A prior equivalence hidden in unindexed tables or specialized classifications cannot be excluded. Weighted counts of Frobenius classes require careful comparison before claiming the 312-equation number new independently. This result does not classify quartics with seven or fewer rational bitangents or their abstract automorphism groups, and no independent external review has been performed.

## References
O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072 (first public 2021-06-24), https://arxiv.org/abs/2106.13072.

O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855 (first public 2022-11-23), https://arxiv.org/abs/2211.12855.

R. Oyono and C. Ritzenthaler, *On rationality of intersection points of a line with a plane quartic*, arXiv:1006.0873 (2010), https://arxiv.org/abs/1006.0873.
