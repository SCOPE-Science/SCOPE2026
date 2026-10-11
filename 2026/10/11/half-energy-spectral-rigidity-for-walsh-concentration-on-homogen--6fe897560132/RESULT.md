# Half-energy spectral rigidity for Walsh concentration on homogeneous halfspaces
## Finding
For every integer \(n\ge1\), every cutoff \(0\le L\le n\), and every real nonzero coefficient vector \(a\in\mathbb R^n\) with no cube vertex on its defining hyperplane, the Walsh-bandlimited concentration operator onto the positive homogeneous halfspace has an exactly determined transition eigenspace. Specifically,
\[
\operatorname{mult}_{C_{a,L}}(1/2)=\binom{n-1}{L},
\]
where \(\binom{n-1}{n}:=0\). All eigenvalues away from \(1/2\) occur in pairs \((\lambda,1-\lambda)\), with equally many above and below \(1/2\). If
\[
m=\min_{x\in\{-1,1\}^n}\left|\sum_{j=1}^n a_jx_j\right|>0,
\qquad M=\sum_{j=1}^n|a_j|,
\]
then every noncentral eigenvalue also satisfies the quantitative gap
\[
|\lambda-1/2|\ge\frac{m}{2M}.
\]
Thus the transition eigenspace dimension is independent of the halfspace's orientation and individual weights; the explicit margin controls how close any other concentration eigenvalue can approach the transition.

## Assumptions and scope
Equip \(X=\{-1,1\}^n\) with normalized counting measure. For \(S\subseteq\{1,\ldots,n\}\), let \(w_S(x)=\prod_{i\in S}x_i\), with \(w_\varnothing=1\). Define \(V_L=\operatorname{span}\{w_S:|S|\le L\}\) and let \(P_L\) be orthogonal projection onto \(V_L\). The positive halfspace is \(H_a=\{x\in X:\ell_a(x)>0\}\), where \(\ell_a(x)=\sum_i a_ix_i\) is *homogeneous*. The no-tie assumption \(\ell_a(x)\ne0\) for all \(x\) is essential; in particular it implies \(H_a\) and \(-H_a\) partition \(X\). The concentration operator is \(C_{a,L}=P_LM_{1_{H_a}}P_L|_{V_L}\). Its dimension is \(D=\sum_{j=0}^{L}\binom nj\), and its spectrum lies in \([0,1]\). At \(L=0\) the noncentral spectral-gap statement is vacuous. At \(L=n\), \(C_{a,n}\) is multiplication by the halfspace indicator, so its only eigenvalues are zero and one.

## Proof
Let \(\sigma(x)=\operatorname{sgn}\ell_a(x)\). Since \(\ell_a(-x)=-\ell_a(x)\) and no ties occur, \(\sigma(-x)=-\sigma(x)\) and \(1_{H_a}=(1+\sigma)/2\). Define \(T=2C_{a,L}-I_{V_L}=P_LM_\sigma P_L|_{V_L}\).

Split \(V_L=E_L\oplus O_L\) into the spans of even and odd Walsh degrees. Multiplication by the odd function \(\sigma\) sends each parity into the opposite parity before projection, so \(T\) has the self-adjoint block form \(\left(\begin{smallmatrix}0&B\\B^*&0\end{smallmatrix}\right)\). The binomial alternating-sum identity gives
\[
\dim E_L-\dim O_L=\sum_{j=0}^L(-1)^j\binom nj=(-1)^L\binom{n-1}{L}.
\]
Consequently, if \(W\) is the smaller of the two parity spaces and \(U\) the larger, then every Walsh monomial of \(W\) has degree at most \(L-1\), and \(\dim U-\dim W=\binom{n-1}{L}\). If \(L=0\), then \(W=\{0\}\), and the asserted spectral multiplicity follows directly. Assume the smaller space is nonzero.

For every nonzero \(g\in W\), multiplying by the linear Walsh polynomial \(\ell_a\) switches parity and increases Walsh degree by at most one. Thus \(\ell_ag\in U\subseteq V_L\). With the usual complex \(L^2\) inner product,
\[
\langle\ell_ag,Tg\rangle=\langle\ell_ag,\sigma g\rangle
=\mathbb E_X[|\ell_a|\,|g|^2]\ge m\|g\|_2^2.
\]
Cauchy--Schwarz and \(\|\ell_ag\|_2\le M\|g\|_2\) therefore give
\[
\|Tg\|_2\ge\frac{m}{M}\|g\|_2,
\qquad g\in W.
\]
In other words, the rectangular off-diagonal block mapping \(W\) into \(U\) is injective, and its least singular value is at least \(m/M\). The nonzero spectrum of the self-adjoint parity-off-diagonal operator \(T\) consists of pairs of opposite singular values. Its kernel has dimension exactly \(\dim U-\dim W=\binom{n-1}{L}\). Applying \(C_{a,L}=(I+T)/2\) establishes the exact half-energy multiplicity, the number and pairing of noncentral eigenvalues, and the lower gap \(m/(2M)\). This argument uses neither a numerically estimated rank nor any asymptotic approximation.

## Verification
The complete standalone, standard-library script `verify.py` independently constructs the Walsh matrix of the threshold sign for multiple no-tie integer coefficient families. It checks odd parity of the Fourier expansion, exact parity dimension differences, full rank of the relevant rectangular matrix over a finite field, and the integer quadratic-form inequalities underlying the margin argument. Execute `python verify.py`; the tested version prints `VERIFY_OK exact_cutoff_cases=443 dimensions=1..7 rank_mod_prime=1000003 parity_and_margin=checked`. These finite examples are corroborative; the preceding proof covers every integer \(n\ge1\), every cutoff and every real weight vector satisfying the no-tie condition.

## Relationship to prior work
Nayar [1] develops Walsh--Fourier level decompositions and linear/Boolean approximation on the cube, but does not examine spatial Slepian concentration or its eigenvalue \(1/2\). Hogan and Lakey [2,3] study Boolean-hypercube time--band limiting with spectral low-pass projection and spatial localization by **Hamming balls**. Their eigenanalysis and multiplicities concern such radially symmetric sets, often with matching ball radius and Fourier cutoff. The present result uses an arbitrary strict homogeneous *weighted halfspace*, not a Hamming ball of arbitrary radius, and gives a weight-independent exact central multiplicity together with a margin-dependent spectral gap. In particular, the analysis does not follow from merely renaming their binomial-difference eigenspace multiplicities.

## Limitations
The theorem does not cover hyperplanes passing through a cube vertex, biased product measures, translated affine halfspaces with nonzero threshold, spatial sets without antipodal complementarity, or arbitrary non-low-pass spectral masks. It gives no closed formulas for individual off-center eigenvalues and does not claim that the gap bound is universally optimal. A possible earlier expression of the parity full-rank principle under linear-threshold or truncated-multiplication terminology remains an originality risk. These mathematical limitations do not weaken the exact statements under the stated hypotheses.

## References
[1] P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1, first public 13 November 2013; *Colloquium Mathematicum* **137** (2014), 253–261, doi:10.4064/cm137-2-9. Primary MSC 42C10.

[2] J. A. Hogan and J. D. Lakey, *An Analogue of Slepian Vectors on Boolean Hypercubes*, *Journal of Fourier Analysis and Applications* **25** (2019), 2004–2020, doi:10.1007/s00041-018-09654-w. The full 17-page paper was examined, including its Hamming-ball localization and appendices.

[3] J. A. Hogan and J. D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1, 21 December 2018; the introduction and spectral-block construction, including Corollary 9, concern spatial Hamming balls.
