# Independent mathematical audit

## correctness

PASS

If both members of a position are omitted, every possible original witness for its duplicate also sees the omitted original; hence only three omission symbols are needed. A neighboring original witness must itself be selected and see no omission at its other neighboring position; a duplicate witness works only for an original omission and must see no other original omission. These are exactly the two clauses in the radius-two rule, including nonexisting path positions. The cyclic wrap for n=4 remains valid. The independent reconstruction reproduced the displayed potential, all 178 arcs on 81 states, all 90 tight arcs, three simple tight cycles of length eight, and boundary state counts 46 each with maxima −2 and 4. Summing 4w−3≤Δh around a cyclic walk gives the 3n/4 omission bound. Equality forces the entire walk to be tight; decomposition into the checked simple cycles requires an order divisible by eight. For the path, the initial four positions contribute explicitly, and the boundary maxima yield floor((3n+2)/4). Direct graph-level enumeration of 174,672 omission subsets for paths of orders 2–8 and cycles 4–8 confirms the small cases and the four-omission maximum for P6. All 14 path and 8 cycle seeds and the necessary eight-step returns were checked. Inserting at a shared four-symbol state adds six omissions in eight positions while preserving all local constraints and endpoints; induction on each residue class, not the finite sample through order 64, proves attainment for arbitrary orders. Replay: cd /workspace/branches/9c41858f-5640-4e3c-9db1-d616e01b6608 && python3 reproduce_split_certificate.py --full (output certificate_reproduction.log). The frozen verifier was inspected, not run; no claim extends to C3 or arbitrary factors.

## originality

PASS

The exact minima on splitting paths and cycles, with the isolated P6 exception and the mod-eight cycle obstruction, survive the bounded statement-level comparison. The strongest directly relevant prior bound explicitly leaves the neighborhood corona with K1 open in general. Bare-base and ordinary-corona findings concern different graphs or different optimization objectives. This is not an assertion of global priority.

## value

PASS

Paths and cycles are canonical inputs for the explicitly excluded singleton neighborhood-corona case. The exact laws, not just a few small values, identify where the density bound is unattainable: a genuine period-eight obstruction for the cycle and a separate small-order exception for the path. The finite potential and splice argument explain the effect and close both infinite families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
