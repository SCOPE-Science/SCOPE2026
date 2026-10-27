# Correcting the explicit species table in the D4-triality example

## Finding

The six Galois orbits of positive roots listed in the D4 triality example of Januszewski's *Rational quiver representations: tame and wild* have orbit-sum dimension vectors

\[
(1,0,0,0),\ (0,1,1,1),\ (3,1,1,1),\ (3,2,2,2),\ (1,1,1,1),\ (2,1,1,1),
\]

in the paper's orbit order. Since the leaf orbit has size three and its stabilizer field is the cubic field \(M/K\), the associated species dimensions \((\dim_K V_K,\dim_M V_M)\) are therefore

\[
(1,0),\ (0,1),\ (3,1),\ (3,2),\ (1,1),\ (2,1).
\]

The explicit species table on p. 7 does not match these data. Its item (3), \((K,M)\) with inclusion, has dimensions \((1,1)\) and belongs to orbit 5, not orbit 3. Item (4), \((M,M)\) with identity, has dimensions \((3,1)\) and belongs to orbit 3, not orbit 4. Item (5), \((\ker\operatorname{Tr}_{M/K},M)\) with inclusion, has dimensions \((2,1)\) and belongs to orbit 6, not orbit 5. Item (6), \((M,K)\) with trace, is not a representation under the immediately preceding convention \((V_K,V_M)\), where \(V_M\) must be an \(M\)-vector space and the map is \(V_K\to V_M\); it also repeats orbit 5's claimed dimension and omits the required orbit-4 dimension \((3,2)\).

The corrected orbit correspondence is: orbit 1 \((K,0)\); orbit 2 \((0,M)\); orbit 3 \((M,M)\) with identity; orbit 4 an indecomposable of dimensions \((3,2)\); orbit 5 \((K,M)\) with the canonical inclusion; orbit 6 \((\ker\operatorname{Tr}_{M/K},M)\) with inclusion. This corrects the explicit table, not the general orbit-classification theorem.

## Assumptions and scope

Work in characteristic zero with an \(S_3\)-Galois extension \(L/K\), and let \(M=L^H\) for a subgroup \(H\cong S_2\). Thus \([M:K]=3\). Use the paper's stated convention that a species representation is a pair \((V_K,V_M)\) with a \(K\)-linear map \(V_K\to V_M\), where \(V_K\) is a \(K\)-space and \(V_M\) is an \(M\)-space.

## Proof

For each orbit of roots, sum its four coordinates. The singleton central root gives \((1,0,0,0)\); the three leaf roots sum to \((0,1,1,1)\); the three roots with the center and one leaf sum to \((3,1,1,1)\); the three roots with the center and two leaves sum to \((3,2,2,2)\); the all-ones root stays \((1,1,1,1)\); and the highest root stays \((2,1,1,1)\). These are direct finite sums, not an inference from labels.

For a rational representation corresponding to a root orbit, the central coordinate is \(\dim_K V_K\), and the common coordinate at each of the three conjugate leaves is \(\dim_M V_M\). This yields the six pairs stated above. Comparing those pairs with the displayed six species entries gives the mismatches and the missing \((3,2)\) entry. Moreover, \(K\) cannot serve as the \(M\)-vector space in item (6), and the trace map has direction \(M\to K\), opposite to the declared map \(V_K\to V_M\).

A concrete indecomposable of the missing dimension \((3,2)\) can be checked in the example \(K=\mathbb Q\), \(M=\mathbb Q(\theta)\), \(\theta^3=2\), whose Galois closure is \(\mathbb Q(\theta,\zeta_3)\) with group \(S_3\). On the \(K\)-basis \((1,\theta,\theta^2)\), let \(\alpha\) have matrix

\[
A=\begin{pmatrix}0&-1&0\1&1&-1\0&1&-1\end{pmatrix},
\]

and take \(V_K=M\), \(V_M=M^2\), \(f(x)=(x,\alpha(x))\). Solving \(\beta f=f\gamma\), with \(\gamma\in M_3(\mathbb Q)\) and \(\beta\in M_2(M)\), gives a three-dimensional \(\mathbb Q\)-endomorphism algebra. It contains the endomorphism whose source-space matrix is

\[
\Gamma_0=\begin{pmatrix}2&36&8\-1&-26&-8\1&0&0\end{pmatrix},
\]

with characteristic polynomial \(z^3+24z^2-24z+80\), irreducible over \(\mathbb Q\). Hence \(\mathbb Q[\Gamma_0]\) already has dimension three and equals the endomorphism algebra; that algebra is a field, so the representation is indecomposable. This provides an explicit replacement example for the missing dimension vector, without claiming a new classification theorem.

## Verification

The root-orbit sums above are checked coordinate by coordinate. The species dimensions follow from \([M:K]=3\) and the stated vertex-orbit correspondence. For the explicit \((3,2)\) example, exact rational linear algebra gives endomorphism-algebra dimension three; the displayed irreducible cubic proves that it is a field and therefore has no nontrivial idempotents. This check concerns the explicit example only.

## Relationship to prior work

The source's Theorem 2.3 states the general classification by Galois orbits of positive roots. The correction reconciles the §3 species table with that theorem and with the paper's own orbit list; it does not contradict the general theorem or claim a new theorem about G2 species. Searches of the indexed finding database finding database for the paper title, arXiv identifier, D4 triality, the G2 species table, and the trace/inclusion descriptions returned no directly matching correction. The closest retrieved records concerned other quiver or algebra problems and do not imply this correction.

## Limitations

The finding is a correction to the explicit example/table, not a refutation of the paper's general descent theorem. The concrete \((3,2)\) representative is supplied for one cubic field \(M/\mathbb Q\); for a general \(S_3\)-extension the orbit classification supplies the indecomposable of that dimension, but this note does not give a uniform coordinate formula. No independent review has been performed, and an unindexed prior correction cannot be excluded.

## References

1. F. Januszewski, *Rational quiver representations: tame and wild*, arXiv:2510.00924v1, submitted 2025-10-01. Full text: https://arxiv.org/abs/2510.00924 and https://arxiv.org/pdf/2510.00924.
2. The source's own Theorem 2.3 and §3 (D4 positive-root orbit list and associated G2-species table), pp. 4–7 of arXiv:2510.00924v1.
