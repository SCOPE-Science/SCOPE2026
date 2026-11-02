# A critical Hilbert–Schmidt pole and exponential column-energy escape for logarithmic Bergman Hilbert matrices

## Finding
Let \(dA(z)=\pi^{-1}dx\,dy\) on the unit disk and let \(\mathcal A_\alpha\) be the analytic Hilbert space with squared norm
\[
\|f\|_{\mathcal A_\alpha}^{2}=\int_{\mathbb D}|f(z)|^2\biggl(\log\frac{e}{1-|z|^2}\biggr)^\alpha dA(z),\qquad\alpha\in\mathbb R.
\]
Let \(H_\alpha:\mathcal A_\alpha\to A^2(\mathbb D)\) be the Hilbert matrix, initially on polynomials, defined by
\[
H_\alpha\Bigl(\sum_{n\ge0}a_nz^n\Bigr)=\sum_{m\ge0}\Bigl(\sum_{n\ge0}\frac{a_n}{m+n+1}\Bigr)z^m.
\]
Then \(H_\alpha\) extends to a Hilbert–Schmidt operator exactly when \(\alpha>2\). Its squared Hilbert–Schmidt norm obeys the **sharp pole and finite-part law**
\[
\|H_{2+\varepsilon}\|_{\mathcal S_2}^2=\frac1\varepsilon+\mathcal C+o(1)\qquad(\varepsilon\downarrow0),
\]
where \(\mathcal C\) is the absolutely convergent series given below. In particular, the leading coefficient is exactly \(1\) under the stated normalization.

There is also a distributional strengthening. Write \(v_n(\alpha)=\|z^n\|_{\mathcal A_\alpha}^2\), \(S_n=\sum_{m\ge0}[(m+1)(m+n+1)^2]^{-1}\), and \(w_{\varepsilon,n}=(S_n/v_n(2+\varepsilon))/\|H_{2+\varepsilon}\|_{\mathcal S_2}^2\). Give index \(n=0,1,2\) location zero and index \(n\ge3\) location \(\varepsilon\log\log n\). The discrete probability measures \(\sum_{n\ge0}w_{\varepsilon,n}\delta_{\mathrm{location}(n)}\) converge weakly to the mean-one exponential distribution on \([0,\infty)\). Thus the dominant Hilbert–Schmidt energy migrates to doubly exponential Taylor-degree scales as the boundedness threshold is approached.

## Assumptions and scope
All operators are complex-linear. The ordinary Bergman codomain has norm \(\|z^m\|^2=1/(m+1)\). The radial source weight, its leading coefficient, and the normalized area measure are fixed exactly as above; merely equivalent renormings can change the pole coefficient and finite part. For \(\alpha\le2\), the Hilbert–Schmidt series diverges on the polynomial domain, independent of whether the operator otherwise extends boundedly. Published boundedness at \(\alpha=2\) and unboundedness for \(\alpha<2\) are not re-claimed here.

Define the usual harmonic sums \(h_n=\sum_{j=1}^n1/j\), \(h_n^{(2)}=\sum_{j=1}^n1/j^2\), both zero at \(n=0\). One has
\[
\begin{split}
S_0&=\zeta(3),\\
S_n&=\frac{h_n}{n^2}-\frac{\zeta(2)-h_n^{(2)}}n \quad(n\ge1),\\
v_n(2)&=\frac{(1+h_{n+1})^2+h_{n+1}^{(2)}}{n+1} \quad(n\ge0).
\end{split}
\]
The explicit finite part is
\[
\mathcal C=\sum_{n=0}^2\frac{S_n}{v_n(2)}-\log\log3+
\sum_{n=3}^\infty\left(\frac{S_n}{v_n(2)}-\log\frac{\log(n+1)}{\log n}\right).
\]
The last series converges absolutely (its summands are \(O(1/(n\log^2n))\)).

## Proof
**1. Orthogonal columns.** Rotation invariance makes the normalized source monomials \(e_n=z^n/\sqrt{v_n(\alpha)}\) an orthonormal basis. Since the squared Bergman norm of \(z^m\) equals \(1/(m+1)\),
\[
\|H_\alpha e_n\|_{A^2}^2=\frac1{v_n(\alpha)}\sum_{m=0}^\infty\frac1{(m+1)(m+n+1)^2}=\frac{S_n}{v_n(\alpha)}.
\]
Consequently \(\|H_\alpha\|_{\mathcal S_2}^2=\sum_{n\ge0}S_n/v_n(\alpha)\) whenever this sum is finite. Conversely finite Hilbert–Schmidt norm of any extension forces convergence. Finite column sum defines a unique Hilbert–Schmidt extension of the polynomial action.

**2. Exact inner series and critical moments.** For \(n\ge1\), partial fractions with \(k=m+1\) yield
\[
\frac1{k(k+n)^2}=\frac1{n^2}\left(\frac1k-\frac1{k+n}\right)-\frac1n\frac1{(k+n)^2},
\]
giving the displayed harmonic formula. For the moments, substitute \(t=|z|^2\), obtaining \(v_n(\alpha)=\int_0^1t^n(1-\log(1-t))^\alpha dt\). Differentiating \(B(n+1,b)\) at \(b=1\) gives the stated exact formula at \(\alpha=2\): the first two moments of \(-\log(1-t)\) under density \((n+1)t^n dt\) are \(h_{n+1}\) and \(h_{n+1}^2+h_{n+1}^{(2)}\).

**3. Uniform asymptotics.** Uniformly for \(2\le\alpha\le3\), elementary logarithmic-moment estimates imply
\[
v_n(\alpha)=\frac{(\log n)^\alpha}{n}\left(1+O((\log n)^{-1})\right)\quad(n\ge3).
\]
For completeness, under the probability density \((n+1)t^n dt\), the variable \(Y=-\log(1-t)\) has the distribution of the maximum of \(n+1\) independent unit exponentials. The centered random variables \(Y-\log(n+1)\) have uniformly bounded absolute moments through order four: from \(\mathbb P(Y>\log(n+1)+u)\le e^{-u}\) and \(\mathbb P(Y<\log(n+1)-u)\le\exp(-e^u)\) in their applicable ranges, integration of tails proves the bound. Applying the mean-value inequality to \((1+Y)^\alpha\), uniformly for \(\alpha\in[2,3]\), gives the displayed estimate. The harmonic formula gives \(S_n=(\log n+O(1))/n^2\). Therefore
\[
\frac{S_n}{v_n(2+\varepsilon)}=
\frac{1}{n(\log n)^{1+\varepsilon}}+r_{n,\varepsilon},
\qquad |r_{n,\varepsilon}|\le\frac{C}{n(\log n)^{2+\varepsilon}}
\]
for \(0\le\varepsilon\le1\) and all \(n\ge3\), with a common constant \(C\). At any fixed \(\alpha\), the same leading asymptotic shows convergence exactly for \(\alpha>2\) by the integral test (and divergence otherwise).

**4. Laurent pole and finite part.** Put \(b_\varepsilon(x)=1/[x(\log x)^{1+\varepsilon}]\) for \(x\ge3\). As \(b_\varepsilon\) is decreasing, the difference between its sum over \(n\ge3\) and the integral over \([3,\infty)\) has a summable termwise decomposition, continuous at \(\varepsilon=0\). Step 3 shows the same for \(S_n/v_n(2+\varepsilon)-b_\varepsilon(n)\), uniformly dominated by \(C/[n(\log n)^2]\). Thus dominated convergence gives a finite limit of
\[
\|H_{2+\varepsilon}\|_{\mathcal S_2}^2-
\int_3^\infty b_\varepsilon(x)\,dx.
\]
The integral equals \((\log3)^{-\varepsilon}/\varepsilon=1/\varepsilon-\log\log3+O(\varepsilon)\). Evaluating the continuous difference at zero yields exactly \(\mathcal C\), proving the expansion.

**5. Exponential escape.** The uniform summable remainder in Step 3 makes the total variation of the unnormalized tail weights and \(b_\varepsilon(n)\) bounded independently of \(\varepsilon\in(0,1]\). The discrepancy from replacing the latter sum by \(b_\varepsilon(x)dx\) is likewise uniformly bounded by the integral test. After division by \(\|H_{2+\varepsilon}\|_{\mathcal S_2}^2\sim1/\varepsilon\), both errors vanish. Under the substitution \(u=\varepsilon\log\log x\),
\[
b_\varepsilon(x)\,dx=\frac1\varepsilon e^{-u}\,du,
\qquad u\ge\varepsilon\log\log3.
\]
Hence normalized tail probabilities converge to \(e^{-t}\) for every \(t>0\), and the mass of the first three indices tends to zero. This proves the asserted weak convergence.

## Verification
The included `checks.py` uses only the standard Python library. It compares the beta-derivative formula for \(v_n(2)\) with an independent convergent integral, the partial-fraction formula for \(S_n\) with a direct finite sum and rigorous remainder inequality, and representative finite asymptotic ratios. It passed 32 checks. These finite checks do not establish the infinite-dimensional assertions; the displayed analytic proof does.

## Relationship to prior work
Norrbo (2026) determines exactly when the Hilbert matrix maps the logarithmically weighted Bergman space boundedly to ordinary Bergman space, including the critical index \(\alpha=2\). Karapetrović (2018) and earlier Karapetrović–Jevtić work establish supercritical mapping properties. The contribution here is **not** another boundedness theorem, but the separate sharp Hilbert–Schmidt pole, exact renormalized finite part, and scaling law for column-energy escape. Related published work on the Fredholm essential spectrum at the critical endpoint treats a noncompact operator and does not imply these supercritical quantitative laws. Broader work on Schatten ideals or generalized Hilbert matrices may still contain implicit reformulations and should be checked for publication priority.

## Limitations
The finite part is presented as an absolutely convergent harmonic series, not as a reduction to elementary constants. The exponential law concerns the column-energy distribution in the distinguished radial monomial basis, not the distribution of singular values or their singular vectors. No assertion is made about general Schatten exponents or other source renormings. Publication-priority comparisons are based on available primary texts and indexed research records; independent mathematical validation has not been performed.

## References
- D. Norrbo, *The Hilbert matrix operator into the Bergman space* (2026), arXiv:2610.00252v1, first public 2026-09-23; https://arxiv.org/html/2610.00252v1.
- B. Karapetrović, *Libera and Hilbert matrix operator on logarithmically weighted Bergman, Bloch and Hardy-Bloch spaces*, Czechoslovak Mathematical Journal 68 (2018), 559–576; https://dml.cz/dmlcz/147236.
- M. Lindström, S. Miihkinen, and D. Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces* (2022), arXiv:2201.09591.
