# Independent mathematical audit

## correctness

PASS

A selected nonendpoint on an m-clique side with a selected vertices requires a−1≥m−a, i.e. a≥h_m. A selected endpoint requires a−1+β≥m−a+1−β, i.e. a+β≥g_m, with β indicating whether the other endpoint is selected. These inequalities give E_m and J_m for one-sided sets; for a connected two-sided set both endpoints must occur. With β=1 a side containing only its endpoint cannot qualify (g_m≥3), and once a≥h_m the endpoint inequality holds. Thus the two-sided count is I_r I_s. A one-sided nonendpoint selection of size h_m exists since h_m≤m−1. For r≥4, put K=h_r+h_s. Degrees K−2 and K−1 are past any one-sided boundary defect (K−2≥h_s+1) and before the product begins. At those degrees the one-sided counts are ordinary binomial coefficients; they decrease strictly in the sum because K−2≤2h_s−2≤s and K−2>s/2. At K the product begins with A_r A_s, A_m=binom(m−1,h_m−1), a central maximum. This exceeds 2A_r+2A_s for r≥5 (both ≥6); for r=4 the left term at K−1 is absent and the right is at most 2A_s<3A_s. For r=3, odd s≥9 leaves an internal gap at degree 4, whereas even s≥4 has a strict drop from h_s to h_s+1 on the decreasing binomial tail (the left can only add at the earlier degree) and a rise at K=h_s+2: binom(s,h_s+1)<2A_s because its two Pascal summands are not both central maxima. Direct substitution confirms the three stated weakly unimodal sequences. Fresh brute-force comparison of all nonempty subsets for 3≤r≤5, r≤s≤8 agreed coefficient by coefficient, with precisely the stated exceptions in that range. This is finite corroboration, not the proof; replay paths are RESULT.md lines 37–98 and the inspected verify.py and verify_output.txt for the package's separate finite tests.

## originality

PASS

Pass for the bridge-joined clique formula and exact unimodality classification. Neither the invariant nor the phenomenon of a non-unimodal strong alliance polynomial is new. No relevant inspected source gives the formula or the if-and-only-if classification for this graph family.

## value

PASS

The bridge is the simplest connected coupling of two complete graphs but changes both the vertex-balance requirement and the connectivity of contributing sets. The exact formula exposes the separation between small one-sided sets and bigger two-sided sets and explains the coefficient valley. The complete classification, including the three genuine exceptions, turns isolated known non-unimodality into a structural infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
