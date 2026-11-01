# Independent mathematical audit

## correctness

PASS

A binary LSD-first addition state consists of (carry,u,v) with carry∈{0,1} and u,v∈Z/3Z. For each proposed target bit, the transition enumerates all addend digits with the indicated outgoing carry and updates popcount residues. Starting at zero and accepting (0,c,c) is exactly the two-summand property; tracking target popcount supplies the one-summand alternative. The source NFA independently represents the finite lists and geometric repunit/3×power families. A breadth-first search over the finite reachable product of subset states is exhaustive over all finite canonical binary expansions; our separate implementation recovered exactly 108,108,107 reachable states with no comparison mismatch, and directly checked 8193 integers. This is a genuine infinite regular-language equivalence certificate, not extrapolation from a finite integer cutoff. The log-count coefficients follow from residue-class exponents and finite-overlap properties.

## originality

PASS

Compared precise theorems against their implication directions and alternate formulations using inspected primary literature and Resultary; no covering statement identified; residual priority risks remain and absence of a match is not a novelty proof.

## value

PASS

An explicit complete infinite exceptional-set classification is a natural additive invariant of binary automatic sequences. Its three distinct logarithmic growth constants and lacunary families are not mere restatements of generic automata decidability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
