# Independent mathematical audit

## correctness

PASS

For a finite product of fields, vertices have nonempty proper support A; ordinary zero-divisor graph adjacency means disjoint supports. Nonzero annihilator supports are subsets of A^c and B^c, so weak adjacency requires choosing distinct annihilator coordinates, equivalent to |A^c∪B^c|≥2. For distinct support classes, the weak-minus-ordinary difference graph joins exactly intersecting supports; an individual class of size |A|≤t-2 is itself complete, whereas coatom classes are internally independent. Thus cliques are weighted intersecting support families, weight a^{|A|} for sizes≤t-2 (a=q-1≥2), weight 1 per coatom. Among families without singleton supports, every coatom can be added; complementary pairs of sizes 2 through t-2 contribute at most a^{max(|A|,t-|A|)}; choosing all >half supports and one from each complementary middle pair attains this bound because any noncomplementary half-sets intersect. A family with singleton {i} is bounded by full i-star, whose apparent singleton advantage over the coatom-complete choice is a-1. A complementary pair {i,j}, [t]\{i,j} has t≥5 and contributes gain at least a^{t-2}-a²≥a²(a-1)>a-1 to the nonsingleton choice, while all other complementary pair contributions are no smaller. Hence no singleton-family maximizes. Strict a>1 forces the larger support from every unequal-size complementary pair, all coatoms and exactly one half-set of every middle pair, proving the full equality classification and count a^{t(t-1)} times 2^{binom(t,t/2)/2} in even dimension. Independent SCIPY HiGHS MILP in integer support space returned globally optimal status and exact values 85,275,326,1491,1239 at (t,q)=(5,3),(5,4),(6,3),(6,4),(7,3), and independent enumeration verified all 2^10=1024 complementary middle choices for t=6; infinite claim follows from combinatorial inequalities, not these finite optimizations.

## originality

PASS

Wani 2026 precisely introduced the same weak zero-divisor difference graph, proved the support reduction, determined small t=3,4 clique numbers, and posed exact general t≥5 as Question 6.11 with upper/lower bounds. The homogeneous q≥3 special family here is a substantive part of that open regime and the new strict singleton-star comparison removes the remaining coatom contribution gap; full equality classification and number of maximizing vertex-cliques also go beyond Wani. Filmus 2016 provides a broad weighted Ahlswede–Khachatrian theorem for full Boolean-lattice product measure; that weight differs crucially at coatoms and omits the full support, so it does not directly give the claimed ring graph theorem. No identical stronger theorem was identified; traditional weighted intersecting-family machinery may simplify the proof but does not erase this natural exact application.

## value

PASS

The same-object foundational 2026 paper specifically asks for the exact clique number when t≥5, and homogeneous products of equal finite fields form a natural symmetric infinite family. The theorem determines not only the sharp clique number but all its maximizing support structures and counts actual vertex cliques, with an essential q≥3 rigidity boundary; this is a motivated structural subcase of a genuine open extremal problem rather than a harmless weight substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
