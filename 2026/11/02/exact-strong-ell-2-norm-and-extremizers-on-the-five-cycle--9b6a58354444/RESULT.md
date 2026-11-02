# Exact strong \(\ell^2\) norm and extremizers on the five-cycle

## Finding
Let \(C_5\) be the undirected five-cycle with counting measure, and let \(M\) be the centered graph-ball Hardy–Littlewood maximal operator. Let \(\lambda_*\) be the unique real root of
\[
225\lambda^3-390\lambda^2+91\lambda-4=0
\]
in \((293/200,733/500)\). Then
\[
\boxed{\|M\|_{\ell^2(C_5)\to\ell^2(C_5)}=\sqrt{\lambda_*}
=1.210645548908955\ldots.}
\]
Every nonzero extremizer, and no other input, has absolute values proportional to a cyclic rotation of
\[
\left(a_*,a_*,1,c_*,1\right),\qquad
c_*=\frac{\lambda_*-1}{\lambda_*},\qquad
 a_*=\frac{4+2c_*}{25\lambda_*-4}.
\]
Here \(a_*=0.142010021445\ldots\) and \(c_*=0.317714752881\ldots\). Each coordinate may independently have either sign. There are exactly five norming nonnegative rays, obtained by the five rotations.

## Assumptions and scope
The vertices are \(0,1,2,3,4\) with edges between successive residues modulo five. Graph balls are closed balls in shortest-path distance. For a real function \(f\),
\[
(Mf)(v)=\max_{r\in\{0,1,2\}}\frac1{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|.
\]
The norm uses the unnormalized counting measure, but an overall constant change in the measure leaves the norm unchanged. Ball sizes are \(1,3,5\). No weights, directed edges, uncentered balls, or exponents other than two are involved.

## Proof
**1. Exact reduction to 243 linear operators.** For each vertex \(v\), select a radius \(s_v\in\{0,1,2\}\), and let \(A_s\) have as row \(v\) the uniform average over \(B(v,s_v)\). Because row choices are independent, for each nonnegative \(g\),
\[
\|Mg\|_2^2=\max_{s\in\{0,1,2\}^5}\|A_sg\|_2^2.
\]
Each \(A_s\) is entrywise nonnegative, so its Euclidean norm is achieved by a nonnegative vector: replacing a vector by its absolute values cannot decrease the norm of its image. Hence
\[
\|M\|_{2\to2}^2=\max_{s\in\{0,1,2\}^5}\lambda_{\max}(A_s^{\mathsf T}A_s).
\]
This is an equality, not a discretization or an approximation.

**2. Exact spectral separation.** Set \(\tau=1463/1000\). For every one of the 238 choices other than the five cyclic rotations of \((2,2,0,1,0)\), the rational symmetric matrix
\[
\tau I-A_s^{\mathsf T}A_s
\]
is positive definite. The accompanying standalone file `verify_c5.py` enumerates these 238 matrices without floating-point arithmetic and checks all positive pivots of a rational \(LDL^{\mathsf T}\) decomposition. Thus all these choices have squared norm strictly less than \(\tau\). The five excluded matrices are cyclic permutation-conjugate and consequently have identical spectra. The enumeration is exhaustive because every vertex has precisely three distinct centered balls.

**3. Largest eigenvalue of the five winners.** For \(s=(2,2,0,1,0)\), the rows of \(A_s\) are two global averages, two singleton evaluations at vertices two and four, and the average of vertices two, three, four. All entries of \(A_s^{\mathsf T}A_s\) are positive. Its Perron eigenvector is positive and reflection-invariant, of the form \((a,a,b,c,b)\). On these coordinates the input squared norm is the quadratic form of \(D=\operatorname{diag}(2,2,1)\), and the output squared norm has the matrix
\[
B=\begin{pmatrix}
8/25&8/25&4/25\\
8/25&622/225&86/225\\
4/25&86/225&43/225
\end{pmatrix}.
\]
A direct determinant expansion gives
\[
\det(B-\lambda D)=-\frac4{225}
(225\lambda^3-390\lambda^2+91\lambda-4).
\]
The polynomial is negative at \(293/200\) and positive at \(733/500\), and its derivative \(675\lambda^2-780\lambda+91\) is positive and increasing throughout this interval and beyond. The root \(\lambda_*\) there is therefore the unique root above \(293/200\), and hence the largest eigenvalue. In particular, \(\lambda_*>293/200>\tau\). Together with Step 2 this identifies all maximizing radius choices exactly.

**4. Extremizers and active balls.** Subtracting the eigenvalue equations for a high coordinate and the central coordinate gives \(\lambda_*(b-c)=b\); the small-coordinate equation gives \(25\lambda_*a=4a+4b+2c\). Normalize \(b=1\), obtaining the formulas in the finding. The root interval implies the strict rational enclosures
\[
\frac7{50}<a_*<\frac3{20},\qquad
\frac{31}{100}<c_*<\frac{33}{100}.
\]
These bounds show that the full average wins at vertices zero and one, the singleton wins at vertices two and four, and the three-point average wins at vertex three. Thus the eigenvector does activate the indicated choices and attains the maximal-operator norm. The strict inequalities also exclude ambiguous active choices. Positivity of the entire winning Gram matrix makes its largest eigenvalue simple, so each winning choice has exactly one nonnegative norming ray. The five rays are distinct, and replacing any coordinate by its negative preserves the maximal output. Conversely, equality forces one of the five winning choices and its positive Perron ray after taking absolute values. This proves the complete classification.

## Verification
Run `python3 verify_c5.py` using Python 3 standard library only. It independently constructs the five-cycle's shortest-path balls by breadth-first search, enumerates all \(3^5=243\) radius choices, verifies all 238 strict \(LDL^{\mathsf T}\) upper certificates, checks conjugacy for the five winners, verifies the cubic determinant identity by four exact specializations, isolates the largest root by rational inequalities, and checks rational enclosures ensuring actual ball selection. The script prints `CERTIFICATE_OK`. The finite census is **exhaustive** for this five-vertex graph; no claim about other cycle sizes is inferred from it.

## Relationship to prior work
Soria and Tradacete (arXiv:1410.6204, first public October 22, 2014) introduced sharp norm problems on finite graphs and treated general estimates for \(0<p\le1\), complete graphs, stars, and other graph features. Their inspected results do not supply this five-cycle strong \(\ell^2\) constant. González-Riquelme and Madrid (arXiv:2005.03146, 2020) gave strong \(\ell^2\) norms for complete graphs and stars, not the five-cycle. The exact strong \(\ell^2\) norm and extremizers on the four-cycle are a distinct previously recorded calculation, not implied by or equivalent to the five-cycle statement. No covering five-cycle statement was identified in the searches performed; that is not a proof of publication priority.

## Limitations
The result is restricted to the finite unweighted five-cycle and centered balls; it gives no exact constants for longer cycles, other exponents, weighted measure, or uncentered maximal operators. A complete historical priority guarantee is unavailable, because not all possible unindexed sources can be ruled out. The independent mathematical audit has not yet been performed.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first submitted October 22, 2014), https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first submitted May 6, 2020), https://arxiv.org/abs/2005.03146.
