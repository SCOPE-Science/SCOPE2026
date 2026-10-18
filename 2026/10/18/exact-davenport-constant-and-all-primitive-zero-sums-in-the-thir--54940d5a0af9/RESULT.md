# Exact Davenport constant and all primitive zero sums in the thirteen-point lattice disk

## Finding

Let \(\mathcal B=\{(x,y)\in\mathbb Z^2:x^2+y^2\le4\}\), the closed radius-two lattice disk (13 points). A *minimal zero-sum multiset* over \(\mathcal B\) is a nonempty multiset with sum zero and with no nonempty proper zero-sum submultiset. With \(D(\mathcal B)\) its maximum cardinality, the following exact census holds:

\[
D(\mathcal B)=5,\qquad
\#\{\text{minimal zero-sum multisets of length }\ell\}=
\begin{cases}
1&\ell=1,\\
6&\ell=2,\\
12&\ell=3,\\
16&\ell=4,\\
12&\ell=5,\\
0&\ell\ge6.
\end{cases}
\]

The twelve maximal multisets form exactly two orbits under the eight-element symmetry group of the square: one orbit of size eight, consisting of multisets supported on three points, and one of size four, consisting of multisets supported on five points. Representatives (exponents denote multiplicity) are

\[
\begin{aligned}
S_3&=\{(-2,0),(0,-1)^{[2]},(1,1)^{[2]}\},\\
S_5&=\{(-2,0),(0,-2),(0,1),(1,0),(1,1)\}.
\end{aligned}
\]

Consequently the disk has exactly 47 nonempty minimal zero-sum multisets, including the singleton \(\{(0,0)\}\) and the six antipodal pairs. Both support types achieve the same extremal length.

## Assumptions and scope

All multisets are unordered, multiplicities are nonnegative integers, and zero-sum means zero in the free abelian group \(\mathbb Z^2\), not modulo any integer. The disk is closed, with Euclidean radius exactly two. Symmetries are sign changes of either coordinate and interchange of the two coordinates, with no translations or arbitrary linear changes. No claim is made for larger radii or dimensions. The finite-exhaustion proof invokes the known planar Euclidean Steinitz constant \(\sqrt5/2\), proved in earlier literature and used by Girard and Plagne.

## Proof

**Finite reduction.** The sharp planar Steinitz rearrangement theorem says that any zero-sum sequence of vectors of Euclidean norm at most two can be permuted so every partial sum has Euclidean norm at most \(\sqrt5\). If a zero-sum sequence is minimal of length \(L\), its initial \(L\) partial sums, at indices \(0,\ldots,L-1\), are all distinct: an equality at two such indices would yield a nonempty proper zero-sum submultiset. They are lattice points in the disk of squared radius five. That disk contains exactly 21 integer points (one of squared norm zero, four each of squared norms one, two, and four, and eight of squared norm five). Hence \(L\le21\).

**Orientation reduction.** An atom of length at least three contains neither zero nor a pair of opposite nonzero vectors: either would be a proper zero-sum submultiset. The twelve nonzero disk points form the six antipodal pairs represented by \((1,0),(2,0),(0,1),(0,2),(1,1),(1,-1)\). Therefore every atom of length at least three uses vectors from at least one of the 64 oriented six-element sets obtained by choosing a sign in each pair. Duplication across orientations is removed by canonical multiset sorting.

**Exhaustive integer certificate.** Fix an oriented six-tuple \(v_0,\ldots,v_5\). Choose two linearly independent pivot vectors \(v_i,v_j\); they always exist because the oriented tuple contains an axis vector in each direction. Write \(\Delta=\det(v_i,v_j)\ne0\). Let \(f_1,\ldots,f_4\) be arbitrary nonnegative multiplicities for the other four vectors, with \(t=\sum f_h\le21\), and put \((X,Y)=-\sum_h f_hv_h\). The only possible multiplicities on the two pivot vectors are

\[
 c_i=\frac{X(v_j)_y-Y(v_j)_x}{\Delta},\qquad
 c_j=\frac{(v_i)_xY-(v_i)_yX}{\Delta}.
\]

Keep the solution only when both values are nonnegative integers, the total length is positive, and \(t+c_i+c_j\le21\). Enumerate free quadruples by increasing \(t\). An integer zero-sum solution is minimal precisely when it contains none of the already found minimal zero-sum solutions coordinatewise. Indeed, if a proper zero-sum submultiset existed, it would contain a minimal zero-sum submultiset; that submultiset has strictly smaller \(t\): equality of all four free multiplicities would force the same two pivot multiplicities by uniqueness, making it the full multiset. Thus induction on \(t\) proves both the soundness and completeness of this test.

Each orientation has exactly \(\binom{25}{4}=12{,}650\) free quadruples with sum at most 21, for a total of 809,600 examined quadruples. The attached standard-library-only program `verify_ball2.py` implements all arithmetic with exact integers and reconstructs every retained multiset. After removal of duplicate orientations the counts at lengths three, four, and five are respectively 12, 16, and 12; it finds none of length six through 21. Together with the singleton zero and six opposite pairs, this proves the claimed length census and \(D(\mathcal B)=5\).

**Symmetry classification.** For each of the twelve length-five multisets, apply all eight maps \((x,y)\mapsto(\varepsilon x,\delta y)\) and \((x,y)\mapsto(\varepsilon y,\delta x)\), with \(\varepsilon,\delta\in\{-1,1\}\). Canonical lexicographic representatives partition the twelve multisets into two classes of respective sizes eight and four. The displayed \(S_3,S_5\) are the computed canonical representatives. Their nonzero sums and minimality are separately checked by direct proper-submultiset enumeration.

## Verification

Run `python3 verify_ball2.py` from this file's directory, using only the Python standard library. Its expected terminal line begins `CERTIFICATE_OK` and reports exactly 809600 free quadruples, 40 primitive multisets of lengths three through five, twelve of maximal length five, and orbit sizes four and eight. A second enumeration enumerates all multiplicity six-tuples of total at most nine directly, without pivot solving, and checks agreement on all sequences of that length. Every reported atom is also checked independently against all of its proper nonempty submultisets. These are finite certificates of a finite classification; the Steinitz bound supplies the necessary global length cutoff.

## Relationship to prior work

Girard and Plagne, *The Davenport constant of balls and boxes* (first publicly posted 2025-10-23), define the exact same disk invariant and prove estimates for general radii, especially asymptotic planar bounds, as well as the radius-one value \(D=2\). Their dimension-two finite theorems do not evaluate the radius-two constant, enumerate its atoms, or classify its maximal orbits. Their Section 4 provides the planar Steinitz bound used here. Classical work on box Davenport constants concerns a different set: the integer square containing the radius-two disk. Neither box estimates nor asymptotic bounds determine this 47-atom classification. The coexistence of three-point and five-point supports at maximal length is a concrete low-radius structural feature of the disk invariant.

## Limitations

The result concerns only the thirteen-point radius-two disk. It uses the established sharp planar Steinitz theorem and an exhaustively verified finite search whose completeness relies on the explicitly stated pivot/antichain algorithm; it is not an independent machine-formal proof. Literature searches cannot rule out an obscure earlier equivalent classification. No statement about larger disks, a formula at general radius, or independence of scientific review is asserted.

## References

1. B. Girard and A. Plagne, *The Davenport constant of balls and boxes*, arXiv:2510.20412, first publicly posted 2025-10-23, https://arxiv.org/abs/2510.20412 . In particular Introduction, Section 2, Section 4, and the discussion of support-restricted constants.
2. W. Banaszczyk, *The Steinitz constant of the plane*, J. reine angew. Math. 373 (1987), 218–220, as cited and applied by Girard and Plagne.
3. A. Plagne and S. Tringali, *The Davenport constant of a box*, Acta Arith. 171 (2015), 197–220, for the distinct square-box problem cited by Girard and Plagne.
