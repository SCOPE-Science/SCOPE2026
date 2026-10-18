# Weak-combinatorial rigidity of minimal plus-one generation at the two-node conic boundary

## Finding
Let \(\mathcal C\subset\mathbb P^2_{\mathbb C}\) consist of \(k\in\{2,3,4\}\) distinct smooth conics, with exactly two \(A_1\) nodes, \(k(k-1)-1\) \(A_3\) tacnodes, and no other singularities. Then the least degree of a nontrivial Jacobian syzygy is \(\operatorname{mdr}(f)=k\), and the three minimal syzygy degrees of \(f\) are \((k,k,k+1)\). Equivalently, every such arrangement is **minimally plus-one generated**, independently of the chosen geometric realization. The three baskets are \(2A_1+A_3\), \(2A_1+5A_3\), and \(2A_1+11A_3\); they yield exponents \((2,2,3)\), \((3,3,4)\), and \((4,4,5)\), respectively. In particular the graded minimal free resolutions are identical within each of these three strata, excluding weak Ziegler pairs inside a stratum.

## Assumptions and scope
The field is \(\mathbb C\). Every component is a smooth reduced conic; all components are distinct. The only singularities of their union are isolated ordinary nodes and ordinary two-branch tacnodes, analytically of types \(A_1\) and \(A_3\), in exactly the specified numbers. Write \(f=\prod_{i=1}^kq_i\in\mathbb C[x,y,z]\), with \(\deg q_i=2\), and \(d=2k\). Let \(AR(f)\) be the graded module of triples \((a,b,c)\) such that \(af_x+bf_y+cf_z=0\). Define \(r=\operatorname{mdr}(f)=\min\{j:AR(f)_j\ne0\}\). The term *minimally plus-one generated* means a three-generator syzygy module with degrees \((d_1,d_2,d_3)\), satisfying \(d_1+d_2=d\) and \(d_3=d_2+1\). All statements concern the embedded plane curve, not the abstract normalizations.

## Proof
The local Tjurina numbers of \(A_1\) and \(A_3\) are, respectively, \(1\) and \(3\). Hence
\[\tau(\mathcal C)=2+3(k(k-1)-1)=3k(k-1)-1.\]
For \(k=2,3,4\) these values are \(5,17,35\). The Bézout count is consistent: \(2+2(k(k-1)-1)=2k(k-1)=4\binom{k}{2}\). The Arnold exponent is \(\alpha_{\mathcal C}=3/4\), because the local Arnold exponents of \(A_1\) and \(A_3\) are \(1\) and \(3/4\). Since all singularities are weighted homogeneous, the Dimca–Sernesi estimate gives
\[r\ge\left\lceil\frac34d-2\right\rceil.\]
The respective lower bounds are \(1,3,4\). The existence of at least one smooth conic component implies \(r\ge1\): a constant-coefficient Jacobian relation would make \(f\) independent of a linear coordinate, and a binary homogeneous polynomial splits into lines over \(\mathbb C\), contradicting the presence of smooth conics. Standard syzygy theory supplies \(r\le d-1\).

Use the du Plessis–Wall estimates, valid for reduced singular plane curves:
\[(d-1)(d-r-1)\le\tau(\mathcal C)\le(d-1)(d-r-1)+r^2,\]
and, when \(2r+1>d\), the sharper upper bound
\[\tau(\mathcal C)\le(d-1)(d-r-1)+r^2-\frac{(2r+1-d)(2r+2-d)}2.\]
For \(k=2\), the first lower bound forbids \(r=1\), since it would give \(\tau\ge6>5\); the sharpened upper bound forbids \(r=3\), since it gives \(\tau\le3<5\). Therefore \(r=2\). For \(k=3\), the Arnold bound gives \(r\ge3\), while the sharpened upper bound gives at most \(15\) when \(r=4\), and at most \(10\) when \(r=5\), both below \(17\). Therefore \(r=3\). For \(k=4\), the Arnold bound gives \(r\ge4\), whereas the sharpened upper bounds for \(r=5,6,7\) are respectively \(33,28,21\), all below \(35\). Therefore \(r=4\). Thus \(r=k=d/2\) in all three cases.

The Dimca–Sticlaru numerical characterization states that any reduced complex plane curve of degree \(d\) with \(r\le d/2\) is minimally plus-one generated if and only if
\[r^2-r(d-1)+(d-1)^2=\tau(\mathcal C)+2.\]
At \(d=2k,r=k\), the left side equals \(3k^2-3k+1\), which agrees exactly with \(\tau+2=3k(k-1)+1\). Consequently each curve has minimal syzygy degrees \((k,k,k+1)\). The standard minimal three-syzygy resolution is determined by these degrees, so two members with identical \(k\) cannot have distinct graded Betti tables. This proves the Ziegler-pair assertion. \(\square\)

## Verification
Run `python3 verify.py` using only Python's standard library. The program checks the Bézout counts, total Tjurina numbers, rational Arnold lower bounds, every allowed integral syzygy-degree candidate against both du Plessis–Wall bounds, and the Dimca–Sticlaru equality. It outputs `VERIFY_OK`. These exact finite arithmetic checks audit the applications of the cited theorems; they do **not** prove those theorems or independently compute Jacobian resolutions for arbitrary curves. The geometric theorem above follows from the published general inequalities and characterization.

## Relationship to prior work
Măcinic–Pokora, *On plus-one generated conic-line arrangements with simple singularities*, Theorem 3.1, constructs individual plus-one generated examples for the three baskets, including parameter-specialized models of the \(k=3\) and \(k=4\) families. Its proof does not give the universal statement for every realization. Bromboszcz–Jarosławski–Pokora, *On plus-one generated arrangements of plane conics*, Theorem 4.2, establishes necessary combinatorial restrictions assuming plus-one generation and realizes examples of the same baskets; it does not establish the converse for all realizations. Its Proposition 4.3 treats the distinct four-conic basket \(4A_1+10A_3\). Dimca–Janasz–Pokora classify nearly-free conic arrangements, for which the maximal-tacnode boundary is different (no nodes). The present claim is the positive uniform rigidity statement on the adjacent exactly-two-node boundary, requiring no genericity or choice of a special parameter. The tools themselves—the Arnold exponent estimate, du Plessis–Wall bounds, and the numerical minimal-plus-one criterion—are established results and are not claimed as new.

## Limitations
This applies only to arrangements of smooth conics with exactly the specified singularity baskets over \(\mathbb C\). It does not classify four-conic arrangements with four nodes and ten tacnodes, arrangements including lines, higher-order singularities, or positive-characteristic reductions. This proof does not explicitly write the syzygy generators for each parameter value, only their universally forced degrees. Although the closest inspected literature establishes examples rather than uniformity, differently phrased or unindexed earlier proofs might exist. An independent audit has not been performed.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, Rend. Lincei Mat. Appl. 35 (2024), 349–364, DOI:10.4171/RLM/1044; first preprint arXiv:2309.15228 (26 September 2023). Theorem 3.1, pp. 355–356.
2. A. Bromboszcz, B. Jarosławski, P. Pokora, *On plus-one generated arrangements of plane conics*, Geom. Dedicata 220 (2026), article 10, DOI:10.1007/s10711-025-01063-w. Theorem 4.2 and Proposition 4.3.
3. A. Dimca, M. Janasz, P. Pokora, *On plane conic arrangements with nodes and tacnodes*, Innov. Incidence Geom. 19 (2022), 47–58, DOI:10.2140/iig.2022.19.47; arXiv:2108.04004. Proposition 1.6.
4. A. Dimca and E. Sernesi, *Syzygies and logarithmic vector fields along plane curves*, J. Éc. Polytech. Math. 1 (2014), 247–267, DOI:10.5802/jep.10 (Arnold exponent bound).
5. A. A. du Plessis and C. T. C. Wall, *Application of the theory of the discriminant to highly singular plane curves*, Math. Proc. Cambridge Philos. Soc. 126 (1999), 259–266 (global Tjurina bounds); see also the explicit statement in *Characterization of quasi-homogeneous singularities of free and nearly free plane curves*, IMRN 2025, Proposition 2.8.
6. A. Dimca and G. Sticlaru, *Plane curves with three syzygies, minimal Tjurina curves, and nearly cuspidal curves*, Geom. Dedicata 207 (2020), 29–49, DOI:10.1007/s10711-019-00485-7; numerical criterion also quoted as Theorem 2.5 in *On combinatorics of plus-one generated line arrangements*.
