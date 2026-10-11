# Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube

## Finding

Let \(V=\mathbb F_2^4\). For every \(A\subset V\) with \(|A|=8\), define \(N(A)\) to be the number of distinct eight-element frequency sets \(B\subset V\) for which the eight Walsh characters \(\chi_b(x)=(-1)^{b\cdot x}\), restricted to \(A\), are an orthogonal basis of \(\mathbb C^A\). Define the complementing-translation set
\[
T(A)=\{t\in V\setminus\{0\}:A+t=V\setminus A\}.
\]
Then the complete spectral-partner classification is:

* If \(A\) is an affine hyperplane, \(N(A)=256\). Writing its direction as \(u^\perp\) for the unique nonzero annihilator \(u\), its spectra are exactly the \(2^8\) transversals of the eight frequency pairs \(\{b,b+u\}\).
* Otherwise \(|T(A)|\in\{0,1,2\}\), and \(N(A)=2|T(A)|\). In this case the spectra are exactly the two affine hyperplanes parallel to \(t^\perp\), for each \(t\in T(A)\); no other spectra exist.

The cardinalities of the four disjoint strata of eight-point sets are
\[
\begin{array}{c|rrrr}
N(A)&0&2&4&256\\\hline
\#\{A: N(A)=\text{given value}\}&10080&1920&840&30.
\end{array}
\]
In particular, exactly \(2790\) of the \(\binom{16}{8}=12870\) eight-point subsets have spectra, and the total number of ordered spectral pairs \((A,B)\) is \(14880\).

Equivalently, the \(16\times16\) Sylvester–Walsh Hadamard matrix has exactly \(14880\) choices of an eight-row set and an eight-column set whose \(8\times8\) restriction is a Hadamard matrix; its eight-row sets have exactly the above multiplicity profile.

## Assumptions and scope

All vector operations, sums of sets, dot products, and orthogonal complements are over \(\mathbb F_2\). A frequency set is counted once as an unordered subset; permutations of its characters are not counted separately. Orthogonality uses ordinary counting measure on \(A\); hence each selected character has squared norm \(8\). Translation of a set is \(A+t=\{a+t:a\in A\}\). An affine hyperplane is a coset of a three-dimensional linear subspace of \(V\). No claim is made for other ambient dimensions, non-binary groups, or frequency multisets.

For any \(E\subset V\), let \(P(E)=\{t:E+t=E\}\) and \(T(E)=\{t\ne0:E+t=E^c\}\). Elements of \(T(E)\) are also called antiperiods. We use the unnormalized Walsh transform \(\widehat f(w)=\sum_{x\in V}f(x)(-1)^{w\cdot x}\).

## Proof

**1. The difference-set bound for non-hyperplanes.** The stabilizer \(P(E)\) is a linear subgroup. If \(T(E)\) is nonempty, its elements form one coset of \(P(E)\), so \(|T(E)|=|P(E)|\). An eight-point set with \(|P(E)|\ge4\) is an affine hyperplane: if \(|P(E)|=4\), it comprises two cosets of a plane, which form an affine line in the quotient \(V/P(E)\); if \(|P(E)|=8\), it is one coset of a hyperplane. Therefore a non-hyperplane eight-point set has \(|T(E)|\le2\).

For \(t\ne0\), the condition \(t\notin E+E\) says that \(E\cap(E+t)=\varnothing\). Because both sets have eight elements in a sixteen-point space, this is equivalent to \(E+t=E^c\). Consequently,
\[
|(E+E)\setminus\{0\}|=15-|T(E)|\ge13
\]
for every non-hyperplane eight-point \(E\).

**2. Fourier zeros of a non-hyperplane.** For \(|A|=8\), the sign function \(s=2\mathbf1_A-1\) takes values \(\pm1\) and has zero mean. Suppose that its Walsh expansion had at most three nonzero coefficients. Write it as \(s=\sum_{j=1}^r c_j\chi_{w_j}\), where \(r\le3\), the \(w_j\) are distinct, and all \(c_j\ne0\). Since \(s^2=1\), each nonconstant Walsh coefficient of \(s^2\) must vanish. But for \(r\le3\), the pair sums \(w_i+w_j\) for \(i<j\) are nonzero and pairwise distinct. Thus the coefficient at \(w_i+w_j\) is exactly \(2c_ic_j\), a contradiction whenever \(r\ge2\). Hence \(r=1\), in which case \(s=\pm\chi_w\) and \(A\) is an affine hyperplane. Contrapositively, a non-hyperplane \(A\) has at least four nonzero Walsh coefficients \(\widehat s(w)\). Since \(\widehat s(0)=0\) and \(\widehat s(w)=2\widehat{\mathbf1_A}(w)\) for \(w\ne0\), the nonzero-frequency Fourier zero set
\[
Z(A)=\{w\in V\setminus\{0\}:\widehat{\mathbf1_A}(w)=0\}
\]
has at most \(11\) elements.

**3. Every spectrum of a non-hyperplane is an affine hyperplane.** Character orthogonality is equivalent to
\[
(B+B)\setminus\{0\}\subseteq Z(A).
\]
If \(B\) were not an affine hyperplane, Step 1 would force its left-hand side to contain at least \(13\) frequencies, while Step 2 permits at most \(11\) Fourier zeros of \(A\). This is impossible. Thus \(B=b+H\), with \(H=t^\perp\) for a unique \(t\ne0\). Its pairwise differences are \(H\setminus\{0\}\). They lie in \(Z(A)\) precisely when \(\widehat{\mathbf1_A}\) vanishes on \(H\setminus\{0\}\).

Set \(g(x)=\mathbf1_A(x)+\mathbf1_A(x+t)\). Its transform satisfies
\[
\widehat g(w)=\bigl(1+(-1)^{w\cdot t}\bigr)\widehat{\mathbf1_A}(w).
\]
It vanishes automatically off \(H\). Vanishing on \(H\setminus\{0\}\) therefore says that \(g\) is constant. Its mean is one, so \(g\equiv1\), equivalent to \(A+t=A^c\). For each \(t\in T(A)\) there are exactly two affine hyperplanes with direction \(t^\perp\), yielding \(N(A)=2|T(A)|\). Distinct \(t\) give different directions, so there is no double-counting.

**4. Hyperplane supports.** If \(A=a+u^\perp\), then \(\widehat{\mathbf1_A}\) is supported on \(\{0,u\}\), and its only nonzero-frequency transform value is at \(u\). Orthogonality therefore holds exactly when no two frequencies in \(B\) differ by \(u\). Eight disjoint pairs \(\{b,b+u\}\) partition the sixteen frequencies, so a valid \(B\) chooses exactly one element from each pair. There are \(2^8=256\) such sets.

**5. The census without enumerating individual sets.** There are \(15\) choices of a three-dimensional direction subspace, each with two affine cosets, so \(30\) affine hyperplanes. For any fixed nonzero \(t\), the group is partitioned into eight pairs \(\{x,x+t\}\); selecting one point from each gives exactly \(2^8\) sets \(A\) satisfying \(t\in T(A)\). Consequently,
\[
\sum_{|A|=8}|T(A)|=15\cdot2^8=3840.
\]
For any ordered pair of distinct nonzero directions \((t,u)\), the subgroup \(\langle t,u\rangle\) has four cosets. A set complemented by translation through both directions has exactly two alternating selections in each of those four cosets. Thus
\[
\sum_{|A|=8}|T(A)|\bigl(|T(A)|-1\bigr)
=15\cdot14\cdot2^4=3360.
\]
Writing \(n_j\) for the number of non-hyperplane eight-point sets with \(|T(A)|=j\), and using \(|T(A)|=8\) for all \(30\) affine hyperplanes, the latter identity gives
\[
2n_2=3360-30\cdot8\cdot7=1680,
\]
so \(n_2=840\). The first identity then gives \(n_1=3840-30\cdot8-2\cdot840=1920\), and the total \(\binom{16}{8}\) gives \(n_0=10080\). Apply the multiplicity formulas of Steps 3–4. Finally,
\[
\sum_{|A|=8}N(A)=2\cdot1920+4\cdot840+256\cdot30=14880.
\]
This proves every assertion.

## Verification

The additional computational cross-check in `checker.py` uses exact integer arithmetic only. It enumerates all \(\binom{16}{8}=12870\) masks, computes Fourier zero masks directly by integer Walsh sums, computes differences of each possible eight-element frequency mask, and counts all partners using the direct orthogonality criterion. It independently counts complementing translations and tests the derived formulas and both double counts. Run using Python 3.10 or newer:

```sh
python checker.py
```

The checker returns `CHECK_PASS` on success. This exhaustive finite calculation corroborates the result, while the proof above establishes it mathematically without reliance on code or floating-point tolerances.

## Relationship to prior work

Kiss, D. Matolcsi, M. Matolcsi, and Somlai (2022) develop the finite-group spectral/tiling and positive-definite weak-tiling framework; in particular their Lemma 1.3 converts character orthogonality to Fourier-zero constraints. Their study concerns tiling implications and complementary four-tuples, not the exact \(8\)-point Walsh spectral-partner multiplicity distribution in \(\mathbb F_2^4\). The new result refines an existence question to every possible partner and a full incidence census.

Herr and Wiegand (2019) develop general methods for complex Hadamard submatrices of cyclic discrete Fourier matrices. Their primitive-set classification applies to the cyclic Fourier matrices \(\mathcal F_m\), not to the noncyclic Walsh character matrix indexed by \(\mathbb F_2^4\); their stated results do not give the present multiplicities. Huckle and Kravvaritis (2017) investigate spectra of Sylvester-Hadamard submatrices, especially leading principal truncations. The accessible abstract does not establish our arbitrary row/column incidence counts, but the full article was not inspected; an equivalent historical enumeration remains a bibliographic risk.

## Limitations

The theorem is specific to eight-point subsets of \(\mathbb F_2^4\) and to distinct Walsh-character frequencies. It neither classifies larger Boolean cubes nor counts non-Walsh orthonormal bases. A separate independent mathematical audit has not been performed. A potentially relevant 2017 Sylvester-submatrix article was accessible at abstract level only, so previous publication of an equivalent characterization or count cannot be ruled out solely from the literature examined.

## References

1. G. Kiss, D. Matolcsi, M. Matolcsi, G. Somlai, *Tiling and weak tiling in \((\mathbb Z_p)^d\)*, arXiv:2212.05513v1, publicly available 11 December 2022. https://arxiv.org/abs/2212.05513
2. J. E. Herr, T. M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets*, arXiv:1909.13145. https://arxiv.org/abs/1909.13145
3. T. K. Huckle, C. D. Kravvaritis, *Properties of submatrices of Sylvester Hadamard matrices*, Linear and Multilinear Algebra 65 (2017), 1629–1642, doi:10.1080/03081087.2016.1250863. Full text not inspected.
