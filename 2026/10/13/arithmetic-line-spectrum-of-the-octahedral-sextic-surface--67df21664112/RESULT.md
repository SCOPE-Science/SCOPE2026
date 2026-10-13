# Arithmetic line spectrum of the octahedral sextic surface

## Finding

Let \(X\subset\mathbb P^3_{\mathbb Q}\) be the smooth sextic surface
\[
X:\quad x^5y-xy^5+z^5w-zw^5=0.
\]
Its \(180\) geometric lines have **minimal common field of definition** \(K=\mathbb Q(\zeta_{24})\), and precisely \(20\) individual lines are defined over \(\mathbb Q\). For every prime \(p\ge7\), the reduction is smooth and contains exactly \(180\) geometric lines. The number \(N_p\) of its \(\mathbb F_p\)-rational lines is completely determined by \(p\bmod24\):

| \(p\bmod24\) | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(N_p\) | 180 | 60 | 40 | 24 | 108 | 84 | 40 | 24 |

In characteristic \(5\), the smooth reduction instead contains exactly \(756\) geometric lines, of which \(156\) are \(\mathbb F_5\)-rational. The eight residue classes have equal natural prime density \(1/8\). Thus the counts \(24,40,60,84,108,180\) occur with densities \(1/4,1/4,1/8,1/8,1/8,1/8\), respectively.

## Assumptions and scope

All geometric lines are projective lines contained in \(X\) after extension to an algebraic closure. A line over \(\mathbb F_p\) is an individual projective line stable under \(p\)-power Frobenius, not merely an unordered Galois orbit of lines. The minimal common field is the smallest extension of \(\mathbb Q\) over which all individual lines are defined. The assertions about good reduction and the displayed residue table concern all rational primes \(p\ge7\), with \(p=5\) separately. Characteristics \(2,3\) are excluded; no count is claimed there. Put \(f(u,v)=uv(u^4-v^4)\).

## Proof

**1. Completeness of line types.** The binary sextic \(f\) has six distinct roots
\[
B=\{\infty,0,1,-1,i,-i\}\subset\mathbb P^1(\overline{\mathbb Q}).
\]
The standard separated-variable line argument (Boissière--Sarti, Proposition 4.1, reproduced by the projection argument below) partitions lines of \(f(x,y)+f(z,w)=0\) into exactly two disjoint kinds. A joining line joins a root \([x:y]\in B\) on \(\{z=w=0\}\) to a root \([z:w]\in B\) on \(\{x=y=0\}\): there are \(6^2=36\). Every other line projects isomorphically to both coordinate projective lines and hence is the graph
\[
(x,y,z,w)=(M(u,v),(u,v))
\]
for an invertible \(2\times2\) matrix \(M\). Restricting the defining equation to the graph yields \(f(M(u,v))=-f(u,v)\), so the projectivity of \(M\) must permute \(B\). Conversely, every projectivity \(A\) permuting \(B\) satisfies \(f(A(u,v))=c_A f(u,v)\) for a nonzero multiplier \(c_A\); the six scalar solutions \(s^6c_A=-1\) give six different graph lines \(M=sA\). To justify the dichotomy, suppose a line meets \(\{z=w=0\}\) at \([a:b:0:0]\). Its parametrization is \((x,y,z,w)=(\alpha a+\beta u,\alpha b+\beta v,\beta c,\beta d)\). If the vectors \((a,b)\) and \((u,v)\) are linearly independent, then \(f(\alpha a+\beta u,\alpha b+\beta v)\) is a binary sextic with six distinct linear factors, hence cannot equal the required scalar multiple of \(\beta^6\). Therefore \((u,v)\) is proportional to \((a,b)\), the first binary term vanishes identically, and \(f(c,d)=0\); the line is a join of two roots. A line not meeting either fixed coordinate line projects isomorphically to both binary coordinate lines, and is necessarily an invertible graph. This uses only distinctness of the six roots and holds in each characteristic considered.

**2. The octahedral group and its arithmetic representatives.** A projectivity is uniquely fixed by images of \(\infty,0,1\). Exactly \(24\) of the \(6\cdot5\cdot4=120\) ordered image triples induce maps preserving the entire six-point set. Normalize each matrix \(A\) by making its first nonzero row-major entry equal to \(1\). All \(24\) matrices lie in \(\operatorname{Mat}_2(\mathbb Z[i])\), are invertible over \(\mathbb Q(i)\), have entries in \(\{0,\pm1,\pm i\}\), and satisfy the following exhaustive multiplier census:

| \(c_A\) | 1 | \(-1\) | \(i\) | \(-i\) | 8 | \(-8\) | \(8i\) | \(-8i\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| number of matrices | 2 | 2 | 2 | 2 | 4 | 4 | 4 | 4 |

The attached `verify.py` constructs the unique matrix for each of the \(120\) triples by determinant formulas and checks the identity for each of the \(24\) successful cases at seven distinct projective input points. Since the binary expressions have degree six, seven evaluations certify the identity. Moreover, for each of the other \(96\) triples, the gcd of the Gaussian norms of the six values \(f(A(b))\), as \(b\) runs through \(B\), has prime support contained in \(\{2,5\}\). This exact exhaustive integer certificate rules out any new projectivity of the reduced six-point set in any characteristic \(p\ge7\): if a candidate induced a bijection in characteristic \(p\), all six values would vanish modulo a prime ideal above \(p\), forcing \(p\) to divide each Gaussian norm and hence their gcd. Every successful matrix remains invertible and different modulo such \(p\), so the stabilizer is still of order \(24\). Therefore all good reductions have \(36+6\cdot24=180\) geometric lines. At \(p\ge7\), smoothness follows directly from \(\partial_u f=v(5u^4-v^4)\) and \(\partial_v f=u(u^4-5v^4)\): a common nonzero critical pair would force \(24=0\).

**3. The minimal splitting field.** Write \(c_A=8^d i^t\) with \(d\in\{0,1\}\) and \(t\in\{0,1,2,3\}\). All solutions of \(s^6c_A=-1\) are
\[
s=2^{-d/2}\zeta_{24}^{\,e},\qquad e=2-t+4j\pmod{24},\quad j=0,\ldots,5.
\]
Hence the entries of all graph matrices \(sA\), and all joining endpoints, lie in \(K=\mathbb Q(\zeta_{24})\). Conversely, \(A=\operatorname{diag}(1,i)\) has \(c_A=i\) and yields the graph with \(M=\zeta_{24}A\). The normalized matrix of a graph is uniquely recovered by projection onto \([z:w]\); thus any field of definition of this individual graph must contain its matrix coefficient \(\zeta_{24}\). Therefore \(K\) is minimal. A joining line is rational exactly when both its root endpoints are rational, giving \(4^2=16\) over \(\mathbb Q\). Among the eight matrices \(A\) with rational entries, only the two with \(c_A=-1\) admit rational scalars \(s\) (\(s=\pm1\)), giving four rational graph lines. The total over \(\mathbb Q\) is \(20\).

**4. Frobenius fixed lines.** Let \(k\in(\mathbb Z/24\mathbb Z)^\times=\{1,5,7,11,13,17,19,23\}\) act on \(\zeta_{24}\) by exponentiation. It acts on \(i\) as \(i\mapsto i^k\), and on \(\sqrt2=\zeta_8+\zeta_8^{-1}\) by sign \(\epsilon_k\), which is positive for \(k\equiv1,7\pmod8\) and negative otherwise. A joining line is fixed exactly when both endpoints are fixed, giving \(36\) for \(k\equiv1\pmod4\) and \(16\) otherwise. A graph \(sA\) is fixed precisely when the normalized \(A\) is fixed and \(s\) is fixed. When \(k\equiv3\pmod4\), only the eight rational matrices \(A\) are fixed; when \(k\equiv1\pmod4\), all \(24\) are fixed. For the exponent \(e\) in step 3, the scalar condition is
\[
(k-1)e\equiv\begin{cases}12\pmod{24},&d=1\text{ and }\epsilon_k=-1,\\0\pmod{24},&\text{otherwise}.
\end{cases}
\]
Exhausting the \(24\) matrices and six allowed exponents gives the following exact fixed-point table:

| \(k\) | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| fixed joining lines | 36 | 36 | 16 | 16 | 36 | 36 | 16 | 16 |
| fixed graph lines | 144 | 24 | 24 | 8 | 72 | 48 | 24 | 8 |
| all fixed lines | 180 | 60 | 40 | 24 | 108 | 84 | 40 | 24 |

The determinant and gcd certificate in step 2 ensures that these are also the complete fixed-line counts for every \(p\ge7\), after taking \(k\equiv p\pmod{24}\). Dirichlet's theorem makes each permitted class have density \(1/8\).

**5. Exceptional characteristic five.** Over \(\overline{\mathbb F}_5\), the six zeros of \(f\) are exactly \(\mathbb P^1(\mathbb F_5)\); its projective stabilizer is therefore \(\operatorname{PGL}_2(\mathbb F_5)\), of order \(120\), because a projectivity is fixed by three distinct points and all image points lie in \(\mathbb F_5\). The line classification consequently gives \(36+6\cdot120=756\) geometric lines. Frobenius yields the polynomial identity \(f(A(u,v))=\det(A)f(u,v)\) for each \(A\in\operatorname{GL}_2(\mathbb F_5)\). A rational graph matrix \(sA\) satisfies \(s^6\det A=-1\); since \(s^6=s^2\) in \(\mathbb F_5^\times\), this equation has two solutions precisely for the \(60\) projectivities with square determinant, and none for the others (\(-1\) is a square in \(\mathbb F_5\)). Thus there are \(120\) rational graph lines and \(36\) rational joining lines: \(156\) altogether. Smoothness follows here from \(\partial_u f=-v^5\) and \(\partial_v f=u^5\).

## Verification

Execute `python3 verify.py` with Python 3. The self-contained exact integer program enumerates all \(120\) image triples, certifies the \(24\) valid projectivities and eight multipliers, checks the gcd obstruction for all \(96\) invalid triples, and independently computes all eight Galois fixed-line counts. As a separate consistency test, it exhaustively enumerates \(\operatorname{PGL}_2(\mathbb F_p)\) and scalar roots for \(p=7,11,13,17,19,23,29,31,37,41,43\), as well as the characteristic-five exception. All of those checks returned `VERIFY_OK`. The proof for infinitely many primes comes from the Gaussian-norm gcd certificate and the group-action argument, not the small-prime tests.

## Relationship to prior work

Boissière and Sarti, *Counting lines on surfaces* (2007), §4.1 and §4.4, establish the separated-variable classification and exhibit an octahedrally symmetric sextic with \(180\) complex lines, projectively equivalent over \(\mathbb Q\) to the present equation (replace one binary variable by its negative). Esser and Li, *Hypersurfaces with large automorphism groups* (first public 2024-05-19), Example 2.9, identify this particular sextic as the exceptional automorphism-extremal surface with \(6912\) complex projective automorphisms. Yang, Yu, and Zhu, *On automorphism groups of smooth hypersurfaces* (first public 2024-05-15), Theorem 1.1, give an independent maximal-automorphism classification over \(\mathbb C\). These sources cover the geometric line total and the complex symmetry description, respectively; neither computes the minimal common arithmetic line field, the rational line count, the exact eight-class Frobenius spectrum, nor the simultaneous exceptional characteristic-five classification in this form. The line-type classification and elementary cyclotomic/Dirichlet principles are explicitly used as known inputs; novelty is confined to their exact arithmetic realization for the named sextic.

## Limitations

The theorem is about individual geometric lines and their fields of definition, not rational points on the surface or its full Néron--Severi group. It makes no assertion in characteristics two or three. The special characteristic-five geometry is a Hermitian phenomenon; its geometric line count is classical, and that number alone is not claimed to be new. Algebraic line completeness uses the general separated-variable line lemma and the exact certificate provided; additional independent manuscript audit has not been performed.

## References

1. L. Esser and J. Li, *Hypersurfaces with large automorphism groups*, arXiv:2405.11666, version 1 submitted 2024-05-19, Example 2.9; https://arxiv.org/abs/2405.11666.
2. S. Boissière and A. Sarti, *Counting lines on surfaces*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze 6 (2007), 39–52, §4; https://www.numdam.org/item/ASNSP_2007_5_6_1_39_0/.
3. S. Yang, X. Yu and Z. Zhu, *On automorphism groups of smooth hypersurfaces*, arXiv:2405.09505, version 1 submitted 2024-05-15, Theorem 1.1; https://arxiv.org/abs/2405.09505.
