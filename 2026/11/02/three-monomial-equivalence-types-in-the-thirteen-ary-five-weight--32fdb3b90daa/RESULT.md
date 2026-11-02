# Three monomial-equivalence types in the thirteen-ary five-weight cyclic family

## Finding

The Hernández--Vega five-weight cyclic-code family has **exactly three** distinct monomial-equivalence classes at alphabet size \(q=13\), not one. They are represented by normalized exponents \(r=1,3,5\). Their Hamming weight enumerators agree, whereas their **complete distributions of support sizes of two-dimensional subcodes** are different. This is a complete equivalence classification within the stated family, not a classification of all codes with the same parameters.

For \(j\in\{0,\ldots,14\}\), let \(N_r(j)\) denote the number of two-dimensional subcodes whose union of nonzero coordinate supports has cardinality \(168-j\). Missing entries in the following table are zero.

| \(j\) | \(r=1\) | \(r=3\) | \(r=5\) |
|---:|---:|---:|---:|
| 0 | 10264 | 10744 | 10936 |
| 1 | 14448 | 12768 | 11928 |
| 2 | 3024 | 5040 | 6384 |
| 3 | 3360 | 2520 | 1680 |
| 5 | 0 | 0 | 168 |
| 7 | 0 | 24 | 0 |
| 12 | 14 | 14 | 14 |
| **Total** | **31110** | **31110** | **31110** |

For all three codes the ordinary Hamming weight enumerator, already determined by Hernández and Vega, is
\[
1+2100z^{144}+14112z^{155}+168z^{156}+12096z^{157}+84z^{168}.
\]
The three different distributions above therefore exhibit equivalence information not supplied by the common ordinary weight enumerator.

## Assumptions and scope

Let \(\mathbb F_{169}\) be the field with \(169\) elements and \(\gamma\) any primitive element. For integers \(e_1,e_2\) satisfying
\[
\gcd(e_1,14)=1,\qquad \gcd(e_2,168)=1,
\]
consider the length-\(168\) code
\[
\mathcal C_{(12e_1,e_2)}
=\left\{\bigl(\operatorname{Tr}_{169/13}(a\gamma^{12e_1i}+b\gamma^{e_2i})\bigr)_{i=0}^{167}:a,b\in\mathbb F_{169}\right\}.
\]
Its dimension is four and minimum distance is \(144\), as follows from the cited primary theorem. Set \(r\equiv e_1e_2^{-1}\pmod {14}\). Since \(e_2\) is invertible modulo \(168\), reordering coordinates gives an equivalent code with generator columns based on \((x^{12r},x)\), for each nonzero \(x\in\mathbb F_{169}\).

Write \(\mathbb F_{169}=\mathbb F_{13}[\zeta]\) with \(\zeta^2=2\). The element \(2\) is nonsquare modulo \(13\), so this is indeed a quadratic field. Identify \((u_0+u_1\zeta,x_0+x_1\zeta)\) with the vector \((u_0,u_1,x_0,x_1)\in\mathbb F_{13}^4\). The trace pairing differs from the corresponding four-row matrix only by the invertible diagonal scaling \(\operatorname{diag}(2,4,2,4)\). Therefore the generator-column projective point set is
\[
S_r=\left\{[u_0:u_1:x_0:x_1]\in\operatorname{PG}(3,13):0\ne x=x_0+x_1\zeta,\;u_0+u_1\zeta=x^{12r}\right\}.
\]
It consists of \(168\) distinct points (no repeated projective coordinates).

## Proof

**Exhaustion of parameters and pairing.** The possible normalized exponents are precisely the units of \(\mathbb Z/14\mathbb Z\), namely \(1,3,5,9,11,13\). Frobenius conjugation sends \(x_0+x_1\zeta\) to \(x_0-x_1\zeta\). Applying the invertible linear transformation \((u_0,u_1,x_0,x_1)\mapsto(u_0,u_1,x_0,-x_1)\) to \(S_r\) yields \(S_{-r}\), since after the variable change \(y=x^{13}\) one has \(x^{12r}=y^{-12r}\). The coordinate positions are permuted accordingly, so the two codes are permutation equivalent. Thus there are at most three equivalence classes.

**Projective distinctness.** If columns for \(x\) and \(y\) are proportional, their last two coordinates force \(y=\lambda x\) with \(\lambda\in\mathbb F_{13}^*\). Since \(\lambda^{12}=1\), their first two coordinates are equal; proportionality forces \(\lambda=1\). Therefore the \(168\) projective points are all distinct.

**Relation to two-dimensional supports.** Every two-dimensional subcode corresponds bijectively, via the injective four-row generator matrix, to a two-dimensional message subspace \(U\subseteq\mathbb F_{13}^4\). Its common zero coordinates are exactly those columns lying in the projective line \(\mathbb P(U^\perp)\). Thus its support size is \(168-|S_r\cap\mathbb P(U^\perp)|\). Orthogonal complementation runs through all projective lines once, so the desired frequencies are exactly the line-intersection frequencies of \(S_r\).

**Complete exact line census.** Each projective line has one reduced row-echelon two-by-four matrix, with pivot columns \(i<j\). The standalone verifier enumerates every such matrix by choosing all allowed free entries in \(\mathbb F_{13}\) and tests all \(14\) projective points on its span. It produces the displayed complete histogram for each of \(r=1,3,5\). The enumeration has exactly
\[
{4\brack2}_{13}=(13^2+1)(13^2+13+1)=31110
\]
lines. In a second, logically different enumeration, all \(\binom{168}{2}=14028\) pairs of distinct columns are assigned to their unique projective line; if a line has \(j\ge2\) columns, it is counted \(\binom j2\) times. Inverting this triangular-number identity reproduces every reported count for \(j\ge2\); the \(j=0,1\) counts are checked by the direct enumeration. Independently, the program tests the total line count and all point-line incidence counts. These are exhaustive finite computations, not extrapolations or sampled experiments.

**Inequivalence.** A monomial coordinate transformation preserves support sizes of subcodes. The histograms are pairwise unequal (one contains lines with \(5\) points, another with \(7\), and the third neither). Hence the three representatives are pairwise monomial inequivalent. Together with the Frobenius pairings, this proves exactly three classes under either monomial or permutation equivalence.

## Verification

Run `python3 verify.py` using only Python's standard library. The program computes, independently for the three representatives, all \(31110\) reduced-echelon lines and all \(14028\) secant pairs; it also checks every one of the \(13^4=28561\) message vectors against the shared Hamming weight enumerator. It explicitly checks projective distinctness and the Frobenius map for negative exponents. Success prints `VERIFY_OK`.

The finite computation is a certificate because the two-by-four reduced-echelon parameterization is bijective to the entire finite set of two-dimensional subspaces. Its completeness, rather than a run-time log, is the essential exhaustive-proof step.

## Relationship to prior work

Hernández and Vega, Theorem 6, already derive the parameters and five-weight Hamming enumerator for the general odd-alphabet family. Their paper also analyzes puncturing, shortening and containment among individual codeword supports, and explains a relation to the perfect-nonlinear-function codes of Li--Qu--Ling. Those results are credited; they do not state the complete two-dimensional subcode-support census or the three-class inequivalence result established here. The invariance of projective line-intersection profiles under monomial equivalence is standard coding-theoretic geometry, but the three exact profiles and resulting classification depend on the present finite census.

## Limitations

This theorem concerns only the stated cyclic family at \(q=13\), not a classification of all \([168,4,144]_{13}\) codes or of the whole odd-prime-power family. The separate support histograms are computer-assisted exact finite proofs whose correctness depends on the openly supplied enumeration; they do not establish a uniform formula for arbitrary alphabets. The ordinary Hamming spectrum is known from the primary source, not newly claimed. Priority against unindexed or inaccessible published computations remains an uncertainty; no independent external mathematical audit has yet been performed.

## References

- F. Hernández and G. Vega, *Few-weight linear codes and their application to secret sharing*, Applicable Algebra in Engineering, Communication and Computing (published 30 September 2026), Theorem 6 and Remark 7. https://doi.org/10.1007/s00200-026-00758-1
- C. Li, L. Qu and S. Ling, *On the covering structures of two classes of linear codes from perfect nonlinear functions*, IEEE Transactions on Information Theory 55 (2009), 70–82. https://doi.org/10.1109/TIT.2008.2008145
