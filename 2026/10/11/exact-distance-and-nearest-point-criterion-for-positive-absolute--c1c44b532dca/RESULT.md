# Exact distance and nearest-point criterion for positive absolutely norm-attaining operators

## Finding

Let \(H\) be any infinite-dimensional complex Hilbert space. A bounded operator \(B:H\to H\) is **absolutely norm-attaining** (abbreviated \(\mathrm{AN}\)) when its restriction to every nonzero closed linear subspace attains its operator norm. Denote by \(\mathcal{AN}_+(H)\) the class of operators which are both positive and absolutely norm-attaining.

**Theorem.** For every bounded positive self-adjoint \(A\), put
\[
m=\min\sigma_{\mathrm{ess}}(A),\qquad M=\max\sigma_{\mathrm{ess}}(A),\qquad
\delta=\frac{M-m}{2},\qquad c=\frac{M+m}{2}.
\]
Then
\[
\inf_{B\in\mathcal{AN}_+(H)}\|A-B\|=\delta.
\]
Moreover, this infimum is achieved **if and only if** the spectral subspace \(E_A([0,m))H\) is finite-dimensional. If it is finite-dimensional, an explicit minimizer is
\[
B_*=A E_A([0,m)) + \bigl(cI+(A-MI)_+\bigr)\bigl(I-E_A([0,m))\bigr).
\]
Here \((A-MI)_+\) is the positive part defined by continuous functional calculus. Both the value and the nearest-point criterion remain valid when \(M=m\), including the case \(m=M=0\).

## Assumptions and scope

The spectrum \(\sigma_{\mathrm{ess}}(A)\) means the spectrum of the image of \(A\) in the Calkin algebra \(\mathcal B(H)/\mathcal K(H)\). It is a nonempty compact subset of \([0,\|A\|]\), and the extrema \(m,M\) exist. The spectral projection \(E_A([0,m))\) is the projection associated with the half-open interval strictly below the smallest essential spectral value; at \(m=0\) it is zero. No separability, compactness, discreteness, or finite-spectrum hypothesis is placed on \(A\). Only **positive** absolutely norm-attaining approximants are considered; no formula for distance to the larger class of arbitrary absolutely norm-attaining operators is asserted.

We use the established characterization of positive absolutely norm-attaining operators: \(B\ge0\) belongs to \(\mathcal{AN}_+(H)\) if and only if there exists \(\beta\ge0\) with \(\sigma_{\mathrm{ess}}(B)=\{\beta\}\) and \(E_B([0,\beta))\) of finite rank. This is the spectral version of \(B=\beta I+K-F\), with \(K\ge0\) compact and \(F\ge0\) finite-rank, supported in orthogonal spectral subspaces. The characterization appears in the works listed in References and is the sole non-elementary imported classification.

## Proof

**1. Universal lower bound.** Write \(\pi\) for the quotient homomorphism to the Calkin algebra. If \(B\in\mathcal{AN}_+(H)\), the spectral characterization supplies a scalar \(\beta\ge0\) for which \(\pi(B)=\beta\pi(I)\). Consequently
\[
\|A-B\|\ge \|\pi(A)-\beta\pi(I)\|
 =\max_{\lambda\in\sigma_{\mathrm{ess}}(A)}|\lambda-\beta|
 =\max\{|m-\beta|,|M-\beta|\}\ge\delta.
\]
The last minimax inequality has the unique minimizing scalar \(\beta=c\), even when \(m=M\).

**2. Approximants arbitrarily close to the bound.** Fix \(\varepsilon>0\). Let \(P_\varepsilon=E_A([0,m-\varepsilon))\), interpreted as zero if the interval is empty. The projection has finite rank: all spectral points strictly separated below \(m\) are isolated finite-multiplicity eigenvalues, with only finitely many in the indicated compact region. Define
\[
B_\varepsilon=A P_\varepsilon+
 \bigl(cI+(A-MI)_+\bigr)(I-P_\varepsilon).
\]
The summands are formed by disjoint spectral functional calculus and hence commute. The operator is positive, and
\[
(B_\varepsilon-cI)_-= (cI-A)P_\varepsilon
\]
is finite-rank, whereas
\[
(B_\varepsilon-cI)_+=(A-MI)_+(I-P_\varepsilon)
\]
is compact because the continuous function \(s\mapsto(s-M)_+\) vanishes on \(\sigma_{\mathrm{ess}}(A)\). Thus \(B_\varepsilon\) is positive absolutely norm-attaining by the cited characterization.

On the spectral interval below \(m-\varepsilon\), the two operators agree. For \(m-\varepsilon\le s\le M\), the new eigenvalue/spectral multiplier is \(c\), so \(|s-c|\le\delta+\varepsilon\). For \(s>M\), it equals \(s-\delta\), with error exactly \(\delta\). Hence
\[
\|A-B_\varepsilon\|\le\delta+\varepsilon.
\]
Together with Step 1, this proves the distance equality.

**3. Sufficiency for attainment.** Suppose \(P=E_A([0,m))\) has finite rank. Repeat Step 2 with \(P\) in place of \(P_\varepsilon\). For \(s\ge m\) the scalar error is at most \(\delta\); below \(m\) the error is zero. The resulting operator is precisely \(B_*\), and its positive and negative parts relative to \(cI\) are respectively compact and finite-rank. Thus \(B_*\in\mathcal{AN}_+(H)\) and \(\|A-B_*\|=\delta\) by Step 1.

**4. Necessity for attainment.** Suppose a positive absolutely norm-attaining \(B\) satisfies \(\|A-B\|\le\delta\). In Step 1 equality forces the unique essential scalar of \(B\) to be \(c\). By the positive \(\mathrm{AN}\) characterization, \(Q=E_B([0,c))\) has finite rank and \(B\ge cI\) on \((I-Q)H\). If \(E_A([0,m))H\) were infinite-dimensional, it would contain a unit vector \(x\) orthogonal to \(QH\). Then
\[
\langle Bx,x\rangle\ge c,
\qquad \langle Ax,x\rangle<m,
\]
because the spectral measure of \(x\) is supported strictly below \(m\). It follows that
\[
\|A-B\|\ge\langle(B-A)x,x\rangle>c-m=\delta,
\]
a contradiction. Hence \(E_A([0,m))\) must have finite rank.

The four steps prove the theorem, including \(\delta=0\): a zero-distance minimizer must equal \(A\), and the criterion reduces exactly to the positive \(\mathrm{AN}\) spectral characterization.

## Verification

All estimates are in operator norm, not a Schatten or strong-operator topology. Step 1 uses the Calkin quotient norm and continuous functional calculus for a self-adjoint element; Steps 2–3 use the vanishing of \((s-M)_+\) on the full essential spectrum, guaranteeing compactness without any eigenvector enumeration; Step 4 uses only finite codimension and a strict spectral-support inequality.

As a sharp illustrative boundary, on \(\ell_2\) let
\[
Ae_{2k-1}=\left(1-\frac1{k+1}\right)e_{2k-1},\qquad
Ae_{2k}=\left(2+\frac1{k+1}\right)e_{2k},\quad k\ge1.
\]
Then \(m=1\), \(M=2\), the distance is \(1/2\), and no nearest positive \(\mathrm{AN}\) operator exists because the entire odd-coordinate space lies below \(1\). Replacing the odd coefficients by \(1+1/(k+1)\) makes the below-\(1\) projection zero; the best-approximant construction then attains distance \(1/2\). Direct finite-prefix numerical checks of these illustrative sequences are optional and are not part of the infinite-dimensional proof.

## Relationship to prior work

Pandey and Paulsen characterize the structure of positive absolutely norm-attaining operators. Doust gives an efficient essential-spectrum and finite-lower-spectrum characterization, including arbitrary Hilbert dimension. Ramesh and Sequeira identify the norm closure of these operators, in particular the singleton-essential-spectrum criterion for positive members of that closure. These statements concern **membership** and **closure**; they do not themselves state the exact distance for an arbitrary positive operator nor the attained-versus-unattained best-approximation dichotomy. The present result combines an essential spectral radius lower bound, explicit asymmetric spectral clipping, and a finite-rank obstruction to exact attainment.

## Limitations

The theorem is restricted to the positive \(\mathrm{AN}\) cone, and does not assert the same formula for nonpositive approximants. No uniqueness of minimizers is asserted. Sources inspected may not exhaust unindexed statements equivalent to the best-approximation criterion. The result is an analytic proof rather than an independently audited or machine-certified theorem.

## References

1. I. Doust, *A note on positive AN operators*, arXiv:1810.08286v1 (first public 18 October 2018), Theorem 2, https://arxiv.org/abs/1810.08286.
2. G. Ramesh and S. S. Sequeira, *On the closure of Absolutely Norm attaining Operators*, arXiv:2204.05912v1 (first public 12 April 2022), Theorems 3.1, 4.1 and 4.5, https://arxiv.org/abs/2204.05912.
3. S. K. Pandey and V. I. Paulsen, *A spectral characterization of AN operators*, Journal of the Australian Mathematical Society 102 (2017), 369–391, Theorem 5.1, https://doi.org/10.1017/S1446788716000239.
