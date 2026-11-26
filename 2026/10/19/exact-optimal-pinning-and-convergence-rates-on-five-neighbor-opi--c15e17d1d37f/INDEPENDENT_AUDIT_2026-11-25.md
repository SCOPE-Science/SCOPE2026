# Independent mathematical audit

## correctness

PASS

For any unpinned cycle, a non-target initial opinion on its vertices persists: those vertices and their two cycle neighbors supply three equal inputs even in the presence of chords; solve the remaining equations with these coordinates fixed and invoke uniqueness. Conversely, order unpinned forest vertices by leaf removal. The jth one sees at least three inputs from pins or earlier removals; a five-input median is between the extreme values of any three inputs. In the shifted, exponentially rescaled coordinates y_i=e^t(x_i−u), pinned values are constant and unpinned derivatives equal the corresponding median of y. Induction and integration give |y_{v_j}|≤R∑_{ℓ=0}^j t^ℓ/ℓ!, proving the all-initial-state bound. In C_n² a triple of consecutive unpinned sites is a triangle. With no such triple, each unpinned edge joins cyclically consecutive unpinned sites, since a length-two shorter arc spanning a third unpin would be such a triple. With no adjacent pins, these consecutive pairs all join into a cycle on at least three unpinned sites; an adjacent pin pair breaks that cycle (zero, one or two unpinned sites are already acyclic). This includes n=5,6, no pins and all pins. The pin bound n≤3p−2 is attained by the stated gap list. Counting ordered deficits from 3 gives p ordered lists at deficit 2, p(p−1) at deficit 3, and binomial(p,2)+p binomial(p−1,2) at deficit 4; from labelled first pins the conversion is n/p. An independent disjoint-set replay counted all 524,256 labelled subsets for n=5…18 and reproduced the forest/gap equivalence and all optimum counts. The frozen verification/verify.py was located and inspected, not run.

## originality

PASS

The forest criterion is a direct consequence of Han et al.'s general cohesive-set criterion and is credited as such. The distinct supported content is the cyclic gap characterization and exact labelled optimum-layout census together with the explicit global time envelope. No inspected exact decycling result or same-graph set census supplies these claims.

## value

PASS

The squared ring is a basic structured nonlinear control example where pin count alone is misleading: an evenly spaced layout can leave a winding cycle while a well-placed adjacent pair breaks it. The formula for every effective gap layout and exact counts among minimum-size layouts give concrete feasibility and robustness information. The all-time uniform bound separately supplies a quantitative guarantee on arbitrary four-regular networks with forest complements; the prior qualitative criterion by itself cannot do that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
