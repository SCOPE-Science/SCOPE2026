# Sharp codimension-two Gram-determinant bound for equal-weight unit decompositions

## Finding
For integers \(n\ge2\) and \(m=n+2\), let \(u_1,\ldots,u_m\in\mathbb R^n\) have unit norm and satisfy
\[
\frac{n}{m}\sum_{i=1}^{m}u_i u_i^{\mathsf T}=I_n.
\]
For each \(n\)-element set \(B\subseteq\{1,\ldots,m\}\), write \(c_B=\det(\langle u_i,u_j\rangle)_{i,j\in B}\). Then
\[
\boxed{\max_{|B|=n}c_B\ge \frac{3m^{n-2}}{n^n}.}
\]
The constant is achieved if and only if \(m\) is divisible by three. All equality configurations are classified by their two-dimensional Naimark complements: after an orthogonal change of coordinates, the normalized complementary rows lie on exactly three unoriented lines at successive angles \(\pi/3\), each with multiplicity \(m/3\). Arbitrary row signs and relabellings leave the classification unchanged. At every fixed \(m\) not divisible by three the strict inequality has a positive, though here unevaluated, uniform gap.

For \(m=6\), \(n=4\), the sharp squared-volume guarantee is \(27/64\), compared with the general Cauchy--Binet guarantee \(27/80\). For every divisible \(m\), the improvement factor is \(3(m-1)/(2m)\).

## Assumptions and scope
All spaces and frames are real. Vectors remain *labelled*, so distinct indices may correspond to identical directions. Unit norm and the equal positive weight \(n/m\) are required; this result does not concern all weighted decompositions. Gram determinants are nonnegative and equal the squares of corresponding parallelotope volumes, without a factorial normalization. The statements quantify over every integer \(n\ge2\), hence \(m=n+2\ge4\).

## Proof
**1. Exact complementary-minor reduction.** Put the \(u_i^{\mathsf T}\) in the rows of a matrix \(U\in\mathbb R^{m\times n}\) and let \(Q=\sqrt{n/m}\,U\). Then \(Q^{\mathsf T}Q=I_n\). Choose \(W\in\mathbb R^{m\times 2}\) with orthonormal columns so that \([Q\ W]\) is an orthogonal \(m\times m\) matrix. The orthogonal projector identity gives each row of \(W\) squared norm
\[
\|W_{i,*}\|^2=1-\|Q_{i,*}\|^2=1-\frac nm=\frac2m.
\]
For every \(n\)-set \(B\), Jacobi's complementary-minor identity for the orthogonal matrix yields \(|\det Q_B|=|\det W_{B^c}|\). Row rescaling therefore gives
\[
 c_B=\left(\frac mn\right)^n\det(W_{B^c})^2.
\]
This equality is valid for every such frame and every \(B\), including singular submatrices.

**2. An exact planar circle statement.** Write the complementary rows as \(W_{i,*}=\sqrt{2/m}(\cos\theta_i,\sin\theta_i)\). Column orthonormality is precisely the pair of conditions \(\sum_i\cos(2\theta_i)=\sum_i\sin(2\theta_i)=0\); thus the complex unit points \(z_i=e^{2\mathrm i\theta_i}\) satisfy \(\sum_i z_i=0\). In particular \(0\) is in their convex hull.

There must be a pair satisfying \(|z_i-z_j|^2\ge3\). Indeed, planar Carathéodory gives at most three of these points whose convex hull contains zero. A two-point witness is an antipodal pair, with squared distance four. Otherwise take three points in cyclic order. Each of their three consecutive circular gaps is at most \(\pi\), since otherwise the three vertices would lie in an open semicircle and their convex hull would omit zero. The gaps sum to \(2\pi\), so one is at least \(2\pi/3\) and the corresponding squared chord length is at least three.

Moreover, if \(\max_{i,j}|z_i-z_j|^2=3\), every zero-containing triple must have all its gaps exactly \(2\pi/3\), hence it comprises a rotated copy of the cubic roots of unity. Any further unit point outside those three positions makes squared chord distance greater than three with one of those roots: on each open intervening arc, its shortest angular separation from the opposite root lies strictly between \(2\pi/3\) and \(\pi\), except at the arc midpoint where it is \(\pi\). Hence all \(z_i\) lie at the three root positions. The equality \(\sum_i z_i=0\) then forces equal multiplicities, because its real and imaginary components imply the three nonnegative integer counts coincide.

**3. Convert the circle estimate to determinant volume.** The relation between phase chords and rows is
\[
\det(W_{\{i,j\}})^2=\frac{4}{m^2}\sin^2(\theta_i-\theta_j)=\frac{|z_i-z_j|^2}{m^2}.
\]
Taking the largest complementary pair in step 1 gives
\[
\max_{|B|=n}c_B=\frac{m^{n-2}}{n^n}\max_{i<j}|z_i-z_j|^2\ge\frac{3m^{n-2}}{n^n}.
\]
Equality is possible only for three equally occupied root positions, so only when \(3\mid m\).

**4. Exact attainment and strictness.** If \(m=3k\), repeat each of the planar unit directions \((1,0)\), \((1/2,\sqrt3/2)\), and \((-1/2,\sqrt3/2)\) exactly \(k\) times and scale every row by \(\sqrt{2/m}\). Their rank-two frame operator is the identity because the sum of their three outer products is \((3/2)I_2\). Complete these two columns to an orthogonal matrix, use its other \(n\) columns as \(Q\), and put \(U=\sqrt{m/n}\,Q\). Every row of \(U\) then has norm one and attains the bound. Conversely the equality reasoning in steps 2 and 3 classifies every extremizer.

If \(m\) is not divisible by three, none can attain equality. The set of admissible labelled unit frames is compact (it is a closed subset of a finite product of unit spheres) and is nonempty: the equally spaced projective directions \(\theta_j=\pi j/m\) give a planar equal-norm Parseval complement. Since the continuous maximum \(\max_B c_B\) attains its minimum, that minimum is strictly larger than the displayed bound for each such \(m\).

## Verification
The standalone script `check_exact.py` forms the rational Gram matrices of the three-direction extremizers for \(m=6,9,12\). It checks diagonal normalization, enumerates *every* size-\(n\) principal Gram determinant using exact rational elimination, verifies the sharp formula, and checks the improvement over the Cauchy--Binet constant. Run with `python3 check_exact.py` from this directory. Its success marker is `EQUAL_LEVERAGE_CODIMENSION_TWO_EXACT_CHECKS_OK`.

These finite symbolic checks validate explicit model configurations only. The universal lower bound, equality classification and strict gap for other sizes follow from the analytic proof above, not from any finite enumeration.

## Relationship to prior work
Zhang's arXiv:2610.10979v1 (Sections 2--4) formulates the largest full-size Gram determinant problem for labelled unit decompositions with **arbitrary** nonnegative weights. Its Cauchy--Binet lower bound for \(m=n+2\) is
\[
L_{m,n}=\frac{m^n}{n^n\binom{m}{n}}.
\]
Our proved equal-weight guarantee divided by \(L_{m,n}\) is exactly \(3(m-1)/(2m)>1\) for \(m\ge4\). That source also uses Jacobi's complementary-minor identity in a stochastic calculation; the new ingredient is the sharp deterministic planar diameter bound under equal complementary row norms and its rigidity.

Fodor--Naszódi--Zarnócz (arXiv:1804.03444v2, Theorem 2) prove a general selected-volume lower bound of Cauchy--Binet strength. Their reduction to at most three weighted directions when \(n=2\) already gives the numerical coefficient \(3/4\) in this one low-dimensional case; the all-dimension equal-weight theorem and sharp equality classification are different conclusions. Ivanov (arXiv:1804.10055v3) develops exterior-algebra/projection-frame identities and extremal *total* zonotope-volume questions; those inspected results do not assert the maximum-principal-minor inequality and its three-direction equality classification. These distinctions rely on the specific proved statements, not merely on differing titles.

## Limitations
The theorem assumes real equal-weight unit decompositions and exactly two excess labels. It neither improves the unrestricted-weight result nor determines the actual minimum for \(m\not\equiv0\pmod3\). Only the divisible-by-three subsequence is proved exactly optimal. No independent scientific audit has been performed. Although published-source and semantic-index comparisons found no identical finite-codimension bound, equivalent older results on tight-frame determinants or spherical diameters may have escaped discovery.

## References
1. H. Zhang, *Sharp Minimax Gram-Determinant Asymptotics for Labelled Unit Decompositions of the Identity*, arXiv:2610.10979v1 (first publicly posted 2026-10-07), https://arxiv.org/abs/2610.10979.
2. F. Fodor, M. Naszódi and T. Zarnócz, *On the Volume Bound in the Dvoretzky--Rogers Lemma*, arXiv:1804.03444v2, https://arxiv.org/abs/1804.03444.
3. G. Ivanov, *Tight Frames and Related Geometric Problems*, arXiv:1804.10055v3, https://arxiv.org/abs/1804.10055.
