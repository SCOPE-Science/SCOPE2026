# Sharp stationary refresh regularization for the Hilbert-cube shift

## Finding
Let \(Q=[0,1]^{\mathbb Z}\) carry the left shift \(\sigma\) and the metric
\[
\rho(x,y)=\sum_{j\in\mathbb Z}2^{-|j|}|x_j-y_j|.
\]
For **every** shift-invariant Borel probability \(\mu\) on \(Q\) and each \(0<\varepsilon\leq1\), let \(X\) have law \(\mu\). Independently choose iid Bernoulli variables \(B_j\) with parameter \(\varepsilon\) and iid uniform variables \(U_j\) on \([0,1]\), and set
\[
Y_j=\begin{cases}X_j,&B_j=0,\\U_j,&B_j=1.\end{cases}\qquad \nu_\varepsilon=\operatorname{Law}(Y).
\]
The following properties hold simultaneously.

1. \(\nu_\varepsilon\) is shift invariant, nonatomic and fully supported. If \(\mu\) is ergodic, weakly mixing or mixing, respectively, then \(\nu_\varepsilon\) has the same respective property.
2. For the stationary-coupling distance
\[
\bar d_1(\mu,\nu)=\inf_{\pi\in J_\sigma(\mu,\nu)}\int|x_0-y_0|\,d\pi(x,y),
\]
where \(J_\sigma\) is the set of shift-invariant joinings, one has
\[
\bar d_1(\mu,\nu_\varepsilon)\leq\varepsilon/2.
\]
This **universal coefficient is exact**, attained when \(\mu\) is the Dirac mass at the constant-zero sequence. Consequently, these fully supported expansive invariant laws converge to every invariant \(\mu\) in \(\bar d_1\), not merely weakly. The same approximation preserves ergodicity when the input is ergodic.
3. Given any \(0<r<1/2\), integer \(N\geq0\) and arbitrary \(z\in Q\), define the coordinate-window cylinder
\[
C_N(z,r)=\{y\in Q:\ |y_j-z_j|\leq r\ \text{for all }-N\leq j\leq N\}.
\]
Then the **sharp distribution-free bound** is
\[
\nu_\varepsilon(C_N(z,r))\leq\bigl(1-\varepsilon(1-2r)\bigr)^{2N+1}.
\]
For every \(r,\varepsilon,N\), equality is attained by \(\mu=\delta_{(1/2)^{\mathbb Z}}\) and \(z=(1/2)^{\mathbb Z}\). In particular, the dynamical ball
\[
\Gamma_r(z)=\{y:\rho(\sigma^kz,\sigma^ky)\leq r\text{ for all }k\in\mathbb Z\}
\]
has \(\nu_\varepsilon\)-measure zero for every \(z\) and **every** \(r<1/2\), with a common radius independent of \(\mu\) and \(\varepsilon\).
4. Every \(\nu_\varepsilon\) has infinite Kolmogorov--Sinai entropy. More quantitatively, for the partition \(\mathcal P_M\) into \(M\geq2\) equal bins according to the zeroth coordinate,
\[
h_{\nu_\varepsilon}(\sigma,\mathcal P_M)\geq H_\varepsilon(M)
= -a_M\log a_M-(M-1)b_M\log b_M,
\quad a_M=1-\varepsilon+\varepsilon/M,\quad b_M=\varepsilon/M.
\]
For fixed \(\varepsilon>0\), \(H_\varepsilon(M)=\varepsilon\log M+O_\varepsilon(1)\) as \(M\to\infty\).

## Assumptions and scope
All probabilities are Borel measures. The original \(\mu\) may be dependent, nonergodic, singular, atomic or of finite entropy; no Markov or product assumption is made. The output coordinates are conditionally independent **given the entire original sequence** but generally dependent without that conditioning. The parameter \(\varepsilon\) is the independent refresh probability, not a perturbation of the shift map. Logarithms in entropy are natural. Every statement includes the endpoint \(\varepsilon=1\); the convergence assertion concerns \(\varepsilon\downarrow0\).

## Proof
**Invariant and recurrent measure classes.** The shift on the triple process \((X,B,U)\) preserves its product law because \(\mu\) is stationary and the other two coordinate processes are iid. The coordinatewise map \((X,B,U)\mapsto Y\) commutes with the shift, proving invariance. An iid Bernoulli process is mixing and hence weakly mixing; its product with an ergodic system is ergodic. It follows that an ergodic input produces an ergodic joint process and therefore an ergodic output factor. Weak mixing and mixing are likewise preserved under products with this Bernoulli noise and passage to factors.

**Full support.** Any nonempty basic open cylinder restricts finitely many coordinates \(j\in F\) to open intervals \(I_j\) of positive Lebesgue length. On the event \(B_j=1\) for all \(j\in F\), those coordinates are independent uniform variables. Therefore
\[
\nu_\varepsilon(\{y:y_j\in I_j\text{ for }j\in F\})\geq \varepsilon^{|F|}\prod_{j\in F}\operatorname{Leb}(I_j)>0.
\]
The nonatomic assertion follows from the all-length bound proved next (or from conditioning on infinitely many refreshes).

**Sharp window bound.** Fix \(z,r,N\) as in the statement. Conditional on \(X\), the refresh noises are independent. Each constraint \(|Y_j-z_j|\leq r\) has conditional probability
\[
(1-\varepsilon){\bf1}_{\{|X_j-z_j|\leq r\}}+\varepsilon\operatorname{Leb}([z_j-r,z_j+r]\cap[0,1])
\leq1-\varepsilon+2r\varepsilon=:q<1.
\]
Multiplying over the \(2N+1\) coordinates and then integrating over \(X\) gives the claimed estimate. If \(\mu\) is concentrated on the all-half sequence and \(z\) equals that sequence, every indicator is one and every interval has length exactly \(2r\). This proves equality for all finite windows; no independence of the coordinates of \(X\) was used.

The coefficient of the zeroth coordinate in \(\rho\) equals one. If \(y\in\Gamma_r(z)\), comparison at shift-time \(j\) gives \(|y_j-z_j|\leq r\). Hence \(\Gamma_r(z)\subseteq C_N(z,r)\) for every \(N\), so
\[
0\leq \nu_\varepsilon(\Gamma_r(z))\leq\inf_{N\geq0}q^{2N+1}=0.
\]
This is measure expansivity, uniformly for every \(0<r<1/2\). The same estimate with \(r=0\) shows singletons have zero \(\nu_\varepsilon\)-measure.

**Sharp stationary coupling cost.** The defining construction is a shift-invariant joining of \(\mu\) and \(\nu_\varepsilon\). Its cost is
\[
\mathbb E|X_0-Y_0|=\varepsilon\mathbb E|X_0-U_0|
=\varepsilon\mathbb E\left[\tfrac12\bigl(X_0^2+(1-X_0)^2\bigr)\right]\leq\varepsilon/2.
\]
For \(\mu=\delta_{0^{\mathbb Z}}\), any joining has its first sequence identically zero; the marginal of \(Y_0\) is \((1-\varepsilon)\delta_0+\varepsilon\operatorname{Leb}\), forcing every joining cost to equal \(\varepsilon/2\). This proves global sharpness. Because the displayed upper bound tends to zero, it proves \(\bar d_1\)-convergence. It also implies weak convergence: a finite-coordinate cylinder-continuous observable is uniformly stable under this coupling, and finite-coordinate continuous observables are uniformly dense in \(C(Q)\).

**Infinite entropy.** Partition \([0,1]\) into \(M\) equal Borel bins, taking the last bin closed at the right endpoint. Let \(Z_j\) denote the bin containing \(Y_j\). Conditional on \(X_j\), the bin of \(X_j\) has probability \(a_M=1-\varepsilon+\varepsilon/M\), and each other bin has probability \(b_M=\varepsilon/M\). Given any finite block of \(X\), the corresponding \(Z_j\) are independent; their conditional Shannon entropies are all exactly \(H_\varepsilon(M)\), independent of the values of \(X_j\). Therefore
\[
H(Z_0,\ldots,Z_{n-1})\geq H(Z_0,\ldots,Z_{n-1}\mid X_0,\ldots,X_{n-1})=nH_\varepsilon(M).
\]
Dividing by \(n\) and taking the stationary entropy-rate limit gives the stated bound. Since \(H_\varepsilon(M)\sim\varepsilon\log M\), the supremum of partition entropy rates is infinite.

## Verification
The proof checks all parameters \(0<\varepsilon\leq1\), \(0<r<1/2\), \(N\geq0\), and all stationary inputs, including boundary-atomic and nonergodic cases. The sharpness examples identify exact extremizers for two different universal bounds. The accompanying `check.py` tests 1,848 exact-rational finite-window and bound instances together with 15 numerical finite-partition entropy diagnostics. Those finite checks do not establish the all-length claim; the conditional-product argument above does. No external mathematical audit has been performed.

## Relationship to prior work
Lacerda's *Typical expansive measures for infinite-dimensional maps* (2026), Theorem A, proves expansivity of iid interval-product measures; its Theorem B establishes density among **all** Borel probabilities using normalization on small sets, without requiring the approximants to be shift invariant. Its Lemma 2.1 supplies the metric-versus-coordinate inclusion used here. The new statement instead regularizes **every stationary input**, including dependent laws, via an explicit stationary joining; it preserves ergodicity and proves sharp \(\bar d_1\) and finite-window estimates with a universal radius.

Arbieto and Morales (2011) prove that ergodic invariant positive-entropy measures are expansive; that qualitative criterion does not give the present common radius, sharp concentration rate, or invariant \(\bar d_1\)-approximation of arbitrary stationary input. Morales (2016) discusses expansive measures with invariant **support**, which is weaker than an invariant measure. Existing product-measure small-ball criteria concern independent coordinates; the refreshed output generally retains dependence through \(X\). The noise-product ergodicity and entropy inequalities are standard tools, not presented as new standalone results.

## Limitations
The density conclusion is for invariant laws in \(\bar d_1\), and within the ergodic (respectively mixing) subclass when the input belongs to that subclass; no claim is made that every output is ergodic for arbitrary nonergodic input. Although \(\bar d_1\) converges to zero, finite metric entropy is never preserved: each positive refresh rate creates infinite entropy. The sharp finite-window bound concerns coordinate cylinders, not an asserted equality for finite-time Bowen balls. Earlier equivalent stationary-channel constructions may exist outside the inspected literature; no priority or independent certification is claimed.

## References
- G. Lacerda, *Typical expansive measures for infinite-dimensional maps*, arXiv:2610.09482v1 (first posted 2026-10-07), especially Theorems A--B, Lemma 2.1 and Section 2.1; https://arxiv.org/html/2610.09482v1.
- A. Arbieto and C. A. Morales, *Expansivity of ergodic measures with positive entropy*, arXiv:1110.5598 (2011); https://arxiv.org/abs/1110.5598.
- C. A. Morales, *On supports of expansive measures*, arXiv:1601.03618 (2016); https://arxiv.org/abs/1601.03618.
- S. L. Carvalho and A. Condori, *On the generic behavior of the metric entropy, and related quantities, of uniformly continuous maps over Polish metric spaces*, Math. Nachr. 296 (2023), 980--995, doi:10.1002/mana.202000312.
