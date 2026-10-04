# Block-weight phase diagram for the qutrit Holevo–MLD separation
## Finding
For the qutrit estimation model of Yamaguchi and Tajima, the strict separation between the Holevo bound and the maximum-logarithmic-derivative (MLD) bound persists for every positive-definite weight that respects the natural \((\theta_1,\theta_2)\mid\theta_3\) block decomposition. More precisely, write
\[
\rho=\operatorname{diag}(p,q,q),\qquad p>q>0,\qquad p+2q=1,
\]
\[
r=\frac{p-q}{p+q}\in(0,1),\qquad \kappa=\frac{4(p-q)^2}{p+q},
\]
and choose
\[
G=\kappa\begin{pmatrix}a&c&0\\c&b&0\\0&0&h\end{pmatrix},\qquad a>0,\ b>0,\ h>0,\ D=ab-c^2>0.
\]
With \(s=\sqrt D\),
\[
C^{\mathrm H}(G)=a+b+h+2rs,
\]
while
\[
C^{\mathrm{MLD}}(G)=
\begin{cases}
a+b+h+2rs-hr^2,&s\ge hr,\\
a+b+h+s^2/h,&s<hr.
\end{cases}
\]
Hence
\[
C^{\mathrm H}(G)-C^{\mathrm{MLD}}(G)=
\begin{cases}
hr^2,&s\ge hr,\\
2rs-s^2/h,&s<hr,
\end{cases}
\]
is strictly positive throughout this cone. The maximizing single-family parameter changes regime at \(s=hr\): for \(s\ge hr\) the MLD supremum is obtained as \(\beta\to1^-\), whereas for \(s<hr\) it is attained at \(\beta_*=s/(hr)\).

## Assumptions and scope
The generators are exactly those in arXiv:2609.31601v1:
\[
H_1=|0\rangle\langle1|+|1\rangle\langle0|,\qquad
H_2=-i|0\rangle\langle1|+i|1\rangle\langle0|,
\]
\[
H_3=|0\rangle\langle2|+|2\rangle\langle0|,
\]
with the local unitary model \(\rho_\theta=e^{-i\sum_j\theta_jH_j}\rho e^{i\sum_j\theta_jH_j}\) evaluated at \(\theta=0\). The finding concerns the asymptotic Holevo cost and the MLD scalar lower bound for the displayed positive-definite block-compatible weights. It does not claim a formula for weights with nonzero \((1,3)\) or \((2,3)\) entries, nor does it claim finite-copy attainability of every feasible covariance matrix.

## Proof
The source computes, for \(\beta\in[0,1)\),
\[
(\mathcal F^\beta_\rho)^{-1}=\frac1\kappa
\begin{pmatrix}
1&-i\beta r&0\\
i\beta r&1&0\\
0&0&1-\beta^2r^2
\end{pmatrix}.
\]
Let
\[
W=\begin{pmatrix}a&c\\c&b\end{pmatrix}>0,\qquad D=\det W,
\]
and write the upper-left block of \(\kappa V-I_2\) as a real symmetric matrix \(X\). The upper-left principal constraint in \(V\ge(\mathcal F^\beta_\rho)^{-1}\) is
\[
X+\begin{pmatrix}0&i\beta r\\-i\beta r&0\end{pmatrix}\ge0.
\]
For a real symmetric \(2\times2\) matrix, this implies \(X\ge0\) and
\[
\det X\ge \beta^2r^2.
\]
Conversely these two conditions are sufficient for this Hermitian \(2\times2\) block. For any \(X\ge0\),
\[
\operatorname{Tr}(WX)\ge2\sqrt{\det(WX)}=2\sqrt{D\det X},
\]
so the weighted contribution of the first block is at least \(2\beta r\sqrt D\). Equality is attained by
\[
X_\beta=\beta r\sqrt D\,W^{-1},
\]
for which \(\det X_\beta=\beta^2r^2\) and \(\operatorname{Tr}(WX_\beta)=2\beta r\sqrt D\). The third principal constraint is \(\kappa V_{33}\ge1-\beta^2r^2\), and it can be attained simultaneously by taking the cross-block entries to be zero. Therefore the exact fixed-\(\beta\) scalar bound is
\[
C^{(\beta)}(G)=a+b+h+2\beta r\sqrt D-h\beta^2r^2.
\]
This concave quadratic has derivative \(2r(\sqrt D-hr\beta)\). Hence its supremum over \([0,1)\) is the stated piecewise MLD formula, with the stated optimizer regime.

For the Holevo bound, the 2026 characterization requires one real symmetric \(V\) to satisfy the matrix inequality for every \(\beta\in[0,1)\). Taking \(\beta\to1^-\) in the first block gives \(\det X\ge r^2\), while \(\beta=0\) gives \(\kappa V_{33}\ge1\). Thus every jointly feasible matrix obeys
\[
\operatorname{Tr}(GV)\ge a+b+2r\sqrt D+h.
\]
The bound is attained by taking cross-block entries zero,
\[
X_*=r\sqrt D\,W^{-1},\qquad \kappa V_{33}=1.
\]
Indeed \(\det X_*=r^2\), so the upper-left Hermitian difference has determinant \(r^2(1-\beta^2)\ge0\) for every \(\beta\in[0,1)\), and the third diagonal difference is \(\beta^2r^2\ge0\). This proves the Holevo formula. Subtracting the MLD expression gives the displayed gap. In the interior branch, \(s<hr\) implies \(2rs-s^2/h=s(2hr-s)/h>0\); in the RLD branch, \(hr^2>0\).

## Verification
The proof is analytic. The accompanying `verify.py` independently checks the determinant identities, the exact weighted-trace equality of the constructed minimizers, the piecewise maximization, and joint feasibility on deterministic parameter choices and a dense \(\beta\)-grid. Running `python3 verify.py` from the package directory prints `VERIFY_OK`.

## Relationship to prior work
Yamaguchi and Tajima prove that the Holevo feasible region is the intersection of the complete \(\beta\)-LD QFI family and introduce the three-parameter qutrit witness used here. For that witness they evaluate only the isotropic choice \(G=\kappa I_3\), obtaining \(C^{\mathrm H}=3+2r\), \(C^{\mathrm{MLD}}=3+2r-r^2\), and gap \(r^2\). Their text explicitly explains the competition between the first two directions and the third direction but does not give the block-weight phase diagram above.

Yamagata introduced the MLD construction and gave explicit solutions for a broader structural class; therefore the fixed-family maximization used here should be viewed as a specialization of that framework rather than as a new general MLD theorem. Niu and Yu established weight-independent Holevo descriptions for two-parameter qubit models. Those results do not cover this three-parameter qutrit separation. The new content here is the exact cone-wide block-weight evaluation and the strict-gap/optimizer classification for the 2026 qutrit witness.

## Limitations
The result is confined to block-compatible weights. A fully general real positive-definite \(3\times3\) weight can couple \(\theta_3\) to the first two parameters, and the present proof does not optimize that case. The result also does not identify a finite-copy measurement attaining the displayed Holevo value; it uses the asymptotic Holevo framework of the source. Searches did not find an equivalent block-weight formula, but absence from the inspected literature is not a proof that no equivalent derivation exists under different notation.

## References
1. K. Yamaguchi and H. Tajima, “Exact Characterization of the Holevo Bound by a Quantum Fisher Information Family,” arXiv:2609.31601v1, first submitted 2026-09-25.
2. K. Yamagata, “Maximum logarithmic derivative bound on quantum state estimation as a dual of the Holevo bound,” Journal of Mathematical Physics 62, 062203 (2021), arXiv:2106.06294v1.
3. C. Niu and S. Yu, “Holevo bound independent of weight matrices for estimating two parameters of a qubit,” Chinese Physics B 33, 020304 (2024), DOI 10.1088/1674-1056/ad117d.
