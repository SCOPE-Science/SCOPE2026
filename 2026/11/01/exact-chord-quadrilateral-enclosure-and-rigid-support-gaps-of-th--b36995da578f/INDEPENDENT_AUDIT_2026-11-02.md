# Independent mathematical audit

## correctness

PASS

Every chord line direction of a regular heptagon corresponds to one of 14 distinct support normals j*pi/7, odd j supporting heptagon edges at h=cos(pi/7) and even j at h=1. A minimized enclosure can be made support-tight; adding a missing heptagon-edge support strictly improves any containing triangle, so four-support cases suffice. Four ordered supports bound a polygon iff each cyclic index gap is <7; exact combination enumeration yields 511. For successive normal gaps delta, independently derived area equals sum of [h_i h_{i+1}−(h_i²+h_{i+1}²) cos(delta)/2]/sin(delta). The seven cyclic normal sets of type {1,3,7,11} have equal area c²[tan(pi/7)+3tan(2pi/7)], ratio 4/7+3/(7cos(2pi/7)), solving 49r³−84r+8=0, and all others differ by >1/40. Independently reimplemented full rational fixed-point certificate with Machin π bounds and Taylor enclosures; ran all 511 candidates: 7 winners, 504 others, minimum rigorous lower excess 25947319986048213/10^18. Finite enumeration is exhaustive only because geometric support reduction covers all candidates.

## originality

PASS

Best-of-knowledge PASS: the same regular-heptagon numerical benchmark was published by Vígh, so the approximate number alone is not original. The exact closed algebraic ratio, seven support configurations and certified 1/40 separation were absent from the inspected full original and are not implied by universal bounds or an optimized parallelogram formula.

## value

PASS

PASS: resolves an explicit natural benchmark of the recent Kuperberg chord-conjecture program exactly, classifies all optimizers and supplies a certificate separating 504 competitors; the numerical observation alone was incomplete. A sharp self-contained finite result with a mathematical role needs no new universal conjecture proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
