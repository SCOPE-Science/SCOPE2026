# Independent mathematical audit

## correctness

PASS

The Rule 54 truth table gives the stated four pair-state matrices and indexed cyclic trace, without quotienting rotations. The active one-bit block satisfies B_active^3=B_active+I and has Perrin traces at positive exponents; C_k has the Padovan traces from k=1 onward. Idempotence after two zeros reduces longer zero-runs to pairs. A cyclic list with a non-C1 factor can always choose a nonexceptional neighboring pair for the next merge; an all-C1 list of length >=3 starts with the triple merge. A strict trace gain at the final merge suffices even when earlier entrywise gains are masked. Two C1's alone give 3, below P_(n-2) for n>=8. For a single zero-run, fewer than n sites after truncation gives strictness by Padovan growth. Filling isolated zeros is nondecreasing by B^3>=BAB. For a last fill reaching the double-zero target, the strict gap g(a,b) applies, and when there was never an adjacent pair the single-zero comparison suffices. Recurrence reductions with a reduced coordinate >=4 stay in the appropriate positive/base domains, in particular a+b>=5 for g. All-zero has fiber 2. Independent `cd /workspace && python3 review_replay.py 3` derived the matrices from the truth table, checked 35 pair bases (minimum trace gain 1) and 30 singleton-removal bases (minimum gap 3), verified the three comparison seeds (10,4,1), (12,5,2), (17,7,2), and exhaustively checked indexed fibers through n=18 starting at n=8. The proof carries the infinite claim; the frozen checker was inspected, not executed.

## originality

PASS

The inspected literature gives finite-block preimage enumeration, periodic Rule 54 structure, and standard transfer machinery. The relevant indexed findings cover Rule 54 image size or singleton fibers and exact rankings for other rules. None gives or implies the all-n Rule 54 runner-up with its Padovan value and precise adjacent-zero equality class. Conventional homogeneous counting is not itself the contribution.

## value

PASS

Reachable outputs can differ greatly in probability under a uniform predecessor. Exact first and second ranks and the complete tie set answer a natural inverse-count question beyond reachability; the adjacent pair rather than isolated-zero patterns matters for that ranking. The all-length strict classification is useful as a benchmark and the merge inequalities explain the mechanism rather than just tabulating it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
