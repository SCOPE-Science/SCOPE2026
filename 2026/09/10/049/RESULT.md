# No 9-direction graph in the AGL-normalized monic degree-7 family over F_13

## Context
For a function f:F_13→F_13 let D(f) be its determined slopes. The graph construction gives a Rédei-type blocking set of size 13+|D(f)|. Size-22 Rédei-type minimal blocking sets in PG(2,13) were already reported by Kadoo (2010); therefore the question addressed here is **not** global existence. It is the narrower classification question whether a 9-direction graph occurs in the natural degree-7=(13+1)/2 polynomial family after the standard affine normalizations.

Ball's direction theorem allows N=|D(f)|≥8 for q=13 and does not forbid N=9. Csajbók's later structural work concerns the small-direction regime and does not give the census below.

## Normalized family
Every degree-7 polynomial with nonzero leading coefficient is direction-cardinality equivalent, under output scaling, input translation, and vertical translation, to

    f(x)=x^7+a5 x^5+a4 x^4+a3 x^3+a2 x^2+a1 x,

with a1,…,a5∈F_13. Input translation kills the x^6 coefficient because 7 is invertible mod 13. Thus there are 13^5=371293 normalized representatives.

## Result
An exhaustive exact census of all 371293 representatives gives

    |D|=8:      13
    |D|=11:    117
    |D|=12:   1196
    |D|=13: 369967
    |D|=9:       0.

Hence no polynomial in this normalized monic degree-7 family yields a 22-point graph-type Rédei set. This is a family obstruction only; it is compatible with Kadoo's prior existence of size-22 Rédei-type minimal blocking sets by other functions/models.

## Verification
The filed pure-Python slope-set enumeration and an independent vectorized Vandermonde/slopes recensus agree exactly on all 371293 functions. The normalization invariances are algebraic and preserve |D|. Blocking/minimality logic for graph constructions is standard; since N=9 never occurs in this family, no 22-point candidate arises here.

## Limitations
- No claim of global size-22 nonexistence is made; size-22 Rédei-type examples are already known from Kadoo (2010).
- The result only excludes degree-7 polynomials up to the stated affine normalizations.
- The exact histogram is computationally exhaustive but finite; reproducibility depends on correct F_13 arithmetic, mitigated by two independent implementations.

## References
- S. Ball, The number of directions determined by a function over a finite field, JCTA 104 (2003), 341–350. DOI 10.1016/j.jcta.2003.09.006.
- B. Csajbók, On bisecants of Rédei type blocking sets and applications, arXiv:1504.06748.
- F. H. Kadoo, The Minimal Blocking Set Of Size 22 In PG(2,13), Al-Rafidain J. Comput. Sci. Math. 7(2) (2010), 77–88. DOI 10.33899/csmj.2010.163898.
