# Independent mathematical audit

## correctness

PASS

The stage operators are I, I+K and I+K/2+K²/4. The weighted endpoint multiplier is 1+z+(1/2−3ε/2)z²+(1/6−ε/4)z³. Independently expanding the two squared complex multipliers gives 144 times the pure defects as 333ε²+276ε−8 and 18963ε²−8148ε+784. These scalar multipliers are independent of planar phase. Orthogonality gives the energy-weighted sum, with positive leading coefficient on [0,1] and discriminant (9216w²−14490w+5341)/16. Its sorted zeros are (2415±7√7409)/3072, both strictly inside [0,1]. Pure endpoints have positive discriminants; zero discriminant gives one repeated root and negative discriminant gives a strictly positive minimum. At w=2/3 the quadratic has leading coefficient 727/16, vertex 422/2181 and minimum 223/2908. Replay: expand these scaled quadratics and take B²−4AC, dividing by 144² for the actual discriminant. The supplied verify.py was inspected, not executed; the independent calculation is exact and concerns one step only, without restrictions on real ε.

## originality

PASS

Credit the existing fixed-direction RF-SSPRK(3,3) method and general quadratic test. The distinct result is failure of a shared first-step correction despite separate feasibility on both blocks, together with the full fraction frontier in a specified example. Neither the general test nor the closest multimode frontier inspected states or settles that phenomenon under these hypotheses.

## value

PASS

A single scalar couples otherwise decoupled oscillators. This motivated counterexample shows why testing correctability mode by mode is insufficient, even allowing unrestricted real changes to the weights. The exact interval and positive rational gap make it a usable regression example for this structure-preserving method. It does not establish long-time instability, defeat other projection directions, or conflict with small-step existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
