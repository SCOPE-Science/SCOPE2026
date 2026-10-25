# Exact four-point splitting-line spectra of the rational BKS quartic over two small extensions

## Finding

Let \(C\) be the rational plane BKS quartic over \(\mathbb F_3\) with projective equation
\[
Y^4+X^3Z+XZ^3+XY^2Z-X^2Z^2=0.
\]
For \(r\in\{3,4\}\), set \(K_r=\mathbb F_{3^r}\), \(\Omega_r=C(K_r)\), and let \(\mathcal L_{r,4}\) denote the set of projective lines defined over \(K_r\) that contain exactly four **distinct** members of \(\Omega_r\). For each \(P\in\mathbb P^2(K_r)\), put
\[
\nu_r(P)=\#\{\ell\in\mathcal L_{r,4}:P\in\ell\}.
\]
The following are **exact**, without sampling:

| Field | Curve points \(\#\Omega_r\) | Rational four-secants \(\#\mathcal L_{r,4}\) | Exterior points with \(\nu_r(P)=0\) |
|---|---:|---:|---:|
| \(\mathbb F_{27}\) | 31 | 24 | 282 |
| \(\mathbb F_{81}\) | 79 | 204 | 108 |

The entire line-intersection spectrum \((a_0,a_1,a_2,a_3,a_4)\), with \(a_j\) the number of rational lines meeting \(\Omega_r\) in exactly \(j\) distinct rational points, equals
\[
(240,256,195,42,24)\quad(r=3),\qquad
(2520,2290,1515,114,204)\quad(r=4).
\]
The entire incidence spectrum of all projective centers, expressed as \(\nu_r(P):\#\{P:\nu_r(P)=\nu\}\), is
\[
\begin{array}{c|rrrr}
r=3:&0:289&1:312&2:132&4:24;\
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrr}
r=4:&0:111&1:1332&2:2496&3:1248&4:1134&5:240&10:72&18:6&24:4.
\end{array}
\]
On the curve itself the spectra are \(\{0:7,4:24\}\) for \(r=3\), and \(\{0:3,10:72,24:4\}\) for \(r=4\). All other centers in each displayed spectrum lie outside the curve. In particular, **the rational BKS quartic is not four-secant-covering over either \(\mathbb F_{27}\) or \(\mathbb F_{81}\)**: precisely 282 and 108 exterior points, respectively, lie on no rational line splitting completely into four distinct curve points.

## Assumptions and scope

The ground curve is **the specified plane model**, not a smooth genus-three curve; its normalization is rational and it has three ordinary double points over \(\mathbb F_3\). Rational points of the plane curve include these singular points and are counted once each. A four-secant means four *distinct* rational intersection points, never intersection multiplicities and never normalization branches. The theorem concerns exactly the base fields \(K_3\) and \(K_4\), not arbitrary \(q\) or arbitrary extensions. All computations use exact finite-field operations. Its primary subject is arithmetic splitting of line sections of a finite-field algebraic curve.

## Proof

**1. Field models.** Represent each element of \(K_r\) by its unique polynomial of degree less than \(r\) in a residue class \(u\), with coefficients \(0,1,2\). The minimal-polynomial moduli are
\[
r=3:\quad u^3+2u^2+1;\qquad
r=4:\quad u^4+u^3+u^2+1.
\]
The verifier constructs the complete multiplication table by polynomial convolution followed by reduction and checks that every nonzero residue has a multiplicative inverse. Thus each quotient is a field of size \(3^r\) (and in particular each modulus is irreducible). Integer encodings \(\sum_{j=0}^{r-1}a_j3^j\) give a finite exhaustive traversal of all field elements without approximation.

**2. Curve points.** On the affine chart \(Z=1\), the equation is
\[
y^4+x^3+x+xy^2-x^2=0.
\]
Its equivalent characteristic-three form, used in both checkers, is
\[
y^4-(x^3+x)+(y^2-2x)^2=0.
\]
Indeed multiplying the latter by \(2\) in characteristic three yields the former. On \(Z=0\) the original homogeneous polynomial reduces to \(Y^4\), so the **unique** point at infinity is \([1:0:0]\). Evaluating the affine polynomial at every \((x,y)\in K_r^2\) therefore exhausts \(\Omega_r\). This produces 31 and 79 rational plane-curve points, respectively; no projective points are omitted.

**3. Lines and intersections.** Each projective line over \(K_r\) has exactly one of the normalized coefficient triples
\[
(a,b,1),\ a,b\in K_r;\quad (1,b,0),\ b\in K_r;\quad (0,1,0).
\]
There are \(Q^2+Q+1\) such lines, where \(Q=3^r\). For each line with coefficients \((a,b,c)\) and each enumerated curve point \([x:y:z]\), test the exact field equation \(ax+by+cz=0\). Sum its indicator to obtain the exact number of *distinct* rational points on that line. This enumerates all 757 lines for \(Q=27\), respectively all 6,643 lines for \(Q=81\), and produces the two complete intersection spectra asserted above. In particular the numbers of four-secants are 24 and 204.

**4. Every incidence center.** The identical canonical projective triples enumerate every point \([x:y:z]\) of the ambient plane, exactly once. Retain only the four-secants from Step 3. For each center \(P\), count exactly how many retained lines contain \(P\); this is \(\nu_r(P)\) by definition. The two displayed full incidence distributions result. Finally distinguish centers belonging to \(\Omega_r\), as enumerated in Step 2, from the others. The on-curve distributions are \(0:7,4:24\) and \(0:3,10:72,24:4\), leaving the claimed 282 and 108 uncovered off-curve points. No probabilistic or asymptotic step occurs.

**5. Internal consistency and second enumeration.** Writing \(a_j\) for the line-intersection counts and \(N=\#\Omega_r\), the enumerated data independently satisfy
\[
\sum_{j=0}^4a_j=Q^2+Q+1,\qquad
\sum_{j=0}^4j a_j=N(Q+1),\qquad
\sum_{j=0}^4\binom j2 a_j=\binom N2.
\]
These follow by counting lines, incident curve-point/line pairs, and pairs of distinct curve points. The number of four-secant/center incidences also equals \(\#\mathcal L_{r,4}(Q+1)\), matching the first moment of the \(\nu_r\) distributions. More independently, the second checker uses the previously established BKS rational parametrization
\[
P(t)=\bigl(2(t+1)^4,\;2+t+t^3,\;1\bigr)
\]
plus the unique infinity and the three rational nodes \((1,1),(1,2),(2,0)\). It verifies equality to the directly enumerated zero set, constructs every four-secant via lines determined by *pairs* of curve points, and independently enumerates all centers. This route gives exactly the same figures without relying on the first checker's loop over all projective lines. The complete executable constructions appear in the embedded `verify.cpp` and `check_parameter.py` and justify every finite assertion above.

## Verification

Compile using `g++ -std=c++17 -O2 verify.cpp -o verify` and run `./verify`. Run the independent checker using `python3 check_parameter.py`. The former prints both entire distributions and terminates with `VERIFY_OK`; the latter prints `PARAM_OK 3` and `PARAM_OK 4`. Both ran successfully using the actual enclosed code. The first performs exhaustive checks of every affine curve pair, every projective line and every ambient projective center, and confirms inverses of all nonzero field elements. The second independently constructs the rational parametrization set, checks its agreement with the zero locus, obtains four-secants from all pair-generated lines, and recounts incidence centers. These are **finite exhaustive proofs of the specific finite-field assertions**; they are not general proofs for arbitrary extension degrees.

## Relationship to prior work

Korchmáros, Nagy and Szőnyi, *Algebraic approach to the completeness problem for (k,n)-arcs in planes over finite fields*, arXiv:2302.10162v1 (2023), §4.2 and Theorem 7.5, introduce and investigate the BKS curve's rational point sets and the splitting-secants question. They establish general extension-degree results under restrictions, and explicitly leave the BKS cases \(r=3,4\) unresolved. Their equation (5), after specializing \(q=3\), agrees with this plane quartic. The BKS construction and its rational parametrization are **their prior work**, not new here. The present result determines the two indicated small-degree exceptions by full exact arithmetic and gives the entire splitting-line incidence spectra rather than only a completeness verdict. The foundational BKS geometric study is Borges, Korchmáros and Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1. An additional later Hermitian-case arc investigation treats a different curve family, not this specific BKS quartic.

## Limitations

This result concerns the **set of distinct rational points of a singular plane curve**, not its normalization point count. In particular, at a node the two geometric branches do not contribute two distinct points. The finite formulas prove neither a universal formula for \(r>4\) nor an isomorphism classification of covering configurations. The computations are self-contained finite exhaustions, not an independently certified proof or machine proof in a general proof assistant. Absence of a matching table in available searches does not establish global priority: an unindexed earlier arithmetic enumeration remains an originality risk. The cited general theorems are neither reproduced nor claimed to be new.

## References

1. G. Korchmáros, G. P. Nagy and T. Szőnyi, *Algebraic approach to the completeness problem for (k,n)-arcs in planes over finite fields*, arXiv:2302.10162v1 (first public February 20, 2023), later J. Combin. Theory Ser. A 204 (2024), 105851; DOI 10.1016/j.jcta.2023.105851. Source equation (5), parametrization (6), §§4.2, 7.2 and §8.
2. F. Borges, G. Korchmáros and A. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1 (2022), geometric BKS background.
