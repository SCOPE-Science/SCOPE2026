# Exact Smith distributions for rank-one repairs over finite chain rings

## Finding

**Theorem (rank-one repair distribution).** Let \(R\) be a finite commutative chain ring of length \(t\ge 1\), maximal ideal \((\pi)\), and residue field of cardinality \(q\). Hence \(|R|=q^t\). Put \(\nu(0)=t\) and for nonzero \(x\in R\) let \(\nu(x)\in\{0,\ldots,t-1\}\) be the unique valuation with \(x\in(\pi^{\nu(x)})\setminus(\pi^{\nu(x)+1})\).

Fix \(n\ge2\), \(d\in R^\times\), and \(A\in M_n(R)\) equivalent by invertible left and right multipliers to \(\operatorname{diag}(I_{n-1},0)\). Independently choose \(E\in R^{n\times1}\) and \(F\in R^{1\times n}\) uniformly. Write \(E=(u,e)^\mathsf T\), \(F=(v,f)\) in coordinates in which \(A=\operatorname{diag}(I_{n-1},0)\), and set

\[\alpha=\nu(1+dvu),\quad\beta=\nu(f),\quad\gamma=\nu(e),\quad i=\min(\alpha,\beta,\gamma),\quad j=\min(t,\beta+\gamma-i).\]

Then the Smith invariant-exponent tuple of \(A+EdF\) equals \((0,\ldots,0,i,j)\) with exactly \(n-2\) initial zeros. In particular \(0\le i\le j\le t\), with exponent \(t\) denoting a zero invariant factor.

Define \(a_t(k)=(1-q^{-1})q^{-k}\) for \(0\le k<t\), \(a_t(t)=q^{-t}\), and, writing \(m=n-1\), define

\[b_{m,t}(0)=1-\frac{1-q^{-m}}q,\qquad b_{m,t}(k)=(1-q^{-m})a_t(k)\quad(1\le k\le t).\]

The exact probability of Smith type \((0^{n-2},i,j)\), for every \(0\le i\le j\le t\), is

\[P_{n,q,t}(i,j)=\sum_{\alpha,\beta,\gamma=0}^{t} b_{m,t}(\alpha)a_t(\beta)a_t(\gamma)\,\mathbf1\!\left\{i=\min(\alpha,\beta,\gamma),\;j=\min(t,\beta+\gamma-i)\right\}.\]

Consequently the exact number of ordered pairs \((E,F)\) of this Smith type is \(q^{2nt}P_{n,q,t}(i,j)\). The law depends only on \((n,q,t)\), not on the chain ring, unit \(d\), or particular \(A\) in its stated equivalence class.

For instance, for \(R=\mathbf Z/4\mathbf Z\) and \(n=2\), types \((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)\) have respective counts \(64,64,112,4,10,2\); their sum is \(4^4=256\). The two-index type records the full cokernel decomposition, whereas mere invertibility records only type \((0,0)\).

## Assumptions and scope

All rings are finite *commutative* chain rings; no statement is made for arbitrary local or noncommutative rings. A chain ring has a unique ideal of every length, and Smith diagonalization by invertible row and column operations applies. The matrix \(A\) has unit Smith factors of multiplicity \(n-1\) and exactly one zero Smith factor. Arbitrary singular matrices with other nonunit factors are outside the theorem. Matrices \(E,F\) are sampled independently with replacement; the count is of ordered factor pairs rather than distinct perturbed matrices. An arbitrary fixed unit \(d\) can be absorbed in \(E\), preserving uniformity.

## Proof

**Reduction to two entries.** In suitable bases put \(A=\operatorname{diag}(I_m,0)\), \(m=n-1\), and absorb \(d\) in \(E\). Form the bordered matrix

\[H=\begin{pmatrix}I_m&0&u\\0&0&e\\-v&-f&1\end{pmatrix}.\]

Eliminating the bottom-right unit entry produces \(H\sim(A+EF)\oplus I_1\); eliminating the upper-left \(I_m\) instead produces \(H\sim I_m\oplus C\), where \(C=\begin{pmatrix}0&e\\-f&1+vu\end{pmatrix}\). Thus the Smith invariants of \(A+EF\) consist of \(m-1\) unit factors and those of \(C\) (cancellation follows from uniqueness of the Smith multiset). Unit row and column exchanges put \(C\) in the form \(\begin{pmatrix}c&f\\-e&0\end{pmatrix}\) up to irrelevant signs, where \(c=1+vu\).

**Exact two-by-two Smith type.** Put \(\alpha=\nu(c)\), \(\beta=\nu(f)\), \(\gamma=\nu(e)\), \(\delta=\min(\alpha,\beta,\gamma)\). A least-valuation nonzero entry is a unit times \(\pi^\delta\), hence divides every entry. Pivot there by invertible row/column operations. If the pivot lies on the off-diagonal, the remaining diagonal entry is respectively \(f\) or \(e\), giving second valuation \(\gamma\) or \(\beta\), matching \(\min(t,\beta+\gamma-\delta)\). If the pivot is \(c\), elimination leaves a unit multiple of \(\pi^{\beta+\gamma-\delta}\), interpreted as zero if the exponent is at least \(t\). The all-zero case has both valuations \(t\). Thus \(C\) has precisely the two claimed Smith exponents, including every boundary case.

**Distribution.** For a uniformly sampled ring element, \(\Pr(\nu(x)=k)=a_t(k)\), since \(|(\pi^k)|=q^{t-k}\). The pair \((e,f)\) is independent of \((u,v)\). A uniformly sampled vector \(u\in R^m\) is primitive (some coordinate is a unit) with probability \(1-q^{-m}\). Conditional on such a vector, \(v\mapsto vu\) is surjective with all fibers equal, so \(1+vu\) is uniform. Conditional on a nonprimitive \(u\), every coordinate of \(u\) lies in \((\pi)\), hence \(1+vu\) is a unit. Combining these cases yields exactly the masses \(b_{m,t}\), independently of the valuations of \(e,f\). Taking the product distribution of the three valuations and applying the deterministic Smith formula gives the displayed finite sum. The two coordinate changes and multiplication by \(d\) are bijections on the uniform sample space, establishing invariance in \(A,d\). \(\square\)

## Verification

Run the standalone script with `python verify.py`. It independently constructs every ordered factor pair over the test rings \(\mathbf Z/2\mathbf Z\), \(\mathbf Z/4\mathbf Z\), \(\mathbf Z/8\mathbf Z\), \(\mathbf Z/3\mathbf Z\), \(\mathbf Z/9\mathbf Z\), and \(\mathbf Z/5\mathbf Z\), for the stated sizes, reduces each perturbed matrix by elementary row and column operations, and checks the resulting complete Smith-type histogram against the product-mass formula. The finite enumeration is a check of instances, not a proof over arbitrary finite chain rings.

## Relationship to prior work

Johan Öinert, *Invertibility of structured perturbations of singular matrices over unital rings* (arXiv:2610.01948v1, first public October 1, 2026) proves invertibility criteria and inverse formulas for \(A+EDF\), in a much more general ring-theoretic setting, but does not establish a distribution of Smith invariant factors. The present result imposes the narrower corank-one, unit-perturbation, finite-chain-ring setting and obtains the complete *probabilistic Smith profile*, which is not implied by an invertibility test alone.

Wang and Stanley, *The Smith normal form distribution of a random integer matrix* (arXiv:1506.00160, SIAM J. Discrete Math. 2017) treat unrestricted random integer-matrix ensembles; such matrices do not have the structured product law \(A+EF\). Standard nonarchimedean Smith diagonalization provides the normal-form tool, but by itself gives no probabilities for this special ensemble. These implication comparisons do not establish an absolute guarantee of historical novelty.

## Limitations

The distribution concerns one rank-one repair of one matrix with exactly one zero and all other unit Smith factors. It does not address multiple-column perturbations, matrices with initial torsion factors, correlations among distinct \(E,F\), or non-chain finite rings. Different ordered pairs can yield the same perturbation. No independent audit has been performed; potential unpublished or terminologically different prior coverage remains a limitation.

## References

1. Johan Öinert, *Invertibility of structured perturbations of singular matrices over unital rings*, arXiv:2610.01948v1 (October 1, 2026), https://arxiv.org/abs/2610.01948.
2. Yinghui Wang and Richard P. Stanley, *The Smith normal form distribution of a random integer matrix*, SIAM Journal on Discrete Mathematics 31 (2017), 2247–2268, DOI:10.1137/16M1098140; arXiv:1506.00160.
3. *Nonarchimedean integral geometry*, Selecta Mathematica (2026), DOI:10.1007/s00029-025-01120-y; Section 2.2 recalls classical Smith diagonalization.
