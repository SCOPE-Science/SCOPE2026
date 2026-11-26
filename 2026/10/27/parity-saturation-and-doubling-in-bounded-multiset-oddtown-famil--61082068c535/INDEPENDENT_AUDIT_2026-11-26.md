# Independent mathematical audit

## correctness

PASS

Equal coordinate-parity patterns give an odd intersection, so each odd-weight pattern contributes at most once. Separately, encoding each multiplicity x_i as the initial segment of length x_i in an m-slot block gives identity Gram matrix over F_2 and the mn bound. The size-4 and size-8 witnesses meet the parity bound and remain feasible as the cap increases. At exact cap 3 and n=4, all maximizers occupy all eight parity classes. Independent enumeration builds one selection from each class and keeps precisely pairwise-compatible choices, exhausting 128 odd vectors and giving six full families; comparing with all 24 coordinate permutations gives exactly the same six families. A different traversal count in the frozen checker is not a mathematical invariant. Replay: /workspace/branches/a3a05a0a-b4ce-4725-8e7e-609e097e4b78/independent_oddtown_check.py with arguments 3 or 4 (see independent_check_n3.out and independent_check_n4.out in the same directory). The uploaded script was inspected, not executed. Concatenating disjoint-support families by zero padding preserves within-block intersections and gives zero across blocks; the excess of 8a+b_r over 2n−2 is respectively 2, 1, 0, 0. This establishes the unbounded claim by construction, not by sampling. No n>4 extremal classification is certified.

## originality

PASS

The supported distinct content is the cap-three parity saturation at n=3,4 (and the extension in m by the same witnesses), the six labelled maximizing families in one coordinate orbit at cap three and n=4, and the resulting density-two amplifier. The classical Gram bound and the disjoint-support operation are not new mechanisms. The inspected sources do not give the decisive cap-three witnesses or extremizer classification; the closest lower-cap results have different exact maxima and a smaller proved asymptotic construction ratio. This is a best-of-knowledge comparison, not historical priority certification.

## value

PASS

The finite orbit classifies exactly how the cap-three model first attains its full eight-pattern ceiling, whereas the cap-two optimum on the same four labels is only six. More than a table entry, that four-coordinate witness gives a uniform lower bound of 2n−2 and a limiting lower density of two per coordinate, versus one for ordinary Oddtown and the inspected cap-two amplifier's 5/3. The finite and asymptotic aspects support each other without claiming the new lower bound is optimal in larger dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
