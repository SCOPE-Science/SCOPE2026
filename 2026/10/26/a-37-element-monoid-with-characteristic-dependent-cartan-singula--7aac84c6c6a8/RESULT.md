# A 37-element monoid with characteristic-dependent Cartan singularity

## Finding

There is an explicit monoid of order \(37\) whose Cartan matrix is nonsingular over \(\mathbb C\) but singular for the monoid algebra over \(\mathbb F_3\). This is a smaller instance of the biset construction in Eisele's counterexample to the Cartan-determinant conjecture: it replaces the published \(397\)-element witness by a \(37\)-element witness. This does not assert that \(37\) is the minimum possible order.

## Assumptions and scope

Let \(G=S_3\), let \(C_2=\langle(12)\rangle\) and \(C_3=\langle(123)\rangle\), and define subgroups of \(G\times G\) by
\[
L_a=\{(g,g^{-1}):g\in G\},\qquad L_b=\{1\}\times C_2,\qquad L_c=G\times C_3.
\]
Let \(X\) be the disjoint union of one copy of \((G\times G)/L_b\) and six copies of \((G\times G)/L_c\), with the standard left \(G\times G\)-action, viewed as a \((G,G)\)-biset by \((g,h)\cdot x=gxh^{-1}\). Form \(M=G\sqcup X\sqcup\{0\}\), where \(G\) multiplies as a group, its left and right actions on \(X\) are those of the biset, products of two elements of \(X\) equal the absorbing zero, and zero is absorbing. The commuting left and right actions make this an associative monoid.

The orbit sizes are \([G\times G:L_b]=18\) and \([G\times G:L_c]=2\). Thus \(|X|=18+6\cdot2=30\) and \(|M|=6+30+1=37\).

## Proof

Order the ordinary irreducible characters of \(S_3\) as trivial, standard, sign. For the subgroups above, the orbit contribution matrices in Eisele's Cartan formula are
\[
\Delta_b=\begin{pmatrix}1&1&0\\2&2&0\\1&1&0\end{pmatrix},\qquad
\Delta_c=\begin{pmatrix}1&0&1\\0&0&0\\0&0&0\end{pmatrix}.
\]
Consequently the Cartan matrix of the contracted complex monoid algebra is
\[
C_{\mathbb C}=I_3+\Delta_b+6\Delta_c
=\begin{pmatrix}8&1&6\\2&3&0\\1&1&1\end{pmatrix}.
\]
Its determinant is
\[
\det C_{\mathbb C}=8(3)-1(2)+6(2-3)=16\ne0.
\]
For characteristic three, the decomposition matrix of \(S_3\), in the same ordinary-character order and the two simple modular-character columns, is
\[
D=\begin{pmatrix}1&0\\1&1\\0&1\end{pmatrix}.
\]
The Cartan matrix in characteristic three is therefore
\[
C_{\mathbb F_3}=D^{\mathsf T}C_{\mathbb C}D
=\begin{pmatrix}14&10\\7&5\end{pmatrix},
\qquad \det C_{\mathbb F_3}=14\cdot5-10\cdot7=0.
\]
These are integer Cartan matrices; the second determinant is exactly zero, not merely divisible by three. Passing from the contracted algebra to the full monoid algebra adds a \(1\times1\) identity block, so it leaves both nonsingularity conclusions unchanged. This proves the claim.

## Verification

The cardinality calculation is \(6+18+6\cdot2+1=37\). The determinant checks are direct integer arithmetic: \(24-2-6=16\) and \(70-70=0\). The matrices \(\Delta_b\), \(\Delta_c\), and \(D\) are the corresponding matrices displayed or specified in the cited construction; the only changed input is the orbit multiplicity vector, from four copies of \(L_a\), two of \(L_b\), and 165 of \(L_c\), to zero, one, and six respectively.

## Relationship to prior work

Eisele's *A counterexample to a conjecture on Cartan determinants of monoid algebras* defines the monoid \(M(G,X)\), gives the orbit contribution formula in Proposition 2.5, and supplies an \(S_3\)-example in Example 2.7 using four \(L_a\)-orbits, two \(L_b\)-orbits, and 165 \(L_c\)-orbits. That example has order \(6+4\cdot6+2\cdot18+165\cdot2+1=397\). The present result uses the same construction and formulas; the new statement is the explicit smaller coefficient choice and its exact \(37\)-element witness, not a new general mechanism. Steinberg's work supplies the conjectural context and the decomposition-matrix identity used in this line of work.

## Limitations

No lower bound for all possible counterexample monoids is proved, and the order \(37\) is not claimed to be globally minimal. The witness uses the same general construction as Eisele, with a different choice of orbit multiplicities. Other groups, bisets, or monoid constructions could yield smaller examples.

## References

1. F. Eisele, “A counterexample to a conjecture on Cartan determinants of monoid algebras,” arXiv:2306.14002v1, first posted 2023-06-24. https://arxiv.org/abs/2306.14002
2. B. Steinberg, “The modular representation theory of monoids,” arXiv:2305.08251v2 (2023). https://arxiv.org/abs/2305.08251
