# Sharp \(L^2\)-to-\(L^4\) extension and nonuniform extremizers on the finite-field cubic graph

## Finding
Let \(q=p^n\), with \(p>3\) prime, and let \(\psi\) be any nontrivial additive character of \(\mathbb F_q\). For any function \(f:\mathbb F_q\to\mathbb C\), define
\[
\mathcal E_q f(X,Y)=\frac1q\sum_{t\in\mathbb F_q}f(t)\psi(Xt+Yt^3),\qquad (X,Y)\in\mathbb F_q^2.
\]
The sharp counting-measure inequality is
\[
\boxed{\sum_{X,Y\in\mathbb F_q}|\mathcal E_qf(X,Y)|^4\leq\frac{3(2q-1)}{2q+1}\left(\frac1q\sum_{t\in\mathbb F_q}|f(t)|^2\right)^2.}
\]
All nonzero equality cases, and no others, are given by the following complete family. Choose one representative \(t\) from each pair \(\{t,-t\}\subset\mathbb F_q^\times\), choose arbitrary angles \(\theta_t\in\mathbb R\), and choose \(\lambda\in\mathbb C^\times\). Then
\[
f(0)=\sqrt{\frac32}\,\lambda,\qquad f(t)=\lambda e^{i\theta_t},\qquad f(-t)=\lambda e^{-i\theta_t}.
\]
Conversely every such function attains equality. Modulo a common nonzero complex scalar, the nonzero extremizers form a torus of real dimension \((q-1)/2\). In particular, every extremizer has squared amplitude at the origin exactly \(3/2\) times its squared amplitude at any nonzero point. Constant inputs are never extremizers.

## Assumptions and scope
The characteristic restriction \(p>3\) is essential for the two-sum rigidity used below. Field cardinality \(q\) may be a nonprime prime power. The formula is for the graph \(\{(t,t^3):t\in\mathbb F_q\}\), with normalized input counting measure \(q^{-1}\) and unnormalized output counting measure on \(\mathbb F_q^2\); neither normalization may be interchanged. The zero input also gives equality but is not included among nonzero extremizers.

## Proof
**Step 1: determine every two-sum fiber.** Write \(\Phi(t)=(t,t^3)\). If \(u+v=s\ne0\), then
\[
u^3+v^3=s^3-3suv.
\]
Because \(3s\ne0\), the sum \(\Phi(u)+\Phi(v)\) determines \(uv\). Its unordered pair \(\{u,v\}\) is therefore uniquely determined as the root multiset of \(T^2-sT+uv\). If the first coordinate of the sum is zero, the second is automatically zero and the pairs are exactly \(\{t,-t\}\), together with the diagonal pair \(\{0,0\}\). Hence every nonzero target has one unordered preimage pair, while the zero target is the only collision fiber.

**Step 2: exact convolution identity.** Put \(M=\sum_t|f(t)|^2\), \(a=f(0)\), and select \(m=(q-1)/2\) representatives \(t_j\) for the opposite pairs. Set \(P_j=f(t_j)f(-t_j)\) and \(R=\sum_t|f(t)|^4\). Orthogonality of additive characters yields
\[
q^2\sum_{X,Y}|\mathcal E_q f(X,Y)|^4
=\sum_{(s,v)\in\mathbb F_q^2}\left|\sum_{u+w=s,\,u^3+w^3=v}f(u)f(w)\right|^2.
\]
All nonzero fibers are diagonal singletons or two permutations of a distinct pair. Summing their squares, and treating the zero fiber separately, gives the *exact* identity
\[
\mathscr T(f)=2M^2-R-|a|^4-4\sum_{j=1}^m|P_j|^2+\left|a^2+2\sum_{j=1}^mP_j\right|^2,
\]
where \(\mathscr T(f)\) denotes the convolution sum on the preceding right-hand side.

**Step 3: sharp amplitude bound.** Define \(x=|a|^2\), \(b_j=|f(t_j)|^2+|f(-t_j)|^2\), and \(r_j=2|P_j|\). Then \(0\le r_j\le b_j\), \(M=x+\sum_jb_j\), and \(R=x^2+\sum_j(b_j^2-r_j^2/2)\). The triangle inequality therefore gives
\[
\mathscr T(f)\le2M^2-2x^2-\sum_jb_j^2-\frac12\sum_jr_j^2+\left(x+\sum_jr_j\right)^2.
\]
The last two terms form a function nondecreasing in each \(r_j\ge0\), because its partial derivative is \(2x+2\sum_kr_k-r_j\ge0\). Its maximum over \(0\le r_j\le b_j\) occurs at every \(r_j=b_j\). When \(M>0\), equality here forces \(r_j=b_j\) for every positive \(b_j\). Consequently,
\[
\mathscr T(f)\le3M^2-2x^2-\frac32\sum_jb_j^2.
\]
Weighted Cauchy--Schwarz now gives
\[
M^2=\left(x+\sum_jb_j\right)^2\le\left(\frac12+\frac{2m}{3}\right)\left(2x^2+\frac32\sum_jb_j^2\right),
\]
so
\[
\mathscr T(f)\le\left(3-\frac6{3+4m}\right)M^2=\frac{3(2q-1)}{2q+1}M^2.
\]
Dividing by \(q^2\) gives the claimed extension inequality.

**Step 4: every equality case.** If \(f\ne0\), equality in weighted Cauchy--Schwarz requires \(4x=3b_j\) for *all* \(j\), hence all \(b_j>0\). Equality in the preceding monotonicity requires \(r_j=b_j\), which is equivalent to \(|f(t_j)|=|f(-t_j)|\). Thus \(b_j\) is independent of \(j\); write the common nonzero coefficient magnitude as \(|\lambda|\). We obtain \(|a|^2=3|\lambda|^2/2\). Equality in the triangle inequality requires all \(P_j\) to have phase \(a^2\), so \(P_j=2a^2/3=\lambda^2\) after choosing \(\lambda=a/\sqrt{3/2}\). Writing each pair as \(\lambda e^{i\theta_j}\), \(\lambda e^{-i\theta_j}\) gives the displayed family. All steps are equalities for this family, proving attainment and completeness. Distinct phase tuples modulo common nonzero scalar represent distinct projective extremizers.

## Verification
Execute `python3 checker.py` with Python's standard library. The checker independently forms all ordered two-sum fibers for prime fields of cardinalities \(5,7,11,13\), proves exact multiplicity patterns there, and checks the rational constant with squared witness magnitudes \(3\) at zero and \(2\) elsewhere. It also evaluates hundreds of random Gaussian-integer coefficient vectors using integer arithmetic. The exact witness convolution energy is \(12q^2-3\) when its total squared mass is \(2q+1\). Those finite tests confirm the calculations but are not substituted for the algebraic proof over every admissible prime power.

## Relationship to prior work
González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first posted 2024-05-26), obtain sharp inequalities for the quadratic parabola, paraboloids, and cones; their Theorems 1.1--1.4 concern different graphs or different even moments, and do not provide the cubic-graph formula or its nonconstant extremizers. Biswas and Stovall, *Sharp Fourier restriction to monomial curves*, arXiv:2302.05317, concerns Euclidean monomial curves and operator-norm concentration, not this finite-field counting-measure coefficient. The classical nonzero-sum uniqueness argument is elementary, but the exceptional *singleton-plus-opposite-pairs* zero fiber forces a different nonuniform optimizing mass profile than an antipodal set with no fixed origin. A prior exact cubic moment-curve endpoint record concerns a three-coordinate cubic moment curve at a sixth moment, and does not imply this two-coordinate fourth-moment result.

## Limitations
The theorem excludes characteristic three: \(t\mapsto t^3\) then becomes additive, destroying nonzero-fiber uniqueness. No claim is made for other monomial exponents, nonfinite fields, or the sixth moment. The finite checker cannot certify the infinite family, whose proof uses algebra valid uniformly in characteristic greater than three. The literature comparison is limited to the sources described above; an older equivalent formulation in additive energy or general extremal two-sum theory remains a bibliographic risk. No independent mathematical audit has been performed.

## References
1. Cristian González-Riquelme and Diogo Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public version 2024-05-26. https://arxiv.org/abs/2405.16647 ; https://arxiv.org/html/2405.16647v2 .
2. Chandan Biswas and Betsy Stovall, *Sharp Fourier restriction to monomial curves*, arXiv:2302.05317, first posted 2023. https://arxiv.org/abs/2302.05317 .
3. Gerd Mockenhaupt and Terence Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (background). https://arxiv.org/abs/math/0204234 .
