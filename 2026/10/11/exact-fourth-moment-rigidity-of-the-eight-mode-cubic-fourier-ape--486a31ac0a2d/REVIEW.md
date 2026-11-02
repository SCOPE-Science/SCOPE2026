# Independent mathematical audit

## correctness

PASS

For coefficients on {0,1}^3 with |c|=1 and Haar probability measure, phase normalization fixes c000,c100,c010,c001=1 and leaves A,B,C,D. The coefficient convolution over {0,1,2}^3 yields M=104+4|1+A+B+C|^2+8Re(D conjugate(A+B+C+AB+AC+BC)). The source checker performs exact Laurent-polynomial expansion, and the audit independently verified Git tree identity and checked the stated convolution-grouping and Newton identity 2S2=S1^2-(1+A^2+B^2+C^2). Triangle inequalities yield M>=88, and equality forces A,B,C to be signs, S1=0, exactly two negatives and D=1. Upper coefficientwise triangle equality yields A=B=C=D=1 and M=216. Continuity of connected phase torus yields full interval; each phase orbit has q^4 lifts, and -1 belongs to μq iff q even. No aliasing occurs for finite grid side orders at least three. The supplied checker source was read, not executed afresh; analytic proof rather than finite checks establishes universal phase and all-order conclusions.

## originality

PASS

Best-of-knowledge: the exact single 2x2x2 aperiodic autocorrelation-energy minimum 88 and complete continuous unimodular equality classes are not mathematically implied by the inspected pair constructions, the higher-dimensional BINARY-only theorem, or the examined 2D array-family results. Quadratic path candidates themselves are previously known. An inaccessible relevant 2021 full paper and unindexed small-array tables pose nonzero priority risks; absence of a match is not proof of novelty.

## value

PASS

A full 2x2x2 cube is the smallest Cartesian Fourier aperture genuinely involving three frequencies axes; its fourth moment is directly the aperiodic sidelobe autocorrelation energy. The exact global complex-phase optimum 88, complete three-orbit rigidity, even-q attainability and q^4 counting give a natural signal-design benchmark with genuinely nontrivial optimization beyond the known construction of sign-path candidates. The result is limited to this small but motivated canonical aperture, not a higher-dimensional general optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
