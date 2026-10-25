# Unbounded Euclidean transients and a weighted stability law for partitioned Rosenbrock–exponential integration

## Finding

The second-order PartRosExp2 method applied to a linear split with symmetric dissipative parts has an exact Cayley–exponential similarity: its physical step matrix \(M\) is similar to a product of two Euclidean contractions. This guarantees power stability in an explicit weighted norm, with strict spectral stability exactly when the two generators have no common null vector. Yet the ordinary one-step Euclidean amplification is **unbounded** as the stiffness of the implicitly treated matrix grows—even while the total physical generator remains strictly dissipative and the step is spectrally stable. The companion method with the operator order reversed has a bound independent of that implicit stiffness when the exponentially treated part is fixed.

The contribution is the joint noncommuting matrix-level classification, explicit unbounded endpoint witness, and contrast between the two published second-order operator orderings. Neither scalar A-stability nor the generic fact that similarity can distort norms is being claimed as new.

## Assumptions and scope

Fix any dimension \(d\ge1\), step size \(h>0\), and **real symmetric negative-semidefinite** matrices \(A,B\in\mathbb R^{d\times d}\). The equation is \(y'(t)=(A+B)y(t)\); matrix exponentials and linear solves are interpreted exactly. Put
\[
X=hA,\quad Y=hB,\quad L=I-X/2,\quad C=L^{-1}(I+X/2),\quad E=e^Y.
\]
Then \(L\) is symmetric positive definite. Define the entire matrix function \(\varphi_1(Y)=\int_0^1 e^{sY}\,ds\), so the identity \(\varphi_1(Y)Y=E-I\) holds even when \(Y\) is singular. By *PartRosExp2* and *PartExpRos2* we mean the **published** coefficient and scheme expressions in Table 1 of Dallerit et al. (2023, published online; 2024 volume). Their preprint Table 1 is not used to disambiguate the final PartRosExp2 formula; see Relationship to prior work.

Define the weighted vector norm \(\|v\|_L=\|Lv\|_2\) and induced operator norm \(\|T\|_L=\|LTL^{-1}\|_2\). The spectral radius is \(\rho(T)\). Statements about unbounded Euclidean amplification concern a family of different split matrices; each individual step matrix has a finite norm.

## Proof

**1. Exact formula and weighted power bound.** On this linear split the PartRosExp2 update gives
\[
M=I+L^{-1}\left(\tfrac12(E+I)X+\varphi_1(Y)Y\right).
\]
Multiply by \(L\) on the left and use \(\varphi_1(Y)Y=E-I\):
\[
LM=L+\tfrac12(E+I)X+E-I
   =E(I+X/2).
\]
Because \(X\) and \(L\) commute, this is the **noncommutative** factorization
\[
M=L^{-1}E(I+X/2)=L^{-1}(EC)L.
\]
Every eigenvalue \(x\le0\) of \(X\) is sent by the Cayley transform to \((1+x/2)/(1-x/2)\in[-1,1]\) (strict modulus below one when \(x<0\)); hence \(\|C\|_2\le1\). Since \(Y\preceq0\), \(\|E\|_2\le1\). Thus for each integer \(k\ge0\),
\[
\|M^k\|_L=\|(EC)^k\|_2\le1,
\qquad
\|M^k\|_2\le\kappa_2(L).
\]
These conclusions do **not** assume that \(A\) and \(B\) commute.

**2. Exact strict spectral stability criterion.** A Euclidean unit vector attains \(\|Cv\|_2=\|v\|_2\) exactly when \(v\in\ker A\), because all negative eigenvalues of \(X\) produce Cayley moduli strictly below one. Similarly, \(\|Ew\|_2=\|w\|_2\) exactly when \(w\in\ker B\). Equality in the chain
\[
\|ECv\|_2\le\|Cv\|_2\le\|v\|_2
\]
therefore holds for a nonzero \(v\) exactly when \(v\in\ker A\cap\ker B\). In finite dimensions the operator norm is attained, so \(\|EC\|_2<1\) exactly when this intersection is trivial. If it is nontrivial, every vector in the intersection satisfies \(ECv=v\). Since \(M\) is similar to \(EC\),
\[
\rho(M)<1\quad\Longleftrightarrow\quad
\ker A\cap\ker B=\{0\}
\quad\Longleftrightarrow\quad A+B\prec0.
\]
Otherwise the spectral radius is exactly one.

**3. A strictly dissipative two-dimensional family with unbounded endpoint gain.** Set \(h=1\) and, for every real \(t>0\),
\[
A_t=\begin{pmatrix}-t&0\\0&0\end{pmatrix},\quad
B=-\frac{\log2}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
E=e^B=\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix}.
\]
Each part is symmetric negative semidefinite. Their kernels are transverse, so \(A_t+B\prec0\), and part 2 proves \(\rho(M_t)<1\) for every finite \(t>0\). The exact first-stage similarity yields
\[
M_t=\begin{pmatrix}
\frac34\frac{1-t/2}{1+t/2}&-\frac{1}{4(1+t/2)}\\
-\frac14(1-t/2)&\frac34
\end{pmatrix}.
\]
Dividing by \(t\) and taking the entrywise limit shows
\[
\lim_{t\to\infty}\frac{M_t}{t}
=\begin{pmatrix}0&0\\1/8&0\end{pmatrix},
\qquad
\boxed{\lim_{t\to\infty}\frac{\|M_t\|_2}{t}=\frac18}.
\]
The determinant tends to \(-1/2\), the trace to zero; hence the two eigenvalues tend to \(\pm 1/\sqrt2\). In particular the unbounded gain is **not** attributable to spectral instability. At the exact stiffness \(t=16\),
\[
M_{16}=\begin{pmatrix}-7/12&-1/36\\7/4&3/4\end{pmatrix},\qquad
\|M_{16}e_1\|_2^2=245/72>1,
\]
while its eigenvalues are \((1\pm\sqrt{57})/12\), both strictly inside the unit disk.

**4. Reversal bounds the same stiffness direction.** The published reverse-order PartExpRos2 update is
\[
N=I+\frac{E+I}{2}\,L^{-1}X+\varphi_1(Y)L^{-1}Y.
\]
By symmetric dissipativity, \(\|L^{-1}\|_2\le1\), \(\|L^{-1}X\|_2\le2\), \(\|(E+I)/2\|_2\le1\), and \(\|\varphi_1(Y)\|_2\le1\). Therefore
\[
\boxed{\|N\|_2\le1+2+\|Y\|_2=3+h\|B\|_2}.
\]
For fixed \(B\) and \(h\) the bound is uniform over **all** symmetric negative-semidefinite implicit matrices \(A\), in sharp contrast with the preceding PartRosExp2 family. The bound does not assert that the reverse map is a contraction.

## Verification

The accompanying file `verify_rosexp.py` performs exact SymPy derivations of the two-dimensional witness, its eigenvalues and asymptotic limit, plus 450 reproducible random symmetric-dissipative identity and spectral checks using NumPy. It also checks the reverse-order bound on a stiffness sequence. Execute `python verify_rosexp.py` with Python 3 and `sympy` and `numpy` installed. The proof above, rather than the finite random and stiffness tests, certifies the universally quantified statements. The only transcendental evaluation required by the witness is the exact identity \(e^{-(\log2)vv^{\mathsf T}/2}\) for \(v=(1,1)^{\mathsf T}\), whose eigenvalues are \(1\) and \(1/2\).

## Relationship to prior work

Dallerit, Buvoli, Tokman and Gaudreault introduced both operator orderings and analyze scalar partitioned A-stability by assuming simultaneous diagonalizability (published Article, §3 Table 1 and §4). The published Table 1 is the definitive definition of PartRosExp2 used here; the earlier June 2023 preprint's displayed Table 1 has a different PartRosExp2 row. Neither version develops this noncommuting similarity, exact kernel criterion, stiffness-uniform reverse-order bound, or an unbounded **endpoint** norm witness. The published paper already recognizes that operator order affects numerical performance, so the general importance of ordering is prior art.

Achleitner, Arnold and Mehrmann (2023) study hypocontractivity and matrix/numerical-range distinctions for dissipative flows. Their general concepts explain why similarity-transformed contractivity need not be Euclidean contractivity, but their work does not state the specific PartRosExp2/PartExpRos2 comparison or the explicit fixed-exponential-part family shown here. Generic Cayley contractions, matrix exponential contractions and similarity norm inequalities are standard tools, not claimed contributions.

## Limitations

Real, finite-dimensional symmetric negative-semidefinite split generators; exact exponential and rational operations; one fixed step; linear autonomous systems. No claim is made for nonsymmetric generators, approximate exponential actions, nonlinear problems, steps with changing matrices, PDE limits, or physical/numerical convergence error bounds. Spectral stability is strict for each fixed member of the witness family but is not asserted uniformly for arbitrary families. The reversed ordering is proved uniformly **bounded**, not necessarily energy contracting or spectrally stable. The particular similarity and witness may be independently derivable from more general product/splitting theory; this remains a publication-priority risk.

## References

1. V. Dallerit, T. Buvoli, M. Tokman, and S. Gaudreault, “Second-order Rosenbrock-exponential (ROSEXP) methods for partitioned differential equations,” *Numerical Algorithms* **96**, 1143–1161 (2024), first online 2023-11-10, DOI `10.1007/s11075-023-01698-4`; earlier public preprint posted 2023-06-29, DOI `10.21203/rs.3.rs-3101972/v1`. Use the final published Table 1 coefficients.
2. F. Achleitner, A. Arnold, and V. Mehrmann, “Hypocoercivity and hypocontractivity concepts for linear dynamical systems,” *Electronic Journal of Linear Algebra* (2023), DOI `10.13001/ela.2023.7531`.
