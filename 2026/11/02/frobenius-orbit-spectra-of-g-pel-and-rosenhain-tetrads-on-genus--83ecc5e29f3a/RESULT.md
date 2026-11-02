# Frobenius orbit spectra of Göpel and Rosenhain tetrads on genus-two Jacobian Kummer quartics

## Finding
Let \(k=\mathbb F_q\) have odd characteristic, and let \(C/k\) be a smooth genus-two hyperelliptic curve with a squarefree degree-six model \(y^2=f(x)\). Let \(\sigma\in S_6\) denote the arithmetic Frobenius permutation of its six geometric Weierstrass points; only its cycle type \(\lambda\) matters. Write \(K\) for the associated Jacobian Kummer quartic, whose sixteen nodes are indexed by \(J(C)[2]\). Let \(\mathcal G\) and \(\mathcal R\) be the respective finite étale \(k\)-schemes of unordered four-node Göpel and Rosenhain tetrads: their geometric points are respectively the \(60\) translates of maximal isotropic \(2\)-subspaces and the \(80\) translates of nonisotropic \(2\)-subspaces of the symplectic space \(J(C)[2]\cong\mathbb F_2^4\).

**The full Frobenius orbit distributions on both tetrad schemes, for every odd \(q\), depend only on \(\lambda\) and are given by the following exhaustive table.** In a cell \(d:c\) means precisely \(c\) disjoint Frobenius cycles of length \(d\), so \(d=1\) counts \(k\)-rational tetrads.

| \(\lambda\) | Göpel cycles (60 tetrads) | Rosenhain cycles (80 tetrads) |
|:--|:--|:--|
| \((6)\) | 1:1, 2:1, 3:5, 6:7 | 2:1, 6:13 |
| \((5,1)\) | 5:12 | 5:16 |
| \((4,2)\) | 1:2, 2:3, 4:13 | 2:4, 4:18 |
| \((4,1,1)\) | 1:2, 2:3, 4:13 | 2:4, 4:18 |
| \((3,3)\) | 1:3, 3:19 | 1:2, 3:26 |
| \((3,2,1)\) | 3:4, 6:8 | 1:3, 2:1, 3:7, 6:9 |
| \((3,1,1,1)\) | 3:20 | 1:5, 3:25 |
| \((2,2,2)\) | 1:16, 2:22 | 2:40 |
| \((2,2,1,1)\) | 1:8, 2:26 | 1:8, 2:36 |
| \((2,1,1,1,1)\) | 1:12, 2:24 | 1:24, 2:28 |
| \((1,1,1,1,1,1)\) | 1:60 | 1:80 |

For either scheme, if its column contains pairs \((d,c_d)\), its zeta function and extension-field point counts are exactly
\[
Z(\mathcal T/k,T)=\prod_d(1-T^d)^{-c_d},\qquad
\#\mathcal T(\mathbb F_{q^n})=\sum_{d\mid n}d\,c_d.
\]
In particular, the least extension of \(k\) over which **all** Göpel tetrads (or **all** Rosenhain tetrads) become individually defined has degree \(\operatorname{ord}(\sigma)=\operatorname{lcm}(\lambda)\), for both species. Every row is realizable by a squarefree sextic over any odd finite field with \(q\ge7\).

## Assumptions and scope
The characteristic is odd; \(f\in k[x]\) is separable of degree exactly six and defines a smooth genus-two curve. The Kummer quartic arises from the Jacobian with its canonical principal polarization. The tetrads are unordered subsets of four *geometric nodes* and are treated as finite Galois sets, not as components of a potentially nonreduced Hilbert scheme. Rational tetrad means Frobenius stabilizes the unordered four-node subset, **not** that every node in it is separately rational. The two tabulated geometric sizes are always \(60\) and \(80\). At \(q=3\) or \(q=5\), only realizable Weierstrass cycle types occur for a given field, but the table applies to all such types.

## Proof
**1. The exact six-point module.** Label the six branch points \(\{0,1,2,3,4,5\}\). The sixteen two-torsion points of \(J(C)\) are the equivalence classes of even subsets of this set under complementation. Representatives are the empty subset and the fifteen two-element subsets. Addition is symmetric difference followed, when necessary, by complementation back to cardinality at most two. The Weil pairing in additive form is \(\langle A,B\rangle=|A\cap B|\pmod2\). These identifications are compatible with Frobenius, which acts by the underlying permutation of the six branch points.

**2. The tetrad classification.** For two linearly independent classes \(a,b\in J(C)[2]\), the four-point affine plane \(v+\langle a,b\rangle\) is a Göpel tetrad when \(\langle a,b\rangle=0\), and Rosenhain otherwise. There are \(35\) two-dimensional linear subspaces in \(\mathbb F_2^4\), precisely \(15\) isotropic and \(20\) nonisotropic. Each has exactly four affine translates, giving \(60\) Göpel and \(80\) Rosenhain tetrads. Distinct affine planes are distinct four-node subsets. This recovers the classical Kummer geometry, not a new enumeration of the geometric tetrads.

**3. Exhaustive Frobenius classification.** Every permutation in \(S_6\) explicitly permutes the sixteen representatives and therefore the \(140\) affine planes. The attached standard-library verifier exhausts all \(720\) six-point permutations, computes the disjoint cycles on each species, checks the weighted sums \(60\) and \(80\), and confirms that the results are constant on each of the eleven conjugacy classes of \(S_6\). Its output is exactly the eleven rows above, which are independently hard-coded and asserted in the verifier. This is an exhaustive finite proof because every possible Frobenius on the six Weierstrass points belongs to one of these \(720\) permutations; no experiment is extrapolated to infinitely many curves.

A second fixed-point calculation provides a distinct check on every rational count: for any stable linear plane \(U\), the number of Frobenius-stable affine translates is
\[
\frac14\#\{v\in J(C)[2] : \sigma(v)-v\in U\}.
\]
Summing this over the \(\sigma\)-stable isotropic or nonisotropic planes agrees with the direct cycle enumeration for all \(720\) permutations. A separate three-point construction recovers exactly the same \(140\) affine parallelograms. The verifier also checks that the least common multiple of the cycle lengths in each column is the order of \(\sigma\).

**4. Descent and realizability.** A finite Galois set with \(c_d\) cycles of length \(d\) has \(\sum_{d\mid n}dc_d\) points over \(\mathbb F_{q^n}\), giving the stated zeta product. Over a finite field \(\mathbb F_q\) with \(q\ge7\), choose a distinct monic irreducible polynomial for each part of a prescribed partition \(\lambda\) of six; for repeated degree-one factors, at most six distinct linear factors are needed. This yields a separable degree-six polynomial whose Weierstrass Frobenius partition is \(\lambda\). Irreducible polynomials of every positive degree exist over every finite field, and for \(q\ge7\) the required multiplicities also exist. The proof applies uniformly to all odd finite fields, subject only to the existence of the chosen curve.

## Verification
Run `python3 verify.py` using Python's standard library in the same directory as this document. `verification_output.txt` contains an actual successful execution transcript ending with `VERIFY_OK`. The verifier checks the \(16\)-element symplectic module identities, independently constructs the \(140\) planes in two ways, enumerates all \(720\) permutations and eleven conjugacy classes, independently verifies the rational fixed-point counts and their cycle-length lcms, and compares each complete orbit spectrum against the explicit table. No floating-point computations, external solvers, sampled characteristics, or unlisted datasets are involved. The proof still uses the standard geometric identification of Jacobian two-torsion with Kummer nodes and of the two classical tetrad types with the two affine plane types.

## Relationship to prior work
The six-branch-point description of \(J(C)[2]\), its symplectic pairing, and the \(60/80\) Göpel/Rosenhain geometric tetrad distinction are classical. Keum's *Automorphisms of Jacobian Kummer surfaces* (1997) gives the geometry and the affine-plane interpretation. Ohashi's *Enriques surfaces covered by Jacobian Kummer surfaces* (2009; arXiv:0909.5352) discusses the \(16\)-node model, symplectic pairing, and tetrads in detail; the relevant material was inspected in the full preprint. Dolgachev's later treatment of Kummer type in characteristic two also describes the geometric affine-plane classification. The present result does not claim any of these facts as new. Its assessed addition is the full explicit arithmetic Frobenius orbit census for **both** finite schemes, including the eleven all-extension zeta signatures and minimal splitting degrees. Relevant published primary texts and mathematical-record searches did not identify these same orbit tables or a stronger arithmetic classification implying them; this is a best-knowledge originality assessment, not an assertion of historical uniqueness. General formulas for \(S_6\)-actions can in principle be applied to compute these distributions.

## Limitations
This is a classification of finite Galois sets of tetrads, not of all projective automorphisms, bitangents, rational divisor classes, or the full Kummer-surface zeta function. It excludes characteristic two and does not treat arithmetic twists whose Kummer structure is not supplied by an explicit Jacobian curve. The table's finiteness and exact arithmetic proof do not constitute an independent mathematical audit or a complete search of historical literature. Some earlier descriptions of Kummer combinatorics could implicitly contain the data without listing the table. A Kyoto preprint of Ohashi's work is dated December 2008 but did not provide an independently verified public day; September 29, 2009 is the first exactly day-verified source date used here.

## References
1. J. H. Keum, *Automorphisms of Jacobian Kummer surfaces*, Compositio Mathematica **107** (1997), 269–288.
2. H. Ohashi, *Enriques surfaces covered by Jacobian Kummer surfaces*, Nagoya Mathematical Journal **195** (2009), 165–186, arXiv:0909.5352, doi:10.1017/S0027763000009764 (arXiv initial public posting 2009-09-29).
3. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, Bulletin of the London Mathematical Society (2024), doi:10.1112/blms.13033, Section 5 (geometric tetrads only).
4. A. González-Hernández, *Explicit desingularisation of Kummer surfaces in characteristic two via specialisation*, first publicly posted 2024 (comparison of distinct node/trope arithmetic invariants, not the present tetrad census).
