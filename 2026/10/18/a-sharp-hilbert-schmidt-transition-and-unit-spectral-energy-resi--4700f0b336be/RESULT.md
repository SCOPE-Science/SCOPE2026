# A sharp Hilbert–Schmidt transition and unit spectral-energy residue at the logarithmic Bergman threshold

## Finding

For real \(\alpha\), consider the logarithmically weighted Bergman Hilbert space \(A^2_{\log^\alpha}\) on the unit disk with measure \(dA(z)=dx\,dy/\pi\) and radial weight \(L(z)^\alpha\), where \(L(z)=\log(e/(1-|z|^2))\). For an analytic polynomial \(f(z)=\sum_{n\ge0}a_nz^n\), let
\[
(\mathcal Hf)(z)=\sum_{m\ge0}\left(\sum_{n\ge0}\frac{a_n}{m+n+1}\right)z^m.
\]
Then the polynomially defined Hilbert-matrix operator admits a Hilbert–Schmidt extension \(\mathcal H:A^2_{\log^\alpha}\to A^2\) **if and only if** \(\alpha>2\). Define
\[
q_\alpha(n)=\int_0^1t^n\left[\log\left(\frac{e}{1-t}\right)\right]^\alpha dt,\qquad H_n=\sum_{j=1}^n\frac1j,\quad H_n^{(2)}=\sum_{j=1}^n\frac1{j^2}.
\]
The exact squared Hilbert–Schmidt norm, finite in precisely that range, is
\[
\|\mathcal H\|_{\mathcal S_2}^2=\frac{\zeta(3)}{q_\alpha(0)}+\sum_{n=1}^\infty\frac1{q_\alpha(n)}\left(\frac{H_n}{n^2}-\frac{\zeta(2)-H_n^{(2)}}n\right).
\]
Moreover, the divergence at the sharp boundary has **unit residue**:
\[
\boxed{\displaystyle\lim_{\alpha\downarrow2}(\alpha-2)\|\mathcal H:A^2_{\log^\alpha}\to A^2\|_{\mathcal S_2}^2=1.}
\]
The previously established boundedness and compactness thresholds are not claimed as new. The new assertion is that every compact member of this parameter family is in the much smaller Hilbert–Schmidt ideal, together with its exact trace formula and critical spectral-energy residue.

## Assumptions and scope

The domain and range are complex Hilbert spaces with the exact, not merely equivalent, weighted area norms stated above. The orthogonal monomials satisfy \(\|z^n\|_{A^2_{\log^\alpha}}^2=q_\alpha(n)\) and \(\|z^m\|_{A^2}^2=1/(m+1)\). The parameter \(\alpha\) is real. Hilbert–Schmidt membership means that the closure from polynomials is a bounded Hilbert–Schmidt operator. No claim about other Schatten exponents or exact operator norms is made.

## Proof

**1. An exact nonnegative trace series.** Relative to the normalized input and output monomial bases, the Hilbert matrix has entries
\[
T_{m,n}=\frac{1}{m+n+1}\frac{1}{\sqrt{(m+1)q_\alpha(n)}}.
\]
Consequently, irrespective of whether this infinite matrix is bounded,
\[
\sum_{m,n\ge0}|T_{m,n}|^2=\sum_{n\ge0}\frac{J_n}{q_\alpha(n)},\qquad
J_n=\sum_{m\ge0}\frac{1}{(m+1)(m+n+1)^2}.
\]
The sum is the squared Hilbert–Schmidt norm whenever finite. It is an infinite nonnegative sum, so its divergence precludes any Hilbert–Schmidt extension, even if some other bounded extension might exist. At \(n=0\), \(J_0=\zeta(3)\). For \(n\ge1\), write \(k=m+1\) and use the exact partial-fraction identity
\[
\frac1{k(k+n)^2}=\frac1{n^2}\left(\frac1k-\frac1{k+n}\right)-\frac1n\frac1{(k+n)^2}.
\]
Summation yields
\[
J_n=\frac{H_n}{n^2}-\frac{\zeta(2)-H_n^{(2)}}n.
\]
This proves the displayed trace formula wherever finite, with no reliance on numerical truncations.

**2. Uniform large-degree moments.** For each fixed \(\alpha\), and uniformly for \(\alpha\in[2,3]\),
\[
q_\alpha(n)=\frac{(\log n)^\alpha}{n}\left(1+O\left(\frac1{\log n}\right)\right),\qquad n\to\infty.
\]
To justify uniformity, substitute \(u=n(1-t)\) in the integral defining \(q_\alpha(n)\). After extracting \((\log n)^\alpha/n\), the remaining integrand equals
\[
\left(1-\frac un\right)^n\left(1+\frac{1-\log u}{\log n}\right)^\alpha\mathbf1_{0<u<n}.
\]
For \(u\le n^{1/2}\), this has a uniform integrable domination by a constant times \(e^{-u/2}(1+|\log u|^3)\), and a first-order expansion yields a relative error \(O(1/\log n)\). For \(u>n^{1/2}\), the exponential factor makes the contribution smaller than every negative power of \(n\), including the integrable singular endpoint \(u\uparrow n\). The leading integral is \(\int_0^\infty e^{-u}du=1\). For arbitrary fixed real \(\alpha\), the same argument without uniform parameter bounds establishes the leading asymptotic \(q_\alpha(n)\sim (\log n)^\alpha/n\).

**3. Harmonic boundary flux.** The harmonic-number expansions give
\[
H_n=\log n+\gamma+O(n^{-1}),\qquad
\zeta(2)-H_n^{(2)}=n^{-1}+O(n^{-2}),
\]
so
\[
J_n=\frac{\log n+\gamma-1}{n^2}+O(n^{-3}).
\]
Combining this with the moments yields, for every fixed \(\alpha\),
\[
\frac{J_n}{q_\alpha(n)}\sim\frac1{n(\log n)^{\alpha-1}}.
\]
By the integral test the series converges exactly when \(\alpha>2\), proving the Hilbert–Schmidt classification. Absolute square summability also directly constructs the unique Hilbert–Schmidt extension.

**4. The sharp critical residue.** Uniformly for \(2\le\alpha\le3\), the preceding two estimates sharpen to
\[
\frac{J_n}{q_\alpha(n)}=\frac1{n(\log n)^{\alpha-1}}+O\left(\frac1{n(\log n)^\alpha}\right),\qquad n\ge3,
\]
with a constant independent of \(\alpha\). The series of error terms is bounded uniformly as \(\alpha\downarrow2\). The finite initial terms are also uniformly bounded. Setting \(\varepsilon=\alpha-2>0\), integral comparison gives
\[
\varepsilon\sum_{n\ge3}\frac1{n(\log n)^{1+\varepsilon}}\longrightarrow1,
\]
because \(\varepsilon\int_3^\infty dx/[x(\log x)^{1+\varepsilon}]=(\log3)^{-\varepsilon}\to1\). Multiplying the trace formula by \(\alpha-2\) proves the unit residue.

## Verification

The proof is analytic and makes no inference from finite numerical experiments to infinite-dimensional claims. The accompanying standalone Python file checks the exact partial-fraction identity against finite tails with explicit integral tail bounds, the leading harmonic asymptotic, and the critical model-series normalization. Its finite checks are supplementary. Every required norm and constant can be reproduced directly from the displayed formulas and the monomial moment integral.

## Relationship to prior work

Norrbo (first publicly posted September 23, 2026) establishes boundedness of the Hilbert matrix into ordinary Bergman space exactly from the logarithmic weight exponent \(\alpha\ge2\), along with the background \(\alpha>2\) mapping result. Earlier logarithmic-Bergman results and published compactness results determine boundedness and noncompactness at the endpoint. These facts neither assert a Hilbert–Schmidt ideal criterion nor compute the divergent quadratic spectral energy. Related essential-norm computations at \(\alpha=2\) involve a Hilbert–Schmidt *difference between operators*; that is not Hilbert–Schmidt membership of the Hilbert matrix itself. The present exact trace and unit pole are distinct and do not follow from compactness alone.

## Limitations

The parameter-independent residue depends on the stated exact radial weight and normalized area measure. Changing domain norm by a scalar changes the residue. The proof concerns only the Hilbert–Schmidt exponent; it does not determine the full singular-value distribution, all Schatten membership, nor the endpoint essential spectrum. Published related results were compared by their explicit claims and one directly motivating article was read in full, but an unindexed equivalent trace computation or a broader operator-ideal theorem could affect priority. Independent verification is not performed.

## References

1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252, publicly posted September 23, 2026. Full arXiv article, Sections 1–4, particularly the weighted monomial moment equivalence and Theorem 3.5.
2. C. Bellavita, V. Daskalogiannis, S. Miihkinen, D. Norrbo, G. Stylogiannis, and J. A. Virtanen, *Generalized Hilbert matrix operators acting on Bergman spaces*, Journal of Functional Analysis 288 (2025), article 110856.
3. Published published-finding corpus research records *Compactness phase transition for the logarithmic Hilbert matrix endpoint* and *Exact essential norm at the logarithmic Bergman endpoint*, indexed October 11, 2026; used for mathematical implication comparisons, not as novelty certificates.
