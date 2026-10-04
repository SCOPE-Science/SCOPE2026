# Equality cases for the sharp additive-energy bound on the binary cube

## Finding
Let \(A\subseteq\{0,1\}^d\) be nonempty. Define its additive energy by
\[
E(A)=\bigl|\{(a,b,c,e)\in A^4:a+b=c+e\}\bigr|,
\]
and put \(p=\log_2 6\). The sharp bound \(E(A)\le |A|^p\) has equality exactly for proper affine Boolean cubes. More precisely,
\[
E(A)=|A|^p
\]
if and only if, for some integer \(m\ge 0\), there are \(b,v_1,\ldots,v_m\in\mathbb Z^d\) such that \(v_1,\ldots,v_m\) are linearly independent over \(\mathbb Z\), every point below lies in \(\{0,1\}^d\), and
\[
A=b+\bigl\{\varepsilon_1v_1+\cdots+\varepsilon_mv_m:\varepsilon_j\in\{0,1\}\bigr\}.
\]
In particular, equality forces \(|A|=2^m\), and then \(E(A)=6^m\).

## Assumptions and scope
All sums are taken in \(\mathbb Z^d\), not modulo two. The set \(A\) is finite and nonempty. Here a proper affine Boolean cube means precisely a displayed representation with integer-linearly independent generators; this in particular makes the subset-sum parametrization injective. The rank-zero case is a singleton.

The claim concerns ordinary additive energy, the \(\kappa=2\) case of generalized additive energies. It does not classify equality for every generalized-energy exponent or for arbitrary complex-valued functions in the corresponding Fourier inequalities.

## Proof
Proceed by induction on \(d\). For \(d=0\), the only nonempty set is a singleton, which is a rank-zero affine Boolean cube and has energy one.

For \(d\ge1\), split according to the last coordinate,
\[
A=(A_0\times\{0\})\,\dot\cup\,(A_1\times\{1\}),
\]
where \(A_0,A_1\subseteq\{0,1\}^{d-1}\). Put \(a=|A_0|\), \(b=|A_1|\), and \(e_i=E(A_i)\). For a finite set \(B\subseteq\mathbb Z^{d-1}\), write
\[
r_B(z)=\bigl|\{(x,y)\in B^2:x-y=z\}\bigr|.
\]
An exact last-coordinate decomposition gives
\[
E(A)=e_0+e_1+4N,\qquad N=\sum_z r_{A_0}(z)r_{A_1}(z).
\]
By Cauchy--Schwarz,
\[
N\le\sqrt{e_0e_1}.
\]
Using the induction hypothesis for the inequality and the sharp two-point inequality of Kane--Tao,
\[
a^p+b^p+4(ab)^{p/2}\le(a+b)^p,
\]
whose equality cases are exactly \(ab=0\) or \(a=b\), we obtain
\[
E(A)\le e_0+e_1+4\sqrt{e_0e_1}
\le a^p+b^p+4(ab)^{p/2}
\le(a+b)^p.
\]

Suppose equality holds throughout. Every inequality in this monotone chain must then be equality. Hence each nonempty slice is itself an equality case. If one slice is empty, induction immediately gives the required affine Boolean cube, merely embedded in one last-coordinate hyperplane.

Assume now that both slices are nonempty. The scalar equality condition gives \(a=b\). Equality in Cauchy--Schwarz makes the two nonnegative functions \(r_{A_0}\) and \(r_{A_1}\) proportional. Since \(r_{A_i}(0)=|A_i|\) and the sizes agree, the proportionality factor is one, so
\[
r_{A_0}=r_{A_1}.
\]
By induction, each slice is a proper affine Boolean cube of the same rank \(m\).

It remains to identify two proper affine Boolean cubes with the same difference multiplicities. If \(m=0\), both cubes are singletons and hence translates. Assume \(m\ge1\). Write
\[
B=b_0+\sum_{j=1}^m\{0,u_j\},
\]
with the \(u_j\) integer-linearly independent. Every difference has a unique representation
\[
z=\sum_{j=1}^m\delta_j u_j,\qquad \delta_j\in\{-1,0,1\},
\]
and
\[
r_B(z)=2^{|\{j:\delta_j=0\}|}.
\]
Therefore the nonzero differences having multiplicity \(2^{m-1}\) are exactly \(\{\pm u_1,\ldots,\pm u_m\}\). Thus the complete difference-multiplicity function recovers the generator directions up to permutation and sign. Changing a generator sign only translates the subset-sum cube, so two same-rank proper affine Boolean cubes with identical difference multiplicities are translates of each other. Hence \(A_1=A_0+t\) for some \(t\in\mathbb Z^{d-1}\).

If
\[
A_0=b_0+\sum_{j=1}^m\{0,u_j\},
\]
then
\[
A=(b_0,0)+\sum_{j=1}^m\{0,(u_j,0)\}+\{0,(t,1)\},
\]
which is a proper affine Boolean cube of rank \(m+1\); the last generator is independent of the others because its final coordinate is one.

Conversely, let \(A\) be any proper affine Boolean cube of rank \(m\). Integer linear independence makes the difference coefficients \(\delta_j\in\{-1,0,1\}\) unique, and the same counting gives
\[
E(A)=\sum_{\delta\in\{-1,0,1\}^m}4^{|\{j:\delta_j=0\}|}=(1+4+1)^m=6^m.
\]
Since \(|A|=2^m\) and \(p=\log_2 6\), this equals \(|A|^p\). This proves both directions.

## Verification
The proof above is exact and does not depend on finite experiments. As a separate consistency check, `verify_extremizers.py` exhaustively enumerates every nonempty subset of \(\{0,1\}^d\) for \(1\le d\le4\), computes additive energy exactly, independently recognizes affine Boolean cubes from their difference multiplicities and subset-sum structure, and compares the two predicates.

The exhaustive counts agree in every tested dimension. For \(d=4\), the equality cases by cardinality are 16 singletons, 120 two-point sets, 100 four-point sets, 20 eight-point sets, and the full sixteen-point cube; no mismatch occurs. The stored output ends with `VERIFY_OK`.

## Relationship to prior work
Kane and Tao proved the sharp ordinary-energy inequality \(E(A)\le |A|^{\log_2 6}\) for subsets of the binary cube and supplied the induction and sharp scalar inequality used above. De Dios Pont, Greenfeld, Ivanisvili, and Madrid developed the higher-additive-energy theory on discrete cubes. Crmarić, Kovač, and Shiraki recently placed these bounds in a broader sharp Fourier-inequality framework; their Corollary 2 includes the generalized-energy estimate and notes the full binary cube as an equality example.

The inspected statements and proofs of these sources do not give an if-and-only-if structural classification of all equality sets for the ordinary energy bound. Targeted searches for equality cases, affine Boolean cubes, Hilbert cubes, homometric formulations, and stronger covering statements likewise did not locate a published classification. The present argument extracts the equality constraints from the sharp induction and closes them using the elementary difference-multiplicity rigidity lemma above.

## Limitations
The originality check is necessarily literature-dependent: targeted repository and web searches cannot exclude an unindexed note, folklore argument, or a statement hidden in an inaccessible source. A recent nonlinear Fourier-product preprint was only available through abstract-level metadata during the comparison; its accessible description concerns recovery of sharp bounds rather than equality-set classification.

The result is an equality theorem, not a quantitative stability theorem. It also does not classify extremizing functions for the full Hausdorff--Young or Young convolution inequalities.

## References
1. Tonći Crmarić, Vjekoslav Kovač, and Shobu Shiraki, *Inequalities in Fourier analysis on binary cubes*, arXiv:2507.01359, first posted 2025-07-02. Primary MSC 2020: 42A05.
2. Daniel M. Kane and Terence Tao, *A bound on partitioning clusters*, arXiv:1702.00912, 2017. See the binary-cube additive-energy theorem and its scalar lemma.
3. Pablo de Dios Pont, Nina Greenfeld, Paata Ivanisvili, and José Madrid, *Additive energies on discrete cubes*, arXiv:2112.09352, 2021.
