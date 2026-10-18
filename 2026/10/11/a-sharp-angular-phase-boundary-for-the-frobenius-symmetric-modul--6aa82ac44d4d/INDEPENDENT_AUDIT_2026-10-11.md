# Independent mathematical audit

## correctness

PASS

For the displayed rank-one A=a[[x,0],[sqrt(1-x²),0]] and B=at E22, the orthogonal column supports give |A||B|=0. The 2x2 Cayley--Hamilton square-root identity for Z is |Z|=(Z*Z+|det Z|I)/sqrt(tr Z*Z+2|det Z|) for nonzero Z; applying to Z and Z* and taking squared Frobenius traces yields exactly Δ/a²=t(1-x²)(2x-1-2xt-t²)/(1+2xt+t²). The exact polynomial identity was independently reconstructed and the inspected standard-library checker verifies it coefficientwise and at rational a=5,x=4/5,y=3/5,t=1/5 (positive defect 27/85). For x∈[0,1),t>0 the signs are solely those of the strictly decreasing quadratic 2x-1-2xt-t²; the positive root T(x)=sqrt(x²+2x-1)-x exists iff x>1/2, is increasing to sqrt(2)-1, while x=1 or t=0 yields Δ=0. This proves all endpoints and the stated exact phase diagram, not a global unrestricted matrix inequality.

## originality

PASS

Bourin--Lee raised triangle bounds for the symmetric modulus, and Zhang already disproved unrestricted Frobenius subadditivity with an invertible 2x2 example. Those broad counterexamples are acknowledged as prior. The new claim is the complete signed phase diagram within a natural sparse rank-one orthogonal-input-support family with explicit angular cutoff x=1/2 and coupling threshold, which the inspected Zhang Section 8 does not state or imply. The exact arbitrary-pair failure is not claimed as new. The Resultary lookup failed and unindexed same-family examples remain possible.

## value

PASS

The angular/coupling sign threshold is a natural complete local classification for the simplest rank-one setting with disjoint input supports of a current operator-inequality problem. It separates positive-defect, equality and negative-defect regions exactly, beyond merely recovering the already-known existence of Frobenius counterexamples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
