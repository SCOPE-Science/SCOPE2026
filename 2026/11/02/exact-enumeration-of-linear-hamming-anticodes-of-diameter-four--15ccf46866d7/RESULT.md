# Exact enumeration of linear Hamming anticodes of diameter four

## Finding

Let \(q\) be any prime power, let \(n\geq 0\), and let \(L_q(n,4)\) denote the number of distinct labeled linear subspaces \(C\leq\mathbb F_q^n\) for which every codeword has Hamming weight at most four. The zero subspace is counted. Define \(\binom ns=0\) when \(s>n\). Then, for **every** such \(q,n\),

\[
\begin{aligned}
L_2(n,4)&=1+n+2\binom n2+6\binom n3+26\binom n4+91\binom n5+100\binom n6+30\binom n7,\\
L_3(n,4)&=1+n+3\binom n2+15\binom n3+129\binom n4+200\binom n5,\\
L_4(n,4)&=1+n+4\binom n2+28\binom n3+388\binom n4+162\binom n5,\\
L_q(n,4)&=1+n+q\binom n2+q(2q-1)\binom n3
 +(q^4+3q^3-4q^2+q)\binom n4\qquad(q\geq5).
\end{aligned}
\]

Consequently the exact fixed-diameter polynomial degrees \(\sigma_q(4)\) are \(7\) when \(q=2\), \(5\) when \(q=3\) or \(4\), and \(4\) when \(q\geq5\). The unique full-support binary length-seven type is the binary simplex \([7,3,4]\) code; it has exactly \(30\) distinct coordinate-labeled realizations.

## Assumptions and scope

The alphabet is the finite field \(\mathbb F_q\), with \(q\) a prime power. Hamming weight counts nonzero coordinates. For a linear code, its Hamming diameter equals its maximum codeword weight, because differences of two codewords are codewords. Neither self-orthogonality nor a minimum-distance constraint is imposed. A labeled code means an actual subspace of the fixed ordered coordinate space, not an equivalence class under permutations or monomial transformations. This result concerns diameter **at most** four, not exactly four. It remains valid at \(n\leq4\), where all subspaces qualify.

## Proof

**Support reduction.** For \(s\geq0\), let \(a_q(s,4)\) count full-support subspaces of \(\mathbb F_q^s\) having maximum weight at most four, with \(a_q(0,4)=1\). Puncturing off the zero coordinates gives a unique full-support code on a uniquely specified set of \(s\) positions. Thus

\[
L_q(n,4)=\sum_{s=0}^n\binom ns\,a_q(s,4). \tag{1}
\]

For a positive-dimensional, full-support subspace of dimension \(k\), precisely \((q-1)q^{k-1}\) of its \(q^k\) codewords are nonzero at each position. Double-counting weights gives

\[
s(q-1)q^{k-1}=\sum_{c\in C}\operatorname{wt}(c)
 \leq 4(q^k-1).
\]

In particular, \(s<4q/(q-1)\). Therefore \(s\leq7\) at \(q=2\), \(s\leq5\) at \(q=3,4\), and \(s\leq4\) for every prime power \(q\geq5\). The zero subspace is the sole support-zero case. This is a strict finite-dimensional cutoff; it does not assume an asymptotic theorem.

**The universal short supports.** On \(s\leq4\) coordinates every subspace automatically obeys the diameter restriction. Let

\[
G_q(j)=\sum_{k=0}^j {j\brack k}_q,
\]

where the bracket denotes a Gaussian binomial coefficient, the number of \(k\)-dimensional subspaces of \(\mathbb F_q^j\). Inclusion-exclusion over coordinates identically zero on the subspace yields

\[
a_q(s,4)=\sum_{j=0}^{s}(-1)^{s-j}\binom sj G_q(j)\quad(0\leq s\leq4).
\]

Using the Gaussian binomial formulas for \(j\leq4\) gives, in increasing order of support,

\[
(a_q(0,4),\ldots,a_q(4,4))
=(1,1,q,q(2q-1),q^4+3q^3-4q^2+q). \tag{2}
\]

**All remaining finite supports.** The remaining coefficients, with a refinement by subspace dimension \(k\), are as follows. Blank entries mean zero.

| Field | Support | Dimension-specific counts | Total |
|---|---:|---|---:|
| \(\mathbb F_2\) | 5 | \(k=2:25,\ k=3:55,\ k=4:11\) | 91 |
| \(\mathbb F_2\) | 6 | \(k=2:15,\ k=3:75,\ k=4:10\) | 100 |
| \(\mathbb F_2\) | 7 | \(k=3:30\) | 30 |
| \(\mathbb F_3\) | 5 | \(k=2:160,\ k=3:40\) | 200 |
| \(\mathbb F_4\) | 5 | \(k=2:162\) | 162 |

These are exact **exhaustive finite** counts, not sampling. The accompanying standalone program `census_linear_d4.py` enumerates every reduced-row-echelon generator matrix of every rank on each indicated fixed support; each subspace has exactly one such matrix. For every enumerated subspace it enumerates **all** message vectors and checks all resulting codeword weights and whether each coordinate belongs to the support. It also checks that the number of enumerated matrices equals the sum of Gaussian binomial coefficients. For \(\mathbb F_4\) it performs arithmetic in \(\mathbb F_2[z]/(z^2+z+1)\) and checks field multiplication and distributivity. The exact recorded output, including each dimension count, is in `census_linear_d4.stdout`. Hence the finite coefficient table is a complete, reproducible certificate; the strict support cutoff above proves there are no further coefficients at any ambient length.

As a structural cross-check independent of the finite table, for a binary full-support length-seven code with a rank-\(k\) generator whose nonzero columns have multiplicities \(m_v\), the Hamming weight \(W\) of a uniformly chosen codeword has

\[
\mathbb E W=\tfrac72,\qquad
\mathbb E W^2=\tfrac14\left(49+\sum_v m_v^2\right).
\]

Since \(0\leq W\leq4\), one has \(\mathbb E W^2\leq4\mathbb E W=14\), so \(\sum_vm_v^2\leq7\). Because seven nonzero columns exist, equality holds and all seven columns are distinct. Equality in the moment bound also forces all codeword weights to belong to \(\{0,4\}\). Injectivity of the message-to-codeword map gives

\[
7\cdot2^{k-1}=4(2^k-1),
\]

forcing \(k=3\). The columns are exactly the seven nonzero vectors of \(\mathbb F_2^3\), giving the simplex code. Its coordinate-labeled count is

\[
\frac{7!}{|\operatorname{GL}(3,2)|}=\frac{5040}{168}=30.
\]

Combining the support cutoff, (1), (2) and the finite counts proves every polynomial stated in the finding and the degree assertions.

## Verification

Run `python3 census_linear_d4.py` using ordinary Python 3. The program requires only standard-library modules. The supplied output file is an actual successful run. In particular it reports full-support profiles \((1,1,2,6,26,91,100,30)\) at \(q=2\), \((1,1,3,15,129,200)\) at \(q=3\), and \((1,1,4,28,388,162)\) at \(q=4\). The program checks field axioms for its finite arithmetic, checks full enumeration counts using Gaussian binomial coefficients, independently checks the support decomposition at the largest enumerated ambient length in each field, and checks the inclusion-exclusion formulas at short supports. The mean-weight argument establishes that these fixed-size finite computations cover **all possible nonzero supports** for the full infinite-\(n\) assertion.

## Relationship to prior work

Horlemann and Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (first publicly available October 22, 2026), Proposition 4.3 and Theorem 4.6, give the support decomposition and the fixed-diameter polynomial-order statement with an unspecified exponent \(\sigma_q(d)\). Those facts are inputs acknowledged here. They do not evaluate the complete diameter-four coefficients or specify \(\sigma_q(4)\) for all fields. The present claim is precisely the complete evaluated polynomial, the field-dependent degree, and the extremal binary support type.

Ravagnani's 2016 optimal-anticode classification studies spaces attaining dimension equal to maximum weight; it does not provide the number of **all** subspaces with maximum weight at most four. Di Giusto, Gorla, and Ravagnani (arXiv:2512.17542) study generalized-weight and optimal-anticode test families, rather than this enumeration. Existing simplex-code facts account for the length-seven structural ingredient, but do not give the other finite-support coefficients or their assembled all-length polynomial.

## Limitations

The theorem treats linear subspaces, not arbitrary anticode subsets, and fixes the Hamming-diameter ceiling to four. It does not give formulas for larger diameter or for simultaneous field-size/diameter growth. The numerical coefficients at supports five through seven are established by exhaustive finite RREF enumeration, not by a uniform closed-form symbolic classification of every small-support type. Publication priority beyond the inspected sources may still require independent confirmation. No independent mathematical audit or external formal certification is claimed.

## References

1. A.-L. Horlemann and A. Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1 (October 22, 2026), especially Proposition 4.3, Theorem 4.6, and Remark 4.7. https://arxiv.org/pdf/2610.31618v1
2. A. Ravagnani, *Generalized weights: an anticode approach*, Journal of Pure and Applied Algebra 220 (2016), 1946–1962; arXiv:1410.7207, especially Section 2. https://arxiv.org/pdf/1410.7207
3. A. Di Giusto, E. Gorla, and A. Ravagnani, *A distance-free approach to generalized weights*, arXiv:2512.17542v1 (December 19, 2025). https://arxiv.org/pdf/2512.17542
