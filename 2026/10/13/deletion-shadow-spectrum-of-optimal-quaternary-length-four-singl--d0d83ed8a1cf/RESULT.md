# Deletion-shadow spectrum of optimal quaternary length-four single-deletion codes
## Finding
Let \(B_4=\{0,1,2,3\}\). For a word \(x\in B_4^4\), let \(D_1(x)\subseteq B_4^3\) be the set of distinct words obtained by deleting one coordinate. A code \(C\subseteq B_4^4\) corrects one deletion exactly when the sets \(D_1(x)\), for \(x\in C\), are pairwise disjoint.

The classical optimum is \(|C|=24\). For an optimal code define
\[
n_i=\bigl|\{x\in C:|D_1(x)|=i\}\bigr|,\qquad 1\le i\le4.
\]
Then the complete set of possible shadow-size profiles is exactly
\[
(4,12,0,8),\ (4,10,2,8),\ (4,11,0,9),\ (4,8,4,8),\ (4,9,2,9),\ (4,10,0,10).
\]
Because deletion shadows are disjoint, \(|D_1(C)|=\sum_{i=1}^4 i n_i\). Hence every optimal code covers exactly \(60\), \(62\), or \(64\) of the \(64\) possible received words of length three, and every one of these three values occurs. Equivalently, the only deletion-shadow defects among optimal codes are \(4\), \(2\), and \(0\). The defect-zero cases are exactly the perfect codes.

## Assumptions and scope
The alphabet is the labeled four-symbol set \(B_4\), codewords have length four, and exactly one deletion is to be corrected. Repeated deletion outputs from the same codeword are counted only once, so \(|D_1(x)|\) is the number of distinct one-deletion descendants.

The statement classifies the possible four-component shadow-size profile of every optimal-cardinality code. It does not enumerate all labeled optimal codes or classify them up to alphabet or coordinate symmetries.

## Proof
Kim, Lee, and Oh proved that for every even alphabet size \(q\),
\[
N(4,q,1)=\frac{q^2(q+2)}4.
\]
Thus \(N(4,4,1)=24\). The finite verification independently re-establishes this cardinality by integer optimization.

For each of the \(4^4=256\) words \(w\), introduce a binary variable \(x_w\). For each of the \(4^3=64\) possible received words \(y\), impose the exact set-packing constraint
\[
\sum_{w:\,y\in D_1(w)}x_w\le1.
\]
Impose additionally \(\sum_w x_w=24\). Since feasible integral solutions are exactly optimal-cardinality one-deletion-correcting codes, the shadow coverage is the linear objective
\[
\sum_w |D_1(w)|x_w.
\]
Its exact integer minimum and maximum are \(60\) and \(64\). Feasibility tests at each intervening integer show that \(61\) and \(63\) are impossible, while \(60\), \(62\), and \(64\) are all attained.

There are \(4\), \(36\), \(108\), and \(108\) ambient words having respectively one, two, three, and four distinct deletion descendants. For every nonnegative integer quadruple \((n_1,n_2,n_3,n_4)\) with \(n_1+n_2+n_3+n_4=24\) and total coverage between \(60\) and \(64\), the verifier adds four exact cardinality constraints selecting exactly \(n_i\) words of shadow size \(i\). Exhaustive feasibility testing over all such integer quadruples leaves exactly the six profiles stated above. Explicit witnesses for all six are included in `witnesses.json` and independently checked for disjoint shadows.

## Verification
`verify_profiles.py` reconstructs all \(256\) words and all \(64\) deletion outputs. It first proves the optimum cardinality \(24\), then proves the coverage range \(60\) through \(64\), excludes coverage \(61\) and \(63\), exhausts every candidate profile in that range, and checks one explicit code for each surviving profile. The mixed-integer models use binary integrality and a zero requested relative MIP gap.

The verifier also reconstructs the explicit quaternary optimum printed as Table 2 by Kim, Lee, and Oh. That historical code has profile \((4,12,0,8)\) and covers \(60\) received words, so it realizes the largest possible defect. The supplied witnesses additionally realize both defect \(2\) profiles and all three perfect profiles.

A fresh replay from the packaged path returned:
`VERIFY_OK vertices=256 outputs=64 maximum=24 coverage_values=60,62,64 profiles=4,12,0,8;4,10,2,8;4,11,0,9;4,8,4,8;4,9,2,9;4,10,0,10 paper_table2_profile=4,12,0,8 witnesses_sha256=21ce37204e76e412d7dfece07bb0b4d723719dc932b764545e5b0cb3488b5fc2`

## Relationship to prior work
Kim, Lee, and Oh proved the sharp even-alphabet cardinality formula and gave an explicit optimal code for \(q=4\). They later modify their construction to obtain an optimal perfect code for every even \(q\). Thus the literature already establishes that maximum cardinality and perfectness can coexist and that their displayed quaternary optimum need not be perfect. It does not state the complete shadow-profile spectrum of all quaternary maxima.

Kulkarni and Kiyavash formulate deletion-code optimization as a hypergraph matching and integer program, providing a general framework for nonasymptotic bounds. That framework does not imply which shadow-size profiles occur at equality in the specific quaternary length-four optimum.

Targeted searches under the equivalent formulations “quaternary length-four single-deletion code,” “deletion-shadow profile,” “perfect versus nonperfect optimal code,” and the exact coverage values did not identify a prior statement equivalent to the six-profile classification.

## Limitations
The exclusion of the other finite profiles is computer-assisted through mixed-integer branch-and-bound, rather than a short symbolic classification theorem. The supplied verifier reconstructs the complete finite model and the six positive witnesses, but it is not a proof-assistant certificate in exact rational arithmetic. No claim is made about the number of labeled codes in each profile, their symmetry orbits, or analogous spectra for other alphabet sizes.

A residual originality risk remains that an obscure or unindexed finite enumeration could contain the same profile spectrum.

## References
1. H. K. Kim, J. Y. Lee, and D. Y. Oh, “Optimal codes in deletion and insertion metric,” arXiv:0810.3729, first public version 2008-10-21 UTC.
2. H. K. Kim, J. Y. Lee, and D. Y. Oh, “Construction of optimal codes in deletion and insertion metric,” arXiv:1003.4057; *IEEE Transactions on Information Theory* 56(7) (2010), 3217–3220, DOI 10.1109/TIT.2010.2048492.
3. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128; *IEEE Transactions on Information Theory* 59(8) (2013), 5115–5130.
