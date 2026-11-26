# Independent mathematical audit

## correctness

PASS

For a fixed target hub color, the only peripheral options are the two orders of the remaining colors. Their minimum Hamming cost is 2 for an edge monochromatic in the hub color, 0 for an edge already using both remaining colors, and 1 otherwise. This gives the three exact D_c. Their sum is at most 4m+2. With hub 0 and t,t-1,m-2t+1 monochromatic blades in colors 0,1,2, t=floor((m+2)/3), the costs are m+t,m+t,2m-2t+2; all blade multiplicities are nonnegative and the third cost is no smaller. This proves the unrestricted value. At m>=2 a same-profile target must place the singleton color 0 at the hub; every blade then costs at most one, and the hub costs at most one. The parity-specific witnesses have feasible profile (1,m,m) and attain D_0=m+1. Their remaining costs are 3k-1,3k for m=2k and 3k,3k+2 for m=2k+1, proving the weak lower bound for m>=4. For m=2 with singleton off-hub there is at most one monochromatic blade, so the sum bound is 8. For m=3 the bound is 10 with at most one monochromatic blade; with two, the singleton blade must use the majority color different from the source hub by parity, and selecting the source hub costs three. Singleton-at-hub cases cost at most m and the supplied witnesses attain the exceptional weak values. At m=1 the feasible words are already proper. On three copies weak costs add, and cyclic relabeling of an unrestricted extremizer gives a globally feasible balanced profile, because the same relabeling applied to any proper word produces that profile. This proves the copy formula and gap. Direct bounded reproduction generated the 12 proper labelled targets of F_2, tested all 243 source words and all 90 sources with feasible profiles, and got B=3, B_w=2, Fix_3=3. The frozen verifier was inspected, not executed; its reported 15,590 feasible cases for m=1..6 use singleton color 0 for m>=2, a valid symmetry normalization for the maxima. Finite enumeration does not replace the all-m proof.

## originality

PASS

The supported distinct result is the joint exact single-copy census for the friendship family, including the two small weak exceptions and sharp attainment of the general fixing upper bound. The record expressly acknowledges the known repeated-copy identity and derives the family-specific unbounded gap from the new single-copy data. Neither that identity nor the universal fixing bound supplies those data. No exact earlier single-copy coverage was established in the available comparisons.

## value

PASS

Friendship graphs are a natural connected three-chromatic family. Computing the three distances on the same family isolates the price of preserving named multiplicities from the effect of admitting infeasible profiles, and resolves exactly where weak and ordinary villainy coincide. Combined with the known balancing identity, the comparison gives an explicit growing family where globally feasible disturbances across three identical components impose an unbounded extra repair cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
