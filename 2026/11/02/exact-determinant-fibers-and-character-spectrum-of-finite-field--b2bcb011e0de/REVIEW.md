# Scientific review: Hankel determinant fibers

## Correctness — PASS

The normalization uses the \(q\)-to-one Hermite-pair parameterization of nonsingular Hankel matrices, proved in García-Armas, Ghorpade, and Ram, Theorem 3.5. Its Barnett factorization and Vandermonde diagonalization establish the exact sign \(arepsilon_n\) in \(\det H=arepsilon_n\operatorname{Res}(u,v)\); no sign-free substitution is assumed. For a character of order \(r\), the sum over units modulo \(P^e\) is zero unless \(r\mid e\). The local generating factors multiply to \((1-q^rz^r)/(1-q^{r+1}z^r)\), giving each coefficient and exact Fourier inversion. Character orthogonality proves the if-and-only-if uniformity criterion. The script tests finite instances only; all finite-field degrees and matrix orders follow from the algebraic argument.

## Originality — PASS, subject to identified literature risk

The complete accessible original article arXiv:1011.1760v1 supplies the q-to-one map and total nonsingular/rank enumerations but not prescribed nonzero determinant fibers. The complete accessible arXiv:2109.05415v1 fixes initial anti-diagonal entries while counting rank, a genuinely different invariant. Comparison was made at theorem and implication level: aggregate rank counts do not determine multiplicative-character Fourier coefficients. Searches for exact determinant distributions, resultant-character sums, and Toeplitz aliases revealed no direct stronger theorem among inspected accessible sources. A 1960 persymmetric-matrix distribution paper and other specialist sources could contain overlapping results; its full text was not available for an affirmative exclusion claim. No claim of literature-wide novelty or independent validation is made.

## Mathematical value — PASS

The theorem classifies every fiber of the determinant map on a classical structured matrix space, rather than merely the zero/nonzero split. The exact Fourier-spectrum support criterion \(r\mid n\), integer Ramanujan formulas, and sharp equidistribution boundary \(\gcd(n,q-1)=1\) constitute natural, reusable arithmetic structure valid in all finite characteristics and extension degrees. For example, the nonsingular total alone cannot distinguish the nonuniform \(q=5,n=2\) determinant fibers \((30,20,20,30)\).

## Limitations and references

No claim is made for coefficient-constrained Hankel spaces, general finite rings, or arbitrary structured matrices. Historical distribution references not accessed in full are a residual originality risk. Key references: García-Armas–Ghorpade–Ram (2010), arXiv:1011.1760v1, Proposition 3.4, Theorems 3.5 and 5.1; Dwivedi–Grinberg (2021), arXiv:2109.05415v1, Theorems 1.1 and 1.5; Daykin (1960), DOI 10.1515/crll.1960.203.47 (full text not inspected).

Self-review: passed. Independent audit: not yet performed.
