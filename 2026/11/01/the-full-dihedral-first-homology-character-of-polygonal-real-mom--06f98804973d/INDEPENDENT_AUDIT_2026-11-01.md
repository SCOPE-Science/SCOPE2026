# Independent mathematical audit

## correctness

PASS

PASS. For n>=5, verified the actual cubical active-set cell counts C0=2^n,C1=n2^(n-1),C2=n2^(n-2) and the coefficient-product fundamental 2-cycle: at each oriented 1-cell the two square boundaries cancel, giving top homology Q and its rotation +1/reflection -1 orientation character. Fixed-cell traces under a nonidentity r^k are (2^gcd(n,k),0,0), giving H1 trace 2-2^gcd. Odd reflections give (2^q,2^(q-1),-2^(q-1)); even vertex- and edge-reflections give (2^q,2^q,0) or (2^q,0,-2^q), all with alternating sum zero. Identity gives dim H1=2+(n-4)2^(n-2). Prime p traces vanish off identity and the resulting rational character is the regular D_p character times the stated integer multiplicity. Checked source verify_polygon.py, its finite n=5..14 trace tests and n=5..10 boundary enumeration; finite range is supplementary, uniform argument is the proof. The n=5 case is separately known.

## originality

PASS

PASS on the composite/all-n individual dihedral character at best of knowledge, NOT novelty of genus, Betti numbers, orbit-space invariants or prime-p quotient ranks. Kamiyama 2012 full text Theorems A and B computes H1 of D_n and C_n quotient spaces, including ranks 1,7,163 for n=5,7,11; its rank formula already implies the prime regular-representation multiplicity in combination with vanishing restricted traces, so this prime-number endpoint is not standalone novelty. These finitely many orbit-space ranks and cyclic averages do not mathematically determine all individual rotation traces for composite n or each reflection-type trace. Kamiyama 2012 additional Lefschetz paper plausibly overlaps but full body was not accessible here and is a residual priority risk.

## value

PASS

PASS. An explicit entire-family equivariant homology character of a geometrically canonical surface is a nontrivial representation refinement of known nonequivariant genus and quotient homology. Individual symmetry traces and composite-n behavior can be used for equivariant character decompositions, not obtained merely by renaming a Betti formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
