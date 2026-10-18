# All concurrency walls for sixteen bitangents of Ciani's quartic pencil

## Finding
Over \(\mathbb C\), let
\[
C_\lambda:\quad F_\lambda=X^4+Y^4+Z^4+\lambda(X^2Y^2+Y^2Z^2+Z^2X^2)=0,
\qquad \lambda\notin\{-2,-1,2\}.
\]
Choose either square root \(s\) of \(-\lambda-1\). Define the following sixteen projective lines, with every independent sign chosen from \(\{1,-1\}\):
\[
\mathscr B_\lambda=
\{X+\epsilon Y+\delta Z=0:\epsilon,\delta=\pm1\}
\;\cup\;
\{sX+\epsilon Y+\delta Z=0,\ 
\epsilon X+sY+\delta Z=0,\ 
\epsilon X+\delta Y+sZ=0:\epsilon,\delta=\pm1\}.
\]
There are four lines in the first set and twelve in the second. The union is independent of the sign of \(s\), consists of sixteen **distinct bitangents** (including hyperosculating bitangents), and is exactly the subarrangement of bitangents whose three line coefficients are nonzero in these fixed coordinates. Let \(n_j\) count points in \(\mathbb P^2_{\mathbb C}\) incident to precisely \(j\) lines of this arrangement. Its entire intersection profile is

| Smooth parameter | \(n_2\) | \(n_3\) | \(n_4\) |
|:--|--:|--:|--:|
| \(\lambda=0\) | 48 | 0 | 12 |
| \(\lambda=-5\) | 72 | 4 | 6 |
| \(\lambda=-10\) | 48 | 12 | 6 |
| \(\lambda^2-\lambda+2=0\) (either root) | 48 | 12 | 6 |
| Every other smooth \(\lambda\) | 84 | 0 | 6 |

There are no points incident to five or more of these lines. In particular, the **complete extra-concurrency locus** in this pencil is exactly
\[
\lambda(\lambda+5)(\lambda+10)(\lambda^2-\lambda+2)=0.
\]
The jumps at \(\lambda=-5,-10\) and the two roots of \(\lambda^2-\lambda+2\) produce triple points; the jump at \(\lambda=0\) instead produces six additional quadruple points. This theorem concerns the distinguished sixteen-bitangent subarrangement, **not the full arrangement of twenty-eight bitangents**.

## Assumptions and scope
All geometry and multiplicity counts are over the algebraic closure \(\mathbb C\) in the displayed fixed coordinates. A bitangent may have its two contact points coincide (a hyperflex). The only singular members of the affine Ciani pencil occur at \(\lambda=-2,-1,2\), which are excluded. The term *intersection multiplicity* in the table is the number of **distinct lines** through the point, not the local curve intersection multiplicity with \(C_\lambda\).

The construction is naturally invariant under coordinate permutations and signed coordinate changes, a projective group of order twenty-four. The complementary twelve bitangents have one zero coefficient and are not included in the counted arrangement.

## Proof
**1. Smoothness and the bitangent decomposition.** The derivative in \(X\) is \(2X(2X^2+\lambda(Y^2+Z^2))\), and similarly in \(Y,Z\). At a common zero with exactly two nonzero coordinates, the derivative equations require \(\lambda^2=4\); with all three nonzero, the linear system for \((X^2,Y^2,Z^2)\) has eigenvalues \(2-\lambda\) (twice) and \(2+2\lambda\). The resulting exceptional parameters are precisely \(\{-2,-1,2\}\), and each actually gives a singular curve. Hence the stated smoothness range is exact.

For \(r\ne0\) restrict \(F_\lambda\) to the line \(X+Y+rZ=0\), and put \(u=X+Y\), \(v=X-Y\). The restriction is
\[
A u^4+B u^2v^2+C v^4,\quad
A={ (\lambda+2)r^4+8\lambda r^2+16 \over16r^4},\quad
B={6r^2+4\lambda-\lambda r^2\over8r^2},\quad
C={\lambda+2\over16}.
\]
A direct calculation gives
\[
r^4(B^2-4AC)=-\tfrac14(\lambda-2)(r^2-1)(\lambda+r^2+1).
\]
For \(r^2=1\), the restriction is \((\lambda+2)(3u^2+v^2)^2/16\). For \(r^2=-\lambda-1\), it is
\[
{\lambda+2\over16}
\left({\lambda-3\over r^2}u^2+v^2\right)^2.
\]
Thus the four fixed lines and the twelve signed permutations of \(sX+Y+Z=0\) are bitangents. They are distinct whenever \(s\notin\{0,1,-1\}\), which follows from smoothness. The change \(s\mapsto-s\) leaves their *set* unchanged, by simultaneous sign changes and projective rescaling.

To see that these are **all** the non-coordinate bitangents, note that a smooth complex plane quartic has exactly twenty-eight bitangents. Independently, restricting to \(Z=cY\) gives a square precisely when, for \(t=c^2\),
\[
(\lambda^2-4)(t^2+1)+(2\lambda^2-4\lambda)t=0.
\]
For the smooth range its leading and constant coefficients are nonzero and its discriminant is \(-16(\lambda-2)^2(\lambda+1)\ne0\). Hence it yields four distinct bitangents with the \(X\)-coefficient zero, and similarly for the other two coordinate pairs. These twelve plus the displayed sixteen exhaust all twenty-eight.

**2. Complete determinant divisor.** Use the coefficient rows
\[
(1,\epsilon,\delta),\quad (s,\epsilon,\delta),\quad
(\epsilon,s,\delta),\quad(\epsilon,\delta,s),
\qquad \epsilon,\delta=\pm1,
\]
indexed in that order. For every triple of distinct rows form its \(3\times3\) determinant in \(\mathbb Z[s]\). Exact expansion of all \(\binom{16}{3}=560\) determinants gives exactly 24 identically zero polynomials. Every other determinant is a nonzero constant times a product of factors from the **complete list**
\[
s,\ s-1,\ s+1,\ s^2+1,\ s^2+3,\ s-2,\ s+2,\ s-3,\ s+3,\ s^2+s+2,\ s^2-s+2.
\]
No factor outside this list occurs. The 24 zero determinants are precisely the four triples of lines through each of the six permanent quadruple points \([1:\pm1:0]\), \([1:0:\pm1]\), and \([0:1:\pm1]\).

Since \(s^2=-\lambda-1\), the factors \(s,s\pm1,s^2+3\) correspond respectively to the excluded singular parameters \(\lambda=-1,-2,2\). Among smooth parameters, all possible further changes are therefore \(\lambda=0,-5,-10\) and those obtained by eliminating \(s\) between \(s^2=-\lambda-1\) and \(s^2\pm s+2=0\), namely \(\lambda^2-\lambda+2=0\). This proves that **no other** concurrency-wall parameter exists.

**3. Complete incidence counts on each wall.** For a pair of distinct line rows \(a,b\), compute their projective intersection \(P=a\times b\). The line indices through that point are exactly \(\{k:a_k\cdot P=0\}\). Group the 120 pairs by these containing-index sets, reducing coefficients modulo the monic minimal polynomial of \(s\). The exact counts \((n_2,n_3,n_4)\) are, respectively: generic \((84,0,6)\); \(s^2+1=0\), \((48,0,12)\); \(s=\pm2\), \((72,4,6)\); \(s=\pm3\), \((48,12,6)\); and either quadratic \(s^2\pm s+2=0\), \((48,12,6)\). There is no higher multiplicity. Each case checks \(n_2+3n_3+6n_4=\binom{16}{2}=120\), and the explicit exhaustive exact polynomial checker in `verify.py` proves every equality without numerical approximations. Thus all rows of the table follow.

## Verification
Run `python3 verify.py` with Python 3 (standard library only). The checker constructs all sixteen coefficient triples exactly; factors all 560 triple determinants against the list above (asserting 24 permanent zeros); and groups all 120 pair intersections using integer-polynomial arithmetic modulo exact linear/quadratic factors. It checks both signs at \(s=\pm2,\pm3\), both quadratic factors and the Fermat factor, as well as the generic case. All checks passed. The hand derivation above separately proves smoothness and the bitangency of all sixteen lines.

## Relationship to prior work
Janasz, Pokora and Zieliński (first publicly released August 31, 2023, arXiv:2308.16514, especially Sections 3.1–3.3 and Proposition 3.8) give complete **full-28-line** profiles for the Klein, Dyck/Fermat and Komiya–Kuribayashi quartics, and a lower bound of nine quadruple points for the full arrangement for every smooth Ciani-pencil member. They do not enumerate the parameter-wise triple-concurrence walls of the distinguished sixteen-line subarrangement. The Fermat specialization \(\lambda=0\) is individually computable from their line table, but the other walls and uniform classification here do not follow from the printed special-fiber profiles.

Edge (1945, pp. 10–13) studies the Ciani pencil and four fixed bitangents, and the twelve-undulation member at \(\lambda=3\); it does not supply the displayed sixteen-line wall equation or incidence census. General algorithms for recovering bitangents and theta characteristics, such as those of Ottaviani and collaborators, do not themselves furnish this parametric concurrency classification.

The contribution here is specifically the explicit **discriminant and full incidence stratification** of a canonical coordinate-defined sixteen-line bitangent subarrangement. No claim is made that the complete twenty-eight-line arrangement has the same profile.

## Limitations
The theorem is for complex characteristic zero and the affine one-parameter Ciani pencil in its given coordinates; it does not classify every quartic or all twenty-eight-bitangent intersection profiles. The historical literature on classical quartic line configurations is extensive; equivalent formulas not located in the inspected sources remain possible. A fully independent mathematical audit has not been performed.

## References
1. M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first public version 2023-08-31; later Fundamenta Mathematicae 268 (2025), 151–170. https://arxiv.org/abs/2308.16514
2. W. L. Edge, *A plane quartic curve with twelve undulations*, Edinburgh Mathematical Notes 35 (1945), 10–13. DOI:10.1017/S0950184300000197.
3. G. Ottaviani et al., *Effective methods for plane quartics, their theta characteristics and the Scorza map*, Annali dell'Università di Ferrara (2024), DOI:10.1007/s11565-024-00528-2.
