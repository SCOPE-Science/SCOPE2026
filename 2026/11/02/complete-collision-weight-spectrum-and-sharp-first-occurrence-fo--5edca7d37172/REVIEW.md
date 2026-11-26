# Independent mathematical audit

## correctness

PASS

A based closed de Bruijn walk determines the indexed input and vice versa, also at n=1 and n=2: closure enforces the repeated bits. Matching one common output label per edge gives the pair weight, not twice the weight. The local equation determines the preceding bit from the next two and the output, so agreement on one pair-state forces equality around the ring. Thus distinct-input pairs correspond exactly to the off-diagonal closed walks, and their enumerator is the logarithmic derivative of the off-diagonal determinant. A separate exact polynomial calculation on all 12 off-diagonal states and 20 edges reproduced R=1-2z+z^2-2u^3z^3+2u^3z^4+(u^6-u^4)z^6. It reproduced all ten simple cycles and the two minimizing cycles with a common vertex, verifying the finite inputs of the proof. Independently, using a=z^3/(1-z), R=(1-z)^2(1-a(u^3+u^2))(1-a(u^3-u^2)). The log expansion adds the two signed m-th powers, leaving exactly an even number 2b of u^2 choices. Writing m=c+2b gives positive weight k=3c+4b with first exponent n=3m=k+2b. Minimizing over b congruent to k mod 3 gives the stated formula and excludes exactly 1,2,5. The factor (1-z)^2 gives two zero-weight collisions at each n>=1, starting with the ordered pair 0,1 and its reverse.

## originality

PASS

Credit the explicit evaluated two-variable ordered-collision series and the sharp global support law, not the use of backward pair propagation, trace methods, per-target predecessor counts, or the unweighted image law. A same-day exact Rule 30 image record includes the labelled transformation automaton: its fixed-point counts allow a weighted terminal-state calculation, but the stated image recurrence and unevaluated automaton do not give the explicit reduced polynomial or the all-weight support/minimum without further analysis. The later signed-block record goes further: its theorem entails the positive-weight support law, and its actual proof gives the signed quotient from which the exact R can be evaluated. This very strong later overlap is not credited as an independent corroboration of priority or as evidence of coverage before the frozen entry.

## value

PASS

The output weight makes the indexed predecessor ambiguity sensitive to density instead of only image size or total degree. The compact exact series and its support detect a global weight-five obstruction on all ring lengths, and determine the first possible circumference for every attainable weight. These structural consequences are not read off from a generic per-target counting method, one homogeneous example, or the known unweighted image law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
