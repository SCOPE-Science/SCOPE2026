# Inverse-multiplier action on the order-\(23\) torsion of the Paley tournament complex

## Finding

Let \(P_{23}\) have vertex set \(\mathbb F_{23}\), with \(u\to v\) precisely when \(v-u\) is a nonzero quadratic residue. Let \(X=\operatorname{dFl}(P_{23})\) be the abstract simplicial complex whose simplices are the transitive subtournaments. The published nonequivariant homology is
\[
H_3(X;\mathbb Z)\cong\mathbb Z^{23}\oplus\mathbb Z/23,\qquad H_4(X;\mathbb Z)\cong\mathbb Z^{45},
\]
with no other positive-degree homology. The **new finding** concerns the symmetry action on the torsion summand. For every \(a\) in the multiplicative group \(Q\) of the eleven nonzero squares and every \(b\in\mathbb F_{23}\), the affine tournament automorphism \(g_{a,b}(u)=au+b\) satisfies
\[
(g_{a,b})_*z=a^{-1}z\quad\text{in }\operatorname{Tors}H_3(X;\mathbb Z)\cong\mathbb Z/23.
\]
Thus \(u\mapsto2u\) acts on the cyclic torsion group by multiplication by \(12\) (order eleven), while every translation acts trivially.

## Assumptions and scope

All homology is reduced or unreduced singular/simplicial homology, as appropriate, with indicated coefficients. A simplex is an unordered vertex set whose induced tournament is acyclic; it has a unique transitive ordering. Orient chains by increasing numerical vertex order, and use the alternating deletion boundary. There are exactly \(23,253,1265,2530,1518\) simplices in dimensions \(0,1,2,3,4\), and none above dimension four. The claim concerns the natural order-\(253\) affine subgroup \(\mathbb F_{23}\rtimes Q\); it makes no claim about all tournament automorphisms or other primes.

## Proof

**1. Symmetry and nonequivariant input.** Because the multiplicative group \(Q\) preserves the quadratic residues and translations preserve differences, \(g_{a,b}\) preserves orientation of every tournament edge. The element \(2\) generates \(Q\), since \(2^{11}\equiv1\pmod{23}\) and \(2\ne1\). The 2020 classification of doubly regular tournaments through order \(27\) (Govc, Proposition 3.4) contains exactly one order-\(23\) example with homotopy type
\[
M(\mathbb Z/23,3)\vee\bigvee^{23}S^3\vee\bigvee^{45}S^4.
\]
The quadratic-residue tournament is doubly regular: for a nonzero square difference, the number of common outgoing neighbors is \(5\), by a direct quadratic-character count (and likewise for nonsquare differences by translating the pair). The exact finite calculation below has \(\dim_{\mathbb F_2}H_4(X;\mathbb F_2)=45\), whereas the other order-\(23\) types in Proposition 3.4 have at most one four-sphere summand. Thus it identifies \(X\) with the unique displayed type and establishes the integral homology stated above; that integral homology is previously known, not claimed as new.

**2. Cyclic equivariant chains.** Let \(s(u)=2u\), an automorphism of order \(11\). Its action on all nonempty simplices has only one fixed simplex, the vertex \(\{0\}\): every other orbit has length \(11\), because the sizes of simplices are at most five. The numbers of simplex orbits in dimensions \(0,1,2,3,4\) are \(3,23,115,230,138\). For each orbit, use a sorted representative \(\sigma\) and the signs of the induced vertex reordering in each \(s^j\sigma\). For any eleventh root of unity \(\lambda\in\mathbb F_{23}^{\times}\), the eigenchain generator of a free orbit is
\[
E_{\sigma,\lambda}=\sum_{j=0}^{10}\lambda^{-j}s^j\sigma.
\]
The unique fixed vertex is retained only for \(\lambda=1\). These eigenchain generators form a basis of each eigenspace because \(11\) is invertible in \(\mathbb F_{23}\).

**3. Exact boundary ranks.** Enumerate each transitive vertex set by rejecting every directed three-cycle, and assemble the oriented alternating boundary on the eigenchain bases. The standalone program `verify.py` constructs every simplex and orbit independently from the quadratic-residue rule, and executes exact Gaussian elimination over \(\mathbb F_{23}\). In each eigenspace the ranks of \(\partial_1,\partial_2,\partial_3\) are \(2,21,94\). For \(\lambda=1\) and \(\lambda=12\), the rank of \(\partial_4\) is \(133\), yielding \(\dim H_4(X;\mathbb F_{23})_{\lambda}=5\). For each of the other nine eigenvalues, the rank of \(\partial_4\) is \(134\), yielding \(\dim H_4(X;\mathbb F_{23})_{\lambda}=4\). Summing gives \(\dim H_4(X;\mathbb F_{23})=46\), one greater than the integral free rank. The calculation separately checks the \(\mathbb F_2\)-invariant chain complex: its boundary ranks are \(2,21,94,133\), giving \(\dim H_4(X;\mathbb F_2)^{\langle s\rangle}=5\).

**4. Isolating the torsion character.** From the published integral homology, \(H_4(X;\mathbb Z)\) is free of rank \(45\) and \(H_3(X;\mathbb Z)\) has only one torsion factor, of order \(23\). Because \(11\) is invertible in characteristic two, taking \(\langle s\rangle\)-invariants commutes with homology over \(\mathbb F_2\). The dimension-five invariant group just computed therefore gives a five-dimensional invariant subspace in \(H_4(X;\mathbb Q)\). Over \(\mathbb Q\), the irreducible representations of a cyclic group of prime order \(11\) are the trivial line and the ten-dimensional cyclotomic module. Consequently,
\[
H_4(X;\mathbb Q)|_{\langle s\rangle}\cong \mathbf 1^{\oplus5}\oplus\mathbb Q(\zeta_{11})^{\oplus4}.
\]
Reducing the integral free lattice modulo \(23\), where the eleventh roots of unity are distinct, gives dimension \(5\) in the trivial eigenvalue and dimension \(4\) in each nontrivial eigenvalue. The natural universal-coefficient exact sequence
\[
0\longrightarrow H_4(X;\mathbb Z)\otimes\mathbb F_{23}\longrightarrow H_4(X;\mathbb F_{23})\longrightarrow\operatorname{Tor}_1^{\mathbb Z}(H_3(X;\mathbb Z),\mathbb F_{23})\longrightarrow0
\]
is \(\langle s\rangle\)-equivariant and splits as a module because its order is prime to \(23\). Comparing with the finite-field ranks shows that its one-dimensional torsion quotient is **exactly the \(\lambda=12\) eigenspace**. Naturality identifies that quotient with the order-\(23\) torsion of \(H_3(X;\mathbb Z)\), with the same action. Hence \(s_*z=12z\).

**5. All affine automorphisms.** Every translation has order dividing \(23\). Its induced automorphism on the cyclic group \(\mathbb Z/23\) has order dividing both \(23\) and \(22\), hence is the identity. Each \(a\in Q\) is \(2^j\), and \(12=2^{-1}\pmod{23}\), giving \((g_{a,b})_*z=a^{-1}z\) as stated.

## Verification

Run `python3 verify.py` with Python 3; no third-party packages are required. The script enumerates \(23,253,1265,2530,1518\) simplices, groups them into \(3,23,115,230,138\) orbits, computes signed boundary matrices for all eleven eigenvalues of the order-eleven action, and verifies all ranks and the independent characteristic-two invariant computation. It prints `VERIFY_OK` and `CHAR2_OK` on success. Finite-field computation proves the **equivariant eigenvalue comparison**; the previously established integral-homology classification supplies the necessary integral torsion premise.

## Relationship to prior work

Masulli and Villa (2015, arXiv:1510.00660) define the directed clique complex and use nonequivariant Betti invariants; that public preprint is the earliest verified dated source used here. Govc (2020, arXiv:2006.05333, Proposition 3.4, page 15) classifies the nonequivariant homotopy types of all doubly regular tournaments with at most \(27\) vertices, including a unique type with a \(\mathbb Z/23\) Moore summand at order \(23\). The action of the natural affine symmetry on that torsion generator is not stated there. Existing related calculations of affine actions for a different prime and of torsion classes without affine characters do not determine the inverse-multiplier action proved here.

## Limitations

The claimed symmetry character concerns only the specified Paley tournament, the order-\(23\) summand in degree three, and its natural affine subgroup. It is not a classification of all equivariant homology modules or of the action on integral free homology. The integral torsion order is drawn from the published complete classification, with an independent finite-field identification of the corresponding Paley object; the new eigencharacter is supported by the included finite rank certificate. The literature comparison is bounded, and no independent audit has been performed.

## References

1. P. Masulli and A. E. P. Villa, *The topology of the directed clique complex as a network invariant*, arXiv:1510.00660, first publicly posted 2015-10-02, https://arxiv.org/abs/1510.00660. Methods, definition of directed clique complexes.
2. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333, first publicly posted 2020-06-09, https://arxiv.org/abs/2006.05333. Definition 1.2 and Proposition 3.4, especially page 15; full text inspected.
