# Independent mathematical audit

## correctness

PASS

For each a>=0 the derivative of 0^a splits as h_a+1_S(a)delta_a, where h_a is the indicator of nonempty E_a={0^k1^(a+k): k>=1,a+k in S}; the E_a are pairwise disjoint and disjoint from singleton suffixes {1^j}. Derivatives of 0^a1^b, 1<=b<=a, are delta_(a-b) iff a in S; other derivatives vanish. Unbounded S makes all E_a nonempty and lets every delta_j be generated, giving an isometric closed coordinate-sum c0(N0 disjoint N0). For xi in ell1(words), coefficients A_a=xi(0^a) and B_j=1_S(j)xi(0^j)+sum_{a in S,a>j}xi(0^a1^(a-j)) define bounded Q:ell1(words)->ell1(two indices) with ||Q||<=2, and H=U J Q for the canonical injection J:ell1->c0. J is weakly compact: diagonal coordinate limits of its unit ball stay in ell1 by Fatou, and converge weakly in c0 via its ell1 dual. J is strictly singular: a hypothetical infinite-dimensional isomorphic subspace in c0 gives weakly null unit tail vectors whose inverse under J remains norm-bounded below in ell1, contradicting the Schur property. Noncompactness follows from infinitely many separated q_(0^a) columns. A universal rank-one half-ones approximation and the separation give norm distance exactly 1/2, already known. Independent fresh prefix/suffix tests check 32193 instances on S={2,4}; this is diagnostic, not proof for arbitrary infinite S.

## originality

PASS

Hristov–Ilchev–Nedelcheva–Zlatanov arXiv:2608.15185 provides the general nonregular-language compact distance and approximation number 1/2, explicitly attributed. Its main regularity and Banach geometry results do not yield an isometric c0 normal form or classification as weakly compact plus strictly singular for the arbitrary infinite matched-block family. The new work is the concrete derivative-support factorization and operator-ideal placement; classical Schur/Eberlein–Šmulian lemmas are methods, not claimed innovations. Older weakly almost periodic language theory poses an explicit priority risk.

## value

PASS

The balanced one-counter language is a canonical nonregular example. For every infinite length restriction S, identifying its derivative Banach space isometrically as c0 and locating its noncompact Hankel map simultaneously in the weakly compact and strictly singular operator ideals exposes distinctions invisible to the generic noncompactness theorem. This full natural infinite-family operator-structure classification has independent functional-analytic value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
