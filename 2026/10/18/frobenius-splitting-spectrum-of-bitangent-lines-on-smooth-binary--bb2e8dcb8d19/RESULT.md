# Frobenius splitting spectrum of bitangent lines on smooth binary plane quartics

## Finding
Let \(F\) range over the \(2^{15}-1=32{,}767\) nonzero homogeneous quartic equations in \(\mathbf F_2[X,Y,Z]\). For every geometrically smooth curve \(C_F: F=0\), a **geometric bitangent line** means a line over \(\overline{\mathbf F}_2\) whose intersection divisor on \(C_F\) is twice an effective divisor of degree two, including the hyperflex case. The lengths of the Frobenius orbits of distinct geometric bitangent lines constitute the **splitting partition**. Curves and equations are counted with their fixed plane embedding; the projective-orbit column identifies orbits under \(\operatorname{PGL}_3(\mathbf F_2)\).

Exactly \(10{,}920\) equations are geometrically smooth, forming \(78\) projective equivalence classes. The complete splitting distribution is:

| Frobenius cycle partition | Smooth equations | Projective classes |
|:--|--:|--:|
| \((1)\) | 1,344 | 10 |
| \((1,1)\) | 1,344 | 10 |
| \((1,1,1,1)\) | 112 | 2 |
| \((1,1,2)\) | 1,008 | 7 |
| \((1,3)\) | 1,568 | 10 |
| \((1,1,1,1,1,1,1)\) | 1 | 1 |
| \((1,1,1,2,2)\) | 105 | 2 |
| \((1,2,4)\) | 966 | 7 |
| \((1,3,3)\) | 1,400 | 9 |
| \((7)\) | **3,072** | **20** |
| **Total** | **10,920** | **78** |

In particular, \(3{,}072\) equations have seven geometric bitangents forming a single Frobenius orbit: no bitangent is rational over any proper subfield of \(\mathbf F_{2^7}\) that contains \(\mathbf F_2\). These equations occupy \(20\) projective orbits. The absence of rational bitangents by itself is not claimed as new: the complete rational-bitangent marginal was computed previously. The new assertion is the **full field-of-definition partition census** and its projective-class refinement.

The explicit curve
\[
X^3Y+X^3Z+XZ^3+Y^3Z=0
\]
represents one seven-cycle class; it has five \(\mathbf F_2\)-rational points and projective orbit size \(168\). In the model \(\mathbf F_{128}=\mathbf F_2[\alpha]/(\alpha^7+\alpha+1)\), the seven geometric bitangents are the Frobenius conjugates of
\[
X+(\alpha^3+1)Y+(\alpha^3+\alpha+1)Z=0.
\]
Here integers \(9\) and \(11\) represent the respective polynomial-basis coefficients \(\alpha^3+1\) and \(\alpha^3+\alpha+1\). Their orbit is length seven, as checked by direct substitution.

## Assumptions and scope
All coefficients lie in \(\mathbf F_2\), curves are geometrically smooth plane quartics, bitangents are geometric lines satisfying the stated even-contact condition, and Frobenius acts by squaring line coefficients. No claim is made for quartics over a larger base field, singular quartics, abstract curves without the marked plane model, or odd characteristic. Every equation over \(\mathbf F_2\) is uniquely normalized because its only nonzero scalar is one. The genus of each smooth plane quartic is three.

## Proof
**1. Exhaustive projective-curve reduction.** Order the fifteen degree-four monomials lexicographically, starting \(X^4,X^3Y,X^3Z\) and ending \(Z^4\), and encode an equation by a fifteen-bit nonzero mask. The source file `enumerate_quartics.py` generates the transformations \(X\mapsto X+Y\) and \((X,Y,Z)\mapsto(Y,Z,X)\). Their matrix closure has order \(168\), hence equals \(\operatorname{GL}_3(\mathbf F_2)=\operatorname{PGL}_3(\mathbf F_2)\). Breadth-first orbit enumeration partitions all \(32{,}767\) masks into \(279\) orbits. For each orbit representative \(F\), on each affine chart \(W=1\) (with \(W=X,Y,Z\)), calculate the ideal \((f,\partial_u f,\partial_v f)\) in \(\mathbf F_2[u,v]\). The curve is geometrically smooth precisely when the reduced Gröbner basis of each such ideal is \(\{1\}\), since the geometric singular locus is empty if and only if each localized Jacobian ideal is the unit ideal over an algebraic closure. This yields \(78\) smooth orbits of weighted size \(10{,}920\), with full representative and orbit-size evidence in `quartic_orbits.json`.

**2. Exact bitangent criterion in characteristic two.** Parametrize a projective line by independent vectors \(P,Q\). Write the restricted binary quartic as
\[
F(sP+tQ)=c_4s^4+c_3s^3t+c_2s^2t^2+c_1st^3+c_0t^4.
\]
Its divisor is even over an algebraic closure if and only if it is the square of a binary quadratic, equivalently \(c_3=c_1=0\): in characteristic two a square contains only even exponents, and every coefficient has a square root over \(\overline{\mathbf F}_2\). This equivalence also covers two coincident contacts, so no hyperflex line is omitted. The test is invariant under changing the line parametrization and under projective transformations.

**3. Fixed lines and Frobenius cycles.** For each \(k=1,\dots,7\), work in the explicitly specified degree-\(k\) field \(\mathbf F_{2^k}\). Every rational projective line has a unique coefficient triple in one of the forms \((1,b,c),(0,1,c),(0,0,1)\), so there are \(2^{2k}+2^k+1\) lines to test. Count those with \(c_3=c_1=0\). If \(N_k\) denotes this count and \(m_d\) the number of Frobenius orbits of length \(d\), then
\[
N_k=\sum_{d\mid k}d\,m_d,\qquad
m_k=\frac{N_k-\sum_{d\mid k,\ d<k}d\,m_d}{k}.
\]
The geometric bitangent count of a smooth plane quartic in characteristic two is known to be \(1,2,4\) or \(7\), according as its Jacobian \(2\)-rank is \(0,1,2\) or \(3\) (Resmini; Stöhr--Voloch, as cited by Dolgachev--Kondō). Each Frobenius orbit of at most seven distinct geometric lines has length at most seven. Hence the searches through degree seven recover **every** cycle without extrapolating from bounded field experiments. The independent Hasse--Witt stable-rank calculation verifies the predicted total number \(1,2,4,7\) in each of the \(78\) cases. Summing the orbit sizes produces exactly the table above.

**4. Explicit seven-cycle witness.** In `splitting_orbits.csv`, equation mask `2566` is smooth of orbit size \(168\), with \(N_1=\cdots=N_6=0\) and \(N_7=7\); direct line evaluation yields seven bitangent coefficient pairs in the polynomial model of \(\mathbf F_{128}\): \((9,11),(65,69),(97,113),(121,127),(63,43),(75,93),(37,55)\), visited in that order by Frobenius squaring. Their orbit exhausts all geometric bitangents by the known seven-line bound. Its Cartier--Manin matrix has rank three, consistent with ordinary Jacobian \(2\)-rank.

## Verification
All checks described here are reproducible without external services or proprietary software. With Python 3 plus SymPy and a C++17 compiler, execute from one directory:

```
python enumerate_quartics.py
g++ -O2 -std=c++17 bitangent_spectrum.cpp -o primary
./primary
g++ -O2 -std=c++17 independent_spectrum.cpp -o independent
./independent
python analyze_splitting.py
```

The two C++ implementations independently compute all \(78\times7\) fixed-line counts: one extracts the odd coefficients by binary expansions, and the other constructs full restricted polynomials by convolution. They use different irreducible field polynomials for extension degrees three through seven. Both agree exactly, and the Python checker additionally verifies Hasse--Witt stable ranks, the sum of orbit multiplicities, and all ten weighted distributions. See `README.md` for input/output formats and `splittings.tsv` for the raw fixed-line and Möbius-inverted counts. Every relevant field-defining polynomial in both programs was separately checked irreducible over \(\mathbf F_2\).

## Relationship to prior work
The correspondence between geometric bitangent counts \(1,2,4,7\) and characteristic-two Hasse--Witt ranks is classical (Resmini 1970; Stöhr and Voloch 1987) and is specifically invoked by Dolgachev and Kondō (2024, Section 6); it is **not** a new part of this result. Their paper principally studies bitangent *surfaces* to quartic hypersurfaces in \(\mathbf P^3\), not the finite-field orbit distribution of lines tangent to plane quartic *curves*. Lercier, Ritzenthaler, Rovetta and Sijsling (2014) classify plane quartics using parameter families predominantly in characteristics at least five and do not supply this binary splitting census. Top's small-field genus-three study primarily concerns maximal point counts. An earlier exact count of rational even-contact lines among binary smooth quartics gives the \(k=1\) marginal (and totals \(10{,}920\) equations), but the extensions \(k=2,\dots,7\), cycle partitions, and \(78\)-orbit refinement were not contained in that statement. A complete earlier zeta-function / \(2\)-torsion table might imply part of the spectrum; none of the examined sources supplied such a table. Literature nonappearance cannot certify novelty.

## Limitations
This is an exact, finite-field computation and an exhaustive classification only for \(\mathbf F_2\) plane quartics, not a uniform theorem over all characteristic-two fields. The two programs independently implement the line-contact computation but use the same separately enumerated list of \(78\) smooth orbit representatives; the geometric smoothness enumeration itself uses one Gröbner-basis implementation. The Hasse--Witt cross-check and total geometric bitangent theorem give further safeguards, but they are not independent validation by a separate research group. Possible unindexed historical classifications and the stronger possibility of deriving the distribution from a pre-existing complete Frobenius-on-two-torsion census remain priority risks. No external independent audit is claimed.

## References
1. I. Dolgachev and S. Kondō, *Bitangent surfaces and involutions of quartic surfaces*, arXiv:2406.16246v1 (first public 2024-06-24), especially the introduction and the known characteristic-two plane-quartic bitangent counts in Section 6. https://arxiv.org/html/2406.16246v1
2. M. J. de Resmini, *Sulle quartiche piane sopra un di caratteristica due*, Ricerche di Matematica 19 (1970), 133–160; cited by Dolgachev--Kondō.
3. K.-O. Stöhr and J. F. Voloch, *A formula for the Cartier operator on plane algebraic curves*, J. Reine Angew. Math. 377 (1987), 49–64; cited by Dolgachev--Kondō.
4. R. Lercier, C. Ritzenthaler, J. Rovetta and J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562 (2014). https://arxiv.org/pdf/1403.0562
5. J. Top, *Curves of genus 3 over small finite fields*, 2003. https://www.math.rug.nl/~top/curves.pdf
