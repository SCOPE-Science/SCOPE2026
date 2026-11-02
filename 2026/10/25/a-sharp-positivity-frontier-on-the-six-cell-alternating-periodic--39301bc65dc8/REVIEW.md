# Independent mathematical audit

## correctness

PASS

For a six-element periodic P1 heat FEM mesh with alternating edges a,b, consistent mass M has offdiagonal h/6, stiffness K offdiagonal -1/h. For tau>0, independent exact 3-mode cyclic Fourier reduction of 6x6 D=M+tau K verifies P_{0,2}=2tau(6tau-a²)(ab+b²+6tau)/H and P_{0,4}=2tau(6tau-b²)(a²+ab+6tau)/H, H=(ab+6tau)(ab+12tau)(a²+3ab+b²+6tau)>0. Hence positivity forces tau>=max(a²,b²)/6. Conversely at or above threshold offdiagonals D<=0, strict row diagonal dominance by D1=M1>0, so D inverse nonnegative M matrix and P=D^-1M>=0; tau=0 gives identity. Six independent exact rational 6x6 inversions and fully symbolic mode decomposition confirm both entries. The proof covers every a,b>0 including equal case and endpoint equality.

## originality

PASS

The mesh-dependent lower-step M-matrix maximum-principle condition is classical, notably Li–Huang Theorem 3.1. The exact necessity for the six-element alternating periodic mesh is a distinct sign calculation. Inspected general theorem supplies sufficient condition only; no identified prior exact same six-cell necessity table. Best-of-knowledge PASS with risk of older specialized FEM analyses.

## value

PASS

A sharp positivity-preservation frontier for the smallest meaningful three-period alternating mesh tests necessity of a widespread sufficient maximum-principle condition. The exact negative nonadjacent entries detect failure below the boundary for arbitrary mesh contrast and are naturally relevant to preserving physical bounds of heat discretizations. The result is narrow but a complete motivated sharp classification, not a generic textbook M-matrix sufficiency restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
