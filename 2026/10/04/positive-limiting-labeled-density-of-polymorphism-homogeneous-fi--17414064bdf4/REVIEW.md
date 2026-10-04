# Review: Positive limiting labeled density of polymorphism-homogeneous finite abelian groups

## Correctness
PASS. The decisive classification premise is Theorem 4.7 of Tóth--Waldhauser: for finite abelian groups, polymorphism-homogeneity is equivalent to every Sylow subgroup being homocyclic. The counting step is orbit-stabilizer: a group isomorphism type \(G\) contributes \(N!/|\operatorname{Aut}(G)|\) labeled laws on an \(N\)-element set. For the homocyclic \(p\)-group \((\mathbb Z/p^e\mathbb Z)^m\), the automorphism group is \(\operatorname{GL}_m(\mathbb Z/p^e\mathbb Z)\) with order \(p^{m^2e}\prod_{j=1}^m(1-p^{-j})\). Substituting \(em=a\), dividing by the classical total mass \(p^{-a}/\prod_{j=1}^a(1-p^{-j})\), and factoring across Sylow subgroups gives the stated formula. The limit follows because the \(m=1\) term is the finite product \(\prod_{j=2}^a(1-p^{-j})\) and all remaining divisor terms total at most \(\tau(a)p^{-a}\). The verifier independently checks partition-by-partition masses and sample densities.

## Originality
PASS with residual folklore risk. Tóth--Waldhauser state the homocyclic-Sylow classification but do not enumerate labeled group laws or derive a density. Majumder and the Cohen--Lenstra literature provide the reciprocal-automorphism mass but do not connect it to polymorphism-homogeneity. Searches combining the exact model-theoretic property with homocyclic groups, labeled laws, and Cohen--Lenstra weighting found no source stating the displayed density, its multiplicativity over prime powers, or its fixed-prime limiting constant. The deduction is short enough that an unindexed folklore observation remains possible.

## Value
PASS. The classification by isomorphism type alone does not indicate how frequently the property occurs among concrete finite operation tables. The exact formula shows a non-obvious phenomenon: at fixed prime, the labeled density does not go to zero as the order grows through \(p\)-powers, but converges to an explicit positive constant. This links a model-theoretic extension property to the canonical automorphism-weighted distribution on finite abelian groups and gives an immediately reusable statistic for random labeled group-law models.

## Closest literature and limitations
The closest source is Tóth--Waldhauser, Theorem 4.7, which supplies the structural classification but no enumeration. The Hall--Cohen--Lenstra mass identity supplies the normalization over all abelian \(p\)-groups. No uniform asymptotic with both \(p\) and \(a\) varying is claimed, and the result is about labeled operation tables rather than the unweighted distribution on isomorphism classes.

Same-model review: passed. Independent audit: not yet performed.
