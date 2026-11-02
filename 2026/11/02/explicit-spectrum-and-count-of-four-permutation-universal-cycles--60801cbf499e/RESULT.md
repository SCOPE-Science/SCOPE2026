# Explicit spectrum and count of four-permutation universal cycles

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(n\ge5\). Let \(P_{n,4}\) be the \(n(n-1)(n-2)(n-3)\) length-four words whose letters are pairwise distinct. A *universal cycle* is a circular word of **exact length \(n(n-1)(n-2)(n-3)\)** over \(\Sigma\) in which every member of \(P_{n,4}\) appears exactly once as a cyclic factor. Count cycles up to cyclic rotation only, **not** reversal or relabeling.

Put
\[
N=n(n-1)(n-2),\quad d=n-3,\quad
E=\frac{N}{3}-(n-1)^2,\quad
s=\frac{n(n-3)}2,\quad t=\frac{(n-1)(n-2)}2.
\]
Then the exact number \(U_{n,4}\) of universal cycles is
\[
\boxed{U_{n,4}=\frac{((n-4)!)^{N}}{N}
(d+1)^E(d^2-d+1)^{E+1}
(nd^2)^{n-1}
\bigl(d(d+2)(d-1)\bigr)^s
\bigl(d^2(d-1)\bigr)^t.}
\]
In particular, \(U_{5,4}=7{,}044{,}820{,}107{,}264{,}000\) (the known shorthand case), while
\[
\boxed{U_{6,4}=2^{171}3^{43}5^8 7^{16}.}
\]

More structurally, let \(A_n\) be the \(N\times N\) adjacency matrix on distinct ordered triples, with an arc \((a,b,c)\to(b,c,e)\) when all four letters are distinct. Its characteristic polynomial is exactly
\[
\boxed{\begin{aligned}
\det(xI-A_n)={}&(x^3+1)^E(x-d)(x^2-x+1)\\
&\cdot(x^3+x^2+dx+d^2)^{n-1}\\
&\cdot(x^3+x^2-x-d)^s\\
&\cdot(x^3-x^2+x-d)^t.
\end{aligned}}
\]
The characteristic-polynomial identity is stronger than the enumeration identity and allows the latter to be evaluated without a growing matrix determinant.

## Assumptions and scope

All \(n\) symbols are labeled; \(n\) is an integer at least five; factors wrap around the circular word. The equivalence relation is **rotation alone**. The restriction is pairwise distinctness in each consecutive block of four. The required cycle length is exactly \(|P_{n,4}|=Nd\); there are no additional forbidden factors. The theorem does not count universal cycles of arbitrary permutations understood as order-isomorphism classes, nor universal cycles for \(k\)-subsets or shortened/partial universality.

## Proof

**1. Eulerian correspondence.** Let \(V_3\) be the vector space of rational-valued functions on the \(N\) ordered triples with distinct entries, and \(V_2\) the analogous space on the \(n(n-1)\) ordered pairs. The overlap graph with adjacency \(A_n\) is \(d\)-in-regular and \(d\)-out-regular, and each arc corresponds bijectively to a length-four distinct-letter word. An Eulerian circuit therefore gives a universal cycle, with cyclic shifts of the arc order identified. Distinct arcs ensure no shorter rotational period. Connectivity follows, for example, from the known existence theorem for \(k\)-permutation universal cycles when \(k<n\) (Jackson, 1993), or from the positive arborescence product obtained below.

**2. Rank reduction.** Define the three-cycle operator
\[
(Rf)(a,b,c)=f(b,c,a),
\]
and the maps \(D:V_3\to V_2\), \(J:V_2\to V_3\) by
\[
(Df)(b,c)=\sum_{e\notin\{b,c\}}f(b,c,e),\qquad
(Jg)(a,b,c)=g(b,c).
\]
The forbidden fourth symbol is \(a\), so \(A_n=JD-R\). As \(R^3=I\) and the triples split into \(N/3\) rotation orbits, \(\det(xI+R)=(x^3+1)^{N/3}\), and
\[
(xI+R)^{-1}=\frac{x^2I-xR+R^2}{x^3+1}.
\]
The matrix determinant lemma, initially over the rational-function field, yields
\[
\det(xI-A_n)=(x^3+1)^{N/3-n(n-1)}\det H(x),
\]
where
\[
H(x)=(x^3+1)I-x^2DJ+xDRJ-DR^2J.
\]
Write \(r_c=\sum_{e\ne c}g(c,e)\) and \(c_b=\sum_{e\ne b}g(e,b)\). Direct substitution gives
\[
(Hg)(b,c)=(x^3-n+3)g(b,c)+(x^2-x)g(c,b)-x^2r_c+xc_b.
\]
The displayed rational-function identities are polynomial identities after taking determinants, including at the roots of \(x^3+1\).

**3. Exact invariant-space determinant.** The pair space is a direct sum over \(\mathbb Q\) of (i) matrices with all row sums and column sums zero and (ii) matrices \(g(b,c)=u_b+v_c\). This follows because on mean-zero vectors the row/column-sum map has coefficient matrix \(\left(\begin{smallmatrix}n-1&-1\\-1&n-1\end{smallmatrix}\right)\), of determinant \(n(n-2)\ne0\); the complementary common-constant direction is also nonsingular.

On the zero-sum part, transpose is an involution. The symmetric subspace has dimension \(s=n(n-3)/2\), because the degree-sum incidence matrix of the complete graph has rank \(n\). The skew-symmetric subspace has dimension \(t=(n-1)(n-2)/2\), because the signed incidence matrix has rank \(n-1\). The two respective scalar factors of \(H\) are
\[
F_+(x)=x^3+x^2-x-d,\qquad F_-(x)=x^3-x^2+x-d.
\]

On the constant matrix \(g=1\), the scalar factor is
\[
(x-d)(x^2-x+1).
\]
On each of the \(n-1\) independent mean-zero coordinate directions in \(g(b,c)=u_b+v_c\), \(H\) acts on the two coefficient vectors by
\[
\begin{pmatrix}
\alpha-x & x^2+(n-2)x\\
-(n-2)x^2-x & \alpha+x^2
\end{pmatrix},\qquad \alpha=x^3-n+3.
\]
Its determinant expands exactly to
\[
(x^3+1)(x^3+x^2+dx+d^2).
\]
Consequently,
\[
\det H=(x-d)(x^2-x+1)
\bigl((x^3+1)(x^3+x^2+dx+d^2)\bigr)^{n-1}
F_+(x)^sF_-(x)^t.
\]
Substituting into the rank-reduction identity produces the stated characteristic polynomial, because the total exponent on \(x^3+1\) is \(N/3-(n-1)^2=E\). All dimensions add to \(N\), verifying no omitted eigenvalues or factors.

**4. Matrix-tree and BEST.** At \(x=d\), the factors other than \(x-d\) are strictly positive for \(n\ge5\). The graph is vertex-transitive under alphabet relabeling; hence all \(N\) directed Laplacian cofactors are equal. The directed matrix-tree theorem thus gives the number of in-arborescences rooted at any given triple:
\[
\tau_n=\frac1N\lim_{x\to d}\frac{\det(xI-A_n)}{x-d}.
\]
Evaluating the factors at \(x=d\) gives
\[
\tau_n=\frac1N(d+1)^E(d^2-d+1)^{E+1}(nd^2)^{n-1}
\bigl(d(d+2)(d-1)\bigr)^s\bigl(d^2(d-1)\bigr)^t.
\]
The BEST theorem counts cyclic Eulerian tours by \(\tau_n\prod_{v}(\deg^+(v)-1)!=\tau_n((n-4)!)^N\), proving the universal-cycle formula. There is no extra factor for the choice of starting position.

## Verification

The accompanying standard-library-only `verify.py` builds the original directed overlap graphs independently, computes their exact integer Laplacian cofactors by fraction-free elimination for \(5\le n\le8\), and compares them with the closed arborescence formula. It also evaluates the characteristic polynomial as an independent direct determinant at seven integer arguments for \(n=5,6,7\). It prints `VERIFY_OK` when every assertion succeeds. The checked vertex counts are \(60,120,210,336\); the corresponding arborescence counts have \(16,55,124,233\) decimal digits. These finite checks are cross-checks, not the proof of the all-\(n\) statement; that proof is the exact operator decomposition above.

Execute: `python3 verify.py`.

## Relationship to prior work

Chang and Xue (arXiv:2111.13814, initially public on 2021-11-27) give exact formulas for permutation-word universal cycles for \(k=2\) and \(k=3\), and express the general problem in terms of adjacency/Laplacian eigenvalues. Their Sections 1–4 do not evaluate the \(k=4\) spectrum or supply this all-alphabet product formula. The present result explicitly computes the next-order spectrum and eliminates the graph-size determinant.

The OEIS shorthand-permutation entry A120061 records the known boundary value \(n=5,k=4\), which agrees exactly with the formula; it concerns \(k=n-1\) and therefore does not furnish the \(n\ge6,k=4\) sequence. The arrangement graph studied by Chen, Ghorbani and Wong (2013) joins tuples that differ in one coordinate; it is not the directed shift-and-append graph used here. Jackson (1993) establishes existence, not this cardinality. Results on shortened cycles using order-isomorphic permutations address a different alphabet representation and equivalence relation.

## Limitations

This counts only universally covering *literal* four-tuples with distinct labels, not unlabeled pattern classes or reversal classes. It does not provide an explicit fast generator for the cycles themselves or a general formula for all window lengths \(k\). A broader previously unindexed spectral identity might imply these factors; the cited primary sources and published-database searches did not show such an identity. Mathematical correctness is established by the displayed proof and reproducible finite checks, but independent expert validation has not been performed.

## References

1. Z. Chang and J. Xue, *Enumerations of Universal Cycles for \(k\)-Permutations*, first posted 2021-11-27, https://arxiv.org/abs/2111.13814 (Sections 1–4, especially the counting lemma and the two/three-permutation formulas).
2. B. W. Jackson, *Universal cycles of \(k\)-subsets and \(k\)-permutations*, Discrete Mathematics **117** (1993), 141–150, https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=4120477 (existence theorem; bibliographic reference).
3. The OEIS Foundation, A120061, *Number of universal cycles for permutations of \(n\) objects*, https://oeis.org/A120061 (the shorthand boundary case, not an all-\(k=4\) formula).
4. B. F. Chen, E. Ghorbani and K. B. Wong, *Cyclic Decomposition of \(k\)-Permutations and Eigenvalues of the Arrangement Graphs*, Electronic Journal of Combinatorics **20** (2013), P22, https://doi.org/10.37236/3711 (a distinct, undirected tuple graph).
5. S. Kitaev, A. Potapov and V. Vajnovszki, *On shortening u-cycles and u-words for permutations*, Discrete Applied Mathematics **260** (2019), 203–213, https://doi.org/10.1016/j.dam.2019.01.025 (shortened order-pattern setting, not this literal-label enumeration).
