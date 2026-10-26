# Three rational components of higher commuting-tuple varieties in the four-by-four nilradical

## Finding

Let \(k\) be an algebraically closed field of **arbitrary characteristic**, and let \(\mathfrak n_4(k)\) be the six-dimensional Lie algebra of strictly upper-triangular \(4\times4\) matrices, with bracket \([X,Y]=XY-YX\). For every integer \(r\ge3\), the **reduced** variety
\[
\mathcal C_r=\{(X_1,\ldots,X_r)\in\mathfrak n_4(k)^r:[X_i,X_j]=0\ \text{for all }i,j\}
\]
has exactly **three geometrically irreducible, rational components**. Two have dimension \(3r+3\), and the third has dimension \(4r\). Thus the commuting-triple variety has exactly three components, all of dimension \(12\), whereas for every \(r\ge4\) the variety is not equidimensional and has dimension exactly \(4r\).

The three components are described explicitly by the row coordinates in the next section. There is also a complete arithmetic companion: for every prime power \(q\), the number of ordered commuting \(r\)-tuples in \(\mathfrak n_4(\mathbb F_q)\) is
\[
\boxed{\begin{aligned}
N_r(q)=q^r\bigl[&1+(q^3+q^2+q+1)(q^r-1)\\
&+(q+1)(q^2+1)(q^r-1)(q^r-q)\\
&+(q^r-1)\bigl(q^{2r}+(q^2-1)q^{r+1}\bigr)\bigr].
\end{aligned}}
\]
The counting identity holds for all \(r\ge1\); the new component classification concerns \(r\ge3\). In particular, \(N_3(2)=12160\), \(N_3(3)=1668681\), and \(N_3(4)=52903936\).

## Assumptions and scope

Write the \(i\)-th matrix in a tuple as
\[
X_i=\begin{pmatrix}
0&a_i&d_i&f_i\\0&0&b_i&e_i\\0&0&0&c_i\\0&0&0&0
\end{pmatrix}.
\]
The six arrays \(a,b,c,d,e,f\) are vectors in \(k^r\). The notation \(u\wedge v=0\) means that every \(2\times2\) minor of the two-row matrix \((u;v)\) is zero. This is equivalent to linear dependence, also in characteristic two.

Define the following closed subvarieties of \(\mathcal C_r\):

* \(\mathcal Z_r=\{a=c=0\}\), with \(b,d,e,f\) unrestricted.
* \(\mathcal S_r=\{b=0,\ a\wedge e+d\wedge c=0\}\), with \(f\) unrestricted.
* \(\mathcal R_r\), the closure of tuples having \(b\ne0\) and unique scalars \((\lambda,\mu)\ne(0,0)\) such that \(a=\lambda b\), \(c=\mu b\), and \(\lambda e-\mu d\in kb\).

All three subvarieties are defined over the prime field. The theorem is about the underlying reduced algebraic variety, not its possibly nonreduced commuting scheme. Over finite fields, \(N_r(q)\) counts points, without weighting by scheme multiplicity.

## Proof

**1. Reduction to three exterior equations.** Direct multiplication gives
\[
[X_i,X_j]_{13}=a_ib_j-a_jb_i,\qquad
[X_i,X_j]_{24}=b_ic_j-b_jc_i,
\]
\[
[X_i,X_j]_{14}=a_ie_j-a_je_i+d_ic_j-d_jc_i.
\]
All other commutator entries vanish. Consequently, the equations are exactly
\[
a\wedge b=0,\qquad b\wedge c=0,\qquad a\wedge e+d\wedge c=0,
\]
and \(f\) is free.

**2. The stratum \(b=0\).** On this stratum the only remaining equation is \(a\wedge e+d\wedge c=0\). For every tuple index, regard \((a_i,d_i,c_i,e_i)\) as a vector in the split symplectic four-space \(W=k^4\) with form
\[
\omega((a,d,c,e),(a',d',c',e'))=ae'-a'e+dc'-d'c.
\]
The equation asserts that all \(r\) vectors are pairwise orthogonal for \(\omega\); their span is totally isotropic and has dimension at most two. Every such span lies in a Lagrangian two-plane. The Lagrangian Grassmannian \(\operatorname{LG}(2,4)\) is irreducible, rational, and three-dimensional. Its universal rank-two bundle yields an incidence variety of \(r\) vectors in one Lagrangian plane, of dimension \(3+2r\). For \(r\ge2\), the locus where the vectors span the plane is open and nonempty, and the plane is then unique. Therefore its image is \(\mathcal S_r\), irreducible of dimension \(3+2r+r=3r+3\) after including \(f\). The same dense-open description makes \(\mathcal S_r\) rational.

**3. The stratum \(b\ne0\).** The first two equations force \(a=\lambda b\) and \(c=\mu b\) for unique \(\lambda,\mu\in k\). The third becomes
\[
b\wedge(\lambda e-\mu d)=0.
\]
If \((\lambda,\mu)=(0,0)\), this stratum belongs to \(\mathcal Z_r\). Otherwise the condition says \(\lambda e-\mu d\in kb\), giving a linear fiber of dimension \(r+1\) in \((d,e)\). With the \(r\)-dimensional nonzero \(b\), two scalar parameters, and the free \(r\)-dimensional \(f\), the locus has dimension \(r+2+(r+1)+r=3r+3\). It is an affine vector bundle locally over the irreducible rational base \((k^r\setminus\{0\})\times(k^2\setminus\{0\})\). Its closure \(\mathcal R_r\) is therefore irreducible and rational of dimension \(3r+3\).

**4. The affine component.** The set \(\mathcal Z_r\) is affine space of dimension \(4r\). Every commuting tuple lies in the union \(\mathcal Z_r\cup\mathcal S_r\cup\mathcal R_r\), by the two cases just analyzed. All three are closed and irreducible. To prove that each is a genuine component, it remains to rule out containment.

**5. Noncontainment for \(r\ge3\).** On the dense defining stratum of \(\mathcal R_r\), a nonzero pair \((\lambda,\mu)\) satisfies \(\lambda e-\mu d\in kb\), so the \(3\times r\) matrix with rows \(b,d,e\) has rank at most two. The same rank condition holds on its closure. For \(r\ge3\), \(\mathcal Z_r\) contains points where these three rows are linearly independent; such points have \(b\ne0\), so they lie in neither \(\mathcal R_r\) nor \(\mathcal S_r\). Moreover, \(\mathcal S_r\) has points with \(a,c\) independent; these cannot lie in \(\mathcal R_r\), which satisfies \(a\wedge c=0\), nor in \(\mathcal Z_r\). Finally, \(\mathcal R_r\) has points with \(b\ne0\) and \((a,c)\ne(0,0)\), so it is contained in neither \(\mathcal S_r\) nor \(\mathcal Z_r\). None of the three irreducible closed sets is contained in another, proving the component classification.

For \(r=2\), every nonzero \(b\) makes the quotient \(k^r/kb\) one-dimensional. Thus for arbitrary \(d,e\) there is some nonzero pair \((\lambda,\mu)\) with \(\lambda e-\mu d\in kb\). Letting \(a=t\lambda b\) and \(c=t\mu b\) and then \(t\to0\) shows that the \(b\ne0\) part of \(\mathcal Z_2\) lies in \(\mathcal R_2\); the \(b=0\) part lies in \(\mathcal S_2\). Hence only the two noncontained components \(\mathcal S_2,\mathcal R_2\) remain, agreeing with the established pair case. This boundary argument is not needed to prove the higher-tuple classification.

**6. Finite-field formula.** Over \(\mathbb F_q\), classify the \(b=0\) tuples by the dimension of their isotropic span in \(W\). The rank-zero case contributes \(1\). There are \((q^4-1)/(q-1)=q^3+q^2+q+1\) isotropic lines, and each supports \(q^r-1\) spanning tuples. There are \((q+1)(q^2+1)\) Lagrangian planes, each supporting \((q^r-1)(q^r-q)\) tuples spanning it. Thus the number of choices of \((a,c,d,e)\) with \(b=0\) is
\[
F_r(q)=1+(q^3+q^2+q+1)(q^r-1)
 +(q+1)(q^2+1)(q^r-1)(q^r-q).
\]
For \(b\ne0\), choose \(b\) in \(q^r-1\) ways. The case \(\lambda=\mu=0\) has \(q^{2r}\) arbitrary choices of \((d,e)\). Each of the other \(q^2-1\) scalar pairs gives precisely \(q^{r+1}\) choices, because \((d,e)\mapsto\lambda e-\mu d\) is a surjective linear map to \(k^r\), and the required image is the one-space \(kb\). Multiplication by \(q^r\) for free \(f\) proves the boxed formula. No division by two occurs; all conclusions remain valid in characteristic two.

## Verification

The self-contained `verify.py` uses literal triangular matrix multiplication, independently enumerates bracket-zero row configurations for selected fields and tuple lengths, and counts commuting pairs via independent adjoint-matrix ranks. Run it with `python3 verify.py`. Its successful replay prints `VERIFY_OK_UT4_COMMUTING_TUPLES`. The finite test includes exhaustive commuting triples over \(\mathbb F_2\), exhaustive pairs over \(\mathbb F_3\), and independent pair tests over \(\mathbb F_4\); the geometry and arbitrary-field assertions rest on the proof above, not on these finite tests.

## Relationship to prior work

Goodwin and Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras* (arXiv:1209.1289, 6 September 2012), determine the ordinary **pair** variety for type \(A_3\) and find two components in Section 3.3. This provides the sharp baseline at \(r=2\), not an arbitrary-length component classification. Ngo, *On nilpotent commuting varieties and cohomology of Frobenius kernels* (arXiv:1401.6820, 27 January 2014), Proposition 3.1.2, establishes one regular component of dimension \(3r+3\) in this nilradical; Proposition 3.2.2 gives a non-equidimensionality criterion for this type when \(r>3\). Neither statement lists all components or gives their exact finite-field point counts. The classification above identifies a third component already at the previously unclassified triple threshold and proves the exact dimensions and rationality of all components.

Li, *Commuting Schemes of Upper Triangular Matrices and Representation Homology* (arXiv:2403.13953), studies pair schemes and genus-dependent products of group commutators. Its completeness-of-intersection results do not imply a decomposition for commuting arbitrary-length tuples of **Lie-algebra elements**. General nilpotent-matrix commuting varieties in \(\mathfrak{gl}_4\) concern a different ambient space; their irreducibility properties do not determine those of this fixed nilradical subvariety.

## Limitations

The theorem classifies reduced varieties of tuples in the **fixed** four-by-four strictly upper-triangular Lie algebra; it does not determine scheme multiplicities, components for larger matrices, group-commuting tuples, or the full nilpotent cone of \(\mathfrak{gl}_4\). The algebraic geometry is proved over algebraically closed fields; the arithmetic formula counts rational points over finite fields. Literature comparison, though focused on the closest available primary results, cannot establish definitive historical priority or exclude a previously implicit equivalent formulation.

## References

1. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289 (first public version 6 September 2012), Section 3.3; https://arxiv.org/abs/1209.1289.
2. N. V. Ngo, *On nilpotent commuting varieties and cohomology of Frobenius kernels*, arXiv:1401.6820 (first public version 27 January 2014), Propositions 3.1.2 and 3.2.2; https://arxiv.org/abs/1401.6820.
3. G. Li, *Commuting Schemes of Upper Triangular Matrices and Representation Homology*, arXiv:2403.13953 (first public version March 2024), Introduction and Theorem 3.3; https://arxiv.org/abs/2403.13953.
