# Proper rational tritangent spectrum of canonical genus-four curves on the nonsplit binary quadric

## Finding

Let \(Q\subset\mathbf P^3_{\mathbf F_2}\) be the smooth nonsplit quadric \(x_0x_1+x_2^2+x_2x_3+x_3^2=0\). A geometrically smooth intersection \(C=Q\cap\{F=0\}\) with \(F\) cubic is a canonical genus-four curve. A rational hyperplane \(H\) is a **proper tritangent** if its intersection divisor on \(C\) is \(2D\), with \(D\) a reduced geometric divisor of degree three.

Among the \(65\,535\) nonzero cubic sections of \(\mathcal O_Q(3)\), exactly \(27\,060\) yield smooth curves. Their proper rational tritangent counts \(\tau\) are **completely classified**:

| \(\tau\) | Smooth sections | Projective orbits |
|---:|---:|---:|
| 0 | 10,300 | 96 |
| 1 | 12,810 | 120 |
| 2 | 3,600 | 32 |
| 3 | 350 | 6 |
| **Total** | **27,060** | **254** |

In particular, \(\tau(C)\leq3\), with equality for exactly \(350\) sections constituting six orbits under \(\operatorname{Aut}_{\mathbf F_2}(Q)\cong S_5\). Let \(a\) count proper tritangents from the ten rational planes cutting \(Q\) in smooth conics, and \(b\) those from the five rational planes tangent to \(Q\). The **complete joint spectrum** by \((\#C(\mathbf F_2),a,b)\), containing 33 occurring triples, is given in `expected.json` and `orbit_certificate.tsv`. Among the \(396\) smooth sections containing all five rational points of \(Q\), none has three proper rational tritangents (their total-tritangent counts are 0 for 96 sections, 1 for 60, and 2 for 240).

## Assumptions and scope

All fields have characteristic two and the ground field is exactly \(\mathbf F_2\). Sections are nonzero elements in the sixteen-dimensional quotient \(H^0(\mathbf P^3,\mathcal O(3))/(Q\cdot H^0(\mathbf P^3,\mathcal O(1)))\); scalar equivalence is trivial over \(\mathbf F_2\). Projective orbits are under the \(120\)-element group of rational automorphisms of the fixed nonsplit quadric, **not** abstract isomorphism classes of curves. Smoothness and distinctness of tritangent contacts are geometric, over an algebraic closure. A plane is counted only when defined over \(\mathbf F_2\), while contact points need not be rational. A plane with nonreduced support of fewer than three contacts is excluded.

## Proof

The five rational points of \(Q\) form a projective frame. Each permutation uniquely determines a linear projective transformation preserving the quadric, giving \(\operatorname{Aut}_{\mathbf F_2}(Q)\cong S_5\). Representatives of cubic sections use the sixteen cubic monomials not containing both \(x_0\) and \(x_1\), reducing all other monomials with \(x_0x_1=x_2^2+x_2x_3+x_3^2\). The transposition and five-cycle generators yield exactly 683 orbits on the \(65\,535\) nonzero coefficient masks; the orbit sizes sum to \(65\,535\).

Since \(Q\) is smooth, \(C\) is geometrically singular precisely when the homogeneous ideal consisting of \(Q\), \(F\), and the six \(2\times2\) minors of their Jacobian has a projective point over the algebraic closure. The three charts \(x_0=1\), \(x_1=1\), and \(x_2=1\) cover \(Q\). The affine ideal-unit criterion, computed by an explicit Buchberger algorithm over \(\mathbf F_2\), detects singularity exactly (not by point sampling). Applying it to all 683 orbit representatives leaves 254 geometrically smooth orbits, with summed size \(27\,060\).

For a rational plane cutting \(Q\) in a smooth conic, pull the cubic section back along a quadratic parametrization of that conic. This gives a binary sextic \(f(s,t)\). It is a square of a **squarefree** binary cubic exactly when its odd-index coefficients vanish and the square-root cubic \(a s^3+b s^2t+c st^2+d t^3\) has discriminant \(ad+bc=1\) in \(\mathbf F_2\). This is exactly the proper-tritangent condition. There are ten such planes.

Each of the other five rational planes is tangent to \(Q\) at a rational point \(P\) and its section splits over \(\mathbf F_4\) into conjugate lines through \(P\). On either line write the cubic restriction as \(a s^3+b s^2t+c st^2+d t^3\), with \(P\) represented by \(t=0\). The rational tangent plane is a proper tritangent exactly when \(a=0\), \(b\ne0\), and \(c=0\): its intersection divisor is twice the rational point \(P\) plus twice each of two conjugate non-\(P\) geometric points. The converse follows from the unique intersection of the two ruling lines at \(P\).

Applying these two exact contact tests to each of the 254 smooth orbits yields the complete joint spectrum certified in `orbit_certificate.tsv`. Their orbit-weighted multiplicities give the stated \(\tau\) distribution. The six extremal orbit representatives, in the documented monomial-mask convention, are `217c`, `2286`, `22a0`, `2364`, `28ad`, and `8276` (hexadecimal); their orbit sizes are 60, 60, 120, 30, 60, and 20, respectively. Two notably different extremal types occur: `217c` has three quadric-tangent-plane tritangents and three rational curve points, whereas `8276` has three smooth-conic-plane tritangents and **no** rational curve points.

## Verification

Run `python verify.py` using Python 3, with the accompanying four exact inputs `nonsplit_genus4.py`, `groebner_gf2.py`, `tritangents.py`, `orbit_certificate.tsv`, and `expected.json` in the same directory. No third-party package is required. The checker reconstructs all 683 orbits, repeats all exact affine ideal tests, checks the saved row for every orbit, and retests the tritangent counts on **each of the 27,060 smooth equations**, not solely on representatives. It verifies all 33 occurring joint triples, all six extremal orbits, and the five-rational-point stratum. Separate symbolic Groebner and alternative parametrization checks agreed with the exact standalone checker; those additional checks are not required to replay the embedded evidence.

## Relationship to prior work

Xarles's genus-four census establishes a complete classification of abstract genus-four curves over \(\mathbf F_2\) and publishes equations and extension-field point counts. Its associated public Magma code and data were inspected; their stated invariants are geometric models, Jacobian point counts, and isomorphism classes, not the proper-rational-tritangent contact spectrum or the joint \((\#C(\mathbf F_2),a,b)\) distribution here. Bergström–Faber–Payne analyze finite-field point counts of moduli spaces and the nonsplit-quadric case, with marked-point counts but not this tritangent contact decomposition. Kulkarni–Ren–Sayyary Namin–Sturmfels establish a tritangent framework for space sextics over the real numbers, not this binary characteristic-two finite-field census. The already established smooth **split** quadric tritangent count is a different embedded problem and does not imply the nonsplit spectrum. The orbit counts alone are not offered as a novel abstract-curve census.

## Limitations

The theorem applies only to the fixed nonsplit quadric over \(\mathbf F_2\), its cubic sections, and **proper** rational tritangents. It says nothing about tangent planes defined only over extensions, nonproper even-contact hyperplanes, or all genus-four curves over larger fields. Exact finite enumeration is a complete proof here because every parameter and orbit is finite and enumerated, but the computation has only the provided same-authority reproducibility review, not an independent mathematical audit. The earlier literature may contain unpublished or unindexed equivalent contact tables, so bibliographic priority requires external confirmation. The numbers count embedded equations, not abstract isomorphism classes.

## References

1. M. Kulkarni, Y. Ren, M. Sayyary Namin, B. Sturmfels, *Real Space Sextics and their Tritangents* (2017), arXiv:1712.06274.
2. X. Xarles, *A census of all genus 4 curves over the field with 2 elements* (2020), arXiv:2007.07822; computational data at https://github.com/XavierXarles/Censusforgenus4curvesoverF2.
3. J. Bergström, C. Faber, S. Payne, *Polynomial point counts and odd cohomology vanishing on moduli spaces of stable curves* (2022), arXiv:2206.07759.
