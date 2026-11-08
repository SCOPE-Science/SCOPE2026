# Independent mathematical audit

## correctness

PASS

The final RESULT proves an exact extremum of the odd Schubert numerator p among two-bridge knots of crossing c>=3: M_c=F_{c+1} unless c≡2 (mod 3), and M_c=F_{c+1}-F_{c-4} in that residue class (F_0=0,F_1=1). Every positive continuant of total twist weight c is generated from (P,Q)=(1,1) by c-1 operations (P,Q)->(P+Q,Q) (increase last digit) or (P,Q)->(P+Q,P) (append 1); conversely reduction from any positive word reaches (1). Since P>=Q>0, preserving the larger second coordinate dominates all future first coordinates, giving the universal F_{c+1} bound. F_{c+1} is even exactly when c≡2 (mod 3). The first effective non-greedy choice at weight j (2<=j<=c-2) loses exactly F_{j-1}F_{c-j-1} compared with the all-greedy path under subsequent greedy choices. The identity F_r F_s - F_{r+s-2}=F_{r-2}F_{s-2} for r,s>=2 (and easy r=1 or s=1 boundary checks) proves a loss >=F_{c-4}. Reduced positive alternating rational diagrams (3) at c=3, (2,1^{c-4},2) when c>=4 and c≢2, (3,2) at c=5, and (2,2,1^{c-6},2) for c>=8 and c≡2 have exactly c crossings and attain the specified odd continuants. The cited Kim--Morifuji estimate N<=16p^2 on the stated irreducible curve component then yields N<=16M_c^2 conditionally on that published input; the constant 16 is not rederived from character-variety theory in this package. Independent reimplementation enumerated all positive compositions for c=3..18 and checked witnesses and Fibonacci identities, but this finite test is not the infinite proof. The source statement properly distinguishes sharpness of p from any unattested sharpness of N.

## originality

PASS

Best-of-knowledge original as an exact fixed-crossing odd-continuant/Schubert-numerator maximum, and consequently a parity-refined uniform two-bridge specialization of the monic-character estimate. The classical determinant recurrence and all-one Fibonacci observation do not themselves give the optimal odd value in the obstructed congruence class; published global determinant maxima differ (OEIS A345130: global eight-crossing maximum 45 versus the claimed two-bridge 31). The recent character-count paper supplies a parameter-dependent estimate and discusses crossing bounds; its full text could not be independently retrieved here, so no whole-paper NOT_COVERING assertion is made about that source. Targeted Resultary searches returned this identical finding and unrelated knot facts, not a distinct antecedent; targeted external searches did not expose an implication-equivalent preexisting two-bridge theorem. Searches do not prove novelty; possible inaccessible exact coverage is a stated risk.

## value

PASS

The problem optimizes a natural classical knot invariant (odd Schubert numerator/determinant) over the entire natural two-bridge class at fixed minimal crossing number. The parity obstruction identifies a meaningful knot/link boundary, and the exact Fibonacci correction requires a global continuant optimization rather than a table lookup. Combining this reusable sharp extremum with the new Kim--Morifuji character-variety estimate provides a uniform bound of exponential scale φ^(2c), strictly better than the generic 8^c-scale crossing estimate. The paper does not pretend that 16M_c^2 is attained by any character variety. This is a motivated, self-contained structural extremal lemma of plausible use for rational-knot determinant and monic-character questions, not an arbitrary tiny numeric change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
