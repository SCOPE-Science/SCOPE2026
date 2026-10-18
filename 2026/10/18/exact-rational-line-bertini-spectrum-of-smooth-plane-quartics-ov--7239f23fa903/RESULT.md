# Exact rational-line Bertini spectrum of smooth plane quartics over \(\mathbf F_2\)

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_2}\) range over geometrically smooth plane quartics. Define \(t(C)\) to be the number of the seven rational projective lines \(L\) for which \(C\cap L\) consists of four **distinct geometric points**, counted over an algebraic closure. Then the exact distribution, counting distinct projective equations over \(\mathbf F_2\), is:

| \(t(C)\) | Number of quartics | Projective orbit count |
|---:|---:|---:|
| 0 | 25 | 2 |
| 1 | 168 | 1 |
| 2 | 588 | 4 |
| 3 | 2604 | 19 |
| 4 | 3885 | 26 |
| 5 | 2940 | 19 |
| 6 | 686 | 6 |
| 7 | 24 | 1 |
| **Total** | **10920** | **78** |

Thus exactly \(25\) of the \(10920\) smooth plane quartics are transverse-free; the conditional exact proportion is \(5/2184\). The transverse-free locus consists of one projective orbit of size \(24\) whose curves have all seven rational points, and one fixed projective class represented by
\[
X^4+X^2Y^2+X^2YZ+X^2Z^2+XY^2Z+XYZ^2+Y^4+Y^2Z^2+Z^4=0,
\]
which has no rational points. This particular split is a refinement of the spectrum, not a claim of first discovering smooth plane-filling quartics.

The complete joint distribution by \(n(C)=\#C(\mathbf F_2)\) and \(t(C)\) consists of the following nonzero counts; every omitted pair has count zero:

| \(n(C)\) | \(t(C)\) | Number | \(n(C)\) | \(t(C)\) | Number |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 5 | 84 |
| 0 | 6 | 56 | 0 | 7 | 24 |
| 1 | 3 | 84 | 1 | 5 | 504 |
| 1 | 6 | 420 | 2 | 3 | 84 |
| 2 | 4 | 756 | 2 | 5 | 1596 |
| 2 | 6 | 210 | 3 | 3 | 420 |
| 3 | 4 | 2184 | 3 | 5 | 756 |
| 4 | 3 | 1596 | 4 | 4 | 945 |
| 5 | 2 | 588 | 5 | 3 | 420 |
| 6 | 1 | 168 | 7 | 0 | 24 |

## Assumptions and scope
All curves and coordinates are over \(\mathbf F_2\), while smoothness and transversality mean geometric smoothness and intersections over \(\overline{\mathbf F}_2\). A quartic is represented uniquely by its nonzero homogeneous degree-four ternary polynomial: scalar equivalence is trivial because \(\mathbf F_2^\times\) has one element. Thus the count covers all \(2^{15}-1=32767\) quartic equations, not merely chosen normal forms. Projective orbits are under \(\operatorname{PGL}_3(\mathbf F_2)\), of order \(168\), not under absolute curve isomorphism. Every smooth quartic has genus three. A transverse rational line need not meet the curve in rational points.

## Proof
**1. A complete algebraic smoothness test.** Let \(S=\mathbf F_2[X,Y,Z]\), let \(F\in S_4\), and let \(J=(F,F_X,F_Y,F_Z)\). The curve is geometrically smooth exactly when the four generators have no common projective zero over the algebraic closure. Form the degree-ten multiplication map
\[
\Phi_F:S_6\oplus S_7^{\oplus3}\longrightarrow S_{10},\quad (A,B,C,D)\longmapsto AF+BF_X+CF_Y+DF_Z.
\]
Since \(\dim S_{10}=66\), the criterion used is \(\operatorname{rank}\Phi_F=66\).

We justify the converse rather than assume a finite truncation is exhaustive. If the four generators have no common projective zero, the degree-four linear system spanned by \(F\) and the nine products \(X_iF_{X_j}\) is base-point free. Over the infinite algebraic closure, three generic degree-four members of this linear system have no common projective zero. They form a homogeneous regular sequence of degrees \((4,4,4)\); its Artinian quotient has socle degree \(3(4-1)=9\). Hence every degree-ten form is in their ideal, so \(J_{10}=S_{10}\) and \(\Phi_F\) is surjective. Conversely surjectivity forces the common projective zero locus to be empty. The test therefore certifies geometric, not merely rational, smoothness.

**2. An exact restriction test for each rational line.** Each of the seven lines corresponds to one of the seven two-dimensional subspaces of \(\mathbf F_2^3\). Choose a basis \((u,v)\) and restrict \(F\) to the binary quartic
\[
f(s,t)=as^4+bs^3t+cs^2t^2+dst^3+et^4.
\]
In characteristic two the two partial derivatives vanish simultaneously where \(bs^2+dt^2=0\); if \(b=d=0\), the restriction is inseparable and not transverse. Otherwise the unique critical geometric point is \([s:t]=[\sqrt d:\sqrt b]\). Substituting it into \(f\), and exploiting \(b,d\in\mathbf F_2\), yields this exact transversality test: \((b,d)=(1,0)\) requires \(e=1\); \((b,d)=(0,1)\) requires \(a=1\); \((b,d)=(1,1)\) requires \(a+c+e=1\). The test is equivalent to square-freeness and makes no assertion based solely on rational intersection points.

**3. Exhaustion and projective classes.** Order the 15 degree-four monomials as descending lexicographic triples of exponents, and encode each form by its 15-bit coefficient mask. The bundled `verify_quartic_spectrum.py` generates the \(66\times136\) binary matrix of \(\Phi_F\), eliminates it over \(\mathbf F_2\) using integer bit operations, evaluates the seven binary line restrictions, and independently computes \(\#C(\mathbf F_2)\) by seven point evaluations. Enumerating every mask \(1,\ldots,32767\) gives exactly \(10920\) full-rank forms and the two histograms printed above. It then constructs all \(168\) invertible ternary coordinate changes and their orbits, exhaustively partitions the \(10920\) forms into \(78\) orbits, and verifies the orbit-count column.

The two transverse-free orbit representatives have coefficient masks \(21945\) and \(6670\), with orbit sizes \(1\) and \(24\), respectively. The first is the explicit displayed equation; it has no rational point. The second has seven rational points and belongs to the previously studied plane-filling quartic family. All these are exact finite computations, completed over the entire parameter space. There is no interpolation from sampled finite-field points to geometric smoothness.

## Verification
Execute `python3 verify_quartic_spectrum.py` in the directory containing the bundled files; Python 3 alone suffices. The script asserts all counts above, all \(78\) orbits, the full joint spectrum, and the two transverse-free orbit sizes and rational-point counts. For a structurally different secondary check, if SymPy is installed, execute `python3 verify_groebner.py`: it computes unit Gröbner bases for the ideals \((F,F_X,F_Y,F_Z)\) on all three affine charts for all \(78\) smooth orbit representatives. Both programs were executed successfully from the embedded sources before packaging. The theorem depends on the algebraic criterion and exhaustive calculation; the secondary chart check is corroborative.

## Relationship to prior work
Asgarli and Freidin (2020) investigate the asymptotic density of transverse-free smooth plane curves and define the same geometric notion, but their main theorem does not give the finite \(\mathbf F_2\), degree-four spectrum. Asgarli (2018) studies sharp existence bounds and gives plane-filling examples, with standing odd-characteristic hypotheses for his main theorem. Bruggemann–Choi–Freidin–Whyte (2024) extend the problem to other projective settings, rather than classifying binary plane quartic line profiles. Homma–Kim (2009/2013) already provide all nonsingular plane-filling curves of minimum degree: the size-24 rational-point-full orbit is therefore not new by itself. Dickson's 1915 work gives extensive projective classifications and bitangent data for characteristic-two quartics, including rational-point strata; an older implicit derivation is a residual bibliographic risk, particularly for the extremal cases. The asserted contribution is the **full rational-line transversality distribution jointly with rational-point counts and projective-orbit decomposition**, not the existence of plane-filling examples or the quartic genus formula.

## Limitations
The result covers quartics only over \(\mathbf F_2\), not extensions and not higher degrees. It counts embedded projective equations and projective orbits, not absolute moduli/isomorphism classes. The integer tables rely on a reproducible finite enumeration and the proved rank criterion. Historical bitangent classifications may contain implicitly equivalent information; no claim of a priority decision against inaccessible complete nineteenth- or early twentieth-century tables is made. Independent external audit has not occurred.

## References
1. S. Asgarli and B. Freidin, *On the proportion of transverse-free plane curves*, arXiv:2009.13421v1, first public 2020-09-28, https://arxiv.org/abs/2009.13421.
2. S. Asgarli, *Sharp Bertini theorem for plane curves over finite fields*, arXiv:1804.01569v1, first public 2018-04-04, https://arxiv.org/abs/1804.01569.
3. C. Bruggemann, V. Choi, B. Freidin and J. Whyte, *Transverse-freeness in finite geometries*, arXiv:2409.05248v1, first public 2024-09-08, https://arxiv.org/abs/2409.05248.
4. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, arXiv:0903.1918v1; *Linear Algebra Appl.* 438 (2013), 969–985.
5. L. E. Dickson, *Quartic curves modulo 2*, *Trans. Amer. Math. Soc.* 16 (1915), 111–120, doi:10.2307/1988711.
6. L. E. Dickson, *Geometrical and invariantive theory of quartic curves modulo 2*, *Amer. J. Math.* 37 (1915), 337–354, doi:10.2307/2370210.
7. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, 2023-07-06.
