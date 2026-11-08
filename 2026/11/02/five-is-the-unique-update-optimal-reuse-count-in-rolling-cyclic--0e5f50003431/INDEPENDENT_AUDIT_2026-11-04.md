# Independent mathematical audit

## correctness

PASS

For the stated source-derived rate sigma_ell (sqrt2 for ell1,2; 2 for ell3; root (2ell-3+sqrt((2ell-3)^2-8))/2 for ell>=4), independent differentiation gives F=log(sigma)/ell and Fprime=-H/ell², H=log(sigma)-2ell/sqrt((2ell-3)^2-8), Hprime>0. Exact rational bounds establish H(5)>0 and sigma5^4>sigma4^5; sigma5²>32 dominates ell1,2,3. Thus all ell>=6 strictly inferior and ell=5 unique. I independently verified rational inequalities and first 100 candidate slopes, supplementary only. The claim is CONDITIONAL on the original rate formula/transfer-to-every-update and common generic set; full primary theorem could not be independently inspected due to access, so its hypotheses remain a prominent validity risk rather than pretending source verification.

## originality

PASS

Original Ran Gu 2026 theorem supplies delayed Ritz recurrence, its fixed-ell sigma_ell and per-update rate (credited); surviving mathematical claim is optimization over infinitely many ell with sharp unique integer solution. Other cyclic steepest-descent and safeguarded RASG analyses have different algorithms. Original exact source arxiv:2610.32705 was abstract-only via arxiv/OA, with authorized Oxford retrieval blocked vpn_disconnected, so the possibility it already optimizes ell cannot be ruled out by an abstract; priority judgment expressly qualified.

## value

PASS

Choice of how many times to reuse historical Ritz steps is an algorithm-design parameter; global exact update-normalized optimum with a strict tail proof is mathematically motivated despite a small rate difference from ell=4. Restricted exact active-spectrum regime and asymptotic gradient updates, not claimed practical wall-clock optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
