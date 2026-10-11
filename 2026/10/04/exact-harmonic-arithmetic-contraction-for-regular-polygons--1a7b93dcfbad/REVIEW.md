# Independent mathematical audit

## correctness

PASS

For even \(n\), central symmetry makes both symmetrizations equal to the polygon. For odd \(n\), with unit circumradius, \(r=\cos(\pi/n)\), \(c=\cos(\pi/(2n))\), and asymmetry \(s=1/r\), polarity gives \(P_n^\circ=s(-P_n)\) and hence \(H_n=rA_n^\circ\). The half-difference body \(A_n\) is a regular \(2n\)-gon of circumradius \(c\) and inradius \(c^2\); its polar is rotated by half a sector with circumradius \(1/c^2\). Therefore the vertices of \(H_n\) lie in side-normal directions of \(A_n\), and the least centered containment factor is \(r/c^4=4s/(s+1)^2\). Opposite contact points saturate a supporting-strip width, which rules out improvement by translation. Independent symbolic reconstruction verified \(r/c^4=4s/(s+1)^2\), and the package polygon checker reconstructs the operations through \(n=51\). The all-\(n\) claim rests on the regular-polygon/polar argument, not the finite replay.

## originality

PASS

The 2021/2023 primary paper gives the sharp planar lower envelope \(4s/(s+1)^2\) for harmonic-to-arithmetic containment and separately analyzes regular odd polygons in the reverse containment direction. The inspected regular-polygon example does not supply the missing forward inclusion equality for odd \(n\ge5\). A universal lower bound cannot by itself show that this canonical family attains it, and the reverse factor does not imply the forward factor. The audited polarity calculation provides the matching upper inclusion. Current Resultary searches return the assigned regular-polygon equality record as the exact hit and no stronger statement identifying all odd regular polygons as lower-envelope extremizers.

## value

PASS

Regular polygons are canonical test bodies for sharp symmetrization inequalities. Showing that every odd regular polygon hits the known sharp planar lower envelope supplies a natural infinite equality family, extends the prior triangle endpoint, and quantifies the quartic approach to symmetry. That is a motivated exact geometric classification even though the final polar calculation is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
