# Weak off-diagonal necessity for monomial-curve commutators in every dimension

## Statement

Let
\[
\gamma(t)=
\begin{cases}
(\varepsilon_1 |t|^{\beta_1},\ldots,\varepsilon_n |t|^{\beta_n}),&t>0,\\
(\delta_1 |t|^{\beta_1},\ldots,\delta_n |t|^{\beta_n}),&t\le 0,
\end{cases}
\]
be a monomial curve in \(\mathbb R^n\), where
\(0<\beta_1<\cdots<\beta_n\), \(\varepsilon_i,\delta_i\in\{-1,1\}\), and the two
sign vectors are not identical. Write
\[
|\beta|=\beta_1+\cdots+\beta_n,
\qquad
H_\gamma f(x)=\operatorname{p.v.}\int_{\mathbb R} f(x-\gamma(t))\,\frac{dt}{t},
\]
and \([b,H_\gamma]=bH_\gamma-H_\gamma(b\,\cdot)\).

A \(\gamma\)-cube is a coordinate rectangle
\(Q=I_1\times\cdots\times I_n\) with
\(\ell(I_j)^{1/\beta_j}\) independent of \(j\). Thus
\(|Q|=\ell(Q)^{|\beta|}\), where \(\ell(Q)\) denotes this common anisotropic
sidelength. For \(\alpha\ge0\), set
\[
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}}
=
\sup_Q |Q|^{-\alpha/|\beta|}
\frac1{|Q|}\int_Q |b-b_Q|,
\qquad
b_Q=\frac1{|Q|}\int_Q b.
\]

### Theorem

Let \(1<p\le q<\infty\) and put
\[
\frac{\alpha}{|\beta|}=\frac1p-\frac1q.
\]
If \(b\in L^1_{\mathrm{loc}}(\mathbb R^n;\mathbb C)\) and
\[
[b,H_\gamma]:L^p(\mathbb R^n)\longrightarrow L^{q,\infty}(\mathbb R^n)
\]
is bounded, then
\[
b\in \operatorname{BMO}^{\gamma,\alpha}(\mathbb R^n)
\]
and
\[
\boxed{
\|b\|_{\operatorname{BMO}^{\gamma,\alpha}}
\lesssim_{\gamma,p,q}
\|[b,H_\gamma]\|_{L^p\to L^{q,\infty}}.
}
\]

In particular, weak \((p,p)\) boundedness already forces
\(b\in\operatorname{BMO}^{\gamma}\) in every dimension.

### Corollary in the known strong-boundedness range

Oikari proved that if \((1/p,1/q)\in\Xi(n)\) and
\(\alpha/|\beta|=1/p-1/q\), then
\[
b\in\operatorname{BMO}^{\gamma,\alpha}
\quad\Longrightarrow\quad
[b,H_\gamma]:L^p\to L^q
\]
in every dimension. Combining that result with the theorem above gives, for
\((1/p,1/q)\in\Xi(n)\),
\[
\boxed{
b\in\operatorname{BMO}^{\gamma,\alpha}
\iff
[b,H_\gamma]:L^p\to L^q
\iff
[b,H_\gamma]:L^p\to L^{q,\infty}.
}
\]
Thus the boundedness-necessity part of the higher-dimensional problem raised in
Oikari's Question 1.22 is settled throughout the known sufficiency region. The
necessity theorem itself does not require \((1/p,1/q)\in\Xi(n)\).

## Context

Li and Zeng recently proved the diagonal necessity
\[
\|b\|_{\operatorname{BMO}^{\gamma}}
\lesssim
\|[b,H_\gamma]\|_{L^p\to L^p}
\]
for monomial curves in arbitrary dimension. Their proof introduces a companion
\(\gamma\)-cube and converts mean oscillation on \(Q\) into a finite sum of
averages of commutator outputs.

Earlier, Oikari obtained off-diagonal sufficiency in arbitrary dimension but
restricted the necessity results to the plane. In the same paper, Question 1.22
asks for a higher-dimensional version of the geometric lower-bound mechanism and
the corresponding extension of the necessity results.

The observation here is that the new companion-cube proof has more exponent
flexibility than its diagonal statement suggests. Replacing its final \(L^p\)
estimate by the Banach associate norm of weak \(L^q\) yields the full unweighted
off-diagonal necessity for every \(q\ge p\).

## Proof

Let
\[
T=[b,H_\gamma],\qquad
\mathcal N=\|T\|_{L^p\to L^{q,\infty}},
\qquad
m_Q=\frac1{|Q|}\int_Q |b-b_Q|.
\]

### 1. A norm for weak \(L^q\)

For \(1<q<\infty\), define
\[
\|F\|_{q,\infty}^{\#}
=
\sup_{0<|A|<\infty}
|A|^{-1/q'}\int_A |F|.
\]
This is a norm and
\[
\|F\|_{L^{q,\infty}}
\le
\|F\|_{q,\infty}^{\#}
\le
q'\|F\|_{L^{q,\infty}}.
\]
The second inequality follows from the rearrangement estimate
\(F^*(s)\le \|F\|_{L^{q,\infty}}s^{-1/q}\).
Most importantly,
\[
\left\|\int_\Theta F_\theta\,d\mu(\theta)\right\|_{q,\infty}^{\#}
\le
\int_\Theta \|F_\theta\|_{q,\infty}^{\#}\,d\mu(\theta),
\]
so the Minkowski step in the companion-cube argument remains available although
the usual weak-\(L^q\) quasi-norm is not subadditive.

### 2. The companion-cube estimate

We use the companion-cube construction underlying Li--Zeng's proof. For each
\(\gamma\)-cube \(Q\), it supplies a translate \(P\) of \(Q\), hence
\(|P|=|Q|\), and fixed scale-separated parameter intervals
\[
u_j\asymp c_j\ell(Q),\qquad j=1,\ldots,n,
\]
with constants depending only on \(\gamma\). The change of variables
\[
x=z-\gamma(u_1)-\cdots-\gamma(u_n)
\]
is one-to-one on the relevant parameter box. Li--Zeng prove the construction in
detail in dimension three and state explicitly that the same determinant
argument extends to arbitrary dimension.

The normalization appearing after the Jacobian change of variables has the form
\[
C_Q=
\Big(\prod_{j=1}^n a_j\Big)
\left|\det\big(\gamma'(a_1),\ldots,\gamma'(a_n)\big)\right|,
\qquad
a_j=c_j\ell(Q).
\]
Anisotropic homogeneity gives
\[
\det\big(\gamma'(\ell v_1),\ldots,\gamma'(\ell v_n)\big)
=
\ell^{|\beta|-n}
\det\big(\gamma'(v_1),\ldots,\gamma'(v_n)\big),
\]
and therefore
\[
C_Q\asymp_\gamma \ell(Q)^{|\beta|}=|Q|.
\]
All remaining parameter integrals use \(du_j/u_j\) on fixed-ratio intervals, so
their total masses are bounded independently of \(Q\).

Set
\[
E=\{z\in P: |b(z)-b_Q|\ge m_Q\}.
\]
If \(|E|\ge |P|/2\), the Li--Zeng telescoping and error absorption yield, on
\(E\), a finite sum of terms of the following form:
\[
m_Q
\lesssim_\gamma
\int_\Theta
\big|T(1_{Q+y_\theta})(z-v_\theta)\big|\,d\mu(\theta),
\]
where \(\mu(\Theta)\lesssim_\gamma1\), and \(y_\theta,v_\theta\) are translations
depending on the parameters. This is precisely the scale-free form obtained
after the factor \(C_Q/|Q|\) is canceled.

Taking the \(\|\cdot\|_{q,\infty}^{\#}\) norm on \(E\), using
\(|E|\ge |Q|/2\), Minkowski, translation invariance of Lebesgue measure, and
\(\|1_{Q+y}\|_p=|Q|^{1/p}\), gives
\[
m_Q |Q|^{1/q}
\lesssim_{\gamma,q}
\mathcal N |Q|^{1/p}.
\]
Hence
\[
m_Q\lesssim_{\gamma,p,q}
\mathcal N |Q|^{1/p-1/q}.
\]

If \(|E|<|P|/2\), Li--Zeng use
\[
g(x)=
\left(
\operatorname{sgn}(b(x)-b_Q)
-\big\langle\operatorname{sgn}(b-b_Q)\big\rangle_Q
\right)1_Q(x),
\]
with the complex sign chosen so that
\((b-b_Q)\operatorname{sgn}(b-b_Q)=|b-b_Q|\).
Then \(|g|\le2\,1_Q\), so \(\|g\|_p\le2|Q|^{1/p}\), and on the major subset
\(P\setminus E\) the same telescoping argument, with \(g\) replacing \(1_Q\),
gives the identical weak-\(L^q\) estimate:
\[
m_Q |Q|^{1/q}
\lesssim_{\gamma,p,q}
\mathcal N |Q|^{1/p}.
\]

Thus for every \(\gamma\)-cube \(Q\),
\[
|Q|^{-\alpha/|\beta|}m_Q
\lesssim_{\gamma,p,q}\mathcal N,
\]
because \(\alpha/|\beta|=1/p-1/q\). Taking the supremum over \(Q\) proves the
theorem.

## Checks and boundary cases

- When \(q=p\), \(\alpha=0\), and the conclusion is ordinary
  \(\operatorname{BMO}^{\gamma}\). The hypothesis is weaker than the strong
  \(L^p\) hypothesis in Li--Zeng's theorem.
- In dimension two, the strong \(L^p\)-to-\(L^q\) necessity is consistent with
  Oikari's earlier plane result; the statement above additionally permits a weak
  \(L^q\) target.
- The power \(|Q|^{1/p-1/q}\) is forced by anisotropic scaling, so the
  Campanato exponent is exactly the one in Oikari's
  \(\operatorname{BMO}^{\gamma,\alpha}\) definition.
- Constants have zero seminorm and zero commutator, as required.

## Limitations

The result treats unweighted boundedness only, with \(1<p\le q<\infty\). It does
not claim the higher-dimensional weighted Bloom necessity, compactness
characterizations, the case \(q<p\), or an extension from monomial curves to
general curves with torsion. Outside Oikari's region \(\Xi(n)\), the theorem is
only a necessary condition and does not provide a matching sufficiency result.

The proof uses the higher-dimensional companion-cube geometry asserted in
Li--Zeng's theorem and Remark 2.4. Their paper writes the detailed determinant
and telescoping formulas in dimension three and explains the extension to
arbitrary dimension; the present argument changes the final function-space
estimate rather than that geometry.

## Originality assessment

To the best of our knowledge, the all-dimensional off-diagonal necessity and its
weak-target strengthening have not previously been stated. Li--Zeng's September
2026 paper states the all-dimensional result only on the diagonal
\(L^p\to L^p\). Oikari's 2023 paper gives off-diagonal sufficiency in arbitrary
dimension, explicitly restricts necessity to dimension two, and asks in Question
1.22 for higher-dimensional necessity. Searches for higher-dimensional
off-diagonal or weak-type monomial-curve commutator necessity did not identify a
matching statement.

Because the Li--Zeng preprint is very recent, contemporaneous or not-yet-indexed
observations remain a material originality risk. The contribution claimed here
is the exponent-flexible consequence of their new companion-cube argument, not
the companion geometry itself.

## References

1. K. Li and Y. Zeng, *Curved commutators in higher dimensions*,
   arXiv:2609.18613 (2026). https://arxiv.org/abs/2609.18613
2. T. Oikari, *On the \(L^p\)-to-\(L^q\) boundedness and compactness of
   commutators along monomial curves*, arXiv:2304.00621v2 (2023).
   https://arxiv.org/abs/2304.00621
3. T. Bongers, Z. Guo, J. Li and B. D. Wick, *Commutators of Hilbert transforms
   along monomial curves*, Studia Math. 257 (2021), 295--311.
