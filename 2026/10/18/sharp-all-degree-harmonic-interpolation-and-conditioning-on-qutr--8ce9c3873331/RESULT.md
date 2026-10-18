# Sharp all-degree harmonic interpolation and conditioning on qutrit mutually unbiased bases

## Finding
Let \(X\subset\mathbb{CP}^{2}\) consist of the twelve lines from **any** four mutually unbiased orthonormal bases of \(\mathbb C^3\). For an integer \(q\ge0\), let \(E_q\) evaluate the phase-invariant complex spherical harmonics \(\mathcal H_{q,q}(\mathbb C^3)\) at these twelve lines, with the source norm from probability-normalized measure on the unit sphere. Write \(G_q=E_qE_q^*\) for the twelve-by-twelve sampling Gram matrix.

Let \(P_q^{(1,0)}\) denote the classical Jacobi polynomial, normalized by \(P_q^{(1,0)}(1)=q+1\), and put
\[
a_q=\frac{(-1)^q}{q+1},\qquad b_q=\frac{P_q^{(1,0)}(-1/3)}{q+1}.
\]
For every integer \(q\ge0\), the complete eigenvalue list of \(G_q/(q+1)^3\) is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1-a_q&8\\
1+2a_q-3b_q&3\\
1+2a_q+9b_q&1.
\end{array}
\]
Consequently,
\[
\operatorname{rank}E_q=\begin{cases}1&q=0,\\8&q=1,\\11&q=2,\\12&q\ge3.\end{cases}
\]
At degree \(q=0\) the attainable data are the constant vectors. At \(q=1\) the attainable data are exactly the vectors whose entries sum to zero **separately in each of the four bases**. At \(q=2\) only the global sum must be zero. At every degree \(q\ge3\), arbitrary complex data can be interpolated.

More strongly, the **globally sharp uniform spectral bounds** for every \(q\ge3\) are
\[
\boxed{\frac{2}{27}(q+1)^3 I_{12}\preceq G_q\preceq\frac{28}{15}(q+1)^3 I_{12}.}
\]
The lower equality occurs only in degree \(q=5\), on the globally constant-data mode; the upper equality occurs only in degree \(q=4\), on the same mode. Moreover, the **globally sharp spectral condition number**, across all invertible individual degrees and every choice of four mutually unbiased bases, is
\[
\boxed{\sup_{q\ge3}\kappa_2(G_q)=\frac{63}{4},}
\]
with equality **only at \(q=5\)**. At that degree the three normalized eigenvalues are \(7/6,70/81,2/27\) (multiplicities \(8,3,1\), respectively). Thus the evaluation operator has worst nonzero singular-value condition number \(3\sqrt7/2\). The exact optimal reconstruction of admissible data \(y\) is
\[
f_y(z)=\sum_{j=1}^{12}(G_q^+y)_j\,K_q(z,v_j),\qquad \|f_y\|_2^2=y^*G_q^+y,
\]
where \(G_q^+\) is the Moore–Penrose inverse, \(v_j\) is any unit representative of the corresponding line, and \(K_q\) is the reproducing kernel described below. The reconstruction is unique among minimum-norm interpolants.

## Assumptions and scope
Mutual unbiasedness means \(|\langle u,v\rangle|^2=1/3\) whenever \(u,v\) belong to different bases; distinct vectors in a common basis are orthogonal. Each vector is unit norm, and the twelve lines are distinct. Complex spherical harmonics of bidegree \((q,q)\) are the restrictions to the unit sphere \(S^5\subset\mathbb C^3\) of polynomials homogeneous of degree \(q\) in the complex coordinates and degree \(q\) in their conjugates, annihilated by the complex Euclidean Laplacian. All such functions are invariant under multiplying their argument by a unit complex phase, so the evaluation on projective lines is well defined. The source inner product is the \(L^2\) product of the unique \(U(3)\)-invariant probability measure on \(S^5\); the target uses counting-measure \(\ell^2\) on the twelve lines. Changing the target by a common positive weight does not alter ranks or condition numbers.

The statement concerns *one exact bidegree at a time*, not the sum of all degrees up to a cutoff. It concerns linear interpolation of complex values, not quantum-state tomography from intensities.

## Proof
**Reproducing kernel.** By the addition theorem for complex spherical harmonics, the dimension is
\[
d_q=\binom{q+2}{2}^2-\binom{q+1}{2}^2=(q+1)^3,
\]
and the probability-normalized reproducing kernel is
\[
K_q(z,w)=d_q\,\frac{P_q^{(1,0)}(2|\langle z,w\rangle|^2-1)}{q+1}.
\]
In particular \(K_q(z,z)=d_q\), including at \(q=0\). The three possible squared overlaps among sampled lines are \(1\), \(0\), and \(1/3\), giving normalized kernel entries \(1\), \(a_q\), and \(b_q\), respectively. The Jacobi endpoint formula gives \(a_q=(-1)^q/(q+1)\).

**Exact three-sector diagonalization.** Order the twelve sampled lines by their four bases. Let \(I\) be the identity, let \(T\) be the block diagonal matrix with four blocks \(J_3\), and let \(J\) be the twelve-by-twelve all-ones matrix. Then
\[
G_q/d_q=(1-a_q)I+(a_q-b_q)T+b_qJ.
\]
The mutually orthogonal projectors
\[
\Pi_8=I-T/3,\qquad \Pi_3=T/3-J/12,\qquad \Pi_1=J/12
\]
have ranks \(8,3,1\). They project, respectively, onto within-basis contrasts, onto vectors constant within each basis with the four constants summing to zero, and onto globally constant vectors. Substitution gives exactly the three eigenvalues claimed. Positivity and interpolation constraints follow by identifying the positive eigenspaces.

**Low degrees.** The exact pairs \((a_q,b_q)\) at \(q=0,1,2\) are \((1,1)\), \((-1/2,0)\), and \((1/3,-5/27)\). Thus the spectra are, respectively, \((0,0,12)\), \((3/2,0,0)\), and \((2/3,20/9,0)\), with sector multiplicities as stated. This gives ranks \(1,8,11\) and precisely the advertised data constraints.

**Finite part of the sharp stability bound.** The elementary Christoffel identity gives
\[
P_q^{(1,0)}(x)=\frac{P_q(x)-P_{q+1}(x)}{1-x},
\]
where \(P_q\) on the right is the usual Legendre polynomial. In particular,
\[
b_q=\frac{3}{4(q+1)}\bigl(P_q(-1/3)-P_{q+1}(-1/3)\bigr).
\]
Starting with \(P_0=1\), \(P_1(x)=x\), use the exact rational recurrence
\[
(q+1)P_{q+1}(x)=(2q+1)xP_q(x)-qP_{q-1}(x).
\]
The following table is reproducible using these three formulas; the middle column is the minimum normalized Gram eigenvalue, and the final column is the exact condition number. All entries in the middle column are strictly positive.

| \(q\) | Minimum eigenvalue of \(G_q/d_q\) | \(\kappa_2(G_q)\) |
|---:|---:|---:|
| 3 | \(5/18\) | \(9/2\) |
| 4 | \(4/5\) | \(7/3\) |
| 5 | \(2/27\) | \(63/4\) |
| 6 | \(6/7\) | \(124/81\) |
| 7 | \(203/324\) | \(729/406\) |
| 8 | \(8/9\) | \(3190/2187\) |
| 9 | \(7228/10935\) | \(24057/14456\) |
| 10 | \(10/11\) | \(1144/729\) |
| 11 | \(94075/118098\) | \(255879/188150\) |
| 12 | \(12/13\) | \(696710/531441\) |
| 13 | \(1009346/1240029\) | \(2657205/2018692\) |
| 14 | \(14/15\) | \(75412/59049\) |
| 15 | \(1039661/1417176\) | \(3011499/2079322\) |
| 16 | \(16/17\) | \(869497/708588\) |

The minimum spectral value in this exact finite table is \(2/27\) (degree five), and the maximum is \(28/15\) (degree four), each uniquely attained. The maximum condition number is \(63/4\), attained only at \(q=5\). The attached standalone checker verifies the rational arithmetic, the three projectors, the eigenvalue identities, and a twelve-point mutually unbiased construction without floating point.

**Infinite tail.** For every \(n\ge0\) and \(x\in[-1,1]\), \(|P_n(x)|\le1\). For instance, Laplace's integral representation \(P_n(\cos\theta)=\pi^{-1}\int_0^\pi(\cos\theta+i\sin\theta\cos\phi)^n\,d\phi\) makes the bound immediate. Therefore
\[
|a_q|=\frac1{q+1},\qquad |b_q|\le\frac{3}{2(q+1)}.
\]
Every one of the three normalized Gram eigenvalues then lies in
\[
\left[1-\frac{31}{2(q+1)},\;1+\frac{31}{2(q+1)}\right].
\]
For all \(q\ge17\), this interval is strictly positive, and monotonicity of its endpoint ratio gives
\[
\kappa_2(G_q)\le\frac{1+31/36}{1-31/36}=\frac{67}{5}<\frac{63}{4}.
\]
Also \(1-31/36=5/36>2/27\) and \(1+31/36=67/36<28/15\), so the same tail estimate proves the two sharp degree-uniform normalized Gram bounds. Together with the finite table this establishes full interpolation at all \(q\ge3\), the two sharp uniform spectral endpoints, the sharp uniform condition number, and their unique equality degrees. Finally, the reproducing-kernel representer theorem (or the elementary orthogonal projection onto the kernel span) yields the stated minimum-norm formula, also for rank-deficient degrees via the pseudoinverse. \(\square\)

## Verification
Run `python3 check.py` using only Python's standard library. It computes all Legendre/Jacobi values as exact rational fractions, verifies the four projective bases using arithmetic in \(\mathbb Q(\omega)\) for \(\omega^3=1\), checks the three spectral projectors as twelve-by-twelve rational matrices, and tests every finite entry in the displayed table. The generated `exact_table.json` records the complete three-eigenvalue data for degrees \(3\) through \(16\). The analytic Legendre bound, explicitly proved above, covers all larger degrees; neither finite numerical tests nor a program timeout is used as an infinite proof.

## Relationship to prior work
Klappenecker–Rötteler construct complete finite-field mutually unbiased bases and identify their relation to projective two-designs. Roy–Scott study two-designs arising from bases and optimal first-order quantum-state determination. Roy–Suda give the complex harmonic reproducing kernels and their Jacobi representation. Those results supply the geometric and harmonic foundations; the displayed exact all-bidegree three-sector spectrum, the two successive interpolation constraints, the two sharp global frame endpoints, and the unique sharp worst-degree stability constant \(63/4\) are the specific conclusions established here. In particular, first-order projective two-design tightness neither supplies nor rules out the pronounced near-singularity at bidegree \((5,5)\). This statement does not claim new construction of MUBs or new addition theorems.

## Limitations
The analysis applies to complete families of four mutually unbiased bases in complex dimension three, with unweighted individual-degree evaluations and probability-normalized harmonic kernels. It does not characterize incomplete or weighted families, noisy nonlinear phase retrieval, or higher ambient dimensions. The result has been checked internally using exact arithmetic and mathematical reconstruction; no independent mathematical audit or publication-priority certification has been performed. A 1975 paper by Delsarte–Goethals–Seidel supplies earlier projective Jacobi machinery, but a full-text comparison with that paper was not available. Consequently, an implicitly equivalent earlier association-scheme treatment cannot be ruled out solely by the source inspection performed here.

## References
1. A. Klappenecker and M. Rötteler, *Constructions of Mutually Unbiased Bases*, arXiv:quant-ph/0309120, publicly posted 15 September 2003. https://arxiv.org/abs/quant-ph/0309120
2. A. Klappenecker and M. Rötteler, *Mutually Unbiased Bases are Complex Projective 2-Designs*, arXiv:quant-ph/0502031, publicly posted 4 February 2005. https://arxiv.org/abs/quant-ph/0502031
3. A. Roy and A. J. Scott, *Weighted complex projective 2-designs from bases: optimal state determination by orthogonal measurements*, arXiv:quant-ph/0703025, 2007. https://arxiv.org/abs/quant-ph/0703025
4. A. Roy and S. Suda, *Complex spherical designs and codes*, arXiv:1104.4692, publicly posted 25 April 2011. https://arxiv.org/abs/1104.4692
5. P. Delsarte, J. M. Goethals and J. J. Seidel, *Bounds for systems of lines, and Jacobi polynomials*, Philips Research Reports 30 (1975), 91–105. Bibliographic listing: https://research.tue.nl/en/publications/bounds-for-systems-of-lines-and-jacobi-polynomials/
