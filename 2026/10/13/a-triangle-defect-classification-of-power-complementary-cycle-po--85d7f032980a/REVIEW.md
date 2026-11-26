# Independent mathematical audit

## correctness

PASS

The distance in C_n^k between distinct vertices is the ceiling of their cyclic distance divided by k: each jump covers at most k and partitioning a shortest cyclic arc attains this bound. Thus the power is C_n^(pk). If it is complete, the complement of C_n^k cannot be complete because it omits every original cycle edge; this is the relevant boundary justification, rather than the complement merely having at least one edge. Otherwise degree equality gives n=2(p+1)k+1. For r=pk, a powered-cycle triangle has cyclic gaps each at most r or at least n-r. The unique-large-gap class is counted n binom(r,2), by the first vertex following the gap and the two positive offsets. If there is no large gap, the deficits from r sum to (p-2)k-1; the class is empty at p=2 and otherwise positivity imposes no additional bound on the weak compositions. Each unordered triangle has three possible cyclic starting vertices, giving the second term (n/3) binom((p-2)k+1,2). Complement triangles have all gaps >=k+1, which also precludes a gap >=n-k. Their count is (n/3) binom((2p-1)k,2). Subtraction gives exactly nk(k-1)/2. This excludes all k>=2. At k=1, n=2p+3 and gcd(p+1,2p+3)=1, so the multiplier p+1 sends the omitted distance-one edges of the complement to the omitted distance-(p+1) edges of the powered cycle. This handles the full integer ranges. The supplied notes, script and recorded output were inspected, not executed. Separate adjacency-mask and common-neighbor counts gave (7,7) at (n,k,p)=(7,1,2) and (272,255) at (17,2,3); these are finite corroboration, not the classification proof.

## originality

PASS

The supported distinct result is the joint all-p classification for consecutive-distance cycle powers together with the exact uniform triangle obstruction at equal degree. The square C7 and cube C9 positives are established and explicitly excluded from the originality claim. Checked exclusions for other graph classes and constructions with nonconsecutive jumps do not cover this family. This is a bounded, best-of-knowledge assessment; the early general graph-equation paper remains an access risk.

## value

PASS

A natural infinite cyclic graph family admits a complete isomorphism classification despite an unbounded degree-matched candidate set. The exact defect isolates a simple invariant obstruction and shows precisely why degree and all positive ordinary-cycle examples do not extend to thicker cycle powers. The mathematical value is the all-exponent obstruction and sharp classification, not novelty of the known example cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
