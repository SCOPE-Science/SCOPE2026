# The second excluded-middle gap in finite Heyting algebras

## Finding
Let \(H\) be a finite non-Boolean Heyting algebra and write
\[
\operatorname{ds}_{\mathrm{EM}}(H)
=\frac{|\{a\in H:a\vee\neg a=1\}|}{|H|}.
\]
Bumpus and Kocsis proved \(\operatorname{ds}_{\mathrm{EM}}(H)\le 2/3\), and the preceding equality analysis identifies the \(2/3\) family as \(C_3\times C_2^k\). Once that extremal family is removed, there is a second sharp gap:
\[
\boxed{
H\not\cong C_3\times C_2^k\ (k\ge0)
\quad\Longrightarrow\quad
\operatorname{ds}_{\mathrm{EM}}(H)\le\frac12.
}
\]
Moreover,
\[
\boxed{
\operatorname{ds}_{\mathrm{EM}}(H)=\frac12
\quad\Longleftrightarrow\quad
H\cong C_4\times C_2^k
\text{ for a unique }k\ge0.
}
\]
Thus no finite non-Boolean Heyting algebra has excluded-middle degree strictly between \(1/2\) and \(2/3\). The second-largest possible degree is exactly \(1/2\), and its equality family is completely rigid up to a Boolean direct factor.

Under finite Birkhoff duality, the \(1/2\) cases are exactly the upset algebras of posets consisting of one three-element chain and \(k\) isolated points.

## Assumptions and scope
All Heyting algebras are finite. The notation \(C_m\) denotes the \(m\)-element Heyting chain, and \(C_2^k\) is the direct product of \(k\) two-element Boolean algebras, with \(C_2^0\) the empty product.

The hypothesis excludes only the already-classified \(2/3\) extremizers. Boolean algebras, whose excluded-middle degree is \(1\), are already excluded by assuming \(H\) non-Boolean. The result concerns excluded middle only and does not assert a second-gap phenomenon for other classical principles or for infinite density notions.

## Proof
Bumpus and Kocsis identify the excluded-middle elements of a Heyting algebra with its Boolean center and prove multiplicativity of degree of satisfiability under finite direct products. Their proof of the \(2/3\) theorem also gives the central splitting
\[
H\cong H_c\times H_{\neg c}
\]
whenever \(c\) is a nontrivial central element. Iterating this finite splitting yields
\[
H\cong H_1\times\cdots\times H_r
\]
where every factor \(H_i\) has trivial center. Consequently each factor has exactly two excluded-middle elements and contributes
\[
\operatorname{ds}_{\mathrm{EM}}(H_i)=\frac{2}{|H_i|}.
\]
A factor of size \(2\) is \(C_2\) and contributes \(1\). Every non-Boolean factor has size at least \(3\).

Suppose first that at least two factors are non-Boolean. Then multiplicativity gives
\[
\operatorname{ds}_{\mathrm{EM}}(H)
\le \left(\frac23\right)^2
=\frac49<\frac12.
\]
So any algebra with degree at least \(1/2\) has exactly one non-Boolean center-trivial factor, say \(K\), and all other factors are \(C_2\). In that case
\[
\operatorname{ds}_{\mathrm{EM}}(H)=\frac{2}{|K|}.
\]
If \(|K|=3\), then \(K\cong C_3\), giving precisely the excluded extremal family \(C_3\times C_2^k\). Otherwise \(|K|\ge4\), and hence
\[
\operatorname{ds}_{\mathrm{EM}}(H)\le\frac12.
\]
This proves the second gap.

Equality at \(1/2\) forces \(|K|=4\). A four-element bounded distributive lattice is either the four-element chain or the four-element Boolean algebra: if its two middle elements are comparable it is a chain, while if they are incomparable their meet and join are the bounds, giving the Boolean square. Since \(K\) has trivial center, it cannot be the Boolean algebra. Hence \(K\cong C_4\), and
\[
H\cong C_4\times C_2^k.
\]
Conversely, \(C_4\) has exactly two excluded-middle elements, so multiplicativity gives
\[
\operatorname{ds}_{\mathrm{EM}}(C_4\times C_2^k)=\frac12.
\]
The integer \(k\) is uniquely determined by \(|H|=4\cdot2^k\).

For the dual formulation, the upset algebra of a three-element chain is \(C_4\), the upset algebra of a singleton is \(C_2\), and disjoint unions of finite posets dualize to direct products. This gives exactly one three-chain component and \(k\) isolated points.

## Verification
The script `verify_second_excluded_middle_gap.py` independently checks the dual statement on every labelled poset with at most five points. For each poset it enumerates all upsets and all complemented upsets, computes the excluded-middle ratio exactly, reconstructs comparability components, and verifies three statements simultaneously: the known \(2/3\) family, the absence of ratios in \((1/2,2/3)\) away from that family, and the exact \(1/2\) equality structure.

It examines all
\[
1+3+19+219+4231=4473
\]
labelled posets of sizes one through five. The numbers of \(1/2\) equality cases are
\[
0,0,6,24,60,
\]
which equal \(n(n-1)(n-2)\) for \(n\ge3\): choose the three vertices of the unique nontrivial component and choose one of the \(3!\) linear orders on them.

Replay:

```text
python3 verify_second_excluded_middle_gap.py
```

Expected final line:

```text
VERIFY_OK 17907 exact assertions
```

The exhaustive computation is a finite corroboration of the structural proof, not a substitute for it.

## Relationship to prior work
Bumpus and Kocsis prove the sharp non-Boolean upper bound \(2/3\), identify excluded-middle elements with the Boolean center, prove multiplicativity under products, and explicitly split finite Heyting algebras at nontrivial central elements. Immediately after their proof they state that the \(2/3\) bound is tight and is realized by the three-element Heyting algebra.

The current cumulative ledger already contains the complete \(2/3\) equality classification \(C_3\times C_2^k\). That result does not imply the present theorem: after removing the top family it only gives a strict inequality below \(2/3\), not a new universal ceiling or its equality cases. The additional factor-size analysis above yields the forbidden interval \((1/2,2/3)\) and identifies the exact second extremizers \(C_4\times C_2^k\).

Candidate-specific searches under “second largest”, \(1/2\), \(C_4\), Boolean-center, direct-product, and dual-poset formulations located the published \(2/3\) theorem but no equivalent second-gap classification. The inspected primary text states the top bound and the three-element tight example, not a \(1/2\) second rung.

## Limitations
The argument is specific to finite Heyting algebras and excluded middle. It does not determine the complete set of attainable excluded-middle degrees below \(1/2\), nor does it address analogous second gaps for other equations or infinite density measures.

Because the proof is a short refinement of a published multiplicative decomposition, an equivalent statement could exist as uncatalogued folklore or under lattice-theoretic center terminology. Self-review has checked the deduction; independent audit has not been performed.

## References
1. Benjamin Merlin Bumpus and Zoltan A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, Journal of Symbolic Logic 90 (2025), 533–551, DOI 10.1017/jsl.2024.2; first public preprint arXiv:2110.11515 (21 October 2021). Proposition 1.9 gives multiplicativity; Definition 1.10 and Proposition 1.11 identify excluded-middle elements with the Boolean center; Theorem 2.2 gives the central splitting argument and the sharp \(2/3\) bound.
2. Standard finite Birkhoff duality for finite distributive lattices, used for the equivalent poset formulation and the finite verifier.
