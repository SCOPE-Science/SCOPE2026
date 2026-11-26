# Independent mathematical audit

## correctness

PASS

The radial Hermite formula uses the area coordinate t=π(x²+ξ²). The ratio q_n/q_m is a positive constant times the conditional mean of t^(n−m). Differentiating both moving endpoints expresses its derivative as the sum of two nonnegative terms, the upper-end term strictly positive. At a=0 this is a right derivative, and the ordered Poisson tails give q_n<q_m; the ratio diverges as a→∞. The strict endpoint bounds on the conditional mean give a<B<a+w. The adjacent differences change sign at most once, with at most one zero, excluding a triple equality; a nonadjacent crossing has larger intervening values. For the limit, M(R)≤N_w(R)≤M(R+w) exactly and B≥n/e. To justify the lattice count, use step indicators formed by m=floor(Tx), n=floor(Ty): their integrals are M(T)/T², they are supported in a fixed bounded region, and Stirling gives convergence off the axes, diagonal and the curve I(x,y)=1. This curve has zero area by the parametrization y=e·t^(t/(1−t)), x=ty. Dominated convergence and the Jacobian y yield precisely the stated integral. The width is fixed in area coordinates, and different pairs at one radius are counted separately.

## originality

PASS

The radial formula is established, and the same-date Resultary source contains the adjacent switches and a rising/falling structure that already implies no triple equality. This review does not credit those pieces as distinct. The contribution that survives comparison is the fixed-area-width census of crossings of all Hermite pairs and its common quadratic coefficient; even the entire adjacent staircase supplies only an O(R) subcount. The conditional-moment transversality argument is elementary, but the all-pair census exploits strict area brackets and a two-variable limit not found in the compared statements.

## value

PASS

The incidence count is an exact leading spectral invariant of a natural one-parameter deformation. It measures all mode-pair resonances, including non-maximal ones invisible to the top eigenvalue, and quantifies their growth and independence of fixed width. Width independence and the leading constant are not obtainable from the adjacent-switch census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
