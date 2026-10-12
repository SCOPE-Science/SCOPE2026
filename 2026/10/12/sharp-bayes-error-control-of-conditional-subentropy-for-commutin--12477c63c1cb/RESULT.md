# Sharp Bayes-error control of conditional subentropy for commuting ensembles

## Finding

Let \(X\) and \(B\) be finite classical registers with arbitrary joint distribution \(p_{xb}\), including zero probabilities. Define the marginals \(q_b=\sum_x p_{xb}\), and use natural-logarithm subentropy \(Q\). Then
\[
\boxed{0\le Q(p_{xb})-Q(q_b)\le 1-\sum_b\max_x p_{xb}\le-\ln\!\left(\sum_b\max_x p_{xb}\right).}
\]
All sums run over their respective finite alphabets, and \(\sum_{x,b}p_{xb}=1\). Equivalently, if \(\rho_{XB}=\sum_x p_x|x\rangle\langle x|\otimes\rho_x^B\) is a finite-dimensional classical–quantum state whose conditional density operators commute pairwise, its conditional subentropy obeys
\[
\boxed{Q(X|B)_\rho\le 1-p_{\mathrm{guess}}(X|B)_\rho,}
\]
where \(Q(X|B)_\rho=Q(\rho_{XB})-Q(\rho_B)\), and \(p_{\mathrm{guess}}(X|B)_\rho\) is the optimal probability of correctly guessing \(X\) by observing \(B\). Thus \(p_{\mathrm{guess}}(X|B)_\rho\le1-Q(X|B)_\rho\), a linear upper bound sharper than the conjectured exponential certificate for commuting signals.

The coefficient \(1\) on the classical Bayes error is optimal uniformly over dimensions: for a trivial side-information register and binary law \((1-\varepsilon,\varepsilon)\),
\[
\lim_{\varepsilon\downarrow0}\frac{Q(1-\varepsilon,\varepsilon)}{\varepsilon}=1.
\]

## Assumptions and scope

The alphabets of \(X,B\) are finite and nonempty. The joint law may have arbitrary support, and no lower bound on positive entries is assumed. All logarithms are natural. Subentropy for a probability vector \(v=(v_1,\ldots,v_n)\) is the continuous extension of
\[
Q(v)=-\sum_{i=1}^n\frac{v_i^{\,n}\ln v_i}{\prod_{j\ne i}(v_i-v_j)}
\]
from distinct positive entries, with coincident values understood by limits. Appending zero entries leaves \(Q\) unchanged. For a diagonal density matrix, the same formula applies to its eigenvalues.

The conclusion for a classical–quantum state assumes pairwise commutation \([\rho_x^B,\rho_y^B]=0\) for all labels \(x,y\). This provides a common orthonormal diagonalizing basis on \(B\); with \(p_{xb}=p_x\langle b|\rho_x^B|b\rangle\), the spectrum of \(\rho_{XB}\) is the list \(p_{xb}\), and that of \(\rho_B\) is the list \(q_b\). The optimal measurement for distinguishing commuting signal states reads that basis and guesses a maximizing \(x\) for each \(b\), so \(p_{\mathrm{guess}}=\sum_b\max_x p_{xb}\).

## Proof

**Integral representation.** The half-axis identity for normalized subentropy is
\[
Q(v)=\int_0^\infty\left[\frac{t}{t+1}-\prod_i\frac{t}{t+v_i}\right]\,\mathrm dt.
\tag{1}
\]
It follows from the divided-difference definition by substituting the integral formula for logarithms and resolving the partial fractions. It is also formula (14) of Jozsa–Mitchison after setting the first elementary symmetric polynomial equal to \(1\). All factors \(t/(t+v_i)\) lie in \((0,1]\) for \(t>0\), and factors for zero entries equal \(1\). The integrand in (1) is integrable near both endpoints; the formula extends to coinciding values and zero entries by continuity.

**Sharp mass-splitting lemma.** Suppose \(v=(w,v_2,\ldots,v_n)\) is a probability vector with \(w>0\). Replace the mass \(w\) by \((w-a,a)\) for \(0\le a\le w\), keeping all other masses unchanged; denote the new vector by \(v^{(a)}\). Set \(F(a)=Q(v^{(a)})\), with \(F(0)=Q(v)\) by zero-padding. Subtracting (1) gives
\[
F(a)-F(0)=a(w-a)\int_0^\infty
 \frac{t\,\prod_{j=2}^n t/(t+v_j)}{(t+w)(t+w-a)(t+a)}\,\mathrm dt\ge0.
\tag{2}
\]
For each \(t>0\), the function of a nonnegative mass list \(z\) defined by \(G_t(z)=\prod_j t/(t+z_j)\) is convex: indeed \(\log G_t(z)=\sum_j[\log t-\log(t+z_j)]\) has nonnegative diagonal Hessian, so \(G_t\) is log-convex and therefore convex. Equation (1) shows \(Q\) is concave along all affine mass-preserving paths, so \(F\) is concave on \([0,w]\). By differentiating (2) at \(0\), justified by the integrable dominating function \(w/(t+w)^2\),
\[
0\le F'(0+)
 =w\int_0^\infty\frac{\prod_{j=2}^n t/(t+v_j)}{(t+w)^2}\,\mathrm dt
 \le w\int_0^\infty\frac{\mathrm dt}{(t+w)^2}=1.
\]
The supporting-line inequality for a concave function now yields the dimension-free sharp refinement bound
\[
\boxed{0\le Q(v^{(a)})-Q(v)\le a.}
\tag{3}
\]
The case \(w=0\) is trivial; the endpoint cases \(a=0,w\) follow by continuity.

**Apply refinement to each observation.** Starting with the marginal probability list \((q_b)_b\), retain for every \(b\) a label \(x_b\) at which \(p_{xb}\) is maximal. For fixed \(b\), split the mass \(q_b\) into the individual entries \(p_{xb}\) by peeling off all \(p_{xb}\) with \(x\ne x_b\), leaving \(p_{x_b b}\) as the remainder. At each peel, inequality (3) bounds the increase of subentropy by the amount peeled, irrespective of all other entries. After finitely many operations, the resulting list consists of all \(p_{xb}\) up to permutation and zero padding. Telescoping gives
\[
0\le Q(p_{xb})-Q(q_b)
 \le\sum_b\sum_{x\ne x_b}p_{xb}
 =\sum_b(q_b-\max_xp_{xb})
 =1-p_{\mathrm{guess}}(X|B).
\]
Since \(0<p_{\mathrm{guess}}\le1\), the elementary inequality \(1-u\le-\ln u\) yields the final displayed bound. For the sharpness assertion, start from the one-point law \((1)\), split its mass into \((1-\varepsilon,\varepsilon)\), and use the derivative formula with \(w=1\) and no other nonzero mass: its right derivative at zero is \(\int_0^\infty(1+t)^{-2}\,\mathrm dt=1\). Therefore \(Q(1-\varepsilon,\varepsilon)=\varepsilon+o(\varepsilon)\).

## Verification

The proof of (3) is analytic and covers all finite dimensions, arbitrary real probabilities, repeated spectral values and zero entries. A separate runnable checker, `verify_subentropy.py`, evaluates subentropy directly from its divided-difference definition at high precision for 48 explicit and reproducibly generated rational joint distributions, including a law with zeros, and checks the linear bound. It also tests three small positive binary errors. Executing the packaged checker produced:

`VERIFY_OK tables=48 binary_edges=3 precision=85 analytic_proof_required=yes`

These finite spot checks are not used to infer the universal inequality or the sharp asymptotic coefficient.

## Relationship to prior work

Datta, Dorlas, Jozsa and Benatti introduced \(Q(X|B)\), proved its nonnegativity for every classical–quantum state (Proposition 5), and conjectured \(Q(X|B)\le-\ln p_{\mathrm{guess}}(X|B)\) for all such states (Conjecture 2). Their Proposition 6 treats two pure conditional states. The present theorem proves a strictly stronger linear bound on the complete commuting-signal sector, with arbitrary numbers of labels, mixed conditional states and nonuniform priors; it does not address noncommuting signals.

Jozsa and Mitchison developed integral and monotonicity formulas for subentropy. Their formula (14) is precisely the integral identity (1), and their Property 9 gives the already-known lower inequality \(Q(p_{xb})\ge Q(q_b)\). Those statements supply general analytic structure and the nonnegative half of the present theorem, but neither states the Bayes-error upper bound nor the sharp mass-splitting estimate. The new implication depends on applying a sharp one-sided derivative bound through successive conditional refinements.

## Limitations

The upper bound has only been proved for commuting conditional density matrices (equivalently classical–classical joint states). It does not settle the original conjecture for noncommuting ensembles, and it is not a statement about arbitrary bipartite quantum states. The numerical checker tests distinct positive spectra and some zero entries; repeated positive spectra, arbitrary dimensions and the exact sharpness statement are handled by the analytic argument rather than exhaustive computation. The originality comparison cannot exclude an unindexed equivalent bound under statistical decision-theory or spectral-refinement terminology. No independently conducted mathematical audit has been performed.

## References

1. N. Datta, T. Dorlas, R. Jozsa and F. Benatti, *Properties of subentropy*, arXiv:1310.1312 (first public preprint 2013-10-04); *Journal of Mathematical Physics* **55**, 062203 (2014), DOI:10.1063/1.4882935. See §2.5, Proposition 5, Conjecture 2 and Proposition 6.
2. R. Jozsa and G. Mitchison, *Symmetric polynomials in information theory: entropy and subentropy*, arXiv:1404.7694 (2014). See §2, formula (14), and Appendix Property 9.
