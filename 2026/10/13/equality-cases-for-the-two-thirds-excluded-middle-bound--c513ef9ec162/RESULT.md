# Equality cases for the two-thirds excluded-middle bound

## Finding
Let \(H\) be a finite non-Boolean Heyting algebra and write
\[
\mathrm{EM}(H)=\{a\in H:a\vee\neg a=1\}.
\]
Bumpus and Kocsis proved the sharp inequality
\[
\frac{|\mathrm{EM}(H)|}{|H|}\le \frac23.
\]
The equality cases admit a complete classification:
\[
\boxed{\frac{|\mathrm{EM}(H)|}{|H|}=\frac23
\quad\Longleftrightarrow\quad
H\cong C_3\times C_2^k\text{ for a unique }k\ge0.}
\]
Here \(C_m\) denotes the \(m\)-element Heyting chain and \(C_2^0\) denotes the empty product. Consequently, the orders of the extremal finite non-Boolean Heyting algebras are exactly
\[
3,6,12,24,\ldots,3\cdot2^k,\ldots,
\]
and for each such order there is exactly one isomorphism type.

There is also a simple finite-poset reformulation. If \(H\cong\operatorname{Up}(P)\) is represented as the upset algebra of its finite Birkhoff dual poset, then equality holds exactly when \(P\) is the disjoint union of one two-element chain and \(k\) isolated points.

## Assumptions and scope
All Heyting algebras here are finite. The degree of satisfiability of excluded middle is
\[
\operatorname{ds}_H(p\vee\neg p=1)=\frac{|\mathrm{EM}(H)|}{|H|}.
\]
The claim classifies the equality case in the sharp finite non-Boolean bound of Bumpus and Kocsis. It does not make a corresponding assertion for their infinitary density notions, nor does it classify equality cases for other one-variable equations.

The notation \(C_2^k\) is a direct product of \(k\) copies of the two-element Boolean algebra. Thus \(C_2^k\) is the unique Boolean algebra of size \(2^k\), with the usual empty-product convention at \(k=0\).

## Proof
Bumpus and Kocsis identify \(\mathrm{EM}(H)\) with the center of \(H\), prove that it is the largest Boolean subalgebra of \(H\), and prove the product rule
\[
\operatorname{ds}_{A\times B}(p\vee\neg p=1)
=
\operatorname{ds}_{A}(p\vee\neg p=1)
\operatorname{ds}_{B}(p\vee\neg p=1).
\]
Their proof of the \(2/3\) bound splits a finite Heyting algebra at a nontrivial central element \(c\):
\[
H\cong H_c\times H_{\neg c},
\qquad
H_c=\{x\in H:x\le c\}.
\]
Iterating this finite decomposition writes
\[
H\cong H_1\times\cdots\times H_r
\]
with every factor \(H_i\) having trivial center, meaning \(|\mathrm{EM}(H_i)|=2\). This same factorization is explicitly used later in the source.

For such a factor,
\[
\operatorname{ds}_{H_i}(p\vee\neg p=1)=\frac{2}{|H_i|}.
\]
If \(|H_i|=2\), then \(H_i\cong C_2\) is Boolean and this degree is \(1\). If \(H_i\) is non-Boolean, then \(|H_i|\ge3\), so its degree is at most \(2/3\), with equality precisely when \(|H_i|=3\). There is only one three-element bounded distributive lattice, namely the chain, and its Heyting implication is uniquely determined; hence that factor is \(C_3\).

Now suppose \(H\) is non-Boolean and has excluded-middle degree \(2/3\). At least one center-trivial factor is non-Boolean. If two factors were non-Boolean, multiplicativity would give at most
\[
\left(\frac23\right)^2=\frac49<\frac23.
\]
Therefore exactly one factor is non-Boolean. For the product to have degree exactly \(2/3\), that factor must itself have degree \(2/3\), hence must be \(C_3\); every other factor must have degree \(1\), hence must be \(C_2\). Thus
\[
H\cong C_3\times C_2^k.
\]
Conversely, multiplicativity immediately gives
\[
\operatorname{ds}_{C_3\times C_2^k}(p\vee\neg p=1)
=
\frac23\cdot1^k
=
\frac23.
\]
The integer \(k\) is determined by the cardinality \(|H|=3\cdot2^k\), so it is unique.

For the dual formulation, finite Birkhoff duality sends a disjoint union of posets to a direct product of upset lattices. The two-element chain has exactly three upsets and a singleton has exactly two. Hence the dual of \(C_3\times C_2^k\) is one two-element chain together with \(k\) isolated points, and conversely.

## Verification
The script `verify_excluded_middle_equality.py` independently checks the Birkhoff-dual formulation on every labelled poset with at most five points. For each poset it enumerates all upsets, identifies complemented upsets by checking that the set complement is again an upset, computes the excluded-middle ratio exactly as a rational number, and compares the equality condition with the claimed component structure.

It examines all
\[
1+3+19+219+4231=4473
\]
labelled posets of sizes one through five. The numbers of equality cases are
\[
0,2,6,12,20,
\]
which for \(n\ge2\) are exactly \(n(n-1)\): choose the two vertices of the unique nontrivial component and orient their chain. The verifier also independently checks that the number of complemented upsets is \(2^c\), where \(c\) is the number of comparability components.

Replay:

```text
python3 verify_excluded_middle_equality.py
```

Expected final line:

```text
VERIFY_OK 8956 exact assertions
```

This finite computation corroborates the structural proof; it is not used in place of the general argument.

## Relationship to prior work
Bumpus and Kocsis prove that excluded middle has finite satisfiability gap \(1/3\): every finite non-Boolean Heyting algebra has excluded-middle degree at most \(2/3\). Their proof develops exactly the two ingredients used above: multiplicativity under direct products and splitting along nontrivial central elements. Immediately after the proof they state that the bound is tight and is realized by the three-element Heyting algebra.

The inspected source does not classify all algebras attaining equality. Its later discussion again uses the decomposition into trivial-center factors, but no equality-case theorem is stated. Targeted searches for the product classification, its order spectrum, and the dual-poset formulation found the sharp inequality and the three-element example, but no equivalent classification. Searches of the cumulative research ledgers likewise found other results about finite Heyting algebras, but none concerning the excluded-middle equality case.

Thus the new step is an equality analysis of the published multiplicative proof: equality forces exactly one non-Boolean center-trivial factor, and that factor must have three elements.

## Limitations
The argument is specific to finite Heyting algebras and to the law of excluded middle. It does not classify extremizers for other finite-gap equations, and it does not address possible equality notions for infinite density measures. The equality analysis is short enough that an equivalent observation could exist as uncatalogued folklore or in literature not indexed under degree-of-satisfiability terminology.

Self-review has checked the deduction against the full published proof, but no independent audit has been performed.

## References
1. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, Journal of Symbolic Logic 90 (2025), 533–551, DOI 10.1017/jsl.2024.2; first public preprint arXiv:2110.11515 (21 October 2021). Proposition 1.9 gives multiplicativity of degrees under products; Definition 1.10 and Proposition 1.11 identify excluded-middle elements with the Boolean center; Theorem 2.2 proves the sharp \(2/3\) non-Boolean bound by splitting at central elements.
2. Standard finite Birkhoff duality for finite distributive lattices, used only for the equivalent poset reformulation and the finite verifier.
