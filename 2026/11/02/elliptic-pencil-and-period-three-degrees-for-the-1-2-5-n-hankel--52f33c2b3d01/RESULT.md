# Elliptic pencil and period-three degrees for the \(\{1,2,5,n\}\) Hankel projections

## Finding
For each integer \(n\ge6\), the projection of the complex rank-at-most-two Hankel variety \(H_{2,n}\subset\mathbb A^n\) onto observations at indices \(\{1,2,5,n\}\) is generically finite of degree
\[
\deg\pi_{\{1,2,5,n\}}=\begin{cases}
2n-7,& n\equiv2\pmod3,\\
2n-6,& n\not\equiv2\pmod3.
\end{cases}
\]
Before the final observation, the generic curve of completions has genus one. On its smooth compactification the last observation has exactly two poles; the periodic drop of one at one pole accounts for the residue-three dependence. These are exact formulas for every \(n\ge6\), not extrapolations from finite computations.

## Assumptions and scope
Work over \(\mathbb C\). Write the ordered Hankel moments as \((x_1,\ldots,x_n)\); the determinantal equations are all \(3\times3\) minors of the \(3\times(n-2)\) Hankel matrix. On the dense open rank-two locus a sequence \((a_0,\ldots,a_{n-1})\), with \(a_j=x_{j+1}/x_1\), satisfies a unique second-order recurrence
\[a_{j+2}=Sa_{j+1}-Pa_j,\qquad a_0=1,\quad a_1=b=x_2/x_1.\]
Uniqueness holds where \(a_2-b^2\ne0\); the recurrence parameters are rational functions of four consecutive moments. The use of \(x_1=1\) is a normalization on \(x_1\ne0\), and does not restrict the generic field-extension degree. Fix \(a_4=c=x_5/x_1\). Assume \(b\ne0\), \(c\ne0\), \(c\ne b^4\); these conditions describe a nonempty Zariski-open set of the three-observation base. All degree claims are generic, and multiplicities are counted over \(\mathbb C\).

## Proof
**1. The genus-one intermediate fiber.** The recurrence gives
\[a_2=bS-P,\qquad a_3=bS^2-P(S+b),\qquad a_4=bS^3-P(S^2+2bS)+P^2.\]
Thus the fixed-three-observation fiber has affine model
\[F(S,P)=P^2-(S^2+2bS)P+bS^3-c=0.\]
Putting \(Y=2P-S^2-2bS\) yields
\[Y^2=S^4+4b^2S^2+4c.\]
Its derivative in \(S\) is \(4S(S^2+2b^2)\), so the quartic has four distinct roots when \(c(c-b^4)\ne0\). The smooth projective completion is therefore a genus-one double cover of \(\mathbb P^1_S\), with two distinct points \(Q_+\) and \(Q_-\) over infinity. The affine curve is irreducible. The recurrence parametrization is birational to the generic three-observation slice of \(H_{2,n}\), since whenever \(a_2-b^2\ne0\) one recovers
\[S=(a_3-ba_2)/(a_2-b^2),\qquad P=bS-a_2.\]

**2. Expansion at the two infinite points.** Choose the square-root branches so that \(Y\sim+S^2\) at \(Q_+\) and \(Y\sim-S^2\) at \(Q_-\). With \(S^{-1}\) as local parameter, the exact defining equation gives
\[\begin{aligned}
P\big|_{Q_+}&=S^2+bS+b^2+O(S^{-2}),\\
P\big|_{Q_-}&=bS-b^2+O(S^{-2}).
\end{aligned}\]
Consequently
\[a_3|_{Q_+}=-S^3+O(S^2),\qquad a_5|_{Q_+}=S^5+O(S^4),\]
and
\[a_3|_{Q_-}=b^3+O(S^{-1}),\qquad a_5|_{Q_-}=(c-b^4)S+O(1).\]
The second leading coefficient is nonzero by hypothesis.

**3. Uniform pole orders.** For \(k\ge0\), introduce the Lucas-type recurrence polynomials \(H_0=0\), \(H_1=1\), and \(H_{k+1}=SH_k-PH_{k-1}\). Repeated application of the recurrence gives, for \(k\ge1\),
\[a_{4+k}=H_k(S,P)a_5-PH_{k-1}(S,P)c.\]
Weighted homogeneity yields \(H_k(S,P)=S^{k-1}h_k(P/S^2)\), with \(h_0=0\), \(h_1=1\) and \(h_{k+1}=h_k-zh_{k-1}\). At \(z=1\), the values of \(h_k(1)\) repeat \(0,1,1,0,-1,-1\), so they vanish exactly when \(3\mid k\). For \(k=3m\), the root formula \(h_k(z)=(\alpha^k-\beta^k)/(\alpha-\beta)\), where \(\alpha+\beta=1\) and \(\alpha\beta=z\), gives
\[h_{3m}(z)=(1-z)\sum_{j=0}^{m-1}\alpha^{3(m-1-j)}\beta^{3j}.\]
Since at \(z=1\) both cubed roots equal \(-1\), we obtain \(h'_{3m}(1)=(-1)^m m\ne0\). Along \(Q_+\), \(P/S^2=1+b/S+O(S^{-2})\). Therefore \(H_k\) has a pole of order \(k-1\) when \(3\nmid k\) and \(k-2\) when \(3\mid k\), with nonzero leading coefficient in both cases because \(b\ne0\). The term \(PH_{k-1}c\) has pole order at most \(k\), strictly below the pole order \(k+4\) or \(k+3\) of \(H_ka_5\). Hence
\[\operatorname{ord}_{Q_+}(a_{4+k})=\begin{cases}-(k+4),&3\nmid k,\\-(k+3),&3\mid k.\end{cases}\]
At \(Q_-\), we have \(P/S^2\to0\) and \(h_k(0)=1\). Hence \(H_k\sim S^{k-1}\), the leading term of \(H_ka_5\) is \((c-b^4)S^k\), and \(PH_{k-1}c=O(S^{k-1})\). Thus \(\operatorname{ord}_{Q_-}(a_{4+k})=-k\) for every \(k\ge1\).

**4. Generic degree.** Each \(a_j\) is polynomial in \(S,P\), hence regular at every finite point of the smooth affine curve; these are the only poles of \(a_{4+k}\). Over characteristic zero the nonconstant function \(a_{4+k}:E_{b,c}\to\mathbb P^1\) is finite and separable, and its degree is the sum of its polar orders. Therefore
\[\deg(a_{4+k})=\begin{cases}2k+3,&3\mid k,\\2k+4,&3\nmid k.\end{cases}\]
Taking \(k=n-5\), the condition \(3\mid k\) is exactly \(n\equiv2\pmod3\). Since the original rank-two Hankel slice is birational to the recurrence-parameter curve, this equals \([\mathbb C(H_{2,n}):\mathbb C(x_1,x_2,x_5,x_n)]\) and proves the theorem.

## Verification
The standalone `verify.py` uses SymPy with exact integer/rational coefficients, not floating-point arithmetic. It checks the quadratic relation against the recurrence, tests squarefreeness of the quartic for two nonexceptional parameter specializations, and computes exact elimination resultants in \(P\) for \(6\le n\le12\). Their degrees in \(S\), and their generic squarefreeness in the final coordinate, agree with the theorem. These checks are finite corroboration; the proof of the uniform statement is the valuation argument above. Execute `python verify.py` with SymPy installed.

## Relationship to prior work
Reed and Tsakiris, *On Hankel Determinantal Matroids* (arXiv:2610.27554, first public version 2026-10-20), prove uniformity of the Hankel algebraic matroid and bound degrees of coordinate projections. Their Theorem 5 gives, for the present pattern, the upper bound \(3\max\{3,n-5\}\); Remark 7 tabulates other patterns with third observed index \(4\) and \(6\), but no all-\(n\) degree for third index \(5\). The theorem here replaces that bound with the exact periodic degree and exhibits a genus-one intermediate fiber. Classical decimated Prony literature, for example Batenkov (arXiv:1308.0753), primarily studies stability under arithmetic-progression samples and does not give this non-arithmetic four-observation enumerative degree. Related exact degree formulas for other coordinate patterns neither imply this statement nor share its genus-one mechanism. These comparisons are qualified literature checks, not a claim to conclusive priority.

## Limitations
Only the complex generic projection degree for rank at most two and the specified coordinate pattern is determined. Exceptional fibers, scheme-theoretic multiplicity at special observations, real completion counts, higher Hankel rank, and general missing-data patterns are not classified. Algebraic and literature checks are not independent mathematical certification; a broader unlocated formula in older sparse Prony or secant-variety literature remains a potential priority risk.

## References
1. Ethan Reed and Manolis C. Tsakiris, *On Hankel Determinantal Matroids*, arXiv:2610.27554v1 (2026-10-20), Theorem 1, Theorem 5, Remark 7, and §5.3. https://arxiv.org/pdf/2610.27554
2. Dmitry Batenkov, *Decimated generalized Prony systems*, arXiv:1308.0753v1 (2013), Introduction, main stability results and Discussion. https://arxiv.org/pdf/1308.0753
