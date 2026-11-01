# Independent mathematical audit

## correctness

PASS

The rule depends only on center color c and exact set S of occupied leaf colors, yielding exactly 3(2³−1)=21 support states and exact deterministic support-map Φ. I independently rebuilt all 21 transitions and their first hitting times (0..6 or never), finding only (2,{0,1,2}) nonsynchronizing. For any r, a support set of size j represents precisely U1=1, U2=2^r−2 or U3=3^r−3·2^r+3 surjective assignments of labelled leaves. Weighting the 21 support states by their first-hit times proves every histogram entry and total 3^{r+1}, with r=1 boundary sharp maximum three and r≥2 sharp maximum six. Independent direct full labelled-state simulations for r=1..7 agreed with the claimed counts, including ∞. As r→∞, times 5,6,∞ each have proportion 1/3. The all-r proof is the complete finite state quotient, not an extrapolated enumeration.

## originality

PASS

Lyu introduced this inhibitory finite-state pulse-coupled rule and proved qualitative degree/branching synchronization obstructions; a later paper treats tree recurrence and worst-case complexity. Those results already imply failure of universal synchronization for stars with at least three leaves but not the full labelled first-hit-time histogram and macroscopically split 5/6/∞ basins. The support-state classification is a concrete quantitative refinement not found in actual Resultary or inspected Lyu star sections.

## value

PASS

The complete labelled basin/hitting-time distribution on the simplest branching tree is a natural finite-state dynamics classification. It resolves what fraction of starts synchronize, exactly when, and how non-synchronizing orbits coexist, refining known graph-theoretic thresholds; the 1/3–1/3–1/3 asymptotic basin partition and uniform six-step cutoff are meaningful dynamical invariants, not an arbitrary tiny graph computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
