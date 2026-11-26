# Independent mathematical audit

## correctness

PASS

On X0=1 use u=t+s. The first three nonconstant coordinates recover u,s²,s³ in odd characteristic (the last has coefficient 2 on s³), and every later expansion has no s term. Thus the reduced ring really is k[u,y,z]/(z²−y³), with y=s²,z=s³. Its intrinsic Fitt_2 ideal is (3y²,2z), giving length three in characteristic three and two in all other odd characteristics. There are no extra singularities: the proper tangent-incidence map has singleton geometric fibers in odd characteristic (recover t,s on X0≠0; at a finite base point with X0=0, X1≠0 and X2/X1=2t; the tangent at infinity is disjoint from these and handled by reversal). It is finite, and near the finite pure tangent directions A=v/(1+vt), B=2t−At² have invertible differential in (v,t) at v=0. The induced completed image ring injects into the single completed source ring by finiteness, and A,B already generate that complete regular ring. Reversal gives r=−s/[t(t+ds)]; the s²-leading coefficient of r² is t^−4, so on the reduction the j-th nilpotent grade transforms with weight −4j. Summing dn−4j+1 gives exactly 3dn−9 or 2dn−2. In characteristic two the parity coordinate blocks give the two disjoint Veronese blocks of the smooth scroll S(floor(d/2),floor((d−1)/2)). For d=3 in characteristic three, homogenizing the cusp equation gives the stated irreducible quartic; its two nonzero partials define the supported codimension-two scheme, with the quartic redundant by Euler's identity and Hilbert polynomial 9n−9 by the cubic complete intersection formula.

## originality

PASS

The d=4 characteristic-three specialization and the entire characteristic-two comparison have direct published matches. The distinct assertion supported here is the intrinsic Jacobian singular-scheme filtration and Hilbert polynomial uniformly in all degrees and its odd-characteristic jump; neither the checked special-degree calculation nor general syzygy or scroll theorems give that statement.

## value

PASS

The intrinsic singular scheme is a natural invariant of the reduced tangential surface. The characteristic-three effect is genuinely scheme-theoretic: the reduced cusp support alone misses the jump in the local Jacobian length, and the global grades determine a quantitative degree and Hilbert-polynomial change for an infinite family. Restricting the contribution to the uniform calculation, rather than the already covered quartic or scroll examples, leaves a useful distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
