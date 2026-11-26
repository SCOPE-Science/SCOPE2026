# Independent mathematical audit

## correctness

PASS

For distinct a,b the mixed products cannot collide with either square. If a,b commute, the two product squares coincide exactly when ab⁻¹ has order two, which also detects the quotient collision. If they do not commute and have equal squares, (ab⁻¹)²=1 would imply that ab⁻¹ commutes with b, a contradiction. Thus precisely the noncommuting unequal-square pairs witness size two. If all noncommuting pairs have equal squares, choose one such pair and set c=a²=b². It is central in the generated subgroup. Applying the same condition to (a,ab) and (b,ba) gives (ab)²=(ba)²=c, while (ab)²=c implies ba=ab⁻¹=c⁻¹ab. Squaring forces c=c⁻¹; c=1 would force commutation. The quotient by ⟨c⟩ has two distinct nontrivial commuting involutions represented by a,b and hence order four; the resulting order-eight presentation is quaternion. On {1,a,b} the products are {1,a,b,c,ab,cab} and the quotients are {1,a,ca,b,cb,ab,cab}, establishing size three. For abelian groups, on {0,g,3g} the sum residues 0,1,2,3,4,6 and difference residues 0,±1,±2,±3 give (5,6) at order six and (6,7) at larger orders. Without such an element, primary decomposition gives the listed exceptions or a subgroup C₃², C₅² or C₄×C₂, with direct independent-generator counts (6,7), (6,7), (5,6) on {0,a,b}. Finally, exponent two gives identical sets pointwise and orders three through five saturate both sets whenever 2|A|>|G|; smaller subsets balance by the pair calculation. These arguments cover all quantifiers, including the trivial group and empty subset. The proof in RESULT.md §§1–4 is replayable by exact set arithmetic. VERIFICATION.md and verify.py were inspected but the attached script was not executed; its finite checks do not establish the classification.

## originality

PASS

The supported distinct claim is the all-finite-group classification together with the minimum witness size, not the existence of a specific quaternion, dihedral, or cyclic witness in isolation. No equivalent or dominating statement was identified in the inspected evidence.

## value

PASS

For the standard sum/difference statistic, universal balance is decided by subsets of size at most three, with a sharp size threshold and a local structural obstruction. This is a useful exact complement to larger-subset count and asymptotic-balance results. The quaternion reduction explains why pair testing alone is insufficient even for nonabelian groups; the result is not merely a small-order census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
