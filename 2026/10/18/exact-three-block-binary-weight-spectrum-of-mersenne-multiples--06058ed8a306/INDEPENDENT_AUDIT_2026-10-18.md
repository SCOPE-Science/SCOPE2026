# Independent mathematical audit

## correctness

PASS

For 0<=N<2^(3m), split into three m-bit blocks x,y,w. Q divides N iff x+y+w in {0,Q,2Q,3Q}; zero excluded and 3Q gives unique all-ones triple. Complement exchanges Q and 2Q, changing weight d to 3m-d. Carry automaton for sum Q has transitions 0->0 count 3 weight1, 0->1 count1 weight3, 1->0 count1 weight0, 1->1 count3 weight2. Return paths: loops at 0 contribute m; any excursion of length L raises weight L-1, so A_m support m..2m-1, complemented support m+1..2m. Two-block analysis and k=2^m+2, 2^m+3 calculations establish least weight m+1. Trace=3z(1+z), det=8z^3 yields Cayley-Hamilton recurrence. Independent newly written enumeration and matrix multiplication agreed for all m=2..8 (87,891 total multipliers), including sharp boundaries and gap; finite test corroborative, not proof.

## originality

PASS

Clokie et al prove Mersenne sturdy minimum-weight bounds and arbitrary later higher-weight existence; neither entails the exact joint three-block weight enumerator, finite spectrum gap or first next-to-minimum multiplier. Stolarsky minimum-weight precedent is credited, not relabeled. Searches did not find an equivalent finite-cutoff classification; the 1980 Stolarsky full text was inaccessible, so residual historical risk persists.

## value

PASS

Binary Hamming-weight spectra for multiples of Mersenne moduli are natural arithmetic-combinatorial invariants. An exact all-m finite-window enumerator and forbidden-weight interval provide nontrivial structure beyond known minimum weights, and a fixed 2-state recurrence enables analysis for arbitrary m.

The dated certificate retains the supplied scientific assessment, sources and limitations.
