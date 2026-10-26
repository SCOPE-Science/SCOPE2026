# Unique completion modulo 73 of a four-term Sidon seed

## Finding

Let \(A=\{1,2,4,8\}\subset\mathbb Z\) and let
\[
B=\{1,2,4,8,16,32,37,55,64\}\subset\mathbb Z/73\mathbb Z.
\]
A perfect difference set modulo \(73\) is a nine-element set whose \(9\cdot8=72\) ordered differences of distinct elements represent each nonzero residue exactly once.

**Claim.** Among all perfect difference sets modulo \(73\), exactly one contains the residue set \(A\), namely \(B\). Equivalently, among the \(584\) affine images \(uB+v\), where \(u\in(\mathbb Z/73\mathbb Z)^\times\) and \(v\in\mathbb Z/73\mathbb Z\), the unique image containing \(A\) is \(B\).

## Assumptions and scope

The statement concerns the fixed seed \(A\), the fixed modulus \(73\), and cyclic \((73,9,1)\) perfect difference sets. The published classification that every such set lies in the Singer affine orbit is used as a literature premise; it is not reproved here. No claim is made about completions at other moduli or about the general Sidon-extension conjecture.

## Proof

First, \(B\) is the set of powers \(2^j\bmod 73\) for \(0\le j\le8\). Exact modular arithmetic verifies that the \(72\) ordered differences \(b-b'\pmod{73}\), for \(b,b'\in B\) with \(b\ne b'\), are pairwise distinct. Hence they are exactly the nonzero residues and \(B\) is a perfect difference set. Clearly \(A\subset B\).

The affine group has \(72\cdot73=5256\) maps \(x\mapsto ux+v\). Since \(\sum_{b\in B}b\equiv0\pmod{73}\), any affine map stabilizing \(B\) must have \(9v\equiv0\pmod{73}\), hence \(v=0\). The multipliers stabilizing \(B\) are exactly the nine elements of the subgroup \(B=\langle2\rangle\). Thus the stabilizer has size \(9\), and the affine orbit has size \(5256/9=584\). Hall's uniqueness result, as explicitly reported and checked for \(\mathbb Z/73\mathbb Z\) by Niu, says this orbit contains every cyclic \((73,9,1)\) perfect difference set.

It remains to count which orbit elements contain \(A\). For a four-set \(C\subset\mathbb Z/73\mathbb Z\), define its affine signature by normalizing each ordered pair \(x\ne y\) to \(0,1\), sorting the four resulting residues, and taking the lexicographically least tuple. This is a complete invariant for affine equivalence. The seed has signature \((0,1,3,7)\). An exact enumeration of all \(\binom94=126\) four-subsets of \(B\) finds exactly nine with this signature:
\[
\begin{gathered}
\{1,2,4,8\},\ \{2,4,8,16\},\ \{4,8,16,32\},\\
\{8,16,32,64\},\ \{16,32,55,64\},\ \{32,37,55,64\},\\
\{1,37,55,64\},\ \{1,2,4,37\},\ \{1,2,37,55\}.
\end{gathered}
\]
They are exactly \(2^jA\pmod{73}\) for \(0\le j\le8\). A separate exact check over all \(5256\) affine maps shows that \(A\) has trivial affine stabilizer. Therefore precisely nine affine maps send some four-subset of \(B\) to \(A\), equivalently precisely nine affine maps have an image of \(B\) containing \(A\). Each distinct orbit element has exactly nine affine representations because the stabilizer of \(B\) has size nine. Consequently exactly one distinct affine image contains \(A\); since \(B\) itself does, it is the unique one. The cited classification transfers this conclusion to all perfect difference sets modulo \(73\). \(\square\)

## Verification

The standalone checker `verify.py` uses only exact integer arithmetic and exhaustive finite loops. Run `python verify.py` from the artifact directory. It checks all \(72\) differences, all \(5256\) affine maps, the orbit size and stabilizer, all \(126\) four-subsets, and the seed stabilizer. Its terminal status is `VERIFY_OK`.

The computation verifies the finite claim and the stated orbit counts. The completeness of the affine orbit among all perfect difference sets modulo \(73\) is supplied by the cited classification, not by an independent census of arbitrary nine-subsets.

## Relationship to prior work

Alexeev and Mixon identify \(\{1,2,4,8\}\) as a Sidon set that cannot extend to a perfect difference set of prime order, and explicitly note the extension modulo \(73\) given by \(B\). Niu reports that all \(584\) perfect difference sets in \(\mathbb Z/73\mathbb Z\) lie in this Singer affine orbit. Neither inspected source states the exact seed-containment multiplicity proved here. The result refines the known existence example by showing that its completion at this modulus is rigid: there is no second perfect difference set modulo \(73\) containing the same seed.

## Limitations

This is a single-modulus completion count. It does not show that \(A\) extends or fails to extend at any other modulus, does not classify all Sidon sets of size four, and does not resolve the prime-power conjecture. The global uniqueness statement depends on the published classification of cyclic \((73,9,1)\) difference sets. Independent audit and independent validation have not been performed.

## References

1. B. Alexeev and D. G. Mixon, “Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof,” arXiv:2510.19804, first posted 2025-10-22; see Theorem 8 and the discussion of the explicit perfect difference set modulo \(73\).
2. T. Niu, “Empirical evidence for size-4 counterexamples to Erdős’s Sidon-extension conjecture,” arXiv:2604.25214, first posted 2026-04-28; see §2.1 and §3.2 for the \(584\)-element affine orbit in \(\mathbb Z/73\mathbb Z\) and the seed’s extension.
3. M. Hall, “Cyclic projective planes,” *Duke Mathematical Journal* 14 (1947), 1079–1090. The classification used for order \(8\) is also stated in Niu’s §2.1.
