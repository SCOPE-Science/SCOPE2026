# Independent mathematical audit

## correctness

PASS

The source defines signed double Italian functions on labels {-1,1,2,3}; leaf and support constraints force minimum arm weight 1 only for (-1,2) when center z>=1, and weight-2 improving arm (3,-1). Center closed-neighborhood sum yields r>=ceil(q/4), ceil((q-1)/4), or ceil((q-2)/4) as z=1,2,3; center -1 forces arm weight >=2. Comparison for every q>=4 gives q+ceil(q/4)+1 and the residue-one center-2 tie. Equality forces the stated binomial optimizer counts. Inspected bundled verify.py, which independently derives arm states and DP q=4..60; did not execute the exhaustive brute-force script. Full foundational Proposition 2 confirms the q=4k upper bound only.

## originality

PASS

Primary Almulhim Proposition 2 (2023) explicitly constructs f of weight 5k+1 for T_{4k} and gives only gamma_sdI<=5k+1; no matching lower bound or optimal-label count in that proposition. The general tree bounds and exact formulas for stars/paths/cycles do not imply the once-subdivided family equality. Subsequent specialized literature could contain it; Resultary attempt was unavailable.

## value

PASS

The exact optimum and complete minimizer classification for a natural tree family close a concrete open inequality in its foundational paper and distinguish signed Italian from signed Roman domination. The q mod 4 two-type change is a genuine structural feature, not merely parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
