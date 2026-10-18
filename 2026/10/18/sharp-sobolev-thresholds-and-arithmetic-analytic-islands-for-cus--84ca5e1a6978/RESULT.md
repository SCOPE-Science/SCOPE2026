# Sharp Sobolev thresholds and arithmetic analytic islands for cusp-tent invariant densities

## Finding

For \(0<\alpha<1\), consider the symmetric full-branch cusp-tent map
\[
T_\alpha(x)=1-\frac34|2x-1|-\frac14|2x-1|^\alpha,
\qquad 0\le x\le1.
\]
It has a unique absolutely continuous invariant probability, whose density is written \(h_\alpha\). Put \(p=\alpha^{-1}>1\). For every integer \(k\ge1\), its **exact spatial Sobolev classification** is
\[
 h_\alpha\in W^{k,1}(0,1)
 \quad\Longleftrightarrow\quad
 \bigl(k<p\bigr)\ \text{or}\ \bigl(p\in\{2,3,4,\ldots\}\bigr).
\]
Furthermore, \(h_\alpha\) extends holomorphically to a complex neighborhood of the closed interval \([0,1]\) if and only if \(p\) is an integer. If \(p\) is not an integer, the exact boundary-leading term is
\[
 h_\alpha(1-u)\sim p4^p h_\alpha(1/2)u^{p-1},
 \qquad u\downarrow0,
 \qquad h_\alpha(1/2)>0.
\]
Thus the noninteger exponents admit exactly the integer Sobolev orders below \(p\), while each reciprocal-integer cusp exponent has an analytic invariant density.

## Assumptions and scope

The parameter is real and satisfies \(0<\alpha<1\). Sobolev spaces \(W^{k,1}(0,1)\) are defined by weak derivatives through order \(k\) in \(L^1\). Analyticity means a single holomorphic extension to some open complex neighborhood containing \([0,1]\); it is **spatial**, not parameter differentiability. All statements concern the unperturbed, full-height map shown above. No claim is made for perturbed cusp heights, random compositions, or endpoints \(\alpha=0,1\).

Write \(c=1/2\) and define \(s=\psi(u)\) as the unique \(s\in[0,1]\) satisfying
\[
 u=\frac34s+\frac14s^\alpha,
 \qquad 0\le u\le1.
\]
The inverse branches at target \(y\) are
\[
 \phi_\pm(y)=\frac{1\pm\psi(1-y)}2,
 \qquad |\phi_\pm'(y)|=\frac{\psi'(1-y)}2.
\]
Consequently, for integrable \(f\), the Perron--Frobenius operator is
\[
 (\mathcal Lf)(y)=\frac{\psi'(1-y)}2\left[f(\phi_-(y))+f(\phi_+(y))\right]
 \quad\text{for a.e. }0<y<1.
\]
On both monotonicity intervals, \(|T_\alpha'|\ge(3+\alpha)/2>1\); hence both inverse branches contract by at most \(\gamma=2/(3+\alpha)<1\).

## Proof

**1. Regularity of inverse branches.** At \(u=1\) the equation defining \(\psi\) has nonvanishing \(s\)-derivative, so \(\psi\) is real analytic there. At \(u=0\), put \(p=1/\alpha\), \(s=(4u)^p q\). The equation becomes
\[
 1=q^\alpha+3(4u)^{p-1}q.
\]
The analytic implicit-function theorem at \((q,\eta)=(1,0)\), where \(\eta=(4u)^{p-1}\), supplies a real-analytic \(q=Q(\eta)\) with \(Q(0)=1\). Therefore
\[
 \psi(u)=4^p u^p Q\!\left((4u)^{p-1}\right),
 \qquad \psi'(u)\sim p4^p u^{p-1}.
\]
Termwise differentiation of this convergent generalized-power expansion yields \(\psi^{(j)}(u)=O(u^{p-j})\) for every prescribed integer \(j\ge1\), provided \(p\) is noninteger. In particular, whenever \(k<p\), derivatives through order \(k\) are bounded and \(\psi^{(k+1)}\in L^1(0,1)\). If instead \(p=m\ge2\) is an integer, let \(z=s^{1/m}\); then \(4u=z+3z^m\). Analytic implicit inversion near \(z=0\) shows \(\psi(u)=z(u)^m\) is analytic at \(0\), and analytic continuation along \([0,1]\) yields a holomorphic extension to a neighborhood of the entire interval. In this case derivatives of every finite order are bounded.

**2. A Sobolev Lasota--Yorke estimate.** Fix an integer \(k\ge1\) such that either \(k<p\) or \(p\) is an integer. By Step 1, the inverse branches \(\phi_\pm\) have bounded derivatives through order \(k\), and their \((k+1)\)-st derivatives are integrable. For smooth \(f\), the order-\(k\) derivative of \(\mathcal Lf\) has leading term
\[
 \sum_{\sigma\in\{+,-\}}|\phi_\sigma'| (\phi_\sigma')^k f^{(k)}\!\circ\phi_\sigma,
\]
plus terms with \(f^{(j)}\circ\phi_\sigma\), \(0\le j<k\), and coefficients in \(L^1(0,1)\). Changing variables in the leading terms bounds their \(L^1\) norm by \(\gamma^k\|f^{(k)}\|_1\). For the terms \(j\le k-2\), one-dimensional Sobolev embedding bounds them by a constant times \(\|f\|_{W^{k-1,1}}\). For \(j=k-1\), change variables to \(x=\phi_\sigma(y)\): each term becomes \(\int b(x)|f^{(k-1)}(x)|\,dx\), where \(b\in L^1\) on the corresponding half interval. Split \(b=b_{\rm bounded}+b_{\rm small}\) with \(\|b_{\rm small}\|_1<\varepsilon\), and use
\[
 \|g\|_\infty\le \|g\|_1+\|g'\|_1,
 \quad g=f^{(k-1)}.
\]
It follows, after absorbing lower derivatives and choosing any small \(\varepsilon>0\), that
\[
 \|\mathcal Lf\|_{W^{k,1}}
 \le (\gamma^k+\varepsilon)\|f\|_{W^{k,1}}
       +C_{k,\varepsilon}\|f\|_{W^{k-1,1}},
 \qquad \gamma^k+\varepsilon<1.
\]
Approximation extends the estimate and bounded action to \(W^{k,1}\). The positive operator \(\mathcal L\) is an \(L^1\) contraction and preserves the integral. For clarity, write \(\lambda_k=\gamma^k+\varepsilon<1\). Iteration of the one-step estimate gives
\[
 \|\mathcal L^n f\|_{W^{k,1}}\le\lambda_k^n\|f\|_{W^{k,1}}
 + C\sum_{j=0}^{n-1}\lambda_k^{n-1-j}\|\mathcal L^j f\|_{W^{k-1,1}}.
\]
Starting from the \(L^1\) contraction at order zero, induction gives uniform bounds on lower-order powers, hence a uniform power bound on \(W^{k,1}\). Compact embedding \(W^{k,1}\hookrightarrow W^{k-1,1}\) and the strict Lasota--Yorke inequality give essential spectral radius at most \(\lambda_k<1\) (the standard compactness/quasi-compactness lemma). This also produces a nonzero eigenvector at eigenvalue \(1\), as follows. To see the last assertion explicitly, the invariant integration functional makes \(1\) belong to the spectrum; quasi-compactness places it in the point spectrum. Eigenvalues outside the unit disk are excluded by the \(L^1\) contraction. The usual one-dimensional full-branch expanding uniqueness argument (or the standard Rychlik/Lasota--Yorke theory applied to the bounded-variation inverse slopes) yields a unique normalized invariant density \(h_\alpha\in W^{1,1}\); therefore every higher-order invariant eigenvector agrees with \(h_\alpha\) up to scaling. This proves the asserted **sufficient** Sobolev orders.

**3. Strict positivity at the cusp point.** Since \(h_\alpha\in W^{1,1}\), it has a continuous representative. There is an open interval \(J\subset(0,1)\) on which \(h_\alpha\) is bounded below by a positive constant. The cylinders formed from the two full inverse branches partition \([0,1]\) and have lengths at most \(\gamma^n\), so some cylinder of sufficiently large depth lies wholly inside \(J\). Applying the invariant equation \(h_\alpha=\mathcal L^n h_\alpha\) to that cylinder shows that \(h_\alpha(y)>0\) at every interior \(y\); all inverse derivatives there are strictly positive. In particular \(h_\alpha(c)>0\).

**4. Sharp failure beyond the threshold.** Substitute the continuous values \(h_\alpha(\phi_\pm(1-u))\to h_\alpha(c)\) into the transfer equation. Step 1 then gives
\[
 h_\alpha(1-u)
   =\frac{\psi'(u)}2\bigl[h_\alpha(\phi_-(1-u))+h_\alpha(\phi_+(1-u))\bigr]
   \sim p4^p h_\alpha(c)u^{p-1}.
\]
For noninteger \(p\), put \(r=\lceil p\rceil\). If \(h_\alpha\) belonged to \(W^{r,1}\), then the one-dimensional Sobolev embedding would give a \(C^{r-1}\) representative on \([0,1]\). But the strictly nonzero fractional-power leading term \(u^{p-1}\) has exponent strictly between \(r-2\) and \(r-1\) and cannot have a \(C^{r-1}\) Taylor expansion at the endpoint. Thus \(h_\alpha\notin W^{r,1}\), and membership in any higher integer Sobolev order is also impossible. Together with Step 2 this is the exact noninteger classification.

**5. Integer-resonance analyticity.** If \(p=m\) is an integer, Step 1 makes both inverse branches and their Jacobian weights holomorphic near \([0,1]\). Their real derivatives are bounded in modulus by \(\gamma<1\), hence for a sufficiently thin bounded complex neighborhood \(U\) of \([0,1]\), each branch sends \(\overline U\) compactly into \(U\). The holomorphic weighted composition operator \(\mathcal L:H^\infty(U)\to H^\infty(U)\) is compact by Montel's theorem. Integration along \([0,1]\) is a nonzero continuous invariant functional, so \(1\) belongs to its spectrum and, by compactness, is an eigenvalue. Any associated eigenfunction is smooth on \([0,1]\), lies in \(W^{1,1}\), and hence is a scalar multiple of the unique invariant density; therefore \(h_\alpha\) has the asserted holomorphic extension. Conversely, if \(p\notin\mathbb N\), Step 4 precludes analyticity. This completes the classification.

## Verification

The inverse-function formula is exact: for each \(u\in[0,1]\), the equation \(4u=3s+s^\alpha\) is strictly increasing in \(s\), and at the endpoints it yields \(\psi(0)=0\), \(\psi(1)=1\). Differentiating gives
\[
 \psi'(u)=\frac4{3+\alpha\psi(u)^{\alpha-1}},
 \qquad \left|\phi_\pm'(y)\right|=\frac{2}{3+\alpha\psi(1-y)^{\alpha-1}}\le\frac2{3+\alpha}.
\]
The power substitution \(s=(4u)^p q\) exactly recovers \(1=q^\alpha+3(4u)^{p-1}q\). At \(p=m\in\mathbb N\), \(4u=z+3z^m\) gives a simple analytic inverse with positive derivative throughout the real interval. All estimates above are analytic, not finite-sample extrapolations. As additional exploratory checks, a high-precision inverse solver verifies \(\psi'(u)/(p4^pu^{p-1})\to1\) for exponents \(p=2,5/2,3,4\), and a finite-grid transfer iteration checks the boundary ratio; these numerical checks are not used as proofs.

## Relationship to prior work

Bahsoun and Galatolo introduced this cusp-tent construction at reciprocal exponent \(p=8\), establishing a Sobolev \(W^{2,1}\) spectral gap and linear response for cusp-height perturbations. Oltiboev later obtained \(W^{2,q}\) results for broader cusp parameters and \(L^q\) linear response. These results do not provide the exact all-order **spatial** Sobolev threshold nor the necessity of reciprocal-integer exponents for spatial analyticity. The general holomorphic transfer-operator theory of Bandtlow and Jenkinson explains the analytic mechanism, but their stated strictly positive endpoint-weight setting does not directly cover the weight vanishing at the critical value in this map. Contemporary random-map cusp papers address \(W^{2,1}\) regularity and analytic **parameter response**, not the present complete spatial regularity classification. The proof's nontrivial additions are the noninteger upper-bound obstruction, the all-order Sobolev bootstrap and the complete arithmetic dichotomy.

## Limitations

The result is confined to the exact full-height two-branch formula above. It does not establish higher-order linear response under changes of the cusp height, nor stability of the classification under asymmetry or stochastic forcing. The boundary asymptotic gives only the first nonzero term, not a full asymptotic series for \(h_\alpha\). Numerical examples are illustrative only.

## References

1. W. Bahsoun and S. Galatolo, *Linear response due to singularities*, arXiv:2301.02301 (first posted 2023-01-05); *Nonlinearity* 37 (2024), 075010. https://arxiv.org/html/2301.02301v3
2. D. Oltiboev, *Linear response for systems with a cusp*, arXiv:2505.17462 (2025). https://arxiv.org/html/2505.17462v1
3. O. F. Bandtlow and O. Jenkinson, *Invariant measures for real analytic expanding maps*, *J. London Math. Soc.* 75 (2007), 343--368, Theorem 8.5. https://webspace.maths.qmul.ac.uk/o.m.jenkinson/weights25.pdf
4. M. Rychlik, *Bounded variation and invariant measures*, *Studia Math.* 76 (1983), 69--80.
5. D. Oltiboev and F. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, *ACTA NUUz* 2 (2026), 178--183. https://journals.nuu.uz/index.php/actanuuz/article/view/15305
6. D. Oltiboev, K. Rakhimov and M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969 (2026). https://arxiv.org/abs/2608.26969
