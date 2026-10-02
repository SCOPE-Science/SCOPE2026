# Minimal Rédei-type blocking sets in PG(2,13) at sizes 21, 23, 24 with direction spectra and a size-22 graph-family narrowing lemma

## Context

Small minimal blocking sets in prime-order projective planes are classical objects connected with direction sets of functions over finite fields. For p=13, the Blokhuis lower bound for a nontrivial blocking set is 3(p+1)/2=21. Size 22 is not globally open: Kadoo (2010) reported a 22-point minimal blocking set of Rédei type in PG(2,13). The contribution here is instead an explicit witness package at sizes 21, 23 and 24, together with a finite exclusion for low-complexity graph functions that could produce exactly nine directions.

## Definitions

Work in PG(2,13), with 183 points and 183 lines. A blocking set meets every line; it is minimal when every point is essential, equivalently every point lies on a tangent line meeting the set only there.

For a function f:F_13->F_13 let U={(x,f(x),1):x in F_13} and let D(f) be the set of slopes (f(x)-f(y))/(x-y) for x!=y. The graph-type Rédei blocking set used here is B=U union {(1,m,0):m in D(f)}. Its size is 13+|D(f)|. The line spectrum records how many projective lines meet B in exactly i points.

## Result

### Theorem 1: verified witnesses

The following graph-type Rédei sets are minimal blocking sets in PG(2,13):

| name | f(x) | |D(f)| | D(f) | |B| | line spectrum |
|---|---|---:|---|---:|---|
| W21 | \(x^7\) | 8 | {1,3,4,5,8,9,10,12} | 21 | 1:126, 2:18, 3:36, 8:3 |
| W23 | \(x^9+x^5\) | 10 | {0,1,2,3,4,5,9,10,11,12} | 23 | 1:96, 2:52, 3:32, 6:1, 10:2 |
| W24 | \(x^7+2x^3\) | 11 | {0,1,2,3,4,6,7,9,10,11,12} | 24 | 1:91, 2:59, 3:16, 4:14, 6:2, 11:1 |

For each witness, exact finite-field recomputation confirms the displayed direction set, the expected number of points on the Rédei line, incidence with every one of the 183 lines, a tangent through every point, the complete line spectrum, and the standard Rédei divisibility condition for every undetermined slope. W21 attains the size-21 Blokhuis lower bound.

### Theorem 2: low-complexity graph-family exclusion for size 22

A graph-type Rédei blocking set of size 22 requires |D(f)|=9. Exhaustive computation over F_13 gives no function with nine directions in any of these families:

- all monomials \(a x^e\), whose attained direction counts are {1,8,12,13};
- all binomials \(a x^e+b x^j\), with counts {1,8,10,11,12,13};
- all monic trinomials \(x^e+a x^j+b x^k\), with counts {8,10,11,12,13};
- all degree <=6 polynomials after the standard output-scaling, linear-term and constant normalizations, with counts {1,11,12,13}.

Consequently, within the graph-function model, any nine-direction polynomial representative must have at least four nonzero terms and degree at least 7. This is a family obstruction only; it is not a claim of global size-22 nonexistence.

## Proof / evidence

`artifacts/verify.py` reconstructs PG(2,13) exactly and checks the three witness sets from the displayed polynomials. `artifacts/polylog.py` exhausts the four polynomial families with exact arithmetic. The normalizations preserve the number of directions because f -> a*f+m*x+c sends each secant slope s to a*s+m, a bijection of F_13 when a is nonzero. Thus the normalized degree<=6 and monic trinomial scans cover the stated families.

A fresh independent recensus reproduced every direction set, line spectrum, blocking/minimality verdict, and the four N-value sets above.

## Limitations

- Kadoo (2010) already reports existence of a 22-point minimal blocking set of Rédei type in PG(2,13); this record does not claim otherwise.
- Theorem 2 is only a low-complexity graph-function exclusion. Other graph representations and broader Rédei constructions are not excluded.
- No PGL(3,13)-uniqueness or exhaustiveness is claimed at sizes 21, 23 or 24; the result supplies one certified representative at each listed size.
- The certificates are finite computations over F_13, not general classification theorems.

## Reproducibility

Run `python3 artifacts/verify.py` for the projective-plane witness checks and `python3 artifacts/polylog.py` for the polynomial-family exclusion.

## References

- F. H. Kadoo, “The Minimal Blocking Set Of Size 22 In PG(2,13),” Al-Rafidain Journal of Computer Sciences and Mathematics 7(2) (2010), 77–88. DOI: 10.33899/csmj.2010.163898.
- S. Ball, “The number of directions determined by a function over a finite field,” Journal of Combinatorial Theory, Series A 104 (2003), 341–350. DOI: 10.1016/j.jcta.2003.09.006.
- B. Csajbók, “On bisecants of Rédei type blocking sets and applications,” arXiv:1504.06748.
- “Full Characterization of Minimal Linear Codes as Cutting Blocking Sets,” arXiv:1911.09867.
