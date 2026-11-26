# Independent mathematical audit

## correctness

PASS

For a first nonlinear term a t^{d+1}, N sends t^i into degrees ≥i+d, with coefficient i a at i+d. In a j-fold iterate the coefficient at i+jd is a^j times the product of i+hd for h=0,…,j−1; terms of higher filtration cannot contribute there. In the tame range, if that degree survives, all factors lie in [1,m−1−d]⊆[1,p−1], giving one independent pivot per surviving i and no other nonconstant inputs. At m=p+d+1, N kills t^p by Frobenius since p(d+1)≥m, and kills t^{p+1} and higher by filtration. At power j, any input with i+(j−1)d≥p is therefore killed; all remaining positive i give distinct nonzero pivots by the same product. This reproduces both ranks and the fixed ideals with constants; the one-rank loss is relative to the tame prediction only when that prediction is positive, as specified in the Finding, not for already zero powers. The ranks identify the two shift partitions by chains in residues 1,…,d and the extra singleton blocks. At the common truncation the depth-(d+1) map is tame. The two ranks at j=1 are p−1, while at j=2 they are max(p−1−d,0) and max(p−2−d,0); when both are zero all later powers vanish, proving the exact collision criterion. This works also in characteristic 2. Counting the first nonzero and later coefficients gives the stratum sizes and, in the short tame range, fixed dimension d+1 and distinct ranks for distinct depths. Static inspection of artifacts/verify.py:39–153 and VERIFICATION.md:19–26 confirms direct finite matrix-power checks in the specified regimes and selected comparisons, not a proof for arbitrary truncations. No frozen code was executed.

## originality

PASS

Credit is limited to the complete natural-module rank profiles, sharp first loss, and first-wild collision criterion. Substitution matrices, their filtration estimate and Frobenius support restrictions are known; the short-range fixed-space count is included as context rather than credited as novel. Exact statement comparisons did not supply the higher-power ranks or the different-depth natural-module similarity criterion. In particular the previously inaccessible exponent paper was retrieved and inspected at its relevant matrix and ramification lemmas. Its aim and results use p-power matrices to track compositions, not all natural-module ranks.

## value

PASS

The natural module is a canonical representation of these truncated groups. The formula finds the exact boundary of coefficient-independent shift ranks and shows exactly when this representation first fails to distinguish consecutive depths. It yields full similarity information, not merely group order or fixed-space size. The all-characteristic transition and its sharp collision criterion provide substantive structure beyond a routine enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
