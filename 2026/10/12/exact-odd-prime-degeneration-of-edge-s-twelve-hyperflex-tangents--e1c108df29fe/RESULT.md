# Exact odd-prime degeneration of Edge's twelve hyperflex tangents

## Finding

Let the **Edge quartic** be the integral plane curve
\[
C: X^4+Y^4+Z^4+3(X^2Y^2+X^2Z^2+Y^2Z^2)=0.
\]
Its twelve characteristic-zero hyperflex tangent lines form a natural arrangement \(\mathcal A\). The following table classifies the **reduced arrangement** after specialization to every odd characteristic. A geometric point of multiplicity \(r\) lies on exactly \(r\) distinct reduced components.

| Characteristic | Distinct lines | Double points | Quadruple points | All intersection points |
| --- | ---: | ---: | ---: | ---: |
| \(p\ge7\) | 12 | 66 | 0 | 66 |
| \(p=3\) | 12 | 30 | 6 | 36 |
| \(p=5\) | 4 | 6 | 0 | 6 |

There are no points of any other intersection multiplicity in the specified range. In particular, the **only exceptional odd primes** for the geometric incidence lattice of this fixed integral configuration are \(3\) and \(5\).

For the rational intersection points and rational reduced lines over \(\mathbb F_p\), the complete count is

| Condition | Rational intersection points | Rational component lines |
| --- | ---: | ---: |
| \(p\ge7\), \(p\equiv1\pmod4\) | 66 | 12 |
| \(p\ge7\), \(p\equiv3\pmod4\) | 6 | 0 |
| \(p=3\) | 6 | 0 |
| \(p=5\) | 6 | 4 |

## Assumptions and scope

Write \(i^2=-1\). Lines are defined over \(\mathbb Z[i]\) by the following **ordered, primitive coefficient vectors** for \(aX+bY+cZ=0\):
\[
\begin{array}{rrrr}
(2i,1,-1),&(-2i,1,-1),&(-1,2i,1),&(-1,-2i,1),\\
(1,-1,2i),&(1,-1,-2i),&(-2i,1,1),&(2i,1,1),\\
(1,-2i,1),&(1,2i,1),&(1,1,-2i),&(1,1,2i).
\end{array}
\]
For each odd rational prime \(p\), choose either image of \(i\) in \(\overline{\mathbb F}_p\); the two choices permute this set of twelve lines, so all assertions are independent of the choice. The reduction is of the *specified integral model*; when multiple labeled lines become equal, counts use their reduced support, not repeated labeled components.

These vectors are the gradients divided by four at the twelve points
\[
\begin{array}{rrrr}
(i,1,-1),&(-i,1,-1),&(-1,i,1),&(-1,-i,1),\\
(1,-1,i),&(1,-1,-i),&(-i,1,1),&(i,1,1),\\
(1,-i,1),&(1,i,1),&(1,1,-i),&(1,1,i).
\end{array}
\]
All twelve points and their tangents were given in the originating literature. The present claim concerns the reduction of this explicitly specified tangent-line arrangement, not the classification of all positive-characteristic hyperflexes or arbitrary models.

## Proof

**1. Integrity of the tangent equations.** For
\[
F=X^4+Y^4+Z^4+3(X^2Y^2+X^2Z^2+Y^2Z^2),
\]
the first partial derivative in \(X\) is \(4X^3+6X(Y^2+Z^2)\), with cyclic permutations for the others. Substitution of each displayed point gives \(F=0\) and precisely four times the corresponding displayed line vector as the gradient. In characteristic zero the vectors are nonzero and define the twelve hyperflex tangents described by Edge and by Dimca–Ilardi–Pokora–Sticlaru.

**2. All-prime obstruction from determinants.** For each of the \(\binom{12}{3}=220\) unordered triples of distinct line vectors, take its determinant \(d\in\mathbb Z[i]\) and Gaussian norm \(N(d)=d\overline d\in\mathbb Z\). An exact, exhaustive evaluation gives

| \(N(d)\) | 4 | 20 | 36 | 40 | 64 | 80 | 100 | 200 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Frequency | 8 | 48 | 24 | 24 | 12 | 48 | 48 | 8 |

Every determinant is nonzero, and every displayed norm has prime divisors in \(\{2,3,5\}\) only. If a triple were concurrent after reduction at a rational prime \(p\ge7\), its determinant would vanish at a prime of \(\mathbb Z[i]\) above \(p\); hence \(p\) would divide its norm, a contradiction. A coincident pair of lines also forces such a triple for any third line; hence all twelve remain distinct. Every pair now meets at its own point and no three meet: there are \(\binom{12}{2}=66\) ordinary double points in every such characteristic. This is a proof for *all* primes at least seven, not an extrapolation from sample fields.

**3. The six quadruple points in characteristic three.** Here \(\mathbb F_9=\mathbb F_3(i)\) with \(i^2=-1\). The twelve reduced lines are pairwise distinct by their explicit coordinates. Substitution shows that each of the six points
\[
[1:i:0],\ [1:-i:0],\ [1:0:i],\ [1:0:-i],\ [0:1:i],\ [0:1:-i]
\]
is incident to exactly four component lines, and these six quadruple incidences use \(6\binom 43=24\) distinct concurrent triples. The determinant-norm table shows exactly 24 of the 220 determinants vanish modulo three: precisely those of norm \(36\). Therefore there are no further triple concurrences. The quadruple points account for \(6\binom42=36\) of the 66 line pairs, leaving 30 pairs that meet in distinct ordinary double points. Thus the geometric spectrum is exactly six quadruple and thirty double points. The six quadruple points are not \(\mathbb F_3\)-rational.

**4. The four-line degeneration in characteristic five.** In \(\mathbb F_5\), choose \(i=2\). The twelve ordered vectors reduce to the following four projective lines, with the indicated sets of three original labels:

| Reduced equation | Original labels |
| --- | --- |
| \(X-Y+Z=0\) | 1, 6, 10 |
| \(X+Y-Z=0\) | 2, 3, 12 |
| \(X-Y-Z=0\) | 4, 5, 8 |
| \(X+Y+Z=0\) | 7, 9, 11 |

The other embedding permutes these four groups. Direct multiplication shows in \(\mathbb F_5[X,Y,Z]\) that
\[
F=(X+Y+Z)(X+Y-Z)(X-Y+Z)(X-Y-Z).
\]
The four lines are in general position, having exactly six distinct rational double points. Thus the reduced arrangement coincides with the four-component reduction of the original quartic at five.

**5. Rationality.** If \(p\ge7\) and \(p\equiv1\pmod4\), then \(i\in\mathbb F_p\), so every line and every one of its 66 pair intersections is rational. For \(p\ge7\) with \(p\equiv3\pmod4\), the twelve lines form six nontrivial Frobenius-conjugate pairs, with none rational. In an arrangement with no triple point, a Frobenius-fixed intersection must be defined by a conjugate pair; those six intersections are distinct and rational, while no others are. In characteristic three, the six displayed nonrational quadruple points leave six rational double intersections, obtained from the six conjugate pairs; a direct \(\mathbb F_9\) incidence enumeration independently verifies this count. The characteristic-five four lines and six double intersections are all rational.

## Verification

Run `python3 verify.py` with a standard Python interpreter. This standalone file derives the twelve lines from the gradients at the listed points, enumerates the 220 Gaussian determinants and norms, performs complete incidence enumeration in \(\mathbb F_9\), and checks reduction over \(\mathbb F_5\) including the factorization. It also checks generic sample primes in the two residue classes. The exact determinant-norm support, not the sample-prime checks, establishes the universal assertion for all primes at least seven. The proof of Frobenius rationality is given above rather than inferred from sampling.

## Relationship to prior work

Edge's 1945 paper constructs the quartic and its twelve undulations. Dimca–Ilardi–Pokora–Sticlaru (Sect. 5, Remark 5.1) recover the twelve tangent lines and record that their characteristic-zero arrangement has only double intersections. Those geometric facts and the equations are inputs, **not novel parts** of the assertion. Pacini–Testa study the same twelve hyperinflection lines and their projective stabilizer, including a different exceptional phenomenon in characteristic thirteen; their results concern reconstruction/stabilizer, not the reduced incidence spectrum and prime-field point counts established here. Janasz–Pokora–Zieliński study the different arrangement of all 28 bitangents of related quartics, rather than these twelve hyperflex tangents. The new statement specifies the two bad odd primes, both degeneration schemes, and the complete rational-intersection spectrum for the fixed integral twelve-line arrangement.

## Limitations

Characteristic two is excluded. The theorem refers to this integral model, not all projective twists or every positive-characteristic quartic with twelve hyperflexes. In characteristic five the original quartic itself is reducible; the line arrangement is counted as a reduced union. No claim about freeness, scheme-theoretic moduli of tangent configurations, or all positive-characteristic hyperflexes is made.

## References

1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117 (first public 3 January 2023), *Results in Mathematics* 79 (2024), 11, DOI:10.1007/s00025-023-02036-9; Sect. 5, especially Remark 5.1. https://arxiv.org/abs/2301.01117
2. M. Pacini, D. Testa, *Plane quartics with at least 8 hyperinflection points*, arXiv:1301.1865 (2013); Sect. 2, proof for the quartics \(F\) and \(K\). https://arxiv.org/abs/1301.1865
3. W. L. Edge, *A plane quartic curve with twelve undulations*, *Edinburgh Mathematical Notes* 35 (1945), 10–13, DOI:10.1017/S0950184300000197. The accessible journal extract was consulted; full historical text was not available for inspection.
4. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514 (2023), DOI:10.4064/fm240105-13-12. https://arxiv.org/abs/2308.16514
