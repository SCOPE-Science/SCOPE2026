# First failure of simultaneous prime-ideal balance in \(\mathbb Z[\omega]\)

## Finding
Write \(R=\mathbb Z[\omega]\), with \(\omega^2+\omega+1=0\). A finite \(S\subset R\) of cardinality \(n+1\) is **\(n\)-optimal** if for every nonzero prime ideal \(\mathfrak p\) and every \(j\ge1\), the occupancies of all classes in \(R/\mathfrak p^j\) differ by at most one. This is equivalent to testing integer-valued polynomials of degree at most \(n\) on \(S\).

**Theorem.** Such sets exist for \(n=1,2,3,4\), but not for \(n=5\). Thus the first degree lacking an optimal interpolation set over the Eisenstein integers is five. The smallest cardinality of any \(5\)-universal interpolation set is exactly **seven**: six points are impossible by the theorem, while seven suffice by the general theorem of Byszewski, Frączyk and Szumowicz.

## Assumptions and scope
Here \(n\) is a positive integer; \(R\) is the full ring of integers of \(\mathbb Q(\sqrt{-3})\); \(R\) is a principal ideal domain. For \(z=a+b\omega\), use the positive definite norm \(N(z)=a^2-ab+b^2\). The prime ideal \(\mathfrak l=(1-\omega)\) has norm three and \((2)\) is an inert prime ideal of norm four. Reduction modulo \(\mathfrak l\) sends \(a+b\omega\) to \(a+b\pmod3\), while reduction modulo \((2)\) sends it to \((a\bmod2,b\bmod2)\). Almost-uniform distribution means the maximum and minimum among **all** residue classes differ by at most one, including empty classes.

## Proof
**1. Necessary small differences for six points.** Suppose \(S\) is \(5\)-optimal; \(|S|=6\). At any prime ideal of norm \(q\ge6\), all six points must occupy distinct classes, because six occupancies across \(q\) classes must be zero or one. Similarly, all six points must be distinct modulo \(\mathfrak l^2\) (norm nine) and modulo \((2)^2\) (norm sixteen). The only prime ideals with residue norm less than six in \(R\) are \(\mathfrak l\) (norm three) and \((2)\) (norm four). Unique prime-ideal factorization therefore forces every nonzero difference \(z=s-t\) to have \(N(z)\in\{1,3,4,12\}\). Indeed neither of these two prime ideals may occur with exponent at least two, and no other prime may divide \(z\).

**2. Exhaustive finite obstruction.** Translate an arbitrary member of \(S\) to zero. Every other point must belong to
\[
V=\{a+b\omega:N(a+b\omega)\in\{1,3,4,12\}\},
\]
which has exactly twenty-four elements (six for each norm). The identities \(4N=(2a-b)^2+3b^2=(2b-a)^2+3a^2\) show that \(N\le12\) implies \(|a|,|b|\le4\); therefore the verifier's coordinate box \([-5,5]^2\) contains **every** element of \(V\), not merely a sampled neighborhood. Hence every candidate is among the \(\binom{24}{5}=42504\) choices of five distinct nonzero points in \(V\). Retain only those for which every pairwise difference again has norm in \(\{1,3,4,12\}\). The complete executable enumeration in `verify_eisenstein_optimal.py` yields exactly 54 candidates. Modulo translation, multiplication by the six units, and conjugation these reduce to three classes, with rooted multiplicities 12, 36 and 6. For these three classes, the increasing sorted occupancy profiles modulo \(\mathfrak l\) and \((2)\) are respectively:

| Rooted candidates | Three-class occupancy | Four-class occupancy |
| ---: | --- | --- |
| 12 | \((2,2,2)\) | \((1,1,1,3)\) |
| 36 | \((1,2,3)\) | \((1,1,2,2)\) |
| 6 | \((0,3,3)\) | \((0,2,2,2)\) |

An almost-uniform six-point set must have three-class profile precisely \((2,2,2)\) and four-class profile precisely \((1,1,2,2)\). No orbit has both. The finite enumeration is exhaustive because it checks all five-subsets of the proved complete twenty-four-point candidate set; the program constructs no heuristic bounded search region. Thus no \(5\)-optimal set exists.

**3. Existence in degrees one through four.** The following explicit sets, where each \((a,b)\) stands for \(a+b\omega\), give the required witnesses:

| \(n\) | Coordinate pairs in \(S_n\) | Occupancies modulo \(\mathfrak l\) | Occupancies modulo \((2)\) |
| --- | --- | --- | --- |
| 1 | \((0,0),(1,0)\) | \((0,1,1)\) | \((0,0,1,1)\) |
| 2 | \((0,0),(0,1),(1,1)\) | \((1,1,1)\) | \((0,1,1,1)\) |
| 3 | \((0,0),(0,1),(1,2),(1,1)\) | \((1,1,2)\) | \((1,1,1,1)\) |
| 4 | \((0,0),(0,2),(0,1),(1,2),(1,1)\) | \((1,2,2)\) | \((1,1,1,2)\) |

Each pairwise difference in these sets has norm in \(\{1,3,4,12\}\), as checked exactly in the verifier. Consequently, all points are distinct modulo powers \(\mathfrak l^j\) for \(j\ge2\), modulo powers \((2)^j\) for \(j\ge2\), and modulo *every* other prime ideal (already at exponent one). In these larger residue rings the number of classes is at least nine, and there are at most five points, so occupancy is automatically almost uniform. The first-power occupancies in the table complete the proof of optimality.

**4. Exact universal-set minimum in degree five.** A five-universal set must have at least six points by interpolation dimension. A six-point five-universal set would be five-optimal by the established local-global characterization, which step 2 excludes. Theorem 1.3 of Byszewski, Frączyk and Szumowicz supplies an \((n+2)\)-point \(n\)-universal set over every Dedekind domain; taking \(n=5\) gives a seven-point set. Thus the minimum is seven.

## Verification
The standalone Python 3 standard-library program `verify_eisenstein_optimal.py` independently calculates norms and residue profiles, generates the entire twenty-four-point necessary set, examines **all 42,504** five-subsets containing the translated origin, verifies exactly 54 pairwise-compatible six-point candidates, independently canonicalizes them under the twelve dihedral ring symmetries and translations, and checks the three orbit profiles and four explicit optimal witnesses. It returns `VERIFY_OK`. The finite check is an exhaustive decidable subproblem after the unbounded global reduction, not a numerical extrapolation to an infinite domain.

## Relationship to prior work
Petrov and Volkov (arXiv:1108.3212, 16 August 2011), Lemma 1 and their introduction, established the prime-power almost-uniform criterion for Gaussian integers, asymptotic nonexistence there, and the distinct Gaussian phenomenon: four-optimal sets fail but five-optimal sets exist. Byszewski, Frączyk and Szumowicz (arXiv:1506.02696, 2015), Proposition 2.6 and Theorems 1.2–1.3, extended the criterion and large-degree nonexistence to arbitrary imaginary quadratic integer rings, and proved the general \(n+2\) universal upper bound. Neither inspected primary full text determines the **first** failure or the exact degree-five universal minimum for \(\mathbb Z[\omega]\). This paper supplies the sharp Eisenstein finite obstruction, not the local criterion or upper bound.

## Limitations
The theorem settles optimality only in degrees one through five; it does **not** assert that optimality fails for every degree beyond five. The 54-candidate census is exhaustive only for the rigorously reduced six-point problem, not for sets of arbitrary size. The seven-point upper bound is quoted from existing literature rather than independently constructed here. Equivalent treatment in unlocated literature remains possible.

## References
1. F. Petrov and V. Volkov, *On the interpolation of integer-valued polynomials*, arXiv:1108.3212 (first posted 2011-08-16), especially Lemma 1 and §1.
2. J. Byszewski, M. Frączyk and A. Szumowicz, *Simultaneous p-orderings and minimising volumes in number fields*, arXiv:1506.02696 (2015 preprint), especially Proposition 2.6, Theorems 1.2 and 1.3.
