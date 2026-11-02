# Arithmetic filling and polynomial spectral regions for two-atom Hausdorff matrices

## Finding

Let \(0<u,v<1\) be distinct and let \(a,b>0\). Consider the Hausdorff matrix \(\mathcal H_{\mu}\) associated with \(\mu=a\delta_u+b\delta_v\), acting either on \(\mathrm{BMOA}\) or the Bloch space \(\mathscr B\). Write \(M=a/u+b/v\). Then its ordinary spectrum and its Fredholm essential spectrum **coincide** on both spaces. Their common value is determined by an arithmetic dichotomy:

* If \(\log u/\log v\notin\mathbb Q\), the two spectra equal the **closed disk** \(\{w\in\mathbb C:|w|\le M\}\).
* If \(\log u/\log v=m/n\in\mathbb Q\), with relatively prime positive integers \(m,n\), let \(q=u^{1/m}=v^{1/n}\in(0,1)\). The spectra equal the exact polynomial region
  \[\left\{a z^m+b z^n:|z|\le q^{-1}\right\}.\]

The rational-case region can be strictly smaller than the disk of radius \(M\): for \(m=1,n=2\), its boundary cannot contain \(-M\), although it contains \(M\). In contrast, irrational logarithmic ratios always fill the full disk even in the Fredholm essential spectrum.

## Assumptions and scope

The spaces are complex Banach spaces of holomorphic functions on the unit disk \(\mathbb D\). The BMOA and Bloch norms are their standard norms. The Hausdorff matrix is defined on Taylor coefficients by
\[c_{j,k}=\binom{j}{k}\bigl(a u^k(1-u)^{j-k}+b v^k(1-v)^{j-k}\bigr),\qquad 0\le k\le j,\]
and extended by boundedness to the stated spaces. Equivalently, its holomorphic action is
\[\mathcal H_{\mu}f(z)=\sum_{t\in\{u,v\}}\frac{\mu(\{t\})}{1-(1-t)z}\,f\!\left(\frac{t z}{1-(1-t)z}\right).\]
Only **positive** masses and two **distinct** strictly interior atoms are claimed. The Fredholm essential spectrum is \(\{w:wI-T\text{ is not Fredholm}\}\), not the Weyl or Browder spectrum. No assertion about fine spectral types or the point spectrum on the dual target spaces is made.

## Proof

**Step 1: transfer to common-boundary-point composition semigroups.** On \(H^1\) let
\[C_t f(z)=f(1-t+t z),\qquad 0<t\le1.\]
By the coefficient-pairing duality in Galanopoulos–Mahillo–Oliva-Maza–Siskakis, \(\mathcal H_\mu\) on BMOA has the same ordinary and Fredholm essential spectra as \(S=aC_u+bC_v\) on \(H^1\). For the Bloch space, the preadjoint on \(A^1\) is conjugate, through the bounded isomorphism \(J:D^1\to A^1\), \(Jf=(zf)'\), to the same \(S\) on the Dirichlet-type space
\[D^1=\{f\in\operatorname{Hol}(\mathbb D):\ |f(0)|+\int_\mathbb D|f'(z)|\,dA(z)<\infty\}.\]
The source proves these preadjoint identifications, including the effect of coefficient conjugation. For the positive real masses used here, the spectral sets are invariant under conjugation, so the identification is exact. It therefore suffices to establish both spectra of \(S\) on either \(X=H^1\) or \(X=D^1\).

**Step 2: common growth and eigenfunctions.** The composition law is \(C_sC_t=C_{st}\). The source establishes uniform constants \(K_X<\infty\) for
\[\|C_t\|_{X\to X}\le K_X t^{-1}\qquad(0<t\le1)\]
on both spaces. The functions
\[f_\lambda(z)=(1-z)^{-\lambda},\qquad \operatorname{Re}\lambda<1,\]
belong to both spaces and satisfy
\[C_t f_\lambda=t^{-\lambda}f_\lambda.\]
In \(D^1\) the constant function also occurs, but no additional case is needed. By the binomial theorem and the semigroup law,
\[\|S^k\|\le K_X\sum_{j=0}^{k}\binom kj(a/u)^j(b/v)^{k-j}=K_X M^k.\]
Thus the spectral radius of \(S\) does not exceed \(M\), so \(\sigma(S)\subseteq\overline{D(0,M)}\).

**Step 3: a local-vanishing lemma for vertical eigenfunction families.** Fix \(x<1\) and let \(\lambda_y=x+iy\) as \(y\to+\infty\). Set \(g_y=f_{\lambda_y}/\|f_{\lambda_y}\|_X\). Then \(\|g_y\|_X=1\), while \(g_y\to0\) locally uniformly on \(\mathbb D\). To verify this rather than merely invoke it, use the branch of \(\log(1-z)\) with \(|\arg(1-z)|<\pi/2\). On any compact \(K\Subset\mathbb D\), choose \(c_K<\pi/2\) bounding \(\arg(1-z)\); thus \(\sup_K|f_{x+iy}|\le C_{K,x}e^{c_Ky}\). For any fixed \(c\in(c_K,\pi/2)\), choose a positive-length boundary arc (for \(H^1\)) or a fixed positive-area interior patch (for \(D^1\)) on which \(\arg(1-z)>c\). The integral defining the norm, using \(f'_{x+iy}=(x+iy)(1-z)^{-x-iy-1}\) in \(D^1\), then gives \(\|f_{x+iy}\|_X\ge C_{x,c}e^{cy}\) for large \(y\) (and in fact an additional factor \(|x+iy|\) in \(D^1\)). Consequently \(\sup_K|g_y|\to0\). All constants depend only on the displayed fixed data, not on \(y\).

**Step 4: irrational logarithmic ratio.** Suppose \(\log u/\log v\notin\mathbb Q\). Fix any \(w\ne0\) with \(|w|<M\). The continuous, strictly increasing function
\[F(x)=a u^{-x}+b v^{-x},\qquad x<1,\]
has range \((0,M)\); choose its unique \(x\) with \(F(x)=|w|\). By the two-frequency Kronecker density theorem, there are \(y_j\to+\infty\) such that
\[u^{-iy_j}\to w/|w|,\qquad v^{-iy_j}\to w/|w|.\]
It follows that \(Sg_{y_j}=w_jg_{y_j}\) for eigenvalues \(w_j=a u^{-x-iy_j}+b v^{-x-iy_j}\to w\), and \(\|(S-wI)g_{y_j}\|\to0\). If \(S-wI\) were Fredholm, closedness of its range and the open mapping theorem would give a constant \(C\) such that
\[\operatorname{dist}(f,\ker(S-wI))\le C\|(S-wI)f\|,\qquad f\in X.\]
Hence \(g_{y_j}\) would approach a finite-dimensional kernel in norm. A norm-convergent subsequence would converge to a unit kernel element, contradicting the local uniform convergence to zero and continuity of point evaluations on \(X\). Thus every \(w\) in the punctured disk is in the **Fredholm essential** spectrum. Since that spectrum is closed, it contains the origin and the boundary as well. The spectral-radius upper bound from Step 2 proves the claimed equality.

**Step 5: rational logarithmic ratio.** If \(u=q^m\) and \(v=q^n\), then \(S=p(C_q)\) for \(p(z)=az^m+bz^n\). The estimate in Step 2, applied to \(C_q\), shows \(\sigma(C_q)\subseteq\{z:|z|\le q^{-1}\}\). Conversely every nonzero \(z\) with \(|z|<q^{-1}\) can be written \(q^{-\lambda}=z\) with \(\operatorname{Re}\lambda<1\). It is an eigenvalue of \(C_q\) on both \(X\), with an **infinite-dimensional eigenspace**: replacing \(\lambda\) by \(\lambda+2\pi i k/\log q\), \(k\in\mathbb Z\), preserves the eigenvalue and produces linearly independent functions \(f_\lambda\). Therefore \(\sigma_{\mathrm{ess}}(C_q)=\sigma(C_q)=\{z:|z|\le q^{-1}\}\). Polynomial spectral mapping yields \(\sigma(p(C_q))=p(\{z:|z|\le q^{-1}\})\). Every point in \(p(\{0<|z|<q^{-1}\})\) is an infinite-multiplicity eigenvalue of \(p(C_q)\), so the closure of these points, namely the full polynomial image of the closed disk, belongs to the Fredholm essential spectrum. That spectrum lies inside the ordinary spectrum, proving equality.

**Step 6: noncircularity witness.** For \(m=1\), \(n=2\), the maximal modulus \(M=a q^{-1}+b q^{-2}\) is attained in \(p(\{z:|z|\le q^{-1}\})\) only if both positive monomial summands are phase-aligned. To obtain the value \(-M\), each summand would have to be negative real. This requires simultaneously \(e^{i\theta}=-1\) and \(e^{2i\theta}=-1\), which is impossible. Compactness of the polynomial image excludes \(-M\), proving strict non-disk geometry in this natural resonant case.

## Verification

The argument uses exact semigroup, norm, duality, and eigenfunction identities documented above. The Fredholm conclusion in the irrational case is proved via a locally vanishing normalized approximate-eigenvector family and does **not** infer Fredholm failure from eigenvalue density alone. The rational case uses infinite-dimensional eigenspaces before invoking spectral mapping. The optional script `checks/spectral_sanity.py` tests finite polynomial phase/algebra identities and boundedness of sampled eigenvalues; its finite checks are **not** a proof of the infinite spectral claims. Independent external verification has not been performed.

## Relationship to prior work

Galanopoulos, Mahillo, Oliva-Maza and Siskakis (2026) prove spectral and Fredholm essential-spectral formulas for BMOA and Bloch Hausdorff operators when the shifted Mellin transform belongs to the extended Dunford–Riesz class \(\mathcal E\). A positive finite sum of genuine interior atoms is not in that class: its Laplace transform has nonzero exponential terms and is unbounded in every sector of opening strictly greater than \(\pi\), unlike an \(\mathcal E\)-function. Their predual identifications and norm estimates are used here as established inputs; their spectral mapping conclusion does not apply to these atomic measures. The present result classifies these excluded measures with two atoms and shows arithmetic dependence and essential-spectrum filling.

Abadias and Oliva-Maza (2024) study generalized Hausdorff spectral sets on Hardy, Bergman, and related spaces. Its full text could not be inspected for an exact overlap comparison; the possibility of an implicit related atomic classification is a publication-priority risk. A previous upper-half-plane Hilbert-space atomic Hausdorff example concerns unitary dilation spectra (annuli or curves), not these one-boundary-point composition semigroups on BMOA or Bloch.

## Limitations

Only two strictly interior atoms with positive real masses, on BMOA and Bloch, are covered. The proof does not classify three or more atoms, signed/complex masses, or weighted spaces with different semigroup growth exponents. The result identifies Fredholm essential sets, not the indices of possible Fredholm resolvents in other models. The spectral identifications use established predual theory, while the arithmetic filling and polynomial classification are derived here. Publication priority remains best-knowledge rather than independently certified.

## References

1. P. Galanopoulos, A. Mahillo, J. Oliva-Maza, A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1 (first public 2026-10-15), https://arxiv.org/html/2610.22554. In particular Introduction, Lemmas 2.3–2.4 and 4.1–4.2, duality arguments in Sections 3–4.
2. L. Abadias and J. Oliva-Maza, *Spectral sets of generalized Hausdorff matrices on spaces of holomorphic functions on the disk*, J. Funct. Anal. 286 (2024), 110298, DOI 10.1016/j.jfa.2023.110298 (full-text inspection not completed).
3. P. S. Bourdon, *Spectra of some composition operators and associated weighted composition operators*, J. Operator Theory 67 (2012), 537–560, https://jot.theta.ro/jot/archive/2012-067-002/2012-067-002-013.html (context for single boundary-contact composition-operator spectral theory).
