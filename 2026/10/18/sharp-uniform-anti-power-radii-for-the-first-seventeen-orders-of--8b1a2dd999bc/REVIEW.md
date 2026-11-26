# Independent mathematical audit

## correctness

PASS

The recurrence agrees with the odd-part definition. At length 4, even starts have unequal first/third bits and odd starts have unequal second/fourth bits, excluding four of the 16 possible factors. At all other tested lengths L>=7 the published paperfolding complexity is 4L. A separate bounded computation using the odd-part digits and tuple comparisons on the first 2048 symbols reproduced the eight tuples (order, radius, factor count, number obstructing every shorter length, witness index): (2,2,12,6,7), (3,5,60,1,86), (4,6,96,1,3), (5,7,140,3,20), (8,7,224,32,15), (9,9,324,10,100), (16,9,576,258,31), (17,15,1020,4,552). All factors at each tested length k*r had some m<=r. Equality with the exact global factor cardinality, not sample size, certifies all positions. One obstructing actual start at each order gives sharpness. Dropping the last block proves monotonicity and fills both plateaus. Replay: python3 /workspace/branches/21d9a3ae-c20f-4ae8-807c-7da58014fb55/independent_certificate.py; the frozen verify.py was inspected, not executed. No exact values beyond order 17 were verified.

## originality

PASS

The supported increment is the exact worst-start spectrum for literal antipowers in this particular regular paperfolding word, including the 16-to-17 jump, not the anti-power definition, existence, or paperfolding factor complexity.

## value

PASS

The worst-start radius is a natural refinement of quantitative antipower existence for a canonical automatic word. The consecutive initial plateaus, covering the doubling milestones 8 and 16, and the first sharp jump past 16 (9 to 15) give a meaningful finite cutoff and exact benchmarks for any theory of the radius. Neither longer-range regularity nor cutoff optimality in order is presumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
