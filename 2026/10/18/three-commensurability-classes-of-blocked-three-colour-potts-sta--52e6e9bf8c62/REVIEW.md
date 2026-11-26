# Independent mathematical audit

## correctness

PASS

Changing an occupied colour c to d in part i changes H by the difference of exterior colour counts, so each used colour must minimize those counts, with ties allowed. An absent global colour would force all used colours to be exclusive, impossible across three nonempty parts with only two colours. A part using all three imposes three equal exterior counts summing to 2n, hence 3 divides n. For 3∤n an exclusive colour forces every colour in that part to be exclusive. Two exclusive colours in one part leave the same third colour on both other parts, where a switch to either exclusive colour would improve. The exclusive-colour part is therefore pure. On the other two parts, if either part is mixed, equality of the exterior counts of its colours forces the opposite part to split equally, which in turn forces the first part to split equally. These are blocked because the third colour has exterior count n to either split part. This gives six proper configurations and, for even n, 9 supports of weight binom(n,n/2)² and energy n²/2. Without exclusive colours the incidence matrix must have exactly two occupied cells in every row and column, so its absent cells are a permutation. The counts in each row are the exterior minima of the two other rows; the three row sums force every such minimum to be n/2. These are blocked since the absent colour has exterior count n. The six supports yield weight binom(n,n/2)³ and energy 3n²/4. For 3|n the all-balanced family gives the stated multinomial-cubed lower bound, and Stirling squeezes its normalized logarithm with the all-colourings upper bound to log 3. The exact nontriple formula yields the other two limits, 0 and log 2. Independent labelled enumeration, looping over 3^(3n) spin words and testing energy changes from the explicit cross-part neighbours, gave histograms {0:6}, {0:6,2:36,3:48}, and {0:6,9:216} for n=1,2,3. This is only corroboration; the proof treats all n.

## originality

PASS

The same stability predicate is established in the stable-colouring literature, but the inspected comparative results do not give the equal tripartite support exhaustion, energy-resolved multiplicities or three arithmetic entropy limits. The closest indexed records either change the stability rule or the graph and ground-state versus blocked-state question. This is a bounded statement-level judgment, not priority certification.

## value

PASS

The balanced complete tripartite graph is a natural symmetric dense geometry in which the three colours compete across parts. The same normalization gives six traps along one infinite arithmetic family, a binomial-scale exponentially large population along a second, and a multinomial-scale rate along a third. This is a failure of the unrestricted kinetic entropy limit, not an equilibrium transition. The exact energy-resolved counts on 3∤n distinguish two trap geometries, so the finding adds a reusable census rather than just another existence argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
