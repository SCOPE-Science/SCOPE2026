# Generic irreducibility of the minimal unexpected octic for the 18-point plus-one configuration
## Finding
Let \(Z\subset \mathbb P^2_{\mathbb C}\) be the 18-point configuration of Malara--Pokora--Tutaj-Gasińska, Example 5.10:
\[
\begin{aligned}
Z=\{&(0,1,0),(-1,1,0),(-2,1,0),(-3,1,0),(-3,2,0),(4,0,-1),\\
&(1,1,-1),(2,1,-1),(3,1,-1),(4,1,-1),(0,2,-1),(1,2,-1),\\
&(2,2,-1),(0,3,-1),(1,3,-1),(-2,3,-1),(-1,3,-1),(-2,4,-1)\}.
\end{aligned}
\]
For a general point \(P\in\mathbb P^2_{\mathbb C}\), the unique minimal unexpected curve
\[
C_P\in [I(Z+7P)]_8
\]
is absolutely irreducible.

An exact witness occurs at \(P_0=[3:5:1]\). The 18 point conditions and the 28 jet conditions of order below \(7\) form a \(46\times45\) integer interpolation matrix of rank exactly \(44\). Its one-dimensional kernel gives an octic \(F\). After setting \(x=3+u\), \(y=5+v\), and \(z=1\), one has
\[
F(3+u,5+v,1)=A_7(u,v)+B_8(u,v),
\]
where
\[
A_7=-420\left(2664u^7-11816u^6v+20734u^5v^2-19116u^4v^3+9701u^3v^4-2560u^2v^5+315uv^6-18v^7\right)
\]
and
\[
B_8=uv(u+v)(u+2v)(u+3v)(2u+3v)(342u^2-395uv+109v^2).
\]
These two homogeneous forms are coprime. In particular, no line through \(P_0\) divides \(F\).

## Assumptions and scope
All geometry is over \(\mathbb C\). The phrase “general point” means a point in a nonempty Zariski-open subset of \(\mathbb P^2\). The source proves that this configuration has splitting type \((7,10)\) and admits unexpected curves of degrees \(8\) and \(9\); its cited general theorem says the minimal unexpected curve has degree \(8\) and is unique for a general assigned point. The present result concerns the irreducibility of that degree-\(8\) curve, not the degree-\(9\) system and not the freeness properties of the dual arrangement.

## Proof
For degree \(8\), the space of homogeneous forms has dimension \(45\). The 18 points of \(Z\) impose 18 independent conditions, so \(\dim I(Z)_8=27\). A point of multiplicity at least \(7\) imposes 28 jet conditions. The expected dimension is therefore zero, while the source theorem gives a one-dimensional space for a general assigned point.

At \(P_0=[3:5:1]\), the exact interpolation matrix has rank \(44\): a nonzero kernel vector is archived in the verifier, and a \(44\)-rank certificate modulo \(1000003\) proves the rational rank is at least \(44\); the kernel vector proves it is at most \(44\). Thus the octic \(F\) is unique up to scale at \(P_0\). The translated expansion displayed above contains only homogeneous pieces of degrees \(7\) and \(8\), with \(A_7\neq0\), so \(F\) has multiplicity exactly \(7\) at \(P_0\).

The univariate dehomogenizations \(A_7(u,1)\) and \(B_8(u,1)\) have gcd \(1\), and \(A_7(1,0)=-1118880\neq0\). Hence \(A_7\) and \(B_8\) have no common homogeneous factor over \(\mathbb C\), so no line through \(P_0\) divides \(F\).

Suppose a degree-\(8\) plane curve with multiplicity \(7\) at \(P_0\) were reducible. Writing its nonconstant factors with degrees \(d_i\) and multiplicities \(m_i\) at \(P_0\), one has \(m_i\le d_i\), \(\sum d_i=8\), and \(\sum m_i=7\). Thus \(\sum(d_i-m_i)=1\). If there is more than one factor, at least one factor satisfies \(d_i=m_i>0\). In translated affine coordinates that factor is a homogeneous binary form of degree \(d_i\), so over \(\mathbb C\) it splits into lines through \(P_0\). Therefore reducibility would force a line through \(P_0\) to divide \(F\), contradicting the coprimality of \(A_7\) and \(B_8\). Hence the witness octic is absolutely irreducible.

Finally, the interpolation matrix depends algebraically on the assigned point. Since the source theorem gives generic kernel dimension one, all \(45\times45\) minors vanish identically, while the rank-\(44\) minor certified at \(P_0\) stays nonzero on a neighborhood. On that nonempty open set the kernels form an algebraic map to the projective space of octics. Reducible degree-\(8\) forms constitute a Zariski-closed subset, being the finite union of the proper images of multiplication maps \(\mathbb P(S_d)\times\mathbb P(S_{8-d})\to\mathbb P(S_8)\). Since the value at \(P_0\) is irreducible, irreducibility holds on a nonempty Zariski-open subset. This proves the general claim.

## Verification
The standalone script `artifacts/verify.py` uses only the Python standard library. It reconstructs the 45 coefficient coordinates of \(F\), checks vanishing at all 18 points, checks all 28 order-\(<7\) jet conditions at \(P_0\), verifies a rank of \(44\) modulo four primes, verifies the 18 point conditions are independent, reconstructs the translated degree-\(7\) and degree-\(8\) pieces, checks the displayed factorization of \(B_8\), and computes the exact gcd of \(A_7(u,1)\) and \(B_8(u,1)\). A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Malara--Pokora--Tutaj-Gasińska compute the splitting type \((7,10)\) for this exact 18-point configuration and conclude that unexpected curves occur in degrees \(8\) and \(9\). Their Theorem 5.1, citing the general theory of Cook II--Harbourne--Migliore--Nagel and Dimca, gives a criterion for irreducibility of a minimal unexpected curve, but Example 5.10 does not evaluate that criterion or state irreducibility for this configuration. The present calculation supplies an explicit exact irreducible octic at one assigned point and upgrades it, by openness, to generic absolute irreducibility for the source's concrete example.

Targeted searches using the point coordinates, the exponent triple \((7,11,12)\), the phrase “Example 5.10,” and the source identifier located the source paper and general unexpected-curve literature but no statement covering this explicit irreducibility result. The general framework does not imply the result without an additional configuration-specific irreducibility check.

## Limitations
The proof establishes generic absolute irreducibility of the minimal unexpected octic. It does not classify the exceptional assigned points where the interpolation rank or factorization type may change, does not determine singularities away from the assigned sevenfold point, and does not analyze the degree-\(9\) unexpected system. Literature searches cannot exclude unindexed or unpublished computations; that residual originality risk is recorded in the review data.

## References
1. G. Malara, P. Pokora, H. Tutaj-Gasińska, “On 3-syzygy and unexpected plane curves,” arXiv:2007.04162v1; *Geometriae Dedicata* 214 (2021), 49–63, doi:10.1007/s10711-021-00602-5.
2. D. Cook II, B. Harbourne, J. Migliore, U. Nagel, “Line arrangements and configurations of points with an unexpected geometric property,” arXiv:1602.02300; *Compositio Mathematica* 154 (2018), 2150–2194, doi:10.1112/S0010437X18007376.
