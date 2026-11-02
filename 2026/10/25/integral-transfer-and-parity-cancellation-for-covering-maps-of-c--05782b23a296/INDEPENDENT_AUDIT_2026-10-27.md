# Independent mathematical audit

## correctness

PASS

For m>=4,n>=5,k,l>=1 the canonical reduction C_kn→C_n and pullback C_lm→C_m define the Hom-complex map. The circle-sector component classification excludes strict equality |kn·w|=m (isolated maps). For a target cycle length t>=5, the cubical covering of a circle component has primitive deck period t/gcd(t,2); evaluation along a primitive deck generator traverses the target circle 2/gcd(t,2)=d(t) times. The evaluation map is natural under postcomposition by C_kn→C_n (geometric degree k) and under precomposition by the source cover fixing vertex 0. Comparing evaluation degrees forces D=k*d(kn)/d(n): k/2 precisely if n odd and k even, otherwise k. Strict inequality and parity guarantee that mapped circle sectors remain circles. Repeating edge step sequence l times gives winding k*l*w; odd/even target labels govern sector merges. Within each target sector every mapped generator has the same positive integer coefficient D, giving a single Smith invariant D for each hit row; hence ker Z^(B-s) and coker (Z/D)^s⊕Z^(T-s). Independently enumerated homomorphism colorings for 5 mixed-parity cases and checked winding conversion; source finite script examines closed paths but the universal argument is the deck normalization and naturality, not enumeration.

## originality

PASS

Čukić–Kozlov classify winding and circle/point components, Fujii et al. construct the explicit universal cover and deck generator, and Dochtermann gives graph Hom functoriality. These strong premises make the degree extraction short and transparent, but their inspected statements do not give this exact integer map for arbitrary simultaneous cyclic coverings, the parity-primitive two-sheeted exception, or the full kernel/torsion-cokernel classification across target sectors. It is a direct derived invariant, not an independently discovered new circle topology; an implicit corollary in these sources remains a genuine risk.

## value

PASS

Canonical covering-induced maps are natural morphisms whose first-homology Smith factors are not captured by classifying components individually. The parity cancellation distinguishes an odd-target two-fold map of index one from an even-target map of index two, and the complete integral sectorwise kernel/cokernel controls genuinely different functorial invariants for all winding admissibilities. This motivated exact interpretation goes beyond a rephrasing of Betti numbers, albeit with a short proof using known deck data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
