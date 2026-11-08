# Independent mathematical audit

## correctness

PASS

On x=0 and 2<b<8/3, centered order-3 cardinal B-spline support entails exactly k=-3,-2,-1,0,1,2,3; symmetric sum is cubic P_b(t) in t=cos(2*pi*nu) with coefficients from B3(k/b). Direct checks recover P_b(-1)=-3(b-2)^2/(4b^2)<0 and P_b(-1/2)=(3b-8)^2/(8b^2)>0. Möbius substitution t=(u-1)/(u+1) yields coefficient signs with exactly one change for 2<b<=78/31; for 78/31<b<8/3 the derivative of P_b has positive leading coefficient and negative discriminant, so P_b is increasing. Hence precisely one t_b in (-1,-1/2), and two conjugate frequencies nu_b and 1-nu_b. The root is simple and analytic in the chamber. At b=2, P_2=(t+1)^2/2 gives h=t+1~[(6+sqrt42)/4](b-2), hence square-root departure of nu from 1/2. At b=8/3, P_t=3/32, P_b=0, P_bb=81/256 yield t_b+1/2=-(27/16)(8/3-b)^2+O((8/3-b)^3) and the stated frequency coefficient. Independent symbolic checks confirmed endpoint signs, derivatives and exact rational isolations at b=201/100,9/4,13/5; finite samples were not used as an all-b proof.

## originality

PASS

The directly relevant Hasannasab–Lemvig (arXiv:2609.13116) primary abstract advertises a complete B2 hat-spline classification for all scales and higher-order classification for lambda>1, while the assessed B3 chamber corresponds to lambda=1/b in (3/8,1/2), strictly below one. Its full text was unavailable via arXiv, OA mirrors and authorized institutional access (VPN disconnected); no assertion of full-document noncoverage is made. A nonprimary detailed synopsis notes more complicated higher-order zeros and rational Gabor obstructions, without identifying this exact x=0 B3 moving branch. Earlier Lemvig–Nielsen and Lemvig frame-set works concern rational zeros and nonframe conditions, not complete continuously moving quadratic-spline x=0 zero pairs. Best-of-knowledge novelty is qualified by inability to read the closest full paper and possibly implicit trigonometric-polynomial literature.

## value

PASS

A complete support-knot chamber of symmetry-axis zeros for the smallest odd-order B-spline resolves a natural local classification problem, including both pair multiplicity and distinct endpoint critical exponents. Zak zeros directly inform Gabor frame obstructions although no frame-set result follows here. The cutoff 8/3 is dictated by activation of the k=+-4 spline sample, not an arbitrary numerical interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
