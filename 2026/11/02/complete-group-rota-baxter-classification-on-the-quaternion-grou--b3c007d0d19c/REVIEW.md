# Scientific review: group Rota–Baxter operators on the quaternion group

## Correctness — PASS

The derivation is a two-branch exhaustive proof. The group identity forces \(B(1)=1\); the unique involution and centrality force \(B(-1)\) to be either \(1\) or \(-1\). When it is \(1\), the map \(B\) factors as a homomorphism through the elementary-abelian quotient \(Q_8/Z\) and must land in the center. When it is \(-1\), the auxiliary map \(g\mapsto gB(g)\) factors through the same quotient and again has central image. Both families satisfy the original equation. There are four characters, their two forms are disjoint, and the image/cardinality/orbit/dual statements are proved directly. The uniqueness of the quaternion involution rules out nontrivial exact subgroup factorizations. A C++17 exhaustive checker evaluated every one of the \(8^7\) normalized functions (not just sampled cases); a separately coded Python implementation checked the eight normal forms and duals. Outputs and reproduction steps appear in `VERIFICATION.md`.

## Originality — PASS, with explicit residual risk

Savelyev's 2026 extraspecial-group classification explicitly treats odd primes \(p\ge3\); the quaternion group is an extraspecial \(2\)-group and falls outside those asserted results. The dihedral/alternating-group classification concerns other finite-group families. The general group Rota–Baxter literature supplies the operator identity and constructions and is not claimed as new. Targeted bibliographic searches for quaternion/Hamiltonian/extraspecial \(2\)-groups and a mathematical-record semantic comparison did not return a complete \(Q_8\) classification, while adjacent records about *linear* operators on quaternion or exterior algebras have different objects and axioms. No claim of an exhaustive literature census or guaranteed historical priority is made. A relevant paper's accessible abstract/introduction and odd-prime restrictions were inspected; full inspection was unavailable, and older small-group group-operator tables could still contain an equivalent result.

## Mathematical value — PASS

The smallest nonabelian extraspecial \(2\)-group is a natural structural boundary excluded from an emerging odd-prime classification. A normal-form theorem for every group operator, exact count and image-size profile, automorphism orbits, dual bijectivity obstruction and splitting classification together characterize this boundary. This is a finite complete classification supported by a short conceptual quotient argument, not an arbitrary partial enumeration. It does not solve the general extraspecial \(2\)-group problem.

## Scope and priority limitation

The theorem applies only to weight-one group-theoretic operators on \(Q_8\). The general operator identity, central-character examples, and trivial/inversion operators predate this work. It is not a classification of linear Rota–Baxter operators over a quaternion algebra, and unindexed historical work may supersede the priority claim. Independent human or formal verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
