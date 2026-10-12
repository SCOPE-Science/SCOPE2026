# A sharp full-rank transition for average mixing on Johnson triple graphs

## Finding
Let \(n\) be an integer with \(n\ge6\). In the Johnson graph \(J(n,3)\), the vertices are the three-element subsets of \(\{1,\ldots,n\}\); two distinct vertices are adjacent precisely when their intersection has size two. Let \(A\) be the unweighted real adjacency matrix and define
\[
\widehat M(n)=\lim_{T\to\infty}\frac1T\int_0^T\big(e^{itA}\circ e^{-itA}\big)\,dt,
\]
where \(\circ\) denotes entrywise multiplication. Then
\[
\operatorname{rank}\widehat M(n)=
\begin{cases}
10,&n=6,\\
\binom n3,&n\ge7.
\end{cases}
\]
Moreover, for every \(n\ge7\), the entrywise square of the spectral projector \(E_3\) corresponding to the lowest adjacency eigenvalue \(-3\) is *itself* positive definite, and hence \(\widehat M(n)\) is strictly positive definite.

The exact four eigenvalues of \(K(n):=E_3\circ E_3\), indexed by Johnson eigenspaces \(j=0,1,2,3\), are
\[
\begin{aligned}
\lambda_0&=\frac{n-5}{n-2},\\
\lambda_1&=\frac{(n-6)(n-5)}{(n-4)(n-3)},\\
\lambda_2&=\frac{(n-5)(n^3-14n^2+63n-86)}{(n-4)^2(n-3)^2},\\
\lambda_3&=\frac{(n-6)(n^3-13n^2+56n-74)}{(n-4)^2(n-3)(n-2)}.
\end{aligned}
\]
Each indexed eigenvalue has multiplicity \(m_j=\binom nj-\binom n{j-1}\), with \(\binom n{-1}=0\); equal eigenvalues have their multiplicities added. For \(n\ge7\),
\[
\lambda_0>\lambda_1\ge\lambda_2>\lambda_3>0,
\qquad
\lambda_{\min}(\widehat M(n))\ge\lambda_3.
\]
For \(n=6\), the eigenvalues of \(K(6)\) are \((1/4,0,1/9,0)\) with indexed multiplicities \((1,5,9,5)\); its rank and the rank of \(\widehat M(6)\) are exactly \(10\).

## Assumptions and scope
All assertions concern the *ordinary infinite-time Cesàro* mixing matrix for the real, unweighted adjacency Hamiltonian \(A\), and arbitrary integers \(n\ge6\). The case \(n=6\) is the antipodal boundary; \(n\ge7\) supplies primitive distance-regular diameter-three Johnson graphs. These statements do not address instantaneous uniform mixing, arbitrary time-sampling distributions, Johnson graphs on four or more elements per vertex, or the general primitive distance-regular rank problem.

The spectral projectors \(E_j\), for \(j=0,1,2,3\), are the orthogonal projectors of \(A\) for its four distinct eigenvalues
\[
\theta_j=(3-j)(n-3-j)-j.
\]
Every \(E_j\) is positive semidefinite. Thus the Schur-product theorem implies each \(E_j\circ E_j\) is positive semidefinite and the standard spectral expansion implies \(\widehat M=\sum_{j=0}^3 E_j\circ E_j\).

## Proof
**Step 1: Johnson distance algebra and the lowest projector.** Write \(A_d\) for the distance-\(d\) adjacency matrix, \(d=0,1,2,3\), so \(A_0=I\) and \(A_1=A\). For vertices \(S,T\), graph distance is \(d=3-|S\cap T|\). The Johnson intersection parameters are
\[
 b_d=(3-d)(n-3-d),\quad c_d=d^2,\quad a_d=3(n-3)-b_d-c_d.
\]
Consequently, for any matrix \(F=\sum_{d=0}^3 f_d A_d\), the coefficient of \(A_d\) in \(AF\) is \(c_df_{d-1}+a_df_d+b_df_{d+1}\), with out-of-range terms omitted. Using \(\theta_3=-3\) and the diagonal projector entry \(f_0=m_3/\binom n3=(n-5)/(n-2)\), solve \(AF=-3F\) successively. This gives
\[
(f_0,f_1,f_2,f_3)=\left(
\frac{n-5}{n-2},
-\frac{n-5}{(n-3)(n-2)},
\frac{2(n-5)}{(n-4)(n-3)(n-2)},
-\frac6{(n-4)(n-3)(n-2)}
\right).
\]
The final \(d=3\) recurrence also holds. Since the distance algebra is simultaneously diagonalizable with the adjacency matrix, the unique matrix in this algebra satisfying \(AF=-3F\) is a scalar multiple of \(E_3\). Here \(\operatorname{tr}F=\binom n3 f_0=m_3\); therefore \(F=E_3\). Equivalently, \((E_3)_{ST}=f_{3-|S\cap T|}\).

**Step 2: The four eigenvalues of the Schur square.** Define \(P_j(d)\) as the eigenvalue of \(A_d\) on the \(\theta_j\)-eigenspace. The distance recurrence
\[
\theta_j P_j(d)=b_{d-1}P_j(d-1)+a_dP_j(d)+c_{d+1}P_j(d+1),
\quad P_j(0)=1,\quad P_j(1)=\theta_j
\]
produces the following exact rows (each row lists \(d=0,1,2,3\)):
\[
\begin{aligned}
P_0&=\big(1,\ 3(n-3),\ 3(n-4)(n-3)/2,\ (n-5)(n-4)(n-3)/6\big),\\
P_1&=\big(1,\ 2n-9,\ (n-9)(n-4)/2,\ -(n-5)(n-4)/2\big),\\
P_2&=\big(1,\ n-7,\ 11-2n,\ n-5\big),\\
P_3&=\big(1,\ -3,\ 3,\ -1\big).
\end{aligned}
\]
Since \(K=E_3\circ E_3=\sum_{d=0}^3f_d^2A_d\), its eigenvalues are exactly \(\lambda_j=\sum_{d=0}^3f_d^2P_j(d)\), which simplify to the four displayed rational functions. The multiplicities are the standard Johnson eigenmodule dimensions \(m_j=\binom nj-\binom n{j-1}\). The symbolic equalities and the spectral projection formula are independently reproduced by the embedded checker.

**Step 3: Strict positivity for all \(n\ge7\).** Set \(h=n-7\ge0\). The two cubic numerators in \(\lambda_2\) and \(\lambda_3\) become, respectively,
\[
h^3+7h^2+14h+12,\qquad h^3+8h^2+21h+24,
\]
both strictly positive. To give the *least* eigenvalue, compute the successive exact gaps:
\[
\begin{aligned}
\lambda_0-\lambda_1&=\frac{n(n-5)}{(n-4)(n-3)(n-2)},\\
\lambda_1-\lambda_2&=\frac{(n-7)(n-5)(n-2)}{(n-4)^2(n-3)^2},\\
\lambda_2-\lambda_3&=\frac{n^3-16n^2+81n-118}{(n-4)(n-3)^2(n-2)}.
\end{aligned}
\]
The last numerator equals \(h^3+5h^2+4h+8>0\). Thus \(K\succ0\) and its least eigenvalue is \(\lambda_3>0\). Since \(\widehat M-K=\sum_{j=0}^2 E_j\circ E_j\succeq0\), the claimed positive definiteness, exact full rank, and quantitative lower bound follow.

**Step 4: The sharp boundary \(n=6\).** Here every triple \(S\) has a unique disjoint triple \(S^c\). The corresponding complement permutation is the distance-three matrix \(C=A_3\). The distance eigenvalue rows at \(n=6\) have \(P_j(3)=(-1)^j\), so \(CE_j=(-1)^jE_j\). Rows of each \(E_j\) indexed by \(S\) and \(S^c\) differ by a sign; their entrywise squares are therefore identical. It follows that the \(20\times20\) matrix \(\widehat M(6)\) has at most \(10\) distinct rows, so rank at most \(10\). From the four formulas, the positive eigenvalues of \(K(6)\) are \(\lambda_0=1/4\) and \(\lambda_2=1/9\), with respective multiplicities \(1\) and \(9\). Hence \(\operatorname{rank}K(6)=10\). As \(\widehat M(6)\succeq K(6)\), its rank is at least \(10\), proving the exact boundary rank.

## Verification
Run `python verify.py` with the SymPy version identified by `requirements.txt`. The program symbolically verifies all four projector-distance coefficients, all four Schur-square eigenvalue rational functions, the three positivity polynomial expansions and the exact eigenvalue gap identities. Independently of the distance algebra, it forms the adjacency matrices and the lowest spectral projector by the degree-three Lagrange polynomial in \(A\) for \(n=6,7,8\), checking the projector identity, trace, eigenvalue equation, and all \(4,761\) exact rational projector entries. It also constructs **all** four spectral projectors on \(J(6,3)\) and checks the exact rank \(10\) of their Schur-square sum. The checks cover finite matrices; the theorem for arbitrary \(n\) is proved by the symbolic identities plus the inequalities above, not by finite sampling.

## Relationship to prior work
The standard identity \(\widehat M=\sum_jE_j\circ E_j\) and the general exact treatment of average mixing are established, particularly by Godsil (2011), Coutinho–Godsil–Guo–Zhan (2017), and Coutinho–Baptista–Godsil–Spier–Werner (2022). Coutinho and Guo (2024, Open Problem 4.1) ask about full rank on **all primitive distance-regular graphs**. The present argument addresses only the diameter-three Johnson triple family, independently of the known diameter-two strongly regular cases.

Burcroff (2017, Theorem 1.1/Corollary 7.5) establishes the complete spectrum of **any** matrix in the Johnson adjacency algebra. That strong general theorem is compatible with and implies an algorithm for computing the eigenvalues above after the specific \(E_3\)-square coefficients have been determined; the present contribution is **not** a new general Johnson eigenvalue formula. Its specialized claim is the sharp \(n=6\)/\(n\ge7\) full-rank classification for quantum average mixing, with an explicit positive Schur-square witness and strict lower bound. Standard nonnegativity of Krein parameters alone does not provide the strict inequalities needed here. A pre-existing stronger positivity characterization or implicit corollary could cover this claim and remains a literature risk.

## Limitations
This is a conventional long-time average, not a finite-time state-transfer or uniform-mixing theorem. The inequality is a lower bound on the least eigenvalue of \(\widehat M\), not an asserted formula for its full spectrum. No classification for Johnson graphs on larger fixed subset sizes is proved. Full rank of \(\widehat M\) for general primitive distance-regular graphs remains unresolved by this result. Earlier general spectral formulas are acknowledged; novelty depends on the previously unreported strict-positivity specialization, with possible equivalent Krein-parameter coverage remaining to be ruled out by wider literature inspection. Independent review has not been performed.

## References
- C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, 2011, https://arxiv.org/abs/1103.2578.
- G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, 2017, https://arxiv.org/abs/1709.03591.
- G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1, first public 2022-08-18, https://arxiv.org/abs/2208.08971.
- G. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236v1, 2024, Section 4, Open Problem 4.1, https://arxiv.org/abs/2404.02236.
- A. Burcroff, *Johnson Schemes and Certain Matrices with Integral Eigenvalues*, 2017, Theorem 1.1 and Corollary 7.5, https://math.uchicago.edu/~may/REU2017/REUPapers/Burcroff.pdf.
- C. Godsil, *Association Schemes*, University of Waterloo notes, Section 2.4 on Krein parameters, https://www.math.uwaterloo.ca/~cgodsil/pdfs/assoc2.pdf.
