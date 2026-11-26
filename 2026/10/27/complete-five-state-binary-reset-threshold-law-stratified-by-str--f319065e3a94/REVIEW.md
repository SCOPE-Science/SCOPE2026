# Independent mathematical audit

## correctness

PASS

The base-five map encoding is a bijection and the ordered product includes loops, repeated letters and all disconnected cases without normalization. A word resets iff it sends the full subset to a singleton. The queue and frontier programs use exact image masks with shortest-layer semantics; if the full set reaches a singleton, a shortest path is simple and fits the supplied loop bound. Strong connectivity, not merely reachability from one root, is equivalent to full forward and reverse closure from a root. The prose at line 55 imprecisely calls this one-vertex reachability, but both implementations test the correct graph property. For an independent complete replay I used reverse preimages starting from all five singletons; the first reach of the full set certifies the shortest length, and exhaustion certifies infinity. A digraph is strongly connected iff it has no nonempty proper forward-closed subset, checked here via intersection of the closed-subset masks for the individual letters. The 47 conjugacy classes of first maps cover all 3125 maps, and multiplying each first-map representative's full second-map scan by its first-map orbit size is exact: conjugation bijects the second maps and preserves threshold and connectivity. The replay matches every published joint row, returns zeros at all larger bins, totals 7,211,281 and 2,554,344 and finite first moments 18,821,345 and 11,030,640. Division gives the stated reduced means and the maxima are read from the table. As a boundary check, tau=1 is equivalent to a constant letter: 2*5*3125−25=31,225. Strong connectivity then requires the other letter's orbit from the constant target to visit all five states, giving 2*5*4!*5=1,200, with no strongly connected both-constant case.

## originality

PASS

The high-threshold marginal class counts and the maximum 16 are prior, and a same-universe indexed census already gives the synchronizing subtotal. The distinct contribution that passes is the full exact threshold-by-strong-connectivity distribution and its conditional and structural consequences in the ordered labelled universe. The strongest prior table and indexed comparisons provide proper fragments or different statistics, not the joint law.

## value

PASS

This exhaustive small-state model directly calibrates sampled averages and randomized two-letter reset experiments with exact denominators. Strong connectivity is a meaningful stratifier: the finite conditional means differ materially, and at this size the positive nonsynchronizing mass and the disappearance of non-strongly-connected finite cases above length 10 are separately measurable, unlike in a single high-tail marginal. The value is the full natural finite benchmark and these comparisons, not re-verification of the already known overall maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
