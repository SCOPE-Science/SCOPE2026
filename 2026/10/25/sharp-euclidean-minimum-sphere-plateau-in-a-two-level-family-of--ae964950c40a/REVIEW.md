# Independent mathematical audit

## correctness

PASS

The actual RESULT.md specifies p,q>=2 and t in [0,1] for K={(x,y): x_i>=0,(1-t)x_i<=y_j,y_j+t x_i<=1}. Independently reconstruct the hull A=(0,epsilon) for epsilon in {0,1}^q and B=(delta,(1-t)1_q) for nonzero delta in {0,1}^p by splitting at M=max_i x_i. For c=(a1_p,1/2 1_q), a=(p-qt(1-t))_+/(2p), every A vertex has squared distance pa^2+q/4. Each B vertex of lower Hamming weight k has exact radius gap qt(1-t)-k(1-2a)>=0, with the claimed contact equality conditions including t=0,1 and qt(1-t)=p. Contact barycenter: if a>0 place weight a at the all-ones B vertex and 1-a on A with Bernoulli parameter (1/2-a(1-t))/(1-a); if a=0 average A. The variance identity shows any other center has strictly larger required squared radius, so this is the unique global smallest sphere. The plateau inequality qt(1-t)>=p has an open interval precisely q>4p. Independent rational arithmetic checked 50 parameter profiles. Proof is for all integer sizes and real t, not inferred from experiments.

## originality

PASS

Qualified PASS for the metric covering-ball and contact-screening theorem, not for the marked-poset construction, vertex symmetry, face-lattice constancy or generic smallest-ball characterization. The exact all-parameter Euclidean outer-sphere law with plateau is not implied by the inspected face-vector, inball/John ellipsoid, or enriched-chain metric statements. Possible old convex-hull-of-cubes covering-ball theorem remains a priority risk.

## value

PASS

The smallest Euclidean covering ball is a natural metric invariant of the standard marked-poset interpolation, and its exact plateau separates combinatorially identical interior polytopes into distinct metric/contact regimes. The theorem classifies all p,q,t and exponentially many contact vertices using a constructive certificate, not a tiny gain or naming substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
