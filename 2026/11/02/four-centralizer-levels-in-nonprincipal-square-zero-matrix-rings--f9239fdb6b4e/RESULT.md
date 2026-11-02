# Four centralizer levels in nonprincipal square-zero matrix rings

## Finding
Let \(q\) be any prime power, \(d\geq 2\) an integer, and
\[
R_{q,d}=\mathbb F_q[\varepsilon_1,\ldots,\varepsilon_d]/(\varepsilon_i\varepsilon_j:1\leq i,j\leq d).
\]
For \(A\in M_2(R_{q,d})\), let \(c(A)=|\{B\in M_2(R_{q,d}):AB=BA\}|\), and put \(P=q^2+q+1\). Then \(c(A)\) assumes **exactly four values**, with the following multiplicities:
\[
\begin{array}{c|l}
 c(A)&\#\{A:c(A)\text{ has this value}\}\\\hline
 q^{2d+2}&(q^4-q)q^{4d}\\
 q^{4d+1}&q\bigl(q^{4d}-q^d-P(q^{2d}-q^d)\bigr)\\
 q^{4d+2}&qP(q^{2d}-q^d)\\
 q^{4d+4}&q^{d+1}
\end{array}
\]
All four rows have positive multiplicity for \(d\geq2\). In particular, the exact number of ordered commuting pairs is
\[
 C_{q,d}=(q^4-q)q^{6d+2}
 +q^{4d+2}\Bigl[q^{4d}-q^d+(q-1)(q^2+q+1)(q^{2d}-q^d)\Bigr]
 +q^{5d+5}.
\]
As \(d\to\infty\) with \(q\) fixed, the commuting probability converges to a **positive** limit:
\[
\Pr_{A,B\in M_2(R_{q,d})}(AB=BA)=\frac{C_{q,d}}{q^{8d+8}}=q^{-6}+O_q(q^{-2d}).
\]

## Assumptions and scope
The coefficient algebra is split, commutative, local and Artinian, with maximal ideal \(J=(\varepsilon_1,\ldots,\varepsilon_d)\), \(J^2=0\), and \(\dim_{\mathbb F_q}J=d\). All counts include nonunits and the zero matrix. The theorem applies to every finite field, including characteristic two, and every \(d\ge2\). It does **not** assert the same formula for arbitrary mixed-characteristic local rings or higher nilpotency lengths.

## Proof
Write every matrix uniquely as
\[
 A=A_0+\sum_{i=1}^d\varepsilon_i A_i,
 \qquad B=B_0+\sum_{i=1}^d\varepsilon_i B_i,
 \qquad A_i,B_i\in M_2(\mathbb F_q).
\]
The coefficient equations for \(AB=BA\) are
\[
 [A_0,B_0]=0,\qquad [A_0,B_i]+[A_i,B_0]=0\quad(1\le i\le d).
\]

**Nonscalar residue.** If \(A_0\) is nonscalar, its centralizer in \(M_2(\mathbb F_q)\) is precisely \(\mathbb F_q I+\mathbb F_q A_0\), of size \(q^2\). To see this in arbitrary characteristic, choose a vector \(v\) for which \(v,A_0v\) are linearly independent; otherwise every line would be invariant and \(A_0\) would be scalar. A commuting endomorphism is determined by its image of \(v\), so has dimension two, and the displayed two-dimensional span is contained in it. Hence \(B_0=aI+bA_0\). Every remaining equation becomes
\[
 [A_0,B_i-bA_i]=0,
\]
with exactly \(q^2\) choices of \(B_i\), independently for all \(i\). Thus \(c(A)=q^{2d+2}\) for each of the \((q^4-q)q^{4d}\) matrices with nonscalar \(A_0\).

**Scalar residue.** If \(A_0=aI\), all \(B_i\) are arbitrary (\(q^{4d}\) choices). The only constraint on \(B_0\) is that it commute with the full tuple \((A_1,\ldots,A_d)\). When every \(A_i\) is scalar, the common centralizer is all \(M_2(\mathbb F_q)\), of dimension four. There are \(q^d\) scalar tuples, and \(q\) possible \(a\); this gives \(q^{d+1}\) matrices with centralizer size \(q^{4d+4}\).

If at least one \(A_j\) is nonscalar, the common centralizer of the tuple is either \(\mathbb F_q I+\mathbb F_q A_j\) (dimension two) or \(\mathbb F_q I\) (dimension one). Indeed, centralizing \(A_j\) restricts \(B_0\) to \(uI+vA_j\); any other \(A_i\) not commuting with \(A_j\) forces \(v=0\). Moreover, the tuple has a two-dimensional common centralizer exactly when every \(A_i\) lies in that same two-dimensional algebra (because the centralizer of any nonscalar element of it is the whole algebra).

There are exactly
\[
 \frac{q^4-q}{q^2-q}=q^2+q+1=P
\]
subalgebras \(\mathbb F_q I+\mathbb F_q T\) with \(T\) nonscalar: every one has \(q^2-q\) nonscalar matrices, and each nonscalar matrix determines its algebra uniquely. In any one such algebra, exactly \(q^{2d}-q^d\) tuples contain a nonscalar member; each such tuple belongs to only one of the \(P\) algebras. Thus exactly \(P(q^{2d}-q^d)\) radical tuples have a two-dimensional common centralizer, and the remaining \(q^{4d}-q^d-P(q^{2d}-q^d)\) have a one-dimensional common centralizer. Multiplying each by the \(q\) choices of scalar residue establishes the remaining two rows of the table.

The four counts sum to \(q^{4d+4}=|M_2(R_{q,d})|\); they are nonzero for \(d\ge2\) (e.g. take two noncommuting radical coefficient matrices for the one-dimensional stratum). Summing \(c(A)\) proves the commuting-pair formula. Dividing it by \(q^{8d+8}\) yields the limit: the scalar-residue, one-dimensional-common-centralizer stratum contributes \(q^{-6}(1+O_q(q^{-2d}))\); all other contributions are \(O_q(q^{-2d})\).

## Verification
The independent finite-field checker `verify.py` constructs every \(2\)-by-\(2\) coefficient matrix over the specified truncated ring, builds the commutator linear transformation on the full vector space, and computes each centralizer cardinality from its kernel dimension. Complete enumeration passed for \((q,d)=(2,1),(2,2),(3,1)\), involving \(256\), \(4096\), and \(6561\) matrices respectively. For \((q,d)=(2,2)\), the four centralizer multiplicities, listed in increasing size order, are \((3584,336,168,8)\), and the total commuting-pair count is \(606208\). An additional independent direct product enumeration of all \(256^2\) ordered pairs for \((q,d)=(2,1)\) gives \(6400\) commuting pairs. Run `python3 verify.py`; success ends with `VERIFY_OK`. The general proof, not the finite tests, covers arbitrary prime powers.

## Relationship to prior work
Xi and Zhang [1] investigate structural properties of centralizer matrix algebras and their Frobenius/cellular structures; the main theorems do not enumerate finite-ring centralizer-size fibers. Prasad, Singla and Spallone [2] count similarity classes and centralizers over principal length-two local rings, and **Section 10 explicitly names the same nonprincipal coefficient algebra** \(\mathbb F_q[\varepsilon_1,\ldots,\varepsilon_d]/(\varepsilon_i\varepsilon_j)\), reducing general similarity classification to a difficult simultaneous-conjugacy problem. Their nonprincipal section does not produce the elementwise four-stratum commutant count or its limiting commuting probability. Shumyatsky and Vannacci [3] prove a general structural theorem from a commuting-probability lower bound, not an exact enumeration for this family. The familiar one-radical-generator case is not claimed as new here.

## Limitations
This is an exact element-centralizer *size* classification, not a classification of similarity or conjugacy orbits; it does not solve the wild simultaneous-conjugacy problem. It treats split square-zero local algebras only. Although the cited relevant texts and mathematical-record searches did not reveal the exact four-stratum formula, a different earlier centralizer enumeration or a general tensor-algebra counting theorem might imply it; historical priority has not been independently certified. Independent expert mathematical validation has not been performed.

## References
[1] C. Xi and J. Zhang, *Structure of centralizer algebras*, first public preprint 21 December 2020, arXiv:2012.11089v1, especially introduction and Theorems 1.1–1.2. https://arxiv.org/abs/2012.11089

[2] A. Prasad, P. Singla and S. Spallone, *Similarity of matrices over local rings of length two*, first public preprint 26 December 2012, arXiv:1212.6157, especially Section 10 and Corollary 10.4. https://arxiv.org/abs/1212.6157

[3] P. Shumyatsky and M. Vannacci, *Commuting and product-zero probability in finite rings*, first public preprint 24 July 2023, arXiv:2307.12633v1, especially Corollary 1.2. https://arxiv.org/abs/2307.12633
